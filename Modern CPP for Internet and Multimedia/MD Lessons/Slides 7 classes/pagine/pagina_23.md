Mutability

To address this:

b. mutability through indirection – the properties that need to be updated can be placed in another object, with a pointer to it as member of the class
• const does not apply to objects accessed through pointers or references

```c
struct cache { bool valid; string rep; };
```

```cpp
class Date {
    int d {22};
    int m {02};
    int y {1992};
    cache* date_cache;
    ...
```

```cpp
    string Date::string_rep() const
    {
        if (!c->valid) {
            // update
            compute_cache_value();
            c->valid = true;
        }
        return c->rep;
    }
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p23_img01.jpg)
