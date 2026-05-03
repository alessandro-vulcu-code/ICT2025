Threads in C++ – the task f – 4

@f is the task to be executed:
4. It can be a lambda function

```cpp
// f - as a lambda function
int main() {
  std::thread thr( [&]() {
    for (int i = 0; i < n_times; i++)
      a = a + 1;
  });
  ...
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p24_img01.jpg)
