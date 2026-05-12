Replication issue

A class can inherit from multiple bases
• Public inheritance to inherit the interface
• Private/protected inheritance to inherit implementation details

There may be a replication issue

```java
class A : public B, public C { ... };
class B : public D { ... };
class C : public D { ... };
class D { ... };

A has two objects of type D
• if D is not an abstract class and has data, A may have repeated members
```

---

**Immagini estratte:**

![Figura estratta 1](images/p33_img01.jpg)
