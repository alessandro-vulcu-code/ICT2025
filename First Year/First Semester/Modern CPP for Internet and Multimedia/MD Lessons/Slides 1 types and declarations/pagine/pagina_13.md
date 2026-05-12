Scope

• Different scopes:
  • Namespace
    Namespace member name if defined in namespace `but` outside functions, enum, classes, etc
    The scope extends from the point of declaration to the end of the namespace
  • Global
    Name defined in outside functions, enum, classes, namespaces
    The scope extends from the point of declaration to the end of the file, and can be accessed from other files by using external linkage
  • Statement scope
    Name defined in () part of `for`, `while`, `if`, `switch`
    The scope extends from point of declaration to } of the statement

```cpp
for(int index = 0; index < 10; ++index)
{
    Scope of index
    std::cout << index << std::endl;
}
// index does not exist here
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)
