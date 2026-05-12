Constructors and destructors

```c
int main()
{
    Tracer tr{"a string"};
}
```

The output to the terminal is
a string
~ a string
i.e.,

1. The constructor is called to create `tr`, and the constructor body prints a string to the terminal
2. `tr` goes out of scope: the destructor is called, and its body prints ~ a string to the terminal

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)
