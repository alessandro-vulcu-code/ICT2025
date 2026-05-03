Access control for base classes

A base class can be

• public – the derivation creates a subtype for example X is a kind of B, and they can be used for runtime polymorphism

```python
class X : public B { ... }
```

• private – the derivation restricts the interface to that of a base and changes some details only the derived class is aware that is inheriting from the base, so the base B cannot be further derived through the already derived class Y

```python
class Y : private B { ... }
```

---

**Immagini estratte:**

![Figura estratta 1](images/p31_img01.jpg)
