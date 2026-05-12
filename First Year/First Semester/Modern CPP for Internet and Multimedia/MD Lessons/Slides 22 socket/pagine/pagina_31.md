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
