# Initialization with constructors

If an ordinary constructor is defined

1. the default constructor **disappears**
2. the user-provided ordinary constructor **must** be used
3. the copy constructor still exists

```c
struct Work {
    std::string name;
    int number;
    Work(std::string a) : name{a} {number = name.length();}
};
```

Work some_work {}; // error
Work other_work {"long_thread"};
std::cout << other_work.name << " " << other_work.number;
```

---

**Immagini estratte:**

![Figura estratta 1](images/p17_img01.jpg)
