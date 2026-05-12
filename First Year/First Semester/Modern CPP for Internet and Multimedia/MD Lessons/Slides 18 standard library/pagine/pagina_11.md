Map element access

```cpp
//SOL1 : use []
std::string s1 = map_int_s[7]; // if k = 7
// is not present, it adds map_int_s[7] =
// std::string{} and returns it

//SOL2: use find() → best option
auto entry_it = map_int_s.find(4);
if(entry_it ≠ map_int_s.end()) {
    std::string s2 = entry_it.second()
} // it uses iterators: if k = 4 is not
// present, it returns map_int_s.end()
```

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)
