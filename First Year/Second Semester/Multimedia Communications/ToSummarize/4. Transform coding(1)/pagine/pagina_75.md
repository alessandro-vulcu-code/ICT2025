DFT as a compression tool

The DFT is never directly used for compression because of the **frequency leakage** DFT is the discrete-time analogous of the **Fourier Series**.

This means that with the DFT we analyze a periodized version $x_{\text{PER}}$ of the original signal $x$.

This periodized version introduces high-frequency content ("jumps") near the signal boundaries.

To represent this artificial "jump" in the frequency domain, the DFT must generate **high-frequency coefficients** with significant energy.

- This is a form of **spectral leakage**: energy that should be in the low frequencies "leaks" into the high ones.
- Result: The representation is **less sparse** than it could be, making compression much less effective.

Thus, even a smooth signal will have relatively high-frequency content just because of periodization.

---

**Immagini estratte:**

![Figura estratta 1](p75_img01.jpg)
