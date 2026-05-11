---
name: rewrite-big-data-notes
description: Rewrite Big Data Computing Markdown lecture notes into complete, polished, exam-ready Obsidian notes saved under the course Notes/ folder. Use when the user invokes /riscrivi with a Markdown file path, asks to rewrite a file from ToSummarize/, or requests faithful cleanup of Big Data Computing notes covering MapReduce, Spark, coresets, streaming algorithms, probabilistic bounds, distributed systems, or related homework notes.
---

# Rewrite Big Data Notes

## Overview

Rewrite one Markdown file about Big Data Computing into a clean, complete, faithful course note for exam preparation. The output is a rewrite, not a summary: preserve the source content while repairing slide transcription artifacts, OCR damage, broken formatting, and unclear academic prose.

## Command

Accept requests in this form:

```text
/riscrivi <path/to/file.md>
```

The input should normally be in:

```text
ToSummarize/<filename>.md
```

Save the output to:

```text
Notes/<same-base-filename>.md
```

Create `Notes/` if missing. If the input is already inside `Notes/`, or the user explicitly asks for a non-destructive rewrite, save to:

```text
Rewritten/<same-base-filename>.md
```

Confirm completion exactly like:

```text
Rewrite saved -> Notes/<filename>.md
```

or, for non-destructive rewrites:

```text
Rewrite saved -> Rewritten/<filename>.md
```

## Workflow

1. Resolve the input path relative to the Big Data Computing course root when needed.
2. Read the entire source file before editing.
3. If the target file already exists, read it before overwriting so useful manual additions are not accidentally discarded.
4. Inspect nearby image references and the relevant `Pics/` subfolder. Preserve every existing image filename exactly.
5. Create or update the target file.
6. Preserve the lecture's complete content: every definition, observation, algorithm, theorem, proof sketch, formula, figure, example, exercise, and answer must appear.
7. Run a quick local check with `rg` or file inspection to verify the output path exists and major headings, formulas, and image references were preserved.

## Language And Fidelity

- Write all prose in English, regardless of whether the source mixes English and Italian. Do not translate code, identifiers, mathematical notation, API names, commands, or filenames.
- Preserve original prose verbatim where it is already readable English.
- Rephrase only to repair transcription damage, fragmented slide prose, broken grammar, or unclear formatting.
- Do not omit, shorten, simplify, or reorder formulas, assumptions, bounds, pseudocode, or algorithm steps.
- Preserve asymptotic notation, probability notation, key-value pair notation, Spark API names, and variable names exactly unless the source is clearly malformed.
- If a source fragment is ambiguous, keep it and add `(note: possible transcription artifact)`.
- Add short bridging sentences where slide bullets are too terse for studying, but never replace the original technical content with the bridge.
- Maintain rigorous, exam-useful explanations for Big Data Computing topics.

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
- `##` major lecture topic
- `###` section
- `####` subsection

Formatting rules:

- Use **bold** for technical terms and definitions introduced for the first time.
- Use *italic* for method names, expanded acronyms, framework names used as concepts, and emphasis.
- Use inline math as `$formula$`.
- Use display math on separate lines:

```markdown
$$
formula
$$
```

- Use `-` bullets for enumerations and `1.` numbered lists for algorithms or ordered procedures.
- Use fenced code blocks with a language tag for Spark, Python, Scala, shell, or pseudocode examples. Use `text` when no language applies.
- Convert comparisons, parameters, algorithm properties, and design goals into Markdown tables when this repairs source formatting.

## Big Data Computing Content Rules

- For **MapReduce**, keep the map phase, shuffle, reduce phase, round count $R$, local space $M_L$, aggregate space $M_A$, partitioning strategy, and reducer semantics explicit.
- For **Spark**, keep the distinctions among driver, executor, cluster manager, RDD/DataFrame abstractions, transformations, actions, lazy evaluation, caching, partitioning, and shuffles explicit.
- For **coresets**, preserve definitions of the objective, approximation factor, sampling strategy, merge-and-reduce structure, and all proofs or proof sketches.
- For **streaming**, preserve the stream model, memory bounds, approximation guarantees, hash functions, sketches, and update/query algorithms.
- For probabilistic arguments, preserve assumptions such as independence, events, union bounds, Markov/Chernoff bounds, and constants in the final probability statements.
- For algorithms, use a compact pseudocode block and then explain inputs, outputs, state, communication cost, memory cost, and correctness argument when present in the source.

## Important Callouts

Wrap definitions, observations, theorems, lemmas, propositions, important bounds, algorithms, and design goals in `[!Important]` callouts when they are central to the lecture:

```markdown
> [!Important] Theorem / Algorithm / Definition Name
> **Statement:** faithful transcription of the original statement.
>
> $$
> formula
> $$
>
> **Reasoning:** Reproduce every proof step, derivation, or justification in the source. Add bridging sentences only to make the logic explicit.
>
> **Intuition:** Explain why the result matters for distributed or big-data computation and how it is used in the course.
```

If the source contains a proof or proof sketch, reproduce it in full. Never write "proof omitted".

## Example Callouts

Wrap examples, exercises, homework-style problems, and worked algorithm traces in `[!Example]` callouts:

```markdown
> [!Example] Example / Exercise Title
> **Problem:** faithful transcription of the problem statement.
>
> **Approach:** state which model, algorithm, theorem, or Spark primitive applies and why.
>
> **Solution:**
> 1. First step with formula, pseudocode, or key-value pairs.
> 2. Second step.
>
> **Result:** final answer with interpretation.
>
> **Takeaway:** what to generalize for the exam.
```

Every exercise must appear with its complete worked solution if the source provides one. If the source gives only an answer, derive the missing steps from the surrounding theory and keep the original answer visible.

## Figures

For every figure, graph, architecture diagram, table screenshot, or handwritten diagram in the source, preserve the exact Obsidian image filename when present:

```markdown
![[exact_original_filename.png]]
*Figure N - description of what the figure shows and why it is relevant.*
```

If the source contains only a textual figure placeholder, inspect the relevant `Pics/` subfolder and use the matching image only when the correspondence is clear from order, topic, or nearby existing notes. If uncertain, keep the textual placeholder and add `(note: image match uncertain)` rather than inventing a filename.

## Final Summary Table

End the file with a Markdown summary table of the lecture's key concepts. Adapt the columns to the content:

```markdown
| Concept | Definition / Formula | Conditions / Notes |
|---|---|---|
```

For algorithm-focused lectures, prefer:

```markdown
| Algorithm / Technique | Model | Cost / Bound | Typical use |
|---|---|---|---|
```

The summary table is additive. It must not replace any original content.
