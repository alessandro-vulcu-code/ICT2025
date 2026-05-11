# Repository Guidelines

## Project Structure & Module Organization

This repository is a Markdown-based university notes workspace for Big Data Computing. Source notes live in `Notes/`, with raw or draft material in `ToSummarize/`. Homework writeups and supporting material are in `Homeworks/`, while lecture PDFs and other course assets are in `Slides/`. Agent and automation helpers, when present, live under `.agents/`. Images should be stored in a course-local `Pics/` folder and embedded with Obsidian syntax such as `![[Pics/diagram.png|500]]`.

## Build, Test, and Development Commands

There is no application build or test suite. Use optional validation/export commands when needed:

```bash
markdownlint "**/*.md" --ignore ".obsidian/" --ignore "logseq/"
```

Checks Markdown formatting if `markdownlint-cli` is installed.

```bash
pandoc "Notes/1.MapReduce2526.md" -o "MapReduce.pdf" --template=../formatting.yaml
```

Exports a note to PDF using the shared Pandoc/LaTeX configuration. Adjust the relative path to `formatting.yaml` if running from another directory.

## Markdown Style & Naming Conventions

Use ATX headings (`#`, `##`) and keep paragraphs readable, ideally around 100 characters per line. Use `-` for unordered lists and `1.` for ordered lists. Always label fenced code blocks, for example ` ```python ` or ` ```cpp `. Use single-dollar inline math (`$E = mc^2$`) and separate `$$` blocks for displayed equations. Prefer Obsidian wiki-links for internal references, such as `[[1.MapReduce2526]]`.

Name sequential notes with a numeric prefix and descriptive title, matching existing files such as `Notes/3.WordCountSpark.md` or `ToSummarize/6. Streaming2526-1.md`.

## Testing Guidelines

No automated tests are required. Before committing, preview edited notes in Obsidian or another Markdown viewer and run `markdownlint` for larger edits. For LaTeX-heavy notes, export at least one affected file with Pandoc to catch broken math, missing images, or malformed tables.

## Commit & Pull Request Guidelines

Recent history uses short, imperative or descriptive commit messages such as `Added codex skill` and `Stochastic rewrites`. Keep commits focused on one course topic or maintenance task, for example `Add Spark streaming notes`.

Pull requests should summarize changed notes, list any generated PDFs or assets, and mention whether Markdown linting or Pandoc export was checked. Include screenshots only when visual formatting, diagrams, or rendered equations are important to review.

## Security & Academic Integrity

Do not commit secrets, account data, or private course platform credentials. Notes should be rewritten in your own words and cite external material where appropriate.
