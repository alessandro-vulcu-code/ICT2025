C++ strings

• strings are implemented with a template that accepts different kinds of character types
• the characters are stored contiguously (as in an array)

```cpp
template<typename C,
typename Tr = char_traits<C>,
typename A = allocator<C>>
class basic_string {
public:
    using traits_type = Tr;
    using value_type = typename Tr::char_type;
    using allocator_type = A;
    using size_type = typename allocator_traits<A>::size_type;
    using difference_type = typename allocator_traits<A>::difference_type;
    using reference = value_type&;
    using const_reference = const value_type&;
    using pointer = typename allocator_traits<A>::pointer;
    using const_pointer = typename allocator_traits<A>::const_pointer;
    using iterator = /* implementation-defined */;
    using const_iterator = /* implementation-defined */;
    using reverse_iterator = std::reverse_iterator<iterator>;
    using const_reverse_iterator = std::reverse_iterator<const_iterator>;

    static const size_type npos = -1; // integer representing end-of-string
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p29_img01.jpg)
