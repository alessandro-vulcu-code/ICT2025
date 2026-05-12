JPEG Standard: Quality factor

▶ It is a non-normative tool that eases the selection of a quantization matrix
▶ The quality factor $Q$ is between 1 and 100
▶ It defines a scaling factor $S_F$ for the quantization matrix

$$S_F = \begin{cases} \frac{5000}{Q} & 1 \leq Q \leq 50 \\ 200 - 2Q & 50 < Q \leq 99 \\ 1 & Q = 100 \end{cases}$$

$$q \leftarrow \frac{S_F}{100} q^*$$

---

**Immagini estratte:**

![Figura estratta 1](p111_img01.jpg)
