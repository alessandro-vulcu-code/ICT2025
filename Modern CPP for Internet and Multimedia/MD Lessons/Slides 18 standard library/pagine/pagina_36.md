String streams

• The `<sstream>` header defines streams to and from a string
  • istringstream to read from a std::string
  • ostringstream to write to a std::string
  • stringstream to do both

• They can be used to create strings – for example, when looping

```cpp
std::stringstream ss {};
std::vector< std::string > studentNames {“john”, “jane”};
for(auto student : studentNames)
{
    ss << student << ",";
}
// create a std::string and output to terminal
std::cout << ss.str() << std::endl;
```

• C++ has also the operator+ for strings, but it is not as efficient as a stream

---

**Immagini estratte:**

![Figura estratta 1](images/p36_img01.jpg)
