Mutability

To address this:

a. declare members mutable – they can be modified even in const objects
• this is ok only if a small part of the object needs to change

```cpp
class Date {
  int d {22};
  int m {02};
  int y {1992};
  mutable std::string string_cache;
  mutable bool valid_cache;
  ...
public:
    std::string string_rep() const;
private:
    void compute_cache_value() const;
```

---

**Immagini estratte:**

![Figura estratta 1](images/p21_img01.jpg)
