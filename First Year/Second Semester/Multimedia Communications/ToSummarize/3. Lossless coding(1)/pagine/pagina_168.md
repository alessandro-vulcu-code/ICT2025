2. Latent Variable Models: Mapping to Manifolds

Theoretical Framework

Based on Variational Inference. The image $x$ is mapped to a lower-dimensional latent representation $z$ (similar to a non-linear PCA).

▶ Two-stage Coding:
1. Encode the latent features $z$ (the "summary").
2. Encode the data $x$ given $z$ (the "residuals" or likelihood).

▶ The Bits-back Principle: In a sequence of images, the bits used to specify $z$ can be "recovered" from the randomness of the previous message.

▶ Limit: The compression performance is bounded by the ELBO (Evidence Lower Bound), which is the variational approximation of the true log-likelihood.

---

**Immagini estratte:**

![Figura estratta 1](images/p168_img01.jpg)
