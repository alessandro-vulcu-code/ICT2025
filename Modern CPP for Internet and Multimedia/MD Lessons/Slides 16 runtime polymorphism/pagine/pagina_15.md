Other casts

```cpp
static_cast<T>()
```

• converts between related types
  • pointers in hierarchies
  • integral to enumerators
  • floating point types to integral (and vice versa)

• it does not examine the object it casts from
  • no run-time costs, no checks

• the compiler cannot assume anything on memory pointed by void*: dynamic_cast does not work with void*
```

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)
