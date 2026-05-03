Dynamic cast

C++ has a typed conversion operation that
• returns a valid pointer if the object is of the expected type
• nullptr otherwise

```cpp
void f(B* ptr)
{
    D* der_ptr {dynamic_cast<D*>(ptr)};
}

if ptr points to an object of type D, der_ptr is valid,
otherwise is a nullptr
```

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)
