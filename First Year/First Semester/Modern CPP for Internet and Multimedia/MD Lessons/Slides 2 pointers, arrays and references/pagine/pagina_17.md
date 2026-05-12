Optimizations with rvalue references

Classic swap function without rvalues and move semantic

```cpp
template<class T>
swap(T& a, T& b) // "old-style swap"
{
    T tmp {a}; // two copies of a
    a = b; // two copies of b
    b = tmp; // two copies of tmp (aka a)
}

3 copy operations + destructors + memory consumption
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)
