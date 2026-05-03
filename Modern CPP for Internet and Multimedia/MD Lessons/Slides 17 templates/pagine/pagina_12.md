# Member templates

Members can be templates as well

```cpp
template<typename S>
class complex {

S re, im;

public:
    complex() :re{}, im{} {}

    complex(S rr, S ii =0) : re{rr}, im{ii} { }

    complex(const complex&) = default;

    template<typename T>
    complex(const complex<T>& c) :
        re{c.real()}, im{c.imag()} { }

// ... };
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
