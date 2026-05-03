Mutability

• A name can refer to a object with values which are
  • Mutable
  • Immutable, i.e., const
• Member functions need to work on const objects

1. **Constant member functions**

```c
int getDay() const;
```

const is part of the type, it must be repeated also in the definition

These functions do not modify the value of the object

• Const member functions work on const and non-const objects
• Non-const member functions do not work on const objects

---

**Immagini estratte:**

![Figura estratta 1](images/p19_img01.jpg)
