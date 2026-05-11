---
name: rewrite-modern-cpp-lessons
description: Rewrite and summarize Modern C++ for Internet and Multimedia Markdown lessons converted from PDFs. Use when Codex must transform files from "MD Lessons" into complete English oral-exam study notes, preserving every topic, code example, existing image, and "5 mins questions" exam prompt.
---

# Rewrite Modern C++ Lessons

## Purpose

Rewrite one or more Markdown lessons from `MD Lessons` into clear English study notes for an oral exam in Modern C++ for Internet and Multimedia. Produce faithful, complete notes: summarize and explain, but do not skip concepts, examples, caveats, code blocks, or exam-style questions.

## Inputs

- Prefer the aggregate lesson file at `MD Lessons/<lesson folder>/<lesson title>.md`.
- Use `pagine/*.md` only when the aggregate file is missing, incomplete, or the user explicitly asks to work page by page.
- If the user asks for all lessons, process the aggregate `.md` files directly under each lesson folder and skip files under `pagine/`.
- Optionally run `scripts/lesson_inventory.py "MD Lessons"` to list lesson files and detect image references that point to missing files.

## Output Location

- If the user specifies an output path, use it.
- Otherwise write rewritten notes under `Rewritten Lessons/` at the project root, one file per lesson, preserving a readable lesson name.
- Keep output in Markdown suitable for Obsidian.
- Write the study notes in English, even if the user request is in Italian.

## Required Structure

Each rewritten lesson must use this structure:

```markdown
# <Lesson Title>

## Outline
- [Main topic](#main-topic)
  - [Subtopic](#subtopic)

## Study Notes
...

## 5 Mins Questions
...

## Final Summary
...
```

- The outline must be clickable: every bullet must link to a real heading in the same file using Markdown anchor links, for example `[Declarations](#declarations)`.
- Keep outline labels short and readable. Do not link to every tiny paragraph; link to the main topics and important subtopics.
- Make sure linked heading text and anchors stay stable if you edit section titles.

If the source contains no "5 mins questions", include `## 5 Mins Questions` only when useful and write `No 5 mins questions are present in the source material.` Do not invent exam questions unless the user explicitly asks.

## Rewriting Rules

- Preserve the original lesson order unless a small reordering is needed to make a concept understandable.
- Use heading levels intentionally: `##` for required top-level sections, `###` for main lesson topics, `####` for subtopics, and deeper levels only when genuinely useful.
- Use **bold** for important terms, keywords, and exam-relevant distinctions. Use *italics* sparingly for emphasis or nuance. Do not over-format entire sentences.
- Explain every concept clearly and precisely, using complete sentences suitable for oral-exam preparation, but keep the explanation concise.
- Make implicit slide bullets explicit: define terms, explain why they matter, and connect them to C++ behavior. Prefer tight paragraphs over long prose.
- Do not omit edge cases, warnings, limitations, definitions, references, commands, diagrams, or examples present in the source.
- Remove PDF-conversion noise such as repeated page separators only when it has no content value.
- Keep course-specific terminology, library names, shell commands, file names, compiler options, and C++ identifiers exact.
- Do not add emoji, decorative icons, AI-style filler, or casual motivational wording.
- When uncertain about a corrupted phrase, keep the original wording nearby and mark it as needing review instead of silently rewriting it.

## Code Blocks

- Preserve every source code block and command block.
- Use the correct language tag when clear, such as `cpp`, `bash`, `make`, or `text`.
- After each non-trivial code block, add an explanation covering:
  - what the code does;
  - the key C++ concepts involved;
  - ownership, lifetime, type, memory, compilation, or concurrency implications when relevant;
  - common mistakes or exam-relevant points if the slide implies them.
- Keep code explanations focused: usually one short paragraph is enough, unless the example contains several distinct pitfalls.
- Do not "simplify away" code examples. If a code block appears malformed because of PDF conversion, preserve it and add a short note explaining the likely intended form.

## Images

- Preserve image references only when the referenced image file exists on disk.
- For a Markdown image like `![...](images/p05_img02.jpg)`, resolve the path relative to the source Markdown file.
- If the image file exists, include the image in the rewritten note and adjust the link so it is valid from the output file location.
- If the image file does not exist in the corresponding images folder, omit that image reference. Do not create placeholders for missing images unless the user asks.
- Add a brief caption or explanation for included diagrams when the surrounding slide text makes the meaning clear.

## 5 Mins Questions

- Preserve all "5 mins questions", "5 min questions", and similarly named question sections.
- Keep the original question wording when possible.
- If the source provides answers or hints, include them and explain them.
- If the source only provides questions, copy the questions under `## 5 Mins Questions` without inventing answers unless the user explicitly asks for solved answers.

## Completeness Check

Before finishing a rewritten lesson:

1. Compare the source headings, page titles, code blocks, images, and question sections against the output.
2. Verify every source code block appears in the output.
3. Verify every existing source image reference appears with a valid path from the output file.
4. Verify missing images were omitted, not replaced by broken links.
5. Verify every outline link points to an existing heading in the same output file.
6. Verify heading levels reflect main topics and subtopics rather than using a flat structure.
7. Verify the note uses useful **bold** and *italic* emphasis without becoming noisy.
8. Verify the note starts with an outline and ends with a final summary.
9. Verify the output is in English and contains no emoji or decorative AI-style markers.
