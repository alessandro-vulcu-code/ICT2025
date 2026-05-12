List arguments

If there is ambiguity, `std::initializer_list<T>` has the precedence – this may cause errors

```cpp
template<class T>
void f(initializer_list<T>);

template<class T, int N>
void f(T (&r)[N]);

struct S { int a; string s; };
void f(S);

void g() {
    f({1,2,3,4}); // T is int + initializer_list has size 4
    f({1,"MKS"}); // calls f(S), not all the values can be
                // implicitly cast to int
    f({1}); // T is int + initializer_list has size 1
}
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p19_img01.jpg)
