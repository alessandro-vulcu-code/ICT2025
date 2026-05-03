Run-time type information

dynamic_cast<T*>() is used when the compiler cannot check a priori if a conversion is correct

• it works from polymorphic types (base classes with virtual methods)
  • the target can be a concrete class with no virtual methods

• the compiler automatically associates information on the actual type of an object, which is then used at run-time (run-time type information or RTTI)

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)
