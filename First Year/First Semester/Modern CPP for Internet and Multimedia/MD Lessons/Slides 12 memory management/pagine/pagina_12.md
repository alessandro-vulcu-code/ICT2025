Memory management issues

3. Double deletion
• call delete and then call delete again
• this leads to memory corruption

```c
int f() {
    int* a {new int{10}};

    if (*a = 10)
    {
        delete a;
    }

    // some code
    delete a;
}
```

if *a is 10, the area of memory which a has already been released

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
