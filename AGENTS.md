# AGENTS.md - ICT2025 University Notes Repository

This repository contains university course notes in Markdown format with LaTeX support.

## Repository Structure

```
ICT2025/
├── {Course Name}/          # One folder per course
│   ├── Notes/             # Lecture notes (.md files)
│   ├── Slides/            # Course slides
│   └── Labs/              # Lab materials
├── formatting.yaml        # LaTeX export configuration
└── .obsidian/             # Obsidian configuration
```

## Commands

This is a documentation repository. No build/test/lint commands are required.

### Markdown Validation (Optional)

```bash
# Install markdownlint for markdown checking
npm install -g markdownlint-cli
markdownlint "**/*.md" --ignore "logseq/" --ignore ".obsidian/"
```

### LaTeX Export

Uses pandoc with formatting.yaml configuration:

```bash
# Convert single markdown to PDF
pandoc "Notes/file.md" -o "output.pdf" --template=formatting.yaml

# VS Code: Use LaTeX Workshop extension with xelatex recipe
```

## Code Style Guidelines

### Markdown Formatting

- **Line length**: No strict limit, but keep paragraphs readable (wrap at ~100 chars)
- **Headers**: Use ATX style (`# Header`), not Setext
- **Lists**: Use `-` for unordered, `1.` for ordered
- **Emphasis**: Use `**bold**` and `*italic*` (not underscores)
- **Code blocks**: Always specify language (e.g., ` ```cpp `)

### File Naming Conventions

- Use descriptive names: `{number}. {Topic}.md` (e.g., `1. Types and declarations.md`)
- Use sentence case for titles within files
- Avoid spaces in folder names where possible
- Use kebab-case or descriptive names: `Labs 25-26/`, `Latex last summaries/`

### LaTeX Math

- **Inline math**: Use single `$` delimiters: `$E = mc^2$`
- **Block math**: Use `$$` delimiters on separate lines:
  ```markdown
  $$
  \mathcal{D}(f, \tilde{f}) = \frac{1}{NM} \sum \epsilon^2
  $$
  ```
- **Math operators**: Use `\mathcal{}` for fancy letters, `\text{}` for text in math
- **Escaping**: Always escape underscores in math mode: `\sigma_{xy}`

### Obsidian-Specific Syntax

This repository uses Obsidian for note-taking. Supported syntax:

- **Wiki-links**: `[[Internal Link]]` for note linking
- **Image embeds**: `![[Pasted image YYYYMMDDHHMMSS.png]]`
- **Image sizing**: `![[image.png|500]]` for 500px width
- **Callouts**: Use standard format:
  ```markdown
  > [!info] Definition — Title
  > Content here

  > [!warning] Warning
  > Important warning content
  ```
- **Tags**: Use `#tag` for categorization

### Code Blocks

Always specify the language for syntax highlighting:

```cpp
// C++ code example
bool flag {true};
```

```python
# Python code example
def function():
    pass
```

### Tables

Use GitHub-flavored markdown tables with alignment:

```markdown
|Column 1|Column 2|Column 3|
|---|---|---|
|Left|Center|Right|
```

## Content Guidelines

### Note Organization

1. **One concept per file**: Each `.md` file should cover a cohesive topic
2. **Progressive numbering**: Use `{number}. {Title}.md` for sequential topics
3. **Cross-references**: Link related notes using `[[File Name]]`

### Writing Style

- Use clear, concise academic language
- Define terms using callouts: `> [!info] Definition — Term`
- Include examples for complex concepts
- Add visual aids (images, diagrams) where helpful

### Image Handling

- Store images in `Pics/` folder within each course directory
- Use Obsidian's paste-to-embed feature (creates `Pasted image...` files)
- Prefer PNG for diagrams, JPEG for photos
- Include alt text or descriptive captions

## Git Workflow

```bash
# Standard workflow for notes
git add .
git commit -m "Add notes for [topic]"
git push origin main
```

### .gitignore

Repository excludes:
- `.obsidian/plugins/remotely-save/` (plugin that caused sync issues)
- `.obsidian/workspace.json` and `last-update.json` (layout files)
- `.obsidian/plugins/**/*.js` (plugin JS files)

## LaTeX Export Configuration

See `formatting.yaml` for PDF export settings:
- Document class: `book`
- Font size: 11pt
- Margins: 2.5cm
- Packages: `fancyhdr`, `amsmath`, `amssymb`

## VS Code Settings

LaTeX Workshop is configured for xelatex compilation:
- Recipe: `xelatex` or `latexmk (xelatex)`
- Flags: `-synctex=1`, `-interaction=nonstopmode`

## Important Reminders

1. **No secrets**: Never commit API keys, passwords, or personal data
2. **Academic integrity**: Notes should reflect your understanding, not copy-pasted content
3. **Regular commits**: Commit notes regularly to prevent loss
4. **Backup**: This repo serves as backup - keep it synced
