Operators on pointers

• It is possible to apply operators to pointers
• They operate on the address (i.e., the value of the operator), not on the values the address points to!
• The increment (decrement) depends on the type of the object pointed to by the pointer
  T arrayt[4];
  T* pt = arrayt;
  pt++; // the numeric value is pt + sizeof(T)
• Subtraction $q - p$ is valid only for elements in the range of the array -> returns the number of elements in the range [p, q)
• Addition of pointers is not allowed (just integer values)

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)
