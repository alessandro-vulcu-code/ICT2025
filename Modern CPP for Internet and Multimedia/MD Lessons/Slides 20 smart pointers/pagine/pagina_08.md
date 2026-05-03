Raw pointers memory leak - example

```c
int performTask() {
    char* buffer = new char [256];

    ...
    ...
    ...
    if(<some_condition>) {
        delete []buffer;
        return 1;
    }
    delete []buffer;
    return 0;
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)
