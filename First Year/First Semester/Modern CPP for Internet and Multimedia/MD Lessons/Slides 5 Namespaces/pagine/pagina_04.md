Need for modularity

• Consider two libraries

```cpp
// a library for shapes
class Shape { /* ... */ };
class Line : public Shape { /* ... */ };
class Poly_line: public Shape { /* ... */ };
class Text : public Shape { /* ... */ };

// a library for text
class Glyph { /* ... */ };
class Word { /* ... */ };
class Line { /* ... */ };
class Text { /* ... */ };
```

• If a program uses both of them, it will not compile, because Line and Text have multiple declarations

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)
