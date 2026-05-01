Context-based coding

- Estimation of joint probability $P(X^K)$ may be difficult
- On the other hand, often a symbol only depends on a few neighbors
- We define as context a set of a few, let us say $N_S$ previous symbols that mainly impacts on the current one
- The number of possible contexts is $N_C = M^{N_S}$ at most
  - Contexts may be clustered in order to reduce complexity and improve probability estimation
- Using $N_C$ contexts is equivalent to having $N_C$ different arithmethic encoders and switching from the one to the other

---

**Immagini estratte:**

![Figura estratta 1](images/p86_img01.jpg)
