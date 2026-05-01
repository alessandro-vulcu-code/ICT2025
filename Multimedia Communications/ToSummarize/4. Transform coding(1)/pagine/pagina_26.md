Orthogonal Transforms and Coding Gain

▶ Let $X$ be a random vector of $M$ components (sound, image...)

▶ Hypothesis: $X$ components are identically distributed (i.d.) Gaussian RVs: $\forall k, X_k \sim \mathcal{N}(0, \sigma_X^2)$
▶ Note that $X$ components are not assumed to be independent

▶ In this case resource allocation is trivial since all the components have the same variance and shape factor. For historical reasons, the distortion in this case (non-transformed, i.d. RVs) is referred to as $D_{\text{PCM}}$, so we get

$$D_{\text{PCM}} = c_N \sigma_X^2 2^{-2\hat{R}}$$

▶ Let us now consider a generic OT, such that $Y = \mathcal{T}X$

▶ Question: how much can we reduce the quantization distortion by applying the transform coding paradigm?

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)
