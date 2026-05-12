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
