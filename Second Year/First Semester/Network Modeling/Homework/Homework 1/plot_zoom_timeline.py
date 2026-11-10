"""Plot the selected Zoom uplink; times refer to first selected packet."""
import csv
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/zoom-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

with open("zoom_uplink.csv", newline="") as source:
    rows = list(csv.DictReader(source))
t = np.array([float(row["time_s"]) for row in rows])
sizes = np.array([int(row["frame.len"]) for row in rows])
edges = np.arange(0, np.ceil(t[-1]) + 1, 1)
byte_counts, _ = np.histogram(t, bins=edges, weights=sizes)
counts, _ = np.histogram(t, bins=edges)
widths = np.minimum(edges[1:], t[-1]) - edges[:-1]
fig, axes = plt.subplots(3, 1, figsize=(12, 8), sharex=True)
axes[0].stairs(8 * byte_counts / widths / 1000, edges)
axes[0].set_ylabel("Uplink (kbit/s)")
axes[0].set_title("Selected UDP stream 0 uplink: phase boundaries not yet established")
axes[1].stairs(counts / widths, edges)
axes[1].set_ylabel("Packets/s")
axes[2].scatter(t, sizes, s=1, alpha=0.25, rasterized=True)
axes[2].set_ylabel("Frame length (bytes)")
axes[2].set_xlabel("Seconds since first selected packet (not stopwatch start)")
for ax in axes:
    ax.grid(alpha=0.25)
    ax.set_xlim(0, t[-1])
fig.tight_layout()
fig.savefig("zoom_uplink_timeline.png", dpi=160)
plt.close(fig)
for start in range(0, int(t[-1]), 30):
    end = min(start + 30, t[-1])
    selected = (t >= start) & (t < end)
    print(f"{start:3d}-{end:6.1f} s: {8*sizes[selected].sum()/(end-start)/1000:7.1f} kbit/s; {selected.sum():5d} packets")
