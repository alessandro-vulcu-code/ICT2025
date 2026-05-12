Function templates: lvalue and rvalue

• It is possible to distinguish lvalues and rvalues as arguments even with function templates

```cpp
template<typename T>
class Xref {
public:
    Xref(int i, T* p); // pointer
    Xref(int i, T& lvref); // lvalue ref
    Xref(int i, T&& rvref); // rvalue ref

private:
    T* elem;
}
```

---

**Immagini estratte:**

![Figura estratta 1](p18_img01.jpg)
