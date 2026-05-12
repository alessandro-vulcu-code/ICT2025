Linker

• The linker produces the final compilation output from the object files the compiler produced. This output can be either a shared (or dynamic) library or an executable.

• It links all the object files by replacing the references to undefined symbols with the correct addresses.

• Each of these symbols can be defined in other object files or in libraries.

• If they are defined in libraries other than the standard library, you need to tell the linker about them.

• The most common errors are missing definitions (not exists or the file not provided to the linker) or duplicate definitions.

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)
