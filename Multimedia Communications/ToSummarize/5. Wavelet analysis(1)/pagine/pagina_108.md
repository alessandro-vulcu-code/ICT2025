EZW Encoding: Bitplane 3 ($T = 4$)

| 26 | 6 | -13 | 10 |
| :--- | :--- | :--- | :--- |
| -7 | 3 | 6 | 4 |
| 4 | -3 | 3 | -3 |
| 2 | -2 | -2 | 0 |

Refinement Pass

Write the bit in position $\log_2 T = 2$ for all the significant coeff’s abs. values:
$$26_{10} = 11010_2 \rightarrow 1 \quad 13_{10} = 11010_2 \rightarrow 0 \quad 10_{10} = 1010_2 \rightarrow 1 \quad 6_{10} = 110_2 \rightarrow 1 \quad 7_{10} = 111_2 \rightarrow 1$$
$$6_{10} = 110_2 \rightarrow 1 \quad 4_{10} = 100_2 \rightarrow 0 \quad 4_{10} = 100_2 \rightarrow 0$$

Symbol stream (SP, SN, ZR, IZ are arithmetically encoded):

| SP | ZR | ZR | ZR | 1 | IZ | ZR | ZR | SN | SP | ZR | ZR | 0 | 1 | 0 | SP | SN |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ZR | SP | SP | SP | ZR | ZR | ZR | ZR | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | ... | |

---

**Immagini estratte:**

![Figura estratta 1](images/p108_img01.jpg)
