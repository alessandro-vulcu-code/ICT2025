lvalues and rvalues

| | Has identity | Is movable |
| :--- | :--- | :--- |
| lvalue | Yes | No |
| rvalue | X (it depends) | Yes |

• rvalues are **movable** and may or may not have identity
• For example: temporary values returned by functions

```cpp
std::vector<int> vec1 {1, 2, 3};
auto vec2 = someFunction(vec1);
lvalue rvalue
auto vec3 = vec1;
lvalue
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p20_img01.jpg)
