String literals

• Character sequence in double quotes
• Represented by `array of chars` terminated by ‘\0’
• Statically allocated (i.e., safe to return from function)

The type is constant (cannot change the value)

```cpp
const char stringExample[] = "Unipd";
std::cout << sizeof(stringExample) << std::endl; // $\textcircled{6}$
```

return the size of an expression or a data type, measured in number of bytes

5 chars + the termination ‘\0’

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)
