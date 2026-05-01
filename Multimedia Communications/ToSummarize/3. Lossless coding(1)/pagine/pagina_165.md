Neural Lossless Coding: The Density Estimation Perspective

Neural Network (NN) estimates the true, high-order distribution $P(X^n)$ of the source

The Information-Theoretic Limit

In Neural Lossless Coding (NLC), we minimize the Cross-Entropy between the true distribution $P$ and the neural model (estimated distribution) $Q$:

$$H(P, Q) = H(P) + D_{KL}(P \parallel Q)$$

- $H(P)$ is the source entropy (physical limit).
- $D_{KL}$ is the penalty for model inaccuracy (redundancy).
- The NN does not "compress" directly, but acts as a probability distribution estimator providing $Q$ to an arithmetic coder.

---

**Immagini estratte:**

![Figura estratta 1](images/p165_img01.jpg)
