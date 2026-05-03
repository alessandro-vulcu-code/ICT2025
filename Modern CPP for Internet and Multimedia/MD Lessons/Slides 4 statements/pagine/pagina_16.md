for statements – pre increment

• pre-increment: increment, and then evaluate the new value
• post-increment: increment the value but evaluate the old value

• In C++, pre-increment is preferred when they are equivalent (e.g., in for loops)
  • It avoids the (implicit) generation of an extra temporary variable
  • No difference with fundamental types
  • Performance difference with user-defined types (e.g., iterators on standard library data structures)

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)
