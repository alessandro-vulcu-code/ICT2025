Proof of Sufficiency

Goal: Given $\{\ell_i\}$ such that $\sum 2^{-l_i} \leq 1$, construct a prefix code.

Greedy Construction Algorithm:
1. Sort lengths: $\ell_1 \leq \ell_2 \leq \cdots \leq \ell_N$.
2. At each step $k$, pick an available node at depth $\ell_k$.
3. Mark all its descendants as "forbidden".

Existence Argument: At step $k$, the "consumed capacity" of the tree is $\sum_{i=1}^{k-1} 2^{-\ell_i}$. Since the total sum is $\leq 1$, and $\ell_k \geq \ell_{k-1}$, there must be at least one branch available at depth $\ell_k$ to place the next codeword.

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)
