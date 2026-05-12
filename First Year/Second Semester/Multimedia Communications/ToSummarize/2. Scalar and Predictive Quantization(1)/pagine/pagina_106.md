Impact of Filter Order on Prediction Gain

In global DPCM, the predictor $v(n)$ uses a linear combination of $N$ causal neighbors.

▶ **Order Selection:** Increasing the order from 2 to 4 typically improves the Prediction Gain $(G_p = \sigma_X^2 / \sigma_Y^2)$, leading to a more "whitened" residual.

▶ **Screening Effect:** The benefit of including "distant" pixels diminishes rapidly. In typical image statistics, the immediate neighbors capture most of the mutual information. Distant pixels are often redundant as their correlation with the target is already "screened" by the closer neighbors.

▶ **Complexity vs. Performance:** Higher orders increase computational overhead with negligible PSNR gains for most natural textures.

---

**Immagini estratte:**

![Figura estratta 1](images/p106_img01.jpg)
