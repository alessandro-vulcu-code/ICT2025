DFT vs DCT

In black, we show the vector $X$. We compute $Y_{\text{DCT}} = \mathcal{T}_{\text{DCT}} X$ and $Y_{\text{DFT}} = \mathcal{T}_{\text{DFT}} X$. We set:

$$\hat{Y}_{\text{DCT}}(k) = \begin{cases} Y_{\text{DCT}}(k) & \text{if } k < 3 \\ 0 & \text{otherwise} \end{cases}$$

$$\hat{X}_{\text{DCT}} = \mathcal{T}_{\text{DCT}} \hat{Y}_{\text{DCT}}$$

$$\hat{Y}_{\text{DFT}}(k) = \begin{cases} Y_{\text{DFT}}(k) & \text{if } k < 3 \\ 0 & \text{otherwise} \end{cases}$$

$$\hat{X}_{\text{DFT}} = \mathcal{T}_{\text{DFT}} \hat{Y}_{\text{DFT}}$$

The reconstructed signal $\hat{X}_{\text{DFT}}$ struggles with the border effect and has a less effective energy compaction.

---

**Immagini estratte:**

![Figura estratta 1](images/p86_img01.jpg)
