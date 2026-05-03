Binary and unary operators

Binary operators

• Two arguments
  • Non-static member with the form `aa.operator@(bb)`
  • Non-member function with the form `operator@(aa, bb)`

Unary operators

• One argument (prefix or postfix)
  • Non-static member with the form `aa.operator@()`
  • Non-member with the form `operator@(aa)`

this is necessary for operators where aa is not in our control:
• built-in types
• user-defined types defined by someone else

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)
