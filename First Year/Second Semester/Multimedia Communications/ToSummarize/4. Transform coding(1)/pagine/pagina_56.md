KLT: Properties

Let $T_{\text{KLT}}$ be the KLT for $X$, and let $Y$ be the transformed vector $Y = T_{\text{KLT}}X$. The KLT has the following properties (without proof):

1. Orthogonality: $T_{\text{KLT}}^{-1} = T_{\text{KLT}}^T$
2. Decorrelating transform: $\mathbb{E}[Y_i Y_j] = \lambda_i \delta_{ij}$
3. Best energy concentration (sparsity):
   Let $T$ be any other orthogonal transform, and $Z = TX$, then
   $$\forall N \in \{1, \ldots, M\} \sum_{i=1}^{N} E[Y_i^2] \geq \sum_{i=1}^{N} E[Z_i^2]$$
4. Optimality for Gaussian random vector:
   If $X$ is a Gaussian RV, let $T$ be any other orthogonal transform, and $Z = TX$, then $\sigma_{GM,Y}^2 \leq \sigma_{GM,Z}^2$, meaning that the KLT has the largest coding gain among all orthogonal transforms

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/5.%20Wavelet%20analysis(1)/images/p56_img01.jpg)
