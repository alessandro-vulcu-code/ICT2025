Preprocessor: always before compiler

• Evaluates the preprocessor directives, aka whatever is written after #, and substitutes them into the code. Agnostic to C++ syntax.

• E.g.: macros → use them as less as possible (here use constexpr!)

CPP FILE

```c
#define MAX_HGHT 720
#define AREA(a,b) (a*b)
int maxArea(int a)
{
    return
        AREA(a,MAX_HGHT);
}
int main(int argc,
          char* argv[])
{
    int l = MAX_HGHT;
    int a = maxArea(l);
}
```

PREPROCESSOR

TRANSLATION UNIT

```c
int maxArea(int a)
{
    return
        a*720;
}
int main(int argc,
          char* argv[])
{
    int l = 720;
    int a = maxArea(l);
}
```

---

**Immagini estratte:**

![Figura estratta 1](p05_img01.jpg)
