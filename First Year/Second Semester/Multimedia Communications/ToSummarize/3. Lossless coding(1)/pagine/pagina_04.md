# From Samples to Bits: The Encoding Process

1. **Spatial Prediction**: Leverages local correlation to reduce variance. $y(n) = x(n) - \hat{x}(n)$
2. **Quantization**: Maps the high-precision residuals into a finite set of discrete indices $i(n)$.
The Central Question: How do we map the resulting indices into an efficient bitstream?
The Answer: **Lossless Coding**
The chosen code must satisfy two fundamental requirements: **Uniquely Decodable**: one-to-one mapping from the bitstream back to the symbol **sequence**
**Compact**: smallest possible average codeword length

4/102 18.03.26 Lossless coding principles Marco Cagnazzo

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img04.jpg)

![Figura estratta 2](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)

![Figura estratta 3](p04_img03.jpg)

![Figura estratta 4](p04_img02.jpg)
