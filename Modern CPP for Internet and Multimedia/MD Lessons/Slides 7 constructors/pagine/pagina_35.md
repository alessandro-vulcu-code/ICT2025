Move

After x is moved to y
• y owns the resources/values that x had
• x is left in a valid state (the destructor can be called, possibly efficiently), but it does not own anymore resources and/or does not have a valid logical state

C++ provides
• move constructor – X(X&&)
  • it gets ownership of the resources of the argument while initializing a new object
  • the argument is an rvalue reference, to differentiate from copy
  • the argument is non const, because it may need to be modified
• move assignment – X& operator = (X&&)

---

**Immagini estratte:**

![Figura estratta 1](images/p35_img01.jpg)
