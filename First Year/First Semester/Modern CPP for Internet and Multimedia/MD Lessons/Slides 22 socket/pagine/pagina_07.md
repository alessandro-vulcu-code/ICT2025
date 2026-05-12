What is a socket? – syscall and port

• socket() system routine creates the socket file descriptor
• send() and recv() socket calls are used to communicate through the socket
  • NOTE: they are system call, and it is pure C, not C++!

• A socket is composed by a copy `<ip_address,port>`, where
  • ip_address is the ip address of the host
  • port is the port in which the process of host is listening
  • use only port > 1024, the others are well-known ports (for example, 21 = ftp, 22=ssh 80=http)

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)
