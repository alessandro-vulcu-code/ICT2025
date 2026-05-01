# Distortion of a scalar quantizer

▶ We use the squared error, which, on a single sample is:

$$d[x(n), Q[x(n)]] = |e(n)|^2 = |x(n) - Q[x(n)]|^2$$

▶ For a signal $x(\cdot)$ of duration $N$, we use the mean square error (MSE):

$$D = \frac{1}{N} \sum_{n=0}^{N-1} d[x(n), Q[x(n)]]$$

▶ For random signals$^1$, $D = \mathbb{E}\left\{|X(n) - Q(X(n))|^2\right\} = \mathbb{E}\left\{|E(n)|^2\right\}$

▶ In this case, distortion is the variance of the random process $E(n) = X(n) - Q(X(n))$, and is indicated as $\sigma_Q^2$

$^1$Notice that we use lower-case letters for deterministic signals and upper-case letter for random variables/signals, while $E$ is the expectation operator.

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)
