import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 10,
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.dpi": 300
})


df = pd.read_csv("meet_traffic.csv")
df["Inter_Arrival"] = df["Time"].diff()
real_ia = df["Inter_Arrival"].dropna().to_numpy()
real_sizes = df["Length"].to_numpy()


tau = 0.001
df["New_Batch"] = df["Inter_Arrival"].isna() | (df["Inter_Arrival"] > tau)
df["Batch_ID"] = df["New_Batch"].cumsum()

real_batch_sizes = df.groupby("Batch_ID").size().to_numpy()
batch_start_times = df.groupby("Batch_ID")["Time"].first().to_numpy()
real_inter_batch = np.diff(batch_start_times)
real_intra_batch = df[~df["New_Batch"]]["Inter_Arrival"].to_numpy()


np.random.seed(42)
n_packets = len(df)
n_batches = len(real_batch_sizes)


naive_ia = np.random.exponential(scale=real_ia.mean(), size=n_packets - 1)
naive_new_batch = np.concatenate([[True], naive_ia > tau])
naive_batch_sizes = pd.Series(np.cumsum(naive_new_batch)).value_counts(sort=False).to_numpy()

shape_g, loc_g, scale_g = stats.gamma.fit(real_inter_batch, floc=0)
syn_inter_batch = stats.gamma.rvs(shape_g, loc=0, scale=scale_g, size=n_batches - 1)
syn_inter_batch = np.maximum(syn_inter_batch, tau + 1e-5)


p_geom = 1.0 / real_batch_sizes.mean()
syn_batch_sizes = stats.geom.rvs(p_geom, size=n_batches)


mean_intra = real_intra_batch.mean()
syn_ia_list = []
for idx, b_size in enumerate(syn_batch_sizes):
    if b_size > 1:
        intra = np.random.exponential(scale=mean_intra, size=b_size - 1)
        intra = np.clip(intra, 1e-6, tau)
        syn_ia_list.extend(intra)
    if idx < len(syn_inter_batch):
        syn_ia_list.append(syn_inter_batch[idx])
syn_ia = np.array(syn_ia_list)


n_syn_packets = syn_batch_sizes.sum()
weights = [0.2469, 0.0186, 0.7345]
comp = np.random.choice([0, 1, 2], size=n_syn_packets, p=weights)

syn_sizes = np.zeros(n_syn_packets)
m0, m1, m2 = (comp == 0), (comp == 1), (comp == 2)
syn_sizes[m0] = np.clip(np.random.normal(146.46, 59.59, m0.sum()), 60, 299)
syn_sizes[m1] = np.clip(np.random.normal(681.36, 199.02, m1.sum()), 300, 899)
syn_sizes[m2] = np.clip(np.random.normal(1141.74, 73.59, m2.sum()), 900, 1274)
syn_sizes = np.round(syn_sizes).astype(int)


fig1, axes1 = plt.subplots(1, 2, figsize=(7.2, 2.7))


sample_idx = np.arange(1, 2001)
axes1[0].scatter(real_ia[sample_idx] * 1000, real_sizes[sample_idx],
                 alpha=0.35, s=8, c="#1f77b4", edgecolors="none")
axes1[0].axvline(tau * 1000, color="red", linestyle="--", linewidth=1, label=r"Batch threshold $\tau=1$ ms")
axes1[0].set_xscale("log")
axes1[0].set_xlabel("Inter-arrival Time $A_i$ [ms] (log scale)")
axes1[0].set_ylabel("Packet Size $W_i$ [Bytes]")
axes1[0].set_title("(a) Joint Scatterplot ($A_i$ vs $W_i$)")
axes1[0].legend(loc="lower left")
axes1[0].grid(True, which="both", alpha=0.25)

axes1[1].hist(real_sizes, bins=45, density=True, alpha=0.55, color="#2ca02c", edgecolor="black", linewidth=0.4, label="Empirical Data")
x_w = np.linspace(60, 1274, 500)
gmm_pdf = (weights[0] * stats.norm.pdf(x_w, 146.46, 59.59) +
           weights[1] * stats.norm.pdf(x_w, 681.36, 199.02) +
           weights[2] * stats.norm.pdf(x_w, 1141.74, 73.59))
axes1[1].plot(x_w, gmm_pdf, "r-", linewidth=1.5, label="3-GMM Analytic Fit")
axes1[1].set_xlabel("Packet Size $W_i$ [Bytes]")
axes1[1].set_ylabel("Probability Density")
axes1[1].set_title("(b) Workload Distribution & 3-GMM Fit")
axes1[1].legend(loc="upper left")
axes1[1].grid(True, alpha=0.25)

plt.tight_layout()
plt.savefig("fig1_traffic_profile.pdf", bbox_inches="tight")
plt.close(fig1)


fig2, axes2 = plt.subplots(2, 2, figsize=(7.2, 5.0))

for arr, lbl, col, ls in [
    (real_ia * 1000, "Empirical", "black", "-"),
    (syn_ia * 1000, "Compound Model (Proposed)", "#1f77b4", "--"),
    (naive_ia * 1000, "Naive Exponential", "#d62728", ":")
]:
    xs = np.sort(arr)
    ys = np.arange(1, len(xs) + 1) / len(xs)
    axes2[0, 0].plot(xs, ys, label=lbl, color=col, linestyle=ls, linewidth=1.5)
axes2[0, 0].set_xlim(0, 20)
axes2[0, 0].set_xlabel("Inter-arrival Time $A_i$ [ms]")
axes2[0, 0].set_ylabel("CDF $F_A(a)$")
axes2[0, 0].set_title("(a) Packet Inter-Arrival Time CDF")
axes2[0, 0].legend(loc="lower right")
axes2[0, 0].grid(True, alpha=0.25)

q_grid = np.linspace(0.01, 0.99, 100)
q_emp = np.quantile(real_inter_batch * 1000, q_grid)
q_syn = np.quantile(syn_inter_batch * 1000, q_grid)
axes2[0, 1].scatter(q_emp, q_syn, s=12, alpha=0.7, color="#9467bd", label="Quantiles (1%–99%)")
max_v = max(q_emp.max(), q_syn.max())
axes2[0, 1].plot([0, max_v], [0, max_v], "r--", linewidth=1.2, label="45° Ideal Reference")
axes2[0, 1].set_xlabel("Empirical Inter-Batch Quantiles [ms]")
axes2[0, 1].set_ylabel("Gamma Model Quantiles [ms]")
axes2[0, 1].set_title("(b) Q-Q Plot: Inter-Batch Time")
axes2[0, 1].legend(loc="upper left")
axes2[0, 1].grid(True, alpha=0.25)


b_bins = np.arange(1, 15)
emp_pmf = [np.mean(real_batch_sizes == k) for k in b_bins]
syn_pmf = [np.mean(syn_batch_sizes == k) for k in b_bins]
naive_pmf = [np.mean(naive_batch_sizes == k) for k in b_bins]
width = 0.28
axes2[1, 0].bar(b_bins - width, emp_pmf, width=width, label="Empirical", color="black", alpha=0.75)
axes2[1, 0].bar(b_bins, syn_pmf, width=width, label="Geometric ($p=0.425$)", color="#1f77b4", alpha=0.8)
axes2[1, 0].bar(b_bins + width, naive_pmf, width=width, label="Naive Exp Derived", color="#d62728", alpha=0.7)
axes2[1, 0].set_xlabel("Batch Size $B_i$ [packets]")
axes2[1, 0].set_ylabel("Probability Mass $P(B_i = b)$")
axes2[1, 0].set_title("(c) Batch Size Distribution ($B_i$)")
axes2[1, 0].set_xticks(range(1, 15, 2))
axes2[1, 0].legend(loc="upper right")
axes2[1, 0].grid(True, alpha=0.25)


bp = axes2[1, 1].boxplot(
    [real_sizes, syn_sizes],
    labels=["Empirical $W_i$", "Synthetic 3-GMM $W_i$"],
    widths=0.45,
    patch_artist=True,
    showmeans=True,
    meanprops={"marker": "o", "markerfacecolor": "white", "markeredgecolor": "black"}
)
for patch, color in zip(bp["boxes"], ["#aec7e8", "#98df8a"]):
    patch.set_facecolor(color)
axes2[1, 1].set_ylabel("Packet Size $W_i$ [Bytes]")
axes2[1, 1].set_title("(d) Workload Boxplot & ECDF Match")
axes2[1, 1].grid(True, alpha=0.25)

plt.tight_layout()
plt.savefig("fig2_model_validation.pdf", bbox_inches="tight")
plt.close(fig2)
print("Figures 'fig1_traffic_profile.pdf' and 'fig2_model_validation.pdf' successfully generated!")