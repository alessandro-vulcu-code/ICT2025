Example: Multi/Hyperspectral Imaging

Multi/Hyperspectral images possess large correlation across spectral bands
We consider a pixel vector
$$X(m, n) = [X_1, X_2, \cdots X_M]^T$$ as the samples of the spectral signature (reflectance) at a given location
We compute the inter-band correlation $R_X$ and the transform matrix $T_{KLT}$ from its eigenvectors
The transform is applied to each pixel vector:
$$Y(m, n) = T_{KLT}X(m, n),$$ generating as many “eigen-bands” as the original number of spectral bands.
The first "Principal Components" capture common structural information (luminance/topography).
Subsequent bands contain specific spectral innovations or noise.

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/5.%20Wavelet%20analysis(1)/images/p61_img01.jpg)
