JPEG: Entropy coding of DC coeffs

Here we show the tables for DC categories and for encoding an amplitude given the category:

| Category | Code |
| :--- | :--- |
| 0 | 00 |
| 1 | 010 |
| 2 | 011 |
| 3 | 100 |
| 4 | 101 |
| 5 | 110 |
| 6 | 1110 |
| 7 | 11110 |
| 8 | 111110 |
| 9 | 1111110 |
| 10 | 11111110 |
| 11 | 111111110 |

| Category | Amplitude | Code |
| :--- | :--- | :--- |
| 0 | 0 | - |
| 1 | +1 | 1 |
| 2 | +2 | 10 |
| 3 | +3 | 11 |
| 4 | -2 | 01 |
| 5 | -3 | 00 |
| 6 | +4 | 100 |
| 7 | +5 | 101 |
| ... | ... | ... |
| 11 | 1024 | 1 000 0000 000 |
| ... | ... | ... |
| -2047 | 0 000 0000 000 |

For example, if the prediction error is $DC_p = DC_n - DC_{n-1} = -5$, we first find the category $k = \lceil \log_2(|DC_p| + 1) \rceil = 3$.

Now we write the code of category: 100; and 5 in binary: 101, but we complement each bit because the value is negative: finally we encode: 100010.

If we were to encode +5, we would have 100101.

---

**Immagini estratte:**

![Figura estratta 1](p120_img01.jpg)
