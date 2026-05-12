Plain Old Data (POD)

• Simple types that can be copied or move around in memory without risks (e.g., with std::memcpy())
because they are contiguous in memory. A POD must have
  • No complex layout
  • No user-defined copy
  • Trivial default constructor (non user-provided)

```c
struct Trivial { // just a wrapper, actually useless
  int a;
  Trivial(int aa) : a(aa) { }
  Trivial() = default; // use the compiler generated
  // constructor
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)
