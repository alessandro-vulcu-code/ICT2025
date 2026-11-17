---
name: summarize-game-theory
description: Summarize Game Theory lesson PDFs and optional professor transcripts into concise English Markdown notes with direct explanations, bullet points, source figures, and explicitly attributed exercises. Use for preparing or rewriting this repository's Game Theory lesson notes.
---

# Summarize Game Theory

Create source-faithful notes that teach a beginner and support solving problems during a **75-minute written exam with printed material allowed and electronic devices forbidden**. This exam format is user-provided context, not a claim about current university regulations. Explain the material directly and fluidly, without adding supplementary theory.

## Inputs and scope

- Accept a lesson folder or a PDF/transcript inside it; inspect the containing folder for companion sources. Locate the repository's `Game Theory/` directory rather than hard-coding absolute machine paths.
- Expect a lecture PDF, sometimes accompanied by one or two online-lecture transcripts. Some folders contain multiple PDFs. Compare titles and content with transcripts before deciding which sources cover which topics: folder numbers, PDF numbers, and recording numbers can differ. Do not silently discard a PDF because it does not match a recording; summarize distinct supplied lesson material under clearly separated topics unless the user requests narrower coverage.
- Read every relevant slide and transcript, not only headings or initial pages. Use PDF text extraction plus rendered inspection for visual content and equations. If a source is unreadable, state the gap rather than claiming complete coverage.
- Use the lecture PDF as the backbone for topics, notation, and coverage. Integrate the professor's transcript where it explains, clarifies, or supplements that material. These are the primary sources: do not expand the lesson with outside theory, unrelated background, or extra notes. Make only the minimal clarifications needed to understand the supplied material. Missing transcripts do not block work. Do not infer what was said in person. Merge overlapping recording segments, remove repetition and administrative chatter, and reconcile transcription errors against slides and mathematics.
- For material conflicts, preserve the distinction between sources and label necessary, justified mathematical corrections briefly. Do not turn these corrections into extended digressions. Never silently turn an uncertain transcription into a theorem or formula.
- Use `Game Theory/Game Theory. A Handbook of Problems and Excercises.pdf` only as a supplementary exercise source; preserve the actual filename spelling. Search relevant sections when an exercise is useful for the requested lesson. Do not use the handbook to expand the theory covered by the PDF and transcript. If unavailable, continue with lecture sources; do not automatically replace missing handbook exercises with invented practice.
- Process the requested lesson or batch only. Do not automatically rewrite the first five lessons, alter original PDFs/transcripts, or generate a whole-course textbook.

## Teaching and writing

The student has **no Game Theory background and missed the first five lessons**. Do not assume familiarity with players, actions, strategies, payoffs, best responses, equilibrium, probability notation, or optimization conventions.

- Write notes entirely in **natural, clear English**, using complete sentences. Ignore conversational shorthand or caveman style when writing the study artifact. Keep terminology consistent; avoid inflated prose and repeated summaries.
- Explain concepts directly. Avoid source-narration filler such as “In the lecture it is explained that...”, “The professor explains...”, “The slides introduce...”, or “The central question becomes...”. State the explanation itself; put provenance in concise source references, captions, or exercise labels instead.
- Use short, connected paragraphs for explanations. Introduce related terms where they naturally matter in the explanation; do not stack glossary-like definitions, such as “A player is... An action is... An outcome is... A payoff is...”, in a single paragraph. Explain how concepts relate through the lesson's example or reasoning. Use bullet points for genuinely parallel items, properties, assumptions, or distinctions, and numbered lists for ordered solution steps. Avoid both long walls of prose and lists that break one coherent explanation into fragments.
- Do not interrupt explanations with rhetorical questions or alternate questions and answers. Use declarative headings and direct statements. Questions belong only to actual exercise prompts. Turn rhetorical questions from the sources into direct explanations rather than copying their question-and-answer framing.
- Add a short **Prerequisites you need** bridge only when earlier concepts are essential to follow the lesson. Keep it minimal and grounded in course material. Inspect earlier course sources when necessary to recover conventions. Define symbols at first use, including payoff order and what each probability conditions on.
- Introduce a central concept with its meaning and intuition, then give its precise definition or formula and any application present in the sources. Put important definitions in Obsidian callouts such as `> [!info] Definition — Nash equilibrium`.
- For a theorem, state the source's assumptions, conclusion, and meaning. Include proof reasoning when present in the PDF or transcript; explain its steps without adding an independent proof or a new result. Condense peripheral formal detail.
- Prioritize the concepts, assumptions, solving procedures, distinctions, and failure cases covered by the PDF and professor's transcript. Concision must not remove steps needed by a beginner or omit important lecture topics. Do not add background, commentary, or generic study advice to fill out the note. No rigid word/page quota.
- Explain relevant distinctions explicitly when they arise in the actual lesson, for example action versus contingent strategy or pure versus mixed strategies. Do not introduce later concepts merely to compare them with the current topic.

## Worked examples and practice

- Work through examples and exercises present in the lecture PDF or professor's transcript. Do not require a new example for every concept or generate additional practice by default. Reuse a source example across related ideas when useful without changing its assumptions.
- State the provenance **beside every example or exercise**. Label lecture material **Lecture example** or **Lecture exercise**, with the PDF filename and page or transcript reference. Label handbook material **Handbook exercise**, with the verified chapter, exercise number/title, and page. Distinguish printed pages from PDF page indices when they differ.
- If an invented example or practice problem is requested or indispensable for a minimal clarification, label it **Original example — invented, not from the lecture or handbook** or **Original practice — invented, not from the lecture or handbook**. Do not present it as the professor's exercise or a past exam question. If changing a source exercise's assumptions, numbers, or questions, label it **Adapted example** and identify both the source and the changes.
- Explain the situation, players, choices, information, and payoffs in connected prose before calculating. Use numbered steps when solution order matters. Show why a method applies, essential intermediate calculations, final answer, and interpretation. Define strategy and payoff ordering explicitly. Distinguish a solution worked out for the note from a solution supplied by the professor or handbook.
- Check results against definitions: profitable deviations for equilibria, feasibility and boundaries for optimization, probability bounds and unused-strategy inequalities for mixing, and sequential incentives at off-path subgames when relevant. Do not claim a complete equilibrium set after finding only some candidates or only pure equilibria.
- Include counterexamples and common mistakes when covered by the sources; do not append an extra collection of warnings or edge cases. Avoid unexplained jumps such as “clearly” in place of reasoning.
- Include a small selection of handbook exercises only when useful for the requested lesson or explicitly requested, with their origin clearly labeled. Provide a brief solution route or worked solution where useful; keep unsolved prompts separate from answers. Never fabricate exercise references, claim an unverified solution is official, or invent exam frequency or authoritative time estimates.

## Figures from PDFs

Include explanatory visual content: payoff matrices, game trees, information sets, graphs, and diagrams. Select figures that materially help understanding; avoid decorative images and repetitive incremental slides.

1. Render the relevant PDF page, inspect it, and identify a tight crop retaining labels, legends, payoff tuples, and assumptions needed to read it. For vector diagrams or mixed text/graphics, render a clipped page region rather than relying on embedded-image extraction.
2. Save images under the lesson's `Pics/` directory. Use names such as `gth2009-p25-subgames.png` to preserve provenance and avoid collisions across PDFs. The bundled `scripts/crop_pdf.py` provides deterministic PNG crops using PyMuPDF; run `--help` for usage. Coordinates are PDF points in rendered page orientation, with origin at top left and page numbers starting at 1.
3. Inspect each saved crop at readable size. Avoid clipped branches, missing labels, large margins, tiny text, and page headers. Explain the figure beside it, with descriptive alt text and a caption naming source PDF and page.
4. A clean redraw is permitted when it improves readability or consistency. Prefer deterministic drawing tools for mathematical diagrams. Preserve choices, edges, information sets, probabilities, terminal payoffs, and payoff order; distinguish source facts from added annotations. Label it **Redrawn from [PDF, page]** and compare visually and mathematically with the original. An attractive but changed game is incorrect.

Example invocation:

```bash
python3 /path/to/summarize-game-theory/scripts/crop_pdf.py "/path/to/Gth2009.pdf" --page 25 --box 50 85 700 510 --output "/path/to/Lesson 11/Pics/gth2009-p25-subgames.png"
```

Coordinates above are illustrative; measure the actual page. PyMuPDF (`fitz`) is required. If missing, use available PDF rendering tools or report the dependency gap; do not leave fake image links or claim images were produced.

## Output and paper exam use

- Save an English Markdown note inside the lesson folder, normally `{lesson number}. {Topic}.md`, following repository conventions. Reuse the existing main note when asked to rewrite it, preserving unrelated user additions. Keep original sources intact.
- Organize by the concepts and methods in the supplied sources, not slide-by-slide narration. Use declarative headings, fluid paragraphs, selectively placed lists, source examples, and figures. Add prerequisites, practice, or an **Exam quick reference** only when they serve the actual lesson; do not fill a template with extra material.
- If including a quick reference, condense only formulas, assumptions, and solution procedures already explained from the sources. Use short bullet points or a small table with declarative problem cues, not rhetorical questions. State variable meanings locally so it works on paper; do not add new theory or generic exam advice.
- Use standard Markdown headings and tables, `$...$` inline math, and `$$` display math on separate lines. Use relative Markdown image links with angle brackets around paths containing spaces, keeping assets portable and exportable. Essential explanations must remain visible when printed; no hover-only text, collapsed answers, or links as substitutes for content.
- Ensure diagrams work in grayscale: labels, shapes, or line styles must supplement color. Do not rely on interactive visualizations or Obsidian-only features for essential reasoning.
- Include a short source list and lightweight section/figure page references. Distinguish PDF page indices from printed handbook page numbers when they differ. Transcript timestamps help resolve ambiguous claims but are not required on every paragraph.
- Markdown and local images are default deliverables. Produce a printable PDF only when requested; if producing one, render and inspect it for broken formulas, unreadable diagrams, and split tables.

## Completion checks

Check coverage against selected PDFs and transcripts, mathematical consistency, example calculations, theorem assumptions, exercise provenance, image existence and readability, and relative link resolution. Remove source-narration filler, rhetorical questions outside exercise prompts, glossary-like definition dumps, unbroken walls of prose, and unsupported additions. Keep related explanations fluid; use lists only when they improve clarity. Confirm that each non-lecture example is visibly labeled and every handbook reference is verified. Check that any prerequisites are minimal and any quick reference condenses existing content. Report created/updated paths and genuine source gaps briefly, without guaranteeing exam coverage or success.
