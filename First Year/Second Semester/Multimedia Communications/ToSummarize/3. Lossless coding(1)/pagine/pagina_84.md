Arithmetic coding: average length

$$L(n) = -\left[ \sum_{i=1}^{n} \log_2 p(x_i) \right] + 1 < -\sum_{i=1}^{n} \log_2 p(x_i) + 2$$

$$\bar{L}(n) < \frac{-\sum_{i=1}^{n} \log_2 p(x_i) + 2}{n}$$

$$\mathcal{L} = E[\bar{L}(n)] < \frac{-\sum_{i=1}^{n} E[\log_2 p(x_i)] + 2}{n}$$

$$\mathcal{L} < H(X) + \frac{2}{n} \rightarrow H(X)$$

---

**Immagini estratte:**

![Figura estratta 1](images/p84_img01.jpg)
