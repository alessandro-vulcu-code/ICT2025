Function templates: example

```cpp
template<typename T1, typename T2>
std::pair<T1,T2> make_pair(T1 a, T2 b)
{
    return {a,b};
}

// .....
auto x = make_pair(1,2);
// x is a std::pair<int,int>

auto y = make_pair(string("New York"),7.7);
// y is a std::pair<string,double>
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p16_img01.jpg)
