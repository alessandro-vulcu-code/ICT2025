In-class initializers

• Classes can have many constructors, accepting different arguments
• It can be useful to have `default` values for the data members
• A constructor can then modify them if needed

```cpp
class Date {
  int d {22};
  int m {02};          in-class initialization
  int y {1992};
public:
  Date(int, int, int); // day, month, year
  Date(int, int); // day, month, year is default
  Date(int); // day, month and year are default
  Date(); // default date, 22/02/1992
  Date(const char*); // date in string representation
  ...
}
```

---

**Immagini estratte:**

![Figura estratta 1](p18_img01.jpg)
