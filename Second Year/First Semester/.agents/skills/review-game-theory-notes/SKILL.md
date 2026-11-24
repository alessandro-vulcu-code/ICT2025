---
name: review-game-theory-notes
description: Review an existing Game Theory Markdown note against supplied lecture files or all relevant materials in the note's folder. Check fidelity to the slides, worked examples, formulas, embedded figures, and natural English. Edit the note when the user asks for corrections.
---

# Review Game Theory Notes

Use this skill to review an existing English study note for a student new to Game Theory who needs to follow the reasoning and solve similar problems on paper.

## Choose the comparison materials

```text
$review-game-theory-notes "file.md" "presentation.pdf"
$review-game-theory-notes "file.md" "presentation.pdf" "lecture.transcript.txt"
$review-game-theory-notes "file.md"
```

Treat the first path as the Markdown note under review. When comparison files are supplied, use all of them and keep the comparison within that set. You can still open images embedded in the target note to verify them.

With only the Markdown path, inspect its entire containing folder, including subfolders. Read every relevant lecture PDF, transcript, and companion document, and inspect image assets such as those in `Pics/`. Match materials by title and content because folder, slide, and recording numbers can differ. Skip exact duplicates and report materially unrelated or unreadable files if they affect the review. Keep the scope inside that folder.

Use the presentation's conceptual sequence, notation, and examples as the backbone. Use transcripts to recover explanations and intermediate reasoning. Read the relevant materials in full, rendering PDF pages where equations or graphics need visual inspection. Flag conflicting or unreadable evidence in the review. If no comparison sources are available, still review prose, internal consistency, and image links, and state that source fidelity could not be checked.

## Review the note

- **Coverage and coherence.** Follow the presentation's teaching sequence and logical dependencies, grouping related ideas where that helps readability. Find missing core concepts, assumptions, reasoning steps, or examples, and flag unsupported additions. Check definitions, notation, theorem conditions, and conclusions against the materials.
- **Worked examples.** Check that the note uses the presentation's relevant examples and preserves their setup, action and strategy order, information sets, payoffs, and results. Verify calculations independently. Show enough intermediate reasoning for a beginner to follow how the result was obtained, especially when testing profitable deviations or checking off-path decisions.
- **Figures.** Check that the note actually embeds the relevant diagrams, game trees, payoff matrices, or graphs from the comparison materials near the explanations that use them. Resolve relative Markdown links and Obsidian embeds, open the images, and check correspondence with the source, readability, and completeness of labels, branches, and payoffs. A figure stored in `Pics/` counts only when embedded in the note.
- **English prose.** Use complete, connected sentences and paragraphs. Link definitions, reasoning, and examples so the reader can follow why each step matters. Flag strings of clipped sentences and bullets that split a single argument. Reserve lists for parallel items or ordered solution steps. Remove source narration such as “in this slide,” “in this lesson,” and “the lecturer explains.” State the idea directly.
- **References.** Source lists, routine slide or page citations, and provenance labels are optional in the note. Flag meaningful gaps and errors even when the note has no citations. Use page numbers or transcript locations in the review when they help locate supporting evidence.

## Deliver the review or apply requested edits

For a review, report actionable findings in priority order. Give the note's section or line, describe what needs fixing, and include the expected content or a short proposed rewrite where helpful. State any limits on verification. Edit the Markdown and create image files only when the user also requests corrections.

When correcting, edit the existing note in place and preserve its valid content, notation, local formatting, and the original comparison files. For a missing or unreadable source figure, crop a rendered PDF page into the lesson's `Pics/` folder and embed it nearby using the existing link convention. The sibling `summarize-game-theory/scripts/crop_pdf.py` can render a crop when available. Inspect the result and verify the link. Use a short descriptive caption where it aids understanding.
