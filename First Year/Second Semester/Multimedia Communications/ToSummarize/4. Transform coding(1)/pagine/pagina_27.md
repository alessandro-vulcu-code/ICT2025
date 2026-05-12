Orthogonal Transforms and Coding Gain

- Remember that the transform coding paradigm consists in computing $Y = \mathcal{T}X$, apply quantization to $Y$, and obtain $\hat{Y} = Q(Y)$
- The decoded version of $X$ is $\hat{X} = \mathcal{T}^{-1}\hat{Y}$
- Let us compute the distortion of $X$ in the case of transform coding, $\mathcal{D}_T$
- Remember that, since we use orthogonal transforms, the distortion can be computed directly on $Y$:

$$\mathcal{D}_T = \frac{1}{M} \text{E} \left\| X - \hat{X} \right\|^2 = \frac{1}{M} \text{E} \left\| \mathcal{T}^{-1} Y - \mathcal{T}^{-1} \hat{Y} \right\|^2 = \frac{1}{M} \text{E} \left\| Y - \hat{Y} \right\|^2 = \mathcal{D}_Y$$

---

**Immagini estratte:**

![Figura estratta 1](images/p27_img01.jpg)
