### Question 1: CAN Bus Reverse Engineering

**Question:** Since you have taken the CPSec course and learned about the CAN bus, you want to develop something for your car. In particular, you want a small monitor to check the car's speed since the one in the dashboard is broken. You managed to access the CAN bus, but then you need to identify what packet is responsible for transmitting such information. How can you approach this reverse engineering task?

* [x] **monitor the traffic on the CAN bus looking at what packet changes when increasing or decreasing the vehicle's speed**
* [ ] monitor the speed of packets on the CAN bus looking at what packet changes faster than the others
* [ ] Monitor the traffic of a specific ECU to get information regarding the network configuration and its main features

---

### Question 2: Digital Twin

**Question:** In a Digital Twin

* [x] **the digital and physical models should be tightly coupled to avoid falling behind with the state generation process**
* [ ] The digital part does not need to receive information from the physical object is representing
* [ ] the unique purpose of the replica is anomaly detection

---

### Question 3: Platoon Attack

**Question:** Consider a platoon with N cars, where car  follows car . Denoting as  the location of car , we can denote the distance between car  and its preceding car as . Cars aim at maintaining a desired distance , and their controller computes the error as . Assume that the control rule is such that , the error value is updated accordingly, and that an attacker launches an attack able to modify the value of . What is the effect of an attacker reporting higher values for  compared to the actual ones?

*Note:  if ,  if ,  if *

* [x] **The car will speed up to try to maintain the constant headway and will result inot a crash**
* [ ] The attack has no effect, as the controller is able to mitigate this type of attacks
* [ ] The car will slow down and increase the distance to the preceding car, thus disrupting the platoon

---

### Question 4: CAN Bus Bit Series

**Question:** Given the following bit series of a message in the CAN bus, complete the attacker's bit series such that it increases the TEC of the victim (notice that bold numbers are for arbitration).
Victim: `0 1 0 1 0 0 1 1`
Attacker: `?`

* [ ] `0 0 0 0 0 0 1 1`
* [x] **`0 1 0 1 0 0 0 1`**
* [ ] `1 1 0 1 0 0 1 1`

---

### Question 5: Stuxnet

**Question:** Stuxnet is

* [x] **a malicious computer worm**
* [ ] a zero-day vulnerability of a SCADA system
* [ ] an anomaly detection system able to block malicious worms

---

### Question 6: LiDAR Saturation

**Question:** A saturation attack to a LiDAR

* [ ] precision of the time measurements of the sensors
* [x] **is a Denial of Service attack that leverages the limits in the linear region of sensors**
* [ ] is a Denial of Service attack that leverages the limits in the operational range of sensors

---

### Question 7: ECU Definition

**Question:** An ECU is

* [x] **an embedded systems that control one or more (sub)system(s) in a car**
* [ ] an in-vehicle network bus-based standard
* [ ] a counter value that can be used to implement the bus-off attack

---

### Question 8: CAN Bus Signalling

**Question:** The CAN bus uses

* [ ] a differential wired-OR signalling
* [x] **a differential wired-AND signalling**
* [ ] a current loop wired-AND signalling

---

### Question 9: ACC Scenario

**Question:** In an ACC scenario, an attacker can

* [ ] Deliver a replay attack by recording previously delivered instruction from the leader vehicle
* [ ] create a spike in the control signal and makes the vehicle accelerate
* [x] **leverage the existing communication channel between two vehicles to convey malicious information**

---

### Question 10: Drone Threat Model

**Question:** In the threat model related to drone technology

* [x] **the drone can be either a victim or an attacker**
* [ ] the drone is the target of malicious users and cannot be used to deliver attacks
* [ ] the attacker needs to have physical access to the drone

---

Ecco la trascrizione delle nuove domande e risposte caricate, formattate in Markdown. Come prima, la risposta selezionata nell'immagine è contrassegnata con `[x]`.

### Question 11: Geo-indistinguishability

**Question:** Geo-indistinguishability is

* [ ] a protocol that is vulnerable to DoS attacks by an external attacker
* [x] **a methodology that drones can use to preserve their location privacy**
* [ ] a methodology that an attacker can use to avoid being detected by drone detection systems

---

### Question 12: Optical Flow

**Question:** Optical flow refers to

* [x] **the pattern of apparent motion of objects, surfaces, and edges**
* [ ] an attack methodology used to hijack the drone's trajectory
* [ ] a feature detection algorithm to identify and target specific on-ground victims

---

### Question 13: Bus-off Attack

**Question:** In a bus-off attack

* [ ] The attacker needs to reverse engineer CAN bus packets
* [ ] The attacker needs to wait for the victim to be in error passive mode before delivering the attack
* [x] **The attacker can disconnect a node from the CAN bus**

---
Ecco la trascrizione delle domande e risposte contenute nelle nuove immagini caricate.

**Nota:** Per le immagini 13, 14 e 15 e le immagini 9 e 10 del nuovo set (2025), ho indicato la risposta selezionata con `[x]`. Per le altre domande del set "2024-2025" dove non appare nessuna selezione visibile (pallino blu), ho lasciato tutte le opzioni vuote `[ ]`.

### Question: Geo-indistinguishability (Photo 13)

**Question:** Geo-indistinguishability is

* [ ] a protocol that is vulnerable to DoS attacks by an external attacker
* [x] **a methodology that drones can use to preserve their location privacy**
* [ ] a methodology that an attacker can use to avoid being detected by drone detection systems

---

### Question: Optical Flow (Photo 14)

**Question:** Optical flow refers to

* [x] **the pattern of apparent motion of objects, surfaces, and edges**
* [ ] an attack methodology used to hijack the drone's trajectory
* [ ] a feature detection algorithm to identify and target specific on-ground victims

---

### Question: Bus-off Attack - Method (Photo 15)

**Question:** In a bus-off attack

* [ ] The attacker needs to reverse engineer CAN bus packets
* [ ] The attacker needs to wait for the victim to be in error passive mode before delivering the attack
* [x] **The attacker can disconnect a node from the CAN bus**

---

### Question: Bus-off Attack - Synchronization (Photo 1 2025)

**Question:** In order for the bus-off attack to be effective, the attacker achieves precise synchronization by

* [x] **detecting the ID of the packet of interest of the victim ECU**
* [ ] detecting in real-time the presence of the target packet
* [ ] leveraging the periodicity of messages and priorities

---

### Question: Industrial Plant Segmentation (Photo 2 2025)

**Question:** In an industrial plant, segmentation

* [ ] is only applied at the control network, as corporate network is already segmented
* [ ] refers to the process of grouping sensors according to their functionalities
* [x] **occurs at layer three thanks to a router device**

---

### Question: Reduced Headway Attack (Photo 3 2025)

**Question:** In a reduced headway attack

* [ ] the car ignores the predefined headway policy and closely follow the preceding vehicles
* [x] **the attacker injects a fake location in the communication and reduces the headway of a victim vehicle**
* [ ] the attacker causes the following (victim) vehicle to increase its distance from the preceding vehicle

---

### Question: CUSUM Statistic (Photo 4 2025)

**Question:** Let us consider the CUSUM statistic update, and consider a value , where the received signal is the actually received signal, the estimate is the output of the model and the last term is a compensation parameter. The nonparametric CUSUM statistic at time  is given by . Let us assume that , that , and that the detection rule triggers an alarm when  is greater than 10.
Assuming that the process is such that the received signal is constant = 1, if an attacker starts an attack against sensor  such that the reported measurement is always twice the expected value, then

* [ ] after 5 steps, the anomaly detector triggers the alarm
* [x] **after 6 steps, the anomaly detector triggers the alarm**
* [ ] the detector does not work as the compensation parameter is too high

---

### Question: ICS Sensor Attacks (Photo 5 2025)

**Question:** In attacks to the sensors used in an ICS, the attacker needs to

* [ ] launch a DoS attack as the only means to be effective
* [x] create attacks that lie within the operational range of sensors to be stealthy
* [ ] create attacks that lie outside the operational range of sensors to be stealthy

---

### Question: CACC (Photo 6 2025)

**Question:** In CACC

* [ ] the vehicle uses a radar and a controller to automate acceleration tasks
* [x] the vehicle uses information from the preceding vehicle in a feed-forward loop
* [ ] the sensed distance from the preceding car is reported to the controller, which acts on the speed to maintain a minimum safety distance

---

### Question: MEMS Attack (Photo 7 2025)

**Question:** In attack to MEMS, the attacker exploits

* [ ] the physical world to trick the sensor into detecting a phenomena that does not exist
* [ ] the digital world, by capturing the drone and modifying its firmware
* [ ] the physical world by tampering the hardware itself

---

### Question: SAE Level-4 (Photo 8 2025)

**Question:** A SAE Level-4 autonomous driving indicates

* [ ] full automation with the vehicle performing all driving tasks in all conditions
* [ ] conditional automation, where the vehicle can perform most of the driving task
* [ ] high automation where the vehicle performs all driving tasks under specific circumstances and in geofenced areas

---

### Question: LiDAR Saturation (Photo 9 2025)

**Question:** A saturation attack to a LiDAR

* [ ] precision of the time measurements of the sensors
* [x] **is a Denial of Service attack that leverages the limits in the linear region of sensors**
* [ ] is a Denial of Service attack that leverages the limits in the operational range of sensors

---

### Question: ECU Definition (Photo 10 2025)

**Question:** An ECU is

* [ ] an in-vehicle network bus-based standard
* [x] **an embedded systems that control one or more (sub)system(s) in a car**
* [ ] a counter value that can be used to implement the bus-off attack

---

Ecco il quiz basato esclusivamente sul contenuto del file di testo fornito (`February_2024__Questions.txt`). Ho contrassegnato con `[x]` le risposte indicate come corrette o definitive nel documento.

### Question 1: CAN Controller Functions

**Question:** What are the functions of the Can controller?

* [x] **Send serial bits and talk with the processor**

---

### Question 2: Bus Off Attack Strategy

**Question:** Bus off attack: why attacker doesn’t go to passive error mode?

* [x] **Because it decrease its error counter after the victim goes to error passive mode**
* [ ] Because it decrease its error counter after the victim goes to error active mode
* [ ] Because during the first phase a message gets correctly transmitted so TEC = TEC - 1

---

### Question 3: CAN Bus Voltage

**Question:** What is the Dominant bit voltage in CAN-bus?

* [x] **The bit is zero and its voltage is high (3.5 v and 1.5 v respectively)**
* [ ] The bit is one and its voltage is high (3.5 v and 1.5 v respectively)
* [ ] The bit is zero and its voltage is low (2.5 for both ends)

---

### Question 4: Optical Flow

**Question:** Considering Optical flow, what does the attacker exploit?

* [x] **The attacker exploits the optical flow assumption which is that the ground is stationary**
* [ ] The attacker exploits the optical flow assumption which is that the ground is moving

---

### Question 5: PLC Definition

**Question:** What is a PLC?

* [x] **Specialized computer used to automate functions**

---

### Question 6: IoT Network Packets

**Question:** Question about DIS and DIO packets in an IOT network

* [x] **triggers the sending of DIO packets**

---

### Question 7: AES-CTR Security

**Question:** (IOT security) Consider the aes-ctr. How does block counter work to increase security?

* [x] **block counter is increased every time to use multiple nonce values**

---

### Question 8: GPS Spoofing

**Question:** What is soft gps spoofing?

* [x] **the drone gradually locks to the spoofed gps signal**

---

---

### Question 10: Closed Control Loop

**Question:** In a closed control loop

* [x] **The reference value is compared with the process value**
* [ ] The reference value is compared with a value not generated by the process
* [ ] There’s no need to compare values