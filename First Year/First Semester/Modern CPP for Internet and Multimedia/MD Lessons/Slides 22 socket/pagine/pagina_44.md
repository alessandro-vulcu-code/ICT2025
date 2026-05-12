TCP client–connect and exchange data

if (connect(sckfd, (struct sockaddr*) &dest_addr, sizeof(dest_addr)) < 0) { /*ERROR: CLOSE AND EXIT*/}
char buf[512] = "data to tx";
size_t data_size = 10;
int sent_size = send(sckfd, buf, data_size, 0);
if(sent_size<0) { /*ERROR: CLOSE AND EXIT*/}
memset(buf, 0, max_size); // set buffer to zero for next read
int rcv_size = recv(sockfd, buf, max_size, 0);
if(rcv_size < 0) { /*ERR!!!*/}
std::cout << buf << std::end;
close(sockfd);

---

**Immagini estratte:**

![Figura estratta 1](p44_img01.jpg)
