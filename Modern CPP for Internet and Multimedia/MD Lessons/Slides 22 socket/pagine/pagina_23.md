UDP receive in C++

Code to receive with a bound SERVER:

1. struct sockaddr_in srcaddr = {0}; //struct to get source address
2. socklen_t addrlen = sizeof(srcaddr); // variable with its size
3. int recv_bytes = recvfrom(sckfd, rx_buffer, max_size, 0, (struct sockaddr *)&srcaddr, &addrlen);

• Always set the flag to 0, others are for specific behaviors
• srcaddr and addrlen are set from recvfrom, so the server can check from which host it is receiving (e.g., checking if the client changed)
• recv_bytes = -1 in case of error

---

**Immagini estratte:**

![Figura estratta 1](images/p23_img01.jpg)
