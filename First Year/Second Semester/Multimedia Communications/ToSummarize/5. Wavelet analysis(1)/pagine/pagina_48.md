Recap of the last lesson

▶ “Trends+anomalies” model for visual signals
▶ A filterbank (LPF, HPF, subsampling) can separate approximation and details, inducing signal sparsification
▶ Recursive analysis of the approximation can further sparsify the signal
▶ It is possible to find FIR filterbanks with perfect reconstruction and any number of vanishing moments (i.e., ability to remove polynomial parts of the signal)
▶ However we must choose between symmetry (which avoids frequency leaking) and orthogonality: for compression symmetry is more important
▶ The most compact filters achieving these properties are the Daubechies filters
▶ In image compression, 2 filterbanks are used:
  ▶ Daubechies 9/7: four vanishing moments, best fit for image compression
  ▶ Daubechies 5/3: two vanishing moments, but integer-valued filter taps, allowing for error-free reconstruction
▶ The filterbanks are equivalent to a linear transform (matrix multiplication), referred to as Discrete Wavelet Transform (DWT)

---

**Immagini estratte:**

![Figura estratta 1](p48_img01.jpg)
