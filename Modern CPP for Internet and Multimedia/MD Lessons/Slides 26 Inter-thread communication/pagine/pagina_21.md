Producer–final solution

```cpp
//..all include statements, i.e: queue, mutex, atomic, condition_variable
int main(){
    std::queue<int> q; std::mutex m_a;
    std::condition_variable cv;
    std::atomic<bool> exit_flag(false);
    //..code for the consumer tr1
    std::unique_lock <std::mutex> lk2(m_a); //1.
    q.push(17); //2.
    lk2.unlock(); //3.
    cv.notify_one(); //4.
    exit_flag.store(true); //5.
    cv.notify_all(); //6.
    tr1.join();
}
```

Steps in main thread (producer)
1. Lock the mutex
2. Produce the resource
3. Unlock the mutex
4. Notify a thread waiting with cv that the resource is ready
5. Set the exit flag to true
6. Notify all waiting thread with cv to exit

---

**Immagini estratte:**

![Figura estratta 1](images/p21_img01.jpg)
