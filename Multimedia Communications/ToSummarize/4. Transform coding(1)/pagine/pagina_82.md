DCT Transformation Matrix

It can be shown that the following process:

▶ Create the mirror-periodic version $x_{\text{SYM}}$ of $x$
▶ Compute the DFT of $x_{\text{SYM}}
▶ Apply a “frequency domain modulation” (a mathematical trick that allows to obtain symmetrical, real valued coefficients)
▶ Keep only $M$ of the coefficients

is equivalent to a single orthogonal transform defined by the following matrix:

$$\left( \mathcal{T}_{\text{DCT}} \right)_{k,n} = \begin{cases} \frac{1}{\sqrt{M}}, & k = 0 \\ \sqrt{\frac{2}{M}} \cos \frac{(2n+1)k\pi}{2M}, & k > 0 \end{cases}$$

$k, n = 0, 1, \ldots, M-1$

---

**Immagini estratte:**

![Figura estratta 1](images/p82_img01.jpg)
