# Uniform Quantization: RD curve

Let us apply these results to find the distortion of a uniform RV quantized with UQ.

**Hypotheses:** $X \sim \mathcal{U} \left( -\frac{A}{2}, \frac{A}{2} \right)$ and $Q(x)$ is a uniform quantizer with $L$ levels.

**Goal:** Find $\sigma_Q^2 = \mathbb{E} \left[ (X - \hat{X})^2 \right]$ as a function of $A, L$.

We observe that $\sigma_Q^2 = \mathbb{E} \left[ g(X) \right]$, where $\forall u \in \mathbb{R}, g(u) = (u - Q(u))^2$.

$$\sigma_Q^2 = \mathbb{E} \left[ (X - \hat{X})^2 \right]$$
$$\ldots = \sum_{i=1}^{L} \int_{\Theta^i} \frac{1}{A} \left[ u - \hat{x}^i \right]^2 du$$
$$= \frac{1}{A} \sum_{i=1}^{L} \int_{-\Delta/2}^{\Delta/2} t^2 dt$$
$$= \frac{1}{A} L \frac{\Delta^3}{12} = \frac{\Delta^2}{12} = \frac{1}{12} \frac{A^2}{L^2}$$

---

**Immagini estratte:**

![Figura estratta 1](images/p77_img01.jpg)
