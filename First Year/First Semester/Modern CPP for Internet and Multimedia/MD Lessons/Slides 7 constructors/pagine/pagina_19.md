Default constructors

• It is a constructor that can be invoked without an argument
  • a default argument can make a constructor with arguments a default constructor. Use it with care!
    ```c
    struct Work {
        Work(std::string a =“work”) : name{a} {};
    };
    ```

• Do not use default arguments in base classes, but only in derived classes (it is substituted at compile time and not in run-time)!

• A default constructor is needed when
  • it makes sense to have a default value
  • the user-defined type is used as element type for a data structure (array, vector, etc)

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p19_img01.jpg)
