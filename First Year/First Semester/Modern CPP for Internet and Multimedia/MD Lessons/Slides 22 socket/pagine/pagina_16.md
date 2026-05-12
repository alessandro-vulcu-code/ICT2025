Open a sockets in C++

```c
int socket(family,type,protocol);
• @return socket file descriptor. If < 0 operation failed
• @family we always use AF_INET = address type IPv4
  • These families are defined in <sys/socket.h>
• @type SOCK_DGRAM = UDP socket,
  SOCK_STREAM = TCP socket
• @protocol: always set it to 0 for the internet protocol (IP)

int udp_socket_fd = socket(AF_INET,
  SOCK_DGRAM,0)

int tcp_socket_fd = socket(AF_INET,
  SOCK_STREAM,0)
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p16_img01.jpg)
