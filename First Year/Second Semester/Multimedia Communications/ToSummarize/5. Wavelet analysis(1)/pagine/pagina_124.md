EBCOT

Optimization

▶ If we keep all the bitstreams of all the codeblocks, we end up with a huge bitrate
▶ We have to truncate the bitstream to attain the target bit-rate
▶ Problem: how to truncate the bitstreams with a minimum resulting distortion?

$$\min \sum_i D_i \quad \text{subject to} \quad \sum_i R_i \leq R_{\text{tot}}$$

▶ Solution : Lagrange multiplier

$$J = \sum_i D_i + \lambda \left( \sum_i R_i - R \right)$$

---

**Immagini estratte:**

![Figura estratta 1](images/p124_img01.jpg)
