Functions for Internet addresses

• struct sockaddr_in is a structure for handling internet addresses (e.g., my_addr), defined in <netinet/in.h>
  struct sockaddr_in my_addr = {0}; /**< init it to 0 */

• htonl, htons, ntohl, and ntohs convert values between host and network byte order (big endian vs little endian).
  • htonl unsigned long host to network
  • htons unsigned short host to network
  • ntohl unsigned long network to host
  • ntohs unsigned short network to host
  my_addr.sin_port = htons(listen_port);

---

**Immagini estratte:**

![Figura estratta 1](images/p17_img01.jpg)
