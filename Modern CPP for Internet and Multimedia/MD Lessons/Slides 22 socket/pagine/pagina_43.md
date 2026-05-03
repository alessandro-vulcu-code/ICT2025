TCP client example – setup

```cpp
int sckfd = socket(AF_INET, SOCK_STREAM, 0);
if (sckfd < 0){ /*ERR*/}
int option(1);
setsockopt(sckfd, SOL_SOCKET, SO_REUSEADDR,
             (char*)&option, sizeof(option));
struct sockaddr_in dest_addr = {0};
dest_addr.sin_family = AF_INET;
const char* dest_ip = "192.168.100.12";
int dest_port = 55555;
dest_addr.sin_port = htons(dest_port);
if (inet_pton(AF_INET, dest_ip, &dest_addr.sin_addr)
≤ 0) {
    /*conversion host_ip to AF_ADDRESS FAILED*/
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p43_img01.jpg)
