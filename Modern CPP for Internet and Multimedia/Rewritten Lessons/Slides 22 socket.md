# Socket Programming

## Outline
- [Buffer Preparation](#buffer-preparation)
  - [Stack and Heap Buffers](#stack-and-heap-buffers)
  - [Printing Small Integer Types](#printing-small-integer-types)
- [What Is a Socket](#what-is-a-socket)
  - [Ports and File Descriptors](#ports-and-file-descriptors)
  - [Clients, Servers, and Socket Types](#clients-servers-and-socket-types)
- [Linux Network Tools](#linux-network-tools)
  - [Check Local IP](#check-local-ip)
  - [Ping and Netcat](#ping-and-netcat)
  - [Da Lab Firewall](#da-lab-firewall)
- [Socket Headers and Address Functions](#socket-headers-and-address-functions)
  - [Required Headers](#required-headers)
  - [Creating a Socket](#creating-a-socket)
  - [Internet Addresses](#internet-addresses)
- [Binding and Closing Sockets](#binding-and-closing-sockets)
  - [Bind](#bind)
  - [Close and Shutdown](#close-and-shutdown)
- [Sending and Receiving Data](#sending-and-receiving-data)
  - [Buffers for Send and Receive](#buffers-for-send-and-receive)
  - [UDP Receive and Send](#udp-receive-and-send)
  - [TCP Listen, Accept, and Connect](#tcp-listen-accept-and-connect)
  - [TCP Receive and Send](#tcp-receive-and-send)
- [SIGPIPE and POSIX Signals](#sigpipe-and-posix-signals)
  - [Ignoring SIGPIPE](#ignoring-sigpipe)
  - [Handling SIGPIPE](#handling-sigpipe)
- [Socket Options](#socket-options)
- [Client Server Examples](#client-server-examples)
  - [UDP Server](#udp-server)
  - [UDP Client](#udp-client)
  - [TCP Server](#tcp-server)
  - [TCP Client](#tcp-client)
- [Reference](#reference)

## Study Notes

### Buffer Preparation

Before using sockets, the lesson reviews how to prepare **byte buffers**. This matters because `send()`, `recv()`, `sendto()`, and `recvfrom()` work with raw memory areas, typically `char` arrays.

#### Stack and Heap Buffers

For serialization, an empty buffer should have all bits initialized to zero. An uninitialized C-style array contains **indeterminate values**.

```cpp
char buffer[3]; // WRONG, IT HAS RANDOM VALUES
char buffer[3] = {0,0,0};
char buffer[3] = {0}; // others will be set to 0
char buffer[3];
memset(buffer, 0, max_size); // remember to #include "string.h"
```

The first declaration is unsafe if the code expects zeros. `char buffer[3] = {0};` is the compact way to zero-initialize the whole array. `memset()` is useful when the buffer must be cleared again before a new receive operation.

With C++ containers, `std::array` is usually clearer:

```cpp
std::array<char,3> b1 = {0}; // b1.data() provides direct access to its underlying C-style array
```

`std::array` keeps the fixed-size array semantics but gives a safer C++ object. `b1.data()` returns the raw pointer needed by C socket calls.

For heap allocation with a C-style array:

```cpp
char* buffer = new char[3]; // remember the delete []!!
```

This should be avoided when possible because ownership is manual. If `delete[]` is forgotten, the memory leaks.

The slide warns that C arrays with smart pointers are not ideal in this course because a `shared_ptr` to an array needs a suitable deleter. A better course-level solution is to allocate a C++ object:

```cpp
auto b1 = std::make_shared<std::array<char,3>>(); // b1->data() provides direct access to its underlying C-style array
```

This uses `shared_ptr` to manage a `std::array`. The source used a corrupted arrow character; the intended C++ operator is `->`.

#### Printing Small Integer Types

If printing a value of type `uint_fast8_t` gives strange output, the usual reason is that very small integer types may be represented as character-like types by the implementation. Then `std::cout` may print a character instead of the numeric value.

For numeric output, cast explicitly:

```cpp
std::cout << static_cast<unsigned int>(value) << std::endl;
```

The exam point is that fixed-width or fast-width integer types are still typedefs to implementation-chosen fundamental types, so their stream behavior can depend on the underlying type.

### What Is a Socket

A **socket** is a Unix mechanism for communication between programs. In Unix-like systems, a socket is accessed through a **file descriptor**, just like files, pipes, terminals, and other I/O objects.

At the network stack level:

- the **network layer** delivers data to the right host;
- the **transport layer** delivers data to the right process on that host.

So sockets implement **process-to-process communication**.

#### Ports and File Descriptors

A file descriptor is an integer associated with an open I/O resource. For sockets, the system call:

```c
socket()
```

creates a socket file descriptor. Communication then happens through socket-related system calls such as:

```c
send()
recv()
```

These are **system calls** from the POSIX C API, not C++ abstractions.

A socket endpoint is identified by an address pair:

```text
<ip_address, port>
```

The **IP address** identifies the host. The **port** identifies the process/service on that host. For laboratory code, use ports greater than `1024`, because lower ports include well-known services such as FTP (`21`), SSH (`22`), and HTTP (`80`).

#### Clients, Servers, and Socket Types

A **server** is a program that listens on a known IP address and port. A **client** is a program that knows the server IP and port and contacts it. Clients and servers are programs, not machines: the same host can run many clients and many servers at the same time.

The main socket types in this course are:

- **Datagram sockets**, `SOCK_DGRAM`, used for UDP.
- **Stream sockets**, `SOCK_STREAM`, used for TCP.
- **Raw sockets**, which are low-level and outside the course scope.

UDP datagram sockets are **fast**, **connectionless**, and **unreliable**: packets can be lost or arrive out of order. If a UDP datagram arrives, it arrives correctly as a datagram. UDP is common in audio/video streams and multiplayer games.

TCP stream sockets provide **two-way connected communication**. TCP is reliable: it handles reordering, retransmission, and error-free delivery at the stream level. It is used by FTP, HTTP, SSH, and many application protocols.

### Linux Network Tools

#### Check Local IP

Older Linux distributions commonly used `ifconfig`:

```bash
# old distros way: in new distro install net-tools:
# sudo apt install net-tools
# DO NOT INSTALL ANYTHING IN DA LAB!! (just in your PC)
ifconfig

eno1 Link encap:Ethernet  HWaddr 98:90:96:d9:e2:c4
inet addr:147.162.97.6  ...
```

The source slide had a malformed code fence around the newer command. The intended modern command is:

```bash
ip addr

2: eno1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 ...
link/ether 98:90:96:d9:e2:c4 brd ff:ff:ff:ff:ff:ff
inet 147.162.97.6/24 brd 147.162.97.255 scope ...
```

Use this to find the IP address of the machine and the active network interfaces.

#### Ping and Netcat

`ping` checks whether a host is reachable on an IP network and measures round-trip time.

```bash
# ping is used to check the reachability of a host on
# an IP network, and to measure the round-trip time

ping 147.162.97.5

PING 147.162.97.5 (147.162.97.5) 56(84) bytes of data.
64 bytes from 147.162.97.5: icmp_seq=1 ttl=64 time=7.91 ms
64 bytes from 147.162.97.5: icmp_seq=2 ttl=64 time=1.46 ms
64 bytes from 147.162.97.5: icmp_seq=3 ttl=64 time=1.50 ms
64 bytes from 147.162.97.5: icmp_seq=4 ttl=64 time=1.47 ms
```

`netcat` is a networking utility for reading from and writing to TCP or UDP connections. It is useful to test whether a socket server/client idea works before writing code.

TCP netcat server and client:

```bash
nc -l 55555
nc 147.162.97.6 55555
```

The first command listens as a TCP server on port `55555`. The second command connects as a TCP client to that IP and port.

UDP netcat server and client:

```bash
nc -lu 55556
nc -u 147.162.97.6 55556
```

`-u` selects UDP. Without `-u`, netcat uses TCP.

#### Da Lab Firewall

The Da lab local firewall normally blocks socket connections between different hosts in the lab LAN. The course notes say TCP and UDP port `55555` were opened for experiments, so students can try a netcat chat with a neighbor.

During the exam, that port will be closed; sockets can still be tested locally, for example through loopback `127.0.0.1`.

### Socket Headers and Address Functions

#### Required Headers

The lesson lists several C/POSIX headers needed for socket programming.

```c
#include <string.h> // all c_string and memory manipulation:
// memmove, memcpy, memset, ...

#include <netinet/tcp.h> // includes:
// the tcphdr struct and TCP macros

#include <arpa/inet.h> // includes:
// the struct in_addr,
// the functions: htonl, htons, ntohl, ntohs
```

The source block is corrupted by PDF conversion: it uses bullets inside a C code fence and writes `memcopy`, but the standard function name is `memcpy`.

```c
#include <sys/socket.h> // includes:
// the sockaddr struct,
// the socket macros: SOCK_DGRAM, SOCK_STREAM, ...

#include <netinet/in.h> // includes:
// the sockaddr_in struct used to store addresses for the Internet protocol family,
// must be cast to sockaddr struct for use with socket

#include <unistd.h> // includes:
// the POSIX operating system API syscall wrappers for I/O:
// read, write and close
```

The source writes `socketaddr`; the standard type is **`sockaddr`**. `sockaddr_in` is the IPv4-specific address structure and is cast to `sockaddr*` when passed to generic socket functions.

#### Creating a Socket

The POSIX socket creation call is:

```c
int socket(family, type, protocol);
```

The return value is the socket file descriptor. If it is less than `0`, the operation failed.

For this course:

- `family` is `AF_INET`, meaning IPv4;
- `type` is `SOCK_DGRAM` for UDP or `SOCK_STREAM` for TCP;
- `protocol` is set to `0` for the Internet protocol default.

```c
int udp_socket_fd = socket(AF_INET, SOCK_DGRAM, 0);

int tcp_socket_fd = socket(AF_INET, SOCK_STREAM, 0);
```

The source version missed semicolons after the socket calls; the corrected form above shows the intended C/C++ syntax.

#### Internet Addresses

`struct sockaddr_in` stores IPv4 socket addresses and is defined in `<netinet/in.h>`.

```c
struct sockaddr_in my_addr = {0}; /**< init it to 0 */
```

Always initialize address structures before filling fields. This avoids garbage in unused fields.

Network protocols use **network byte order**, which is big endian. Hosts may use a different byte order, so conversion functions are required:

- `htonl`: host to network, unsigned long;
- `htons`: host to network, unsigned short;
- `ntohl`: network to host, unsigned long;
- `ntohs`: network to host, unsigned short.

```c
my_addr.sin_port = htons(listen_port);
```

Ports must be converted with `htons()` before being stored in `sin_port`.

`inet_addr()` converts an IPv4 dotted-decimal string to an Internet address. `inet_pton()` is similar and also supports IPv6.

```c
dest_addr.sin_addr.s_addr =
inet_addr("192.168.100.1");
```

`inet_ntoa()` converts an IPv4 address back to dotted-decimal string form. `inet_ntop()` is the more general modern counterpart.

```c
char* ip = inet_ntoa(dest_addr.sin_addr);
```

The source labels these examples as Python, but they are C socket API examples.

### Binding and Closing Sockets

#### Bind

`bind()` associates a socket with a local IP address, port, and interface. A server normally binds before receiving UDP datagrams or listening for TCP connections.

```c
my_addr.sin_addr.s_addr = htonl(INADDR_ANY);
```

`INADDR_ANY` means the socket accepts traffic on all available local interfaces: Ethernet, Wi-Fi, loopback, and so on.

To bind only to one interface, set a specific IP address:

```c
my_addr.sin_addr.s_addr =
inet_addr("127.0.0.1"); // loopback
```

Example bind setup:

```c
int sckfd = socket(AF_INET, SOCK_STREAM, 0);
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

The source misses a semicolon after `socket(...)`; the version above includes it. The important pattern is: create socket, fill `sockaddr_in`, cast it to `struct sockaddr*`, then call `bind()`.

#### Close and Shutdown

Always close sockets when they are no longer needed.

```c
close(socket_fd);
```

`close()` closes a file descriptor, so it no longer refers to a socket or file and the descriptor number may be reused. It destroys the socket; pending data can be lost.

```c
shutdown(socket_fd, flag);
```

`shutdown()` blocks communication in one or both directions without necessarily destroying the descriptor immediately:

- `SHUT_RD` disables further receiving;
- `SHUT_WR` disables further sending;
- `SHUT_RDWR` disables both.

The note in the slides is important: after shutting down writing, the process may still receive pending data already sent by the peer.

### Sending and Receiving Data

#### Buffers for Send and Receive

Socket I/O uses buffers. The common course approach is a `char` array.

Before receiving:

```cpp
const size_t max_size = 256; // max size that can be received in a single read at maximum
char rx_buf[max_size] = {0}; // create a rx buffer
memset(buffer, 0, max_size); // before each read set all the buffer fields to 0
```

The first initialization already clears the buffer. `memset()` is needed before later reads if old bytes must not remain visible after receiving a shorter message.

Before transmitting:

```cpp
char tx_buf[256] = {0}; // create a tx buffer
// place the data to transmit in the buffer
size_t size2tx = 9; // save the size of the data to be transmitted
```

The source writes `tx_buf = "ciao ciao";`, but arrays cannot be assigned that way after declaration. Use initialization, `strcpy`/`memcpy` with care, or a C++ string whose data is copied/sent explicitly.

#### UDP Receive and Send

UDP receive with a bound server uses `recvfrom()`:

```c
struct sockaddr_in srcaddr = {0}; // struct to get source address
socklen_t addrlen = sizeof(srcaddr); // variable with its size
int recv_bytes = recvfrom(sckfd, rx_buffer, max_size, 0,
                          (struct sockaddr *)&srcaddr,
                          &addrlen);
```

The flag is `0` in the course examples. `srcaddr` and `addrlen` are filled by `recvfrom()`, so the server can know which host sent the datagram. `recv_bytes == -1` means error.

UDP send uses `sendto()` with a destination address:

```c
const char* dest_ip = "192.168.100.123";
struct sockaddr_in dest_addr = {0}; // struct to set destination
dest_addr.sin_family = AF_INET; // use IPv4
dest_addr.sin_port = htons(dest_port); // set dest port
if (inet_pton(AF_INET, dest_ip, &dest_addr.sin_addr) <= 0) {
    /* ERR: conversion host_ip to AF_ADDR failed */
} // set dest IP
int w_bytes = sendto(sckfd, tx_buf, size2tx, 0,
                     (struct sockaddr*) &dest_addr,
                     sizeof(dest_addr)); // send
```

The source uses curly quotes and `<flag>`; the usual course value for the flag is `0`.

The core `sendto()` call is:

```c
int w_bytes = sendto(sckfd, tx_buf, size2tx,
                     0,
                     (struct sockaddr*) &dest_addr,
                     sizeof(dest_addr)); // send
```

If `w_bytes < 0`, a socket error occurred.

#### TCP Listen, Accept, and Connect

TCP is a **connected** protocol. The server creates and binds a listening socket, then calls `listen()`:

```c
if (listen(scklist, 5) < 0) { // Accept max 5 clients together
    // ERR
}
```

The second argument is the backlog: how many pending clients can wait to be accepted. In the basic examples, the server serves one client at a time. Serving multiple clients requires concurrency, such as multithreading.

The TCP server accepts a client with `accept()`:

```c
struct sockaddr_in remote_addr = {0};
socklen_t addr_l = sizeof(remote_addr);
int sockfd = accept(socklist, (struct sockaddr*) &remote_addr,
                    &addr_l);
```

`socklist` is the listening socket. `sockfd` is a **new socket** returned by `accept()` and is used to send and receive data with only that accepted client. `remote_addr` contains information about the client.

The TCP client connects to the server IP and port:

```c
struct sockaddr_in serv_addr = {0};
serv_addr.sin_family = AF_INET;
serv_addr.sin_port = htons(server_port);
if (inet_pton(AF_INET, serv_ip, &serv_addr.sin_addr) <= 0) {
    /* ERR */
}
if (connect(sockfd, (struct sockaddr*) &serv_addr,
            sizeof(serv_addr)) < 0) {
    /* connect ERROR */
}
```

After a successful `connect()`, the client uses `sockfd` to send and receive data with the server. The source used a non-C++ less-than-or-equal symbol; the intended operator is `<=`.

#### TCP Receive and Send

For TCP receive, the course shows both `recv()` and `read()`:

```c
int recv_bytes = recv(sckfd, buffer, max_size, 0);
```

The flag is `0` in these examples. `recv_bytes < 0` means error. `recv()` is socket-specific.

```c
int recv_bytes = read(sckfd, buffer, max_size);
```

`read()` is equivalent to `recv()` with flag `0` for this basic case, and it is also used for files.

For TCP send, the course shows both `send()` and `write()`:

```c
int sent_bytes = send(sckfd, buffer, size2tx, 0);
```

`sent_bytes < 0` means error. `send()` is socket-specific.

```c
int sent_bytes = write(sckfd, buffer, size2tx);
```

`write()` is equivalent to `send()` with flag `0` for this basic case, and it is also used for files.

Important exam caveat: TCP is a byte stream, so a single `send()` is not guaranteed to correspond to a single `recv()` of the same size. The slides do not go deeply into this, but robust TCP programs must handle partial sends and partial receives.

### SIGPIPE and POSIX Signals

When writing to a socket, hardware or connection failures can occur: the remote host may disconnect, the network interface may fail, the Ethernet cable may be unplugged, or Wi-Fi may go down.

```c
int sent_bytes = send(sckfd, buffer, max_size, 0);
```

If `sent_bytes < 0`, an error occurred.

On POSIX systems, trying to write to a broken connection can raise **SIGPIPE**. By default, SIGPIPE can terminate the process. A server should not die just because a temporary network fault happened.

A **signal** is an asynchronous notification sent to a process or thread to report an event.

Common POSIX signals from the slides:

- `SIGABRT`: abort the process, usually caused by another signal;
- `SIGFPE`: erroneous arithmetic operation, such as division by zero;
- `SIGINT`: interrupt from terminal, usually Ctrl+C;
- `SIGKILL`: terminate immediately and cannot be caught;
- `SIGPIPE`: write to a pipe/socket with no process connected at the other end;
- `SIGSEGV`: invalid virtual memory reference, segmentation fault;
- `SIGTERM`: termination request, similar in effect to an interrupt request.

#### Ignoring SIGPIPE

One solution is to ignore SIGPIPE:

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

The source is slightly malformed: `main()` has no return type, and the comment placement is broken. The essential operation is setting `act.sa_handler = SIG_IGN` and registering it with `sigaction(SIGPIPE, &act, NULL)`.

#### Handling SIGPIPE

Another solution is to install a custom handler:

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

The source declaration `void function handleIt` is malformed; the intended form is likely `void handleIt(int sig_id)`. The main concept is that the process registers a function to execute when SIGPIPE arrives.

### Socket Options

Socket options are set and read with `setsockopt()` and `getsockopt()`. The slide focuses on `setsockopt()`:

```c
int res = setsockopt(socketfd, level, opt_name, opt_val, opt_size);
```

For this course, `level` is usually `SOL_SOCKET`, meaning the option is at the socket API level. If `res < 0`, an error occurred.

One important option is **`SO_REUSEADDR`**. By default, the kernel may keep a port blocked for a few minutes after socket destruction. `SO_REUSEADDR` allows the program to reuse the port immediately.

```c
int option(1);

int res = setsockopt(socketfd, SOL_SOCKET, SO_REUSEADDR,
                     (char*)&option, sizeof(option));

// res = 0 means success
```

This is useful during development and for servers that may be restarted frequently.

### Client Server Examples

The final slides assemble the previous calls into UDP and TCP examples. Several source snippets are malformed by PDF extraction; the notes below preserve them while explaining the intended flow.

#### UDP Server

Setup:

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

The source cuts off the error-handling block and splits `int option = 1;` across two lines. The setup creates a UDP socket, enables address reuse, prepares the local address, and binds the socket to `recv_port`.

Exchange data:

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

This is a UDP echo server: it receives a datagram, prints it, sends the same bytes back to the source address, clears the buffer, and repeats. The source has `close(skfd)` but the socket variable is `sckfd`; that is likely a typo.

#### UDP Client

Setup:

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
<= 0) {
    /*conversion host_ip to AF_ADDRESS FAILED*/
}
```

The client creates a UDP socket, enables address reuse, and prepares the destination IP and port. The source used a non-C++ less-than-or-equal symbol; the intended operator is `<=`.

Exchange data:

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

This client sends a buffer to the UDP server, waits for a response, prints it, and repeats. The source is corrupted: it contains `& &dest_addr`, broken comments, and `close(skfd)` instead of `close(sckfd)`. The intended control flow is still clear.

#### TCP Server

Setup:

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

This creates the TCP listening socket, enables address reuse, binds to all local interfaces on port `55555`, and checks for bind errors.

Listen and accept:

```cpp
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
```

`listen()` turns the bound socket into a listening socket. `accept()` returns a new connected socket, `sockfd`, used for communication with the accepted client. `scklist` remains the listening socket.

Exchange data:

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

This receives data from the accepted client and sends the received bytes back. The source likely has typos: it prints `rx_buf` while the receive buffer is named `buf`, and uses `std::end` where `std::endl` was likely intended.

#### TCP Client

Setup:

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
<= 0) {
    /*conversion host_ip to AF_ADDRESS FAILED*/
}
```

This prepares a TCP client socket and destination address. The next step is `connect()`.

Connect and exchange data:

```cpp
if (connect(sckfd, (struct sockaddr*) &dest_addr, sizeof(dest_addr)) < 0) {
    /*ERROR: CLOSE AND EXIT*/
}
char buf[512] = "data to tx";
size_t data_size = 10;
int sent_size = send(sckfd, buf, data_size, 0);
if(sent_size<0) { /*ERROR: CLOSE AND EXIT*/}
memset(buf, 0, max_size); // set buffer to zero for next read
int rcv_size = recv(sockfd, buf, max_size, 0);
if(rcv_size < 0) { /*ERR!!!*/}
std::cout << buf << std::end;
close(sockfd);
```

This connects to the server, sends data, clears the buffer, receives the response, prints it, and closes the socket. The source likely mixes `sckfd` and `sockfd`; the same connected client socket should be used consistently. It also likely means `std::endl` instead of `std::end`.

### Reference

The lesson references **Beej's Guide to Network Programming - Using Internet Sockets**, Brian "Beej Jorgensen" Hall, Version 3.0.21, June 8, 2016.

## 5 Mins Questions

No 5 mins questions are present in the source material.

## Final Summary

Socket programming in this lesson is POSIX C-style programming used from C++. A socket is a **file descriptor** for process-to-process communication, identified by IP address and port. UDP uses `SOCK_DGRAM`, `sendto()`, and `recvfrom()` for connectionless datagrams. TCP uses `SOCK_STREAM`, with a server sequence of `socket()`, `bind()`, `listen()`, `accept()`, then `recv()`/`send()`, and a client sequence of `socket()`, address setup, `connect()`, then `send()`/`recv()`.

For the exam, focus on the lifecycle and responsibilities: initialize buffers, convert byte order with `htons()`/`htonl()`, fill `sockaddr_in`, bind servers, close sockets, check negative return values, handle SIGPIPE, and use `SO_REUSEADDR` when the same port must be reused quickly.
