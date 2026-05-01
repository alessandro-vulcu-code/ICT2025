Block Coding vs. Context-Based Coding

Comparing the compression efficiency for the "T-shape" image:

| Method | Theoretical Limit (bpp) | Practical Rate (bpp) |
| :--- | :--- | :--- |
| Symbol-wise ($K = 1$) | $H(X) = 0.586$ | 1.000 (Huffman) |
| Block Coding ($K = 2$) | $\frac{H(X^2)}{2} = 0.511$ | 0.650 (Huffman) |
| Block Coding ($K = 4$) | $\frac{H(X^4)}{4} = 0.383$ | 0.433 (Huffman) |
| Context-Based (1D) | $H(X_n|X_{n-1}) = 0.406$ | $\approx 0.406$ (Arithmetic) |

With a simple 1D context (the previous pixel) we achieve almost the same performance of a more complicated $2 \times 2$ block-based coding. More complex context can better capture long-term dependencies than using large block sizes.

---

**Immagini estratte:**

![Figura estratta 1](images/p88_img01.jpg)
