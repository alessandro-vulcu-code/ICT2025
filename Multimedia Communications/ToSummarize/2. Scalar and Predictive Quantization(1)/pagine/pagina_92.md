Lloyd-Max algorithm for data

In real-life problems, we have not signal PDFs, but rather a bunch of data

We can modify Lloyd-Max algorithm as follows:

1. Let $\mathcal{X} = \{u_1, u_2, \ldots, u_M\}$ be the set of data to quantize (or the training set if data is not known in advance)
2. Initialize $(k=0)$ with any dictionary (e.g. uniform): $\mathcal{C}^{(k)} = \{\widehat{x}_0^j\}_{i=1,\ldots,L}$
3. Nearest neighbor rule:

$$W_k^i = \{u_m \in \mathcal{X} : \forall j \neq i \|u_m - \widehat{x}_k^i\| \leq \|u_m - \widehat{x}_k^j\|$$

4. Centroid rule: $\widehat{x}_k^j_{k+1} = \frac{1}{|W_k^i|} \sum_{u_m \in W_k^i} u_m$
5. Iterate to step 3 until convergence

---

**Immagini estratte:**

![Figura estratta 1](images/p92_img01.jpg)
