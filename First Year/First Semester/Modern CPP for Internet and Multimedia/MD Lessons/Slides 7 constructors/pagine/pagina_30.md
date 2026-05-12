Copy

• a developer can implement a custom version of the copy constructor and assignment
• the compiler can generate default copy operations
  • member-wise copy
  • this makes sure the value of every member is copied
  • but it may lead to errors with objects that have pointers as data members

```c
struct Work {
  std::string name;
  int number;
  ...
  Work(const Work & w) : name{w.name}, number{w.number} {}
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p30_img01.jpg)
