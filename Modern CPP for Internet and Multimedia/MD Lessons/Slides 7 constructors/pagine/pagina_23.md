Initializer-list constructors

```cpp
template<class T> class Vector {
public:
    Vector(std::initializer_list<T> s);
// ...
private:
    int sz;
    T* elem;
    void reserve(int size);
};

template<class T>
Vector::Vector(std::initializer_list<T> s) : sz{s.size()}
{
    reserve(sz); // get the right amount of space
    std::uninitialized_copy(
        s.begin(), s.end(), elem);
    // initialize elements in elem[0:s.size()]
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p23_img01.jpg)
