# Lesson 12 visual and source coverage

All six handwritten pages were inspected directly. Page numbers below refer to `../Lesson 12.pdf`. Figures are embedded in `../12. Sample means and Hoeffding’s inequality - Integrated notes.md`.

|Source page|Visual / meaningful annotation|Destination section|Asset or preservation|
|---|---|---|---|
|1|Two empirical-mean trajectories, colored sample points, reference mean and axes|Riprese da lezione 12|01-mean-paths.png; original crop, qualitative|
|1|Variance hyperbola|Riprese da lezione 12|02-variance.png; analytical redraw of variance divided by N|
|1|Two distributions for N=n0 and N=2n0, common mean|Riprese da lezione 12|03-mean-distributions.png; original crop, qualitative|
|2|Multiple distributions, shaded tails and mu ± a thresholds|Question from last lecture: how many samples...?|04-error-tails.png; original crop, qualitative|
|2|Chebyshev arrows and highlighted sample-count condition|Question from last lecture: how many samples...?|Full inequality chain and sufficient N transcribed in math|
|2|Arrival, blocked-call branch, admission box, network system and output|Example|05-cac-system.png; original crop|
|2–3|Illustrative arrival counts 131 and 98|Example|Both values transcribed; explanatory braces represented in prose|
|3|Four-estimator brace, crossed-out maximum, red requests for explanation|How do we compute the block prob.?|06-estimator-options.png plus four-row table and explanations|
|3–4|Pooled estimator algebra, arrow for equal arrival counts, limits to alpha|How do we compute the block prob.?|Classroom algebra and limits transcribed; extra domain commentary removed during transcript-only audit|
|5|Reminder juxtaposition of random mean, expectation, and repeated numerical means|Remind|All three expressions and their relationship transcribed|
|6|Monotonicity, positivity, independence and lemma arrows in proof|Proof of Lemma|Annotations integrated beside corresponding equalities and inequalities|
|6|Convex quadratic exponent|Proof of Lemma|07-convex-exponent.png; schematic analytical redraw|

## Heading coverage

Original headings and question labels retained in original order: Riprese da lezione 12; Question from last lecture: how many samples...?; Example; What value do we need?; How do we compute the block prob.?; Consider the first approach; How do we find N? (the bounds); Hoeffding’s Inequality; Remind; Proof [H2F]; Hoeffding’s Lemma; Hoeffding’s ineq.; Proof of Lemma. The short bracketed proof tag is retained as read from the handwriting; its expansion is not specified. The final application reports the lecturer's closing instruction without adding a numerical solution.

## Transcript coverage

Source: `../6 nov 2026, 12-31.transcript.txt`, read in full.

|Transcript interval|Integrated content|
|---|---|
|00:00:00–00:12:12|Observations versus random variables, repeated empirical means, expectation and variance of S_N, qualitative convergence|
|00:12:17–00:22:34|Error and confidence target, variance bound, Chebyshev sample count, conservative interpretation|
|00:23:32–00:35:35|Poisson calls, CBR rate, CAC, simulated versus real time, count measurements and single-run ratio; duration details omitted because the transcript is garbled|
|00:35:38–00:54:39|Four aggregation proposals, dispersion versus mean, unequal counts, unusual first run, equal-count calculation and limits|
|00:54:57–01:00:21|Accuracy example, equivalent probability statements, more data, rare events versus model violations, missing variance|
|01:00:25–01:08:49|Hoeffding statement, corrected N squared, interval width, one and two tails, exponential decrease|
|01:09:00–01:16:48|Break and partly unintelligible side exchange; no mathematical claims inferred from garbled speech|
|01:16:48–01:18:44|Reminder distinguishing random estimator and fixed expectation|
|01:18:53–01:24:06|Hoeffding lemma and its boundedness condition, inequality proof setup|
|01:24:51–01:39:23|Exponential transform, Markov, product factorization, lemma, convex minimization, corrected factor eight, substitution|
|01:39:28–01:41:47|Opposite tail, factor two, application with width one|

## Transcript-only audit requested by the user

The note was revised against the entire transcript to retain the lecturer's explanations, classroom formulas and original figures. Section timestamps were added for traceability. Mathematical symbols corrupted by speech recognition are written consistently with the original handwritten formulas; this is not a verbatim transcript.

Removed additions not explicitly taught in the transcript:

- Finite-run bias, initialization effects, comparison between expectations of ratios and ratios of expectations.
- Zero-arrival probabilities and proposed conditioning policies.
- Standard-deviation scaling example requiring four times as many samples.
- Integer rounding prescription for the Chebyshev count and appendix-based tightness discussion.
- The exponential-duration parameterization and mean duration: the spoken passage at 00:24:23–00:24:47 is not intelligible enough to verify these details from this transcript.
- Extra weighted-average derivation and hypothetical examples comparing the estimators beyond the classroom example.
- Extensions to non-identically distributed variables, non-strict inequality boundaries, deterministic zero-width cases, and capping bounds at one.
- Second derivative, expanded substitution algebra skipped by the lecturer, and a separate construction with negated variables for the left tail.
- The derived sample-count formula and numerical answer 26492: the lecturer says to apply the bound with interval width one (01:40:08–01:40:39), but does not state this number.

The earlier course-appendix addition has been removed from the study note. The bracketed handwritten proof tag has no supplied expansion. No teaching content was reconstructed from the unintelligible break exchange. No audio-level verification is claimed: this audit compares the supplied transcript, with the original handwritten notation retained for formulas and figures.

## Regeneration

`prepare_figures.py` uses PyMuPDF for five original crops, and Matplotlib/NumPy for two redraws. Run normally when all dependencies share an interpreter, or use `--crops-only` and `--plots-only` in separate environments. Crop bounds refer to the directly inspected 1273 × 1800 page previews and render at 3 pixels per PDF point. No random samples or empirical data are generated.
