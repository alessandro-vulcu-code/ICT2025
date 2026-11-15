"""Compile an existing report, or generate the legacy report from experiment results."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
from source import ROOT


def compile_report(source):
    source = (ROOT / source).resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    output = ROOT / 'output/pdf'
    output.mkdir(parents=True, exist_ok=True)
    for _ in range(2):
        completed = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-synctex=1',
             '-output-directory=' + str(output), source.name],
            cwd=source.parent, capture_output=True, text=True)
        if completed.returncode:
            raise RuntimeError(completed.stdout[-4000:])
    pdf = output / (source.stem + '.pdf')
    for destination in (ROOT / pdf.name, ROOT / 'report.pdf', output / 'report.pdf'):
        if destination != pdf:
            shutil.copyfile(pdf, destination)
    for suffix in ('.aux', '.log', '.synctex.gz'):
        shutil.copyfile(output / (source.stem + suffix), ROOT / (source.stem + suffix))
    print(ROOT / pdf.name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path,
                        help='Compile an existing .tex file without regenerating its text')
    args = parser.parse_args()
    if args.source is not None:
        compile_report(args.source)
        return
    results = json.loads((ROOT/'analysis/results.json').read_text())
    ci = results['ci95']
    rows = []
    labels = [('loss_pct', 'Packet loss (\\%)', '$\\leq 1$'),
              ('byte_delivery_pct', 'Delivered bytes (\\%)', '$\\geq 99$'),
              ('mean_ms', 'Mean delay (ms)', '$\\leq 30$'),
              ('p95_ms', '95th delay percentile (ms)', '$\\leq 50$'),
              ('p99_ms', '99th delay percentile (ms)', '$\\leq 100$'),
              ('jitter95_ms', '95th delay-variation percentile (ms)', '$\\leq 30$'),
              ('offered_kbps', 'Offered rate (kbit/s)', 'Descriptive'),
              ('throughput_kbps', 'Output throughput (kbit/s)', 'Descriptive')]
    for key, label, target in labels:
        x=ci[key]
        rows.append(f'{label} & {target} & ${x["mean"]:.3f} \\pm {x["half95"]:.3f}$'+r' \\')
    table = '\n'.join(rows)
    control = results['controls']
    comparisons = []
    for name, label in [('underprovisioned','Underprovisioned'), ('large_buffers','Large buffers, low rates')]:
        x=control[name]['metrics']
        comparisons.append(f'{label} & {x["loss_pct"]:.2f} & {x["p95_ms"]:.2f} & {x["throughput_kbps"]:.2f}'+r' \\')
    for name,label in [('homework1_offsets','Original within-batch offsets'), ('held_out_capture','Held-out 120 s segment')]:
        x=results['robustness'][name]
        comparisons.append(f'{label} & {x["loss_pct"]:.2f} & {x["p95_ms"]:.2f} & {x["throughput_kbps"]:.2f}'+r' \\')
    text = r'''\documentclass[10pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{times,amsmath,graphicx,booktabs}
\usepackage[top=1.8cm,bottom=1.8cm,left=1.8cm,right=1.8cm]{geometry}
\usepackage{enumitem}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}
\setlist{nosep,leftmargin=*}
\begin{document}
\begin{center}
{\Large Network modeling -- AY 2026/2027}\\[4pt]
{\large Homework 2 -- Composite shaping of Zoom uplink traffic}\\[5pt]
Alessandro Vulcu -- ID 2185190, University of Padua
\end{center}
\begin{abstract}
I implement a simulated-time token bucket followed by a constant-rate leaky bucket,
using the empirical Zoom source fitted in Homework 1. A grid search balances rate
reservations and storage under explicit loss and delay budgets. Independent
30-minute replications confirm the selected configuration. Results describe the
fitted traffic model and shaping contribution to QoS, rather than total call quality.
\end{abstract}
\section{Source and implementation}
Homework 1 selected a camera-on outbound Zoom UDP flow. The first 180 s formed the
training sample (19,645 packets); the next 120 s were held out. Sizes are captured
Ethernet frame lengths, not media payload. I reuse the training CSV, with a 1 ms
clustering threshold and both boundary clusters excluded. The resulting 7,233
complete cycles store $(D_i,\{U_{i,k},L_{i,k}\}_{k=1}^{B_i})$: cluster interval,
packet offsets, and lengths. Uniform independent sampling of whole tuples preserves
dependence between interval, count, and lengths. The fitted mean rate is 865.95 kbit/s;
the maximum packet is 1,341 B. No new capture or refitting on validation is needed.

To meet this assignment's simultaneous-batch convention, all $B_i$ packets are
emitted at the cycle epoch, on separate rows with identical timestamps. The next
epoch is advanced by $D_i$. This retains the cluster-interval, batch-size, and
length distributions, while deliberately removing the short within-cluster offsets
used in Homework 1. A separate option restores those offsets for sensitivity analysis.
The source stops on $[0,T)$ and assigns consecutive unique packet identifiers.

\texttt{source.py} generates the input file; \texttt{shaper.py} reads it and writes
the output. Both use three whitespace-separated fields: identifier, timestamp in
seconds, length in bytes. Input times are generation times; output times are
transmission completion times. IDs and lengths survive unchanged. Dropped IDs
appear only in a separate drop log. No payload or wall-clock waiting is involved.

The token bucket starts full, with real-valued continuous tokens:
\[
q(t+\Delta)=\min\{b,q(t)+\rho\Delta\},\qquad
t_{\rm eligible}=t+\max\{0,L_{\rm head}-q(t)\}/\rho.
\]
One token covers one byte. Only the FIFO head can leave; a transfer consumes its
entire length. Packets exceeding $b$ are explicitly dropped. Insufficient tokens
cause FIFO buffering in $B_i$; insufficient free storage causes a tail drop.
There is no backpressure: a transfer to a full LBF queue is discarded and its
tokens remain consumed. The LBF transmits one packet at a time for $L/\mu$ seconds,
non-preemptively; its waiting queue has capacity $B_o$. Queue capacities count
waiting bytes; the packet in service is excluded. An idle transmitter can therefore
accept a packet even with $B_o=0$.

The event clock jumps to the next arrival, head eligibility, or completion.
At equal times it handles LBF completion first, then eligible queued TBF packets,
then input rows in file order. Buffered packets cannot be bypassed. Both queues
drain after source shutdown. Token eligibility is rounded upward to a representable
time supplying the full packet, avoiding repeated-clock stalls without borrowing
tokens through a fixed tolerance. Ten automated
checks cover exact timing, FIFO, both overflows, oversize rejection, input validation,
source reproduction, conservation, the TBF envelope, small token deficits, and
clock translations up to $10^9$ s. All pass.
\clearpage
\section{QoS budgets and experimental method}
Zoom video is interactive: waiting harms responsiveness, delay variation raises
receiver buffering needs, and loss removes video data. Table 1 gives six shaping-only
QoS budgets; offered rate and throughput are additional descriptive measures, not
acceptance criteria. The budgets leave room for propagation, other queues, codec
processing, and playout; they are design choices, not Zoom specifications.

For a concrete design yardstick, a nominal 30-frame/s cadence gives 33.3 ms per
frame; this is illustrative, not a frame rate measured in Homework 1. Mean delay
$\leq30$ ms keeps average added latency below one such interval. The p95 limit
of 50 ms allows at most 1.5 intervals for 95\% of delivered packets; p99
$\leq100$ ms tolerates rare bursts up to three intervals. A p95 delay-variation
limit of 30 ms keeps 95\% of successive delivered-packet delay changes below
roughly one interval, reducing pressure on the playout buffer. Loss $\leq1\%$ and byte delivery
$\geq99\%$ require preservation of at least 99 out of every 100 packets and bytes,
respectively, preventing low delays achieved by dropping traffic or selectively
losing large packets. These targets do not guarantee decoded video quality.

For each delivered packet $j$, $d_j=t_j^{\rm out}-t_j^{\rm in}$. Delay variation is
$v_j=|d_j-d_{j-1}|$ for consecutive delivered packets, including pairs across lost
IDs. Its 95th percentile is reported as jitter; it is not an RTP jitter estimator.
Throughput counts completed bytes within $[0,T)$ divided by $T$; delivery fractions
and delay include the final drain. Delays describe survivors only and are always
interpreted alongside losses. All rates use captured bytes, not codec goodput.

I evaluate 192 configurations on one common 300 s trace, seed 2026:
\[
\begin{aligned}
\rho&\in\{110,140,180,220\}\times10^3\ \mathrm{B/s},&
b&\in\{1341,4096,8192,16384\}\ \mathrm{B},\\
B_i&\in\{4096,16384\}\ \mathrm{B},&
\mu&\in\{120,220,300\}\times10^3\ \mathrm{B/s},\\
B_o&\in\{4096,16384\}\ \mathrm{B}.&&
\end{aligned}
\]
Common input isolates parameter effects. Of these, @FEASIBLE@ satisfy every budget.
Among feasible candidates I minimize the explicit normalized resource score
\[
C=\frac{\rho}{10^5}+\frac{\mu}{10^5}+\frac{b+B_i+B_o}{16384}.
\]
Each rate reservation and the total storage carry equal unit weights at the stated
scales. Bucket capacity counts as a burst allowance, not literal stored payload.
The score expresses a design preference, not a monetary cost. A positive weight
on every resource gives a non-dominated feasible grid choice; it is not a global
optimum or a unique preference-independent solution.

I then freeze the choice and run ten independent 1,800 s replications, seeds
3026--3035, without reselecting on those results. Each run contains about 196,000
packets, or approximately 72,000 sampled cycles, and lasts ten times the training
window. I retain full-start transient behavior because a call begins with empty
queues and a full token bucket. The long duration makes this short transient small.
All ten runs satisfy every budget. Table 1 gives the mean of each run-level
statistic and a Student-$t$ 95\% confidence interval,
$\bar x\pm t_{0.975,9}s_x/\sqrt{10}$. For quantiles this estimates the mean
run quantile, not a confidence interval for an individual packet or a pooled quantile.
Replications, not correlated packets, are the independent statistical units.

\begin{table}[h]
\centering\small
\caption{Independent confirmation: means and 95\% confidence half-widths.}
\begin{tabular}{lrr}\toprule
KPI & Proposed budget & Mean $\pm$ half-width\\\midrule
@TABLE@
\bottomrule\end{tabular}
\end{table}
\clearpage
\section{Results, trade-offs, and limits}
The selected parameters are
\[
(\rho,b,B_i,\mu,B_o)=(180000,4096,16384,220000,4096),\qquad C=5.50.
\]
This reserves 1.44 Mbit/s at the TBF and a 1.76 Mbit/s serialization rate. Total
waiting storage is 20,480 B; adding the burst allowance gives 24,576 resource units.
Both rates exceed the roughly 0.866 Mbit/s mean source load: short bursts, not only
mean-rate stability, govern the delay budget. The full bucket admits a small burst
before enforcing the long-term rate; the transmitter then serializes it.

\begin{figure}[h]
\centering\includegraphics[width=\textwidth]{analysis/results.pdf}
\caption{Search trade-off, delivered-packet delay distribution, and input/output
rates for the selected setting. Star: minimum-score feasible candidate. Rate samples
use 100 ms bins; packet completions can still cluster around bin boundaries.}
\end{figure}

The representative delivered trace (seed 3026) contains @OUTPUT@ of @INPUT@ packets,
with @DROPS@ input-buffer drops and no output-buffer drops. Peak input occupancy is
@PEAKI@ B and peak output waiting occupancy is @PEAKO@ B. The small output queue
works because the TBF spreads the offered bursts before the faster transmitter.
A bigger $b$ can relieve input waiting but also pushes a larger burst into the output
queue; increasing $B_i$ prevents some losses while allowing longer delay. Increasing
$B_o$ cannot recover packets already discarded at the input. Higher $\rho$ reduces
token waiting; higher $\mu$ shortens serialization and output waiting. Their benefits
depend on which stage is the bottleneck.

\begin{table}[h]
\centering\small
\caption{Controls and robustness checks, using seed 3026 where synthetic.}
\begin{tabular}{lrrr}\toprule
Case & Loss (\%) & p95 delay (ms) & Output (kbit/s)\\\midrule
@COMPARISONS@
\bottomrule\end{tabular}
\end{table}

The underprovisioned control uses $(90000,1341,4096,100000,4096)$: low delay alone
hides severe losses. A low-rate setting with large buffers,
$(110000,8192,65536,120000,65536)$, still fails QoS and raises delay substantially.
More storage alone is therefore insufficient. Restoring Homework 1's packet offsets
barely changes the representative result. Processing the held-out segment of the same capture
also meets all budgets, but this short check does not replace the longer model runs.

The confidence intervals quantify Monte Carlo variability conditional on the fitted
empirical source. They exclude uncertainty from the 180 s training sample, different
users or network paths, and the missing slow temporal correlation identified in
Homework 1. Independent cycle resampling loses that correlation and overstates some
100 ms variability; repeated synthetic hours do not create new observed evidence.
The shaper also does not feed congestion signals back to Zoom's adaptive encoder.
The resource choice is thus defensible for this model, grid, and cost preference;
deployment would require more captures and end-to-end quality measurements.

\textbf{Reproduction.} \texttt{README.md} documents both module CLIs, training-data
provenance, trace aliases, test commands, and full reproduction with
\texttt{python experiments.py} followed by \texttt{python build\_report.py}.
Source code, measured tables, buffer/drop traces, figure source, and this report
are included in the homework directory.
\end{document}
'''
    rep=results['replications_results'][0]
    replacements = {'@FEASIBLE@':str(results['feasible_count']), '@TABLE@':table,
                    '@COMPARISONS@':'\n'.join(comparisons), '@INPUT@':f'{rep["packets"]:,}',
                    '@DROPS@':str(rep['drop_reasons'].get('input_overflow',0)),
                    '@OUTPUT@':f'{rep["packets"]-round(rep["packets"]*rep["loss_pct"]/100):,}',
                    '@PEAKI@':str(rep['peak_bi']), '@PEAKO@':str(rep['peak_bo'])}
    for key,value in replacements.items():
        text=text.replace(key,value)
    (ROOT/'report.tex').write_text(text)
    compile_report(Path('report.tex'))


if __name__ == '__main__':
    main()
