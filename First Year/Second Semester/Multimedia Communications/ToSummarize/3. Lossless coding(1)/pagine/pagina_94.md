Exp-Golomb coding: Unsigned Integers

Encoder

1. $n = 0$ is encoded as "1"
2. For $n \in \{1, 2, \ldots\}$, write $n + 1$ down in binary using the minimum number of bits: $b = \lfloor \log_2(n + 1) \rfloor + 1$.
   Place $b - 1$ zeros before the obtained bitstring for $n$

Decoder: while there are bits in the bitstream

1. If the next bit is "1", decode $n = 0$.
2. Otherwise, count the number $b$ of consecutive zeros. Read the bitstring of $b + 1$ bits, convert from binary to decimal and remove the offset $(-1)$

| $n$ | $n + 1$ on $b$ bits | Leading zeros | $c_U(n)$ |
| :--- | :--- | :--- | :--- |
| 0 | 1 | - | 1 |
| 1 | 10 | 0 | 010 |
| 2 | 11 | 0 | 011 |
| 3 | 100 | 00 | 00100 |
| 4 | 101 | 00 | 00101 |
| 5 | 110 | 00 | 00110 |
| 6 | 111 | 00 | 00111 |
| 7 | 1000 | 000 | 0001000 |
| ... | ... | ... | ... |

---

**Immagini estratte:**

![Figura estratta 1](p94_img01.jpg)
