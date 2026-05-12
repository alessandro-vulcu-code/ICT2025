Unordered associative containers

1. `std::unordered_map<K, V, H, E, A>` unordered map from K to V
   type of the key
   type of the value
   equality test, by default
   `std::equal_to<K>`
   type of the allocator
   hash function to project the key into a searchable space, by default `std::hash<K>`

2. `std::unordered_multimap<K, V, H, E, A>` unordered map from K to V, it allows multiple entries with the same key

3. `std::unordered_set<K, H, E, A>` unordered set of elements with value K

4. `std::unordered_multiset<K, H, E, A>` unordered set of elements with value K, it allows multiple entries with the same value

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
