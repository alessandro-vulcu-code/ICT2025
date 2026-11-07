# Visual inventory and source coverage

All source pages inspected directly from rendered PDF. All nine redraw files embedded in the integrated note; compound figures retain distinct stages. Schematic paths and densities are illustrative, not recovered data. Corrections are explained in the note.

|Source page|Original visual / section|Destination|
|---|---|---|
|1|Users → buffer B → link C / Problem|01-system.png|
|1|Time axis, slots and arrival arrows / Problem|02-slots.png|
|2|Original density, centered right tail, centered two tails / no buffer|03-centering-tails.png (three panels)|
|2|Symmetric density and mean axis / no buffer|04-symmetry.png|
|3|Two separated density concentrations / bound comparison|05-irregular.png|
|3|Buffered system with loss branch / restoring buffer|01-system.png, reused with caption identifying loss event|
|4|Empty-buffer resource region, stability boundary, choice guides / q_i=0|06-empty-region.png|
|4|Family of resource boundaries / q_i=alpha B|07-alpha.png; common service-axis intercept corrected|
|4|Queue step path and initial transient / dynamics|08-queue-paths.png, upper panel|
|4|Unreflected and reflected step paths, negative credits / dynamics|08-queue-paths.png, lower panel|
|5|Orange tradeoff line with candidate points and reference vertical / final heuristic|09-heuristic.png|

Source headings retained in order: Markov Inequality; Chebishev; Problem. Handwritten transitions retained as subsections. Later untitled derivation divided into explanatory subsections.

Transcript Lesson 11: 00:00–00:07 setup and bounds; 00:07–00:22 exercise work/background conversation (no additional reliable mathematical derivation); 00:22–00:30 no-buffer/Markov; 00:30–00:40 Chebyshev and tail geometry; 00:40–00:48 comparison and corrected crossover; 00:48–00:54 buffered event and dependence; 00:54–01:00 empty-state design; 01:00–01:06 alpha and sign correction; break until 01:15; 01:15–01:25 recursion/reflection; 01:25–01:33 moment attempt; 01:33–01:35 mean substitution heuristic. All mathematical segments covered. Whisper slips reconciled against handwritten equations.

Lesson 10: integrated note and both transcripts consulted for Markov assumptions, transformed-variable derivation of Chebyshev, two-tail interpretation, tightness and sufficient-bound design. Course appendix §B.3, PDF pp. 1–3 inspected in text for these statements. No new appendix figure used. Chernoff is not developed in this lesson and is not imported.

Regeneration: run redraw_plots.py with Python containing NumPy and Matplotlib (NumPy trapezoid API). Plot source contains no empirical data. Quantitative region plots follow equations; other plots explicitly schematic.
