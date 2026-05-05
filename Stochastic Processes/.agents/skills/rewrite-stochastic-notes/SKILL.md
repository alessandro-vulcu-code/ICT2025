---
name: rewrite-stochastic-notes
description: Rewrite Stochastic Processes Markdown chapters transcribed from PDF into complete, clean, exam-ready Obsidian notes saved under Stochastic_Processes_2020_output/Rewritten/. Use when the user invokes /riscrivi with a Markdown file path, asks to rewrite a file from Stochastic_Processes_2020_output/Chapters/, or requests faithful cleanup of Stochastic Processes notes covering Markov chains, Poisson processes, renewal theory, queueing, or protocols.
---

# Rewrite Stochastic Notes

## Overview

Rewrite one Markdown file transcribed from PDF into a polished, complete, faithful Stochastic Processes note for exam preparation. The output is a rewrite, not a summary: preserve all source content and only change formatting, OCR damage, and readability scaffolding.

## Command

Accept requests in this form:

```text
/riscrivi <path/to/file.md>
```

The input should normally be in `Stochastic_Processes_2020_output/Chapters/`. Save the output to:

```text
Stochastic_Processes_2020_output/Rewritten/<same-base-filename>.md
```

Create `Rewritten/` if missing. Confirm completion exactly like:

```text
Rewrite saved -> Rewritten/<filename>.md
```

## Workflow

1. Read the entire source file before editing.
2. Inspect nearby image references and preserve every referenced image filename exactly.
3. Create or update `Stochastic_Processes_2020_output/Rewritten/<filename>.md`.
4. Preserve the chapter's complete content: every sentence, theorem, proof, formula, figure, example, exercise, and answer must appear.
5. Run a quick local check with `rg` or file inspection to verify the output path exists and major headings/image references were preserved.

## Language And Fidelity

- Write all prose in English, regardless of source language. Do not translate mathematical notation.
- Preserve original prose verbatim where it is already readable English.
- Rephrase only to repair OCR damage, broken grammar caused by transcription, or unreadable formatting.
- Do not omit, shorten, simplify, or reorder formulas. Transcribe each formula exactly as in the source unless it is clearly broken by OCR.
- If a source fragment is ambiguous, keep it and add `(note: possible OCR artifact)`.
- Add explanatory bridging sentences only between terse mathematical steps; do not replace the original mathematical content with the bridge.
- Maintain graduate-level rigor and exam usefulness.

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
- `##` chapter
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

- Use `-` bullets for enumerations and `1.` numbered lists for sequences or algorithms.
- Convert comparisons, parameters, and special cases into Markdown tables when this repairs source formatting.

## Important Callouts

Wrap theorems, lemmas, corollaries, key definitions, fundamental results, and important bounds in `[!Important]` callouts:

```markdown
> [!Important] Theorem / Lemma / Corollary Name
> **Statement:** faithful transcription of the original statement.
>
> $$
> formula
> $$
>
> **Proof:**
> Reproduce every step of the proof in full. Add bridging sentences between formulas only to make the logic explicit.
>
> $$
> intermediate formula
> $$
>
> **Intuition:** Explain why the result is true, what it means probabilistically or geometrically, and how it is used in practice.
```

If the source contains a proof, reproduce it in full. Never write "proof omitted".

## Example Callouts

Wrap examples and exercises in `[!Example]` callouts:

```markdown
> [!Example] Example / Exercise Title
> **Problem:** exact transcription of the problem statement.
>
> **Approach:** state which technique or theorem applies and why.
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
> **Takeaway:** what to generalize from this example for the exam.
```

Every exercise must appear with its complete worked solution exactly as in the source. If the source gives only an answer without steps, derive the missing steps from the surrounding theory and keep the original answer visible.

## Figures

For every figure, graph, or diagram in the source, preserve the exact original image filename:

```markdown
![[exact_original_filename.jpeg]]
*Figure N - description of what the figure shows and why it is relevant.*
```

Do not skip any figure. Keep filenames exactly as written, such as `Stochastic_Processes_2020_p174_img61.jpeg`.

## Final Summary Table

End the file with a Markdown summary table of the chapter's key concepts. Adapt the columns to the content:

```markdown
| Concept | Definition / Formula | Conditions / Notes |
|---|---|---|
```

For process-focused chapters, prefer:

```markdown
| Process | Key property | Central formula | Typical use |
|---|---|---|---|
```

The summary table is additive. It must not replace any original content.
