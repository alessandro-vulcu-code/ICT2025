Shared pointer

• It represents shared ownership.
  std::shared_ptr<string> sp(new string("ciao")); // *use_count = 1

• It is a counted pointer: it keeps track of how many shared pointers are pointing to the object (the copy constructor increments a pointer to a counter use_count)
  std::shared_ptr<string> sp2 = sp; // *use_count=2

• When the counter becomes zero, the pointer will be deleted automatically
  • The destructor does something like this:
    (*use_count)--;
    if(*use_count ≤ 0) {
      delete p;
    }

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)
