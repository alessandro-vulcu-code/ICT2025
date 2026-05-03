Optimizations with rvalue references

Classic swap function with rvalues

```cpp
template<class T>
swap(T& a, T& b)
{
    T tmp {static_cast<T&&>(a)};
    a = static_cast<T&&>(b);
    b = static_cast<T&&>(tmp);
}
```

this is equivalent to `std::move(tmp)`

`std::move()` does not move, but casts to an rvalue reference so that types with move constructors or assignment can exploit it

```cpp
T tmp {std::move(a)};
a = std::move(b);
b = std::move(tmp);
```

this returns an rvalue reference of type T&& to a

if T has a move constructor (more later), there is a benefit to pass a with an rvalue reference, because it will exploit a move operation instead of a copy operation

no unneeded copies!

---

**Immagini estratte:**

![Figura estratta 1](images/p18_img01.jpg)
