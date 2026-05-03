new and delete implementation

• They are defined in the `<new>` header
  • but to use the new operator it is not necessary to include this header

• It is possible to overload new and provide additional parameters to customize its behavior

• delete should be overloaded to cope with the equivalent new

• Example: `placement syntax`
  • additional parameter that represents and area in memory that has already been allocated

```c
char *buf = new char[sizeof(string)]; // pre-allocated buffer
std::string *p = new (buf) std::string("hi"); // placement new
std::string *q = new std::string("hi"); // ordinary allocation
```

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)
