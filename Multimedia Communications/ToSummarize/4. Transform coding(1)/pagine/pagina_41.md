Modified HS Algorithm

1. We compute $R^*_k$ with Huang-Schulteiss;
2. If some $R^*_k$ are negative, we remove the variances of the concerned components and we repeat the computation. The removed variables are not coded (i.e., “coded with zero bits”)
3. This step is repeated as long as there are negative allocation values.
4. The results are floored
5. The eventual residual rate is allocated to coefficients with the largest error

---

**Immagini estratte:**

![Figura estratta 1](images/p41_img01.jpg)
