Functions declarations

A function declaration has multiple parts:

• **inline** (optional)
  keyword that suggests to the compiler to generate *new code* for every function call, instead than of a single code in memory that is pointed to by every function call. This enables an optimization in terms of execution speed. The compiler is *not required* to respect the inline keyword

• **constexpr** (optional)
  specifies that the function can be evaluated at compile time simple, no loops, no side effects (e.g., no changes to global variables)

• **noexcept** (optional)
  specifies that a function cannot throw an exception

• **static** (optional)
  for linkage, more on this in following lessons

• other keywords for functions defined in classes (member functions)

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)
