Pass by reference

• It is not a good practice to modify arguments passed by reference
  • It is better to explicitly return the modified value – this makes the code clearer and easier to maintain

• It can be more efficient to avoid the copy (with pass-by-value) of large objects

use const references
for large objects which do not need to be copied and/or modified in the function itself

void f(const LargeType& a)

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)
