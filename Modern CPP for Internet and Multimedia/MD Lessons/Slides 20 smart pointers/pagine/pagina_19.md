Shared pointer Cast

• Dynamic cast: std::dynamic_pointer_cast<D>(s_ptr)
• Static cast: std::static_pointer_cast<D>(s_ptr)
• Const cast: std::const_pointer_cast<const D>(s_ptr)

E.g., D derives from B.

```cpp
std::shared_ptr<B> pb = std::make_shared<D>();
std::shared_ptr<D> pd1 =
std::dynamic_pointer_cast<D>(pb);
if(pd1 ≠ nullptr) {...}
std::shared_ptr<D> pd2 =
std::static_pointer_cast<D>(pb);
std::shared_ptr<const D> c_pd =
std::const_pointer_cast<const D>(pb);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p19_img01.jpg)
