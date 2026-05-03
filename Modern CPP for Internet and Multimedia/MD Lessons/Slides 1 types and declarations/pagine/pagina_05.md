Fundamental Types

• **Character** (e.g., char)
  • Different types are available (char, signed char, unsigned char, wchar_t)
  • **Almost** always char has 8 bit
  • 7 bit are enough to represent ASCII
  • signed vs unsigned char:
    • A char may be represented either as signed or unsigned
    • Implementation-defined behavior (Windows vs Linux, 32 vs 64 bit, arm vs x86)
  • Character literals
    • Single character in **single** quotes (e.g., ‘a’, ‘0’) of type char
    • Special characters represented with ‘\’ (the escape character) + letter (e.g., ‘\n’)
    • The ASCII number associated to a literal can also be represented on **hexadecimal** base – using the ‘\x’ + number
  • char c1 = ‘a’;
  • char c2 = ‘\x61’; char c3 = 97;
  • std::cout << c1 << std::endl; // print a
  • std::cout << c2 << std::endl; // print a
  • std::cout << c3 << std::endl; // print a

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)
