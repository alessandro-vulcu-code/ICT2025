Huffman coding

How to improve performance?

▶ Let us refer to the block of $K$ symbols $X^K = (X_1X_2 \ldots X_K)$:

$$H[(X_1X_2 \ldots X_K)] \leq \sum_{i=1}^{K} H(X_i)$$

with equality if and only if components of $X^K$ are independent each from the other

▶ Idea of block coding: Encode the block $X^K$ rather than each individual component

1. If the symbols are not independent, $H(X^K)/K < H(X_i)$
2. $\mathcal{L} < H(X^K) + 1 \Leftrightarrow \mathcal{L}_S < H(X^K)/K + 1/K$

If the symbols are identically distributed (but not necessarily independent), $\mathcal{L}_S < H(X^K)/K + 1/K \leq H(X_i) + 1/K$

---

**Immagini estratte:**

![Figura estratta 1](p66_img01.jpg)
