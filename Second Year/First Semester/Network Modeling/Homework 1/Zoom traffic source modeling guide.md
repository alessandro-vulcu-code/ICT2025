# Homework 1 — A practical guide to modeling Zoom traffic

This is a **working guide**, not a report or a set of measured results. It translates the
[homework brief](Homework1-SourceModel.pdf) into a reproducible Zoom experiment using
the point-process notation from [Lesson 3](../Lesson%203/Lesson%203%20-%20Network%20abstraction%20and%20traffic%20source%20models.md)
and the source models from [Lesson 4](../Lesson%204/4.%20Traffic%20source%20models.md).

## 1. What the assignment actually requires

Starting from a real packet capture of one application, you must:

1. Extract packet timestamps and sizes.
2. Describe the observed traffic pattern.
3. Propose stochastic models for inter-arrival times $\{A_i\}$, batch sizes
   $\{B_i\}$, and packet workloads $\{W_{i,k}\}$.
4. Generate a **synthetic trace** from those models.
5. Compare synthetic and measured traces with suitable plots: time plots, empirical and
   model CDFs, Q–Q plots, boxplots, or similar tools.

The PDF specifies a maximum of **two report pages** and an older course template. Current
course instructions may differ; this guide deliberately does not draft that report.

> [!important] Define the observed source first
> Recommended target: **outbound packets from your computer during one Zoom desktop
> meeting**, with microphone and camera settings recorded. Outbound capture is closer
> to your device's packet-generation process. Inbound packets describe *reception* after
> network delay, loss, and scheduling. Both are allowed by the assignment, but must not
> be pooled into one arrival sequence.

## 2. Plan one controlled Zoom session

Use a meeting with another participant or device so audio and video have a real receiver.
Keep network, interface, participants, and Zoom client fixed during the run. Record a
simple activity timeline separately from the capture:

| Phase | Suggested duration | What it helps reveal |
|---|---:|---|
| Zoom closed, capture running | 30–60 s | Background flows and baseline |
| Meeting connected, microphone muted, camera off | 60 s | Signaling, keepalives, and idle traffic |
| Microphone on, camera off; alternate speech and silence | 2–3 min | Audio packet spacing and possible silence suppression |
| Camera on, speak normally | 3–5 min | Video size variation and packet clusters |
| Camera off again | 60 s | Whether the suspected video flow/rate disappears |

Record exact start/end times of each phase, camera state, microphone state, whether screen
sharing was active, and whether the connection changed. For a **single stationary model**,
analyze one stable phase, such as camera-on uplink, rather than fitting one distribution to
all phases indiscriminately. Use the phase changes to *identify* Zoom traffic and to test
whether a state-based model is needed. A second run under the same conditions helps
check whether the fitted behavior repeats.

Do not expect a fixed Zoom bitrate or a guaranteed 20 ms audio gap: codecs, silence
suppression, congestion adaptation, camera content, and transport choices vary. These are
hypotheses to inspect, not results to claim before capture.

## 3. Configure Wireshark and capture

### Before recording

1. Open **Capture → Options**. Choose the interface carrying the meeting traffic: Wi-Fi
   or Ethernet, not a disconnected adapter. Check that its activity graph changes when
   you use the network.
2. Capture to a named **pcapng** file. Keep full packets (no shortened snap length) so
   length fields and protocol headers remain available. One interface is simplest for
   consistent packet-length interpretation.
3. Leave the **capture filter empty** on the first run. You do not yet know which remote
   addresses and ports the meeting will use. Apply *display filters after capture*.
4. Keep default non-monitor Wi-Fi capture. Raw 802.11 monitor mode is unnecessary for
   traffic-source modeling and may disconnect the interface.
5. Start capture **before** opening the meeting, execute the planned phases, stop it after
   leaving the meeting, and save the file.

Wireshark's [Capture Options](https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureOptions.html)
documents interface, snap length, and pcapng settings. Capture filters discard packets
before they enter the file; [display filters](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkDisplayFilterSection)
only change what is shown.

### Check capture quality

- In **Statistics → Capture File Properties**, inspect capture duration and any reported
  dropped-packet count. A burst of missing packets can create false long inter-arrivals.
- Inspect one packet's `frame.len` (original frame length) and captured length. If captured
  length is shorter, size analysis needs care.
- On a host capture, outbound timestamps mark observation in the operating-system capture
  path, not the exact instant the Zoom encoder generated a media unit. Unusually large
  TCP frames can also reflect segmentation offload; check before treating them as
  ordinary on-wire packet sizes.
- Check that the phase timeline matches visible changes in traffic. If almost nothing
  changes when camera turns on, you may have chosen the wrong interface, direction, or
  flow.
- Save the **raw capture** separately from any filtered export; later filters can then be
  corrected without repeating the meeting.

## 4. Identify Zoom packets before modeling

Do **not** label packets as Zoom solely because they use a familiar port. Zoom currently
lists UDP `3478`, `3479`, `8801–8810` and TCP `443`, `8801`, `8802` among meeting
connectivity rules, but a client may use different paths or fallbacks, and a port can
carry more than one kind of traffic. Treat ports as clues, then check timing and
conversations against your controlled activity changes. See
[Zoom's firewall requirements](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0060548).

In Wireshark:

1. Open **Statistics → Conversations**, especially **UDP** and **TCP** tabs. Sort by
   bytes or packets and inspect start time, duration, both directions, and remote address.
   A plausible media conversation grows during the meeting and changes when media is
   enabled. Wireshark documents those columns in
   [Conversations](https://www.wireshark.org/docs/wsug_html_chunked/ChStatConversations.html).
2. Apply a candidate conversation filter from that dialog, then inspect **Statistics →
   I/O Graphs** at, for example, 20 ms, 100 ms, and 1 s intervals. Use *Bits* with
   **Avg over Time** for bit/s, or count packets per interval. Small intervals show packet
   structure; larger ones show activity periods. See
   [I/O Graphs](https://www.wireshark.org/docs/wsug_html_chunked/ChStatIOGraphs.html).
3. Compare with the baseline and camera-off phases. If a candidate flow does not follow
   your controlled change, investigate further. Another device, browser tab, VPN, or
   automatic update could be the real source.
4. Choose **one direction**: local source IP to remote IP for uplink, or the reverse for
   downlink. If Zoom uses several confirmed media conversations, either analyze one
   clearly identified conversation or document the exact union of flows representing
   your chosen source. Do not silently merge unrelated TCP signaling, UDP media, and
   background traffic.

Example display filter for one identified IPv4 UDP conversation:

```text
udp.stream == 7 && ip.src == 192.0.2.10
```

Here `7` and `192.0.2.10` are **placeholders**, not Zoom identifiers. The `udp.stream`
value comes from *your* capture; `192.0.2.10` must be replaced by the local IP seen in
that capture. For IPv6, use `ipv6.src`. For a TCP fallback, use an identified `tcp.stream`
and model the resulting **observed TCP packets**, stating that segmentation,
retransmissions, and acknowledgments affect them. The
[UDP field reference](https://www.wireshark.org/docs/dfref/u/udp.html) defines
`udp.stream`, and Wireshark accepts `&&` in display filters.

> [!tip] If identification remains ambiguous
> Repeat a shorter capture with no other network activity. Compare media-off and
> media-on rates for each candidate conversation. A computer's process-to-socket view
> can support identification, but timing and the captured five-tuple remain the evidence
> used for the final filter.

## 5. Export a precise packet table

Use one consistent definition of packet size. A practical choice is `frame.len`, **bytes
of the captured link-layer frame**. It includes headers visible on the chosen interface
and is not the encoded Zoom media payload. If comparing payload behavior, also export
`udp.length`: UDP payload bytes are `udp.length - 8`, but Zoom's own media/protocol
headers remain inside that payload. State which field you model and use it consistently
for both real and synthetic traffic.

Using TShark, bundled with Wireshark, export the selected packets as CSV:

```bash
tshark -r "zoom_capture.pcapng" \
  -Y 'udp.stream == 7 && ip.src == 192.0.2.10' \
  -T fields -E header=y -E separator=, -E quote=d \
  -e frame.number -e frame.time_epoch -e frame.len \
  -e ip.src -e ip.dst -e udp.srcport -e udp.dstport -e udp.length \
  > zoom_uplink.csv
```

Replace file, stream number, and IP. For IPv6, change `ip.src`/`ip.dst` to
`ipv6.src`/`ipv6.dst` in both filter and field list. If several *confirmed* UDP streams
form the source, use a parenthesized OR filter, keep their identifiers in the exported
table, and sort all selected packets by timestamp.

`frame.time_epoch` is an absolute timestamp in seconds; `frame.len` is frame length.
TShark's [`-T fields`, `-e`, and `-E` options](https://www.wireshark.org/docs/man-pages/tshark)
control this export. Wireshark also offers **File → Export Packet Dissections → CSV**,
but TShark makes the chosen fields and filter easier to repeat. Do **not** use the
time difference between consecutive *captured* packets: it includes filtered-out
background traffic. Compute differences **after filtering and sorting**. Wireshark's
[time-format documentation](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkTimeFormatsSection.html)
explains displayed versus captured time differences.

Your clean analysis table should contain at least:

| Column | Meaning | Unit |
|---|---|---|
| $t_i$ | Timestamp of selected packet $i$, relative to first selected packet | s |
| $L_i$ | Selected packet length (`frame.len`, or stated alternative) | bytes |
| $A_i^{\mathrm{pkt}}=t_i-t_{i-1}$ | Gap between consecutive selected packets | s |
| Flow ID | Exact conversation or five-tuple used | identifier |
| Phase | Camera/microphone condition at that timestamp | label |

Calculate $A_i^{\mathrm{pkt}}$ only for $i\ge2$. Equal timestamps can result from
capture resolution or several packets arriving together; inspect them rather than
silently deleting zeros. If multiple flows are combined, the packet gap is between
the next packet from **any selected flow**.

This minimal Python check reads the exported CSV without fitting a model:

```python
import csv
from decimal import Decimal
from statistics import mean

with open("zoom_uplink.csv", newline="") as source:
    rows = [
        (Decimal(row["frame.time_epoch"]), int(row["frame.len"]))
        for row in csv.DictReader(source)
        if row["frame.time_epoch"] and row["frame.len"]
    ]

rows.sort(key=lambda row: row[0])
if len(rows) < 2:
    raise ValueError("Need at least two selected packets")

t0 = rows[0][0]
times_s = [float(t - t0) for t, _ in rows]
sizes_B = [size for _, size in rows]
gaps_s = [right - left for left, right in zip(times_s, times_s[1:])]
duration_s = times_s[-1]
if duration_s <= 0:
    raise ValueError("Selected packets have no positive observation span")

print("packets:", len(rows))
print("mean packet gap (s):", mean(gaps_s))
print("mean frame size (B):", mean(sizes_B))
print("observed bit rate (bit/s):", 8 * sum(sizes_B) / duration_s)
```

This rate spans first to last selected packet; for phase-specific rate, use that
phase's **recorded start and end times** as denominator and retain its zero-traffic
edges. A very short selected sample makes either estimate unstable.

## 6. Decide what an event, mark, and weight mean

The lesson's marked and weighted point process is

$$
\mathcal M=\{(\tau_i,B_i,W_{i,1},\ldots,W_{i,B_i})\}_{i\ge1},
\qquad A_i=\tau_i-\tau_{i-1}.
$$

$\tau_i$ is an event time, $B_i$ packets generated in that event, and $W_{i,k}$
the size of packet $k$. The model's long-run offered bit rate, when renewal-reward
assumptions apply, is

$$
\bar G=\frac{E\left[\sum_{k=1}^{B_i}W_{i,k}\right]}{E[A_i]}
\quad\text{bits/s},
$$

provided weights are in bits. With `frame.len` in bytes, multiply numerator by $8$.

**Start with an unambiguous packet-event model.** Let each selected packet be one event:
$\tau_i=t_i$, $B_i=1$, and $W_{i,1}=8L_i$ bits. This fully addresses all three
requested components; the mark distribution is a point mass at one. It is honest if
packet capture gives no defensible evidence of a larger simultaneous batch. Then test
whether the resulting $A_i$ model reproduces bursts and rate variation.

**Add a batch model only when justified.** If packets repeatedly arrive in tight
clusters (for example, groups around video-frame generation), define an explicit
clustering rule: packets separated by no more than a chosen threshold $\delta$ belong
to the same batch. Set $\tau_i$ to the first packet time in cluster $i$, $B_i$ to its
packet count, and $W_{i,k}$ to its packet sizes. Inspect a gap histogram or scatterplot
to choose $\delta$; try nearby values to see whether results change drastically. The
observed packets are not truly simultaneous, so this is an **approximation**. A synthetic
trace also needs within-batch offsets if you want to compare raw packet gaps; setting
every packet in a batch to exactly $\tau_i$ creates artificial zero gaps.

For example, *illustrative, not measured Zoom data*: packet times
$(0,1,2,20)$ ms with sizes $(200,1200,600,220)$ B have raw packet gaps
$(1,1,18)$ ms. With $\delta=3$ ms, they form two batches:
$\tau_1=0$ ms, $B_1=3$; $\tau_2=20$ ms, $B_2=1$; batch inter-arrival
$A_2=20$ ms. The first batch has three distinct weights, not one 2000 B packet.

Alternative: use fixed slots of duration $\Delta$, with one event every $\Delta$,
$B_n=$ number of packets in slot $n$ (including zero), and $W_{n,k}$ their sizes.
Then **event inter-arrivals are fixed** at $A_n=\Delta$ while packet inter-arrivals
$A_i^{\mathrm{pkt}}$ still vary. This is useful for an On–Off/Markov count model, but
state the distinction clearly. Choosing $\Delta$ after looking at 20 ms, 100 ms, and
1 s I/O graphs avoids an arbitrary scale.

## 7. Inspect the data before fitting distributions

For one stable phase, create these diagnostics:

| Plot/statistic | Question it answers |
|---|---|
| Packet size versus time (scatterplot) | Are size modes or media changes visible? |
| Packet gap versus time (scatterplot) | Periodic spacing, clusters, long pauses? |
| Rate $G_\Delta(n)=8\sum_{t_i\in[n\Delta,(n+1)\Delta)}L_i/\Delta$ | How do peaks depend on time scale? |
| CDF and histogram of positive packet gaps | Exponential, narrow periodic peak, long tail, or multimodal? |
| CDF and histogram of packet sizes | Single distribution or distinct size groups? |
| Batch-size frequency/CDF, if batches defined | Are batches mostly one packet or variable? |
| Lag correlation of counts or gaps | Is an i.i.d. renewal model plausible? |

Also calculate packet count, observation duration, mean and median size/gap,
coefficient of variation $CV_A=\operatorname{sd}(A)/E[A]$, and mean rate from total
bits divided by observation duration. For fixed-width count windows, inspect Fano
factor $\operatorname{Var}(N_\Delta)/E[N_\Delta]$ and peak-to-mean rate at **stated**
$\Delta$. These metrics are not interchangeable. Beware zero traffic before or after a
phase: including it changes the estimated mean and gap distribution.

### Reasonable patterns to look for, not promised results

- **Audio-only uplink:** often smaller, more regularly spaced packets during speech;
  silence suppression may create low-activity intervals. A fixed interval plus jitter
  can outperform an exponential model if the gap histogram has a narrow peak.
- **Video uplink:** variable packet sizes, several packets close together, and rate
  changes with scene motion or adaptation. Cluster sizes or slot counts may vary.
- **Camera off:** candidate video flow or its rate should shrink or stop; small
  keepalives/control packets can remain.
- **Whole meeting:** different phases and media can make a multimodal distribution.
  Fitting one exponential to every gap may match the mean while missing time structure.
- **TCP fallback:** packet timing and sizes may reflect TCP segmentation, ACKs, and
  retransmissions; interpret as traffic *observed at your interface*.

Inference above follows the course models and controlled experiment; actual Zoom
behavior must come from your trace.

## 8. Propose a stochastic model in stages

### Baseline model: one packet per arrival

Set $B_i\equiv1$ and fit $A_i^{\mathrm{pkt}}$ and $W_i$ from a stable phase.
Useful candidate families depend on the plots:

| Observation | Candidate for $A$ | Why/limitation |
|---|---|---|
| Roughly exponential CDF, $CV_A\approx1$, little serial dependence | Exponential($\lambda$) with $\hat\lambda=1/\bar A$ | Gives Poisson arrivals; still check count variability and long gaps |
| Narrow peak near a period $T$ | $A=\max(\epsilon,T+J)$ with small fitted jitter $J$ | Represents packetization; independent jitter may still miss longer activity changes |
| Positive skew or long right tail | Gamma, lognormal, Weibull, or empirical resampling | Check tail and serial dependence; heavy tail alone does not force an On–Off model |
| Several peaks or a mass of short gaps plus long pauses | Mixture or state-dependent model | A one-component fit hides multiple mechanisms |

For $W$, packet size is discrete and bounded by the observed network setup. An
**empirical discrete distribution** (sample sizes with their measured frequencies) is a
valid and often defensible first model. A small/medium/large mixture can simplify it
if clear size modes exist. Do not automatically use a normal distribution: it can
generate negative or implausibly large packet lengths. If $A$, $B$, and $W$ appear
dependent, independently fitted marginals will not reproduce their joint behavior.

Fit candidate parameters to one portion of a stable capture; compare against a
held-out portion or a repeated run. For a simple exponential fit, mean gap is enough
to estimate $\lambda$, but agreement of means alone is not model validation.

### Upgrade when bursts or state changes persist

Use an **On–Off source** when traffic repeatedly alternates between busy and quiet
periods. Choose a transparent state rule on binned packet count or bit rate, document
window width and threshold, and estimate empirical ON/OFF durations. Candidate
sojourn-time distributions include exponential, lognormal, or empirical resampling.
During ON, use a packet process suited to the measured data: periodic plus jitter for
near-regular audio, or variable packet counts/sizes for video. OFF can have zero packets
or a small keepalive process if observed. If ON and OFF durations show strong
dependence, do not assert an i.i.d. renewal-cycle model.

A **Markov-modulated model** is a compact alternative. In fixed slots of width
$\Delta$, let $S_n\in\{0,1\}$ be low/high activity. Estimate transition probabilities
from state transitions, for example

$$
\hat p_{01}=\frac{n_{01}}{n_{00}+n_{01}},\qquad
\hat p_{10}=\frac{n_{10}}{n_{10}+n_{11}}.
$$

Given state $s$, model slot packet count $B_n$ by a Poisson, negative-binomial, or
empirical distribution according to its observed variance and zero frequency. Model
packet sizes $W_{n,k}$ conditionally on state when size and activity are related.
This is a **Markov-modulated count process**. A standard continuous-time **MMPP**
instead switches the rate of a Poisson arrival process; use that name only when its
assumptions match the model actually generated. For speech with a near-periodic packet
every ~20 ms during activity, On–Off with periodic ON emissions can be more faithful
than a Poisson ON state, as discussed in Lesson 4.

> [!warning] Keep model complexity tied to evidence
> Start with $B=1$ plus a simple $A$ and $W$ model. Add batches, states, conditional
> sizes, or within-batch timing only when plots show a failure that the addition fixes.
> State a limitation you retain, such as encrypted media classes you cannot identify.

## 9. Generate a synthetic trace

Write down the exact generative order. Examples:

**Packet-event baseline**

1. Draw $A_i>0$ from the fitted gap model.
2. Set $\tau_i=\tau_{i-1}+A_i$ and $B_i=1$.
3. Draw packet size $W_{i,1}$ from its fitted distribution (or condition it on state).
4. Stop when $\tau_i$ reaches the same duration as the measured stable phase.

**On–Off or state model**

1. Generate state durations or Markov state transitions using fitted parameters.
2. Generate arrivals/counts according to the current state.
3. Generate $B_i$ and each $W_{i,k}$, preserving measured dependencies where needed.
4. If events represent batches or slots, assign **within-batch packet times** using a
   stated rule before comparing packet-level inter-arrivals.
5. Stop at the same observation duration; use a fixed random seed for repeatability,
   then repeat with other seeds to assess stochastic variation.

For the packet-level trace, sort synthetic times and recalculate packet gaps exactly
as for the real trace. Do not compare real **packet** gaps with synthetic **batch-event**
gaps: they are different variables. With bit-valued weights, compare the model's
predicted mean rate

$$
\hat G_{\mathrm{model}}\approx
\frac{E\left[\sum_{k=1}^{B_i}W_{i,k}\right]}{E[A_i]}
$$

against total synthetic bits/duration and empirical bits/duration. If states, batch
size, and weight are dependent, use the **joint reward** expectation; do not replace
it with $E[B]E[W]$ without checking independence.

## 10. Compare real and synthetic data

Put both traces through the **same** phase selection, size definition, binning,
clustering, and plot code. Useful comparisons:

1. Packet-time raster or packet-size-versus-time scatterplots over equal-length
   windows. Do clusters, regular spacing, and quiet periods look similar?
2. Empirical versus simulated CDFs for packet gaps, batch sizes, and packet sizes.
   A Q–Q plot reveals tail failures that a mean hides.
3. Boxplots or quantile tables for each variable, including high quantiles of gaps
   and sizes. Mark any truncation or maximum packet-size effect.
4. Bit-rate traces at **20 ms, 100 ms, and 1 s** (adjust if those scales obscure the
   data). Compare mean, peak-to-mean ratio, and quiet/active durations.
5. Serial correlation or Fano factor of count windows. A simulated trace with the
   right marginal gap CDF but no burst correlation is still a weak source model.

If a model fails, name the **specific** failure and change only what addresses it:
large missing peaks suggest state/batch structure; wrong packet sizes suggest a better
$W$ model; long missing pauses suggest an ON/OFF duration or gap-tail problem.
Keep at least one simple baseline to show what the added complexity achieves.

## 11. Concrete sequence to follow

- [ ] Choose uplink or downlink, Zoom client/interface, and one target phase.
- [ ] Capture a baseline plus controlled media changes; save raw pcapng.
- [ ] Identify candidate conversations from timing, byte counts, and phase changes.
- [ ] Freeze and record the exact direction/flow filter.
- [ ] Export timestamps and one consistently defined packet-size field.
- [ ] Inspect $A_i^{\mathrm{pkt}}$, $W_i$, rate at several time scales, and correlation.
- [ ] Start with $B_i=1$; introduce batch/slot definitions only if evidence supports them.
- [ ] Fit one baseline and, if needed, one state-aware model; note assumptions.
- [ ] Simulate equal-duration traces with fixed seed and repeat runs.
- [ ] Compare packet-level variables and time-series behavior using the same analysis.
- [ ] Preserve parameter values, filter, phase timeline, units, and model limitations.

Raw pcapng may contain other applications' traffic and connection metadata. Keep it
private; share only the filtered or aggregated data needed for coursework.
