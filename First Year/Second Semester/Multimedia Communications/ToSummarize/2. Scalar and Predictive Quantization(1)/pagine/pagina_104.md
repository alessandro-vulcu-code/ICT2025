Predictor selection

Minimization of $Y$ variance:

$$\frac{\partial \sigma_Y^2}{\partial \underline{a}} = 2\underline{r} + 2R_X\underline{a} = 0$$

Thus:

$$\underline{a}^{\text{opt}} = -R_X^{-1}\underline{r}$$

$$\sigma_Y^2 = \sigma_X^2 + \underline{r}^t\underline{a}^{\text{opt}}$$

Autocorrelation $r_X$ can be estimated as

$$\hat{r}_X(k) = \frac{1}{N} \sum_{n=0}^{N-1-k} X(n)X(n+k)$$

---

**Immagini estratte:**

![Figura estratta 1](images/p104_img01.jpg)
