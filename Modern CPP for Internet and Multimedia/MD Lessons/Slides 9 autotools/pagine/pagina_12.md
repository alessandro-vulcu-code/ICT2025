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
