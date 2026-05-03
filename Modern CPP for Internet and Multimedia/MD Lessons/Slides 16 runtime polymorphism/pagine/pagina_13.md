Correct approach

It is better to use a virtual method in the base and override it

```java
class Shape {
public:
    virtual void
rotate() = 0;
    // ...
}

class Circle : public
Shape{
public:
    void rotate();
    // ...
}

class Triangle : public
Shape{
public:
    void rotate();
    // ...
}

class Square : public
Shape{
public:
    void rotate();
    // ...
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)
