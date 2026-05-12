<!-- Pagina 1 -->

Socket programming

Modern C++ Programming for ICT
Filippo Campagnaro
campagn1@dei.unipd.it

---

**Immagini estratte:**

![Figura estratta 1](images/p01_img01.jpg)

![Figura estratta 2](images/p01_img04.jpg)

![Figura estratta 3](images/p01_img03.jpg)

![Figura estratta 4](images/p01_img02.jpg)


---

<!-- Pagina 2 -->

Outline

1. What is a socket?
2. Netcat examples
3. UDP Socket
4. TCP Socket
5. Set Socket Options
6. Client-server examples

“Beej's Guide to Network Programming - Using Internet Sockets”, Brian
“Beej Jorgensen” Hall, Version 3.0.21, June 8, 2016

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

HW buffer – stack allocation

How do I create an empty buffer (with all bits set to 0) for the serialization?

Using a C-style array (hdr.serialize(buffer,offset)):

• char buffer[3]; // WRONG, IT HAS RANDOM VALUES
• char buffer[3] = {0,0,0};
• char buffer[3] = {0}; // others will be set to 0
• char buffer[3];
  memset(buffer, 0, max_size); // remember to #include "string.h"

Using a C++ std::array (hdr.serialize(b1.data(),offset)):

• std::array<char,3> b1 = {0}; // b1.data() provides direct access to its underlying C-style array

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

HW buffer – heap allocation

Using a C-style array:

• `char* buffer = new char[3]; // remember the delete []!!`

• Better not to use C array with smart pointers, as you need to set a custom deleter for the shared pointer (we do not address it in this course), better using C++ std::array

Using a C++ std::array (best solution):

• `auto b1 = std::make_shared<std::array<char,3>>(); // b1→data()` provides direct access to its underlying C-style array

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)


---

<!-- Pagina 5 -->

std::cout and uint_fast8_t

If I print the value of an uint_fast8_t I get strange results.

• Why?

---

**Immagini estratte:**

![Figura estratta 1](p05_img01.jpg)


---

<!-- Pagina 6 -->

What is a socket?

• In a Unix system, a socket is a way to speak to other programs using standard Unix file descriptor

• A socket performs process to process communication (transport layer):

  • the network layer delivers a message to the right host (host to host communication),
  • the transport delivers it to the appropriate process (process to process communication).

• Def: a file descriptor is an integer associated with an open file

  • that file can be a network connection, a FIFO, a pipe, a terminal, a real on-the-disk file, or just about anything else (everything in Unix is a file).

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)


---

<!-- Pagina 7 -->

What is a socket? – syscall and port

• socket() system routine creates the socket file descriptor
• send() and recv() socket calls are used to communicate through the socket
  • NOTE: they are system call, and it is pure C, not C++!

• A socket is composed by a copy `<ip_address,port>`, where
  • ip_address is the ip address of the host
  • port is the port in which the process of host is listening
  • use only port > 1024, the others are well-known ports (for example, 21 = ftp, 22=ssh 80=http)

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)


---

<!-- Pagina 8 -->

What is a socket? Client and Server

• If a server program runs a host with ip ip1 listening at port port1, port1 must be known to the clients

• A client program runs in a different or in the same host and accesses the server, as it knows the server ip and port number.

Clients and servers are programs, not machines!

• In a host many client and many server programs can run simultaneously

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)


---

<!-- Pagina 9 -->

Socket types

• A DATAGRAM socket (SOCK_DGRAM) is the socket for UDP
  • Fast, unreliable, packets can arrive out of order
  • If a packet (datagram) arrives, it arrives correctly
  • Connectionless
  • Used for audio and video streams, multiplayer games

• A STREAM socket (SOCK_STREAM) is the socket for TCP
  • Two-way connected communication streams
  • Reliable: reordering of packets, retransmissions, error free.
  • Used for file transfer (ftp), http, ssh

• A RAW Socket: very powerful and low level. They exist, but they are not topic of this course.
  • very specific and advanced stuff

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Linux: check IP address of your machine

```bash
// old distros way: in new distro install net-tools:
// sudo apt install net-tools
// DO NOT INSTALL NOTHING IN Da LAB!! (just in your PC)
ifconfig

eno1 Link encap:Ethernet  HWaddr 98:90:96:d9:e2:c4
inet addr:147.162.97.6  ...
```

// new distros way

ip addr

2: eno1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 ...
link/ether 98:90:96:d9:e2:c4 brd ff:ff:ff:ff:ff:ff
inet 147.162.97.6/24 brd 147.162.97.255 scope ...
```

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Linux: ping a remote machine

```bash
// ping is used to check the reachability of a host on
// an IP network, and to measure the round-trip time

ping 147.162.97.5

PING 147.162.97.5 (147.162.97.5) 56(84) bytes of data.
64 bytes from 147.162.97.5: icmp_seq=1 ttl=64 time=7.91 ms
64 bytes from 147.162.97.5: icmp_seq=2 ttl=64 time=1.46 ms
64 bytes from 147.162.97.5: icmp_seq=3 ttl=64 time=1.50 ms
64 bytes from 147.162.97.5: icmp_seq=4 ttl=64 time=1.47 ms
```

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

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


---

<!-- Pagina 13 -->

Da lab Firewall

• In general, the Da lab local Firewall (a software that controls the network traffic) does not allow you to connect via sockets between different hosts in the Da LAN.

• HOWEVER, we’ve been allowed to open both TCP and UDP port 55555, therefore try to perform a chat with netcat to communicate with your neighbour

• NOTE: during the exam the port will be close, but you can use sockets locally

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Include from standard c library

```c
#include <string.h> // all c_string and memory
manipulation:
• memmove, memcopy, memset, ...
```

#include <netinet/tcp.h> // includes:
• the tcphdr struct and TCP macros

#include <arpa/inet.h> // includes:
• the struct in_addr,
• the functions: htonl, htons, ntohl, ntohs
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Include from standard c library - 2

```c
#include <sys/socket.h> // includes:
• the socketaddr struct,
• the socket macros: SOCK_DGRAM, SOCK_STREAM, ...
#include <netinet/in.h> // includes:
• the socketaddr_in struct used to store addresses for the Internet protocol family, must be cast to socketaddr struct for use with socket
#include <unistd.h>// includes:
• the POSIX operative system API syscall wrapper for I/O
  • read, write and close
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p15_img01.jpg)


---

<!-- Pagina 16 -->

Open a sockets in C++

```c
int socket(family,type,protocol);
• @return socket file descriptor. If < 0 operation failed
• @family we always use AF_INET = address type IPv4
  • These families are defined in <sys/socket.h>
• @type SOCK_DGRAM = UDP socket,
  SOCK_STREAM = TCP socket
• @protocol: always set it to 0 for the internet protocol (IP)

int udp_socket_fd = socket(AF_INET,
  SOCK_DGRAM,0)

int tcp_socket_fd = socket(AF_INET,
  SOCK_STREAM,0)
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p16_img01.jpg)


---

<!-- Pagina 17 -->

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

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)


---

<!-- Pagina 18 -->

Functions for Internet addresses - 2

• `inet_addr()` converts a string in the standard IPv4 dotted decimal notation, to an Internet address.
  • `inet_pton()` similar, but also for IPv6
  ```python
  dest_addr.sin_addr.s_addr =
  inet_addr("192.168.100.1");
```

• `inet_ntoa()` converts the Internet host address to a string in the Internet standard dot notation (IPv4).
  • `inet_pton()` similar, but also for IPv6
  ```python
  char* ip = inet_ntoa(dest_addr.sin_addr);
```

---

**Immagini estratte:**

![Figura estratta 1](p18_img01.jpg)


---

<!-- Pagina 19 -->

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

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p19_img01.jpg)


---

<!-- Pagina 20 -->

Bind a server sockets in C++ - 2

```c
int sckfd = socket(AF_INET, SOCK_STREAM, 0)
struct sockaddr_in my_addr = {0}; /**< init it to 0 */
my_addr.sin_family = AF_INET; /**< Family IPv4 */
my_addr.sin_port = htons(recv_port); /**< Sets socket port*/
my_addr.sin_addr.s_addr = htonl(INADDR_ANY);
 /**< all interfaces */
if (bind(sckfd, (struct sockaddr*) &my_addr,
 /**< bind it */
sizeof(my_addr)) < 0) {
/* ERROR: bind failed: exit */
}
```

Use a socket

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p20_img01.jpg)


---

<!-- Pagina 21 -->

Close a socket

• Always remember to close a socket
• close(socket_fd); closes a file descriptor, so that it no longer refers to any file and may be reused. All send/recv are unlocked.
  • More info: type in terminal man close
  • It destroys the socket and pending data are lost

• shutdown(socket_fd, flag); blocks communication in one (flag = SHUT_RD or flag = SHUT_WR) or both (flag = SHUT_RDWR) directions.
  • you will still be able to receive pending data the peer already sent

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p21_img01.jpg)


---

<!-- Pagina 22 -->

Send and receive buffer

• Send and receive data to and from socket by using a buffer
• The most usual way is to use a char array
• Operation needed before receive:
  1. `const size_t max_size = 256; // max size that can be received in a single read at maximum`
  2. `char rx_buf[max_size] = {0}; // create a rx buffer`
  3. `memset(buffer, 0, max_size); // before each read set all the buffer fields to 0 (not need at the first read)`
• Operation needed before transmit:
  1. `char tx_buf[256] = {0}; // create a tx buffer`
  2. `tx_buf = "ciao ciao"; // place the data to tx in the buffer`
  3. `size_t size2tx = 9; // save the size of the data to be tx`

---

**Immagini estratte:**

![Figura estratta 1](p22_img01.jpg)


---

<!-- Pagina 23 -->

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

![Figura estratta 1](p23_img01.jpg)


---

<!-- Pagina 24 -->

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


---

<!-- Pagina 25 -->

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


---

<!-- Pagina 26 -->

TCP listen

• TCP is a connected protocol, the **server** uses the bound socket as a listen socket to accept connection
• After creating and binding the listener socket **scklist**, the listen method is called to set how many client can be accepted together

```javascript
if (listen(scklist, 5) < 0) { // Accept max
  5 clients together
  //ERR
}
```

• In these basic examples we will always serve one client at a time
• To serve more clients you need multithreading.. We’ll see it next time

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)


---

<!-- Pagina 27 -->

TCP accept in C++ (server)

• TCP is a connected protocol, The **server** uses the bound socket as a listen socket to accept connection
  struct sockaddr_in remote_addr = {0};
  socklen_t addr_l = sizeof(remote_addr);
  int sockfd = accept(socklist, (struct sockaddr*) &remote_addr,
                        &addr_l);

• socklist is the listen socket used to accept incoming clients
  • This socket has already been created with socket(...) and bound with bind

• remote_addr is used to get info of the remote addr

• sockfd is the new socket generated by accept, used for send and receive data with (and only with) the accepted client

• The client connects itself to the server

---

**Immagini estratte:**

![Figura estratta 1](images/p27_img01.jpg)


---

<!-- Pagina 28 -->

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


---

<!-- Pagina 29 -->

TCP receive in C++

You can use both recv() or read()
```c
int recv_bytes = recv(sckfd, buffer, max_size, 0);
```

• Flag always is set to 0: other values are for advanced features
• recv_bytes < 0 means an error occurred
• Specific for socket
```c
int recv_bytes = read(sckfd, buffer, max_size);
```

• recv_bytes < 0 means an error occurred
• Equivalent to recv with flag = 0
• Used also for file

---

**Immagini estratte:**

![Figura estratta 1](images/p29_img01.jpg)


---

<!-- Pagina 30 -->

TCP send in C++

You can use both send() or write()
```c
int sent_bytes = send(sckfd, buffer, size2tx, 0);
```

• Flag always is set to 0: other values are for advanced features
• sent_bytes < 0 means an error occurred
• Specific for socket
```c
int sent_bytes = write(sckfd, buffer, size2tx);
```

• sent_bytes < 0 means an error occurred
• Equivalent to send with flag = 0
• Used also for file

---

**Immagini estratte:**

![Figura estratta 1](images/p30_img01.jpg)


---

<!-- Pagina 31 -->

SIGPIPE signal (send or write)

```c
int sent_bytes = send(sckfd, buffer, max_size, 0);
```

• sent_bytes < 0 means an error occurred (e.g., the remote host disconnected, the NIC has a fault, the Ethernet cable disconnected, etc)

• SIGPIPE signal is sent to the process in case you are trying to write in a socket and has a hardware fault (the NIC has a fault, the Ethernet cable disconnected, WiFi goes down,...)
  • the process terminates!

• We don’t want this behavior: a server should handle temporary hardware faults without interrupt its service

• Def: a signal (POSIX) is an asynchronous notification sent to a process or to a specific thread within the same process in order to notify it of an event that occurred.

---

**Immagini estratte:**

![Figura estratta 1](images/p31_img01.jpg)


---

<!-- Pagina 32 -->

POSIX Signals

• When a signal is sent, the operating system interrupts the target process' normal flow of execution to deliver the signal. If the process has previously registered a signal handler, that routine is executed. Otherwise, the default signal handler is executed.

• Most common signals:
  • SIGABRT // abort the process, usually caused by another signal
  • SIGFPE // erroneous arithmetic operation (division by 0)
  • SIGINT // interrupt the process from terminal (CTR+C)
  • SIGKILL // terminate immediately the process (cannot be caught)
  • SIGPIPE // write to a pipe (mechanism for inter-process communication) without a process connected to the other hand
  • SIGSEGV // invalid virtual memory reference or segmentation fault
  • SIGTERM // identical to SIGINT

---

**Immagini estratte:**

![Figura estratta 1](images/p32_img01.jpg)


---

<!-- Pagina 33 -->

Avoid SIGPIPE killing the process

• Solution 1: ignore the signal
```c
#include <signal.h>
#include <cstring>
main() {
    struct sigaction act; // structure that contains the handler
    memset(&act, '\0', sizeof(act));
    act.sa_handler = SIG_IGN; // handler that ignores the signal
    if (sigaction(SIGPIPE, &act, NULL) < 0) { // set the handler
        std::cerr << "sigaction failed" << std::endl;
// to SIGPIPE
    }
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p33_img01.jpg)


---

<!-- Pagina 34 -->

Solution2: handling SIGPIPE

```c
#include <signal.h>
#include <cstring>

void function handleIt(int sig_id) {/*handle the signal sig_id*/}
main() {
    struct sigaction act;// structure used to handle the signals
    memset(&act, '\0', sizeof(act));
    act.sa_handler = &handleIt; // perform handleIt function
    if (sigaction(SIGPIPE, &act, NULL) < 0) {
        std::cerr << "sigaction failed" << std::endl;
    }
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p34_img01.jpg)


---

<!-- Pagina 35 -->

Set Socket Options

• Several options of the socket can be set (and get) with
• int res= setsockopt(socketfd, <level>,<opt_name>, *opt_val, opt_size));
• level = SOL_SOCKET to operate at socket API level (we always do this)
• res < 0 if error
• E.g., by default the kernel blocks a socket port for few minutes after the socket destruction: to reuse the port immediately use the option REUSEADDR

int option(1);

int res= setsockopt(socketfd, SOL_SOCKET, SO_REUSEADDR, (char*)&option, sizeof(option));

// res = 0 means success

---

**Immagini estratte:**

![Figura estratta 1](images/p35_img01.jpg)


---

<!-- Pagina 36 -->

# UDP Server example – setup

```c
int sckfd = socket(AF_INET, SOCK_DGRAM, 0); int
option = 1;
if (sckfd < 0){ /*ERR*/}
setsockopt(sckfd, SOL_SOCKET, SO_REUSEADDR,
             (char*)&option,
sizeof(option));
struct sockaddr_in my_addr = {0};
struct sockaddr_in srcaddr;
socklen_t addrlen = sizeof(srcaddr);
my_addr.sin_family = AF_INET;
my_addr.sin_port = htons(recv_port);
my_addr.sin_addr.s_addr = htonl(INADDR_ANY);
if (bind(sckfd, (struct sockaddr*) &my_addr,
sizeof(my_addr))<0) {
```

---

**Immagini estratte:**

![Figura estratta 1](images/p36_img01.jpg)


---

<!-- Pagina 37 -->

UDP Server example – exchange data

```cpp
char buffer[256] = {0};
size_t max_size = 256; int size = 0;
while((size = recvfrom(sckfd, buffer, max_size, 0,
    (struct sockaddr *) &srcaddr, &addrlen)) > 0)
{
    std::cout << buffer << std::endl; // print what rx
    if(sendto(sckfd, buffer, size, 0, (struct sockaddr*)
&srcaddr,
    addrlen) < 0) // send it
    { break; } // if error in send, exit the while
    memset(buffer, 0, max_size); // set buffer to zero for next
    "fresh"
    // read
}
close(skfd);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p37_img01.jpg)


---

<!-- Pagina 38 -->

UDP Client example - setup

```cpp
int sckfd = socket(AF_INET, SOCK_DGRAM, 0);
if (sckfd < 0){ /*ERR*/}
int option(1);
setsockopt(sckfd, SOL_SOCKET, SO_REUSEADDR,
             (char*)&option, sizeof(option));
struct sockaddr_in dest_addr = {0};
dest_addr.sin_family = AF_INET;
const char* dest_ip = "192.168.100.12";
int dest_port = 55555;
dest_addr.sin_port = htons(dest_port);
if (inet_pton(AF_INET, dest_ip, &dest_addr.sin_addr)
≤ 0) {
    /*conversion host_ip to AF_ADDRESS FAILED*/
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p38_img01.jpg)


---

<!-- Pagina 39 -->

UDP Client example – exchange data

```c
char buffer[256] = "ciao";
size_t max_size = 256;
while(sendto(sckfd, buffer, max_size, 0, (struct
sockaddr*) &
&dest_addr, sizeof(dest_addr )) > 0) {// send it
memset(buffer, 0, max_size); // set buffer to zero for next
read
socklen_t addrlen = sizeof(dest_addr);
if(recvfrom(sckfd, buffer, max_size, 0, // receive it and
get
(struct sockaddr *) &dest_addr, &addrlen) < 0) //
sender addr
{ break; } // if error in send, exit the while
std::cout << buffer << std::endl; // print what rx
}
close(skfd);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p39_img01.jpg)


---

<!-- Pagina 40 -->

TCP server example - setup

```cpp
int scklist = socket(AF_INET, SOCK_STREAM, 0);
if (scklist < 0){ /*ERR*/}
int option(1);
setsockopt(scklist, SOL_SOCKET, SO_REUSEADDR,
             (char*)&option, sizeof(option));
struct sockaddr_in my_addr = {0};
my_addr.sin_family = AF_INET;
int listen_port = 55555;
my_addr.sin_port = htons(listen_port );
my_addr.sin_addr.s_addr = htonl(INADDR_ANY);
if (bind(scklist,(struct sockaddr*)&my_addr,
sizeof(my_addr)) < 0)
{ /*err*/}
```

---

**Immagini estratte:**

![Figura estratta 1](p40_img01.jpg)


---

<!-- Pagina 41 -->

TCP server example – listen and accept

if (listen(scklist, 5) < 0) { // Accept max 5 clients together
    //ERR
}

struct sockaddr_in client_addr;

socklen_t addr_l = sizeof(client_addr);

int sockfd = accept(scklist, (struct sockaddr*) &client_addr, &addr_l);

if(sockfd < 0) {
    /*ERROR! CLOSE AND EXIT*/
}

std::cout << " connection from " << inet_ntoa(client_addr.sin_addr);

---

**Immagini estratte:**

![Figura estratta 1](p41_img01.jpg)


---

<!-- Pagina 42 -->

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

![Figura estratta 1](p42_img01.jpg)


---

<!-- Pagina 43 -->

TCP client example – setup

```cpp
int sckfd = socket(AF_INET, SOCK_STREAM, 0);
if (sckfd < 0){ /*ERR*/}
int option(1);
setsockopt(sckfd, SOL_SOCKET, SO_REUSEADDR,
             (char*)&option, sizeof(option));
struct sockaddr_in dest_addr = {0};
dest_addr.sin_family = AF_INET;
const char* dest_ip = "192.168.100.12";
int dest_port = 55555;
dest_addr.sin_port = htons(dest_port);
if (inet_pton(AF_INET, dest_ip, &dest_addr.sin_addr)
≤ 0) {
    /*conversion host_ip to AF_ADDRESS FAILED*/
}
```

---

**Immagini estratte:**

![Figura estratta 1](p43_img01.jpg)


---

<!-- Pagina 44 -->

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
