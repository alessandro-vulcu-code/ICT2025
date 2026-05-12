Why do we need parallel programming?

• Multi threading (as well as multi-process) programming is used for parallel programming
• It is essential if your program needs to perform two or more operation in parallel
  • E.g.: a bidirectional chat

```cpp
//Thread 1: read from standard input and send to socket
while(true) {
    getline (std::cin, data);
    write(sk_fd, data, data.size());
}

//Thread 2: read from socket and print to standard output
while(true) {
    read(sk_fd, rx_data, MAX_SIZE);
    std::cout << rx_data << std::endl;
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)
