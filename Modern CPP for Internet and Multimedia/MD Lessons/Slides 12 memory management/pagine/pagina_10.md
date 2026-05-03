Memory management issues

In general, it is hard to track the state of the objects in the free store

1. Memory leaks
   • call new and never call delete
   • if this is frequent, the system may run out of memory

```c
int f() {
    int* a {new int{10}};

    if (*a = 10)
    {
        return 4;
    }
    delete a;
    return 5;
}
```

if *a is 10, this delete is never reached and the memory pointed by a is never released

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)
