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
