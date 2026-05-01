Arithmetic coding

▶ Arithmetic coding allows to perform block coding or context-based coding with linear complexity
▶ Instead of producing the entire dictionary and then selecting the codeword, only the codeword associated to the block of $n$ input symbols is built
▶ The arithmetic is suboptimal, but asymptotically optimal

$$\mathcal{L} \leq H(X^K) + 2$$
$$\mathcal{L}_S = \mathcal{L}/K$$
$$\lim_{K \to \infty} \mathcal{L}_S = \lim_{K \to \infty} \frac{H^K}{K} = \mathcal{H}(X)$$

▶ Low-complexity encoding and decoding: two sums and two multiplications per input symbols (arithmetic operations)

---

**Immagini estratte:**

![Figura estratta 1](images/p77_img01.jpg)
