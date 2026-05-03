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
