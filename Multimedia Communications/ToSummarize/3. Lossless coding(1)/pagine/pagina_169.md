3. Neural Predictive Coding: Non-linear Prediction

Evolution of DPCM

This approach enhances the classical Differential Pulse Code Modulation by replacing the linear predictor with a non-linear Neural Network.

▶ **Concept:** The prediction $\hat{x}_i = f_{NN}$ (Local Context) is no longer a fixed weighted average, but a learned function that adapts to complex edges and textures.

▶ **Loss Function:** Unlike standard NNs (trained on MSE), these are trained to minimize the Cross-Entropy of the residual distribution.

▶ **Implementation:** High throughput compared to AR models, as it can be easily integrated into existing frameworks like JPEG-LS or PNG.

---

**Immagini estratte:**

![Figura estratta 1](images/p169_img01.jpg)
