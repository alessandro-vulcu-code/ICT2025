Bind a server sockets in C++

• Bind associates the socket to its local address, port number and interface (Ethernet1, WiFi, etc) with my_addr
  my_addr.sin_addr.s_addr = htonl(INADDR_ANY);

• INADDR_ANY binds the socket source address to all the source addresses of all the available interfaces.
  • i.e., if a PC has WiFi, Ethernet and loopback interfaces, it permits to use the socket with all of them

• If you decide to use only one of the interfaces, set its IP
  my_addr.sin_addr.s_addr =
  inet_addr("127.0.0.1"); //loopback

---

**Immagini estratte:**

![Figura estratta 1](images/p19_img01.jpg)
