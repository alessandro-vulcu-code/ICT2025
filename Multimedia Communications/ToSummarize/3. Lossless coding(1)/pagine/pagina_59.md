# Huffman coding

| Symbol | Probability | Codeword |
| :--- | :--- | :--- |
| A | 0.4 | 0 |
| B | 0.2 | 100 |
| C | 0.15 | 101 |
| D | 0.15 | 110 |
| E | 0.05 | 1110 |
| F | 0.05 | 1111 |

Find $\mathcal{L}$ and $H$

$$\mathcal{L} = 0.4 \cdot 1 + 0.2 \cdot 3 + 0.15 \cdot 3 + 0.15 \cdot 3 + 0.05 \cdot 4 + 0.05 \cdot 4 = 2.3 \text{ bits/Symbol}$$

$$H = 0.4 \cdot \log_2 \frac{1}{0.4} + 0.2 \cdot \log_2 \frac{1}{0.2} + 2 \cdot 0.15 \cdot \log_2 \frac{1}{0.15} + 2 \cdot 0.05 \cdot \log_2 \frac{1}{0.05}$$

$\simeq 2.2464 \text{ bits/Symbol}$

Go to wooclap.com with the code GYKKIN

---

**Immagini estratte:**

![Figura estratta 1](images/p59_img01.jpg)
