Object lifetime

• The valid lifetime goes from the end of the constructor to the beginning of destructor
  • Automatic – from explicit initialization to out of scope
  • Static – until the program terminates
  • Free store – lifetime explicitly controlled with new and delete
  • thread_local objects – created within a thread and destroyed with it
  • Temporary objects – used in specific cases, generally automatic (destroyed at the end of the full expression using them)

```cpp
std::cout << std::string("tmp").size() << std::endl;
```

another example of rvalue

---

**Immagini estratte:**

![Figura estratta 1](images/p21_img01.jpg)
