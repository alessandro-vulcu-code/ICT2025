autoconf (bash script)

autoconf generates the configuration script from configure.ac

It creates:

• the shell script ‘configure’, that is equal to configure.ac with resolved macros (i.e.: thousands of lines long)
  • In the early 1990s every one was writing its own configuration script.. not easy to maintain!

• the autom4te.cache folder, that contains autom4te caching wrapper for M4, used to decrease the time successive tools spend accessing configure.ac

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)
