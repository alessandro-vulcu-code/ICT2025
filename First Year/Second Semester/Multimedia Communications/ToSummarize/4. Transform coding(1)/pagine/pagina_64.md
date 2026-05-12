Limitations of the KLT

Despite its theoretical optimality, the KLT is rarely used in standard image codecs:

1. **Computational Complexity**: Requires $O(N^3)$ to find eigenvectors and $O(N^2)$ for the matrix multiplication for every block/image.
2. **Signaling Overhead**: Since it is data-dependent, the basis functions (or the matrix $T_{\text{KLT}}$) must be sent to the decoder as metadata.
3. **Model Correctness**: Assuming stationarity is often an oversimplification (e.g., images are locally stationary)

The path to DCT:

- For a Markov Process (AR(1)) with correlation $\rho \rightarrow 1$, **frequency transforms (DFT, DCT)** offer near-optimal performance with **fixed basis functions** and fast algorithms $(O(N \log N))$.

---

**Immagini estratte:**

![Figura estratta 1](p64_img01.jpg)
