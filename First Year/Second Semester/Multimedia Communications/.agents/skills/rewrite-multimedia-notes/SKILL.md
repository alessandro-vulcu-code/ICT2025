---
name: rewrite-multimedia-notes
description: Rewrite Multimedia Communications Markdown notes converted from PDF into complete, clean, exam-ready Obsidian notes with image placeholders for figures that were not extracted. Use when the user invokes /riscrivi-multimedia with a Markdown file path, asks to rewrite a file from Notes/ or ToSummarize/, or requests faithful cleanup of Multimedia Communications notes covering compression, quantization, transform coding, entropy coding, wavelets, motion estimation, JPEG, video coding, learned compression, or modern video standards.
---

# Rewrite Multimedia Notes

## Overview

Rewrite one Markdown file converted from a PDF into a polished, complete, faithful Multimedia Communications note for exam preparation. The output is a rewrite, not a summary: preserve all source content while repairing OCR/transcription damage, structure, math formatting, and readability.

## Command

Accept requests in this form:

```text
/riscrivi-multimedia <path/to/file.md>
```

The input is usually in `Notes/` or `ToSummarize/`. Save the output to:

```text
Lessons/<same-base-filename>.md
```

Create `Lessons/` if missing. If the user requests another destination, follow it. Confirm completion exactly like:

```text
Rewrite saved -> Lessons/<filename>.md
```

## Workflow

1. Read the entire source file before editing.
2. Identify headings, formulas, examples, exercises, tables, figure captions, references to diagrams, and OCR artifacts.
3. Create or update `Lessons/<filename>.md`.
4. Preserve the complete content: every definition, sentence, formula, algorithm, example, exercise, answer, table, and figure reference must appear.
5. Insert explicit image placeholders wherever the source refers to a figure, diagram, graph, block scheme, table image, slide image, or visual example but no image file is available.
6. Run a quick local check with `rg` or file inspection to verify the output path exists and major headings, formulas, and figure placeholders were preserved.

## Language And Fidelity

- Write all prose in English unless the user explicitly asks for another language.
- Preserve readable English prose verbatim when it is already correct.
- Rephrase only to repair OCR damage, broken grammar, duplicated fragments, or unreadable PDF line wrapping.
- Do not omit, shorten, simplify, or reorder formulas.
- Keep acronyms and technical names precise: DCT, DFT, JPEG, MPEG, HEVC, VVC, PSNR, SSIM, MSE, RD, DPCM, PCM, VLC, CABAC, GOP, motion vectors.
- If a source fragment is ambiguous, keep it and add `(note: possible OCR artifact)`.
- Add brief explanatory bridging sentences only when they clarify terse mathematical steps; do not replace original content with commentary.

## Document Format

Start with an Obsidian table of contents:

```markdown
## Table of Contents

- [[#Section Title|Section Title]]
- [[#Section Title 2|Section Title 2]]
  - [[#Subsection|Subsection]]
```

Use this heading hierarchy:

- `#` document title
- `##` chapter or major topic
- `###` section
- `####` subsection

Formatting rules:

- Use **bold** for technical terms and definitions introduced for the first time.
- Use *italic* for method names, expanded acronyms, and emphasis.
- Use inline math as `$formula$`.
- Use display math on separate lines:

```markdown
$$
formula
$$
```

- Use `-` bullets for enumerations and `1.` numbered lists for ordered procedures or algorithms.
- Convert damaged comparisons, parameter lists, codec feature lists, and special cases into Markdown tables when this repairs PDF formatting.
- Use fenced code blocks with a language when the source contains pseudocode or scripts.

## Important Callouts

Wrap key definitions, theorems, codec principles, objective functions, bounds, and fundamental formulas in `[!Important]` callouts:

```markdown
> [!Important] Concept / Result Name
> **Statement:** faithful transcription of the original definition or result.
>
> $$
> formula
> $$
>
> **Interpretation:** Explain what the result means for compression, distortion, rate, perception, or implementation.
```

If the source contains derivations, reproduce every step in full. Never write "derivation omitted".

## Examples And Exercises

Wrap examples and exercises in `[!Example]` callouts:

```markdown
> [!Example] Example / Exercise Title
> **Problem:** exact transcription of the problem statement.
>
> **Approach:** state which coding, quantization, transform, prediction, or estimation method applies and why.
>
> **Solution:**
> 1. First step with formula:
>
> $$
> ...
> $$
>
> 2. Second step...
>
> **Result:** final answer with units and interpretation.
>
> **Takeaway:** what to generalize for the exam.
```

Every exercise must appear with its complete worked solution exactly as in the source. If the source gives only an answer without steps, derive the missing steps from surrounding theory and keep the original answer visible.

## Figure Placeholders

The PDF conversion has no extracted images. For every figure, graph, diagram, block diagram, transform basis image, codec pipeline, RD curve, spectrum plot, matrix illustration, frame sequence, or caption, insert a placeholder where the visual belongs.

Use this format:

```markdown
Figure N: concise description of the missing image.
```

Rules:

- Do not invent image filenames.
- Do not skip any visual reference.
- If the source says only "Figure" or refers to "the diagram below", still add a placeholder.
- If multiple visuals are described in one paragraph, create one placeholder per distinct visual.
- Use a plain text placeholder only, not an Obsidian callout.
- Preserve the original figure number and caption when present.
- If there is no original figure number, assign the next sequential figure number.
- Describe the visual itself using the surrounding text, without extra fields such as placeholder notes, expected content, or source cues.

## Multimedia-Specific Structure

When useful, organize material around the compression pipeline:

1. Signal representation or perception model.
2. Prediction, transform, or analysis stage.
3. Quantization or rate-control stage.
4. Entropy coding or bitstream syntax.
5. Reconstruction, distortion metric, or evaluation.
6. Standards, profiles, tools, and implementation tradeoffs.

Keep equations and diagrams close to the prose that explains them.

## Final Summary Table

End the file with a Markdown summary table of the note's key concepts. Adapt columns to the content:

```markdown
| Concept | Definition / Formula | Compression role | Notes |
|---|---|---|---|
```

For codec-focused notes, prefer:

```markdown
| Tool / Standard | Key idea | Main parameters | Typical use |
|---|---|---|---|
```

The summary table is additive. It must not replace any original content.
