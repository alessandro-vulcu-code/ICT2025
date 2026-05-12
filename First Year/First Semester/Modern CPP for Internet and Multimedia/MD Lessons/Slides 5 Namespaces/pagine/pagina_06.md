Access to namespace members

• Explicit qualification

```cpp
TextLibrary::Line line_object {};

// ::GlobalMemberName can be used to access
// members from the global namespace, which
// are otherwise shadowed by local variables

• using declarations

using std::string;

string a_string {"hello"};
// instead of std::string a_string
```

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)
