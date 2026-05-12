Navigating class hierarchies - virtual

```c
struct Employee {
    virtual void print() const;
    ...
}

void Employee::print() const
{
    std::cout << family_name << std::endl;
}

struct Manager : public Employee {
    void print() const;
    ...
}

void Manager::print() const
{
    Employee::print();
    std::cout << level << std::endl;
}
```

Manager overrides the virtual print() method of Employee

• The call to the print() of the base is needed if the derived has no access to the base private members

• The :: qualifier ensures that the print() from Employee is called – otherwise, infinite recursion

---

**Immagini estratte:**

![Figura estratta 1](p22_img01.jpg)
