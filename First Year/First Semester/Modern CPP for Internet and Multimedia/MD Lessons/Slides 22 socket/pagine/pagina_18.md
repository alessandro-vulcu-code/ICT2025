Functions for Internet addresses - 2

• `inet_addr()` converts a string in the standard IPv4 dotted decimal notation, to an Internet address.
  • `inet_pton()` similar, but also for IPv6
  ```python
  dest_addr.sin_addr.s_addr =
  inet_addr("192.168.100.1");
```

• `inet_ntoa()` converts the Internet host address to a string in the Internet standard dot notation (IPv4).
  • `inet_pton()` similar, but also for IPv6
  ```python
  char* ip = inet_ntoa(dest_addr.sin_addr);
```

---

**Immagini estratte:**

![Figura estratta 1](p18_img01.jpg)
