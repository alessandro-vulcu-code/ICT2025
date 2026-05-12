The Karhunen-Loève Transform (KLT)

Let $X$ be a **zero-mean** random vector of size $M$ with correlation matrix: $R_X = E[XX^T]$. We assume that $R_X$ has $M$ orthogonal eigenvectors $u_1, \ldots, u_M$, which is true for all the most relevant statistical models for audio/visual signals (e.g., Markov chains).

The KLT is defined as the orthonormal matrix $T_{KLT}$ whose **rows** are the eigenvectors:

$$T_{KLT} = \begin{bmatrix} u_1 & u_2 & \ldots & u_M \end{bmatrix}^T$$

The transform is defined as $Y = T_{KLT}X$.

**Fundamental Property**

The KLT is a **data-dependent** transform. Its basis functions are not fixed but are tailored to the statistical properties of the specific source $X$. We need to know or estimate $R_X$ to apply the KLT

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/5.%20Wavelet%20analysis(1)/images/p55_img01.jpg)
