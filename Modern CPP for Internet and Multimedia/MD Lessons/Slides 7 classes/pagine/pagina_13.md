Example of friend classes

```cpp
class Y {
    friend X;
// class x can access both private and public
// members and functions of y
private:
    int v;
    int doSomething(double d);
// for public members, it is necessary to use a
// public label
public: // the user interface is public
    Y(int i =0) :v{i} { } // constructor
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)
