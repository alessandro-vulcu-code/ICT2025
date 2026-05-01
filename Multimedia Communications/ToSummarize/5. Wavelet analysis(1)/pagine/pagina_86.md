Dominant pass

1. Until $\mathcal{L}$ is not empty
   ▶ Let $c$ be the first coefficient of the list
   ▶ If $c > T_k$, encode $c$ as SP (Significant Positive) and put it in $\mathcal{S}$
   ▶ Else if $c < -T_k$, encode $c$ as SN (Significant Negative) and put it in $\mathcal{S}$
   ▶ Else if no descendant is in abs value larger than $T$
      ▶ Encode $c$ as zero-tree root (ZR)
      ▶ Remove all its descendants from $\mathcal{L}$
   ▶ Else encode $c$ as Isolated Zero (IZ)

2. Remove $c$ from $\mathcal{L}$

---

**Immagini estratte:**

![Figura estratta 1](images/p86_img01.jpg)
