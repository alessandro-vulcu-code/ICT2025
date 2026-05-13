---
name: append-study-questions
description: Append English open-ended review questions to a Markdown study note. Use when Codex is asked to read and analyze an .md file, including Obsidian embeds, Markdown images, diagrams, screenshots, and code snippets, then add a numbered "Questions" section at the end to help a student review the main concepts.
---

# Append Study Questions

## Overview

Analyze one Markdown note as study material and append open-ended review questions at the end of the same file. Questions must be in English, numbered, and focused on the document's most important concepts rather than minor details.

## Workflow

1. Confirm the input is a single Markdown file path. If the path is ambiguous or missing, ask for it.
2. Read the full note before writing. For long files, read in chunks and keep track of headings, diagrams, code blocks, callouts, examples, and conclusions.
3. Identify embedded images and inspect the important ones, especially diagrams, screenshots, plots, architecture figures, and images near major sections.
4. Identify the main study themes: core definitions, mechanisms, workflows, comparisons, algorithms, formulas, assumptions, examples, and common pitfalls.
5. Review code blocks. Use code snippets as question material only when they illustrate an important concept, behavior, API, algorithm, or error pattern.
6. Append or update a final `## Questions` section with numbered questions.

## Image Handling

Resolve and inspect image references before generating questions when the image is available locally:

- Obsidian embeds: `![[image.png]]`, `![[image.png|500]]`
- Markdown images: `![caption](relative/path.png)`
- HTML images: `<img src="relative/path.png">`

Resolution order:

1. Resolve relative paths from the Markdown file's directory.
2. For Obsidian wiki embeds, search nearby note folders and common image folders such as `Pics/`, `Pictures/`, `Figures/`, `Images/`, and `assets/`.
3. If needed, use `rg --files` to find the exact image filename within the repository.
4. Use the image viewing tool with the absolute path for relevant images.

If an image is missing or cannot be inspected, still use its filename, caption, alt text, and surrounding section context. Mention the limitation in the final response, not in the generated questions.

## Question Requirements

- Write at least 10 questions. Use 10-15 by default; add more only when the document has many major topics.
- Write questions in English.
- Use a numbered Markdown list.
- Make questions open-ended: ask the student to explain, compare, trace, justify, interpret, or reason.
- Prioritize high-value exam and oral-review material over isolated facts, slide numbers, formatting details, or tiny implementation details.
- Cover the whole note, but weight the questions toward the most central sections.
- Include image-based questions when diagrams or screenshots contain important conceptual information.
- Include code-based questions when code blocks are central, for example: "What happens in this snippet?", "What role does this function play?", "Why is this condition needed?", or "How would the behavior change if ...?"
- Do not include answers, hints, explanations, or answer keys unless the user explicitly asks for them.
- Avoid yes/no questions and questions that can be answered by copying one sentence from the note.

## Editing Rules

Append the section at the end of the Markdown file using this format:

```markdown
## Questions

1. ...
2. ...
```

If the file already ends with a `## Questions` section generated for review questions, update that section instead of duplicating it. If a pre-existing Questions section appears to contain user-authored notes or exercises, preserve it and append a new `## Questions` section only after confirming the user's intent.

Preserve the document's existing content and style. Do not reformat unrelated sections.
