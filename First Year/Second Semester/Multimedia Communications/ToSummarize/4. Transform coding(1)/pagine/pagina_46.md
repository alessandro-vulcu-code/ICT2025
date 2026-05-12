Greedy algorithm

The same allocation as the modified H.S. can be obtained with a greedy algorithm, which can be faster if $R_{\text{Tot}}$ is small.

The algorithms is as follows

1. Initialization
   - $R_k = 0 \quad \forall k \in \{0, 1, \ldots M - 1\}$.
   - $D_k = \sigma_k^2 \forall k \in \{0, 1, \ldots M - 1\}$.

2. While $\sum_k R_k \leq R_{\text{Tot}}$
   - $\ell = \arg \max_k D_k$
   - $R_\ell \leftarrow R_\ell + 1$
   - $D_\ell \leftarrow D_\ell / 4$

Let us see this algorithm at work

---

**Immagini estratte:**

![Figura estratta 1](p46_img01.jpg)
