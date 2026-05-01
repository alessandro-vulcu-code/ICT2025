Why the Equality in Kraft’s Constraint?

To minimize $L = \sum p_i \ell_i$, we must use the available "prefix space" efficiently.

The "Unused Branch" Argument:

▶ If $\sum 2^{-\ell_i} < 1$, there exists at least one leaf in the binary tree that is neither a codeword nor a descendant of one.

▶ We could shorten some codewords by moving them "up" the tree.

▶ Shortening $\ell_i$ strictly decreases $L$ (since $p_i > 0$).

Conclusion: The minimum average length $L^*$ must satisfy the active constraint:

$$\sum 2^{-\ell_i}^* = 1$$

This represents a Complete Code: an efficient tree with no "wasted" branches.

---

**Immagini estratte:**

![Figura estratta 1](images/p48_img01.jpg)
