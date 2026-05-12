# Mutability

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

        string Date::string_rep() const
        {
            if (!valid_cache) {
                // update string_cache
                compute_cache_value();
                valid_cache = true;
            }
            return string_cache;
        }
}
```

---

**Immagini estratte:**

![Figura estratta 1](p22_img01.jpg)
