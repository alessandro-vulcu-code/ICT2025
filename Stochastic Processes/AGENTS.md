# Repository Guidelines

## Project Structure & Module Organization

This repository is a documentation workspace for the Stochastic Processes course. Main content lives in `Stochastic_Processes_2020_output/`.

- `Stochastic_Processes_2020_output.md` and `Stochastic_Processes_2020_output_clean.md`: full extracted source notes.
- `Chapters/`: chapter-level Markdown notes, named `Chapter N - Topic.md`.
- `Summaries/`: condensed chapter summaries; `Summaries/old/` keeps previous versions.
- `Rewritten/`: polished rewritten chapters.
- `images/`: extracted JPEG figures referenced by the notes.

There is no application source tree, test suite, or build system in this folder.

## Build, Test, and Development Commands

No build is required for normal editing. Useful optional commands:

```bash
rg "term" Stochastic_Processes_2020_output/
```

Search notes quickly for definitions, formulas, and cross-references.

```bash
markdownlint "**/*.md"
```

Run Markdown linting if `markdownlint-cli` is installed. Use this as a consistency check, not as a mandatory build gate.

```bash
pandoc "Stochastic_Processes_2020_output/Chapters/Chapter 1 - Probability and Statistics.md" -o chapter1.pdf
```

Export a single note to PDF when Pandoc and a LaTeX distribution are available.

## Markdown Style & Naming Conventions

Use ATX headings (`#`, `##`, `###`) and concise academic prose. Prefer `-` for unordered lists and `1.` for ordered lists. Include a language tag on fenced code blocks, such as ` ```python `.

Use LaTeX math consistently: inline math with `$...$`, display math with `$$` on separate lines. Keep formulas readable and avoid altering notation unless the surrounding chapter already uses the new convention.

Name new chapter files as `Chapter N - Topic.md`. Use descriptive titles for summaries and rewritten notes that match their source chapter.

## Testing Guidelines

There are no automated tests or coverage requirements. Validate changes by previewing Markdown in Obsidian or VS Code, checking that formulas render correctly, and confirming image links still resolve. For large edits, run `rg "!\\[\\["` or inspect embedded image references manually.

## Commit & Pull Request Guidelines

Recent commits use short, descriptive messages such as `Added Stochastic notes` or course-prefixed messages like `[BDC] Fixed all summaries...`. Follow that pattern: state the affected course or topic and the change made.

Pull requests should summarize the edited chapters or summaries, mention any generated files or image changes, and note whether Markdown preview or PDF export was checked.

## Security & Academic Integrity

Do not commit credentials, private data, or unrelated local editor state. Notes should reflect original understanding and proper attribution rather than copied source text.
