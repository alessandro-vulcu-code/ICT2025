# Riassunto Laboratorio 1: LoRaWAN con Arduino MKR WAN 1310

L'obiettivo del laboratorio è configurare un dispositivo **Arduino MKR WAN 1310** per connettersi alla rete **The Things Network (TTN)** tramite protocollo LoRaWAN, inviare messaggi periodici e visualizzarli correttamente decodificati sulla console di TTN.

## 1. Configurazione Hardware e Software
*   **Hardware**: Collegare la scheda Arduino MKR WAN 1310 al PC.
*   **Libreria**: Assicurarsi di aver installato la libreria **MKRWAN** (non la versione V2) nell'Arduino IDE.
*   **Codice Iniziale**: Caricare lo sketch `lab1.ino` (o l'esempio *FirstConfiguration* della libreria) per ottenere il **Device EUI** della scheda. Questo identificativo è univoco e serve per la registrazione su TTN.
    *   Nel codice `lab1.ino`, il DevEUI viene stampato nel Serial Monitor alle righe 30-31:
        ```cpp
        Serial.print("Your device EUI is: ");
        Serial.println(modem.deviceEUI());
        ```

## 2. Configurazione su The Things Network (TTN)
Per permettere al dispositivo di comunicare, è necessario registrarlo sulla piattaforma TTN:
1.  **Creare un'Applicazione**: Accedere alla console TTN e creare una nuova applicazione.
2.  **Registrare il Dispositivo**:
    *   All'interno dell'applicazione, cliccare su "Register End Device".
    *   Inserire il **DevEUI** letto dal Serial Monitor di Arduino.
    *   Generare (o copiare se fornito) l'**AppKey**.
    *   Per l'**AppEUI** (o JoinEUI), TTN V3 spesso usa tutti zeri o un valore specifico fornito dalla console.
3.  **Recuperare le Chiavi**: Copiare **AppEUI** e **AppKey** dalla console di TTN per inserirle nel codice Arduino.

## 3. Spiegazione del Codice Arduino (`lab1.ino`)
Il file `lab1.ino` gestisce la connessione LoRaWAN e l'invio dei dati.

### Setup (`setup()`)
*   **Inizializzazione**: Avvia la comunicazione seriale e il modem LoRa (`modem.begin(EU868)` per la banda europea).
*   **Credenziali**: Definisce le chiavi per la connessione OTAA (Over The Air Activation).
    *   **Nota Importante**: Le righe 34 e 35 contengono dei valori di esempio che **devono essere sostituiti** con quelli ottenuti da TTN:
        ```cpp
        appEui = "2102030608247211"; // Sostituire con il tuo AppEUI
        appKey = "38F37503EE2236A01DB430F00F3920A8"; // Sostituire con la tua AppKey
        ```
    *   *Attenzione*: Il commento alla riga 1 suggerisce di modificare le righe 42-43, ma è un refuso; le chiavi si trovano alle righe 34-35.
*   **Join**: Tenta la connessione alla rete con `modem.joinOTAA(appEui, appKey)`. Se fallisce (es. sei al chiuso lontano da un gateway), il programma si blocca in un loop infinito.

### Loop Principale (`loop()`)
*   **Attesa**: Il codice attende circa 60 secondi (ciclo `while` con `delay(500)` ripetuto 120 volte) prima di inviare un nuovo messaggio.
*   **Invio Dati**:
    1.  Seleziona un messaggio dall'array `messages` in modo ciclico:
        ```cpp
        String messages [4] = {"Welcome to IoT Lab", "This lab is amazing", ...};
        ```
    2.  Invia il messaggio testuale con `modem.print(...)`.
    3.  **Dato Extra**: Invia anche un byte aggiuntivo derivato dalla variabile `float a = 20.0f;` tramite `modem.write(a)`.
        ```cpp
        modem.print(messages[i%4]); // Invia la stringa
        modem.write(a);             // Invia il valore 20 come byte singolo
        ```
        Poiché `write` su Arduino invia un byte, il valore `20.0` viene trattato come intero `20` (che corrisponde a un carattere di controllo ASCII non stampabile, DC4).

## 4. Formattazione dei Dati (`formatter.js`)
Su TTN, i dati arrivano come byte grezzi (payload). Per renderli leggibili, si utilizza un **Payload Formatter**. Il file `formatter.js` contiene una funzione JavaScript che viene eseguita da TTN su ogni messaggio ricevuto.

```javascript
function decodeUplink(input) {
    return {
      data: {
        // Converte ogni byte del payload in un carattere ASCII e li unisce
        message: input.bytes.map(c => String.fromCharCode(c)).join('')
      },
      warnings: [],
      errors: []
    };
}
```

*   **Funzionamento**: La funzione prende l'array di byte (`input.bytes`), converte ogni byte nel corrispondente carattere ASCII (`String.fromCharCode(c)`) e li unisce in un'unica stringa.
*   **Risultato**: Nella sezione "Live Data" di TTN vedrai il messaggio testuale (es. "Welcome to IoT Lab") seguito da un carattere speciale (corrispondente al byte 20 inviato con `modem.write(a)`).

## Riepilogo Passaggi Operativi
1.  Apri `lab1.ino`, carica lo sketch e segnati il **DevEUI** dal monitor seriale.
2.  Registra il device su TTN usando quel DevEUI.
3.  Copia **AppEUI** e **AppKey** da TTN e incollale in `lab1.ino` (righe 34-35).
4.  Carica nuovamente lo sketch aggiornato su Arduino.
5.  Attendi il messaggio "Successfully Joined!".
6.  Copia il codice di `formatter.js` nella sezione "Payload Formatters" -> "Uplink" della console TTN.
7.  Osserva i messaggi decodificati nella tab "Live Data".
