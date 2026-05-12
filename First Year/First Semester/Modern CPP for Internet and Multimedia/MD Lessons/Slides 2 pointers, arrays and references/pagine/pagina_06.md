Pointers and Ownership

• Resource: something that is acquired and then released
  • memory
  • file

• A pointer is often as a handle to a resource

• Confusing: it is not possible to distinguish a pointer that owns a resource from one that does not

```c
int i2 = 7;
int* i = &i2; // i does not own resources

int* i3 = new int{7}; // i3 owns object on the free storage
```

• Rule of thumb: place pointers that own resources in an handle class (class that manages resources with constructors and destructors)

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)
