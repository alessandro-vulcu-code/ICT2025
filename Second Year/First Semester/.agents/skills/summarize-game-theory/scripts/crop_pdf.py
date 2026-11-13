#!/usr/bin/env python3
"""Render a visually selected PDF region to PNG without losing vector content."""

import argparse
import math
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--page", type=int, required=True, help="PDF page index, starting at 1")
    parser.add_argument("--box", type=float, nargs=4, required=True,
                        metavar=("X0", "Y0", "X1", "Y1"),
                        help="PDF points, top-left origin, rendered page orientation")
    parser.add_argument("--dpi", type=int, default=200)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        import fitz
    except ImportError:
        parser.exit(1, "PyMuPDF is required (Python module: fitz).\n")
    if not 72 <= args.dpi <= 600:
        parser.error("--dpi must be between 72 and 600")
    if args.output.suffix.lower() != ".png":
        parser.error("--output must end in .png")
    if args.output.exists():
        parser.error("output already exists; choose a new filename")
    x0, y0, x1, y1 = args.box
    if not all(math.isfinite(v) for v in args.box) or x0 >= x1 or y0 >= y1:
        parser.error("--box requires finite coordinates with X0 < X1 and Y0 < Y1")
    try:
        with fitz.open(args.pdf) as doc:
            if not 1 <= args.page <= len(doc):
                parser.error(f"--page must be between 1 and {len(doc)}")
            page = doc[args.page - 1]
            clip = fitz.Rect(args.box)
            if not page.rect.contains(clip):
                parser.error(f"--box must lie inside page bounds {tuple(page.rect)}")
            pixmap = page.get_pixmap(clip=clip, dpi=args.dpi, alpha=False)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            pixmap.save(args.output)
            print(f"Saved {args.output} ({pixmap.width} x {pixmap.height} px)")
    except (OSError, RuntimeError, ValueError) as exc:
        parser.exit(1, f"Crop failed: {exc}\n")


if __name__ == "__main__":
    main()
