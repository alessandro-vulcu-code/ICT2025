When to use casts - recap

static_cast
• try it first, for conversions between related types and from void*
• for downcasts with polymorphic types, it does not do run-time type checking: prefer dynamic_cast

dynamic_cast
• for downcasting/crosscasting polymorphic types with run-time type checking

const_cast
• for removing constness from pointers and references to non const objects

reinterpret_cast
• the most disruptive, it converts between unrelated types (e.g., int* to int)

---

**Immagini estratte:**

![Figura estratta 1](images/p17_img01.jpg)
