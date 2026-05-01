# Z-domain relationships

filter $ \tilde{C}(z) = \sum_{n=-\infty}^{\infty} \tilde{c}_n z^{-n} = H_0(z) X(z) $
decimation $ C(z) = \frac{1}{2} \left[ \tilde{C}\left(z^{1/2}\right) + \tilde{C}\left(-z^{1/2}\right) \right] $
interpolation $ \hat{C}(z) = C(z^2) $
output $ \tilde{X}(z) = F_0(z) C(z^2) + F_1(z) D(z^2) $

$$\tilde{X}(z) = \frac{1}{2} \left[ F_0(z) H_0(z) + F_1(z) H_1(z) \right] X(z)$$
$$+ \frac{1}{2} \left[ F_0(z) H_0(-z) + F_1(z) H_1(-z) \right] X(-z)$$

---

**Immagini estratte:**

![Figura estratta 1](images/p28_img01.jpg)
