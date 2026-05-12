<!-- Pagina 1 -->

Autotools – quick how-to

Programming for Telecommunications
Filippo Campagnaro
campagn1@dei.unipd.it

---

**Immagini estratte:**

![Figura estratta 1](images/p01_img01.jpg)

![Figura estratta 2](images/p01_img04.jpg)

![Figura estratta 3](images/p01_img03.jpg)

![Figura estratta 4](images/p01_img02.jpg)


---

<!-- Pagina 2 -->

Outline

1. Makefile.am
2. Compile an executable
3. Compile a library

John Calcote, “AUTOTOOLS: A Practitioner's Guide to GNU Autoconf, Automake, and Libtool”, No Starch Press, 1° edition, 2010

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Makefile.am

• It is written with automake sintax
  • \ is the escape character
  • @<var>@ to use whatever variable <var> defined in configure.ac

• Top-level Makefile.am
  • It tells Automake which subdirs are to be built.

• Lower-level Makefile.am
  • It contains the rules on how to build a library or an executable

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

Top-level Makefile.am

AUTOMAKE_OPTIONS = foreign # it tells automake that the project will not follow GNU standards. Use it always, otherwise you need to deal with several txt files of the gnu standard, such as ChangeLog, README, NEWS, etc.

SUBDIRS = m4 \
basic_utilities \
example

it tells Automake which subdirectories are to be built, specifically: m4 and basic_utilities and example. “\” tells to escape the new line.

if WITH_TEST # if WITH_TEST is enabled,
SUBDIRS += \
test/bu_test # it adds test/bu_test folder to SUBDIR and
TESTS = \
test/bu_test/bu_test# it executes test/bu_test/bu_test when testing endif

ACLOCAL_AMFLAGS = -I m4 # it tells Autotools to store libtool configuration macros in the m4 folder

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)


---

<!-- Pagina 5 -->

Add a new executable

To compile a new executable whose source is in example/ex1/:

• Add in `configure.ac`:
  • Add your path to the preprocessor FLAG: `PFICT_CPPFLAGS="$PFICT_CPPFLAGS "-I$(top_srcdir)/examples/ex1"`
  • Add its Makefile.in to the list of the makefile to parse `AC_CONFIG_FILES([
    Makefile
    m4/Makefile
    example/ex1
    ...
  ])`

• Add the subdirectory in Top-level `Makefile.am`:
  `SUBDIRS = m4 \
    example/ex1 \
    .. -> after last subdir DO NOT PLACE the escape "\"`

• Create `example/ex1/Makefile.am` (Makefile.am for executables)

---

**Immagini estratte:**

![Figura estratta 1](p05_img01.jpg)


---

<!-- Pagina 6 -->

Makefile.am for executable

AM_CXXFLAGS = @PFICT_CXXFLAGS@ # sets which Automake CXX flag to use in this makefile. PFICT_CXXFLAGS is defined in configure.ac

bin_PROGRAMS = fun_example # gives the name fun_example to the executable

fun_example_SOURCES = fun-example.cpp class1.cpp # tells which are the source files for the executable

fun_example_CPPFLAGS = @PFICT_CPPFLAGS@ # sets the CPP flags of this executable equal to PFICT_CPPFLAGS, defined in configure.ac

fun_example_LDFLAGS = @PFICT_LDFLAGS@ # tells to the linker to search for libraries into the folders indicated into PFICT_LDFLAGS defined in configure.ac

fun_example_LDADD = @PFICT_LDADD@ # tells to the linker to link against the libraries named as defined in PFICT_LDADD inside the configure.ac. In the case the executable depends only on one library LIB1, link against it (@LIB1_LDADD@)

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)


---

<!-- Pagina 7 -->

Add a new library

To compile a new library whose source is in the folder p_lib1/

• Add in configure.ac:
  • Add the lib path to the preprocessor search path FLAG (-I):
    PFICT_CPPFLAGS="$PFICT_CPPFLAGS "-I$(top_srcdir)/p_lib1"
  • Add the lib path to the linker search path FLAG (-L):
    PFICT_LDFLAGS="$PFICT_LDFLAGS "-L$(top_srcdir)/p_lib1"
  • Create a new linker library (-I) macro, specific for this lib
    P_LIB1_LDADD="$P_LIB1_LDADD "-lp_lib1"
  • Add the new linker macro to the global project macre
    PFICT_LDADD="$PFICT_LDADD $P_LIB1_LDADD"
  • Add its Makefile.in to the list of the makefile to parse
    AC_CONFIG_FILES([
      Makefile
      m4/Makefile
      lib_p
      ...
    ])

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)


---

<!-- Pagina 8 -->

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

![Figura estratta 1](p08_img01.jpg)


---

<!-- Pagina 9 -->

Makefile.am for library

AM_CXXFLAGS = @PFICT_CXXFLAGS@ # like in executable

lib_LTLIBRARIES = libb_util.la # calls the library libb_util

libb_util_la_SOURCES = b-utils.cpp # uses this source file

libb_util_la_CPPFLAGS = @PFICT_CPPFLAGS@ #like in executable

libb_util_la_LDFLAGS = @PFICT_LDFLAGS@ # like in executable

libb_util_la_LIBADD = @PFICT_LIBADD@ # specifies that additional libraries (defined in PFICT_LIBADD defined in configure.ac) are needed to be linked.

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Add the test p_lib1_test

A test is an executable whose source is in test/p_lib1_test/:

• configure.ac: same as executable (replacing with the right path)

• In Top-level Makefile.am: add path and test inside the “if WITH_TEST” statement:

```bash
if WITH_TEST
  SUBDIRS += m4 \
    test/p_lib1_test \
    ...
  TEST = \
    test/p_lib1_test/p_lib1_test_program
```

• Create example/ex1/Makefile.am (Makefile.am for executables)

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)
