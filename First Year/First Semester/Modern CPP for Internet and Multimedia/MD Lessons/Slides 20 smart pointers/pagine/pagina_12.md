Unique pointer – who owns it?

• `std::unique_ptr<string> up2 = up; // not allowed!!`

• `std::unique_ptr<string> up2 = std::move(up); // up releases its ownership of its raw pointer, and gives it to up2`

```cpp
void function f1(std::unique_ptr<T1> up) {
    //do stuff
}

std::unique_ptr<T1> up1 (new T1 ());
f1(up1); // not allowed!!

f1(std::move(up1)); // IT WORKS, BUT BE AWARE THE OBJECT IS DESTROYED INSIDE THE FUNCTION f1!!!
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
