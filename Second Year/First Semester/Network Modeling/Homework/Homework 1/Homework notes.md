```bash
tshark -D #elenco interfaccie
```

scelgo la enp5s0 che dovrebbe essere quella per internet
prova di 10 minuti secondo guida, iniziata alle 16:23 e conclusa alle 16:33

```bash
udp.stream == 0 && ip.src == 192.168.3.7 && frame.number > 32864
```

tabella indicativa:

| Zoom open but all muted, capture running                |            30–60 s | Background flows and baseline                         |
| ------------------------------------------------------- | -----------------: | ----------------------------------------------------- |
| Meeting connected, microphone muted, camera off         |               60 s | Signaling, keepalives, and idle traffic               |
| Microphone on, camera off; alternate speech and silence |            2–3 min | Audio packet spacing and possible silence suppression |
| Camera on, speak normally                               |            3–5 min | Video size variation and packet clusters              |
| Camera off again                                        |               60 s | Whether the suspected video flow/rate disappears      |
