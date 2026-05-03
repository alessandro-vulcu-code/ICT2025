Derived classes

• It is possible to use Manager whenever an Employee is acceptable

```cpp
void f (Manager m1, Employee e1)
{
    std::vector<Employee*> vec {&m1, &e1};
}
```

• NOTE: Do not pass a Manager by value in e1 (slicing, see later)

• A Manager* is also an Employee*
• A Manager& is also an Employee&
• An Employee* is not a Manager*
(in case, an explicit conversion is needed)

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)
