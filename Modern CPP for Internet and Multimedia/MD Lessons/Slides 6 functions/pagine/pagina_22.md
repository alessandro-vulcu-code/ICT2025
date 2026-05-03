Overloaded functions

• Different functions usually have different names
• It could be convenient to name in the same way different functions that perform the same task on different types

Overloading
(already used for operators, e.g., +)

```cpp
void print(int); // print an int
void print(const char*); // print a C-style string

// using different names leads to more complex code
// and more difficult to maintain
void print_int(int);
void print_char(const char*);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p22_img01.jpg)
