---
name: rewrite-network-modeling-notes
description: Rewrite and integrate Network Modeling lecture notes from handwritten iPad notes, Whisper transcripts, and Moodle materials in a lesson folder. Preserve the student's section titles, notation, and every diagram while filling gaps with priority to the lecturer. Use for integrated lecture notes, not standalone summaries or homework solutions.
---

# Rewrite Network Modeling notes

Produce a clear, concise, self-contained Markdown note that follows the student's original notes and incorporates missing explanations from the lecture and relevant Moodle material.

## Inputs and source priority

Inspect the requested lesson folder and identify original notes (handwritten PDF, images, or Markdown), all transcript parts, and additional course materials. Distinguish original notes from previously integrated outputs; do not treat a previous rewrite as the primary source when originals exist. Resolve existing embeds and linked local assets. Read related local materials only when needed to understand a reference.

Use the original notes as the structural and notational anchor. For what was taught and how it was explained, prioritize the lecturer's statements, then relevant Moodle material. Whisper text is evidence of speech, not an infallible authority: reconcile apparent recognition errors with handwriting, formulas, diagrams, and course materials. Never invent missing words, numerical values, assumptions, or claims attributed to the lecturer.

Read all source notes and transcript parts; inspect relevant additional material rather than relying on keyword snippets alone. Inspect handwritten pages and visual material directly; PDF text extraction and OCR alone cannot establish coverage of figures or handwritten formulas. Use available local PDF rendering, image viewing, and extraction tools. No specific cloud service, absolute machine path, or paid tool is required. If a necessary source cannot be read, state the concrete limitation; do not claim complete integration.

## Preserve structure and notation

- Preserve every original section and subsection, their order, and their title wording. Normalize Markdown heading levels only as needed to express the original hierarchy. Transcribe handwritten titles faithfully.
- Improve each section's body in place: repair unclear prose, fill omitted reasoning, and retain useful examples, derivations, conditions, and conclusions. Do not replace the notes with a differently organized textbook chapter.
- Put supplementary content in the existing section where it belongs. Add a clearly labeled subsection only when genuinely missing content has no suitable home; do not rename or rearrange original headings to accommodate it.
- Preserve the student's symbols, subscripts, parameter names, units, and conventions. Translate differing Moodle notation into the existing notation, checking that meanings match. Define a new symbol only for a genuinely new quantity, explain it locally, and avoid collisions.
- Preserve technically meaningful distinctions such as fluid versus packet models, rates versus amounts, stochastic versus deterministic quantities, initial conditions, and inequality boundaries. Keep equations dimensionally consistent.
- Correct demonstrable mathematical or transcription errors with source support. If a substantive correction changes an original formula or claim, explain it briefly near that point. For unresolved contradictions, retain the relevant context and mark the uncertainty; do not silently choose or fabricate a reconciliation.

## Integrate without padding

Include explanations, examples, assumptions, exceptions, and intermediate steps that the lecturer gave but the student missed. Integrate relevant concepts present only in Moodle when they complete or clarify the lesson, briefly labeling them as supplementary material where needed. Do not import an entire chapter or unrelated topics just because they share a source file.

Use the language of the original notes unless the user requests another language. Write normal, concise academic prose, regardless of conversational style. Explain difficult transitions sufficiently for study without repeating the same idea. Use bullets for parallel points and tables for useful comparisons. Define terms near first use; use Obsidian definition callouts when helpful. Avoid generic introductions, redundant conclusions, and unsolicited review questions.

Keep attribution light: identify Moodle-only additions, substantive disagreements, and uncertain readings, with source filenames and page numbers or transcript timestamps when available. Never invent timestamps or citations. Routine integrated prose does not need a citation on every sentence.

## Every visual must survive

Maintain a working inventory of diagrams, schemes, plots, and meaningful visual annotations in the original notes, recording source page, section, and destination. Include every one in the integrated Markdown, including compound panels and distinct stages of a drawing. Also include relevant visuals from supplementary materials that the integrated explanation uses; unrelated visuals elsewhere in a textbook need not be imported.

- Prefer faithful redraws for plots when their geometry and data are recoverable. Use reproducible plotting tools for quantitative plots, and Mermaid or SVG for suitable diagrams. Preserve axes, labels, symbols, units, scales, breakpoints, arrows, legends, and distinctions conveyed by color or line style.
- Never invent samples or numerical coordinates. If only qualitative behavior is known, label a redraw as schematic. If a faithful redraw is uncertain, embed a legible source crop instead.
- Preserve original handwritten figures when their annotations or layout carry meaning a redraw would lose. Crops must retain labels and relevant context. A full page embed is a fallback when a useful crop cannot be made.
- Embed actual renderable figures, not descriptions or placeholders. Provide a short caption explaining their role. Check rendered redraws and extracted crops against the source; do not claim visual verification without viewing them.
- Store new assets in a lesson-local `Pics/` folder and use relative Markdown links or existing Obsidian embed conventions. Preserve and resolve existing image links. Keep any code required to regenerate newly drawn plots alongside the lesson assets when useful.

Before completion, reconcile the visual inventory against the output: every original visual must have a working embed or faithful redraw. A duplicate may share one asset, but retain its pedagogical placement or an explicit local reference. If any visual is unavailable or unreadable, explicitly report it and do not describe the output as complete.

## Output and final checks

Default to a new Markdown file alongside the sources, using the existing lesson naming convention and an `Integrated notes` suffix. Keep source notes, transcripts, and Moodle files intact unless the user explicitly asks to edit a particular file in place. If the intended output already exists and replacement was not requested, choose a distinct name rather than overwriting unrelated work.

Use ATX headings, `$...$` for inline math, and `$$` on separate lines for display math. Use valid LaTeX subscripts, fenced code blocks with language tags, and relative asset paths. Follow applicable repository conventions without hardcoding a course folder layout or machine-specific location.

Before delivering, compare output against the originals for section titles/order, notation, equations, worked examples, and figure coverage. Check transcript coverage section by section and confirm relevant Moodle additions have been placed coherently. Resolve all asset links and remove unfinished placeholders. Report the output path, any added asset folder, and concrete unresolved issues concisely. Do not run unrelated builds or claim validation that was not performed.
