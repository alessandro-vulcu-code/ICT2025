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
