UDP send C++ - send

```c
int w_bytes = sendto(sckfd, tx_buf, size2tx ,
<flag>,
(struct sockaddr*) &dest_addr,
sizeof(dest_addr)); // send

• <flag> always set to 0 (other values are for advanced stuff),

• w_bytes < 0 means socket error
```

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)
