DPCM: 2D Spatial Prediction

A better predictor considers a causal neighborhood (A, B, C) for pixel X:

| C | B |
| :--- | :--- |
| A | X |

The best prediction direction is determined comparing $|B - C|$ with $|A - C|$: if the former is smaller than the latter, horizontal prediction is considered more reliable.

Performance on "house":
- Residual Entropy: 2.830 bpp.
- Huffman: 2.894 bpp.
- Signed Exp-Golomb: 2.941 bpp.
- ZIP: 3.141 bpp.

Note how large errors are much less common with respect to the 1D predictor

---

**Immagini estratte:**

![Figura estratta 1](images/p161_img02.jpg)

![Figura estratta 2](p161_img01.jpg)
