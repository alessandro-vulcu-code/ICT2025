Wrong use of shared pointer

```c
struct Son{
    shared_ptr<Mum> mum
};
struct Mum{
    shared_ptr<Son> son
};
main() {
    shared_ptr<Son> son1 =
        make_shared <Son>();
    shared_ptr<Mum> mum1 =
        make_shared <Mum>();
    son1→mum = mum1; // obj2 use_count = 2
    mum1→son = son1; // obj1 use_count = 2
} CYCLIC REFERENCE → MEMORY LEAK!!
NONE OF THE SHARED PTR GOES OUT OF SCOPE
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p20_img01.jpg)
