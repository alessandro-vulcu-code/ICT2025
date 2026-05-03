Threads in C++ – function parameters

• The parameters of a function executed in a thread are always passed by `value!` DO NOT TRY TO PASS ANYTHING BY REFERENCE, IT JUST DOESN’T WORK
  • if you do so, it passes it by value or crashes, depending on the implementation
  • If you really need to pass something by reference, you can enforce it by using the wrapper `std::ref(v)`. → be aware that it’s dangerous, as both main thread and thr1 share the same memory.
  → You can pass it by (smart) pointer, just be aware you are sharing the memory

```cpp
void incr(int& v) {
  ++v;
}
int main() {
  int v = 1;
  std::thread thr(incr, std::ref(v));
  ...
  thr.join(); // here v = 2
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)
