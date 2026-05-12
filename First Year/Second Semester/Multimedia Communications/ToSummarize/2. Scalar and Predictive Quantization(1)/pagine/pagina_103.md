# Predictor selection

$$\sigma_Y^2 = \mathbb{E}\{X^2(n)\} + 2 \sum_{i=1}^{P} a_i \mathbb{E}\{X(n)X(n-i)\} + \sum_{i=1}^{P} \sum_{j=1}^{P} a_i a_j \mathbb{E}\{X(n-i)X(n-j)\}$$

$$= \sigma_X^2 + 2 \underline{r}^t \underline{a} + \underline{a}^t R_X \underline{a}$$

with:

$$L = [r_X(1) \dots r_X(P)] \quad R_X = \begin{bmatrix}
r_X(0) & r_X(1) & r_X(2) & \dots & r_X(P-1) \\
r_X(1) & r_X(0) & r_X(1) & \dots & r_X(P-2) \\
r_X(2) & r_X(1) & r_X(0) & \dots & r_X(P-3) \\
\dots & \dots & \dots & \dots & \dots \\
r_X(P-2) & r_X(P-3) & r_X(P-4) & \dots & r_X(1) \\
r_X(P-1) & r_X(P-2) & r_X(P-3) & \dots & r_X(0)
\end{bmatrix}$$

$$r_X(k) = \mathbb{E}\{X(n)X(n-k)\}$$

---

**Immagini estratte:**

![Figura estratta 1](images/p103_img01.jpg)
