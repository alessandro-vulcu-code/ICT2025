UQ: wrap-up

▶ UQ is intuitive: just split the input range into $L$ intervals, and represent each interval with its middle.

▶ Implementation is easy:

$$Q(x) = \Delta \cdot \text{round}\left(\frac{x}{\Delta}\right) \quad \text{mid-tread}$$

$$Q(x) = \Delta \cdot \text{floor}\left(\frac{x}{\Delta}\right) + \frac{\Delta}{2} \quad \text{mid-rise}$$

▶ For a given range $A$ and a given number of levels $L$, UQ has the smallest maximum error (optimal minimax quantizer)

▶ The maximum error is half the size of the maximum quantization interval: any modification of the UQ increases the maximum quantization interval and thus the maximum error

▶ Last, but not least, UQ allows for an analytical formula of the RD (rate-distortion) curve. But before that...

---

**Immagini estratte:**

![Figura estratta 1](images/p38_img01.jpg)
