Fields in structures: TCP header

```c
struct SimpleTcpHeader {
    int source_port : 16;
    int destination_port : 16;
    int sequence_number : 32;
    int ack_number : 32;
    char data_offset : 4; // 4 bit
    char : 3; // these are not used
    bool ns : 1;
    bool crw : 1;
    bool ece : 1;
    bool urg : 1;
    bool ack : 1;
    bool psh : 1;
    bool rst : 1;
    bool syn : 1;
    bool fin : 1;
    int window_size : 16;
    int checksum : 16;
    int urgent_pointer : 16;
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)
