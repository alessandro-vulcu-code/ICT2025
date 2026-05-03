Threads in C++ – the task f – 2

@f is the task to be executed:

2. It can be member function, requiring an additional pointer to this

```c
struct A { // f as a function of an object
  int a;
  void incr (int n_times) {
    for (int i = 0; i < n_times; i++)
      a = a + 1;
  }
  void dolncr() {
    std::thread tr(&A::incr, this, 200);
    ...
  }
};
```

It is the way to call a thread that executes `this->incr(200);`

---

**Immagini estratte:**

![Figura estratta 1](images/p19_img01.jpg)
