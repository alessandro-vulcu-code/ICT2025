Mutex in C++11

• In C++, to acquire a mutex you have to lock it
• And always remember to unlock (i.e., release) it!

```c
std::mutex m_a;
void useMutex() {
    m_a.lock();
    //do stuff
    m_a.unlock();
}
```

• If you forget to unlock the mutex, no one else can acquire (lock) it, causing starvation
• If the functions is interrupted (e.g., with a return) before the unlock, we have a problem!
• C++11 provides two RAII classes, lock_guard and unique_lock, to handle such problem:

• Both lock_guard and unique_lock, unlock the mutex when they go out of scope (RAII: i.e., their constructor locks the mutex, and their destructor unlocks it).

• lock_guard is lighter, but we mostly use unique_lock because it provides more functionalities
• We will see them next..

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)
