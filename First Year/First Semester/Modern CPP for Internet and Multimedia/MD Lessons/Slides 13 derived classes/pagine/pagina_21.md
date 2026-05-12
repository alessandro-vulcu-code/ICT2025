Navigating class hierarchies - virtual

```c
struct Employee {
    virtual void print() const;
}

void f (std::vector<Employee*> vec)
{
    for (Employee* elem : vec)
    {
        elem->print();
    }
}
```

Employee* can point to Employee or Manager

here we want to use a different print() for an actual Employee or an actual Manager (there are more members to be printed with a Manager)

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p21_img01.jpg)
