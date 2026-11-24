"""Redraw the alarm examples on pp. 5–7 of Lesson 15.pdf."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


OUT = Path(__file__).resolve().parent
RED, BLUE, GREEN, PURPLE = "#ad2029", "#1661a8", "#387d2f", "#853394"

plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})


def axes(xlabel, ylabel, figsize=(5.1, 2.9)):
    fig, ax = plt.subplots(figsize=figsize, layout="constrained")
    ax.set(xlabel=xlabel, ylabel=ylabel)
    return fig, ax


def save(fig, name):
    fig.savefig(OUT / f"lesson15-{name}.png", dpi=180)
    plt.close(fig)


fig, ax = axes(r"$r_i$", r"$U_i(r_i)$")
ax.set(xlim=(0, 2.2), ylim=(-0.15, 1.2), yticks=[0, 1])
ax.set_xticks([0, 1], ["0", r"$w_i=L/\delta_i$"])
ax.plot([0, 1], [0, 0], color=RED, linewidth=2.5)
ax.plot([1, 2.17], [1, 1], color=RED, linewidth=2.5)
ax.vlines(1, 0, 1, color="0.75", linestyle=":")
ax.scatter([1, 1], [0, 1], facecolors=["white", RED], edgecolors=RED, zorder=4)
save(fig, "p5-alarm-step")

fig, ax = axes(r"$r_i$", r"$U_i(r_i)$")
ax.set(xlim=(0, 2.05), ylim=(-1.15, 0.2), yticks=[-1, 0])
ax.set_xticks([0, 1], ["0", r"$w_i$"])
ax.axhline(0, color="0.8", linewidth=1)
ax.plot([0, 1, 2], [-1, 0, 0], color=BLUE, linewidth=2.5)
save(fig, "p6-alarm-penalty")

fig, ax = axes(r"$r_1$ [Mbit/s]", r"$r_2$ [Mbit/s]")
ax.set(xlim=(0, 1.63), ylim=(0, 1.63), aspect="equal", yticks=[0, 1.5], xticks=[0, 1.5])
ax.fill([0, 1.5, 0], [0, 0, 1.5], facecolor="#f9e3e4")
ax.plot([0, 1.5], [1.5, 0], color=RED, linewidth=2.4)
ax.text(0.18, 0.32, r"$\mathcal{R}$", color=RED)
ax.text(0.79, 0.94, r"$r_2=C-r_1$", color=RED)
save(fig, "p7-capacity-boundary")

fig, ax = axes(r"$r_1$ [Mbit/s]", "Utility", (6.7, 3.7))
c, w1, w2 = 1.5, 1, 2 / 3
rates = [0, c - w2, w1, c]
u1 = [min(0, r1 / w1 - 1) for r1 in rates]
weighted_u2 = [3 * min(0, (c - r1) / w2 - 1) for r1 in rates]
total = [first + second for first, second in zip(u1, weighted_u2)]
ax.set(xlim=(0, 1.54), ylim=(-3.15, 0.43), yticks=[-3, -1, 0])
ax.set_xticks(rates, ["0", r"$5/6$", r"$w_1=1$", r"$C=1.5$"])
ax.axhline(0, color="0.83", linewidth=1)
ax.plot(rates, u1, label=r"$U_1(r_1)$", color=RED, linewidth=2.6)
ax.plot(rates, weighted_u2, label=r"$3U_2(C-r_1)$", color=GREEN, linewidth=2.6)
ax.plot(rates, total, label="Weighted sum", color=PURPLE, linestyle="--", linewidth=2.1)
ax.vlines(c - w2, -3.15, total[1], color="0.64", linestyle=":")
ax.scatter(c - w2, total[1], facecolor="white", edgecolor=PURPLE, linewidth=2, zorder=5)
ax.annotate(r"Maximum $-1/6$", xy=(c - w2, total[1]), xytext=(0.31, -1.29),
            color=PURPLE, arrowprops={"arrowstyle": "->", "color": PURPLE})
ax.legend(loc="lower left", frameon=False, fontsize=10)
save(fig, "p7-weighted-utilities")

fig, ax = axes(r"$r_i$", r"$U_i(r_i)$")
ax.set(xlim=(0, 3.2), ylim=(-0.15, 1.2), yticks=[0, 1])
ax.set_xticks([0, 1, 2], ["0", r"$w_i=L/\delta_i$", r"$w_i^*=2w_i$"])
ax.vlines([1, 2], -0.15, [0, 1], color="0.78", linestyle=":")
ax.hlines(1, 0, 2, color="0.78", linestyle=":")
ax.plot([0, 1, 2, 3.17], [0, 0, 1, 1], color=GREEN, linewidth=2.5)
save(fig, "p7-alarm-clipped-ramp")
