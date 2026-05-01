JPEG: Entropy coding of DC coeffs

- DC Coeff’s difference are represented by the category/amplitude couple
- There are 12 categories, named 0, . . ., 11, coded with a pseudo-Huffman code
- The category $k$ of the DC prediction error $DC_P$ is defined as: $\lceil \log_2(|DC_P| + 1) \rceil$
- In other words, category $k$ contains $2^k$ values (or amplitudes): $\{ \pm 2^{k-1}, \ldots, \pm 2^k - 1 \}$; each amplitude is coded on $k$ bits, using 2’s complements for negative values
- The DC prediction error is then encoded by writing first the bits of the category and then those of the value (or amplitude)

---

**Immagini estratte:**

![Figura estratta 1](images/p119_img01.jpg)
