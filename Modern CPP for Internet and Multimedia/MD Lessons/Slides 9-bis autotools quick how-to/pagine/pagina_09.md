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
