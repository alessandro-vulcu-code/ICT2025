Operator overloading

It is possible to redefine operators for a certain user-defined type

```cpp
class Complex { // very simplified complex

    double re, im;

public:
    Complex(double r, double i) :re{r}, im{i} { }
    Complex operator+(const Complex&);
    Complex operator*(const Complex&);
};

The name of an operator is "operator" followed by the symbol a * b = a.operator*(b)

// so that you can write
Complex c = Complex{2, 3} + Complex{5, 6};
Complex d = c * Complex{0, 1};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)
