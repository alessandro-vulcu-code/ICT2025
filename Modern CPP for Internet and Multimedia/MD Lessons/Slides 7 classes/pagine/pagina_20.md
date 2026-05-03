Mutability

2. Logical constness

A const member function may need to change a member data value, without affecting the actual representation (logical value) of the object

• example: the cache of a string representation of the object value
  class Date {
    int d {22};
    int m {02};
    int y {1992};
    std::string string_cache;
    bool valid_cache;

    public:
      std::string string_rep() const;
  }

• string_rep does not change the status of the object, but it may need to update string_cache if d, m, or y are changed

---

**Immagini estratte:**

![Figura estratta 1](images/p20_img01.jpg)
