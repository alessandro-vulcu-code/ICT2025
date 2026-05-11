# How Does C++ Work?

## Outline
- [Why C++](#why-c)
- [Compilation Pipeline](#compilation-pipeline)
  - [Preprocessing](#preprocessing)
  - [Compilation](#compilation)
  - [Linking](#linking)
- [Preprocessor](#preprocessor)
  - [Macros](#macros)
  - [include and Translation Units](#include-and-translation-units)
  - [Include Guards](#include-guards)
- [Compiler](#compiler)
  - [Object Files and Undefined Symbols](#object-files-and-undefined-symbols)
- [Linker](#linker)
  - [Linker Errors](#linker-errors)
  - [Full Build Pipeline](#full-build-pipeline)
- [Libraries](#libraries)
  - [Static Libraries](#static-libraries)
  - [Shared or Dynamic Libraries](#shared-or-dynamic-libraries)

## Study Notes

This lesson explains the C++ build process: preprocessing, compilation, linking, and the difference between static and dynamic libraries. The source references **Advanced C and C++ Compiling** by Milan Stevanovic and the ARM compiler documentation at `http://www.keil.com/support/man/docs/armcc/armcc_chr1359124221739.htm`.

### Why C++

Java runs over a virtual machine: code is compiled for the VM, and the VM interpreter or runtime translates VM instructions into instructions for the actual hardware architecture.

C++ is different. A C++ program is compiled into **machine code** for a specific target machine and toolchain, such as ARM, x86, or x64. This makes C++ very fast because the generated code runs directly on the machine. The drawback is that software intended for multiple targets must be cross-compiled for each target.

The source connects this to telecommunications: in a Gbps router, routing software must not become the bottleneck. C++ can provide the required speed, but bad C++ programming can still produce slow software.

### Compilation Pipeline

![[Pasted image 20260511102016.png]]

#### Preprocessing

The **preprocessor** takes a C++ source file and handles `#include`, `#define`, and other preprocessor directives. Its output is a "pure" C++ file without preprocessor directives: the **translation unit**.
![[Pasted image 20260511102038.png]]
#### Compilation

The **compiler** takes each translation unit and produces an object file. Each `.cpp` file normally becomes one translation unit, and each translation unit is compiled separately.

#### Linking

The **linker** takes object files and produces either a library or an executable. Linking resolves references between separately compiled object files.

### Preprocessor

The preprocessor always runs before the compiler. It evaluates directives, meaning text written after `#`, and substitutes them into the code. It is **agnostic to C++ syntax**, so it performs textual processing rather than type-aware C++ analysis.

#### Macros

The source warns to use macros as little as possible and to prefer `constexpr` when appropriate.

CPP file:

```cpp
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

After preprocessing, macro names are replaced textually.

Translation unit:

```cpp
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

`MAX_HGHT` becomes `720`, and `AREA(a,MAX_HGHT)` becomes `a*720`. The spelling `MAX_HGHT` is preserved from the source. This example also shows why macros are risky: the replacement is purely textual and does not respect C++ types or scopes.

#### include and Translation Units

`#include` copies header contents into the including file before compilation.

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

This does not compile because `my-fun.h` is included twice into the same translation unit, producing a redefinition of `int incr(int)`.

The source shows the compiler's view after preprocessing:

```cpp
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
```

The `return i+;` lines are corrupted by PDF conversion; they likely meant `return i+1;`. The important point is that headers are not compiled independently. Their text is inserted into `.cpp` files, and the compiler sees one translation unit.

#### Include Guards

Include guards prevent a header from being processed more than once in the same translation unit.

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

- This construct is the wrapper #ifndef or "include guards"
- When the header is included again, the conditional will be false, and the preprocessor will skip over the entire contents of the file, and the compiler will not see it twice.
- Always use it in all your .h files: you never know if you need to include them somewhere in the future!!
- Be sure all headers are defined with a different name, or you'll have big troubles!!!
```

This block mixes C++ and slide text. The actual C++ is the `#ifndef`, `#define`, header body, and `#endif`. The guard macro name must be unique across headers.

With the guard, the translation unit contains only one definition of `incr`:

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

### Compiler

The compiler parses the translation unit, converts it to assembly code for a specific CPU instruction set, optimizes the code, and converts the assembly into machine instructions. The result is an **object file**.

Optimization levels include:

- **`O0`**: minimum optimization; fast compilation, slow code, useful for debugging.
- **`O1`**: limited optimization; removes unused lines, still useful for debugging.
- **`O2`**: high optimization and often the default; harder to debug.
- **`O3`**: maximum optimization; can produce a poor debug view.

Compilation is performed independently for each translation unit.

#### Object Files and Undefined Symbols

An object file contains compiled binary code for symbols found in the translation unit. It may also contain references to symbols that are declared but not defined. At this stage, compiler errors such as syntax errors or overload resolution errors are reported, but the program is still not ready to execute.

Example with a missing definition:

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

The compiler can create `example.o` from `example.cpp`, but it cannot produce an executable alone. The linker reports:

```text
undefined reference to `incr(int)`
collect2: error: ld returned 1 exit status
```

Adding the missing definition fixes the issue:

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

Now `my-fun.cpp` is compiled into `my-fun.o`, `example.cpp` is compiled into `example.o`, and the linker resolves the undefined symbol `incr` to create the executable.

### Linker

The **linker** produces the final build output from object files. The output may be an executable, a shared library, or a dynamic library.

The linker replaces references to undefined symbols with the correct addresses. Those symbols may be defined in other object files or libraries. If non-standard libraries are needed, the build must tell the linker about them.

#### Linker Errors

Common linker errors include missing definitions and duplicate definitions.

Duplicate definitions inside one translation unit are compiler errors. Duplicate definitions across different translation units are linker errors.

```cpp
// my-fun.h
int incr(int i);

// my-fun.cpp
#include "my-fun.h"
int incr(int i) {
    return i+1;
}

// example.cpp
#include "my-fun.h"
int incr(int i) {
    return i+1;
}

int main() {
    std::cout << incr(1);
}
```

The source used curly quotes in `#include`; the valid form uses normal quotes. This program defines `incr(int)` in both `my-fun.cpp` and `example.cpp`, so the linker reports multiple definitions.

```text
my-fun.cpp:3: multiple definition of `incr(int)`
example.cpp:3: first defined here
collect2: error: ld returned 1 exit status
```

#### Full Build Pipeline

Preprocessing expands includes into translation units:

![[Pasted image 20260511102320.png]]

This source block includes slide labels such as `translation unit`. The idea is that the preprocessor produces one translation unit per `.cpp` file.

Compilation then turns translation units into object files:
![[Pasted image 20260511102346.png]]


The diagram represents compilation from translation units into object files.

The linker combines object files into an executable:
![[Pasted image 20260511102423.png]]

The diagram represents `my-fun.o` and `example.o` being linked into `executable_example`.

### Libraries

#### Static Libraries

A **static library** is an archive of object files created at compile time. It is often named with an extension such as `.a`.

Advantages and drawbacks from the source:

- the executable is portable because the library code is included in it;
- the executable can become very large;
- if one file is changed, the whole system may need to be recompiled or relinked depending on the build structure.
![[Pasted image 20260511102504.png]]

#### Shared or Dynamic Libraries

A **shared** or **dynamic** library is created by the linker and loaded at runtime. It can depend on external libraries. In that case, the linker trusts that those dependencies will be available at runtime.

Dynamic libraries are loaded once for all programs that use them. If one file changes, only the library may need recompilation rather than rebuilding every executable that uses it.

![[Pasted image 20260511102524.png]]

The diagram represents dynamic linking: shared libraries such as `lib1.so` and `lib2.so` are loaded at runtime by the loader.

## 5 Mins Questions

No 5 mins questions are present in the source material.

## Final Summary

C++ code becomes an executable through three main stages. The **preprocessor** expands directives and creates translation units. The **compiler** parses and optimizes each translation unit into object files. The **linker** resolves symbols across object files and libraries to create an executable or library.

Headers are not compiled independently; their contents are inserted into `.cpp` files, so include guards are essential. Compiler errors concern individual translation units, while linker errors concern unresolved or duplicated symbols across object files. Static libraries copy library code into executables, while dynamic libraries are loaded at runtime and can be shared across programs.
