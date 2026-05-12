Navigating class hierarchies

2. Type field – the object has a data member that holds the type of the object
• the correctness of this is not enforced by the compiler
• an addition of new derived classes requires changes in other classes
• limited and error prone techniques

```c
struct Employee {
    enum class Empl_type {manager, employee};
    Empl_type m_type;
    ...
    Employee() : m_type{Empl_type::employee} {}
}

struct Manager : public Employee {
    Manager () { m_type = Empl_type::manager; }
    ...
}
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p19_img01.jpg)
