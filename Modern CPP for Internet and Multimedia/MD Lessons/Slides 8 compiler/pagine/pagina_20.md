Shared (or Dynamic) library

• Library created by the linker, it can depend on external libs,
  • In this case the linker trusts the fact it will be able to link them in run time
• Loaded at runtime during the code execution, once for all programs
• If one file is changed, only the library needs to be recompiled

Loader at RUNTIME
Dynamic linking

Objects
101 011
101 011
101 011

Linker
Shared Library lib1.so

Objects
101 011
101 011
101 011

Linker
Shared Library lib2.so

Objects
101 011
101 011
101 011

Linker
Executable

---

**Immagini estratte:**

![Figura estratta 1](images/p20_img01.jpg)

![Figura estratta 2](images/p20_img02.jpg)
