List arguments

A {}-delimited list can be an actual argument to a parameter of type

1. use std::initializer_list<T>
2. reference to array of type T
3. type that can be initialized with the values in the list

```cpp
template<class T>
void f(initializer_list<T>);

template<class T, int N>
void f2(T (&r)[N]);

void g() {
    f({1,2,3,4}); // T is int + initializer_list has size 4
    f2({1}); // T is int N is 1
}
```

---

**Immagini estratte:**

![Figura estratta 1](p18_img01.jpg)
