```markdown
configure.ac – pthread

AC_CHECK_LIB(pthread, pthread_create, [LIBS="$LIBS -lpthread"])#

• This function checks if the pthread library is available or not (running the thread function `pthread_create`). If the check passes, it add lpthread to the libraries to load.
• If you work with threads, you must use it, otherwise it will not compile
• libpthread is a library containing the definition of pthread, i.e., the POSIX threads. It includes four groups of procedures:
  1. Thread management - creating, joining threads etc.
  2. Mutexes
  3. Condition variables
  4. Synchronization between threads using locks and barriers
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)
