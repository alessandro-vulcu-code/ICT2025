Entropy coding

▶ It easy to find an instantaneous code such that $\mathcal{L} < H(X) + 1$, we just take $\ell_i = \lceil -\log_2 p_i \rceil$

▶ Kraft's inequality is satisfied:

$$\ell_i = -\log p_i + \delta_i$$
$$2^{-\ell_i} = p_i \times 2^{-\delta_i} = \epsilon_i p_i$$
$$\sum_i 2^{-\ell_i} = \sum_i \epsilon_i p_i \leq \sum_i p_i = 1$$

▶ The average length is obtained as follows:

$$\ell_i = \lceil -\log_2 p_i \rceil < -\log_2 p_i + 1$$
$$\sum_i p_i \ell_i < \sum_i (-p_i \log_2 p_i + p_i)$$
$$p_i \ell_i < -p_i \log_2 p_i + p_i$$
$$\mathcal{L} < H(X) + 1$$

▶ Since $\mathcal{L}^* \leq \mathcal{L}$, $H(X) \leq \mathcal{L}^* < H(X) + 1$

---

**Immagini estratte:**

![Figura estratta 1](images/p51_img01.jpg)
