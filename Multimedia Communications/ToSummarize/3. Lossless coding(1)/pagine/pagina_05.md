Fixed-Length Coding (FLC): The Baseline

FLC Mapping Table (Two’s complement)

| Index | 4-bit Code | Index | 4-bit Code |
| :--- | :--- | :--- | :--- |
| -7 | 1001 | 1 | 0001 |
| -6 | 1010 | 2 | 0010 |
| -5 | 1011 | 3 | 0011 |
| -4 | 1100 | 4 | 0100 |
| -3 | 1101 | 5 | 0101 |
| -2 | 1110 | 6 | 0110 |
| -1 | 1111 | 7 | 0111 |
| 0 | 0000 | (spare) | 1000 |

Straightforward parsing: the decoder segments the bitstream every $L = 4$ bits

Robustness: a single bit error only affects one symbol

Rate: it is fixed, $R = \log_2 L$

Can we do better?

▶ FLC neglects that indices might be not equally probable

▶ This happens e.g. with predictive quantization

▶ Idea: Assign shorter bitstrings to probable symbols (like 0) and longer ones to rare symbols (like -7 or 7).

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)
