The Discrete Fourier Transform (DFT)

Definition of the 1D DFT Given a signal $x[n]$ of length $M$, the transform coefficients $y[k]$ are defined as:

$$y[k] = \frac{1}{\sqrt{M}} \sum_{n=1}^{M} x[n] e^{-j \frac{2\pi}{M} kn}, \quad k = 1 \ldots, M$$

Note: The factor $1/\sqrt{M}$ is necessary for the transform to be orthonormal (unitary).

Matrix Formulation The DFT is a linear transform that can be expressed as a matrix-vector product: $Y = \mathcal{T}_{DFT} X$ where $X$ and $Y$ are the vectors obtained by the signals' samples.

---

**Immagini estratte:**

![Figura estratta 1](p65_img01.jpg)
