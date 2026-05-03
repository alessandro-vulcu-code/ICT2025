Use of Lambas in Threads

```cpp
int main() {
    int a = 0;
    std::thread thr( [&a]() {
        a = a + 1;
    });
    ... // a = 1
}

int main() {
    int a = 0;
    std::thread thr( [](int v) {
        v = v + 1;
    }, a);
    ... // a = 0
}

int main() {
    int a = 0;
    std::thread thr( [a]() mutable {
        a = a + 1;
    });
    ... // a = 0
}

Question: in all these cases, which is the value of a after joining thr?
```

---

**Immagini estratte:**

![Figura estratta 1](images/p32_img01.jpg)
