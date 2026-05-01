# Variable-Length Coding (VLC)

If we use codewords of different lengths, we face a major hurdle: **The Parsing Problem**. How does the decoder "slice" the continuous bitstream into individual symbols if it doesn’t know where one ends and the next begins?

**Key Questions:**

1. **The Theoretical Bound**: How much can we actually gain by using VLC? *Answer*: The limit is defined by the **Source Entropy** $H(X)$.
2. **Practical Implementation**: How do we achieve this limit while ensuring unique decodability? *Answer*: Huffman coding achieves the best theoretical performance, but faces scalability problems. **Arithmetic coding** is sub-optimal, but asymptotically optimal and scales easily with the input size.
3. All these approaches assume that we know data statistics: what if we don’t? *Answer*: Universal coding (LZW)

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)
