# Threads in C++ - info

Each thread has a unique id, of type `std::thread::id`

- `std::this_thread::get_id()` provides the id of the thread from which it is called
  ```cpp
  int main() {
    auto my_id = std::this_thread::get_id();
  }
  ```

- `thr1.get_id()` provides the id of thread tr1
  - It can be called only in joinable threads (not the detached ones)

```cpp
void print(int a){std::cout<<a;}
int main() {
  std::thread thr1(print,200); // console output
  std::cout << thr1.get_id(); 123782734251776
  thr1.detach();
  std::cout << thr1.get_id();
}
```

- `thread::id of a non-executing thread`
  ```cpp
```

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)
