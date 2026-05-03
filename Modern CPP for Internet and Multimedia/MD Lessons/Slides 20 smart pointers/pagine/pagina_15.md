Unique pointer

Other useful stuff:

• `string* s = up.release();` // returns the raw pointer, and up releases its ownership: up won’t point to it anymore and won’t delete it when destroyed. up now points to nullptr

• `up.reset();` // up loses the ownership of the pointer and destroys the object

• `up.reset(new string("hi"));` // up loses the ownership of the old pointer and destroys the old object acquiring the ownership of the new pointer

• Explicit constructor (no implicit constructor)

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)
