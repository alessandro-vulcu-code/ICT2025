Destructor - RAII

• ~ (“complement”) followed by the name of the class (e.g., for class X -> ~X)
• It does not accept arguments – only one destructor per class
• A destructor is guaranteed to be invoked when an object is destroyed, to clean up and release resources
• Resource Acquisition is Initialization (RAII) paradigm is a constructor/destructor-based resource management:
  • the constructor acquires the resources (e.g., memory)
  • the destructor releases them (e.g., free memory and return it to the control of the OS)
  • this is safer than letting a developer who is using a class manage directly the resources that an object of the class needs

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)
