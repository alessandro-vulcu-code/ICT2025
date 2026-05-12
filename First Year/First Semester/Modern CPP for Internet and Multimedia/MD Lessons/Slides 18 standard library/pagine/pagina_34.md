File streams

• File streams open, read, write and close files
• Defined in the `<fstream>` header
  • ifstream to read a file
  • ofstream to write to a file
  • fstream to do both
• Open a file

```cpp
#include <fstream>
string filename = "test.txt";
// open the file, multiple options available
// (e.g., append, replace, etc)
std::ofstream fout(filename.c_str());
if (!fout) // check if opened correctly
{
    std::cout << "error: open file for output failed!"
            << std::endl;
    exit(127);
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p34_img01.jpg)
