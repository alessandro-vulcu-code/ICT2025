C++ program memory

Different areas of memory have different uses:

1. **const data area**
   - for data known at compile time
   - no user-defined types (only built-in)
   - available throughout the whole program lifetime
   - read-only

2. **stack**
   - memory for “automatic” variables (e.g., local variables in functions)
   - the memory is allocated sequentially (just before an object is created)...
   - and de-allocated sequentially (stack unwinding)
   - it is not possible to directly manipulate this area of memory

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)
