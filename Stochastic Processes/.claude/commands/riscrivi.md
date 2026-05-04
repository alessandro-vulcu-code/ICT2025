> Rewrite a Markdown file transcribed from PDF and save it in `Rewritten/`.

## Input

`/riscrivi <path/to/file.md>`

The file is in `Stochastic_Processes_2020_output/Chapters/`. Subject: **Stochastic Processes** (Markov chains, Poisson processes, renewal theory, queueing, protocols).

---

## Language

Write in **English**, regardless of any other language present. Do not translate mathematical notation.

---

## Goal

Produce a **complete, clean rewrite** of the source file for a student preparing for the exam. The output must be a faithful, well-formatted version of the **entire original content** — not a summary. **Nothing may be omitted, shortened, or paraphrased**: every sentence, theorem, proof, formula, figure, example, and exercise must appear in full, exactly as in the source. The only changes allowed are:

- Fixing OCR artifacts, broken LaTeX, garbled tables
- Adding proper Markdown/Obsidian formatting
- Inserting `[!Important]` and `[!Example]` callouts around theorems and exercises
- Adding bridging sentences between formulas for readability
- Adding an Obsidian Table of Contents and a summary table at the end

---

## Instructions

### 1. Table of Contents (top of file)

```markdown
## Table of Contents

- [[#Section Title|Section Title]]
- [[#Section Title 2|Section Title 2]]
  - [[#Subsection|Subsection]]
```

Use Obsidian internal links (`[[#anchor|label]]`). Generate anchors from section headings.

---

### 2. Document structure

- Heading hierarchy: `#` document title → `##` chapter → `###` section → `####` subsection
- **Bold** for technical terms and definitions introduced for the first time
- *Italic* for method names, expanded acronyms, and emphasis
- Non-inline formulas must be **centered in display blocks**:
  $$formula$$
- Inline formulas: `$formula$`
- Transcribe every formula **exactly as in the source** — no simplifications, no reordering
- Bullet lists for enumerations; numbered lists for sequences and algorithms
- Markdown tables for comparisons, parameters, and special cases
- Preserve the **original prose** verbatim where possible; only rephrase to fix grammar broken by OCR

---

### 3. Theorems, Lemmas, Corollaries, Key Definitions → `[!Important]` callout

```markdown
> [!Important] Theorem / Lemma / Corollary Name
> **Statement:** faithful transcription of the original statement.
> $$formula$$
>
> **Proof:**
> Reproduce **every step** of the proof exactly as in the source.
> Add bridging sentences between formulas to make the logic explicit.
> $$intermediate formula$$
> Conclude with the final result and what it implies.
>
> **Intuition:** plain-language explanation of the result — why it is true,
> what it means probabilistically or geometrically, how it is used in practice.
```

**Rule:** if the source contains a proof, reproduce it **word for word** in full. Never omit any step. Never write "proof omitted".

Use this callout for: theorems, lemmas, corollaries, fundamental definitions, important bounds.

---

### 4. Examples and Exercises → `[!Example]` callout

```markdown
> [!Example] Example / Exercise Title
> **Problem:** exact transcription of the problem statement.
>
> **Approach:** which technique or theorem applies and why.
>
> **Solution:**
> 1. First step with formula:
> $$...$$
> 2. Second step...
>
> **Result:** final answer with units and interpretation.
>
> **Takeaway:** what to generalize from this example for the exam.
```

Every exercise must appear with its **complete worked solution** exactly as in the source. If the source gives only an answer without steps, derive the missing steps from the theory.

---

### 5. Figures and images

For every figure, graph, or diagram in the source:

```markdown
![[exact_original_filename.jpeg]]
*Figure N — description of what the figure shows and why it is relevant, written in italics.*
```

- Use the **exact filename** as it appears in the source (e.g. `Stochastic_Processes_2020_p174_img61.jpeg`)
- Caption always in *italics*
- Do not skip any figure

---

### 6. Summary table (end of file)

Markdown table of the key concepts of the chapter. Adapt columns to the content:

| Concept | Definition / Formula | Conditions / Notes |
|---------|---------------------|--------------------|

or for processes:

| Process | Key property | Central formula | Typical use |
|---------|-------------|----------------|-------------|

---

### 7. Quality standards

- **Completeness:** no sentence, theorem, proof, formula, figure, or exercise from the source may be omitted or shortened
- **Fidelity:** do not paraphrase formulas — transcribe them exactly; if something in the source is ambiguous or appears to be an OCR error, report it as-is with a note *(note: possible OCR artifact)*
- **Clarity:** every mathematical step must be readable; add bridging sentences between formulas where the source is terse
- **Rigour:** maintain the standard of a graduate-level course; do not simplify results
- **Pedagogy:** for every important result explain the probabilistic or geometric intuition

---

### 8. Output

- Save to: `Stochastic_Processes_2020_output/Rewritten/<filename>.md`
  - `<filename>` must be **identical** to the input file base name
- If `Rewritten/` does not exist, create it
- Confirm: `Rewrite saved → Rewritten/<filename>.md`
