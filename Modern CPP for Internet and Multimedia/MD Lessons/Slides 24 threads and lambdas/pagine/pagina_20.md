Threads in C++ – the task f – 3 wrong

@f is the task to be executed:

3. It can be member function, requiring an additional pointer.
Passing it by value is not a good idea

```c
struct A { // f as a function of an object
  int a;
  void incr (int n_times) {
    for (int i = 0; i < n_times; i++)
      a = a + 1;
  }; // end of struct A
int main() {
  A item = {0};
  std::thread thr(&A::incr, item, 200);
  ...
}
```

It is the way to call a thread that executes the incr function to a copy of the object item!!

A item1{item};
item1.incr(200);

---

**Immagini estratte:**

![Figura estratta 1](images/p20_img01.jpg)
