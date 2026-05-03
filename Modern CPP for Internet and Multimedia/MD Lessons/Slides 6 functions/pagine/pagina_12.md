Pass by reference

• When a variable is passed by reference from the caller to the called function, the value of the variable is *not* copied into a new variable

• The function *does directly modify* the variable that is passed to it (unless it is declared const)

```cpp
void increment(int& a)
{
    ++a;
    std::cout << a << std::endl; // when called
    // as below, this will print 3
}

int a = 2;
increment(a);
std::cout << a << std::endl; // this prints 3 – the
// variable a of the caller has been modified by the
// function
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
