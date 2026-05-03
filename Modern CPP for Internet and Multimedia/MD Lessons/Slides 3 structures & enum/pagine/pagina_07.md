# struct declarations

• the type of the struct is immediately available
  ```c
  struct Example {
    Example* pointer_to_other; // correct: the size
  }; // of a pointer is fixed and defined
```

• but new objects of this type can be declared only after a complete definition
  ```c
  struct Example {
    Example other; // error: the size of example is
  }; // unknown
```

• it is possible to declare the name and define it later (forward declaration)
• struct names (which are types) can be overloaded by variables: `this must be avoided`

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)
