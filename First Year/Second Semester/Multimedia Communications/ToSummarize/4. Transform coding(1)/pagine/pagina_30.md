Orthogonal Transforms and Coding Gain

The **Coding Gain** of the transform $\mathcal{T}$ is the ratio between the distortion on the original data and the transform coding distortion:

$$G_{\mathcal{T}} = \frac{\mathcal{D}_{\text{PCM}}}{\mathcal{D}_{\mathcal{T}}} = \frac{c_{\mathcal{N}} \sigma_X^2 2^{-2\bar{R}}}{c_{\mathcal{N}} \sigma_{\text{GM},Y} 2^{-2\bar{R}}} = \frac{\sigma_{\text{AM},Y}^2}{\sigma_{\text{GM},Y}^2}$$

The ratio between the AM and the GM of the variances of $Y$ is the so-called **coding gain** of the transform

Remember that for any OT $\mathcal{T}$, $\sigma_{\text{AM},Y}^2$ is always the same: thus we look for a transform that minimizes $\sigma_{\text{GM},Y}^2$

This supports the idea that the transform must sparsify the signal, i.e. make the variances as diverse as possible

---

**Immagini estratte:**

![Figura estratta 1](images/p30_img01.jpg)
