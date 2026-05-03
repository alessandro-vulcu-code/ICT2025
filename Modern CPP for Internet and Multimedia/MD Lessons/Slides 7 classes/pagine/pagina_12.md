Example of public/private

```cpp
class X {
  // private unless after a public label
  int m;
  // it is possible to use a private label
  private:
    int m2;
    int doSomething(double d);
  // for public members, it is necessary to use a
  // public label
  public: // the user interface is public
    X(int i =0) :m{i} { } // constructor
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
