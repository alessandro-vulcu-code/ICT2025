Raw pointers leak - example

```c
int performTask() {
    char* buffer = new char [256];

    ...
    ... // Some code here
    ... // of several lines
    ... // that may trow exception
    ... // or return something
    ... // before the end is reached
    ...
    delete []buffer;
    return 0;
}
```

THIS IS A LEAK!

Unless you don’t handle each case, remembering to write delete[] everywhere (in each try-catch blocks, before each return, etc.)

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)
