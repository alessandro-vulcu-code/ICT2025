Makefile.am

• It is a programmer-defined file to generate Makefile.in
• It is written with automake sintax
  • I `a A a U U d b T c U A a T C U U C`
  • N `w e T C` N `a b A a d b A a d b U C e T a U A e T C` `A U U A e T U A e` `configure.ac`

In a project with recursive structure, there are different Makefiles:

• Top-level Makefile.am
  • It tells Automake which subdirs are to be built.

• Lower-level Makefile.am
  • It contains the rules on how to build a library or an executable
  • The Makefile.am inside the m4, instead, contains the external dependencies (dependencies from external packages, if any)

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p20_img01.jpg)
