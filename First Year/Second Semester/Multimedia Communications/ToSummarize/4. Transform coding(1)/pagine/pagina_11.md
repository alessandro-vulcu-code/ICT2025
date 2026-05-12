Resource allocation: Problem formulation

▶ Minimize $\mathcal{D}$ under a rate constraint
$$\min \mathcal{D}(R) = \frac{1}{M} \sum_{k=0}^{M-1} c_k \sigma_k^2 2^{-2R_k}$$

subject to $\sum_{k=0}^{M-1} R_k \leq R_{\text{Tot}}$

▶ Lagrange method. Minimize:
$$J(R, \lambda) = \frac{1}{M} \sum_{k=0}^{M-1} c_k \sigma_k^2 2^{-2R_k} + \lambda \left( \sum_{k=0}^{M-1} R_k - R_{\text{Tot}} \right)$$

▶ Solution (Huang-Schulteiss formula):
$$R_k^* = \frac{R_{\text{Tot}}}{M} + \frac{1}{2} \log \left[ \frac{c_k \sigma_k^2}{c_{\text{GM}} \sigma_{\text{GM}}^2} \right]$$

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)
