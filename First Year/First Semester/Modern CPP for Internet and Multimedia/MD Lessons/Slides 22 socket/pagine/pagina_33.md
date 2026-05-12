Avoid SIGPIPE killing the process

• Solution 1: ignore the signal
```c
#include <signal.h>
#include <cstring>
main() {
    struct sigaction act; // structure that contains the handler
    memset(&act, '\0', sizeof(act));
    act.sa_handler = SIG_IGN; // handler that ignores the signal
    if (sigaction(SIGPIPE, &act, NULL) < 0) { // set the handler
        std::cerr << "sigaction failed" << std::endl;
// to SIGPIPE
    }
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p33_img01.jpg)
