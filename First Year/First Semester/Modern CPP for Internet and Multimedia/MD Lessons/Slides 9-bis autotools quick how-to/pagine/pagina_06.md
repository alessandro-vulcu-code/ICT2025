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
