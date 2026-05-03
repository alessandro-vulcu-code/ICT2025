Unique pointer – pass it to a function

Sol1: move it to the argument of the function, and return it.

• Returning a unique pointer by value means moving it, i.e., returning it with move()

```cpp
std::unique_ptr<T1> f1(
    std::unique_ptr<T1> up) {
    //do stuff with up
    return up; // returns it by move
}

std::unique_ptr<T1> up1(new T1());
up1 = f1(std::move(up1));
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)
