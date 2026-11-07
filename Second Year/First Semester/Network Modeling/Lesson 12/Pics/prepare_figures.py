"""Reproduce Lesson 12 crops and analytical redraws; run from any directory."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
# Crop coordinates refer to the inspected 1273 x 1800 page previews.
crops = [
    (0, (375, 865, 900, 1105), '01-mean-paths.png'),
    (0, (810, 1528, 1265, 1780), '03-mean-distributions.png'),
    (1, (815, 85, 1273, 395), '04-error-tails.png'),
    (1, (145, 1190, 915, 1490), '05-cac-system.png'),
    (2, (15, 760, 1200, 1550), '06-estimator-options.png'),
]
if '--plots-only' not in sys.argv:
    import fitz
    doc = fitz.open(HERE.parent / 'Lesson 12.pdf')
    for page, box, name in crops:
        p = doc[page]
        rect = fitz.Rect(box[0] * p.rect.width / 1273,
                         box[1] * p.rect.height / 1800,
                         box[2] * p.rect.width / 1273,
                         box[3] * p.rect.height / 1800)
        p.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect).save(HERE / name)
if '--crops-only' in sys.argv:
    sys.exit(0)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 13, 'axes.spines.top': False,
                     'axes.spines.right': False})
fig, ax = plt.subplots(figsize=(7, 3.2), constrained_layout=True)
n = np.linspace(1, 12, 500)
ax.plot(n, 1/n, color='#ce23cc', lw=2.5)
ax.set(xlim=(0, 12.5), ylim=(0, 1.1), xlabel='$N$',
       ylabel='$\\sigma_{S_N}^2$', xticks=[1], yticks=[1],
       yticklabels=['$\\sigma_x^2$'])
ax.text(4, .55, '$\\sigma_{S_N}^2=\\sigma_x^2/N$')
fig.savefig(HERE / '02-variance.png', dpi=180)
plt.close(fig)

# Dimensionless geometry only; no numerical theta or probability is asserted.
fig, ax = plt.subplots(figsize=(6, 3.4), constrained_layout=True)
t = np.linspace(-.3, 2.35, 400)
ax.plot(t, t*t-2*t, color='#b632db', lw=2.5)
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)
ax.plot([1, 1], [0, -1], '--', color='gray')
ax.set(xticks=[0, 1], xticklabels=['$0$', '$\\theta^*$'], yticks=[],
       xlabel='$\\theta$', ylabel='$f(\\theta)$')
ax.text(.45, .75, 'Schematic: convex exponent')
fig.savefig(HERE / '07-convex-exponent.png', dpi=180)
plt.close(fig)
