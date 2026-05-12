Lloyd-Max algorithm: nearest neighbor rule

Given $\{ \hat{x}^i \}_{i=1,\dots,L}$, we have to define, for each input, which is the best level to use as its representative

The best choice is obviously the nearest neighbor:

$$k = \arg \min_n |x - \hat{x}^n| \Rightarrow Q(x) = \hat{x}^k$$

Choosing the next neighbor is equivalent to set the threshold at the midpoint between consecutive quantization levels:

$$t^i = \frac{\hat{x}^i + \hat{x}^{i+1}}{2}, \quad i \in \{1,\dots,L-1\}$$

---

**Immagini estratte:**

![Figura estratta 1](p88_img01.jpg)
