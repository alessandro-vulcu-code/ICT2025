Initialization without constructors

2. Copy initialization (member-wise copy)

```cpp
Work other_work {some_work};
std::cout << other_work.name << " " << other_work.number;
```

3. Default initialization

It can be called with {}, and it initialize every member to {} (i.e., its default initialization)

```cpp
Work df_work {};
std::cout << df_work.name << " " << df_work.number;
// empty string "” and 0
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)
