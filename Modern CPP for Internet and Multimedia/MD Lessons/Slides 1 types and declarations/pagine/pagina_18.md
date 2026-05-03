Initialize consistently

• If a name is declared and not initialized, the behavior is complex and hard to debug

```cpp
int globalVariable; // means globalVariable{}; → 0
Valid for static, global, namespace names

void f()
{
    int localVariable; // no well-defined value!
}
```

This happens for all local variables and objects on the heap, unless they are user-defined types with a default constructor

---

**Immagini estratte:**

![Figura estratta 1](images/p18_img01.jpg)
