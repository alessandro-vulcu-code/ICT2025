Member initialization

• Member initializers are more efficient:

```cpp
Person::Person(std::string& n, std::string& a) :
name{n}
{
    address = a;
}
```

Given the rules from the previous slides:

• address is first initialized to an empty string (it is not specified in the member initializer list, but it must be initialized before the body executes)
• a is then assigned to address

The member initializer list would have just initialized address with a

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)
