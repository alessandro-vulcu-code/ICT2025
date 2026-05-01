Prediction gain

Prediction Error = Signal Error :

$$q(n) = y(n) - \hat{y}(n) = x(n) - v(n) - \hat{x}(n) + v(n) = \bar{q}(n)$$

Thus the goal of predictive quantization (PQ) is to minimize the distortion of $y$.

The coding gain is:

$$\text{SNR}_P = 10 \log_{10} \frac{\sigma_X^2}{D} = 10 \log_{10} \frac{\sigma_X^2}{\sigma_Y^2} + 10 \log_{10} \frac{\sigma_Y^2}{D} = G_P + G_Q$$

Prediction is effective if and only if the prediction error has a smaller variance than the original signal

---

**Immagini estratte:**

![Figura estratta 1](images/p98_img01.jpg)
