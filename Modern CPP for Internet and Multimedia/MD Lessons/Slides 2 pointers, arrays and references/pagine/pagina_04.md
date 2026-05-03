```markdown

void* and nullptr

• Void* is the type “pointer to object of unknown type”
  • Limited set of operations are allowed:
    • Assign to other void*
    • Compare with other void*
    • Explicitly convert to another type using `static_cast<T>()` (unsafe)
  • Generally used to pass (or return) pointers to (from) functions without assumptions on the type
  • Very low-level

• nullptr is the value of a pointer that does not point to any object
```

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img01.jpg)
