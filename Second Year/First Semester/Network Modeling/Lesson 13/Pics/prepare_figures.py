"""Extract original diagrams; deliberately exclude the p. 3 blackboard photo."""
from pathlib import Path
import fitz

HERE = Path(__file__).resolve().parent
doc = fitz.open(HERE.parent / "Lesson 13.pdf")
# Normalized rectangles, measured against the complete handwritten pages.
FIGURES = [
    (3, (0.00, 0.735, 0.465, 1.00), "01-chernoff-maximum.png"),
    (5, (0.135, 0.065, 0.73, 0.185), "02-cac-system.png"),
    (6, (0.14, 0.52, 0.46, 0.62), "03-buffer-link.png"),
    (6, (0.57, 0.49, 0.95, 0.62), "04-excess-traffic.png"),
]
for number, bounds, name in FIGURES:
    page = doc[number - 1]
    w, h = page.rect.width, page.rect.height
    clip = fitz.Rect(bounds[0]*w, bounds[1]*h, bounds[2]*w, bounds[3]*h)
    page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip).save(HERE / name)
