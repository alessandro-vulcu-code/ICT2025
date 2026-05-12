# Threads in C++ - management

What happens if something (e.g., an exception, a `break` or a `return`) interrupts a function before a thread is joined?

• The thread object goes out of scope, its destructor is called and makes the program crash

• SOL1: for exceptions, after dispatching a thread, use a try-catch block and join in the catch (not that elegant)

• SOL2: Use resource acquisition is initialization (RAII)

```cpp
std::thread thr(incr,200);
try{ ... /* other stuff */ }
catch() {
    thr.join();
}
if(thr.joinable) {
    thr.join();
}
```

```cpp
class A { // RAII
    std::thread thr;
    void incr() {...}
public:
    A:thr(&A::incr,this,200) {}
    ~A() {thr.join();}
};
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)
