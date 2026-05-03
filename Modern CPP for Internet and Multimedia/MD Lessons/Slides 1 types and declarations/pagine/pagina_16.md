Initialization

```c
T a1 {v}; → Introduced in C++11
• Does not allow narrowing
  int a1 {0.2}; //compilation error
• Strongly recommended except with auto
• {} indicates initialization with default value
(if present)

T a2 = {v};

T a3 = v;

T a4(v);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)
