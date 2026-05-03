Initializer-list constructors

• There are two rules for the overload resolution with constructors:
  • if the ambiguity is between a default or an initializer-list constructor, use the default
  • if the ambiguity is between an initializer-list or an ordinary constructor, use the list (this avoids different resolutions with different number of elements)

```c
struct X {
    X(initializer_list<int>);
    X();
    X(int);
};

X x0 {}; // empty list: default constructor
X x1 {1}; // one integer: initializer-list constructor
X x2 (1); // explicitly call X(int);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p22_img01.jpg)
