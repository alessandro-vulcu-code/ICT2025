Class templates

• Declared in the same way as MyString
• All the members **must** be defined and declared
• Put the definition in the header file, otherwise linker error

```java
// my-string.h
template<typename C>
class MyString {
public:
    MyString() { // do something }
    ...

• It is not possible to overload the name of a class template
    template<typename C> class MyString { ... };
    class MyString { ... }; // compilation error
```

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)
