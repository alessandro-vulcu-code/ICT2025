Terminology of lossless coding

Lossless compression is based on data statistical properties. The basic idea is very simple: instead of using fixed-length coding, we use variable-length coding (VLC) with

▶ **Short codewords for probable symbols**
▶ **Long codewords for not probable symbols**

Definitions:

**Alphabet** : $\mathcal{X} = \{x_1, x_2, \ldots, x_M\}$ set of symbols to encode

▶ $\{0, 1, \ldots, 255\}$ for luminance values
▶ Latin alphabet for a text in French, English, ...

**Code** : application between $\mathcal{X}$ and $\{0, 1\}^*$, the set of finite-length bit strings

▶ Fixed-length coding
▶ Variable-length coding

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)
