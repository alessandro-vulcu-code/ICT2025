Complexity and 2D Basis Patterns

Separability transforms an $O(N^4)$ problem into a sequence of $O(N^3)$ operations, or $O(N^2 \log N)$ when using the Fast Fourier Transform (FFT).

The 2D Basis Functions The transform decomposes the image into a weighted sum of $N^2$ orthogonal basis patterns:

$$B_{k,\ell}(n,m) = \frac{1}{N} e^{j \frac{2\pi}{N}(kn+\ell m)}$$

- Each coefficient $Y[k,l]$ represents the "strength" of a specific horizontal and vertical frequency combination.
- Compression Insight: For natural images, most of the energy is concentrated in coefficients where $k$ and $\ell$ are small (low frequencies).

DCT will improve upon this by eliminating boundary discontinuities.

---

**Immagini estratte:**

![Figura estratta 1](images/p70_img01.jpg)
