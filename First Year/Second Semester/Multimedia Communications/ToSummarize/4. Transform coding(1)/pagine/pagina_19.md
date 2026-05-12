# Signal sparsification

We look for an operator $T$ such that:

▶ Is reversible: $Y = T(X) \Leftrightarrow X = T^{-1}(Y)$
▶ Input data is as a vector in $\mathbb{R}^M$
  ▶ Example: $M$ samples of recorded voice
  ▶ Example: $M = M_1 \times M_2$ pixels from a rectangular block of a gray-level image
▶ Input data is **not sparse**
  ▶ This means that any sample is potentially meaningful
▶ Output data $Y = T(X)$ is **sparse** and the quantization error on $Y$ is the same as on $X$
  ▶ A few non-negligible samples and many negligible (near zero) samples
  ▶ If the quantization error is not the same, we risk that after reversing the operator, the error increases

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p19_img01.jpg)
