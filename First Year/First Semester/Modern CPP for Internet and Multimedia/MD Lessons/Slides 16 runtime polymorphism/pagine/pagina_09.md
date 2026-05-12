Capturing bad_cast exception

• Exceptions are raised when an error is met at runtime in a C++ program
• A bad_cast is raised when a dynamic_cast fails to cast to the reference specified as type
• It is possible to enclose these dynamic_casts in try/catch blocks

```cpp
void f(B& r) {
    try {
        D& der_ref {dynamic_cast<D&>(r)};
        // other operations
    } catch (bad_cast) {
        // handle the error
    }
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)
