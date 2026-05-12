```cpp
void* and nullptr

void f(int* pi)
{
    void* pv {pi}; // allowed
    *pv; // compilation error, cannot dereference *void
    // because the type is not implicitly known
    ++pv; // compilation error, cannot increment *void
    // because it does not know the size of the type

    void* pv2 {pi};
    bool pointToSameAddress {pv == pv2};

    int* pi2 {static_cast<int*>(pv)};
    double* pi3 {static_cast<double*>(pv)};
    //allowed but leads to logical errors!

    pi3 = nullptr; // does not point to anything
}
```

---

**Immagini estratte:**

![Figura estratta 1](p05_img01.jpg)
