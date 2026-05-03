Race condition

```cpp
int a = 0;
void incr() {
  for (int i = 0; i < 100000; i++){
    a = a + 1;
    std::this_thread::sleep_for(
      std::chrono::microseconds(1));
  }
}

int main() {
  std::thread thr1(incr);
  std::thread thr2(incr);
  thr2.join();
  thr1.join();
  std::cout << a;
}
```

• Two threads modify the same variable in the same moment, so sometimes it happens that one thread reads the “old” value of `a`
• This is a race condition

| Time | a | thr1 | thr2 |
| :--- | :--- | :--- | :--- |
| T1 | a=10 | R1=a=10 | // |
| T2 | a=10 | R1=10+1 | R2=a=10 |
| T3 | a=11 | a=R1=11 | R2=10+1 |
| T4 | a=11 | // | a=R2=11 |

• If you run this code several times, the value of a might change
• Def: a race condition is anything where the outcome of a program depends on the relative ordering of execution of operations on two or more threads.

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img01.jpg)
