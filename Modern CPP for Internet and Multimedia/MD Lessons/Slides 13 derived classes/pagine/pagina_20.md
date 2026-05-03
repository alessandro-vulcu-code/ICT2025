Navigating class hierarchies - virtual

3. Virtual

A function declared virtual can be redefined (“overridden”) in a derived class

• it must keep the same list of arguments
• it must keep the same return type except for return type pointers or references that can be relaxed from the Base to the Derived class
• the complier and linker will guarantee that the correct function is called
• it is defined in the base class
  • it can be overridden in derived classes only if needed

---

**Immagini estratte:**

![Figura estratta 1](images/p20_img01.jpg)
