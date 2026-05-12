Lloyd-Max algorithm: stop condition

▶ After the $k$-iteration of NN and the centroid rules, we can compute the new distortion value $\sigma_{Q,(k)}^2$

▶ It can be compared with the previous distortion $\sigma_{Q,(k-1)}^2$: the optimization steps assure that the new distortion can only be less than or equal to the old one

▶ We compute the relative distortion reduction: if it is smaller than a threshold, we stop the algorithm:

$$\frac{\sigma_{Q,(k-1)}^2 - \sigma_{Q,(k)}^2}{\sigma_{Q,(k-1)}^2} < \varepsilon$$

▶ Another stop condition is upon a given number of iterations:

$$k = K$$

---

**Immagini estratte:**

![Figura estratta 1](p90_img01.jpg)
