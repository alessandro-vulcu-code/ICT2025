Memory Model

• Operations on an object in memory are never directly performed on the object in memory.
• The object is **loaded** into a processor register, **modified** there, and then **written back**.
• What happens if 2 threads try to modify the same object simultaneously?

```cpp
int a = 0;
void incr() {
    a = a + 1;
}
main() {
    incr();
}
```

Time evolution of the CPU Registers
T1: R1 = 0 # load a
T2: R1 = 0+1 modify
T3: a = R1 write back

Time evolution of the value of a
T1: a = 0
T2: a = 0
T3: a = 1

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)
