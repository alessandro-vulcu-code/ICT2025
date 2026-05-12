Local Adaptation: The Block-wise Approach

Images are non-stationary signals; a single global filter is suboptimal for varying textures (e.g., edges vs. smooth areas). The Strategy: Divide the image into $M \times M$ blocks and compute the locally optimal filter for each.

The Side Information Trade-off Total Rate ($R_{total}$) is now increased by $\frac{N \cdot B}{M^2}$ Where $N$ is the filter order and $B$ is the bits per coefficient (e.g., 16).

▶ Small Blocks: Excellent tracking of local statistics, but massive overhead from filter coefficients.

▶ Large Blocks: Minimal overhead, but the predictor fails to adapt to local features.

---

**Immagini estratte:**

![Figura estratta 1](images/p109_img01.jpg)
