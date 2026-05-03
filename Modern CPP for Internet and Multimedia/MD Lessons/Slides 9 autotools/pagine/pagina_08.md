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
