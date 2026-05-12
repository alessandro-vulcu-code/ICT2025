The 2D DFT: Theoretical Framework

The 2D Discrete Fourier Transform maps an $N \times N$ spatial image $X$ to a frequency representation $Y$.

**Vectorized Perspective.** Conceptually, we can treat the image as a single vector $x \in \mathbb{C}^{N^2}$ by stacking its columns (vectorization):

$$y = \mathcal{A}x$$

- $\mathcal{A}$ is a unitary transformation matrix of size $N^2 \times N^2$.
- The transform represents a **rigid rotation** of the coordinate system in the complex space $\mathbb{C}^{N^2}$.
- Total energy is preserved: $\|y\|^2 = \|x\|^2$.

---

**Immagini estratte:**

![Figura estratta 1](p68_img01.jpg)
