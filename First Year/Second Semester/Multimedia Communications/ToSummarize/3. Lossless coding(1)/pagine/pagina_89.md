Block Coding vs. Context-Based Coding

The Engineer’s Challenge: Finding the Right Context

Instead of increasing the block size $K$ indefinitely, it is more efficient to use context-based coding.

► If the context captures the "significant past" (e.g., the Markov order $N$), we reach the entropy rate $\mathcal{H}$ without massive blocks.

► Too large context: Sparse data makes probability estimation unreliable.

► Too small context: Fails to capture the dependencies, leaving redundancy.

---

**Immagini estratte:**

![Figura estratta 1](images/p89_img01.jpg)
