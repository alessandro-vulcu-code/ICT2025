Uniform quantization for signed data

For signed data (range in $(-A/2, A/2)$) one typically wants zero to be a quantization level (mid-tread quantizer): in such a way, small fluctuations are quantized to zero. Therefore, we always use an odd number of levels for UQ of signed data. In this case, uniform quantization (UQ) amounts to rounding:

$$i = \text{round}\left(\frac{x}{\Delta}\right) \quad \text{encoder}$$

$$\hat{x}^i = \Delta \cdot i \quad \text{decoder}$$

$$Q(x) = \Delta \cdot \text{round}\left(\frac{x}{\Delta}\right)$$

In other words, $Q(x)$ is the closest multiple of $\Delta$. This quantizer is also referred to as mid-tread quantizer.

---

**Immagini estratte:**

![Figura estratta 1](images/p34_img01.jpg)
