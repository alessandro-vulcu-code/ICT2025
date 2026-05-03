Pointer to function

• The code for a function is stored in memory
• It is possible to get its address in a pointer
  • It can be used `only` to call the function

```cpp
void error(int s); {
    // implementation
}

void (*efct)(int); // pointer to function that takes
// int as argument and does not return anything

void f() {
    efct = error; // same as efct = &error
    efct(10); // same as (*efct)(10), dereferencing
    // is optional
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)
