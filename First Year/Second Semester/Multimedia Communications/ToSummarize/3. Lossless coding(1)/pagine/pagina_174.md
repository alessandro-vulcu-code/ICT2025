Counting the Bitrate Overhead

The total cost to transmit the image is:

$$R_{\text{total}} = R_{\text{residuals}} + \frac{L_{\text{model}}}{N} \quad [\text{bits/pixel}]$$

▶ $L_{\text{model}} = (\text{Total Parameters}) \times (\text{Precision})$.
▶ **Example:** A small [10, 5] MLP with 3 inputs has $\approx 100$ weights. Using 32-bit floats, $L_{\text{model}} = 3200$ bits.
▶ Total rate: $R = 2.704 + \frac{3200}{512^2} \approx 2.716$
▶ **Trade-off:** For small images $(N)$, the model cost can outweigh the compression gain. NLC is more efficient for large datasets (weight shared among all the images) or high-resolution images.

---

**Immagini estratte:**

![Figura estratta 1](images/p174_img01.jpg)
