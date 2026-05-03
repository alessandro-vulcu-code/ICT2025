TCP send in C++

You can use both send() or write()
```c
int sent_bytes = send(sckfd, buffer, size2tx, 0);
```

• Flag always is set to 0: other values are for advanced features
• sent_bytes < 0 means an error occurred
• Specific for socket
```c
int sent_bytes = write(sckfd, buffer, size2tx);
```

• sent_bytes < 0 means an error occurred
• Equivalent to send with flag = 0
• Used also for file

---

**Immagini estratte:**

![Figura estratta 1](images/p30_img01.jpg)
