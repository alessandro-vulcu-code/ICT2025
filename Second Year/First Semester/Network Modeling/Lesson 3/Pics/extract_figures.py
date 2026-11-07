"""Reproduce inspected handwritten figure crops from Lesson 3-notes.pdf."""
from pathlib import Path
import fitz

HERE = Path(__file__).resolve().parent
doc = fitz.open(HERE.parent / 'Lesson 3-notes.pdf')
# Coordinates in inspected 1273 x 1800 previews. Render at 3 pixels/PDF point.
CROPS = [
    (0, (45, 695, 1120, 1060), '01-network-modules.png'),
    (2, (55, 65, 430, 300), '02-demand-axes.png'),
    (3, (55, 330, 620, 630), '03-downloader-utilities.png'),
    (3, (630, 350, 1260, 635), '04-watcher-utility.png'),
    (3, (35, 1515, 700, 1800), '05-company-network.png'),
    (4, (40, 275, 500, 545), '06-videocall-utility.png'),
    (4, (570, 275, 1255, 550), '07-blockage-curves.png'),
    (4, (300, 1235, 860, 1600), '08-counting-process.png'),
]
for page, bounds, filename in CROPS:
    p = doc[page]
    rect = fitz.Rect(bounds[0]*p.rect.width/1273,
                     bounds[1]*p.rect.height/1800,
                     bounds[2]*p.rect.width/1273,
                     bounds[3]*p.rect.height/1800)
    p.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect).save(HERE / filename)
