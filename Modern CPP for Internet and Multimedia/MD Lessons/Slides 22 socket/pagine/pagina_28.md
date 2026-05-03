TCP connect in C++ (client)

• The TCP client connects itself to the server `ip:port`
  struct sockaddr_in serv_addr = {0};
  serv_addr.sin_family = AF_INET;
  serv_addr.sin_port = htons(server_port);
  if (inet_pton(AF_INET, serv_ip,
    &serv_addr.sin_addr) ≤ 0) {/*ERR..*/}
  if(connect(sockfd, (struct sockaddr*) &serv_addr,
    sizeof(serv_addr))<0) {/*connect
ERROR*/}
• After connecting to server, `sockfd` can be use to send/receive
data with server

---

**Immagini estratte:**

![Figura estratta 1](images/p28_img01.jpg)
