Example of class

```cpp
class X {
// the representation (implementation) is private
private:
    int m;
public: // the user interface is public
    X(int i = 0) :m{i} { } // constructor
    // member function with definition
    int mf(int i) {
        int old = m;
        m = i;
        return old;
    }
};
```

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)
