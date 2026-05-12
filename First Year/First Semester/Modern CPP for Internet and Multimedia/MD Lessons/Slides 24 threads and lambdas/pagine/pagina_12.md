# Threads in C++

• Standard library provides the class `std::thread`
• A thread constructor takes a task to be executed (e.g., a function) and the arguments required by that task.
  • Number and types of arguments must match the task requirements
• `thread(Function&& f, Args&&... args);` where:
  • `@f` is the task to be executed
  • `@args` is the list of argument required for that task
• Throws `std::system_error` if the thread could not be started started (e.g., it happens if `pthread` not linked by the linker)

```cpp
void incr(int n_times) {
  for (int i = 0; i < n_times; i++)
    a = a + 1;
}
```

```cpp
int main() {
  std::thread thr(incr, 200);
  thr.join();
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
