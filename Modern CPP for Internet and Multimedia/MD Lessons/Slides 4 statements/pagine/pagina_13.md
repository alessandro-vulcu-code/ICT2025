Range-for statements

• Loop and access to each element of a range
• They work with sequences or ranges – entities that
  • yield an iterator for the beginning and the end of the sequence
  • have a begin/end member pair
  • Examples: C++ arrays, std::vector<T>

```cpp
std::vector<int> v {1,2,3,4};
for (int value : v)
{
    std::cout << value << std::endl;
}
```

• Loops over values cannot modify the values
  • If the values needs to be modified, the loop variable needs to be a reference

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)
