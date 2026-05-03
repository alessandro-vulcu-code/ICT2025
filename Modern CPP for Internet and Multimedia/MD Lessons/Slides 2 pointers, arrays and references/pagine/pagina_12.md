Pointers and arrays

```c
const int size = 4;
int v[size] = {1,2,3,4};

for(int * p1 = v; p1 < v + size; ++p1)
{
    std::cout << *p1 << std::endl;
}

// equivalent to

for(int index = 0; index < size; ++index)
{
    std::cout << v[index] << std::endl;
}

const char* strLit = "unipd";

for(; (*strLit ≠ '\0'); ++strLit)
{
    std::cout << *strLit << std::endl;
}
```

• The arrays **do not** carry implicit information on their **size**!
• When passing a pointer to an array to a function (this is the only possible way), one needs to carry along the info on the size

With string literals, it is possible to use this condition without info on the size

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
