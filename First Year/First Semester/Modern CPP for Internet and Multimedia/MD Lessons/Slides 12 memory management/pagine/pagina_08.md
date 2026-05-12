new and delete implementation

```cpp
// allocate space for individual object
void* operator new(size_t) throw(std::bad_alloc);

// if (p) deallocate space allocated using operator new()
void operator delete(void* p);

// allocate space for array
void* operator new[](size_t) throw(std::bad_alloc);

// if (p) deallocate space allocated using operator new[]()
void operator delete[](void* p);

new operator vs operator new():
  • the second (operator new()) can be used by the first to allocate size_t uninitialized memory
  • the first (new) is used to construct an object on the free storage or heap, i.e., in order, it calls operator new() and then the constructor of the object
```

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)
