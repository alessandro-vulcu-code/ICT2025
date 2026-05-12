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
