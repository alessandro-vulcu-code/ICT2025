Delegating constructors

Use a common function

```java
class X {
    int a;
    validate(int x) {
        if (0 < x && x <= max) {a=x;}
        else throw Bad_X(x);
    }
public:
    X(int x) { validate(x); }
    X() { validate(22); }
    X(string s) { int x = to<int>(s); validate(x); }
// ...
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p27_img01.jpg)
