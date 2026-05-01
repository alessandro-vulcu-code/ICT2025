Uniform Quantization: RD curve

Let us apply these results to find the distortion of a uniform RV quantized with UQ.

Hypotheses: $X \sim \mathcal{U} \left( -\frac{A}{2}, \frac{A}{2} \right)$ and $Q(x)$ is a uniform quantizer with $L$ levels.

Goal: Find $\sigma_Q^2 = \mathbb{E} \left[ (X - \hat{X})^2 \right]$ as a function of $A, L$

We observe that $\sigma_Q^2 = \mathbb{E} \left[ g(X) \right]$, where $\forall u \in \mathbb{R}, g(u) = (u - Q(u))^2$.

$$\sigma_Q^2 = \mathbb{E} \left[ (X - \hat{X})^2 \right] = \int_{-\infty}^{+\infty} p_X(u) [u - Q(u)]^2 du$$

---

**Immagini estratte:**

![Figura estratta 1](images/p76_img01.jpg)
