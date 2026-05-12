Default arguments

• Sometimes it is useful to have default values for some arguments
• They can be provided for trailing arguments only

```cpp
int f(int a, int b=0, char* c=nullptr); // OK
int g(int =0, int =0, char*); // error
int h(int =0, int, char* =nullptr); // error
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p21_img01.jpg)
