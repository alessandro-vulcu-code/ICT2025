# Lesson 13 visual inventory

Source: `../Lesson 13.pdf`. All six pages inspected directly. Destinations refer to `../13. Bounds recap, Chernoff bound and CAC - Integrated notes.md`.

|Source page|Visual or meaningful annotation|Destination|Handling|
|---|---|---|---|
|1|Probability-bound and MGF formulas; no standalone diagrams|Bounds recap and its subsections|Transcribed, with local corrections|
|2|Chernoff derivation and red question beside positive theta|4. Chernoff bound → Derivation|Equations transcribed; reason for theta > 0 explained|
|3|Blackboard photo: binary expectation and expectation of a function|Special case|All written formulas transcribed; photo deliberately not embedded, per user request|
|3|Compound plot: green exponent, dashed components, theta-star and maximum guide|Special case|`01-chernoff-maximum.png`; original sketch, caption clarifies linear component|
|4|Optimizer, algebraic grouping, KL identification and continuous definition|Special case|Equations and derivation transcribed; grouping explained in algebra|
|5|Sources → CAC → buffer B → link C|CAC again|`02-cac-system.png`|
|5|ON fraction brace and necessary-condition arrow|Book chapter: ON-OFF|Formula and condition explained in text|
|6|Bernoulli label and ceiling in binomial tail|If B=0|Transcribed with explicit binomial and strict-boundary corrections|
|6|Buffer B → link C|Easy part, now we add the buffer|`03-buffer-link.png`|
|6|Traffic trace, dashed capacity and both shaded excess excursions annotated B|Easy part, now we add the buffer|`04-excess-traffic.png`; retains both stages; axes identified from transcript|
|6|Joint loss event and queue-threshold conditions|Cong. Condition?|Transcribed; finite and virtual queues distinguished|

No supplementary figures imported: chapter material used here is its textual model and admission criteria. Numerical examples and subsequent buffered-queue derivations are outside this lecture's scope. `prepare_figures.py` reproduces the four crops directly from the source PDF.
