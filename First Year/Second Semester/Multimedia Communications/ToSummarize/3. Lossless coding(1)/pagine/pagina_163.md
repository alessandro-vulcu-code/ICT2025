Summary of Results (House Image)

| Method | Direct Image | Simple Pred. | Adv. Pred. |
| :--- | :--- | :--- | :--- |
| Entropy | 7.06 | 3.31 | 2.83 |
| Huffman | 7.08 | 3.38 | 2.89 |
| Exp-Golomb | 11.32 | 3.43 | 2.94 |
| ZIP | 4.00 | 3.23 | 3.14 |

Key Conclusions:

▶ Prediction is very effective for natural images: entropy goes from ~7 to ~2.8 bpp in this example. For other images the residual entropy is often around 4 bpp

▶ DEFLATE (dictionary) only is efficient for direct coding (pattern matching). For residuals, simple entropy coders (Huffman, EG) are equivalent and less complex, in particular EG offers a great complexity/performance trade-off for sparse residuals

▶ Popular formats like PNG use a combination of all these tools

---

**Immagini estratte:**

![Figura estratta 1](images/p163_img01.jpg)
