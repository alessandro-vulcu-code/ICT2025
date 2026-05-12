Constructor

• Invariants need to be maintained also when copying & moving, not just when creating an object from scratch

• If the constructor cannot enforce the invariants (e.g., the parameters that are passed to the ordinary constructor are not valid), it must not create the object

• When halting the construction, make sure that no resources are leaked, i.e.,
  • something that was acquired must be released
  • make sure to release everything

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)
