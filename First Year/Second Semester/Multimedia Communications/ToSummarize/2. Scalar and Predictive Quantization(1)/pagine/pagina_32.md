# Uniform quantization

Uniform quantization is characterized by:

▶ The input range: $(0, A)$ (unsigned data) or $(-\frac{A}{2}, \frac{A}{2})$ (signed data)

▶ The number of levels $L$

The input range is divided into $L$ equal-sized cells. The cell size is $\Delta = \frac{A}{L}$. Each cell is represented by its mid-point, i.e. the quantization levels are the centers of the quantization cells.

$$\forall i, \Delta^i = \Delta = A/L$$

$$t^i = t^{i-1} + \Delta \text{ (red bars)}$$

$$\hat{x}^i = \frac{t^i + t^{i-1}}{2} \text{ (green crosses)}$$

$$\Theta^i = \left( \hat{x}^i - \frac{\Delta}{2}, \hat{x}^i + \frac{\Delta}{2} \right)$$

---

**Immagini estratte:**

![Figura estratta 1](images/p32_img01.jpg)
