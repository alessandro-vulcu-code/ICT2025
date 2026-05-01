Probability Theory Refreshers

1. Uniform Random Variable
   ▶ A continuous random variable $X$ is said to be uniformly distributed on the interval $[a, b]$ if its Probability Density Function (PDF) is defined as:
   $$X \sim U(a, b) \Leftrightarrow f_X(x) = \begin{cases} \frac{1}{b-a} & \text{for } a \leq x \leq b \\ 0 & \text{otherwise} \end{cases}$$
   ▶ Its variance is $\text{Var}(X) = \frac{(b-a)^2}{12}$

2. Expected Value of a Function of an R.V. (LOTUS)
   ▶ Let $X$ be a continuous random variable with PDF $f_X(x)$. The expected value of a real-valued function $g(X)$ is given by:
   $$E[g(X)] = \int_{-\infty}^{+\infty} g(x)f_X(x)dx$$
   ▶ This theorem (Law of the Unconscious Statistician) allows us to calculate the mean of $g(X)$ without first finding its own PDF.

---

**Immagini estratte:**

![Figura estratta 1](images/p74_img01.jpg)
