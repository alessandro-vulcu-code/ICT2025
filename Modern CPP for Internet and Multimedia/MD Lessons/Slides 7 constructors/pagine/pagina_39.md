Default operations

• By default, a class has
  • default constructor
  • default copy constructor
  • default move constructor
  • default copy assignment
  • default move assignment
  • default destructor

the compiler generates them if used in the program
it applies the operation to each non-static and base member (e.g., member-wise copy)

• A developer can control the generation of defaults:
  • if a constructor is declared, the default constructor is not generated
  • if one among a copy/move/destructor operation is declared, no copy/move/destructor operations are default-generated

---

**Immagini estratte:**

![Figura estratta 1](images/p39_img01.jpg)
