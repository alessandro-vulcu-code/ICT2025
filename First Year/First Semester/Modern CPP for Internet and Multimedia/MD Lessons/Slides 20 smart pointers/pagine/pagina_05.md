Dangling pointer - example

You are trying to access a pointer whose associated object has been deleted, so it doesn’t point to any valid memory.

Very dangerous: in the case the distruction is still pending, you may access the old content, so your test may not recognize it.

```cpp
char* buffer = new char [256];
delete []buffer;
std::cout << *buffer
```

THIS IS A DANGLING POINTER!
RESULT = UNDEFINED BEHAVIOR
ONE of the MAIN BUGS in C++

```cpp
char* buffer = new char [256];
delete []buffer; // now buffer is dangling
buffer = null; // now it is not dangling anymore
```

---

**Immagini estratte:**

![Figura estratta 1](p05_img01.jpg)
