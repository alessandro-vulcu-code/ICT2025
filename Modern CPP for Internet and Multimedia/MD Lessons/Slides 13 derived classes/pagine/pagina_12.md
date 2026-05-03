Constructors and destructors

• Each derived class can initialize the `base` and the members of the derived class – not directly those of the base

• Destructors of base classes are generally `virtual`

  • in this way, the destructor of subclasses is actually called
  • using `virtual` is the correct approach: the derived class may have more resources to release, or members that need to be cleared by the destructor -> the destructor defined by the base class may not be enough

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
