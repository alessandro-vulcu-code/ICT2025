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
