2D-DCT

Just as 2D-DFT, 2D-DCT is also implemented as a separable transform
For a data matrix (block of pixels or full image) X, the 2D transform is:
$$Y = \mathcal{T}X\mathcal{T}^T$$
where $\mathcal{T}$ is the 1D transformation matrix
This is equivalent to:
1. Applying the transform to each row of X
2. Applying the transform to each column of the result
DCT only has positive frequencies: after the analysis we have:

---

**Immagini estratte:**

![Figura estratta 1](p87_img01.jpg)
