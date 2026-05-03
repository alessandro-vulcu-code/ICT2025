Operators new and delete

The free store memory is accessed through the operators

• new
  1. initializes memory and assigns a value
  2. returns a pointer to the memory area

• delete
  1. (in case) call the destructor of the object
  2. deallocate the heap memory

• generally, use {} (or ()) when initializing with new

```cpp
void f() {
  int* a {new int{10}};
  // some code
  delete a;
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)
