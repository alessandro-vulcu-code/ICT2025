<!-- Pagina 1 -->

Autotools

Modern C++ Programming for ICT
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

1. What’s going on when I use installer.sh?
2. Libtool
3. Autoconf
4. Automake
5. configure.ac
6. Makefile.am

John Calcote, “AUTOTOOLS: A Practitioner's Guide to GNU Autoconf, Automake, and Libtool”, No Starch Press, 1° edition, 2010

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

GNU Autotools

Autotools is a suite of programming tools designed to assist in making source code packages portable to many Unix-like systems. It is composed by:

• GNU Autoconf, used to generate the configure script for the project
• GNU Automake, used to simplify the process of creating consistent and functional makefiles
• GNU Libtool, that provides an abstraction to the portable creation of libraries

• A makefile contains a list of rules (written as shell commands for that specific processor) that will be applied by the make utility

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

What’s inside the git repo?

```bash
$ls -l
example
test
basic_utilities
m4

installer.sh

autogen.sh

configure.ac

Makefile.am
```

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img01.jpg)


---

<!-- Pagina 5 -->

What’s inside the repo?

```text
example
test
basic_utilities
m4
→ Folders

installer.sh → Installation script

autogen.sh → Automatic file generation

configure.ac → Source code of configure,
written with M4 macros

Makefile.am → makefile with additional
Automake syntax

• A makefile contains a list of rules (written as shell commands for that
specific processor) that will be applied by the make utility
```

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)


---

<!-- Pagina 6 -->

Run the installer.sh (shell script)

```shell
./installer.sh -p <path> -t <flag>
```

Option to set the `<path>` where the program will be installed

Option to set the `<flag>` to enable/disable the test (0 disable, 1 enable)

```shell
./installer.sh -h → Option to print the help string
```

OPTIONS:
- `-h` Show this message
- `-p` Prefix Path
- `-t` Test enable (1) or disable (0, default)
- `-c` clean repository

e.g. `/installer.sh -p <your_home> -t 1`
```

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)


---

<!-- Pagina 7 -->

installer.sh (shell script)

... # various lines for input parameters (i.e., options) checking
./autogen.sh
./configure --prefix $PREFIX
make

Path where the program will be installed, previously passed with “-p”

If test is activated (previously passed with “-t”), perform the make check operation

• `autogen.sh` prepares the environment, creating configure and Makefile.in scripts (and various wrappers for whatever missing)
• `configure` creates makefiles from Makefile.in
• `make` compiles the source code according to the makefiles
• `make check` performs the automatic test and aborts if they do not pass
• `make install` installs executables and libraries inside $PREFIX/lib and $PREFIX/build

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)


---

<!-- Pagina 8 -->

autogen.sh (shell script)

Unix Name
OS with XNU kernel (es, macOS)

Libtool for XNU (macOS)
case `uname` in Darwin*)
glibtoolize ;;
*) libtoolize ;;
esac
aclocal
autoconf
automake --add-missing

• (g)libtoolize prepares a package to use libtool
• package=collection of executables and libraries designed to perform a specific task and placed together (e.g., in an archive)

• aclocal generates ‘aclocal.m4’ macros by scanning ‘configure.ac’
• autoconf generates configuration script from configure.ac
• automake generates Makefile.in for configure from Makefile.am

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)


---

<!-- Pagina 9 -->

(g)libtoilize (shell script)

(g)libtoolize prepares the package to use libtool

• libtool is the GNU portable library tool. It simplifies the operation of building shared libraries on different platforms
• libtoolize generates a customize version of the generic libtool script ltmain.sh, used by config.status
• libtoolize also adds to the m4 folder a set of m4 files to help aclocal to find the M4 macros related to libtool
  • m4/libtool.m4, m4/ltobsolete.m4, m4/ltsugar.m4, m4/ltversion.m4
• The macro language used by Autoconf is called M4

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

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


---

<!-- Pagina 11 -->

autoconf (bash script)

autoconf generates the configuration script from configure.ac

It creates:

• the shell script ‘configure’, that is equal to configure.ac with resolved macros (i.e.: thousands of lines long)
  • In the early 1990s every one was writing its own configuration script.. not easy to maintain!

• the autom4te.cache folder, that contains autom4te caching wrapper for M4, used to decrease the time successive tools spend accessing configure.ac

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

automake (perl script)

automake generates Makefile.in from Makefile.am

• Makefile.in is a standard makefile template (that contains several hundreds of lines of parameterized make scripts)

automake --add-missing adds also the required missing utility scripts into the project:

• install-sh: wrapper of the system’s installation utility, as the Linux installation utility is not portable

• config.guess, config.sub scripts used to obtain info about the system (uname, host, target, CPU, vendor, OS)

• depcomp: script that automatically tracks the dependencies as side-effect of compilation

• test-driver: script that run the tests analyzing their execution, and providing their result in log and console

• ar-lib, compile, missing: various wrappers (for Microsoft libs, old compiler which do not understand some commands; potentially missing gnu programs)

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

```markdown

./configure (shell script)

• Configure determines platform characteristics and features as specified in configure.ac, and stores the check result in config.status
• Configure runs config.status, that creates the makefiles from Makefile.in
• Configure creates config.log, that contains information about configure process and all the events of a configure fails

Makefile.in is a makefiles template, and the user cannot compile with make before running the configure.

• The configure adds platform characteristics into the makefile (uname, host, CPU, target)
• The configure adds also user specified optional features (paths, enable tests, others)
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

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


---

<!-- Pagina 15 -->

```markdown
configure.ac – general

• Written with a mix of shell and M4 macros
• AC_ prefix used for autoconf macros
• AM_ prefix used for automake macros
• AC and AM macros and variables used only for general settings
• PCKGNAME_ prefix used for user-defined macros and variables
• ‘-I’ tells the preprocessor to add a path to its search paths
• ‘-L’ tells the linker to add a path to its search paths
• ‘-l’ tells the linker to link against libraries
• CPPFLAGS are extra flags to give to the C/C++ preprocessor
• CXXFLAGS are extra flags to give to the C++ compiler
• LDFLAGS are extra flags to give to compiler the paths where it is supposed to invoke the linker, using -L.
• LDADD are extra flag that links against libraries with -l
```

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)


---

<!-- Pagina 16 -->

```markdown
configure.ac – content – 1

AC_PREREQ(2.16) # 𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)


---

<!-- Pagina 18 -->

```markdown
configure.ac – content – 3

PFICT_LIBADD="$PFICT_LIBADD" # ääUäääääääääääääääääääääääääääääää

---

**Immagini estratte:**

![Figura estratta 1](images/p18_img01.jpg)


---

<!-- Pagina 20 -->

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

![Figura estratta 1](images/p20_img01.jpg)


---

<!-- Pagina 21 -->

Top-level Makefile.am

AUTOMAKE_OPTIONS = foreign # äÄUäÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ

---

**Immagini estratte:**

![Figura estratta 1](images/p21_img01.jpg)


---

<!-- Pagina 22 -->

Makefile.am for executable

AM_CXXFLAGS = @PFICT_CXXFLAGS@ # dbjdde ààààÁéêêêêêêêêêêêêêêêêêêêêêêêêêêêêêêê

---

**Immagini estratte:**

![Figura estratta 1](images/p22_img01.jpg)


---

<!-- Pagina 25 -->

# pj.m4

AC_DEFUN([AC_ARG_WITH_PJ1], [ `äÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)


---

<!-- Pagina 26 -->

Wrapping it up, add a new executable

To compile a new executable whose source is in example/ex1/:

• Add in `configure.ac`:
  • Add your path to the preprocessor FLAG: `PFICT_CPPFLAGS="$PFICT_CPPFLAGS "'-I$(top_srcdir)/examples/ex1'`
  • Add its Makefile.in to the list of the makefile to parse `AC_CONFIG_FILES([
    Makefile
    m4/Makefile
    example/ex1
    ...
  ])`

• Add the subdirectory in Top-level `Makefile.am`:
  SUBDIRS = m4 \
    example/ex1 \
    .. → after last subdir DO NOT PLACE the escape "\ "

• Create example/ex1/Makefile.am (Makefile.am for executables)

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)


---

<!-- Pagina 27 -->

Wrapping it up, add a new library

To compile a new library whose source is in the folder p_lib1/

• Add in configure.ac:
  • Add the lib path to the preprocessor search path FLAG (-I):
    PFICT_CPPFLAGS="$PFICT_CPPFLAGS "'-I$(top_srcdir)/p_lib1"
  • Add the lib path to the linker search path FLAG (-L):
    PFICT_LDFLAGS="$PFICT_LDFLAGS "'-L$(top_srcdir)/p_lib1"
  • Create a new linker library (-l) macro, specific for this lib
    P_LIB1_LDADD="$P_LIB1_LDADD "'-ap_lib1"
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

![Figura estratta 1](images/p27_img01.jpg)


---

<!-- Pagina 28 -->

Wrapping it up, add a new library - 2

To compile a new library whose source is in the folder p_lib1/

• Add the subdirectory in Top-level Makefile.am:
  SUBDIRS = m4 \
    p_lib1 \
    .. → after last subdir DO NOT PLACE the escape "\\ "

• Create p_lib1/Makefile.am (Makefile.am for libraries)

• Optionally, (but good practice) create a test for the lib
  • A test is an executable to place into the test/ folder
  • It automatically tests the library functionalities
  • In the case the test fails, the installation is not performed
  • It is optionally compiled, if the installer is run with the ¬t1 option
    • This option in the installer launches ./configure --with-test=1

---

**Immagini estratte:**

![Figura estratta 1](images/p28_img01.jpg)


---

<!-- Pagina 29 -->

Add the test p_lib1_test

A test is an executable whose source is in test/p_lib1_test/:

• **configure.ac**: same as executable (replacing with the right path)

• In Top-level **Makefile.am**: add path and test inside the “if WITH_TEST” statement:
  ```makefile
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

![Figura estratta 1](images/p29_img01.jpg)
