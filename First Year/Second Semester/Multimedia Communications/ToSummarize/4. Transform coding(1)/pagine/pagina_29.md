Orthogonal Transforms and Coding Gain

Assuming that resource allocation is done with optimal (H.S.) method, we get:

$$\mathcal{D}_Y = c_{\text{GM},Y} \sigma_{\text{GM},Y} 2^{-2\bar{R}}$$

If $X$ is Gaussian, also $Y$ is Gaussian and thus $c_{\text{GM},Y} = c_{\text{GM},X} = c_N$

Moreover, for any OT $\mathcal{T}$, we have

$$\sigma_{\text{AM},Y}^2 = \frac{1}{M} \sum_{k=1}^{M} \text{E} \left[ Y_k^2 \right] = \frac{1}{M} \text{E} \left[ \sum_{k=1}^{M} Y_k^2 \right] = \frac{1}{M} \text{E} \left\| Y \right\|^2 = \frac{1}{M} \text{E} \left\| X \right\|^2$$

$$= \frac{1}{M} \text{E} \left[ \sum_{k=1}^{M} X_k^2 \right] = \frac{1}{M} \sum_{k=1}^{M} \text{E} \left[ X_k^2 \right] = \sigma_{\text{AM},X}^2 = \sigma_X^2$$

Thus any OT $\mathcal{T}$ does not change the variance AM, but changes the variance GM

---

**Immagini estratte:**

![Figura estratta 1](images/p29_img01.jpg)
