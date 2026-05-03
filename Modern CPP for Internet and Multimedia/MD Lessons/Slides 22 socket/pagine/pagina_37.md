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
