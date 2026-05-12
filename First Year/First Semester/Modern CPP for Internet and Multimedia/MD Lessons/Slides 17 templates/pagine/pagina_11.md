Type aliases

Particularly useful for templates

• the type T is available only to the template
• with an alias, it is possible to refer to it outside the template as well
• the same alias can be used for different templates, to write generic algorithms (“associated types”)
• example: `iterator or value_type`

```cpp
template<typename T>
class Vector {
public:
    using value_type = T;
    using iterator = Vector_iter<T>;  // Vector_iter
    // is another class
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)
