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
