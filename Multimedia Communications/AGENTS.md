# Repository Guidelines

## Project Structure & Module Organization

This repository contains Markdown notes and course materials for Multimedia Communications. Main folders:

- `Notes/`: primary lecture notes and working Markdown files.
- `Summaries/`: polished chapter summaries, usually named with a numeric prefix such as `1. Introduction to Multimedia Compression.md`.
- `ToSummarize/`: source material and page-level extracts used to create summaries.
- `Pics/`: images grouped by topic, for example `Pics/Transform coding/`.
- `Slides/`: course slide files.
- `old/`: archived drafts or previous versions.

There is no application source tree or automated test suite. Treat Markdown files and referenced images as the main project assets.

## Build, Test, and Development Commands

No build is required for normal note editing. Useful optional commands:

```bash
markdownlint "**/*.md" --ignore ".obsidian/" --ignore "logseq/"
```

Checks Markdown style if `markdownlint-cli` is installed.

```bash
pandoc "Notes/file.md" -o "output.pdf"
```

Exports a note to PDF when Pandoc and the required LaTeX tools are available.

```bash
python3 update_images.py
```

Runs the local image-reference helper script. Inspect its behavior before using it on new material.

## Formatting & Naming Conventions

Use ATX headings (`#`, `##`) and concise academic prose. Prefer `-` for unordered lists and `1.` for ordered lists. Specify languages on fenced code blocks, such as ` ```python ` or ` ```cpp `.

Use single-dollar inline math, for example `$E = mc^2$`, and separate block math with `$$` delimiters. Keep Obsidian wiki-links and embeds when they improve navigation: `[[Related Topic]]`, `![[image.png|500]]`.

Name topic files with progressive numeric prefixes and sentence case: `4. Transform coding.md`. Place topic images under the matching `Pics/<Topic>/` folder.

## Review & Validation Guidelines

Before committing, open edited notes in Obsidian or a Markdown preview and check headings, equations, image embeds, and internal links. Run `markdownlint` when making broad formatting changes. For PDF-oriented notes, test one representative Pandoc export.

## Commit & Pull Request Guidelines

Recent commits use short, descriptive messages such as `Added Multimedia notes` or `Stochastic rewrites`. Keep commit messages imperative or descriptive and mention the affected topic.

Pull requests should summarize changed topics, list added or moved assets, and note any generated files. Include screenshots only when visual formatting, diagrams, or exported PDFs are materially changed.

## Security & Academic Integrity

Do not commit credentials, private data, or unrelated local editor state. Notes should reflect original understanding and properly transformed course material, not unreviewed copied text.
