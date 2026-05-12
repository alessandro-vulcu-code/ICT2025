1. Autoregressive Models: Causal Density Estimation

Mathematical Foundation

These models treat the image as a sequence of random variables and apply the Chain Rule of probability:

$$P(x_1, \ldots, x_n) = \prod_{i=1}^{n} P(x_i \mid x_1, \ldots, x_{i-1})$$

▶ **Working Principle**: The network estimates the conditional PDF of the current pixel $x_i$ given all previous pixels (causal context).

▶ **Information Theory**: Since the model captures high-order dependencies, the bit-rate approaches the Entropy Rate $\mathcal{H}$.

▶ **Trade-off:**

---

**Immagini estratte:**

![Figura estratta 1](images/p167_img01.jpg)
