"""
source.py -- 

Generates a synthetic packet flow using the traffic model built in HW1 and writes it
to a trace file (Input_Traffic_Trace.txt).

Model (HW1), the traffic is a "batch arrival" process:
  A : time between consecutive batches   -> mixture of Normal(~20 ms) and LogNormal
  B : batch size (packets per batch)     -> short Geometric (<= 5) mixture with LogNormal (big bursts)
  W : packet size (bytes)                -> two-component LogNormal mixture

Usage:
  python source.py --fit                      # fit parameters from the CSV and write params.json
  python source.py --duration 3600 --seed 1   # generate a 3600 s trace

"""
import numpy as np
import pandas as pd
import scipy.stats as st

import argparse
import json
import os

PARAMS_FILE = "params.json"        # cache of the fitted model parameters

# --- Settings taken from HW1---
THR = 0.001                        # batch threshold: gap <= 1 ms means "same batch"
VOICE_LO, VOICE_HI = 0.015, 0.025  # window of the "voice period" for A (~20 ms)
B_SMALL_MAX = 5                    # boundary between small and big batches for B
W_SPLIT = 400                      # boundary between voice/control (<400 B) and video (>=400 B) for W


# ----------------------------------------------------------------------
# extracts the model parameters from the real trace
# ----------------------------------------------------------------------
def fit_params(csv_file):
    try:
        df = pd.read_csv(csv_file, encoding="latin1")
    except Exception:
        df = pd.read_csv(csv_file, encoding="utf-16")
    df.columns = df.columns.str.strip()
    df = df[["Time", "Length"]].astype(float).sort_values("Time").reset_index(drop=True)

    t = df["Time"].values - df["Time"].values[0]  # time relative to the first packet
    W = df["Length"].values                       # packet sizes in bytes

    # a packet starts a new batch if it arrives more than THR after the previous one.
    new_batch = np.r_[True, np.diff(t) > THR]     # True at the first packet of every batch
    batch_id = np.cumsum(new_batch) - 1           # batch index of every packet
    B = np.bincount(batch_id)                     # number of packets in each batch
    A = np.diff(t[new_batch])                     # time between the starts of consecutive batches

    p = {"THR": THR}                              # dictionary that will be saved as JSON

    # --- A model: periodic voice (normal, ~20 ms) + random delays/bursts (lognormal) ---
    mask_voice = (A > VOICE_LO) & (A < VOICE_HI)  # which gaps look like the 20 ms voice period
    p["p_voice"] = float(mask_voice.mean())       # fraction of gaps that are "voice"
    p["mu_v"] = float(A[mask_voice].mean())       # mean of the voice period
    p["sd_v"] = float(A[mask_voice].std())        # std of the voice period
    p["A_max"] = float(A.max())                   # largest observed gap (used for clipping)
    # all the other gaps are modeled with a lognormal; floc=0 forces the location parameter to 0
    p["par_A_rest"] = [float(x) for x in st.lognorm.fit(A[~mask_voice], floc=0)]

    # --- B model: small batches (shifted geometric) + heavy tail (lognormal) ---
    B_small, B_big = B[B <= B_SMALL_MAX], B[B > B_SMALL_MAX]
    p["p_big"] = float(len(B_big) / len(B))       # probability that a batch is a big burst
    p["p_geo"] = float(1.0 / B_small.mean())      # geometric parameter (mean = 1/p, minimum value 1)
    p["par_B_big"] = [float(x) for x in st.lognorm.fit(B_big, floc=0)]
    p["B_max"] = int(B.max())                     # largest observed batch (used for clipping)

    # --- W model: two-component lognormal mixture (voice/control + video) ---
    W_lo, W_hi = W[W < W_SPLIT], W[W >= W_SPLIT]
    p["p_lo"] = float(len(W_lo) / len(W))         # probability of the small packet component
    p["par_W_lo"] = [float(x) for x in st.lognorm.fit(W_lo, floc=0)]
    p["par_W_hi"] = [float(x) for x in st.lognorm.fit(W_hi, floc=0)]
    p["W_min"], p["W_max"] = float(W.min()), float(W.max())   # observed size limits (clipping)

    with open(PARAMS_FILE, "w") as f:
        json.dump(p, f, indent=2)
    print(f"Parameters written to {PARAMS_FILE}.")
    return p


# ----------------------------------------------------------------------
# draws random samples from the fitted model
# ----------------------------------------------------------------------
def gen_A(p, n, rng):
    """n inter-batch times (seconds)."""
    # Voice component: normal around 20 ms, clipped to the voice window.
    voice = np.clip(rng.normal(p["mu_v"], p["sd_v"], n), VOICE_LO, VOICE_HI)
    # Non-voice component: lognormal.
    rest = st.lognorm.rvs(*p["par_A_rest"], size=n, random_state=rng)
    # For each sample pick "voice" with probability p_voice, otherwise "rest".
    out = np.where(rng.random(n) < p["p_voice"], voice, rest)
    # Never go below THR (otherwise two batches would merge) or above the observed maximum.
    return np.clip(out, p["THR"], p["A_max"])


def gen_B(p, n, rng):
    """n batch sizes (packets per batch, integers >= 1)."""
    # Small batches: geometric distribution, truncated at B_SMALL_MAX.
    small = np.minimum(rng.geometric(p["p_geo"], n), B_SMALL_MAX)
    # Big batches: lognormal, rounded to integers and kept inside [B_SMALL_MAX+1, B_max].
    big = np.round(st.lognorm.rvs(*p["par_B_big"], size=n, random_state=rng))
    big = np.clip(big, B_SMALL_MAX + 1, p["B_max"])
    # Choose "big" with probability p_big, otherwise "small".
    return np.where(rng.random(n) < p["p_big"], big, small).astype(int)


def gen_W(p, n, rng):
    """n packet sizes in bytes."""
    lo = st.lognorm.rvs(*p["par_W_lo"], size=n, random_state=rng)   # small packet cluster
    hi = st.lognorm.rvs(*p["par_W_hi"], size=n, random_state=rng)   # large packet cluster
    out = np.where(rng.random(n) < p["p_lo"], lo, hi)               # mixture
    # Packet sizes are integers inside the observed range (max is 1514 B, the Ethernet limit).
    return np.clip(np.round(out), p["W_min"], p["W_max"]).astype(int)


# ----------------------------------------------------------------------
# places the batches on the time axis and assign packet IDs
# ----------------------------------------------------------------------
def generate_trace(p, duration, seed):
    rng = np.random.default_rng(seed)            # own generator: same seed -> same trace

    # We do not know in advance how many batches fit in `duration`, so we generate them in
    # chunks (estimated from the ~20 ms mean gap, +20% margin) and add chunks until we pass `duration`.
    times = []
    t_now = 0.0
    chunk = int(duration / 0.02 * 1.2) + 100
    while t_now <= duration:
        a = gen_A(p, chunk, rng)                 # inter-batch gaps
        bt = t_now + np.cumsum(a)                # absolute batch times = running sum of the gaps
        times.append(bt)
        t_now = bt[-1]                           # next chunk continues from the last batch
    batch_times = np.concatenate(times)
    batch_times = batch_times[batch_times <= duration]   # drop batches after the end of the experiment

    sizes = gen_B(p, len(batch_times), rng)      # number of packets in each batch
    pkt_times = np.repeat(batch_times, sizes)    # same batch -> same timestamp for all its packets
    lengths = gen_W(p, len(pkt_times), rng)      # size of every single packet
    ids = np.arange(len(pkt_times))              # unique ID: 0, 1, 2, ...
    return ids, pkt_times, lengths


def write_trace(path, ids, times, lengths):
    with open(path, "w") as f:
        for i, t, L in zip(ids, times, lengths):
            f.write(f"{i} {t:.6f} {L}\n")


def read_trace(path):
    data = np.loadtxt(path)
    data = np.atleast_2d(data)
    return data[:, 0].astype(int), data[:, 1], data[:, 2].astype(int)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fit", action="store_true", help="fit the parameters from the CSV")
    ap.add_argument("--csv", default="teams_traffic.csv")
    ap.add_argument("--duration", type=float, default=3600.0, help="simulated time (s)")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", default="Input_Traffic_Trace.txt")
    args = ap.parse_args()

    if args.fit or not os.path.exists(PARAMS_FILE):
        params = fit_params(args.csv)
    else:
        with open(PARAMS_FILE) as f:
            params = json.load(f)

    if not args.fit:
        ids, times, lengths = generate_trace(params, args.duration, args.seed)
        write_trace(args.out, ids, times, lengths)
        print(f"{len(ids)} packets, {args.duration:.0f} s -> {args.out}")
        print(f"mean rate = {lengths.sum() / args.duration / 1000:.2f} kB/s, "
              f"mean packet size = {lengths.mean():.1f} B, max = {lengths.max()} B")
