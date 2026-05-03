Derived class example

```csharp
struct Employee { // this is used as base class
    // it must be declared
    string first_name, family_name;
    char middle_initial;
    Date hiring_date;
    short department;
}

this expresses subclassing

struct Manager : public Employee {
    list<Employee*> group;
    short level;
}

Manager has the same members of Employee
+ its own members!
```

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)
