Netcat examples

• netcat is a computer networking utility for reading from and writing to network connections using TCP or UDP.
• nc -l <p> : netcat TCP server listening at port <p>
• nc <ip> <p> : netcat TCP client try to connect to a server with address <ip> at port <p>

server
nc -l 55555
client
nc 147.162.97.6 55555

• nc -lu <p> : netcat UPD server listening at port <p>
• nc -u <ip> <p> : netcat UDP client try to access the server with address <ip> at port <p>

server
nc -lu 55556
client
nc -u 147.162.97.6 55556

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)
