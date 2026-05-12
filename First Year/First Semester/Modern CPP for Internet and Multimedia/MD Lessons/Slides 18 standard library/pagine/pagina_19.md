Iterators

```cpp
std::vector<int> vec {1,2,3,4};
std::vector<int>::iterator vec_iter = vec.begin();
std::vector<int>::iterator vec_end = vec.end();

while(vec_iter ≠ vec_end)
{
    // this increases the value in the vector,
    // e.g, 1++ → 2
    ++(*vec_iter);
    // this increases the value of the iterator,
    // i.e., the entry to which the iterator points
    ++vec_iter;
}
```

There is also a const_iterator for read-only operations

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p19_img01.jpg)
