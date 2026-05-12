Exp-Golomb coding: Signed Integers

Encoder

1. Map $n \in \mathbb{Z}$ into $m(n) \in \mathbb{N}$:
   ▶ If $n > 0$, then $m(n) = 2n - 1$
   ▶ If $n \leq 0$, then $m(n) = -2n$

2. Encode $m(n)$ with the unsigned Exp-Golomb method

Decoder

1. Decode a positive number $m$ with the unsigned Exp-Golomb method

2. Map it to the integers:
   ▶ If $m$ is odd, $n = \frac{m+1}{2}$
   ▶ If $m$ is even, $n = -\frac{m}{2}$

Go to wooclap.com with the code GYKKIN

---

**Immagini estratte:**

![Figura estratta 1](p95_img01.jpg)
