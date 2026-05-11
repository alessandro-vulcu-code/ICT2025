# Repository Guidelines

## Project Structure & Module Organization

This is a university notes workspace for Modern C++ and related material. Primary notes live in `Modern CPP/` as numbered Markdown files, with labs in `Modern CPP/Lab/` and images in `Modern CPP/Pictures/`. Source or converted lessons are grouped under `MD Lessons/`. Supporting C++ examples are in `Codes/`. LaTeX artifacts and shared preamble files are under `Latex/`; `LdP/` contains additional references, notes, and images.

There is no application source tree or formal test suite. Treat notes, PDFs, images, LaTeX, and C++ examples as the main assets.

## Build, Test, and Development Commands

No build step is required for normal note editing. Useful optional commands:

```bash
markdownlint "**/*.md" --ignore "logseq/" --ignore ".obsidian/"
```

Checks Markdown formatting.

```bash
pandoc "Modern CPP/19. Socket.md" -o "Socket.pdf" --template=formatting.yaml
```

Exports a note to PDF from the wider `ICT2025/` root when `formatting.yaml` is available.

```bash
g++ -std=c++20 Codes/thread_example.cpp -o Codes/thread_example
```

Compiles an example C++ file when changing code snippets or demos.

## Coding Style & Naming Conventions

Use ATX headings (`#`, `##`) and numbered lesson filenames such as `19. Socket.md`. Keep note titles in sentence case. Use `-` for unordered lists and `1.` for ordered lists. Prefer fenced code blocks with an explicit language, for example ` ```cpp `. Inline math uses `$...$`; display math uses `$$` blocks.

For C++ examples, prefer modern course style: clear names, brace initialization where appropriate, and standard-library facilities over manual resource management.

## Testing Guidelines

There are no required tests. For Markdown changes, preview notes in Obsidian or run `markdownlint`. For LaTeX-heavy notes, export with Pandoc or the configured LaTeX Workshop recipe. For C++ examples, compile the touched file with `g++` and run the binary if it demonstrates runtime behavior.

## Commit & Pull Request Guidelines

Recent history uses short messages, sometimes with a conventional prefix such as `feat(multimedia): add video coding notes and rewrite skill`. Keep commits focused on one topic, for example `Add notes for smart pointers` or `fix(cpp): correct thread example`.

Pull requests should summarize changed notes or examples, mention generated PDFs or images, and include screenshots only when visual formatting changed. Avoid committing personal workspace state, secrets, or unrelated generated files.

## Agent-Specific Instructions

Preserve existing note structure and Obsidian syntax such as `[[Wiki Links]]`, image embeds, and callouts. Do not rewrite large sections unless asked; keep edits scoped, factual, and consistent with the surrounding lesson style.
