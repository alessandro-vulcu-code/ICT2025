DFT Transformation Matrix

The DFT transformation matrix is defined as:

$$\mathcal{T}_{\text{DFT}} = \frac{1}{\sqrt{M}} \begin{bmatrix}
1 & 1 & 1 & \cdots & 1 \\
1 & W_M & W_M^2 & \cdots & W_M^{M-1} \\
1 & W_M^2 & W_M^4 & \cdots & W_M^{2(M-1)} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & W_M^{M-1} & W_M^{2(M-1)} & \cdots & W_M^{(M-1)(M-1)}
\end{bmatrix}$$

where $W_M = e^{-j2\pi/M}$ is the Mth primitive root of unity.

Each row of this matrix is the conjugate of one basis vector.

The transformation consists in computing the scalar product of $X$ with each of the basis vector.

This scalar product tells “how much similar” $X$ is to each of the basis vectors

---

**Immagini estratte:**

![Figura estratta 1](images/p66_img01.jpg)
