Shallow copies and shared state

```c
struct S {
    int* p;
};

void f()
{
    // create a new object
    S x {new int{0}};
    // copy with default copy
    S y {x};
    // any change on y also changes x
    *(y.p) = 1;
    std::cout << *(x.p);
}
```

![Diagram of shared state with x and y states](image)

x state: 0x1223414f2
shared: 0
y state: 0x1223414f2

---

**Immagini estratte:**

![Figura estratta 1](images/p32_img01.jpg)
