Lossless Image Compression: JPEG-LS

Unlike general data, images possess strong spatial correlation. JPEG-LS (based on the LOCO-I algorithm) is the standard for low-complexity lossless compression.

The Predictive Framework

▶ Uses a causal neighborhood $(A, B, C)$ to predict the current pixel $X$.

▶ MED Predictor (Median Edge Detector):

$$\hat{x} = \begin{cases} \min(A, B) & \text{if } C \geq \max(A, B) \\ \max(A, B) & \text{if } C \leq \min(A, B) \\ A + B - C & \text{otherwise} \end{cases}$$

▶ Specifically designed to handle sharp edges without overshoot.

Encoding the Residual

▶ Context Modeling: The prediction error $e = x - \hat{x}$ is refined based on local gradients

▶ Golomb-Rice Coding: Used to encode the residuals

▶ Run Mode: Switches to run-length encoding in areas with identical pixels

---

**Immagini estratte:**

![Figura estratta 1](images/p156_img01.jpg)
