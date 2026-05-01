Optimal quantization in high resolution

▶ The optimal quantizer is the one that, for a given PDF $p_X$ of the input samples, provides the least distortion $D = \mathbb{E} \left[ (X - Q(X))^2 \right]$ for a given rate $R$
▶ It is possible to find the rate-distortion curve for the optimal quantizer in the high-resolution hypothesis:
▶ $L \to \infty$
▶ $\max_i \Delta_i \to 0$
▶ $\forall i, \forall u \in \Theta^i, p_X(u) \approx P_i$
▶ Then it can be shown that the optimal quantizer has the following RD curve:

$$\sigma_Q^2 = c_X \sigma_X^2 2^{-2R}$$

with $c_X = \frac{1}{12} \left[ \int_R p_U^{1/3}(t) dt \right]^3$ and $U = \frac{X}{\sigma_X}$

---

**Immagini estratte:**

![Figura estratta 1](images/p83_img01.jpg)
