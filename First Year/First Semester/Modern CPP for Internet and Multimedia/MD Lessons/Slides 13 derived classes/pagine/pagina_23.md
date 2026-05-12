Polymorphism

Virtual enables runtime polymorphism

• use different implementations of a virtual function according to the actual object on which they are called
• the objects need to be manipulated with pointers or references
• for direct manipulation, the type is already known, there is no space left for polymorphism

```cpp
void f (std::vector<Employee*> vec)
{
    for (Employee* elem : vec)
    {
        elem->print();
    }
}
```

the compiler will automatically select the correct print() function for each of the elements in the vector

---

**Immagini estratte:**

![Figura estratta 1](p23_img01.jpg)
