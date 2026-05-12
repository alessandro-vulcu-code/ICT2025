Perfect reconstruction conditions

Matrix form

If the analysis filter bank is given, the synthesis one is determined by:

$$\begin{bmatrix}
H_0(z) & H_1(z) \\
H_0(-z) & H_1(-z)
\end{bmatrix} \cdot \begin{bmatrix}
F_0(z) \\
F_1(z)
\end{bmatrix} = \begin{bmatrix}
2z^{-\ell} \\
0
\end{bmatrix}$$

We need the modulation matrix to be invertible, ie.

$$\forall z \in \mathbb{C}: |z| = 1, \quad \Delta(z) = H_0(z)H_1(-z) - H_1(z)H_0(-z) \neq 0$$

---

**Immagini estratte:**

![Figura estratta 1](images/p30_img01.jpg)
