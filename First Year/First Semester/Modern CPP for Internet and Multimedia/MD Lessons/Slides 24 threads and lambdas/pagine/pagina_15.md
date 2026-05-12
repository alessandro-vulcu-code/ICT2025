Threads in C++ - join and detach – 2

• To detach a thread means to let it running independently by the main thread.
  • The variable `thr` does not handle that thread anymore.
  • Used to initiate a thread to complete a task and forget about it.
  • A detached thread that live forever (or decide itself when to terminate) is called daemon.
  • Really dangerous, in general do not use it.

```cpp
int main() {
  std::thread thr(incr,200);
  thr.detach();//main terminates and forgets about thr,
} //that terminates after the program is over!!!
```

• You cannot join a detached thread, or the program crashes → you can check it with the `joinable()` method

```cpp
if(thr.joinable()) { thr.join(); }
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p15_img01.jpg)
