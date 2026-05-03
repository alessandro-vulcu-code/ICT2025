Unique pointer

Unique pointer
it is a scoped pointer, i.e.:

• its constructor takes a new raw pointer and wraps it
  `std::unique_ptr<string> up(new std::string("ciao"));`

• its destructor performs the delete
  • i.e., the pointed object is destroyed when up goes out of scope, or when it is assigned to another unique pointer

Main characteristics:

• It cannot be copied (no copy constructor), just moved
• It is the most lightweight smart pointer
• It represents the exclusive ownership of a pointer

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)
