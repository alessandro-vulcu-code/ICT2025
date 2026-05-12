Access to namespace members

• with the argument-dependent lookup
  • search for a function in the namespace of its arguments
  • it is particularly useful for operators

• the rules to find a function with the matching signature are as follows:
  • if the argument is a class member, first check the class, then the namespace
  • if the argument is a namespace member, first check the namespace, then the (eventual) enclosing ones, up to the global
  • if the argument is built-in (int, char, bool, etc), there are no associated namespaces

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)
