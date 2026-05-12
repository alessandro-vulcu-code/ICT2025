Sizes

• Implementation-defined
  • The standard leaves the size of the fundamental types to the implementation
  • Well-defined given a certain implementation, but don’t rely on it for portability

Language != what the compiler implements

• Multiple of char
• sizeof function returns the size in number of chars
• Some conditions are always valid, e.g.,
  • 1 ≡ sizeof(char) ≤ sizeof(short) ≤ sizeof(int) ≤ sizeof(long) ≤ sizeof(long long)
  • sizeof(float) ≤ sizeof(double) ≤ sizeof(long double)

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)
