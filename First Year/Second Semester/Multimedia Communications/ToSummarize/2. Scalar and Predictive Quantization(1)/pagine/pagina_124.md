Quantization: wrap-up

▶ UQ: $D = K_X \sigma_X^2 2^{-2R}$ for uniform RV or in high res
▶ Optimal SQ: similar behavior
▶ Both UQ and optimal SQ alone are catastrophic is applied directly on images or sound: the quality drops and the rate is not reduced much
▶ Predictive quantization can improve dramatically performance but:
  1. Never forget to compute the prediction on quantized data, otherwise the decoder will drift
  2. The input signal must be correlated enough
  3. We must use the best encoding strategy to achieve good performance

The best encoding strategy is entropy coding, the subject of the next lesson

---

**Immagini estratte:**

![Figura estratta 1](images/p124_img01.jpg)
