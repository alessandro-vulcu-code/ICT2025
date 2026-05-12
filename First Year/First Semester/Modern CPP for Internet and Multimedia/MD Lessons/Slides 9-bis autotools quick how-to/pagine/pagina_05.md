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
