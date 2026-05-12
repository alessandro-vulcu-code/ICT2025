Move

• a move operation could be convenient for resource handles, given that a move is more efficient than a copy (there is no acquisition of new resources)
• the move for built-in types is a copy
• the compiler knows it can use a move when
  • executing a return statement from a function
  • the argument is an rvalue reference

std::move is a function that returns an rvalue reference
• it does not actually move anything
• it tells the compiler that it can use the move constructor/assignment, if available for the type that is being considered, otherwise it can perform a copy

---

**Immagini estratte:**

![Figura estratta 1](images/p36_img01.jpg)
