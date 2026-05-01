Overcoming the Curse of Dimensionality

▶ Traditional Approach: State-space explodes exponentially ($M^N$). A 3-pixel context at 8 bpp requires $\approx 16.7$ million entries.

▶ Neural Approach: Maps contexts to a continuous vector space. It learns to group similar patterns, generalizing even to unseen contexts.

▶ Efficiency: While classical context-coding reached 0.406 bpp for the T-shape, NLC aims for the true entropy rate $\mathcal{H}$ by leveraging global dependencies (Attention/Transformers).

Key takeaway: NNs replace look-up tables with non-linear function approximation.

---

**Immagini estratte:**

![Figura estratta 1](images/p166_img01.jpg)
