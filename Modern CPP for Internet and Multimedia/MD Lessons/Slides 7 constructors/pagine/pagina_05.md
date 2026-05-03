Constructors and destructors

Pair of actions that are strictly related (object life cycle starts with a constructor and ends with the destructor)

```c
#include <iostream>
struct Tracer {
    std::string mess;

    Tracer(const string& s) : mess{s}
    {
        std::cout << mess;
    }

    ~Tracer()
    {
        std::cout << "~ " << mess;
    }
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)
