Wrapping it up: 2 - Compiler

```cpp
//translation unit
//of my-fun.cpp
int incr(int i);

int incr(int i)
{
    return i+1;
}

compilation
my-fun.o

//translation unit
//of example.cpp
int incr(int i);
inline int ex(int i){
    return incr(i+1);
}
int main() {
    int i = ex(1) + ex(2);
}

compilation
example.o
101
011
17
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)

![Figura estratta 2](p17_img02.jpg)
