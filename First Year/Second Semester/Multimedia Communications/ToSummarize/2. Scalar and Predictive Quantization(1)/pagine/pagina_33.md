Uniform Quantization for unsigned data

For unsigned data (range (0, A)) the thresholds are $(0, \Delta, 2\Delta, \ldots, L\Delta)$, i.e., $t^i = (i - 1)\Delta$.

We can thus define the behavior of the encoder (from $x$ to the quantization index $i$), of the decoder (from $i$ to the quantization level $\hat{x}^i$) and of the full quantization chain:

$$i = \left\lceil \frac{x}{\Delta} \right\rceil \quad \text{encoder}$$

$$\hat{x}^i = i \cdot \Delta - \frac{\Delta}{2} \quad \text{decoder}$$

$$Q(x) = \Delta \cdot \left\lceil \frac{x}{\Delta} \right\rceil - \frac{\Delta}{2}$$

UQ for unsigned data, L=8

---

**Immagini estratte:**

![Figura estratta 1](images/p33_img01.jpg)
