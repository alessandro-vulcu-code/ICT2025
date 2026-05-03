Resource Acquisition Is Initialization

• Objects (handle classes) can be used to manage resources
• RAII paradigm
  1. Acquire the resources (e.g., memory with new) and
  2. Immediately turn its control to resource-managing objects
• Called RAII because the same statement is used to initialize the handle & acquire the resources
• The resource-managing object then uses its destructor to make sure the resources are released (e.g., calls delete)
  • The destructor of such objects is automatically called when they go out of scope!

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)
