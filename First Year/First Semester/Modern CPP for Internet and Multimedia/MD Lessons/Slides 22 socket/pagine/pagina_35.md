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
