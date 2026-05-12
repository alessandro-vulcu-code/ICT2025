HW buffer – heap allocation

Using a C-style array:

• `char* buffer = new char[3]; // remember the delete []!!`

• Better not to use C array with smart pointers, as you need to set a custom deleter for the shared pointer (we do not address it in this course), better using C++ std::array

Using a C++ std::array (best solution):

• `auto b1 = std::make_shared<std::array<char,3>>(); // b1→data()` provides direct access to its underlying C-style array

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)
