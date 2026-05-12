JPEG: Entropy coding of AC coeffs

- AC coeffs are represented by run-length, category, amplitude.
- Categories and run-lengths are coded together using a table (again, a pseudo-Huffman coding)
- The table is not standardized and is specified in the file header
  - Special symbol 1: (15,0) means “at least 15 zeros before next non-zero coefficient” (Zero-Run)
  - Special symbol 2: (0,0) means “end of block” (EOB)
- The amplitude is encoded exactly as as in the DC case

---

**Immagini estratte:**

![Figura estratta 1](images/p121_img01.jpg)
