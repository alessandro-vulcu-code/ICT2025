---
name: rewrite-md-notes
description: Rewrite and clean Markdown notes from a provided .md file while preserving all content, images, Obsidian embeds, math, links, tables, and code. Use when the user invokes /riscrivi-md, asks to riscrivi/sistema/pulisci/fixa a Markdown document, wants typo and formatting cleanup, or has notes where code, commands, logs, formulas, lists, headings, or images are malformed.
---

# Rewrite MD Notes

## Overview

Rewrite one Markdown document into a clean, readable, exam-ready note without summarizing or dropping content. Fix typos, broken Markdown, damaged layout, and missing code fences while preserving the document's language, meaning, images, links, formulas, and Obsidian-specific syntax.

## Command

Accept requests like:

```text
/riscrivi-md <path/to/file.md>
/riscrivi-md <path/to/file.md> -> <path/to/output.md>
```

Default output:

- Save next to the input as `<same-base-filename>.rewritten.md`.
- Never overwrite the source file unless the user explicitly asks for in-place editing.
- If the user specifies a destination, follow it and create parent folders if needed.

Confirm completion exactly like:

```text
Rewrite saved -> <path/to/output.md>
```

## Workflow

1. Read the entire source file before writing the output.
2. Identify the document language, heading structure, images, links, callouts, math, tables, code-like text, examples, exercises, and obvious formatting damage.
3. Create the output file using `apply_patch` or another normal file-editing workflow.
4. Preserve all source content: every definition, paragraph, list item, formula, table row, code fragment, image, caption, example, exercise, and reference must remain represented.
5. Fix Markdown and prose only where needed for readability and rendering.
6. Run a quick verification pass with `rg` or file inspection before final response.

## Fidelity Rules

- Preserve the source language. Do not translate unless the user asks.
- Rewrite, do not summarize. Do not omit, compress, or replace source content with commentary.
- Keep the original order unless moving a line repairs clearly broken PDF/OCR layout.
- Preserve correct prose when it is already readable.
- Fix typos, spacing, punctuation, repeated words, broken line wrapping, malformed lists, and inconsistent heading levels.
- Do not invent facts, examples, image filenames, formulas, or explanations.
- If a fragment is ambiguous, keep the original meaning visible and add `(note: possible transcription artifact)` only when needed.

## Image Preservation

Preserve every image reference exactly unless a path must be adjusted because the output is saved in another directory.

Keep these forms intact:

```markdown
![alt text](relative/or/absolute/path.png)
![[Pasted image 20260510183000.png]]
![[diagram.png|500]]
<img src="..." alt="...">
```

Rules:

- Do not delete, rename, or replace image embeds.
- Keep images close to the surrounding explanation or caption.
- Preserve captions and nearby figure labels.
- Do not invent image files.
- If the source refers to a figure/diagram/screenshot that is missing from the Markdown, insert a short Obsidian callout placeholder:

```markdown
> [!figure] Missing figure - short descriptive title
> **Placeholder:** add the image from the original source.
> **Source cue:** preserve the original figure number, caption, or nearby wording.
```

## Formatting Rules

- Use ATX headings: `#`, `##`, `###`, `####`.
- Use `-` for unordered lists and `1.` for ordered procedures.
- Use `**bold**` for terms or definitions introduced by the source.
- Use `*italic*` only for emphasis or named methods when useful.
- Use inline math as `$...$`.
- Use display math on separate lines:

```markdown
$$
formula
$$
```

- Repair malformed Markdown tables when the source clearly intends a table.
- Preserve Obsidian syntax: wiki-links `[[...]]`, embeds `![[...]]`, callouts, tags, and frontmatter.
- Keep external links and relative links working.

## Code And Technical Text

Wrap code-like blocks in fenced code blocks with the best language tag. Use `text` when the language is unclear.

Common cases that should become fenced blocks:

- Programming snippets in languages such as `cpp`, `java`, `python`, `javascript`, `html`, `css`, `sql`, `bash`, or `json`.
- Shell commands, terminal output, logs, stack traces, configuration, HTTP requests/responses, XML/HTML fragments, and pseudocode.
- Multi-line algorithms or grammar-like definitions.

Use inline code for short identifiers, filenames, commands, flags, paths, variables, functions, classes, HTTP methods, status codes, and literals.

Do not put normal prose in code blocks.

## Callouts

Preserve existing Obsidian callouts. When the source clearly contains a key definition, warning, example, theorem, formula, or exercise but the formatting is broken, use concise callouts:

```markdown
> [!info] Definition - Term
> Cleaned definition text.
```

```markdown
> [!example] Example - Title
> **Problem:** original problem statement.
>
> **Solution:** faithful cleaned solution.
```

Only add callouts when they improve structure; do not overdecorate the note.

## Verification

Before final response, check:

- The output file exists.
- Markdown image/embed counts are not lower than the source unless the user explicitly requested removals.
- Code fences are balanced.
- Major headings and formulas from the source are still present.
- The rewritten file contains no obvious leftover OCR garbage, dangling list markers, or unwrapped code blocks.
