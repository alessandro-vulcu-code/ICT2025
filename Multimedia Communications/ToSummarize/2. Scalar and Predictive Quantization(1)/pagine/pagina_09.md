# Definition : scalar quantization (SQ)

Scalar quantization (SQ) is a function $Q$ from $\mathbb{R}$ to a discrete set called *Dictionary*

$$Q : x \in \mathbb{R} \rightarrow y \in \mathcal{C} = \{\hat{x}^1, \hat{x}^2, \ldots, \hat{x}^L\} \subset \mathbb{R}$$

- $C$ : Dictionary, it is a discrete subset of $\mathbb{R}$
- $\hat{x}^i$ : quantization level, code-word
- $e = x - Q(x)$: Quantization noise
- $\Theta^i = \{x : Q(x) = \hat{x}^i\}$ : Decision regions or cells

Regions and levels completely define the SQ
Regions are typically defined as intervals: $\Theta^i = (t^i, t^{i+1})$
Therefore, thresholds and levels also completely define a SQ

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)
