Example of modular codebase

TCP module

interacts with the
which hides the
Congestion control implementation
Retransmissions interface
Retransmissions implementation
Header parsing implementation

In this way, the TCP program can use – for example – different congestion control algorithms without changing the code

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)
