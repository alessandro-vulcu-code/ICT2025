Call to a member function

```cpp
std::ostream& operator<< (std::ostream& out, const Y& y)
{
    return y.someFunction(out);
}

class Y
{
private:
    int j;
public:
    std::ostream& someFunction(std::ostream& out)
    {
        out << j;
        return out;
    }
}
```

Overloading <

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)
