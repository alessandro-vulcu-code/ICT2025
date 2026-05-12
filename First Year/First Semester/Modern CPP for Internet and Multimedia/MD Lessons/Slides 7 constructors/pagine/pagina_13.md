Initialization without constructors

• It is not possible to define constructors for built-in types (e.g., int, char...)
  • they can just be initialized with a value (e.g., int a{1};)

• Similarly, there are options to initialize an object of a class without a constructor

1. Member-wise initialization (if the members are public)
   ```c
   struct Work {
       std::string name;
       int number;
   };
   ```

   Work some_work {"Teach", 19};
   std::cout << some_work.name << " " << some_work.number;
   ```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)
