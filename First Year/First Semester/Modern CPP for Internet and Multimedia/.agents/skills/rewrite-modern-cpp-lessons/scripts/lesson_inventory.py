#!/usr/bin/env python3
"""List Modern C++ lesson Markdown files and check local image references."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


def is_remote_or_anchor(target: str) -> bool:
    return (
        "://" in target
        or target.startswith("#")
        or target.startswith("mailto:")
        or target.startswith("data:")
    )


def primary_lessons(root: Path) -> list[Path]:
    lessons: list[Path] = []
    for path in sorted(root.rglob("*.md")):
        if "pagine" in path.parts:
            continue
        lessons.append(path)
    return lessons


def image_refs(markdown_path: Path) -> tuple[list[Path], list[str]]:
    existing: list[Path] = []
    missing: list[str] = []
    text = markdown_path.read_text(encoding="utf-8", errors="replace")
    for raw_target in IMAGE_RE.findall(text):
        target = raw_target.strip().split()[0]
        if is_remote_or_anchor(target):
            continue
        candidate = (markdown_path.parent / target).resolve()
        if candidate.exists() and candidate.suffix.lower() in IMAGE_EXTS:
            existing.append(candidate)
        else:
            missing.append(raw_target)
    return existing, missing


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Inventory aggregate Markdown lessons and local image links."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default="MD Lessons",
        help="Root directory containing Modern C++ Markdown lessons.",
    )
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        raise SystemExit(f"Root directory not found: {root}")

    for lesson in primary_lessons(root):
        existing, missing = image_refs(lesson)
        print(lesson)
        print(f"  existing_images: {len(existing)}")
        for path in existing:
            print(f"    ok: {path.relative_to(Path.cwd())}")
        print(f"  missing_image_refs: {len(missing)}")
        for ref in missing:
            print(f"    missing: {ref}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
