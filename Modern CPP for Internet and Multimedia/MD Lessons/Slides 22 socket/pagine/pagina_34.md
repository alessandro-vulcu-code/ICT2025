Solution2: handling SIGPIPE

```c
#include <signal.h>
#include <cstring>

void function handleIt(int sig_id) {/*handle the signal sig_id*/}
main() {
    struct sigaction act;// structure used to handle the signals
    memset(&act, '\0', sizeof(act));
    act.sa_handler = &handleIt; // perform handleIt function
    if (sigaction(SIGPIPE, &act, NULL) < 0) {
        std::cerr << "sigaction failed" << std::endl;
    }
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p34_img01.jpg)
