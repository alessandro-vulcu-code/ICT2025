TCP server example – exchange data

```cpp
int rcv_size = recv(sockfd, buf, max_size, 0);
if(rcv_size < 0) {
    /*ERROR! CLOSE AND EXIT!!!*/
}
std::cout << rx_buf << std::end;
int sent_size = send(sockfd, buf, rcv_size, 0);
if(sent_size < 0) {
    /*ERROR: CLOSE AND EXIT!*/
}
close(sockfd);
close(scklist);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p42_img01.jpg)
