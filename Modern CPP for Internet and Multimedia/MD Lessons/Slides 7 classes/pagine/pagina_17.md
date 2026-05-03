Explicit constructors

```java
class Date {
public:
    explicit Date(int d);
}

// ...
Date d = 15; // error
Date d {15}; // ok,
// {} considered explicit

class Date {
public:
    Date(int d);
}

// ...
Date d = 15; // ok, but
// not very clear
```

• It is a good practice to keep single argument constructors explicit
• Unless exceptions, e.g., `std::complex<double> c = 1;` - it naturally creates a complex with only the real part

---

**Immagini estratte:**

![Figura estratta 1](images/p17_img01.jpg)
