Mutual exclusion – mutex – deadlock

• Always remember to release the mutex to avoid deadlock (that is a type of starvation)

• Def: deadlock = when one thread waits for a mutex that is never released (from another thread or from itself).

```cpp
#include <mutex>
std::mutex m_a;

void useMutex1() {
  std::unique_lock<std::mutex> lk(m_a);
  //do stuff
}

void useMutex2() {
  std::unique_lock<std::mutex> lk(m_a);
  //do stuff
  useMutex1();//it tries to lock again the same mutex
  → deadlock
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
