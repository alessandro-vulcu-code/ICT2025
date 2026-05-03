<!-- Pagina 1 -->

How does C++ work?

Modern C++ Programming for ICT
Filippo Campagnaro
filippo.campagnaro@unipd.it

---

**Immagini estratte:**

![Figura estratta 1](images/p01_img01.jpg)

![Figura estratta 2](images/p01_img04.jpg)

![Figura estratta 3](images/p01_img03.jpg)

![Figura estratta 4](images/p01_img02.jpg)


---

<!-- Pagina 2 -->

Outline

1. Why C++?
2. Compilations steps
3. Preprocessor
4. Compiler
5. Linker
6. Static library vs dynamic library

MORE INFO: “Advanced C and C++ Compiling”, Milan Stevanovic

http://www.keil.com/support/man/docs/armcc/armcc_chr1359124221739.htm

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Why C++, if I’ve learnt Java!

• Java works over a Virtual Machine: your software is “compiled” for the virtual machine, whose interpreter “translates” the instructions for the VM to the instructions for the actual hardware architecture.

• In C++ you must compile in machine code for the target machine for which the code has to be executed, using the proper tool-chain (arm, x86, x64, etc.)

• Way faster: the code is directly executed to the machine!
  • Pay attention: bad programming in C++ may result in slow software

• Drawback: if your software needs to run in different target machines, you need to cross compile it for each target

• In TLC you must be fast (e.g., in a Gbps router, the routing software can’t be the bottleneck!)

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

How C++ works

• Preprocessing: the preprocessor takes a C++ source code file and deals with the #includes, #defines and other preprocessor directives. The output of this step is a "pure" C++ file without pre-processor directives, the translation unit.

• Compilation: the compiler takes the translation units and produces an object file from each of them.

• Linking: the linker takes the object files produced by the compiler and produces either a library or an executable file.

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img01.jpg)


---

<!-- Pagina 5 -->

Preprocessor: always before compiler

• Evaluates the preprocessor directives, aka whatever is written after #, and substitutes them into the code. Agnostic to C++ syntax.

• E.g.: macros → use them as less as possible (here use constexpr!)

CPP FILE

```c
#define MAX_HGHT 720
#define AREA(a,b) (a*b)
int maxArea(int a)
{
    return
        AREA(a,MAX_HGHT);
}
int main(int argc,
          char* argv[])
{
    int l = MAX_HGHT;
    int a = maxArea(l);
}
```

PREPROCESSOR

TRANSLATION UNIT

```c
int maxArea(int a)
{
    return
        a*720;
}
int main(int argc,
          char* argv[])
{
    int l = 720;
    int a = maxArea(l);
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)


---

<!-- Pagina 6 -->

Preprocessor: #include

```cpp
// my-fun.h
inline int incr(int i)
{
    return i+1;
}

// example2.h
#include "my-fun.h"
inline int ex2(int i)
{
    return incr(i+2);
}

// example.h
#include "my-fun.h"
inline int ex(int i)
{
    return incr(i+1);
}

// example.cpp
#include <iostream>
#include "example.h"
#include "example2.h"
int main()
{
    std::cout << ex(1)
             << ex2(2);
}
```

DOES NOT COMPILE!

error: redefinition of ‘int incr(int)’

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)


---

<!-- Pagina 7 -->

Why is it not compiling?
error: redefinition of ‘int incr(int)’
// ONLY CPP FILES ARE COMPILED: NOT HEADERS!!
// THE COMPILER SEES a unique file (translation unit)
... //code of lines of iostream
inline int incr(int i) {
  return i+;
}
inline int ex(int i) {
  return incr(i+1);
}
inline int incr(int i) {
  return i+;
}
inline int ex2(int i) {
  return incr(i+2);
}
int main() {
  std::cout << ex(1) << ex2(2);
}

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)


---

<!-- Pagina 8 -->

Preprocessor: Conditional compilation

```cpp
//my-fun.h
#ifndef MY_FUN_H
#define MY_FUN_H
inline int incr(int i)
{
    return i+1;
}
#endif

If MY_FUN_H already been defined, do not compile this code

• This construct is the wrapper #ifndef or “include guards”
• When the header is included again, the conditional will be false, and the preprocessor will skip over the entire contents of the file, and the compiler will not see it twice.
• Always use it in all your .h files: you never know if you need to include them somewhere in the future!!
• Be sure all headers are defined with a different name, or you’ll have big troubles!!!
```

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)


---

<!-- Pagina 9 -->

Now it compiles...

```cpp
// ONLY CPP FILES ARE COMPILED: NOT HEADERS!!
// THE COMPILER SEES a unique translation unit
// (basically, one per cpp file)

... //code of lines of iostream
inline int incr(int i) {
  return i+1;
}
inline int ex(int i) {
  return incr(i+1);
}

inline int ex2(int i) {
  return incr(i+2);
}
int main() {
  std::cout << ex(1) << ex2(2);
}
```

Example.h

Example2.h

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Compiler

• Parses (linguistic analysis) the translation unit
• Converts it to assembly code (still human readable ASCII) for a specific CPU instruction set
• Optimizes the assembly code: the use of the registers is minimized, and eliminates the parts of the code that do not need to be executed. Different levels of optimization:
  • O0 (Minimum optimizer) doesn’t optimize: fast compilation, slow code, used for debugging
  • O1 (Restricter optimizer) just removes unused lines, used for debugging
  • O2 (High optimization, DEFAULT) minimizes the use of register, harder to debug
  • O3 (Maximum optimization) optimizes more, poor debug view
• Converts the assembly code into the specific machine instructions producing the actual binary: the object file.
• The compilation step is performed on each translation unit: each translation unit is compiled into a binary object file

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Compiler

• The object file contains the compiled code (in binary form) of the symbols found in the translation unit.

• Object files can refer to symbols that are not defined (but just declared).

• You can compile each translation unit separately, so you don't need to recompile everything if you only change a single file.

• The object files can be put in archives called static libraries.

• At this stage only compiler errors, like syntax errors (during the Linguistic analysis phase) or failed overload resolution errors, are reported.

• Code is still not ready to be executed!

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

Compiler

```cpp
// my-fun.h
int incr(int i);

// example.h
#include "my-fun.h"
inline int ex(int i)
{
    return incr(i+1);
}

// example.cpp
#include <iostream>
#include "example.h"
int main()
{
    std::cout << ex(1);
}
```

The compiler CREATES example.o from example.cpp, but doesn’t produce executable: a linker error arises:

undefined reference to `incr(int)`
collect2: error: ld returned 1 exit status

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Compiler

```cpp
// my-fun.h
int incr(int i);

// my-fun.cpp
#include "my-fun.h"
int incr(int i)
{
    return i+1;
}

// example.h
#include "my-fun.h"
inline int ex(int i){
    return incr(i+1);
}

// example.cpp
#include <iostream>
#include "example.h"
int main() {
    std::cout << ex(1);
}
```

It creates the executable:

- my-fun.cpp compiled into my-fun.o
- example.cpp compiled into example.o,
- **Linker** creates the executable, resolving the undefined symbol **incr** into example.o

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Linker

• The linker produces the final compilation output from the object files the compiler produced. This output can be either a shared (or dynamic) library or an executable.

• It links all the object files by replacing the references to undefined symbols with the correct addresses.

• Each of these symbols can be defined in other object files or in libraries.

• If they are defined in libraries other than the standard library, you need to tell the linker about them.

• The most common errors are missing definitions (not exists or the file not provided to the linker) or duplicate definitions.

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Linker vs compiler duplicated definitions

• Duplicated definitions in a single translation unit = compiler error  error: redefinition of ‘int incr(int)’
• Duplicated definition in two different translation units = linker error

```cpp
// my-fun.h
int incr(int i);

// my-fun.cpp
#include “my-fun.h”
int incr(int i) {
    return i+1;
}

// example.cpp
#include “my-fun.h”
int incr(int i) {
    return i+1;
}

int main() {
    std::cout << incr(1);
}
```

my-fun.cpp:3: multiple definition of `incr(int)`
example.cpp:3: first defined here
collect2: error: ld returned 1 exit status

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)


---

<!-- Pagina 16 -->

Wrapping it up: 1 - Preprocessor

```cpp
// my-fun.h
int incr(int i);

// my-fun.cpp
#include "my-fun.h"
int incr(int i)
{
    return i+1;
}

translation unit

// translation unit
//of my-fun.cpp
int incr(int i);
int incr(int i)
{
    return i+1;
}

// example.h
#include "my-fun.h"
inline int ex(int i){
    return incr(i+1);
}

// example.cpp
#include "example.h"
int main() {
    int i = ex(1) + ex(2);
}

translation unit

int incr(int i);
inline int ex(int i){
    return incr(i+1);
}
int main() {
    int i = ex(1) + ex(2);
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)


---

<!-- Pagina 17 -->

Wrapping it up: 2 - Compiler

```cpp
//translation unit
//of my-fun.cpp
int incr(int i);

int incr(int i)
{
    return i+1;
}

compilation
my-fun.o

//translation unit
//of example.cpp
int incr(int i);
inline int ex(int i){
    return incr(i+1);
}
int main() {
    int i = ex(1) + ex(2);
}

compilation
example.o
101
011
17
```

---

**Immagini estratte:**

![Figura estratta 1](images/p17_img01.jpg)

![Figura estratta 2](images/p17_img02.jpg)


---

<!-- Pagina 18 -->

Wrapping it up: 3 - Linker

my-fun.o
definition of
int incr(int)

example.o
101
011

executable_example

---

**Immagini estratte:**

![Figura estratta 1](images/p18_img01.jpg)

![Figura estratta 2](images/p18_img02.jpg)


---

<!-- Pagina 19 -->

Static library

• It is an archive of object files created at compile time
• The executable is portable, but very large
• If one file is changed, the whole system needs to be recompiled

Objects
101 011
101 011
101 011

archiver

Static library
lib1.a

Ecobuild

101 011
101 011
101 011
101 011

linker

executable

Ecobuild

101 011
101 011
101 011
101 011

linker

executable

19

---

**Immagini estratte:**

![Figura estratta 1](images/p19_img01.jpg)

![Figura estratta 2](images/p19_img02.jpg)

![Figura estratta 3](images/p19_img03.jpg)


---

<!-- Pagina 20 -->

Shared (or Dynamic) library

• Library created by the linker, it can depend on external libs,
  • In this case the linker trusts the fact it will be able to link them in run time
• Loaded at runtime during the code execution, once for all programs
• If one file is changed, only the library needs to be recompiled

Loader at RUNTIME
Dynamic linking

Objects
101 011
101 011
101 011

Linker
Shared Library lib1.so

Objects
101 011
101 011
101 011

Linker
Shared Library lib2.so

Objects
101 011
101 011
101 011

Linker
Executable

---

**Immagini estratte:**

![Figura estratta 1](images/p20_img01.jpg)

![Figura estratta 2](images/p20_img02.jpg)
