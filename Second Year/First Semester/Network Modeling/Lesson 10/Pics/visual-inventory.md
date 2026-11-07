# Lesson 10 — Visual inventory and source coverage

Destination: `../10. Stochastic CAC and probability bounds - Integrated notes.md`.

All six handwritten pages were rendered and inspected directly. Every original meaningful visual group below is embedded in the destination. Crops were visually checked, including both panels of the transformation examples. The exact redraws preserve recoverable probabilities and correct errors explicitly discussed in the text; qualitative source sketches remain visible.

| Source page | Original visual group | Asset | Destination |
|---|---|---|---|
| 1 | CAC, source group, shared resource and small buffer symbol | `01-cac-recap.png` | Opening recap |
| 1 | Queue/server and the two service-rate conditions | `02-queue-stability.png` | Opening recap, equality discussion |
| 1 | Input fluctuations, service margin, shaded accumulated traffic and annotation | `03-service-margin.png` | Opening recap, service margin |
| 1 | Two random rates with equal means, shaded differences and vertical interval markers | `04-equal-mean-random-rates.png` | Opening recap, lost spare capacity |
| 2 | Deterministic constraint brace, arrow to stochastic CAC, sources/buffer/link | `05-stochastic-cac.png` | Stochastic CAC |
| 2 | Qualitative tail, Markov curve, level one and mean threshold | `06-markov-tail-sketch.png` | Markov inequality |
| 2 | Gaussian density with mean and density annotation | `07-gaussian-sketch.png` | Ex: Gaussian applicability discussion |
| 3 | Step auxiliary variable and diagonal comparison | `08-markov-proof.png` | Markov, Proof |
| 3 | Both panels: admissible transformation examples and counterexamples | `09-transformation-functions.png` | Corollary |
| 4 | Asymmetric density with both shaded tails and deviation thresholds | `10-chebyshev-tails.png` | Chebishev Bound |
| 4 | Transformation used in the proof | `11-chebyshev-transformation.png` | Chebishev Bound, Proof: |
| 5 | Exact exponential tail and two bound curves, including original annotations | `12-exponential-comparison.png` | Exponential comparison following proof |
| 5 | Circled class of variables with finite moments/variance | `13-moment-class.png` | Question by prof |
| 5 | Three-point probability-mass sketch | `14-three-point-pmf.png` | Question by prof, equality example |
| 5 | Discrete tail and touching upper bound, including endpoint markers | `15-tight-bound-tail.png` | Question by prof, equality example |
| 6 | Overflow target, bound implication and conservative-margin dimension line | `16-cac-bound-condition.png` | Chernoff Bound, concluding CAC connection |
| Derived from pp. 2, 4–5 | Corrected normalized exponential tail and bounds | `17-exponential-bounds-exact.png` | After original exponential comparison |
| Derived from p. 5 | Exact three-point PMF and tail, including central mass and endpoint values | `18-chebyshev-tight-example.png` | After original discrete-tail construction |

No supplementary PDF figures are used. Regeneration code for both exact plots is `redraw_plots.py`.

## Structural check

The first page has no section title: its recap and stability discussion remain opening prose. Subsequent original titles and their order are preserved: Stochastic CAC; Recall [Main Bounds of Statistical Analysis]; Markov inequality; Ex:; Proof; Corollary; Proof; Chebishev Bound; Proof:; Question by prof; Chernoff Bound. The original spelling “Chebishev” is retained in the heading, with the conventional name explained locally. Examples without separate original headings remain inside the surrounding section.

## Transcript coverage

| Source | Material | Placement |
|---|---|---|
| Part 1, 00:00:04–00:00:36 | Homework and introductory questions | No new lesson theory |
| Part 1, 00:00:45–00:05:02 | CAC recap, TBF conditions, warning that the CAC draft has errors | Opening recap; book claims cross-checked rather than assumed correct |
| Part 1, 00:05:27–00:17:02 | Equality with TBF; stochastic queue critical load; finite buffers; shaded rate differences and unused service | Opening recap |
| Part 1, 00:17:16–00:24:44 | Conservative deterministic CAC, violation risk, overflow target and upper bounds | Stochastic CAC |
| Part 1, 00:24:53–00:35:29 | Markov statement, tail sketch, exponential example and Gaussian caveat | Recall / Markov / Ex: |
| Part 1, 00:35:35–00:40:47 | Auxiliary variable, indicator and expectation proof | First Proof |
| Part 1, 00:40:54–00:48:59 | Monotonic transformation, examples, corollary and proof | Corollary / second Proof |
| Part 1, 00:49:06–00:56:10 | Chebyshev statement, tail interpretation and transformed-variable proof | Chebishev Bound / Proof: |
| Part 1, 00:56:16–00:57:48 | Break and questions | No new lesson theory |
| Part 2, 00:00:00–00:08:23 | Exponential example, shift by the mean, variance and bound comparison | After Chebyshev proof |
| Part 2, 00:08:33–00:19:19 | Finite-moment class, meaning of tightness, three-point distribution, equality and narrower classes | Question by prof |
| Part 2, 00:13:03–00:13:41 | Correction of exponential variance | Explicitly noted in exponential example |
| Part 2, 00:19:23–00:22:21 | Chernoff deferred; return to CAC and conservative bound dimensioning | Final original heading |

Both transcript files were read in full:

- `1 30 ott 2026, 12-40.transcript.txt`
- `2 30 ott 2026, 13-49.transcript.txt`

Supplementary source: `NDbook-Chapter-Appendix-RandomProcesses.pdf`, PDF pp. 1–3 (printed pp. 65–67), inspected for Markov assumptions, monotonic transformation, Chebyshev and tightness. Later material on independent sums and Chernoff (including PDF p. 4) was not imported because the lecturer defers it and the student's notes stop at its heading.

## Corrections and limitations carried into the note

- Thresholds dividing Markov/Chebyshev expressions must be positive.
- TBF deterministic constraints allow equality; this is distinguished from critical loading of unconstrained random queues.
- Epsilon concerns overflow/QoS violation in this example, not the distinct event of rejecting a candidate call.
- A Gaussian with a small negative tail does not satisfy exact Markov nonnegativity. The lecturer's heuristic is identified; a rigorous positive-part alternative is clearly a clarification.
- For a nondecreasing transformation with flat portions, event inclusion replaces the equality in the source proof; a positive denominator is required.
- Exponential variance is `1/lambda^2`; the lecturer corrects the verbal mistake.
- The unshifted exponential-tail Chebyshev denominator uses distance from the mean. The original curve label is corrected explicitly.
- The equality example uses `>=`, variance `1/2`, and probability `1/2` at threshold one; the redraw makes all atoms and endpoints explicit.
- The concluding overflow inequality is schematic: the lecture does not identify the queue variable/threshold or compute an admission count. This limitation is stated locally rather than filled with an invented CAC derivation.

Every original visual is available and embedded. No unreadable source figures remain.
