Shallow copies and shared state

• If a class has pointers as members, the default copy copies only the pointers – not the value pointed by the pointer

• This violates independence: operations on any of the two objects after the copy will change the state of the other (shared state)

• This is called shallow copy
  • It generally creates more problems than performance benefits
  • Use it only if strictly necessary
  • A deep copy copies the value of the region of memory pointed to by the pointer

---

**Immagini estratte:**

![Figura estratta 1](images/p31_img01.jpg)
