# Threads in C++ - join and detach

A dispatched thread must be either joined or detached

• Otherwise, the program crashes after the thread object goes out of scope: its destructor throws an exception
• You cannot join a detached thread (or you get `std::system_error`)
• To `join` a thread means to wait for the end of its execution

```cpp
int a = 0;
int main() {
    std::thread thr(incr, 200);
    ... // other stuff
    thr.join(); //main is blocked here until end of incr
}
```

```cpp
void incr(int n_times) {
    for (int i = 0; i < n_times; i++)
        a = a + 1;
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)
