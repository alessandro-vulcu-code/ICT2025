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
