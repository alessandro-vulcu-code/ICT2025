Unique pointer – pass it to a function - 2

Sol2: pass it by const ref

```cpp
void f2(
    const std::unique_ptr<T1>& up) {
    //do stuff with up
}

std::unique_ptr<T1> up1(new T1());
f2(up1);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)
