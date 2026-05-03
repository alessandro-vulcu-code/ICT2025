Bind a server sockets in C++ - 2

```c
int sckfd = socket(AF_INET, SOCK_STREAM, 0)
struct sockaddr_in my_addr = {0}; /**< init it to 0 */
my_addr.sin_family = AF_INET; /**< Family IPv4 */
my_addr.sin_port = htons(recv_port); /**< Sets socket port*/
my_addr.sin_addr.s_addr = htonl(INADDR_ANY);
 /**< all interfaces */
if (bind(sckfd, (struct sockaddr*) &my_addr,
 /**< bind it */
sizeof(my_addr)) < 0) {
/* ERROR: bind failed: exit */
}
```

Use a socket

---

**Immagini estratte:**

![Figura estratta 1](images/p20_img01.jpg)
