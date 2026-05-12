Initializer-list constructors

• It is a constructor with argument of type `std::initializer_list<T>`
• It accepts an arbitrary number of homogeneous arguments
• The list is
  • passed by value, but the process is still efficient
  (std::initializer_list<T> is a small type, basically an handle to an array of T)
  • has an iterator
  • has immutable values (no move operations)

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p21_img01.jpg)
