Proof of Sufficiency

Goal: Given $\{\ell_i\}$ such that $\sum 2^{-l_i} \leq 1$, construct a prefix code.

Greedy Construction Algorithm:

1. Sort lengths: $\ell_1 \leq \ell_2 \leq \cdots \leq \ell_N$.
2. At each step $k$, pick an available node at depth $\ell_k$.
3. Mark all its descendants as "forbidden".

---

**Immagini estratte:**

![Figura estratta 1](images/p24_img01.jpg)
