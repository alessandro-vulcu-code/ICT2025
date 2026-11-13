---
name: summarize-game-theory
description: Summarize Game Theory lesson folders containing lecture PDFs and optional transcripts into concise English Markdown notes with beginner explanations, worked examples, cropped figures, and a paper exam reference. Use for preparing or rewriting this repository's Game Theory lesson notes.
---

# Summarize Game Theory

Create notes that teach a beginner and support solving problems during a **75-minute written exam with printed material allowed and electronic devices forbidden**. This exam format is user-provided context, not a claim about current university regulations. Prefer useful explanations and solution methods over exhaustive transcription.

## Inputs and scope

- Accept a lesson folder or a PDF/transcript inside it; inspect the containing folder for companion sources. Locate the repository's `Game Theory/` directory rather than hard-coding absolute machine paths.
- Expect a lecture PDF, sometimes accompanied by one or two online-lecture transcripts. Some folders contain multiple PDFs. Compare titles and content with transcripts before deciding which sources cover which topics: folder numbers, PDF numbers, and recording numbers can differ. Do not silently discard a PDF because it does not match a recording; summarize distinct supplied lesson material under clearly separated topics unless the user requests narrower coverage.
- Read every relevant slide and transcript, not only headings or initial pages. Use PDF text extraction plus rendered inspection for visual content and equations. If a source is unreadable, state the gap rather than claiming complete coverage.
- Slides define topics and notation; transcripts add explanations, examples, and emphasis. Missing transcripts do not block work. Do not infer what was said in person. Merge overlapping recording segments, remove repetition and administrative chatter, and reconcile transcription errors against slides and mathematics.
- For material conflicts, preserve the distinction between sources and label justified mathematical corrections. Never silently turn an uncertain transcription into a theorem or formula.
- Use `Game Theory/Game Theory. A Handbook of Problems and Excercises.pdf` as the professor's exercise source; preserve the actual filename spelling. Search its contents and relevant sections instead of reading all exercises for every lesson. If unavailable, continue with lecture sources and label original practice problems clearly.
- Process the requested lesson or batch only. Do not automatically rewrite the first five lessons, alter original PDFs/transcripts, or generate a whole-course textbook.

## Teaching and writing

The student has **no Game Theory background and missed the first five lessons**. Do not assume familiarity with players, actions, strategies, payoffs, best responses, equilibrium, probability notation, or optimization conventions.

- Write notes entirely in **natural, clear English**, using complete sentences. Ignore conversational shorthand or caveman style when writing the study artifact. Keep paragraphs short and terminology consistent; avoid inflated prose and repeated summaries.
- Start with a short **Prerequisites you need** bridge explaining only earlier concepts required for this lesson. Inspect earlier course material when necessary to recover conventions, but do not require another note to follow an essential argument. Define symbols at first use, including payoff order and what each probability conditions on.
- Introduce a central concept through its practical question and intuition, then give its precise definition or formula, then apply it. Put important definitions in Obsidian callouts such as `> [!info] Definition — Nash equilibrium`.
- For a theorem, state assumptions, conclusion, meaning, and when it can be used in an exercise. Include proof reasoning when it teaches a needed method or is substantive lecture content; condense peripheral formal detail.
- Prioritize concepts, assumptions, solving procedures, important distinctions, and failure cases. Concision must not remove steps needed by a beginner or omit important lecture topics. No rigid word/page quota.
- Explain relevant distinctions explicitly, for example action versus contingent strategy, equilibrium strategy profile versus outcome, strict versus weak dominance, pure versus mixed strategies, and Nash versus subgame-perfect equilibrium. Include only distinctions needed for the actual lesson.

## Worked examples and practice

- Include a concrete worked example for each major new concept or method. Reuse one coherent example across related ideas when this reduces length without hiding differences.
- Prefer lecture examples or relevant handbook problems. Identify handbook chapter, exercise number/title, and page only after checking them. Label invented examples **Original example** or **Original practice**, never as professor's exercises or past exam questions.
- Explain the situation, players, choices, information, and payoffs before calculating. Show why a method applies, essential intermediate calculations, final answer, and interpretation. Define strategy and payoff ordering explicitly.
- Check results against definitions: profitable deviations for equilibria, feasibility and boundaries for optimization, probability bounds and unused-strategy inequalities for mixing, and sequential incentives at off-path subgames when relevant. Do not claim a complete equilibrium set after finding only some candidates or only pure equilibria.
- Include counterexamples or common mistakes when they prevent a specific likely error. Avoid unexplained jumps such as “clearly” in place of reasoning.
- End practice with a small selection of relevant handbook exercises and what each trains. Provide a brief solution route or worked solution where useful; keep unsolved prompts separate from answers. Never invent missing exercise references, solutions, exam frequency, or authoritative time estimates.

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
- Organize by concepts and methods, not slide-by-slide narration. A useful shape is prerequisite bridge, essential theory with worked examples and figures, practice, and a compact **Exam quick reference**. Adapt sections to the lesson rather than filling empty headings.
- Make the quick reference easy to consult in a 75-minute paper exam: recognizable problem cues, applicable methods, assumptions, essential formulas, short solving steps, and common traps. State variable meanings locally so it works on paper. Include a small decision table when it saves lookup time.
- Use standard Markdown headings and tables, `$...$` inline math, and `$$` display math on separate lines. Use relative Markdown image links with angle brackets around paths containing spaces, keeping assets portable and exportable. Essential explanations must remain visible when printed; no hover-only text, collapsed answers, or links as substitutes for content.
- Ensure diagrams work in grayscale: labels, shapes, or line styles must supplement color. Do not rely on interactive visualizations or Obsidian-only features for essential reasoning.
- Include a short source list and lightweight section/figure page references. Distinguish PDF page indices from printed handbook page numbers when they differ. Transcript timestamps help resolve ambiguous claims but are not required on every paragraph.
- Markdown and local images are default deliverables. Produce a printable PDF only when requested; if producing one, render and inspect it for broken formulas, unreadable diagrams, and split tables.

## Completion checks

Check coverage against selected PDFs and transcripts, mathematical consistency, example calculations, theorem assumptions, verified exercise references, image existence and readability, and relative link resolution. Check that prerequisites support a beginner and the quick reference works without electronic access. Report created/updated paths and genuine source gaps briefly, without guaranteeing exam coverage or success.
