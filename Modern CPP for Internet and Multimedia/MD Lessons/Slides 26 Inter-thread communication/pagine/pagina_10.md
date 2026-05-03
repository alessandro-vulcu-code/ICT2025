# Mutex in C++11 – example

```cpp
#include <mutex> // std::mutex, std::unique_lock
int a = 0; std::mutex m_a;

void doIncr() {
    std::unique_lock<std::mutex> lk_a(m_a);
    a = a + 1;
} // here lk_a goes out of scope, and unlocks the mutex

void incr() {
    for (int i = 0; i < 100000; i++){
        doIncr();
        std::this_thread::sleep_for(
            std::chrono::microseconds(1));
    }
}

int main() {
    std::thread thr1(incr);
    std::thread thr2(incr);
    thr2.join();
    thr1.join();
    std::cout << a << std::endl;
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)
