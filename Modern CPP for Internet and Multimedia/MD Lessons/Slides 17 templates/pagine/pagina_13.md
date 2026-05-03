Member templates

```cpp
template<typename S>
class complex {

S re, im;

public:
    template<typename T>
    complex(const complex<T>& c) :
        re{c.real()}, im{c.imag()} { }

// ... };

```

• by using a different type for the data members and the arguments of the constructor, it is possible to have well-defined conversions between inner types

```cpp
complex<float> cf1 {};
complex<double> cd1 {cf1}; // ok – float to double
complex<float> cf2 {cd1}; // error – narrowing
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)
