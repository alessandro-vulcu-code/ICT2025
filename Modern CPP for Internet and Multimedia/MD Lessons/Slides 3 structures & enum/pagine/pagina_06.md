struct layout

• members are saved in memory in the order they are declared

```c
struct Example {
    char first_member;
    int second_member;
    char third_member
};
```

The size is `at least 6 (1+4+1)`, because some architectures some types must be aligned to certain boundaries

```c
1
2
3
12
```

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)
