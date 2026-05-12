Conditional compilation

• They can be used for conditional compilation

```c
int a = 10;
#ifdef IDENTIFIER
//some code
#endif //IDENTIFIER (good practice to comment)
a -= 2;
```

Unless IDENTIFIER is identified somewhere in the code before this with #define IDENTIFIER, the code between #ifdef and #endif would not be compiled

---

**Immagini estratte:**

![Figura estratta 1](images/p30_img01.jpg)
