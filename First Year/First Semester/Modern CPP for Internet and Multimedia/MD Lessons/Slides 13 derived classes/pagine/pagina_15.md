Inheriting constructors

It is possible to inherit all the constructors of a base class, without the need to declare and define new ones

```java
class Y : public X {
    using X::X;
    // this inherits X constructors
    ...
}
```

The derived class may have additional data members, which would not be initialized in this case

• option 1: do not inherit the constructors
• option 2: in-class initializers for the additional members

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p15_img01.jpg)
