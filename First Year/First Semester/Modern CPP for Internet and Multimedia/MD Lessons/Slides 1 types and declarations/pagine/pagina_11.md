Declarator operators

| Declarator Operators |
|-----------------------|
| prefix * pointer |
| prefix *const constant pointer |
| prefix *volatile volatile pointer |
| prefix & lvalue reference (§7.7.1) |
| prefix && rvalue reference (§7.7.2) |
| prefix auto function (using suffix return type) |
| postfix [] array |
| postfix () function |
| postfix -> returns from function |

Stroustrup, Bjarne. The C++ programming language. Pearson Education, 2013, page 154

• Prefix/postfix
  • Postfix operators bind tighter than prefix operators
    • char*universities[] //array of pointers to chars
    • char(*universities)[] //pointer to array of chars
  • In general, put a space where needed
    • char* universities[]

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)
