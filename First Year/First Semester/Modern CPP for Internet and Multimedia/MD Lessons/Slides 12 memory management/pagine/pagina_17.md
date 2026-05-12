Copy semantic and handle classes

Shallow copy issue: a default copy may not have the results you expect

Other strategies:

1. Prohibit copying (by using =delete or making the copy constructor private)
   Sometimes it does not make sense to copy a resource

2. Reference-count the resource
   Count how many RAII objects point to the resource, increase this by one when copying

3. Transfer ownership
   This however is closer to the move semantic

4. Copy the underlying resource
   Deep copy

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)
