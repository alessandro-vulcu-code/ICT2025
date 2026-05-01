Predictors

▶ Linear Predictors are simple and moreover optimal for Gaussian RV

$$v(n) = -\sum_{i=1}^{P} a_i x_{n-i}$$  Filter with $P$ parameters

$$y(n) = x(n) - v(n) = \sum_{i=0}^{P} a_i x_{n-i}$$  Prediction error

▶ with $a_0 = 1$.

▶ $y$ is the result of filtering $x$ with

$$A(z) = 1 + a_1 z^{-1} + \ldots + a_P z^{-P}$$

▶ Optimal filter: minimization of $\sigma_Y^2$

---

**Immagini estratte:**

![Figura estratta 1](images/p101_img01.jpg)
