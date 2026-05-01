Block coding

Let us consider a block of $M$ random variables $X = [X_1, X_2, \ldots X_M]^T$ (column vector)
The RV do not need to be independent neither i.d.
Let $\sigma_k^2 = \text{Var}(X_k)$ and let $c_k$ be the shape factor of $X_k$
The distortion of $X_k$ with an optimal quantizer is:

$$D_k = c_k \sigma_k^2 2^{-2R_k}$$

where $R_k$ is the bit rate used for $X_k$
Let us consider what happens if the $M$ RV are quantized with a rate that is jointly decided such that the global distortion is minimized
The global distortion is

$$\mathcal{D} = \frac{1}{M} \text{E} \left[ \|X - Q(X)\|^2 \right] = \frac{1}{M} \text{E} \left[ (X - Q(X))^T (X - Q(X)) \right] = \frac{1}{M} \text{E} \left[ \sum_{k=1}^{M} (X_k - Q(X_k))^2 \right]$$

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)
