Error robustness in compressed data

- Transmission and storage operations introduce errors in files with a certain probability
- A wrong bit in an uncompressed image only affects the color of one pixel
- Compressed streams are much more vulnerable:
  - Predictive and differential coding introduce data dependency, implying error propagation
  - Variable lenght coding implies possibly decoding drift
  - Errors on headers and metadata are particularly dangerous

---

**Immagini estratte:**

![Figura estratta 1](images/p138_img01.jpg)
