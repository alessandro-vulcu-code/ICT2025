Solving circular reference: use weak pointers

```c
struct Son{
    weak_ptr<Mum> mum
};
struct Mum{
    weak_ptr<Son> son
};
main() {
    shared_ptr<Son> son1 =
        make_shared <Son>();
    shared_ptr<Mum> mum1 =
        make_shared <Mum>();
    son1->mum = mum1; // obj2 use_count = 1
    mum1->son = son1; // obj1 use_count = 1
} NOW THEY ARE CORRECTLY DESTROYED
```

---

**Immagini estratte:**

![Figura estratta 1](images/p22_img01.jpg)
