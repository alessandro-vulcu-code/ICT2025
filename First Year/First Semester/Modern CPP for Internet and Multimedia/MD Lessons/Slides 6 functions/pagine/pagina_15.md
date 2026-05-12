Guidelines (from C++PL)

Follow these guidelines in order:

1. Pass-by-value for small objects
2. Pass-by-const-lvalue-reference for large objects, not to be modified
3. Return a results with return instead than by modifying the argument
4. Pass-by-rvalue-reference for move and forward (more on this in future lessons)
5. Pass a pointer if the “no object” case can be dealt with and represent “no object” with a nullptr that is portable
6. Pass-by-lvalue-reference only as last option if for some reason the argument needs to be modified by the function, the usage of a pointer can be clearer and easier to understand

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p15_img01.jpg)
