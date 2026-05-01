Linear Transforms as sparsifying operators

Let us consider $Y = \mathcal{T}X$, where $\mathcal{T}$ is an invertible matrix

- We can always find back $X$ from $Y$ using the inverse matrix $\mathcal{T}^{-1}$
- It can be interpreted as basis change i.e. a coordinate change
  - As such, the basis is a set of signals which are used to reconstruct the intended signal
  - Therefore the basis should be relevant to the nature of the signals
  - Sinusoidal signals appear to be a good choice for sound
  - It is also a reasonable choice for images in particular considering the contrast sensitivity dependence on frequency in HVS
- If the matrix is orthogonal, the quantization error is the same on $X$ and $Y$ (see later)
- We should look for the matrix $\mathcal{T}$ that minimizes the GM of the variances of $Y = \mathcal{T}X$

---

**Immagini estratte:**

![Figura estratta 1](images/p21_img01.jpg)
