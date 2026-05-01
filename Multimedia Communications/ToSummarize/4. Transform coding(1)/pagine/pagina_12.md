Proof of the Huang-Schulteiss formula

$$\frac{\partial J}{\partial R_k} = -\frac{2 \ln 2}{M} c_k \sigma_k^2 2^{-2R_k} + \lambda$$

$$\frac{\partial J}{\partial \lambda} = \sum_{k=0}^{M-1} R_k - R_{\text{Tot}}$$

Setting $\nabla J(R^*, \lambda^*) = 0$, we get:

$$- \frac{2 \ln 2}{M} c_k \sigma_k^2 2^{-2R_k} + \lambda = 0$$

$$2^{-2R_k^*} = \frac{M \lambda}{2 \ln 2} \frac{1}{c_k \sigma_k^2}$$

$$-2R_k^* = \log_2 \left( \frac{M \lambda}{2 \ln 2} \right) + \log_2 \left( \frac{1}{c_k \sigma_k^2} \right)$$

$$R_k^* = \frac{1}{2} \log_2 \left( \frac{2 \ln 2}{M \lambda} \right) + \frac{1}{2} \log_2 \left( c_k \sigma_k^2 \right)$$

$$R_k^* = \lambda' + \frac{1}{2} \log_2 \left( c_k \sigma_k^2 \right)$$

where $\lambda' = \frac{1}{2} \log_2 \left( \frac{2 \ln 2}{M \lambda} \right)$. We find its value by imposing the constraint $\sum_{k=1}^{M} R_k^* = R_{\text{Tot}}$, which correspond to $\frac{\partial J}{\partial \lambda} = 0$

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
