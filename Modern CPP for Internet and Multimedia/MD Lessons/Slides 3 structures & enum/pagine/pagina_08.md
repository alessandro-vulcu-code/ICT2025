# struct constructors

• a struct is a simple version of a class: it can have constructors

```c
struct Points {
    std::vector<int> elem;
    Points (int n1, int n2) {
        elem.push_back(n1);
        elem.push_back(n2);
    }
};
```

• if a constructor is explicitly declared, then there is no default constructor

• Enforce invariants (conditions that must be always true in the lifetime of an object)

• Reorder/validate/modify arguments

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)
