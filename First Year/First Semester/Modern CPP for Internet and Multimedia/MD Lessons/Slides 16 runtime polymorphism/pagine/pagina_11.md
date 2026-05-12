Misuses of RTTI

• do not use dynamic_cast in a constructor
  • the information on the object you are constructing is not complete

• use RTTI only when necessary
  • compile-time type checking (i.e., no run-time polymorphism – directly use the exact type) is safer and has less run-time overhead

• prefer interfaces and virtual functions
  • when it is possible to design base classes

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)
