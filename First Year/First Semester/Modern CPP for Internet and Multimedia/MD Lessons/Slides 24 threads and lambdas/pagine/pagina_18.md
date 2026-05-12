Threads in C++ – the task f – 1

@f is the task to be executed:

1. It can be a function

```cpp
// f as a function
int a = 0;
void incr(int n_times) {
    for (int i = 0; i < n_times; i++)
        a = a + 1;
}
int main() {
    std::thread thr(incr, 200);
    ...
}
```

---

**Immagini estratte:**

![Figura estratta 1](p18_img01.jpg)
