Member initialization

• When an object is constructed, its members need to be initialized
• It is possible to use a member initializer list in the definition of a constructor

```cpp
ClassName::ClassName(T1 arg1, T2 arg2) :
    member1{arg1},
    member2{arg2}
{
    // body
    the constructors of the members
    • are called before the body is executed
    • are called in the order of declaration in the class definition (better to use the same order in the member initializer list)
    • if a member does not need arguments for initialization, it can be omitted – but it is better to comment why
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p24_img01.jpg)
