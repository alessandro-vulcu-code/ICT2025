Misuses of RTTI

This is the wrong approach

```cpp
void rotate(Shape* r) {
    if (dynamic_cast<Circle*>(r)) {
        // do nothing
    }
    else if (dynamic_cast<Triangle*>(r)) {
        // ... rotate triangle ...
    }
    else if (dynamic_cast<Square*>(r)) {
        // ... rotate square ...
    }
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
