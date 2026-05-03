deleted functions

It is possible to use the =delete keyword to
• prevent the compiler to use an otherwise default operation
• eliminate undesired conversions

```cpp
class X {
    X(int);
    X(double) =delete;
}
X(1); // ok
X(0.1); // does not compile

• control where a class can be allocated
    • =delete the new operator -> the class cannot go on the free store
    • =delete the destructor -> the class cannot go on the stack
    • deleting the destructor is not a good practice, because then objects cannot be actually destroyed – better to make it private
```

---

**Immagini estratte:**

![Figura estratta 1](images/p42_img01.jpg)
