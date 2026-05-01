Huffman coding

Example: coding a scanned document. Typically many pixels are white and only few are black. If $X$ is a r.v. representing the color of a pixel:

$$\Pr(\{X = B\}) = p \ll 1$$
$$\Pr(\{X = W\}) = 1 - p$$
$$H(X) \ll 1$$

Huffman coding: $B \rightarrow 0$ $W \rightarrow 1$

$$\mathcal{L} = 1 \gg H(X)$$

Conclusion: the entropy is very small, but the optimal code has a coding rate much larger than the entropy: can we do better?

---

**Immagini estratte:**

![Figura estratta 1](images/p61_img01.jpg)
