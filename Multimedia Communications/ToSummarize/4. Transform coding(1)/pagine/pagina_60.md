Optimality and the Gaussian Case

The **Coding Gain** ($G_T$) measures the efficiency of a transform compared to direct block quantization:

$$G_T = \frac{\frac{1}{M} \sum_{i=1}^{M} \sigma_i^2}{\left( \prod_{i=1}^{M} \sigma_i^2 \right)^{1/M}}$$

Theoretical Optimality:

- For **Gaussian sources**, the KLT not only decorrelates the coefficients but makes them **statistically independent**.
- The KLT maximizes the coding gain for Gaussian distributions.
- It provides the best possible MSE performance for a fixed total bit-rate $R$ in the high-bitrate regime.

---

**Immagini estratte:**

![Figura estratta 1](images/p60_img01.jpg)
