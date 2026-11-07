# Lesson 9 — Visual inventory and source coverage

Destination: `../9. Exercises and call admission control - Integrated notes.md`.
All six handwritten pages were inspected as rendered images. All source visual groups below are embedded in the destination; compound drawings retain their panels and annotations. Crops and the exact redraw were visually inspected.

| Source page | Section / visual group | Asset | Destination |
|---|---|---|---|
| 1 | 1): input buffer, token bucket, forwarding gate | `01-token-bucket-scheme.png` | Exercise 1, setup |
| 1 | 1): triangular input, shaded token areas, initial token-content sketch and annotation | `02-triangle-first-analysis.png` | Exercise 1, average and token accumulation |
| 1 | 1): final superimposed input/output over two periods and token-content sketch | `03-triangle-output-and-tokens.png` | Exercise 1, output rate |
| 2 | 1): input-buffer occupancy and question about constant token content | `04-triangle-input-buffer.png` | Exercise 1, input backlog |
| 3 | 2): leaky bucket filter with buffer and output link | `05-leaky-bucket-scheme.png` | Exercise 2, setup |
| 3 | Answers: periodic ON–OFF rate, duration labels and equivalent server | `06-on-off-input.png` | Answer 1 |
| 3 | Answers: queue trajectory, slopes, maximum occupancy | `07-leaky-bucket-buffer.png` | Answer 2 |
| 4 | Max delay: arriving traffic and queue ahead of server | `08-delay-scheme.png` | Answer 3 |
| 4 | Output activity: superimposed rates, queue trajectory, drain interval and total activity interval | `09-leaky-bucket-output-and-buffer.png` | Answer 4 |
| 5 | CAC: both source-pattern examples | `10-cac-source-patterns.png` | CAC, source model |
| 5 | CAC: three admitted sources, candidate source, shared buffer and link | `11-cac-multiplexer.png` | CAC, architecture |
| 5 | CAC: branching classification and efficiency annotation | `12-cac-strategies.png` | Stochastic Bound |
| 6 | CAC: separate TBFs, multiplexing, common buffer and link | `13-shaped-sources.png` | Deterministic Bound, Example |
| Derived from pp. 1–2 | Exact normalized fluid trajectories: input/output, tokens, input backlog | `14-triangle-exact.png` | Exercise 1, after original output sketch |

The source plots of exercise 1 are qualitative: the exact parabolic storage curves and correction notes accompany them. The source drawings remain visible so their annotations and intermediate construction survive. No supplementary-book figures are used: those figures concern the statistical analysis deferred to the next lecture.

## Transcript and supplementary-material coverage

| Source | Coverage | Placement |
|---|---|---|
| `1 27 ott 2026, 08-48.transcript.txt`, 00:00:00–00:09:21 | Correction of the periodic triangular formula | Exercise 1, opening |
| Same, 00:09:30–00:24:07 | Mean rate, token accumulation, exhaustion, buffering, output and cycle reset | Exercise 1 |
| Same, 00:24:15–00:31:28 | LBF problem statement and interpretation of time fractions | Exercise 2, setup and answer 4 |
| Same, 00:31:45–00:38:48 | Minimum service rate, deterministic versus random cycles, buffer maximum and capacity | Answers 1–2 |
| Same, 00:39:07–00:45:59 | Fluid versus packet delay, drain time and output activity | Answers 3–4 |
| Same, 00:46:16–00:46:53 | Questions, Moodle practice and break | No new technical content |
| `2 27 ott 2026, 09-56.transcript.txt`, 00:00:00–00:09:21 | CAC role, resource manager, source/link model and two guarantee types | CAC introduction and Stochastic Bound |
| Same, 00:09:22–00:13:05 | Peak-rate admission and low-utilization example | Deterministic Bound, Example |
| Same, 00:13:11–00:20:09 | TBF parameters, aggregate rate/buffer conditions and their meaning | Same example |
| Same, 00:20:21–00:24:18 | Numerical admission limits and deferred statistical treatment | Same example, correction note |
| `5a-CAC.pdf`, PDF pp. 1–4, printed pp. 17–20 | Introductory context, deterministic criteria, numerical cross-check and conformance caveat | CAC only; supplementary caveat explicitly labeled |

All transcript parts were read. Later book material (statistical tail bounds, effective bandwidth and streaming-buffer dimensioning) was excluded to match the lecturer's stopping point and the user's explicit scope constraint.

## Corrections checked against sources

- Token-content maximum: `G_p T/16`; variable-rate depletion requires an integral.
- Token/input-buffer sketches: straight segments are qualitative; exact storage curves are parabolic.
- LBF maximum-delay numerator: queue at `T_ON`, not `T/2`.
- LBF active duration: `delta = T_ON + T_fw`, not the full ON–OFF period.
- CAC burst: stated `T_ON = 1 ms` gives about `1 kbit`; the handwritten `20 ms` substitution is inconsistent with this example and its admission count.
- Random OFF durations in the book are distinguished from fixed durations in the classroom introduction.

No unreadable original visuals or unresolved substantive contradictions remain; source mistakes are retained in the image crops and corrected explicitly in the prose.
