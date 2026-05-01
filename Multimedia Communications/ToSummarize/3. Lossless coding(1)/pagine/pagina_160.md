DPCM: 1D (horizontal) Spatial Prediction

To exploit spatial correlation, we define a predictor $p(n)$ based on the previous pixel:

$$p(n) = x(n - 1) \implies \text{Error: } y(n) = x(n) - x(n - 1)$$

Sample prediction is often referred to as DPCM (for Differential Pulse Coding Modulation)

- Residual Entropy: 3.312 bpp.
- Signed Exp-Golomb: 3.428 bpp.
- Huffman: 3.383 bpp.
- ZIP: 3.230 bpp.

The signal is now less correlated, and the error is centered at zero.

---

**Immagini estratte:**

![Figura estratta 1](images/p160_img02.jpg)

![Figura estratta 2](images/p160_img01.jpg)
