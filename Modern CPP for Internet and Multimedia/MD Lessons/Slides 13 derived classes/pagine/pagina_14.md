Slicing with copy constructors

```c
struct X {
    int m_number;
}

struct Y : public X {
    int m_second_number;
}

slicing example

// some code
void f(X *p)
{
    X h = *p; // if p points to a Y, only
    // m_number is copied (slicing)
}

Y example {1, 2};
f(&Y);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)
