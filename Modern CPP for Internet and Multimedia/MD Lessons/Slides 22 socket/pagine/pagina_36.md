# UDP Server example – setup

```c
int sckfd = socket(AF_INET, SOCK_DGRAM, 0); int
option = 1;
if (sckfd < 0){ /*ERR*/}
setsockopt(sckfd, SOL_SOCKET, SO_REUSEADDR,
             (char*)&option,
sizeof(option));
struct sockaddr_in my_addr = {0};
struct sockaddr_in srcaddr;
socklen_t addrlen = sizeof(srcaddr);
my_addr.sin_family = AF_INET;
my_addr.sin_port = htons(recv_port);
my_addr.sin_addr.s_addr = htonl(INADDR_ANY);
if (bind(sckfd, (struct sockaddr*) &my_addr,
sizeof(my_addr))<0) {
```

---

**Immagini estratte:**

![Figura estratta 1](images/p36_img01.jpg)
