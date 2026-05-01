Quantization as coding / decoding

- The quantization process can be seen as the cascade of “encoding” and “decoding”
- The encoder produces the index of the quantization region, $i(n) \in \mathbb{Z}$
- The number $i(n)$ is represented with a suitable string of bits, e.g. by using lossless coding
- The decoder associates to $i(n)$ to the corresponding level (or code-word) $\hat{x}^i(n)$
- In a compression system, often with the term quantization we just refer to the operation $x \rightarrow i$, while the evaluation of the quantization level, $i \rightarrow \hat{x}^i$, is referred to as Inverse Quantization
- The first is performed at the encoder, the second at the decoder

---

**Immagini estratte:**

![Figura estratta 1](images/p22_img01.jpg)
