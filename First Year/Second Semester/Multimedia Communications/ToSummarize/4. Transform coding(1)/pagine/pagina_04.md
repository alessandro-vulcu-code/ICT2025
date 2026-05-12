Recall: SQ, PQ, EC

▶ In **scalar quantization** each sample is quantized independently from the others and the resulting distortion may be large:

$$D = \sigma_X^2 2^{-2R}$$

UQ for uniform RV

$$D = K_X \sigma_X^2 2^{-2R}$$

HR UQ for generic RV

$$D = c_X \sigma_X^2 2^{-2R}$$

OQ for generic RV

▶ If the $L$ levels are equiprobable, the entropy of the quantization indexes is $\log_2 L$ and an arithmetic encoder has a rate $R \rightarrow H = \log_2 L$ for a sufficiently long symbol sequence

▶ To improve the performance one must exploit sample dependence:

1. **Predictive quantization**: reduces the signal variance
2. **Block coding**: exploits signal sparsity
3. **Transform coding**: makes the signal sparse

▶ We have seen that PQ reduces the signal variance. Today we focus on block coding and transform coding.

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)
