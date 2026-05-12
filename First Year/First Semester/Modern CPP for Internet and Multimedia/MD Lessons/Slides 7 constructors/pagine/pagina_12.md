Fixed constr/destr sequence of calls

• The operations that a constructor performs are in a fixed order:
  1. (in case the class is derived from another `base` class) the constructor of the base class is called
  2. the constructors of the data members of the class are called
  3. the body of the constructor is executed

• The same goes for the operations of the destructor
  1. the body of the destructor is executed
  2. the destructors of the data members of the class are called
  3. (in case the class is derived from another `base` class) the destructor of the base class is called

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
