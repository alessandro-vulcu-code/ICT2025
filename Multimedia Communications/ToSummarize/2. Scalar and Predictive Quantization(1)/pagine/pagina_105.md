Predictive quantization: example

For the "peppers" image (grayscale), we compute the prediction error using a second order linear predictor:

$$\hat{f}_{n,m} = af_{n-1,m} + bf_{n,m-1}$$

The predictor of $f_{n,m}$ is a weighted average of the top and the left neighbors.

| a | b | $\sigma^2_x$ |
| :--- | :--- | :--- |
| 0 | 0 | 2902.7 |
| 1/2 | 1/2 | 78.7 |
| 0.449 | 0.546 | 78.4 |

The first row correspond to no prediction: thus $\sigma^2_x = 2902.7$. The second row show the distortion of the simplest predictor: the average of the two neighbors. The distortion is reduced by a factor greater than 37. Using the optimal predictor, computed with the formulas shown in the previous slide, only slightly improves the performance.

---

**Immagini estratte:**

![Figura estratta 1](images/p105_img02.jpg)

![Figura estratta 2](images/p105_img01.jpg)
