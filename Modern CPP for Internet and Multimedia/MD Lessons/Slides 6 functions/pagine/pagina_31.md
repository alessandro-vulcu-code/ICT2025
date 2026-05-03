Include guards

• An header file (.h) with some declarations and definitions may be included in multiple files
  e.g., #include <iostream> is included in every file that wants to use std::cout

• There can be errors if the compiler tries to compile the header multiple times (every time it sees an #include)

```c
#ifndef STRUCTS_ENUM_TEST
#define STRUCTS_ENUM_TEST

// code of the header

#endif /* STRUCTS_ENUM_TEST */
```

the first time the header is compiled, STRUCTS_ENUM_TEST is not defined, and this is true

STRUCTS_ENUM_TEST is thus defined

the next times, STRUCTS_ENUM_TEST is defined, and this is false, so the file is not considered for compilation

---

**Immagini estratte:**

![Figura estratta 1](images/p31_img01.jpg)
