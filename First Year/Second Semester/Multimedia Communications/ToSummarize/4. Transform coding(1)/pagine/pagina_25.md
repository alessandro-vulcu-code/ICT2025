Orthogonal Transforms

An orthogonal transform (OT) means that the matrix $T$ is orthogonal and thus $T^{-1} = T^T$, $Y = TX$ and $X = T^TY$.

1. For orthogonal transforms, the inversion is immediate
2. OT are isometries, i.e. they keep the $\mathcal{L}^2$ norm: for any $X$,

$$\| TX \|^2 = (TX)^T (TX) = \left( X^T T^T \right) (TX) = X^T (T^T T) X = X^T X = \| X \|^2$$

The isometry property is very important because it insures that the distortion on $Y$ is the same as the distortion on $X$:

$$\mathcal{D}_Y = \frac{1}{M} \text{E} \left[ \| Y - \hat{Y} \|^2 \right] = \frac{1}{M} \text{E} \left[ \| T \left( X - \hat{X} \right) \|^2 \right] = \frac{1}{M} \text{E} \left[ \| \left( X - \hat{X} \right) \|^2 \right] = \mathcal{D}_X$$

It is very important to keep the same distortion in the transform and in the original domain:

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)
