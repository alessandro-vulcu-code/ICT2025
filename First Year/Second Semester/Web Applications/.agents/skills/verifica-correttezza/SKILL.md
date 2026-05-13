---
name: verifica-correttezza
description: Cross-check a faithful Big Data Computing transcription against its Markdown summary and update the summary in place. Use when the user invokes /verifica_correttezza, provides a transcription and a summary, asks to verify a Big Data note against source transcription, or wants missing definitions, theorems, proofs, algorithms, examples, bounds, formulas, callouts, table of contents, or summary tables corrected in Notes/*.md.
---

# Verifica Correttezza

## Overview

Use this skill to compare two Markdown documents from the Big Data Computing course:
the faithful transcription of the original material and the existing summary note. Produce a
short verification report first, then edit only the summary file if the comparison reveals
missing, incorrect, ambiguous, or poorly structured content.

## Inputs

- Treat the first argument as the transcription path or pasted transcription content.
- Treat the second argument as the summary path or pasted summary content.
- If a file name is provided without a directory for the summary, resolve it under `Notes/`.
- If both inputs are pasted content and no summary file path is available, report the needed
  corrections but ask for the target `Notes/<nome_file>.md` before editing.
- If the summary file is outside `Notes/`, use the file the user explicitly provided, but keep the
  final confirmation path exact.

## Verification Workflow

1. Read the full transcription and the full summary before deciding whether edits are needed.
2. Build a coverage map of every relevant item in the transcription:
   definitions, theorems, lemmas, propositions, corollaries, proofs, handwritten derivations,
   bounds, algorithms, pseudocode, examples, remarks, assumptions, tables, and formulas.
3. Compare the coverage map against the summary and classify issues as:
   missing content, formula mismatch, unclear or incomplete explanation, structural mismatch, or
   missing proof detail.
4. Emit a short report to the user before modifying files, using exactly this structure:

```markdown
## Report verifica

### Elementi mancanti
- <elenco puntato di cio che mancava>

### Formule da correggere
- <elenco puntato con originale -> corretto>

### Sezioni poco chiare espanse
- <elenco puntato>

### Nessuna modifica necessaria
<scrivi questa riga solo se il riassunto e gia completo e corretto>
```

5. If there are issues, edit the summary file directly with targeted changes in the correct
   location. Do not rewrite the note from scratch.
6. If there are no issues, do not touch the file.

## Editing Rules

- Preserve the existing note style, heading hierarchy, Obsidian links, image embeds, callouts,
  table of contents, and summary table when they are already correct.
- Add missing sections, callouts, formulas, algorithms, examples, or proof blocks at the point
  where they belong in the existing structure.
- Keep all additions faithful to the transcription. Do not introduce external explanations,
  alternative proofs, or unstated assumptions.
- Expand unclear passages only enough to make them self-contained for exam study.
- Preserve academic Italian unless the existing note is written in English.
- Use Obsidian callouts consistently with the note. Prefer `[!Important]` for key definitions,
  theorems, bounds, and exam-critical facts, and `[!Example]` for examples.
- Keep Markdown and LaTeX compatible with the repository rules: ATX headings, `-` bullets,
  `1.` ordered lists, `$...$` inline math, and `$$...$$` display math.
- When a table of contents or summary table exists, update it if headings or covered concepts
  change.

## Proofs And Handwritten Material

Treat handwritten definitions, theorems, lemmas, and proofs as exam-critical. If the transcription
contains a proof and the summary omits it or compresses away logical steps, add the full proof to
the summary. Rephrase for clarity only when the mathematical content, assumptions, order of
reasoning, and conclusion remain intact.

## Formula Checks

- Compare formulas symbol by symbol where possible: indices, summation bounds, norms,
  probabilities, constants, asymptotic notation, algorithm variables, and equality or inequality
  direction.
- Correct LaTeX syntax only when the intended formula in the transcription is clear.
- In the report, show formula corrections as `riassunto -> trascrizione corretta`.
- If the transcription is ambiguous or internally inconsistent, do not invent a correction. Flag
  the ambiguity in the report and avoid editing that formula unless the surrounding text resolves it.

## Final Response

After any edits, finish with:

```text
Riassunto aggiornato -> Notes/<nome_file>.md
```

If no edits were needed, finish with:

```text
Verifica completata: nessuna modifica necessaria.
```
