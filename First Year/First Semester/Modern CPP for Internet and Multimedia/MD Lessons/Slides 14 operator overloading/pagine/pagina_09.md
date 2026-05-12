```cpp
friend keyword

class Y
{
private:
    int j;
    friend std::ostream& operator<<
        (std::ostream& out, const Y& y);

public:
    ...
}    j is private in Y!

std::ostream& operator<<(std::ostream& out, const Y& y)
{
    out << y.j;    the overloaded operator is defined as non-
    member in the innermost enclosing scope
    (e.g., the namespace for a class)
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)
