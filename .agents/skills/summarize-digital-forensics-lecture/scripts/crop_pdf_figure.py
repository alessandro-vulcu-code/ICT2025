#!/usr/bin/env python3
"""Render a manually selected PDF figure rectangle as a PNG."""
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--page', type=int, required=True, help='1-based page number')
    parser.add_argument('--rect', type=float, nargs=4, required=True,
                        metavar=('X0', 'Y0', 'X1', 'Y1'),
                        help='Crop in PDF points, top-left origin')
    parser.add_argument('--dpi', type=int, default=200)
    args = parser.parse_args()
    try:
        import fitz
    except ImportError:
        parser.error('PyMuPDF is required (Python import: fitz).')
    if args.dpi <= 0:
        parser.error('--dpi must be positive')
    if args.output.suffix.lower() != '.png':
        parser.error('output must have a .png extension')
    if args.output.exists():
        parser.error('output exists; choose a new filename')
    with fitz.open(args.pdf) as doc:
        if not 1 <= args.page <= len(doc):
            parser.error(f'--page must be between 1 and {len(doc)}')
        page = doc[args.page - 1]
        rect = fitz.Rect(args.rect)
        if rect.is_empty or rect.is_infinite or not page.rect.contains(rect):
            parser.error('--rect must be nonempty and entirely inside the page')
        args.output.parent.mkdir(parents=True, exist_ok=True)
        pix = page.get_pixmap(matrix=fitz.Matrix(args.dpi / 72, args.dpi / 72),
                              clip=rect, colorspace=fitz.csRGB, alpha=False)
        pix.save(args.output)
        print(f'Saved {args.output} ({pix.width} x {pix.height} px), page {args.page}')


if __name__ == '__main__':
    main()
