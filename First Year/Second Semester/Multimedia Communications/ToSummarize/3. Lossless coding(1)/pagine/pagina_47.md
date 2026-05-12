Optimal code

▶ But we need to drop condition $\ell_i \in \mathbb{N}$
▶ Constrained minimization:

$$\ell^* = \arg \min_{\ell} \sum_i p_i \ell_i$$

subject to $$\sum_i 2^{-\ell_i} = 1$$

$$J(\ell) = \sum_i p_i \ell_i + \lambda \left( \sum_i 2^{-\ell_i} - 1 \right)$$

$$\sum_i p_i = (\lambda \ln 2) \sum_i 2^{-\ell_i}^*$$

$$2^{-\ell_i^*} = p_i$$

$$\mathcal{L}^* = \sum_i -p_i \log_2 p_i = H(X)$$

$$\frac{\partial J}{\partial \ell_i} = p_i - (\lambda \ln 2) 2^{-\ell_i^*} = 0$$

$$1 = \lambda \ln 2$$

$$\ell_i^* = -\log_2 p_i$$

---

**Immagini estratte:**

![Figura estratta 1](p47_img01.jpg)
