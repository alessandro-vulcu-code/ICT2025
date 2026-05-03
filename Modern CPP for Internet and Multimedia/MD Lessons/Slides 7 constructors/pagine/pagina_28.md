Delegating constructors

Use a delegating or forwarding constructor

```java
class X {
    int a;
public:
    X(int x) {
        if (0 < x && x <= max) {a=x;}
        else throw Bad_X(x);
    }
    X() : X{22} {}
    X(string s) : X{to<int>s} {}
// ...
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p28_img01.jpg)
