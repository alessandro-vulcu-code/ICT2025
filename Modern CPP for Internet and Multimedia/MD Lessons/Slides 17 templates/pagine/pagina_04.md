Templates - example

```cpp
template<typename C>
class MyString {
public:
    String();
    explicit String(const C*) { // impl }
    String(const String&) { // impl }
    String operator=(const String&) { // impl }
    // ...
    C& operator[](int n) {
        return ptr[n];
    }
    String& operator+=(C c) { // impl }
    // ...
private:
    static const int short_max = 15;
    int sz;
    C* ptr; // ptr points to sz Cs
};
```

this declares the template
C is then used inside the template
declaration as if it was any other
type name

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img01.jpg)
