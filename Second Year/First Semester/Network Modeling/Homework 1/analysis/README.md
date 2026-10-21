# Zoom traffic report: reproduction

The completed source is `../Latex template/Homework-LaTex-template.tex`.
The compiled two-page report is `../output/pdf/Homework-LaTex-template.pdf`.
An identical copy is kept beside the source in `../Latex template/`.
The Discord reference available in this folder was named `Report.pdf`.
The original unfilled LaTeX template is preserved as
`Homework-LaTex-template-original.tex`.

## Data and time reference

`analyze_zoom.py` re-exports the required fields directly from `../zoom.pcapng`:

```text
udp.stream == 0 && ip.src == 192.168.3.7 && frame.number > 32864
```

It sorts selected timestamps before calculating differences. Time zero is the first
selected packet, at epoch `1792333415.004835100`, or `431.222298187` seconds into
the raw capture. This origin is not the recorded stopwatch start.

The camera-on sample is `[270, 570)` seconds from this origin. Training uses
`[270, 450)`; validation uses `[450, 570)`. Camera transitions are inferred from the
traffic profile. Other phase boundaries cannot be recovered from the selected
video-related flow alone. No assumed 60/60/180/300/60-second schedule is imposed.

Sizes are captured Ethernet frame lengths (`frame.len`) in bytes; model weights
are eight times these values, in bits. Rates use the fixed observation-window
duration, including any empty edges.

## Model

The Poisson baseline uses exponential gaps fitted to training packet gaps, one
packet per event, and independently resampled training frame lengths.

The empirical batch-renewal model groups training packets separated by at most
1 ms. Boundary clusters are excluded. Each retained cycle stores its duration to
the next cluster start, packet count, packet offsets and packet sizes. Complete
tuples are sampled uniformly and independently. All marginal distributions are
therefore empirical; no parametric law for a codec frame or batch size is claimed.
The count and weights remain dependent on cycle duration within a sampled tuple.
Batch inter-arrivals are renewal intervals; reconstructed packet gaps are different
variables and need not be independent. Packet offsets are retained rather than
placing all packets at exactly the batch epoch.

Both synthetic traces last 120 seconds. Seed 2026 is used in the figures and table;
seeds 2026 through 2055 assess simulation variability. The 5th–95th percentile
range across seeds is a simulation summary, not a confidence interval for Zoom.
CDF distances are descriptive Kolmogorov distances; no i.i.d. significance test
is asserted. The model's missing correlation and excessive 100 ms count Fano
factor are reported rather than concealed.

The report explicitly distinguishes packet inter-arrival times
`A_j^{pkt} = t_j - t_{j-1}` from cluster-start intervals `D_i`.
The comparison figure retains three full-trace CDFs, a first-second packet
inter-arrival scatterplot, the first ten seconds of rate in 100 ms bins, and the
entire 120-second validation window in 1 s bins. The packet-size scatterplot and
20 ms rate plot remain as commented optional export blocks in `analyze_zoom.py`:
the former adds little to the size CDF, while the latter is crowded by overlapping
spikes. Statistical calculations at 20 ms are still performed.

This construction uses the marked/weighted point-process and renewal-reward
definitions in Lessons 3 and 4. It models a bursty VBR source during camera-on
operation. A sequence of manually controlled camera changes does not supply
repeated natural ON/OFF periods for fitting an On–Off activity model.

## Commands

From the homework directory, with TShark and NumPy/SciPy/Matplotlib installed:

```bash
/home/alessandrovulcu/.conda/envs/sklearn-env/bin/python analysis/analyze_zoom.py
```

Compile from the template directory so its relative figure paths resolve:

```bash
cd "Latex template"
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../output/pdf Homework-LaTex-template.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../output/pdf Homework-LaTex-template.tex
cp ../output/pdf/Homework-LaTex-template.pdf Homework-LaTex-template.pdf
```

Outputs include the training/validation and synthetic CSV traces,
`zoom_report_statistics.json`, a comparison PNG, and two vector PDF figures in
`../Latex template/figure/`. The preliminary root-level `zoom_uplink_summary.json`
describes the entire mixed-phase selection, not the camera-on report sample.
