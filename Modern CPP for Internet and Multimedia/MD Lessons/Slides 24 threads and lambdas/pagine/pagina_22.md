Threads in C++ – the task f – 3 sol2

@f is the task to be executed:

3. It can be member function, requiring an additional pointer.
You can pass it by shared pointer

```c
struct A { // f as a function of an object
  int a;
  void incr (int n_times) {
    for (int i = 0; i < n_times; i++)
      a = a + 1;
  }; // end of struct A
int main() {
  shared_ptr<A> item = make_shared<A>(0);
  std::thread thr(&A::incr, item, 200);
  ...
}
```

It is the way to call a thread that executes `item->incr(200);`

---

**Immagini estratte:**

![Figura estratta 1](images/p22_img01.jpg)
