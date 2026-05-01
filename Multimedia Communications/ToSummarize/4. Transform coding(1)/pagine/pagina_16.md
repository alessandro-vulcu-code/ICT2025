Case of i.d. random variables

Coding of multimedia signals: the samples are reasonably identically distributed, even though they are not independent
In this case,

$$\forall k \in \{1, \ldots, M\} \sigma_k^2 = \sigma_X^2$$
$$c_k = c_X$$
$$R_k^* = \bar{R} + \frac{1}{2} \log_2 \frac{c_k \sigma_k^2}{c_GM \sigma_GM^2} = \bar{R}$$
$$\mathcal{D}_k^* = c_GM \sigma_GM^2 2^{-2\bar{R}} = c_X \sigma_X^2 2^{-2\bar{R}}$$
$$\mathcal{D} = c_GM \sigma_GM^2 2^{-2\bar{R}} = c_X \sigma_X^2 2^{-2\bar{R}}$$

Samples are i.d., the signal is not sparse (all the samples are equally important). Thus, block coding does not really brings in any improvement. But the distortion might be reduced if we manage to reduce $\sigma_GM^2$.

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)
