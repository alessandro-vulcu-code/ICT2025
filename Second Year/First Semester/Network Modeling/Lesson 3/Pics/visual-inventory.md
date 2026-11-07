# Lesson 3 source and visual inventory

Output: `../3. Network abstraction and renewal processes - Integrated notes.md`.

## Source review

- `../Lesson 3-notes.pdf`: all seven handwritten pages rendered and inspected directly. Page 7 has only the heading “Elementary renewal theorem”.
- `../1 6 ott 2026, 08-33.transcript.txt`: all 1338 lines read, covering 00:00:00–00:55:32.
- `../2 6 ott 2026, 09-52.transcript.txt`: all 392 lines read, covering 00:00:00–00:23:39. The recording starts during the point-process explanation and ends after the examples of dependence within renewal-reward pairs.
- `../Lesson3-book.pdf`: all five pages read through text extraction; relevant PDF pp. 2–4 inspected visually. Used to reconcile terminology and identify the counting-boundary difference, not to introduce topics absent from the lecture.
- `../L01-Slide-Intro-to-Modeling.pdf`: text of all 15 slides inspected. The deck concerns the earlier introduction to modeling; no additional slide-only teaching content or figures were imported into this note.

The user's standing constraint is lecture-only content. No independent calculations, chosen distributions, additional theorem statements, or supplementary textbook examples were added.

## Visual coverage

Coordinates and page indices for the crops are recorded in `extract_figures.py`. All eight original crops remain available for comparison. The note now embeds eight code-generated redraws, each with a source caption. Every redraw is saved as PNG and editable SVG with the `-redrawn` suffix.

|Source page|Original visual or meaningful annotation|Destination|Preservation|
|---|---|---|---|
|1|Data generator, CAC, resource manager, scheduler, switching elements, end user; solid and red dotted connections|Main modules|01-network-modules-redrawn.png|
|1|Highlighted four elements of network abstraction|Network Abstraction|Four-item definition list, including the RM description missing in the handwriting|
|2|Demand examples, bottleneck annotation|Resources and Requests|10/6 Mbps example and explanatory source-discrepancy callout for the watcher values|
|2|RM arrows to centralized/distributed; allocation-vector annotation|RM (Resource Management)|Both management labels and allocation-vector definition transcribed; no unsupported explanation of their implementation added|
|2|Red feasibility and PLP conditions|RM (Resource Management)|Both equations preserved in comparison table|
|3|Unfinished probability-example coordinate axes|Ex|02-demand-axes-redrawn.png, explicitly identified as unfinished; no curve invented|
|3|Conditional-probability branches|Ex|Both cases written as piecewise distributions, with spoken and handwritten discrepancies explained locally|
|3|Efficiency derivation and 98% annotation|Ex|Original classroom efficiency and expectation calculation transcribed|
|3|Equal-sharing allocation, D/W labels|Ex|Both allocation components and class meanings preserved|
|4|Three downloader utility curves, colors and label|Utility functions|03-downloader-utilities-redrawn.png, qualitative redraw|
|4|Watcher utility with minimum allocation and 2 Mbit threshold|Utility functions|04-watcher-utility-redrawn.png, qualitative redraw|
|4|Company topology, employees, shared 10 Mbps link and Internet|Examples|05-company-network-redrawn.png|
|5|Video-call utility, thresholds 0.5 and 1.5, plateau at utility 1|Utility functions = ?|06-videocall-utility-redrawn.png|
|5|Multiple blockage curves, highlighted alternative, capacity axis, circled 10 Mbps design point|Utility functions = ?|07-blockage-curves-redrawn.png; no numerical blockage result inferred|
|5|Counting staircase, arrival times, interval arrows, labels and ellipsis|Point process|08-counting-process-redrawn.png; original zero-based labels retained, with index-convention note|
|6|Constant-interarrival and dependent-interarrival examples|Renewal Process|Both examples transcribed; no uniform law assumed for “random between 0 and 1”|
|6|Renewal-reward sum, paired interarrival/reward annotations|Renewal-reward Process|Sum, i.i.d. pair requirement, and possible within-pair dependence explained|
|7|Elementary renewal theorem heading only|Elementary renewal theorem|Heading preserved; missing statement explicitly identified|

Redraws preserve source labels, color distinctions, arrows, breakpoints and relationships. Source 6 has recoverable numerical breakpoints and is drawn exactly from those values. Utility alternatives and blockage candidates are schematic Bezier drawing paths, not fitted functions or sampled data. Their normalized control points specify layout only. The blockage axis is explicitly not to scale; no numeric blockage probability is asserted. The counting sketch preserves event order, unequal schematic gaps, initial drawn offset and zero-based labels, without assigning numerical arrival times. The unfinished demand axes remain empty.

## Section order

Original headings and labels retained in order: How to build a network model; Main modules; Network Abstraction; Users; Resources and Requests; RM (Resource Management); Ex; Utility functions; System utility; The problem; Examples; Utility functions = ?; Network; Point process; Renewal Process; Renewal process; Renewal-reward Process; Elementary renewal theorem. Handwritten capitalization has been normalized to sentence case where appropriate; wording is retained.

## Transcript-to-section coverage

|Source interval|Destination/content|
|---|---|
|Part 1, 00:00:04–00:07:39|Main modules, admission example, allocation versus scheduling, queues, QoE, course roadmap|
|Part 1, 00:07:43–00:10:11|Network Abstraction: purpose and four elements|
|Part 1, 00:10:13–00:13:19|Users: downloaders and watchers, completion time versus smoothness|
|Part 1, 00:13:26–00:20:35|Resources and Requests: capacity, demands, two links and bottleneck|
|Part 1, 00:20:43–00:22:42|RM: allocation notation and feasibility|
|Part 1, 00:22:44–00:34:14|Ex: nominal/actual demand, conditional probabilities, airline utilization, overbooking and PLP|
|Part 1, 00:34:23–00:36:59|Equal sharing, 15 downloaders/five watchers, stated allocations, need for utility|
|Part 1, 00:37:05–00:41:05|Utility functions and alternative qualitative curves|
|Part 1, 00:41:07–00:42:53|System utility, weighted aggregation and customer classes|
|Part 1, 00:42:55–00:44:35|The problem: maximize utility subject to feasibility and minimum service; possible infeasibility|
|Part 1, 00:44:41–00:55:18|Company example, user/resource identification, 0.5/1.5 Mbps utility, blockage-capacity relationship|
|Part 2, 00:00:00–00:08:55|Point-process representations, index warning, batches, workloads and aggregate offered rate|
|Part 2, 00:09:11–00:17:07|Renewal and Poisson distinction, homogeneity, machine/web examples, constant and dependent intervals|
|Part 2, 00:17:19–00:17:51|Formal renewal definition|
|Part 2, 00:17:55–00:23:35|Renewal-reward definition, i.i.d. pairs, why both processes are needed, correlation examples|
|Part 2, 00:23:39|End of recording; elementary renewal theorem not stated|

Classroom interruptions, jokes and unrelated exchanges are not study-note content.

## Unresolved or explicitly corrected readings

- Booked customer: transcript first says 0.01 for absence, then explicitly says 2%; handwriting gives 0.02. The note follows the lecturer's explicit 2% clarification, paired with 98% attendance.
- Unbooked customer: transcript gives 0.01/0.99; handwriting gives 0.001/0.999. Both readings are identified; the main displayed pair follows the spoken values.
- Watcher request: handwritten 3/2 Mbps differs from the spoken 2/2 Mbps discussion. Difference is retained in a local note.
- Counting process: lecturer warns about switching zero/one-based indices. Original figure labels and handwritten strict comparison are retained and distinguished from the book's non-strict comparison. The shifted figure is not used to infer an initial condition.
- “After time t” in the automatic transcript is inconsistent with the spoken counting demonstration and source definition. The note uses “up to t” and explicitly records the issue.
- Elementary renewal theorem: neither an enunciation nor a proof occurs in the supplied transcripts. Nothing has been imported from the book to fill that heading.

No audio recording was supplied in the folder, so no audio-level verification is claimed.

## Regeneration

`redraw_figures.py` regenerates the eight embedded PNG figures and corresponding SVG vectors using Matplotlib. Run it with an interpreter that has Matplotlib installed. Every final redraw was visually compared with its source crop; labels and paths were checked for clipping. Original PDF and crops were preserved.


Run `python3 extract_figures.py` from this folder or any working directory. Requires PyMuPDF. Crops are rendered at three pixels per PDF point from the original PDF, using bounds specified relative to the inspected 1273 × 1800 previews.
