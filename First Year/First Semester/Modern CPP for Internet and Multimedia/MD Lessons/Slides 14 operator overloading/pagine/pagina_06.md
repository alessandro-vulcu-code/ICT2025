Overloading operators

• It is necessary to explicitly overload all the operators to be used
  • For example, the compiler does not infer operator+=() from operator+() and operator=()

• The rules related to passing arguments apply also in this case (value for built-in types, const lvalue references for user-defined types)

• It can be common to return a reference to this (with return type X& for user-defined type X)
  • useful for non-static member operators

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)
