"""
shaper.py --

Runs a trace through the Token Bucket Filter and the Leaky Bucket Filter.

    input trace --> [ input buffer Bi -> TBF (r, b) ] --> [ output buffer Bo -> LBF (mu) ] --> output trace

The simulation is event-driven (discrete-event): the logical clock does not tick every
millisecond, it jumps from one instant to the next. Three kinds of events:
  1) ARRIVAL     : a packet arrives at the shaper          (read from the input trace)
  2) TBF_RELEASE : the packet at the head of the TBF queue now has enough tokens
  3) LBF_DONE    : the LBF finished transmitting a packet  (this is what goes to the output trace)

Parameters:
  r   : token generation rate (tokens/s, 1 token = 1 byte)
  b   : token bucket capacity (tokens)
  Bi  : TBF input buffer (bytes)
  mu  : LBF forwarding rate (bytes/s)
  Bo  : LBF output buffer (bytes)

Usage:
  python shaper.py --r 45800 --b 120000 --Bi 10000 --mu 1830000 --Bo 120000

"""
import argparse
import heapq
from collections import deque

from source import read_trace

ARRIVAL_EPS = 1e-9   # floating point tolerance when comparing tokens with a packet length
# Event kinds. They are also the tie-breaker in the heap (smaller number first): when two events
# happen at the same instant, LBF_DONE is handled before TBF_RELEASE, because it frees buffer space.
LBF_DONE, TBF_RELEASE = 0, 1

# ----------------------------------------------------------------------
# Run the trace through TBF -> LBF.
# ----------------------------------------------------------------------
def shape(ids, times, lengths, r, b, Bi, mu, Bo, init_tokens=None):

    if init_tokens is None:
        init_tokens = b                 # by default the bucket starts full

    # --- state variables ---
    tokens = float(min(init_tokens, b))  # current number of tokens in the bucket
    t_last = 0.0                    # instant at which `tokens` was last updated
    in_q = deque()                  # TBF input queue (FIFO): items are (id, L)
    in_bytes = 0                    # total bytes currently in the input queue
    release_pending = False         # is a TBF_RELEASE event that cheks already scheduled

    out_q = deque()                 # LBF queue (FIFO): items are (id, L); the head is being transmitted
    out_bytes = 0                   # bytes in the LBF (waiting + the one in transmission)
    lbf_busy = False                # is the LBF transmitting right now

    events = []                     # heap of future internal events: (time, kind, seq, data)
    seq = 0                         # unique counter that breaks ties so tuples never compare `data`

    out_ids, out_times, out_lens = [], [], []     # output trace, filled as packets finish
    st = {"n_in": 0, "drop_oversize": 0, "drop_in": 0, "drop_out": 0,
          "max_in_bytes": 0, "max_out_bytes": 0}  # statistics

    # --- helper routines ---
    def refill(t):
        """Lazy token update: add the tokens generated since the last update, capped at b."""
        nonlocal tokens, t_last
        tokens = min(b, tokens + r * (t - t_last))
        t_last = t

    def lbf_enter(t, pid, L):
        """A packet left the TBF and enters the LBF at time t."""
        nonlocal out_bytes, lbf_busy, seq
        if out_bytes + L > Bo:                   # output buffer cannot hold it so drop
            st["drop_out"] += 1
            return
        out_bytes += L
        st["max_out_bytes"] = max(st["max_out_bytes"], out_bytes)
        out_q.append((pid, L))
        if not lbf_busy:                         # LBF idle: start transmitting immediately
            lbf_busy = True
            seq += 1
            heapq.heappush(events, (t + L / mu, LBF_DONE, seq, None))   # transmission time = L/mu

    def serve_tbf(t):
        """Release from the queue every head packet that has enough tokens; if the next one
        does not, schedule the instant at which it will."""
        nonlocal tokens, in_bytes, release_pending, seq
        refill(t)
        while in_q and tokens >= in_q[0][1] - ARRIVAL_EPS:   # enough tokens for the head packet
            pid, L = in_q.popleft()
            in_bytes -= L
            tokens = max(0.0, tokens - L)        # pay L tokens (max() removes float noise)
            lbf_enter(t, pid, L)
        if in_q and not release_pending:
            need = in_q[0][1] - tokens           # missing tokens
            release_pending = True
            seq += 1
            # tokens grow at rate r, so the missing amount takes need/r seconds to accumulate
            heapq.heappush(events, (t + need / r, TBF_RELEASE, seq, None))

    def handle_internal(t, kind):
        nonlocal release_pending, out_bytes, lbf_busy, seq, tokens
        if kind == TBF_RELEASE:
            release_pending = False
            refill(t)
            # Float rounding can leave tokens barely below L; force it, or the release would loop forever.
            if in_q and tokens < in_q[0][1]:
                tokens = float(in_q[0][1])
            serve_tbf(t)
        else:  # LBF_DONE: the transmission of the head packet of out_q has finished
            pid, L = out_q.popleft()
            out_bytes -= L                       # the space is freed only when transmission ends
            out_ids.append(pid); out_times.append(t); out_lens.append(L)   # write to the output trace
            if out_q:                            # start the next packet, if any
                seq += 1
                heapq.heappush(events, (t + out_q[0][1] / mu, LBF_DONE, seq, None))
            else:
                lbf_busy = False

    def handle_arrival(t, pid, L):
        nonlocal in_bytes, tokens
        st["n_in"] += 1
        if L > b:                                # larger than the whole bucket: can never pass
            st["drop_oversize"] += 1
            return
        refill(t)
        # Fast path: queue empty AND enough tokens -> the packet passes at once, without buffering.
        # (`not in_q` is required to keep the FIFO order.)
        if not in_q and tokens >= L - ARRIVAL_EPS:
            tokens = max(0.0, tokens - L)
            lbf_enter(t, pid, L)
            return
        if in_bytes + L > Bi:                    # input buffer full, drop
            st["drop_in"] += 1
            return
        in_q.append((pid, L))                    # otherwise wait in the input queue
        in_bytes += L
        st["max_in_bytes"] = max(st["max_in_bytes"], in_bytes)
        serve_tbf(t)                             # schedules a TBF_RELEASE if none is pending

    # --- main loop: next event = earliest between next arrival and top of the event heap ---
    ids_l, times_l, lens_l = ids.tolist(), times.tolist(), lengths.tolist()
    n, i = len(ids_l), 0
    while i < n or events:
        if events and (i >= n or events[0][0] <= times_l[i]):   # on ties the internal event goes first
            t, kind, _, _ = heapq.heappop(events)
            handle_internal(t, kind)
        else:
            handle_arrival(times_l[i], ids_l[i], lens_l[i])
            i += 1

    return out_ids, out_times, out_lens, st


def write_output(path, out_ids, out_times, out_lens):
    with open(path, "w") as f:
        for i, t, L in zip(out_ids, out_times, out_lens):
            f.write(f"{i} {t:.6f} {L}\n")


# ----------------------------------------------------------------------
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--r", type=float, required=True, help="token rate (tokens/s)")
    ap.add_argument("--b", type=float, required=True, help="bucket capacity (tokens)")
    ap.add_argument("--Bi", type=float, required=True, help="input buffer (bytes)")
    ap.add_argument("--mu", type=float, required=True, help="LBF rate (bytes/s)")
    ap.add_argument("--Bo", type=float, required=True, help="output buffer (bytes)")
    ap.add_argument("--inp", default="Input_Traffic_Trace.txt")
    ap.add_argument("--out", default="Output_Traffic_Trace.txt")
    a = ap.parse_args()

    ids, times, lens = read_trace(a.inp)
    o_ids, o_t, o_L, st = shape(ids, times, lens, a.r, a.b, a.Bi, a.mu, a.Bo)
    write_output(a.out, o_ids, o_t, o_L)
    n_drop = st["drop_oversize"] + st["drop_in"] + st["drop_out"]
    print(f"in={st['n_in']}  out={len(o_ids)}  dropped={n_drop} "
          f"(oversize={st['drop_oversize']}, input buffer={st['drop_in']}, "
          f"output buffer={st['drop_out']})  loss rate={n_drop / st['n_in']:.4%}")
