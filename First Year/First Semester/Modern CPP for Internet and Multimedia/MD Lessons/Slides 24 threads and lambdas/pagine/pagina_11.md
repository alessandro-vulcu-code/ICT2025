Threads disadvantages (vs process)

• If a thread crashes, the whole program crashes.
• If a process of a multi-process program crashes, instead, only that process needs to be restarted, while the other processes of the program keep working.
• A multi process program can easily become a distributed program, where different processes run in different machines
• A multithreading program, instead, cannot become a distributed program, as all the threads must run in the same machine
• In this course we do not address distributed programming, so we go with threads 😊

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)
