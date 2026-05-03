Mutual exclusion – starvation

• Def: If several threads are blocked on a mutex, the system scheduler could in principle select the thread to be unblocked in such a way that some other unfortunate threads would never get to run. This is called starvation. Why? Because the CPU scheduler does not guarantee fairness.

• Sol: Acquire the mutex for the minimal amount of time (only for accessing critical regions), in order to avoid other threads waiting for the mutex release for no reasons

```c
#include <mutex>
std::mutex m_a;
void useMutex1() {
  while(true) {
    std::unique_lock<
      std::mutex> lk1(m_a);
    //do stuff
  }
}
```

int main() {
  std::thread thr1(useMutex1());
  while(true) {
    std::unique_lock<std::mutex>
      lk2(m_a);
    ...//do other stuff
  }
  ... //do other stuff2
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)
