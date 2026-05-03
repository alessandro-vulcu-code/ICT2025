Pass by value

• When a variable is passed by value from the caller to the called function, the value of the variable is copied into a new variable, which is independent on the first

• The function `does not` modify the variable that is passed to it, but copies the value into a new one and uses that

```cpp
void increment(int a)
{
    ++a;
    std::cout << a << std::endl; // when called
    // as below, this will print 3
}

int a = 2;
increment(a);
std::cout << a << std::endl; // this prints 2 – the
// variable a outside of the function is not modified
```

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)
