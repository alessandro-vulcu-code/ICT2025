Ordered associative containers

This is an example of std::map usage

```cpp
std::map<int, std::string> map_int_s;

map_int_s.insert(std::make_pair(4, "four"));
map_int_s[5] = "five";
// this updates the value associated with
// the key, if present, or it performs the
// insertion otherwise.

auto entry_it = map_int_s.find(4);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)
