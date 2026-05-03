Initialization without constructors

3. Default initialization

It can be called with {}, and it initialize every member to {} (i.e., its default initialization)

DO NOT forget the {}

```cpp
void f()
{
    Work df_work {};
    std::cout << df_work.name << " " << df_work.number;
    // empty string "" and 0

    Work df_without_curly_braces;
    std::cout << df_without_curly_braces.number;
    // undefined value!
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)
