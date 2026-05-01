# Main Dictionary-Based Algorithms

Dictionary coding methods are generally classified into two generations: the sliding window approach (LZ77 family) and the explicit dictionary approach (LZ8 family).

| Algorithm | Year | Technical Characteristic |
| :--- | :--- | :--- |
| LZ77 | 1977 | Uses a sliding window to reference previous strings via (offset, length) pairs. |
| LZ78 | 1978 | Builds an explicit dictionary of strings encountered in the data stream. |
| LZSS | 1982 | Enhances LZ77 by using a flag bit to distinguish between literals and pointers. |
| LZW | 1984 | A LZ78 refinement that eliminates character transmission by pre-filling the dictionary. |
| LZMA | 1998 | Combines large dictionary sizes with range coding (arithmetic) for high compression. |

---

**Immagini estratte:**

![Figura estratta 1](images/p98_img01.jpg)
