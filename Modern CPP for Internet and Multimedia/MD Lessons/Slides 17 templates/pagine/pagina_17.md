Function templates: example

• If the parameters cannot be deduced automatically, it is necessary to specify them with the `<>` notation
• For example, “factory” functions used to create other objects (and have no arguments related to the type)

```cpp
template<typename T>
T* create();

void f()
{
    int* p = create<int>();
    int* q = create(); //ERROR
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p17_img01.jpg)
