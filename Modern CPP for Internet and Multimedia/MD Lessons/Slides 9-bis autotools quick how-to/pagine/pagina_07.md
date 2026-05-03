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

![Figura estratta 1](images/p07_img01.jpg)
