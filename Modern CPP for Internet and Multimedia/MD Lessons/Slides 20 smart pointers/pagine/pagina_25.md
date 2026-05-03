Wrong use of smart pointers

```cpp
string* p = new string("ciao");
std::shared_ptr<string> sp(p); // count = 1
std::shared_ptr<string> sp2(p); // count = 1

• Who is responsible of deleting the object?

To avoid this problem follow this rule:

• An object should be assigned to a smart pointer as soon as it is created

std::shared_ptr<string> sp1 =
    std::make_shared<string>("ciao");
```

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)
