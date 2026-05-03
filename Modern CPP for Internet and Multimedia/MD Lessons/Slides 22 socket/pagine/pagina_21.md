Close a socket

• Always remember to close a socket
• close(socket_fd); closes a file descriptor, so that it no longer refers to any file and may be reused. All send/recv are unlocked.
  • More info: type in terminal man close
  • It destroys the socket and pending data are lost

• shutdown(socket_fd, flag); blocks communication in one (flag = SHUT_RD or flag = SHUT_WR) or both (flag = SHUT_RDWR) directions.
  • you will still be able to receive pending data the peer already sent

---

**Immagini estratte:**

![Figura estratta 1](images/p21_img01.jpg)
