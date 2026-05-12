# struct

• array: aggregate of elements of the same type
• struct: aggregate of elements with different types

## declaration and definition

```c
struct Address {
    const char* name;
    int number;
    const char* street;
    const char* town;
    char state[2];
    const char* zip;
};
```

## initialization

```c
Address jd = {
    "Jim Dandy",
    61,
    "South St",
    "New Providence",
    {'N','J'},
    "07974"
};
```

• two structs are different types even when they have the same members

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)
