C++ strings

There are some specializations of the basic_string template already available

• using std::string = std::basic_string<char>
• using std::wstring = std::basic_string<wchar>

There are multiple constructors, the most useful are

```cpp
std::string empty {}; // default
std::string c_style {"this is a C-style string"};
std::string another {c_style}; // copy
```

---

**Immagini estratte:**

![Figura estratta 1](images/p30_img01.jpg)
