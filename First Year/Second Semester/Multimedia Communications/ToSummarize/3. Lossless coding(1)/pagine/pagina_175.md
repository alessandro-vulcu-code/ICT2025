Current Limitations of Neural Lossless Coding

Despite superior compression ratios, NLC faces significant deployment hurdles.

▶ **Computational Complexity**: AR models require $N$ forward passes for an $N$-pixel image, making real-time decoding nearly impossible without massive optimization.

▶ **Generalization Gap**: NNs are sensitive to "out-of-distribution" data. A model trained on natural images may fail (or expand) medical or satellite imagery.

▶ **Hardware Requirements**: Unlike Huffman or LZW, NLC requires GPUs or specialized AI accelerators (NPUs) at the decoder side.

▶ **Deterministic Requirements**: Lossless coding requires perfect bit-reproducibility across different hardware (handling floating-point rounding errors).

---

**Immagini estratte:**

![Figura estratta 1](images/p175_img01.jpg)
