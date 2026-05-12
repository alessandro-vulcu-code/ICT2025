Transform coding: Toy Example

Couple of highly correlated RV's: once we know the value of $X_1$, $X_2$ is constrained into a small interval. Nevertheless, each variable has the same marginal distribution. This could be a relatively good model for a couple of neighboring pixels in an image

$$f_{X_1, X_2}(x_1, x_2) = \begin{cases} \frac{1}{\Delta_1 \Delta_2} & \text{if } (x_1, x_2) \in S \\ 0 & \text{if } (x_1, x_2) \notin S \end{cases}$$

$\Delta_1 \gg \Delta_2$

$X_1 \sim X_2 \sim \mathcal{U} \left[ -\frac{\Delta_1}{2\sqrt{2}}, \frac{\Delta_1}{2\sqrt{2}} \right]$$

---

**Immagini estratte:**

![Figura estratta 1](images/p32_img01.jpg)
