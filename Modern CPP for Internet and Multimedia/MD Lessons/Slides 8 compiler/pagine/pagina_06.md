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
