UDP send C++

• To send to the remote, address and port specified in `dest_addr`
  1. `const char* dest_ip = “192.168.100.123”`;
  2. `struct sockaddr_in dest_addr = {0}; // struct to set destination`
  3. `dest_addr.sin_family = AF_INET; // use IPv4`
  4. `dest_addr.sin_port = htons(dest_port); // set dest port`
  5. `if (inet_pton(AF_INET, dest_ip, &dest_addr.sin_addr) <= 0) {
    /*ERR: conversion host_ip to AF_ADDR failed*/
  } // set dest IP`
  6. `int w_bytes = sendto(sckfd, tx_buf, size2tx, <flag>, (struct sockaddr*) &dest_addr, sizeof(dest_addr)); // send`

---

**Immagini estratte:**

![Figura estratta 1](images/p24_img01.jpg)
