# Riassunto Laboratorio 3: BLE e MQTT

Questo laboratorio esplora due protocolli fondamentali per l'IoT: **Bluetooth Low Energy (BLE)** e **MQTT**.

---

## Parte 1: Bluetooth Low Energy (BLE)

### Cos'è il BLE?
Il **Bluetooth Low Energy (BLE)** è una variante del Bluetooth progettata specificamente per l'Internet of Things (IoT). A differenza del Bluetooth "Classico" (orientato allo streaming audio/dati ad alta velocità), il BLE è ottimizzato per:
*   **Basso consumo energetico**: Ideale per dispositivi a batteria (wearable, sensori, beacon).
*   **Trasmissione dati sporadica**: Piccoli pacchetti di dati inviati a intervalli.

### Architettura e Stack
Il sistema BLE è diviso in due parti principali che comunicano tramite l'interfaccia **HCI (Host Controller Interface)**:
1.  **Host (Software)**: Gestisce i livelli superiori (GAP, GATT, L2CAP, SMP).
2.  **Controller (Hardware/Firmware)**: Gestisce la radio e il livello fisico (Link Layer + PHY).
3. **HCI = Host Controller Interface**: canale comando/evento tra Host e Controller; i comandi HCI vengono inviati dall'Host ed eseguiti all'interno del controller Bluetooth.

![MQTT QoS](ble_mqtt-006.png)

![BLE Stack](ble_mqtt-001.png)

### Ruoli e Funzionamento (GATT)
Il modello di comunicazione si basa su **Server** e **Client**:
*   **GATT Server (Periferica)**: Espone i dati sotto forma di **Servizi** e **Caratteristiche**. Esempio: uno smartwatch che espone il battito cardiaco.
*   **GATT Client (Centrale)**: Scansiona, si connette e legge/scrive i valori dal server. Esempio: uno smartphone.

Ogni servizio e caratteristica è identificato da un **UUID** (Universally Unique Identifier).

### Attività di Laboratorio: Simulazione Smartwatch
L'obiettivo è simulare l'interazione tra uno smartphone (Client) e uno smartwatch (Server) per leggere il nome del dispositivo e il battito cardiaco.

**Scenario:**
*   **Smartwatch**: Espone il *Device Information Service* (Nome) e l'*Heart Rate Service* (Battito).
*   **Smartphone**: Deve connettersi e recuperare questi dati.

**Passaggi Operativi:**
1.  Andare nella cartella `examples` del progetto Bumble.
2.  Eseguire lo script interattivo:
    ```bash
    python3 ble_interactive_lab.py
    ```
3.  Seguire il flusso GAP/GATT:
    *   **Scan**: Trovare il dispositivo.
    *   **Connect**: Stabilire la connessione.
    *   **Discover**: Scoprire i servizi disponibili.
    *   **Read**: Leggere i valori delle caratteristiche (es. UUID 0x2A37 per il battito cardiaco).

---

## Come funziona la simulazione
Questo codice Python è uno script educativo molto ben strutturato che simula l'intera interazione Bluetooth Low Energy (BLE) tra due dispositivi.

Non utilizza l'hardware Bluetooth fisico del tuo computer. Invece, utilizza una libreria chiamata **Bumble** per creare un ambiente virtuale in cui i pacchetti vengono scambiati direttamente in memoria.

Ecco i meccanismi principali con cui avviene la simulazione:

### 1. Il "Cavo Virtuale" (LocalLink)

Il cuore della simulazione si trova nella funzione `step_1_power_on_server`.
Il codice crea un oggetto `LocalLink()`:

```python
link = LocalLink()
```

Questo oggetto agisce come l'etere (l'aria) in cui viaggiano le onde radio. Invece di trasmettere segnali reali, i due dispositivi simulati sono collegati a questo stesso oggetto `link`. Quando un dispositivo "trasmette", passa semplicemente i dati a questo oggetto, che li consegna istantaneamente all'altro dispositivo.

### 2. Creazione dello Stack Virtuale

Il codice costruisce un intero stack Bluetooth software per due dispositivi distinti:

* **Controller:** Simula il chip fisico Bluetooth.
* `server_controller = Controller("server", link=link)`
* `client_controller = Controller("client", link=link)`
* Nota che entrambi sono collegati allo stesso `link`.


* **Host:** Simula il driver o il sistema operativo che gestisce il controller.
* **Device:** L'astrazione di alto livello che rappresenta il dispositivo (es. un fitness tracker o uno smartphone).

### 3. Simulazione dei Ruoli (GAP)

Lo script divide chiaramente i ruoli secondo il profilo **GAP (Generic Access Profile)**:

* **Server (Peripheral):** Viene configurato per fare **Advertising**.
* Definisce i dati di advertising (nome "Bumble Server", flag).
* Usa comandi HCI (Host Controller Interface) simulati come `LE Set Advertising Parameters` per iniziare a trasmettere la sua presenza sul `link`.


* **Client (Central):** Viene configurato per fare **Scanning**.
* Si mette in ascolto sul `link`.
* Quando il `link` trasporta il pacchetto di advertising del server, il client attiva l'evento `on_advertisement`.



### 4. Simulazione dello Scambio Dati (GATT)

Una volta connessi (fase `step_5_connection`), il codice passa al livello **GATT (Generic Attribute Profile)**. Qui simula la struttura dati interna di un dispositivo BLE:

* **Servizi e Caratteristiche:**
Il codice definisce manualmente i servizi, come se fosse il firmware di un vero dispositivo:
```python
# Esempio dal codice: Creazione del servizio Battito Cardiaco
heart_rate_measurement = Characteristic(...)
heart_rate_service = Service(GATT_HEART_RATE_SERVICE, [heart_rate_measurement])
server_device.add_service(heart_rate_service)

```


* **Protocollo ATT:**
Quando l'utente sceglie di leggere un dato (es. il battito cardiaco), lo script invia un vero pacchetto **ATT Read Request** attraverso il `link`. Il server virtuale riceve la richiesta, cerca il valore nella sua memoria e risponde con un **ATT Read Response**.

### 5. Interfaccia Educativa (HCI e Log)

La parte più interessante per l'apprendimento è come il codice "verbalizza" ciò che accade.
Usa funzioni come `print_protocol_message` per mostrarti cosa accadrebbe "sotto il cofano":

* **HCI (Host Controller Interface):** Mostra i comandi che la CPU invierebbe al chip Bluetooth (es. "Accenditi", "Scansiona").
* **ATT (Attribute Protocol):** Mostra i messaggi di richiesta/risposta dati (es. "Dammi il valore dell'handle 0x0012").

### Riassunto del Flusso

1. **Setup:** Crea due dispositivi virtuali in RAM.
2. **Discovery:** Il Server scrive dati nel `LocalLink`, il Client li legge (simulazione radio).
3. **Connection:** Si stabilisce un canale diretto logico.
4. **Interaction:** Il Client invia richieste di lettura byte, il Server risponde con byte predefiniti (es. `bytes([0x00, 75])` per 75 bpm).

È un eccellente esempio di come simulare protocolli di rete complessi in un ambiente controllato senza bisogno di hardware esterno o sniffer di pacchetti.

---

## Parte 2: MQTT (Message Queuing Telemetry Transport)

### Cos'è MQTT?
MQTT (Message Queuing Telemetry Transport) è un protocollo di messaggistica leggero basato sul paradigma **Publish/Subscribe**, ideale per reti con banda limitata e latenza elevata.

### Componenti Principali
*   **Broker (Server)**: Il cuore del sistema. Riceve tutti i messaggi e li smista ai client interessati.
*   **Client**: Possono essere **Publisher** (inviano dati) o **Subscriber** (ricevono dati).
*   **Topic**: Una stringa (es. `casa/cucina/temp`) che funge da indirizzo per i messaggi.
![[Pasted image 20251216094815.png]]


### Quality of Service (QoS)
MQTT definisce tre livelli di affidabilità per la consegna dei messaggi:

1.  **QoS 0 (At most once)**: "Fire and forget". Il messaggio viene inviato una sola volta senza conferme. Nessuna garanzia di consegna.
2.  **QoS 1 (At least once)**: Il messaggio viene sicuramente consegnato (conferma tramite PUBACK), ma potrebbe arrivare duplicato.
3.  **QoS 2 (Exactly once)**: Il livello più sicuro (e lento). Garantisce che il messaggio arrivi esattamente una volta tramite un handshake a 4 vie.
	1. PUBLISH
	2. PUBREC (Broker confirms reception)
	3. PUBREL (Client allows for release/forwarding)
	4. PUBCOMP (Broker confirms end of operations)



### Attività di Laboratorio

#### Esercizio 1: Pub/Sub Base
Utilizzando `mosquitto` (un popolare broker MQTT):
1.  Avviare il broker: `mosquitto -v`
2.  Avviare un subscriber su un terminale:
    ```bash
    mosquitto_sub -h localhost -t 'test/topic' -q 0
    ```
3.  Pubblicare un messaggio da un altro terminale:
    ```bash
    mosquitto_pub -h localhost -t "test/topic" -m "hello world" -q 0
    ```

#### Esercizio 2: QoS e Wildcard
Si sperimentano diversi livelli di QoS e l'uso di caratteri jolly (wildcard) nei topic:
*   **`#` (Multi-level wildcard)**: Corrisponde a qualsiasi numero di livelli (es. `casa/#` riceve `casa/cucina`, `casa/bagno/luce`).
*   **`+` (Single-level wildcard)**: Corrisponde a un solo livello.

**Osservazioni:**
*   I messaggi con QoS più alto hanno priorità.
*   I subscriber con wildcard `#` ricevono tutto il traffico che corrisponde al pattern, utile per il debugging o il logging globale.
![[Pasted image 20251218152336.png]]