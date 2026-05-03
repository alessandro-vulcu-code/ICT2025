# Member types for containers

| Member types (§iso.23.2, §iso.23.3.6.1) |
| :--- |
| `value_type` Type of element |
| `allocator_type` Type of memory manager |
| `size_type` Unsigned type of container subscripts, element counts, etc. |
| `difference_type` Signed type of difference between iterators |
| `iterator` Behaves like `value_type*` |
| `const_iterator` Behaves like `const_value_type*` |
| `reverse_iterator` Behaves like `value_type*` |
| `const_reverse_iterator` Behaves like `const_value_type*` |
| `reference` `value_type&` |
| `const_reference` `const_value_type&` |
| `pointer` Behaves like `value_type*` |
| `const_pointer` Behaves like `const_value_type*` |
| `key_type` Type of key; associative containers only |
| `mapped_type` Type of mapped value; associative containers only |
| `key_compare` Type of comparison criterion; ordered containers only |
| `hasher` Type of hash function; unordered containers only |
| `key_equal` Type of equivalence function; unordered containers only |
| `local_iterator` Type of bucket iterator; unordered containers only |
| `const_local_iterator` Type of bucket iterator; unordered containers only |

page 896, c++pl

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)
