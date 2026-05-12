Example of member functions

```cpp
class X {
    ...
    // member function with inlined definition
    int mf(int i) {
        int old = m;
        m = i;
        return old;
    }
    // member function with only declaration
    int amf(int j);
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)
