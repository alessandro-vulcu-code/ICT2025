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
