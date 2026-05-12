Raw pointers memory leak - example

```c
int performTask() {
    char* buffer = new char [256];
    ...
    ...
    ...
    if(<some_condition>) {
        return 1;
    }
    delete []buffer;
    return 0;
}
```

THIS IS A MEMORY LEAK!

Unless you don’t handle each case, remembering to write delete[] everywhere (in each try-catch blocks, before each return, etc.)

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)
