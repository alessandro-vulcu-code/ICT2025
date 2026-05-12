Context-Based vs. Block Coding

Experimental Data (T-shape image)

| Method | Limit (bpp) | Practical (bpp) |
| :--- | :--- | :--- |
| Symbol-wise ($K = 1$) | 0.586 | 1.000 (Huffman) |
| Block Coding ($K = 4$) | 0.383 | 0.433 (Huffman) |
| Context-Based | 0.406 | $\approx$ 0.406 (Arithmetic) |

▶ Block Coding: Complexity grows exponentially ($M^K$)
▶ Context-Based: Reaches the entropy rate $\mathcal{H}$ by capturing the "significant past" without massive tables.

---

**Immagini estratte:**

![Figura estratta 1](images/p179_img01.jpg)
