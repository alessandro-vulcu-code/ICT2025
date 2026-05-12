Threads in C++ – the task f – 3 sol1

@f is the task to be executed:

3. It can be member function, requiring an additional pointer.
You should pass it by pointer

```c
struct A { // f as a function of an object
  int a;
  void incr (int n_times) {
    for (int i = 0; i < n_times; i++)
      a = a + 1;
  }; // end of struct A
int main() {
  A item = {0};
  std::thread thr(&A::incr, &item, 200);
  ...
}
```

It is the way to call a thread that executes `item->incr(200);`

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p21_img01.jpg)
