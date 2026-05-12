Member functions

• Functions declared within a class definition
• They are invoked only for variables of the appropriate type
• Definition:
  • in a separate location (usually a .cpp file) than the declaration (usually in header .h file). In this case, the definition needs to have the name of the class
  • in the class declaration
    • small and rarely modified functions – otherwise, the code that uses them is recompiled every time the function is modified
    • they are implicitly inlined
      recall from the class on functions: inline = new code for every function call, instead than of a single code in memory that is pointed to by every function call.

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)
