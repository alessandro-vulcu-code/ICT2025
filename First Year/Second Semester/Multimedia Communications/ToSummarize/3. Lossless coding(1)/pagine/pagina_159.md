Lossless Compression: Baseline Analysis

The experiment evaluates different lossless techniques on a 256-level gray-scale image (house. pgm, 8 bpp).

Pixel-level Statistics:

▶ Entropy ($H$): Estimated via relative frequency of gray levels. For the "house" image, $H = 7.056$ bpp.

▶ Huffman Coding: Results in an average length of 7.081 bpp.

▶ ZIP (Deflate, i.e. LZ77): Achieves 4.003 bpp. It outperforms pixel-wise Huffman by exploiting string repetitions.

▶ Unsigned Exp-Golomb: Results in 11.320 bpp (inefficient for raw luminance).

Observation

Huffman coding at the pixel level is close to the entropy but offers poor compression because it ignores spatial dependencies. ZIP performs better as it identifies block redundancies.

---

**Immagini estratte:**

![Figura estratta 1](images/p159_img01.jpg)
