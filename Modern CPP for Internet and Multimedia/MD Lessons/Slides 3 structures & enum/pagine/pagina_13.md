Operators on enum class

• Enumerators are useful to provide a human-understandable semantic
• It is possible to specify the values – for example to make them work with bitfield operations!

```cpp
enum class Printer_flags { acknowledge=1, paper_empty=2,
    busy=4, out_of_black=8, out_of_color=16};
```

• Operators can then be (re)defined to work with enumerators

```cpp
constexpr Printer_flags operator|(
    Printer_flags a, Printer_flags b) {
    return static_cast<Printer_flags>(
        static_cast<int>(a)|static_cast<int>(b));
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)
