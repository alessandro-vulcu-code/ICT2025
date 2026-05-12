Comparison of Lossless Coding Techniques

| Method | Efficiency | Complexity | Latency | Best use case |
| :--- | :--- | :--- | :--- | :--- |
| Neural (SOTA) | Highest | Ultra High | High | SOTA Image/Video |
| Arithmetic | High (to H) | High (CPU) | Med | Bi-level images, CABAC |
| Dictionary | Universal | Moderate | Low/Med | Repeating patterns |
| Huffman | Good to high (1 < L < H + 1) | Low/Med | Very Low | JPEG, general purpose |
| Exp-Golomb | Good (approx.) | Very Low | Negligible | Metadata, Residuals |

Statistical Modeling
- Huffman/Arithmetic: Use probabilities $P(X)$.
- Neural: Estimates $P(X)$ via non-linear density estimation.

The 1-bit Penalty
- Huffman: Fails if $H(X) < 1$ bit/symbol
- Arithmetic: Efficient below 1 bit/symbol

---

**Immagini estratte:**

![Figura estratta 1](images/p178_img01.jpg)
