TCP receive in C++

You can use both recv() or read()
```c
int recv_bytes = recv(sckfd, buffer, max_size, 0);
```

• Flag always is set to 0: other values are for advanced features
• recv_bytes < 0 means an error occurred
• Specific for socket
```c
int recv_bytes = read(sckfd, buffer, max_size);
```

• recv_bytes < 0 means an error occurred
• Equivalent to recv with flag = 0
• Used also for file

---

**Immagini estratte:**

![Figura estratta 1](images/p29_img01.jpg)
