make (binary program)

• The make utility will determine automatically which pieces of a large program need to be recompiled, and issue the commands to recompile them (man make)

• `make (re)compiles according to the makefile`
• `make check` (optional) performs the automatic test and aborts if they do not pass → used for unit testing
• `make install` installs executables and libraries inside path specified during the configuration (and inserted into the makefile form the configure)
• `make clean` removes all object files (*.o) and libraries
• `make distclean` removes all `makefiles`, object files (*.o), libraries, executable, hidden folders with dependencies, ...

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)
