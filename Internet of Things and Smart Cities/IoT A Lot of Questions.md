# Lecture 5 - Bluetooth
**S3 Which class of Bluetooth is used by smart home devices?**
- Bluetooth Low energy

**S4 Describe very briefly the piconet and scatter netnetworks and the different states of their connected devices.**
- In Bluetooth Classic the devices are connected in piconets, which can be grouped also as scatternets. This is a star topology, in which a Master is designated among other slaves. In each piconet they can be up to 8 active devices and 255 sleep (parked) devices, which are syncronized but cannot take part to the communication until the active state.

**S8 What is the frequency-hopping spread spectrum in the radio layer (≡PHY layer)? What is the relevant dwell time?**
- The frequency hopping spectrum in BR/EDR is 79 channels for of 1 MHz, for a dwell time of 625 us

**S10 Describe the data communication (TDD) in the baseband layer(≡MAC layer). Which are the two steps of the connection procedure?**
- TDD is Time Division Duplex, which is used to manage physical channels. The two steps of the connection procedure are:
	- Inquiry: the master decides the frequency hopping and sends the request to a slave.
	- Paging: the slave sends his Device Access Code (DAC) to the slave

**S12 Which are the two types of communication in L2CAP?**
- The 2 types of communication in L2CAP are SCO (Syncronized Connection Oriented), which is Syncronized, focused more on faster transmission than integrity of the packets and every slave has a dedicated connection to the master, and ACO, which is Asyncronous and is more focused on integrity of the packet. If a part of the payload is corrupted, it will be sent again. 

**S16 Which are the differences between BLE and the BR/EDR (≡Bluetooth Classic)?**
- Bluetooth Low Energy is a more IoT oriented Bluetooth technology. It is focused on low energy consumption and it's indicated for devices that have small batteries (like smartwatches). BLE has 40 channels (2 GHz) instead of 79, it works at 2 Mbps to reduce the trasmission time (less consumption) and works only with GPSK modulation. Also, BLE uses a different topology (no piconets or scatternets). Instead, it uses a mesh profile, where the nodes are:
	- Relays
	- Low power nodes 
	- Managed flooding mechanisms

**S17 Lists theroles of nodes in BLE.**
- Broadcaster: only sends adverisement
- Observer: only receives advertisements
- Peripherial: send advertisements and accepts connections request (Slave)
- Central: remains open to receive advertisements and sends connection request (Master)

---

# IEEE 802.15.4
## General
S4 What does IEEE 802.15.4 define? Which communication technologies use it?
- IEEE 802.15.4 defines a new PHY and MAC layer for LowPAN (Low Personal Area Network) and it is focused on low energy consumption but with high throughput. Two technologies built on this are ZigBee and 6LowPAN.

S6 If the node acts as a PAN (personal area network) coordinator, which type is it?
- When a node acts as a PAN it is a FFD or Full Function Device. In this case, the node acts as a relay, it has a full PHY and MAC implementation and can use any topology.
- The other type of device is RFD or Reduces Function Device, which does not act as relay (depends on FFD), simpler PHY and MAC implementation and can use only star topology.

S4 List all the topologies of IEEE 802.15.4.
- Star, mesh and cluster tree, good for IoT and routing

S10 Explain how thebeacon-enable modeworks in the MAC layer.
- In the beacon-enable modes, the PAN coordinator sends periodically beacon frames, to create a structure named superframe. When the nodes doesn't receive the frames, it goes into sleep mode. Instead, during the active period, we have this division:
	- **Contention Access Period**: comunication managed by collision detection CSMA/CA
	- **Contention Free Protocol**: optional guaranteed time slots for specific devices.

S12 Which network protocol is used to control access to the channel for the non-beacon-enabled mode?
- CSMA/CA

