Replication issue – virtual base

• The replication issue can be solved by declaring a base class virtual

```java
class A : public B, public C { ... };
class B : public virtual D { ... };
class C : public virtual D { ... };
class D { ... };
```

---

**Immagini estratte:**

![Figura estratta 1](images/p34_img01.jpg)
