TCP server example - setup

```cpp
int scklist = socket(AF_INET, SOCK_STREAM, 0);
if (scklist < 0){ /*ERR*/}
int option(1);
setsockopt(scklist, SOL_SOCKET, SO_REUSEADDR,
             (char*)&option, sizeof(option));
struct sockaddr_in my_addr = {0};
my_addr.sin_family = AF_INET;
int listen_port = 55555;
my_addr.sin_port = htons(listen_port );
my_addr.sin_addr.s_addr = htonl(INADDR_ANY);
if (bind(scklist,(struct sockaddr*)&my_addr,
sizeof(my_addr)) < 0)
{ /*err*/}
```

---

**Immagini estratte:**

![Figura estratta 1](p40_img01.jpg)
