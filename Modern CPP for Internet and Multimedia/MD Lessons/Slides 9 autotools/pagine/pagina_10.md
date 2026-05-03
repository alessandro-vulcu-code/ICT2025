aclocal (perl script)

aclocal generates ‘aclocal.m4’ by scanning ‘configure.ac’
aclocal.m4 contains:

• all the user-defined macros (from the configure.ac);
• all required Automake macros, included with the m4_include statement
  e.g.: m4_include(m4/libtool.m4)
• aclocal.m4 contains all the macros that will be used by automake
• Writing it manually (as in the early days) it is a very advanced operations: aclocal does if for you.

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)
