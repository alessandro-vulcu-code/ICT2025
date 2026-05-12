> Summarize a Markdown file transcribed from PDF and save it in `Summaries/`.

## Input

`/riassumi <path/to/file.md>`

The file is in `Stochastic_Processes_2020_output/Chapters/`. Subject: **Stochastic Processes** (Markov chains, Poisson processes, renewal theory, queueing, protocols).

---

## Language

Write the summary in **English**, regardless of any other language present. Do not translate mathematical notation.

---

## Goal

Produce a summary that is **fully self-contained** for a student preparing for the exam. Reading the summary must be sufficient — no need to re-read the original PDF. **Nothing may be omitted**: every theorem, proof, formula, figure, and exercise must appear.

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
- Transcribe every formula **exactly as in the source** — no simplifications
- Bullet lists for enumerations; numbered lists for sequences and algorithms
- Markdown tables for comparisons, parameters, and special cases

---

### 3. Theorems, Lemmas, Corollaries, Key Definitions → `[!Important]` callout

```markdown
> [!Important] Theorem / Lemma / Corollary Name
> **Statement:** faithful transcription of the original statement.
> $$formula$$
>
> **Proof:**
> Report **every step** of the proof present in the source.
> Explain the *why* behind each step, not just the *what*.
> $$intermediate formula$$
> Conclude with the final result and what it implies.
>
> **Intuition:** plain-language explanation of the result — why it is true,
> what it means probabilistically or geometrically, how it is used in practice.
```

**Rule:** if the source contains a proof, reproduce it **in full**. Never write "proof omitted" if the proof is present in the source.

Use this callout for: theorems, lemmas, corollaries, fundamental definitions, important bounds.

---

### 4. Examples and Exercises → `[!Example]` callout

```markdown
> [!Example] Example / Exercise Title
> **Problem:** statement of the problem.
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

Every exercise present in the source must appear with a **complete worked solution**. If the source states only the answer without working, derive the steps from the theory covered.

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

Markdown table of the key concepts of the chapter. Adapt columns to the content. Example:

| Concept | Definition / Formula | Conditions / Notes |
|---------|---------------------|--------------------|

or for processes:

| Process | Key property | Central formula | Typical use |
|---------|-------------|----------------|-------------|

---

### 7. Quality standards

- **Completeness:** no theorem, proof, formula, figure, or exercise from the source may be omitted
- **Clarity:** every mathematical step must be readable; add bridging sentences between formulas
- **Rigour:** maintain the standard of a graduate-level course; do not simplify results
- **Pedagogy:** for every important result explain the probabilistic or geometric intuition
- **Fidelity:** do not invent content; do not paraphrase formulas — transcribe them exactly; if something in the source is ambiguous, report it as-is with a note *(note: ...)*

---

### 8. Output

- Save to: `Stochastic_Processes_2020_output/Summaries/<filename>.md`
  - `<filename>` must be **identical** to the input file base name
- If `Summaries/` does not exist, create it
- Confirm: `Summary saved → Summaries/<filename>.md`
