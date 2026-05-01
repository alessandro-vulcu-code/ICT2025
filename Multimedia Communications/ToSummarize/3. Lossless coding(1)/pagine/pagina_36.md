Distribution with maximum entropy

Let us go back to our constrained maximization problem:

$$p^* = \arg \max_p \sum_{i=1}^{M} p_i \log \frac{1}{p_i}$$

$$\sum_{i=1}^{M} p_i = 1$$

The distribution maximizing the entropy of a $M$-ary discrete r.v. is found applying the Lagrange's method: $p^* = \left[ p_1^* p_2^* \dots p_M^* \right]$ such that $p_i^* = \frac{1}{M}$

$$J(p) = -\sum_{i=1}^{M} p_i \log p_i + \lambda \left( \sum_{i=1}^{M} p_i - 1 \right)$$

$$\frac{\partial J}{\partial p_i} = -\left( \frac{\log e}{p_i} p_i + \log p_i \right) + \lambda$$

$$\log p_i^* = \lambda - \log e = \text{constant}$$

---

**Immagini estratte:**

![Figura estratta 1](images/p36_img01.jpg)
