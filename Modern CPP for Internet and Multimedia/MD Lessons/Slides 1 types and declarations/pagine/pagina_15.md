Hiding or shadowing

• Names can be redefined in nested blocks: minimize or avoid it!

```cpp
int index = 10; // global x

void f()
{
    char index = 'a'; // local index 1
    std::cout << index << std::endl;
    for(int index = 0; index < 10; ++index)
    {
        // statement index
        std::cout << index << std::endl;
    }

    {
        double index = 0.2; // local index 2 hides 1
        std::cout << index << std::endl;
    }
    index = 'b'; // assign to local index 1
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)
