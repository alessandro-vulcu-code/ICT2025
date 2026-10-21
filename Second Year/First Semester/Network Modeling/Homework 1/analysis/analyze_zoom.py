"""Reproduce the Zoom report from the raw capture (Python + NumPy/SciPy/Matplotlib).

Run from the homework directory with the sklearn-env Python interpreter.
All times are measured from the first packet matching FILTER, not the stopwatch.
"""
from pathlib import Path
import csv
from decimal import Decimal
import io
import json
import os
import subprocess

os.environ.setdefault("MPLCONFIGDIR", "/tmp/zoom-report-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from scipy.stats import ks_2samp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis"
FIG = ROOT / "Latex template" / "figure"
FILTER = "udp.stream == 0 && ip.src == 192.168.3.7 && frame.number > 32864"
SEED = 2026
DELTA = 0.001
TRAIN_DURATION = 180.0
TEST_DURATION = 120.0


def extract():
    fields = ["frame.number", "frame.time_epoch", "frame.time_relative", "frame.len",
              "frame.cap_len", "ip.src", "ip.dst", "udp.stream", "udp.srcport", "udp.dstport"]
    cmd = ["tshark", "-n", "-r", str(ROOT / "zoom.pcapng"), "-Y", FILTER,
           "-T", "fields", "-E", "header=y", "-E", "separator=,", "-E", "quote=d"]
    for field in fields:
        cmd.extend(["-e", field])
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    rows = list(csv.DictReader(io.StringIO(result.stdout)))
    rows.sort(key=lambda r: (Decimal(r["frame.time_epoch"]), int(r["frame.number"])))
    origin = Decimal(rows[0]["frame.time_epoch"])
    times = np.array([float(Decimal(r["frame.time_epoch"]) - origin) for r in rows])
    sizes = np.array([int(r["frame.len"]) for r in rows])
    assert all(r["ip.dst"] == "206.247.58.75" and r["udp.srcport"] == "42613"
               and r["udp.dstport"] == "8801" for r in rows)
    assert all(int(r["frame.cap_len"]) == int(r["frame.len"]) for r in rows)
    return times, sizes, rows


def clusters(t, size, threshold=DELTA):
    starts = np.r_[0, np.flatnonzero(np.diff(t) > threshold) + 1]
    ends = np.r_[starts[1:], len(t)]
    return starts, ends


def fit_cycles(t, sizes, threshold=DELTA):
    starts, ends = clusters(t, sizes, threshold)
    # Omit both boundary clusters; a cycle ends at the next cluster start.
    cycles = []
    for i in range(1, len(starts) - 1):
        lo, hi = starts[i], ends[i]
        duration = t[starts[i + 1]] - t[lo]
        offsets = t[lo:hi] - t[lo]
        assert offsets[-1] < duration
        cycles.append((duration, offsets, sizes[lo:hi]))
    return cycles


def simulate_batch(cycles, duration, seed):
    rng = np.random.default_rng(seed)
    times, sizes = [], []
    tau = 0.0
    while tau < duration:
        interval, offsets, weights = cycles[rng.integers(len(cycles))]
        keep = tau + offsets < duration
        times.extend((tau + offsets[keep]).tolist())
        sizes.extend(weights[keep].tolist())
        tau += interval
    return np.array(times), np.array(sizes)


def simulate_poisson(train_t, train_l, duration, seed):
    rng = np.random.default_rng(seed)
    gap_mean = np.diff(train_t).mean()
    t, tau = [], 0.0
    while True:
        tau += rng.exponential(gap_mean)
        if tau >= duration:
            break
        t.append(tau)
    return np.array(t), rng.choice(train_l, size=len(t))


def binned(t, l, duration, width):
    edges = np.linspace(0, duration, int(round(duration / width)) + 1)
    count = np.histogram(t, bins=edges)[0]
    rate = 8 * np.histogram(t, bins=edges, weights=l)[0] / width / 1000
    return edges, count, rate


def metrics(t, l, duration):
    a = np.diff(t)
    result = dict(packets=len(t), duration_s=duration, mean_frame_B=float(l.mean()),
                  median_frame_B=float(np.median(l)), min_frame_B=int(l.min()),
                  max_frame_B=int(l.max()), mean_gap_ms=float(a.mean()*1000),
                  median_gap_us=float(np.median(a)*1e6), gap_cv=float(a.std(ddof=1)/a.mean()),
                  bitrate_kbps=float(8*l.sum()/duration/1000),
                  gap_below_1ms_fraction=float(np.mean(a <= DELTA)))
    for width in [.02, .1, 1.0]:
        _, count, rate = binned(t, l, duration, width)
        result[f"fano_{width:g}s"] = float(count.var(ddof=1)/count.mean())
        result[f"rate_peak_mean_{width:g}s"] = float(rate.max()/rate.mean())
        result[f"count_lag1_{width:g}s"] = float(np.corrcoef(count[:-1], count[1:])[0, 1])
    return result


def save_trace(name, t, l):
    with open(OUT / name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time_s", "frame_length_B"])
        writer.writerows(zip(t, l))


def cdf(ax, values, label, color, style="-", log=False):
    x = np.sort(values)
    ax.plot(x, np.arange(1, len(x)+1)/len(x), label=label, color=color,
            ls=style, lw=1.1)
    if log:
        ax.set_xscale("log")
    ax.set_ylim(0, 1.02)
    ax.set_ylabel("CDF")


def plots(t, l, train, observed, baseline, synthetic):
    plt.rcParams.update({"font.size": 8, "axes.titlesize": 8.5, "axes.labelsize": 8,
                         "xtick.labelsize": 7, "ytick.labelsize": 7,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "pdf.fonttype": 42})
    blue, red, grey = "#1764a0", "#c84936", "#777777"
    fig, ax = plt.subplots(figsize=(7.1, 1.30))
    edges = np.arange(0, np.ceil(t[-1])+1)
    ax.stairs(np.histogram(t, edges, weights=l)[0]*8/1000, edges, color=blue, lw=.8)
    ax.axvspan(270, 450, color="#4b9d66", alpha=.13, label="Training (180 s)")
    ax.axvspan(450, 570, color="#e0a331", alpha=.18, label="Validation (120 s)")
    ax.set(xlabel="Time since first filtered packet (s)", ylabel="Uplink (kbit/s)", xlim=(0,t[-1]))
    ax.legend(fontsize=7, loc="upper left", frameon=False)
    ax.grid(alpha=.2)
    fig.tight_layout(pad=.5)
    fig.savefig(FIG / "zoom_phase_timeline.pdf")
    plt.close(fig)

    ot, ol = observed
    pt, pl = baseline
    st, sl = synthetic
    fig = plt.figure(figsize=(7.1, 3.65), layout="constrained")
    grid = fig.add_gridspec(2, 3)
    panels = [fig.add_subplot(grid[0, i]) for i in range(3)]
    for tt, ll, label, color, style in [(ot,ol,"Observed",blue,"-"),
                                      (pt,pl,"Poisson baseline",grey,":"),
                                      (st,sl,"Batch model",red,"--")]:
        cdf(panels[0], np.diff(tt)*1000, label, color, style, log=True)
        cdf(panels[1], ll, label, color, style)
        starts, ends = clusters(tt, ll)
        cdf(panels[2], ends-starts, label, color, style)
    panels[0].set(title="(a) Packet inter-arrival CDF",
                  xlabel="Inter-arrival time (ms, log scale)")
    panels[1].set(title="(b) Packet-size CDF", xlabel="Frame length (B)")
    panels[2].set(title="(c) Cluster-size CDF", xlabel="Packets / cluster")

    ax = fig.add_subplot(grid[1, 0])
    for tt, color in [(ot, blue), (st, red)]:
        use = tt[1:] < 1
        ax.scatter(tt[1:][use], np.diff(tt)[use]*1000, s=5, alpha=.75, color=color)
    ax.set(yscale="log", title="(d) Packet inter-arrival times\nFirst second",
           ylabel="Inter-arrival time (ms)", xlabel="Time (s)")

    for j, (width, duration) in enumerate([(.1, 10), (1, TEST_DURATION)], start=1):
        ax = fig.add_subplot(grid[1, j])
        # Use the same bin origin and duration for both independent traces.
        for tt, ll, color, style in [(ot,ol,blue,"-"),(st,sl,red,"--")]:
            use = tt < duration
            edges, _, rate = binned(tt[use], ll[use], duration, width)
            ax.stairs(rate, edges, color=color, lw=.7, ls=style)
        ax.set(title=f"({chr(100+j)}) Rate: {width*1000:g} ms bins\n"
                     f"{'Full validation window' if duration == TEST_DURATION else 'First ten seconds'}",
               xlabel="Time (s)", ylabel="kbit/s", xlim=(0,duration))
    for ax in fig.axes:
        ax.grid(alpha=.2)
    fig.legend(handles=[Line2D([],[],color=blue,label="Observed validation"),
                        Line2D([],[],color=red,ls="--",label="Batch model, seed 2026"),
                        Line2D([],[],color=grey,ls=":",label="Poisson baseline")],
               loc="outside lower center", ncol=3, frameon=False, fontsize=7)
    fig.savefig(FIG / "zoom_model_comparison.pdf")
    fig.savefig(OUT / "zoom_model_comparison.png", dpi=180)
    plt.close(fig)

    # Optional packet-size scatterplot, omitted from the report: its first-second
    # snapshot adds little to the full-trace size CDF. Uncomment to export it.
    # fig, ax = plt.subplots(figsize=(7.1, 2.0), layout="constrained")
    # for tt, ll, label, color in [(ot, ol, "Observed", blue),
    #                              (st, sl, "Batch model", red)]:
    #     use = tt < 1
    #     ax.scatter(tt[use], ll[use], s=5, alpha=.75, color=color, label=label)
    # ax.set(title="Packet sizes: first second", ylabel="Frame length (B)",
    #        xlabel="Time (s)")
    # ax.legend(frameon=False)
    # fig.savefig(FIG / "zoom_packet_size_scatter.pdf")
    # plt.close(fig)

    # Optional 20 ms rate plot, omitted from the report: overlapping spikes make
    # comparison harder than at 100 ms and 1 s. Uncomment to export it.
    # fig, ax = plt.subplots(figsize=(7.1, 2.0), layout="constrained")
    # for tt, ll, label, color, style in [(ot, ol, "Observed", blue, "-"),
    #                                    (st, sl, "Batch model", red, "--")]:
    #     use = tt < 10
    #     edges, _, rate = binned(tt[use], ll[use], 10, .02)
    #     ax.stairs(rate, edges, color=color, lw=.7, ls=style, label=label)
    # ax.set(title="Rate: 20 ms bins", xlabel="Time (s)", ylabel="kbit/s", xlim=(0, 10))
    # ax.legend(frameon=False)
    # fig.savefig(FIG / "zoom_rate_20ms.pdf")
    # plt.close(fig)


def main():
    OUT.mkdir(exist_ok=True)
    FIG.mkdir(exist_ok=True)
    t, l, rows = extract()
    video = (t >= 270) & (t < 570)
    vt, vl = t[video]-270, l[video]
    training = vt < TRAIN_DURATION
    tt, tl = vt[training], vl[training]
    ot, ol = vt[~training]-TRAIN_DURATION, vl[~training]
    cycles = fit_cycles(tt, tl)
    st, sl = simulate_batch(cycles, TEST_DURATION, SEED)
    pt, pl = simulate_poisson(tt, tl, TEST_DURATION, SEED)
    complete_mean_D = float(np.mean([c[0] for c in cycles]))
    complete_mean_B = float(np.mean([len(c[1]) for c in cycles]))
    predicted_rate = float(np.mean([8*c[2].sum() for c in cycles])/complete_mean_D/1000)
    stats = {"filter": FILTER, "time_origin_epoch": rows[0]["frame.time_epoch"],
             "time_origin_capture_relative_s": rows[0]["frame.time_relative"],
             "phase_selection_s": [270,570], "training_selection_s": [270,450],
             "validation_selection_s": [450,570], "threshold_s": DELTA, "seed": SEED,
             "video": metrics(vt,vl,300), "training": metrics(tt,tl,TRAIN_DURATION),
             "observed_validation": metrics(ot,ol,TEST_DURATION),
             "poisson": metrics(pt,pl,TEST_DURATION), "batch": metrics(st,sl,TEST_DURATION),
             "cycle_fit": {"complete_cycles":len(cycles),"mean_D_ms":complete_mean_D*1000,
                           "mean_B":complete_mean_B,"predicted_kbps":predicted_rate,
                           "poisson_lambda_pps":1/np.diff(tt).mean()},
             "sensitivity": [], "repeat_seeds": {}}
    for d in [.0005,.001,.003]:
        fitted=fit_cycles(tt,tl,d)
        stats["sensitivity"].append({"threshold_ms":d*1000,"cycles":len(fitted),
            "mean_B":float(np.mean([len(c[1]) for c in fitted])),
            "mean_D_ms":float(np.mean([c[0] for c in fitted])*1000)})
    for name, times, size in [("batch",st,sl),("poisson",pt,pl)]:
        stats[name]["gap_KS_vs_validation"]=float(ks_2samp(np.diff(ot),np.diff(times)).statistic)
        stats[name]["size_KS_vs_validation"]=float(ks_2samp(ol,size).statistic)
    for model in ["batch","poisson"]:
        runs=[]
        for seed in range(SEED,SEED+30):
            a,b=(simulate_batch(cycles,TEST_DURATION,seed) if model=="batch" else
                 simulate_poisson(tt,tl,TEST_DURATION,seed))
            runs.append(metrics(a,b,TEST_DURATION))
        stats["repeat_seeds"][model]={key:{"mean":float(np.mean([r[key] for r in runs])),
             "p05":float(np.quantile([r[key] for r in runs],.05)),
             "p95":float(np.quantile([r[key] for r in runs],.95))}
             for key in ["bitrate_kbps","packets","fano_0.1s","count_lag1_1s"]}
    for name, a,b in [("zoom_video_300s.csv",vt,vl),("zoom_training_180s.csv",tt,tl),
                      ("zoom_validation_120s.csv",ot,ol),("zoom_synthetic_batch_120s.csv",st,sl),
                      ("zoom_synthetic_poisson_120s.csv",pt,pl)]:
        save_trace(name,a,b)
    (OUT/"zoom_report_statistics.json").write_text(json.dumps(stats,indent=2)+"\n")
    plots(t,l,(tt,tl),(ot,ol),(pt,pl),(st,sl))
    print(json.dumps(stats,indent=2))


if __name__=="__main__":
    main()
