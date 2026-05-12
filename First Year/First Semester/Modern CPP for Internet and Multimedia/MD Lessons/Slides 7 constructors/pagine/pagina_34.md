Shallow copies and shared state

It is possible to avoid shallow copies by providing a user-defined copy constructor & assignment

```c
struct S {
    int* p;
    S (const S& a) : p{new int{*a}} {}
};

void f2()
{
    // create a new object
    S x {new int{0}};
    // copy with non-default deep copy
    S y {x};
    *(y.p) = 1;
    std::cout << *(x.p);
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p34_img01.jpg)
