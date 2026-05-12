Variadic templates

• C++ type-safe mechanism to provide an arbitrary number of parameters with arbitrary types

```cpp
template<typename T, typename ... Args>
void f(T value, Args ... args)
{
    // do something
    // with value
    f(args ... );
}
```

parameter pack: sequence of type and value pairs from which the first is automatically removed at every recursive call

at the second call, the first entry is removed from args ... and passed as T value
• need to account for the case with an empty args

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p19_img01.jpg)
