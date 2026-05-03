Add a new library - 2

To compile a new library whose source is in the folder p_lib1/

• Add the subdirectory in Top-level Makefile.am:
  SUBDIRS = m4 \
  p_lib1 \
  .. → after last subdir DO NOT PLACE the escape "\"

• Create p_lib1/Makefile.am (Makefile.am for libraries)

• Optionally, (but good practice) create a test for the lib
  • A test is an executable to place into the test/ folder
  • It automatically tests the library functionalities
  • In the case the test fails, the installation is not performed
  • It is optionally compiled, if the installer is run with the −t 1 option
  • This option in the installer launches ./configure --with-test=1

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)
