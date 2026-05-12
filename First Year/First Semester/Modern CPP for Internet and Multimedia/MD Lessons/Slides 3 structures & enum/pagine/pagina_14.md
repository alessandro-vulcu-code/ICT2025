Plain enum

• The enumerators of a plain enum are not scoped and can be converted to int
• In general, prefer enum classes, which provide a better defined behavior

```cpp
enum TrafficLight {green, yellow, red};
TrafficLight a = TrafficLight::red;
int a2 = a; // ok!
bool a3 {a == 2}; // ok!

enum Other char {green, blue}; // error
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)
