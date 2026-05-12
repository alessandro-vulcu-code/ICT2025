Include from standard c library - 2

```c
#include <sys/socket.h> // includes:
• the socketaddr struct,
• the socket macros: SOCK_DGRAM, SOCK_STREAM, ...
#include <netinet/in.h> // includes:
• the socketaddr_in struct used to store addresses for the Internet protocol family, must be cast to socketaddr struct for use with socket
#include <unistd.h>// includes:
• the POSIX operative system API syscall wrapper for I/O
  • read, write and close
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p15_img01.jpg)
