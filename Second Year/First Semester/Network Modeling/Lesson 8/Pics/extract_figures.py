"""Regenerate faithful figure crops from Lesson 8.pdf (PyMuPDF required)."""
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parent
FIGURES = [
    (1, (0.012, 0.053, 0.72, 0.21), '01-shaper-and-link.png'),
    (1, (0.018, 0.41, 0.995, 0.623), '02-above-declared-peak.png'),
    (1, (0.018, 0.702, 0.995, 0.892), '03-below-declared-peak.png'),
    (2, (0.15, 0.43, 0.69, 0.55), '04-sensor-packets.png'),
    (2, (0.002, 0.56, 0.97, 0.857), '05-sensor-fluid-profile.png'),
    (3, (0.01, 0.86, 0.995, 0.995), '06-empty-bucket-alarm.png'),
    (4, (0.015, 0.007, 0.535, 0.175), '07-board-two-alarms.png'),
]
with fitz.open(ROOT.parent / 'Lesson 8.pdf') as doc:
    for page_no, bounds, filename in FIGURES:
        page = doc[page_no - 1]
        w, h = page.rect.width, page.rect.height
        clip = fitz.Rect(bounds[0]*w, bounds[1]*h, bounds[2]*w, bounds[3]*h)
        page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=clip).save(ROOT / filename)
