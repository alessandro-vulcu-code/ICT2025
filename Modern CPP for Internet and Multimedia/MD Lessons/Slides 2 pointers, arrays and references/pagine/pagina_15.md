Lvalue References

• They refer to objects whose value can be changed

```c
int var {1};
int &ref {var};
int var2 = ref + 4;
int* pointer = &ref;
++ref;
++pointer;
```

• always need initialization
• cannot be changed after
• a reference can be used in the same way of a name
• points to var
• increase var
• increase the value of pointer

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)
