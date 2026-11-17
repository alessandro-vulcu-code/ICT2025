---
name: summarize-digital-forensics-lecture
description: Merge Digital Forensics lecture transcripts, presentation PDFs, extended notes, and solved exercises into concise English Markdown study notes for handwriting on iPad. Preserve original section titles and lecture order, explain worked exercises, and embed cropped original figures. Use for Digital Forensics course materials, not other courses or independent forensic investigations.
---

# Summarize Digital Forensics lectures

Produce concise English Markdown notes that a student can copy by hand onto an iPad and later study. Combine the supplied sources into one explanation of the Digital Forensics lesson. Favor completeness of essential reasoning over exhaustive transcription, and brevity over textbook-style expansion. Follow explicit user overrides.

## Identify sources and their roles

- Inspect the requested lesson folder and applicable repository instructions. Respect user-specified filenames, transcript order, and topic boundaries. If no folder is specified, use the current lesson folder; clarify only material ambiguity.
- Identify the transcript, main presentation, extended lecture notes, and any exercise or solved-exercise PDFs. Do not hardcode lesson numbers, filenames, a professor's identity, or a fixed exercise duration.
- Read all relevant sources in full, splitting long extracted text into chunks to avoid truncation. Render PDF pages to inspect diagrams, equations, tables, and annotations that text extraction misses.
- Map the transcript's progression to the slides and supporting notes. The transcript establishes what was explained and when; the presentation supplies the topic sequence and original section titles; extended notes clarify definitions, missing reasoning, and necessary detail; solved exercises supply the worked solution.
- Follow explicit oral corrections over an older slide, identifying substantive discrepancies briefly. Do not silently invent missing facts or reconcile incompatible values.

Example of source mapping, not a fixed configuration: Lesson 8's transcript discusses an exercise for roughly the first 30 minutes, matched to `exercise_solved.pdf`, then introduces Multimedia Forensics using `pres_lecture08b.pdf` with `NotesAboutMultimediaForensics.pdf` as extended support. Infer the equivalent mapping anew for each lesson.

## Integrate in teaching order

- Begin with the material the professor explains first. If an exercise precedes a new topic, explain the exercise before introducing that topic. Keep supporting detail beside its matching concept; do not jump ahead to follow the separate order of an extended document.
- Preserve original section titles exactly, including wording, numbering, capitalization, and language. Use presentation titles for the presentation portion and original exercise titles for exercise portions. Use source-provided subheadings where useful.
- Do not invent section or subsection titles, translate headings, or add generic sections such as “Key takeaways”, “Background”, or “Review questions”. If clarification has no source heading, place it as a short paragraph or bullet beneath the existing relevant heading. Where an exercise lacks a heading, begin directly with its content rather than inventing one.
- Group contiguous repeated slide titles when they cover one explanation. Keep a title again if the lecturer returns to it later and merging would disrupt the sequence. Decorative covers and footer text need not become sections.
- Merge overlapping explanations instead of summarizing each source separately. Use extended notes to resolve gaps and preserve essentials, not as a reason to include every detail absent from the taught lesson. Mention substantial untaught material only if the user's requested scope includes it.

## Explain solved exercises concisely

- Rewrite the problem's goal, relevant given data, and assumptions. Retain units, variable meanings, parameters, and the exact question being answered.
- Present the solution in short logical steps: calculation or operation, why it is needed, and the resulting value or inference. Preserve intermediate steps necessary to reproduce the solution; remove repeated arithmetic or verbal commentary.
- Include relevant commands, formulas, data excerpts, plots, or tables only when they explain the method or support the answer. Keep literal technical syntax accurate.
- End the worked explanation with the result and what it means for the question. Distinguish observed evidence, inferred conclusions, and stated assumptions. Do not upgrade a probabilistic indication into proof of authenticity, manipulation, or attribution.
- Check numerical results against the solved PDF and the professor's explanation. Mark unresolved inconsistencies briefly rather than introducing a different exercise solution without notice.

## Keep the note suitable for handwriting

- Use clear academic English, short paragraphs, compact bullets, and small comparison tables where they save writing. The artifact must use normal grammatical prose even if conversation uses shorthand.
- Retain essential definitions, methods, assumptions, equations, interpretations, and limitations. Keep the smallest useful example when it makes a concept understandable.
- Remove jokes, administrative details, rhetorical questions, digressions, repeated definitions, and duplicated explanations. Avoid introductory filler, exhaustive slide paraphrases, and a second recap of points already covered.
- Explain a term once and use it consistently. Preserve the course's technical distinctions and notation; define symbols near their first use. For forensic methods, retain what the method detects, its operating idea, and any limitation emphasized by the professor.
- Use LaTeX math with `$...$` and separate `$$` blocks, following repository conventions. Provide only derivation steps needed to follow or reproduce the argument.
- Avoid arbitrary word counts that cut essential concepts. Before finishing, remove sentences that add no new definition, reasoning, evidence, or necessary distinction.
- Base notes on supplied materials. Use external authoritative sources only when verification is needed; distinguish any added correction and cite it locally. Avoid adding unrelated legal guidance or broad forensic background.

## Embed useful cropped visuals

**Use crops of figures, not screenshots of full PDF pages.** Carry forward this user's preference from their lecture-summary workflow.

- Include every distinct useful image, graph, diagram, scheme, and table supporting the taught material. Skip decorative graphics and literal duplicates. For near-duplicates, retain variants only when they teach a different point.
- Crop around the complete visual with a small margin. Exclude page titles, general slide prose, footers, and logos; preserve axes, tick values, legends, units, labels, annotation arrows, keys, and necessary captions.
- Keep paired images together when the comparison is meaningful, especially original/manipulated images, intermediate processing stages, or aligned plots. Preserve image details, aspect ratio, and color relevant to the forensic explanation; do not retouch, recolor, or generate substitute evidence images.
- Reproduce simple tables in Markdown when that improves readability. Keep an original crop when visual layout, highlighting, or graphical information matters. Avoid redundant image-plus-text copies when nothing is gained.
- Render vector diagrams and their text together as PDF clips. The bundled `scripts/crop_pdf_figure.py` helper requires PyMuPDF (`fitz`) and accepts a 1-based page number plus a rectangle in PDF points (72 points/inch, top-left origin).
- Inspect a temporary full-page preview, choose coordinates for the actual figure, render at about 180-240 dpi, and inspect the crop. Adjust until all labels remain readable and no unrelated page content remains. Whitespace trimming alone does not identify figure boundaries.
- Save final assets under the lesson's `Pics/` or existing image directory with descriptive source/page filenames. Embed relative Markdown image links with useful alt text next to the corresponding explanation. Keep temporary previews outside final assets.

Example helper usage; select coordinates independently for the current page:

```bash
python scripts/crop_pdf_figure.py slides.pdf Pics/p12-image-comparison.png --page 12 --rect 40 130 680 470 --dpi 200
```

## Verify and deliver

- Save a descriptive `.md` file in the requested lesson folder, following local naming rules. Preserve existing notes unless replacement was requested.
- Check coverage of all transcript portions, correct exercise/topic mapping, unchanged source headings, and uninterrupted lecture order. Check that extended notes have not inflated the summary beyond the requested taught scope.
- Verify formulas, numerical values, technical terms, table entries, and distinction between observations and conclusions. Check relative links and balanced math delimiters.
- Open every final crop and verify readability and completeness. Confirm all useful visual material is represented without entire-page screenshots.
- Include compact source links or page references where helpful, without adding invented section titles or excessive provenance text to handwritten study content.
- Report the clickable Markdown path and briefly note cropped visuals or unresolved source issues. Do not commit, push, alter other lessons, or append review questions unless asked.
