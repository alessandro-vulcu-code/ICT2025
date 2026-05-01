Lloyd-Max algorithm: centroid condition

Given the thresholds $\{t^0, \ldots, t^L\}$, the best levels are those minimizing the distortion:

$$\sigma_Q^2 = \sum_{i=1}^{L} \int_{t^{i-1}}^{t^i} (u - \hat{x}^i)^2 p_X(u) du$$

To find the optimal levels, we compute the gradient of the distortion and set it to 0.

$$\frac{\partial \sigma_Q^2}{\partial \hat{x}^i} = \frac{\partial}{\partial \hat{x}^i} \int_{t^{i-1}}^{t^i} (u - \hat{x}^i)^2 p_X(u) du = \int_{t^{i-1}}^{t^i} \frac{\partial}{\partial \hat{x}^i} (u - \hat{x}^i)^2 p_X(u) du$$

$$= \int_{t^{i-1}}^{t^i} 2(\hat{x}^i - u) p_X(u) du = 2\hat{x}^i \int_{t^{i-1}}^{t^i} p_X(u) du - 2 \int_{t^{i-1}}^{t^i} up_X(u) du$$

$$\hat{x}^i = \frac{\int_{t^{i-1}}^{t^i} up_X(u) du}{\int_{t^{i-1}}^{t^i} p_X(u) du} = \frac{\int_{\Theta_i} up_X(u) du}{\int_{\Theta_i} p_X(u) du} = \text{E} [X | X \in \Theta_i]$$

This is the so-called centroid condition: the best representative of a quantization region is its centroid, i.e. the conditional average of $X$ given $X \in \Theta^i$

---

**Immagini estratte:**

![Figura estratta 1](images/p89_img01.jpg)
