Producer – close to the solution

Steps in main thread (producer)
1. Lock the mutex
2. Produce the resource (thus the pred of the cond. variable becomes true)
3. Unlock the mutex
4. Notify a thread waiting with the cond. variable that the resource is ready

```c
#include <condition_variable>
#include <mutex> //...all other includes (queue)
int main(){
    std::queue<int> q; std::mutex m_a;
    std::condition_variable cv;
    ... // consumer code

    std::unique_lock< std::mutex> lk2(m_a); //1.
    q.push(17); //2.
    lk2.unlock(); //3.
    cv.notify_one(); //4.
    tr1.join();}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)
