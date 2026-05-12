Scope

• A name can be used only in specific parts of a program
• Fundamental for C++ resource management
• Different scopes:

• Local
  Declared in a function, valid from declaration to the end of the block

```c
f()
{
    Block: from { to }
    int a {10};
    std::cout << a << std::endl;
}
// a does not exist here

• Class
  Member name if defined in class `but` outside functions
  The scope extends to the class block (from { after the declaration to the end })
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
