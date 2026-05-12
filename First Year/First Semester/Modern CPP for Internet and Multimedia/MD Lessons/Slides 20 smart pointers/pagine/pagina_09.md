Pointers: avoiding leaks

• Sol1: handle each case, paying attention to writing `delete[]` everywhere the scope may be interrupted (in each `try-catch` blocks, before each `return`, etc.)
  • Writing code like this is very messy, you must pay a lot of attention and it is hard to maintain

• Sol2: RAII (Resource allocation is initialization), i.e., let a wrapper class allocate the pointer on construction and remove the allocation on destruction

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)
