Now it compiles...

```cpp
// ONLY CPP FILES ARE COMPILED: NOT HEADERS!!
// THE COMPILER SEES a unique translation unit
// (basically, one per cpp file)

... //code of lines of iostream
inline int incr(int i) {
  return i+1;
}
inline int ex(int i) {
  return incr(i+1);
}

inline int ex2(int i) {
  return incr(i+2);
}
int main() {
  std::cout << ex(1) << ex2(2);
}
```

Example.h

Example2.h

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)
