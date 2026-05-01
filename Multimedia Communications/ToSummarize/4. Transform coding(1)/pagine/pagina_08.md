Block coding

Let us continue the calculation of $\mathcal{D}$:

$$\mathcal{D} = \frac{1}{M} \mathrm{E} \left[ \sum_{k=1}^{M} \left(X_k - Q(X_k)\right)^2 \right] = \frac{1}{M} \sum_{k=1}^{M} \mathrm{E} \left[ \left(X_k - Q(X_k)\right)^2 \right]$$

$$= \frac{1}{M} \sum_{k=1}^{M} \mathcal{D}_k = \frac{1}{M} \sum_{k=1}^{M} c_k \sigma_k^2 2^{-2R_k}$$

The problem of block coding, also known as resource allocation problem, is to find the rate vector $R = \left[R_1, \ldots, R_M\right]^T$ such that the global distortion is minimized under a constraint on the total rate $\sum_{k=1}^{M} R_k = R_{\text{Tot}}$. This problem can be solved using Lagrange multipliers.

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)
