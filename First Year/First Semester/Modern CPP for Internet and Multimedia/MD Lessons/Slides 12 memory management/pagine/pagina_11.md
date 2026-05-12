Memory management issues

2. Premature deletion (dangling pointer)
• call delete and then try to reuse the pointer
• this leads to bad write/read operations

```c
int f() {
    int* a {new int{10}};

    if (*a = 10)
    {
        delete a;
    }

    // some code
    *a = 5;
}
```

if *a is 10, the area of memory which a was associated to could now be associated to something else

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)
