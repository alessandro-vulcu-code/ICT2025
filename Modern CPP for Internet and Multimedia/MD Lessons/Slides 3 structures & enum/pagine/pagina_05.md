# struct

• access to individual members can be done in different ways

```cpp
Address jd;
jd.name = "Jim Dandy";

void f(Address &addr)
{
    addr.name = "Jim Dandy";
}

void f(Address *addr)
{
    addr->name = "Jim Dandy";
    // or
    (*addr).name = "Jim Dandy";
}
```

• by default, members are public

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)
