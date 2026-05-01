Practical Implementation: Separability

Directly using the $N^2 \times N^2$ matrix $\mathcal{A}$ is computationally prohibitive. Fortunately, the DFT is a separable transform.

Matrix Product Formulation We can apply the transform directly to the image matrix $X$ using 1D operators:

$$Y = \mathcal{T}X\mathcal{T}^T$$

- $\mathcal{T}$ is the $N \times N$ matrix representing the 1D DFT.
- **Step 1** ($\mathcal{T}X$): Each column of the image is transformed.
- **Step 2** (Post-multiplication by $\mathcal{T}^T$): Each row of the intermediate result is transformed.
- The order of operations (rows then columns or vice-versa) does not change the result.
- We end up with horizontal and vertical frequency analysis.

---

**Immagini estratte:**

![Figura estratta 1](images/p69_img01.jpg)
