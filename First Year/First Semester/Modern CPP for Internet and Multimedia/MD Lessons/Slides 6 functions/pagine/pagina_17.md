Array arguments

• The information on the size is lost – and not implicitly available to the function

• Workarounds:
  • Explicitly pass the size as argument
    void f(int* p, size_t size_of_the_array);

  • Pass a reference type to the array
    void f(int (&r)[1000]);

  the size is compulsory (part of the type), thus the flexibility of this call is limited

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)
