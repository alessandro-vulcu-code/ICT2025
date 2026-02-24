# Analisi del file `tcp-client.cpp`
## Struttura del Codice

### 1. Inclusione delle Librerie

```cpp
#include <arpa/inet.h>   // Definizioni per operazioni su indirizzi internet (es. inet_pton, htons)
#include <iostream>      // Libreria standard di I/O C++ (std::cout, std::endl)
#include <netinet/in.h>  // Definizioni per protocolli internet (struct sockaddr_in, AF_INET)
#include <netinet/tcp.h> // Opzioni specifiche per il protocollo TCP
#include <string.h>      // Funzioni per la manipolazione di stringhe e memoria (es. memset)
#include <sys/socket.h>  // Funzioni fondamentali per i socket (socket, connect, send, recv)
#include <unistd.h>      // Funzioni standard POSIX (es. close)
```

### 2. Funzione Main

Il punto di ingresso del programma.

```cpp
int main(int argc, char **argv) {
```
-   `argc`: conta il numero di argomenti passati da riga di comando.
-   `argv`: array di stringhe contenente gli argomenti stessi.

#### Gestione Argomenti (IP e Porta)

```cpp
  // Se argc è 1 (nessun argomento extra), usa "127.0.0.1" (localhost).
  // Altrimenti, usa il primo argomento passato (argv[1]) come indirizzo IP.
  const char *dest_ip = argc == 1 ? "127.0.0.1" : argv[1];

  // Se ci sono più di 2 argomenti (programma + IP + Porta), usa il secondo come porta.
  // atoi converte la stringa in intero. Altrimenti usa 55555 come default.
  const int dest_port = argc > 2 ? atoi(argv[2]) : 55555;
```

#### Apertura del Socket

```cpp
  // Crea un endpoint per la comunicazione.
  // AF_INET: Specifica IPv4.
  // SOCK_STREAM: Specifica un socket TCP (flusso affidabile).
  // 0: Protocollo predefinito.
  int sckfd = socket(AF_INET, SOCK_STREAM, 0);

  // Controllo errori: se il descrittore del file è negativo, la creazione è fallita.
  if (sckfd < 0) {
    std::cout << "ERROR: OPEN SOCKET" << std::endl; // Stampa errore su stdout
    close(sckfd); // Chiude il descrittore (buona pratica anche se fallito)
    return -1;    // Termina il programma con codice errore -1
  }
```

#### Configurazione Opzioni Socket

```cpp
  int option(1);
  // Imposta l'opzione SO_REUSEADDR a livello SOL_SOCKET.
  // Permette di rilegare il socket a un indirizzo/porta ancora in stato TIME_WAIT.
  // Utile per evitare errori "Address already in use" durante i test rapidi.
  setsockopt(sckfd, SOL_SOCKET, SO_REUSEADDR, (char *)&option, sizeof(option));
```

#### Configurazione Indirizzo Destinazione

Prepara la struttura dati che contiene le informazioni su dove connettersi.

```cpp
  struct sockaddr_in dest_addr = {0}; // Inizializza la struttura a zero.
  dest_addr.sin_family = AF_INET;     // Imposta la famiglia di indirizzi a IPv4.

  // Imposta la porta. htons (Host TO Network Short) converte l'ordine dei byte
  // dall'ordine della macchina (solitamente Little Endian) a quello di rete (Big Endian).
  dest_addr.sin_port = htons(dest_port);

  // Converte l'indirizzo IP testuale (es "127.0.0.1") in formato binario di rete
  // e lo salva direttamente in dest_addr.sin_addr.
  if (inet_pton(AF_INET, dest_ip, &dest_addr.sin_addr) <= 0) {
    std::cout << "ERROR CONVERTING IP TO INTERNET ADDR" << std::endl;
    close(sckfd);
    return -2; // Errore conversione IP
  }
```

#### Connessione (Three-Way Handshake)

```cpp
  // Avvia la connessione TCP verso l'indirizzo e porta specificati.
  // È una chiamata bloccante che esegue l'handshake SYN -> SYN-ACK -> ACK.
  if (connect(sckfd, (struct sockaddr *)&dest_addr, sizeof(dest_addr)) < 0) {
    std::cout << "ERROR: CONNECT" << std::endl;
    close(sckfd);
    return -3; // Errore di connessione
  }
```

#### Trasmissione Dati

```cpp
  const size_t max_size = 512;        // Dimensione del buffer
  char buf[max_size] = "data to tx";  // Buffer inizializzato con una stringa
  size_t data_size = 10;              // Dimensione dei dati da inviare (lunghezza stringa)

  // Invia i dati attraverso il socket connesso.
  // sckfd: descrittore del socket.
  // buf: puntatore ai dati.
  // data_size: byte da inviare.
  // 0: flag.
  int sent_size = send(sckfd, buf, data_size, 0);
  
  // Controllo se l'invio è riuscito (send ritorna -1 in caso di errore)
  if (sent_size < 0) {
    std::cout << "ERROR: SEND" << std::endl;
    close(sckfd);
    return -4;
  }
```

#### Ricezione Dati

```cpp
  // Pulisce il buffer (lo riempie di 0) per prepararlo a ricevere nuovi dati.
  memset(buf, 0, max_size);

  // ESERCIZIO 2: Ricezione dei dati dal server.
  // recv legge i dati dal socket e li mette nel buffer.
  // Ritorna il numero di byte letti o -1 in caso di errore.
  int received_size = recv(sckfd, buf, max_size, 0);
  
  if (received_size < 0) {
    std::cout << "ERROR: RECV" << std::endl;
    close(sckfd);
    return -5;
  }
  
  // Stampa il buffer ricevuto su standard output.
  std::cout << buf << std::endl;
```

#### Chiusura

```cpp
  // Chiude il socket, terminando la connessione e liberando le risorse.
  close(sckfd);
}
```

----

# Analisi del file `tcp-server.cpp`

Questo documento fornisce una spiegazione dettagliata riga per riga del file sorgente `tcp-server.cpp`, che implementa un server TCP che riceve messaggi, li inverte e li rispedisce al mittente.

## Struttura del Codice

### 1. Inclusione delle Librerie

```cpp
#include <arpa/inet.h>   // Definizioni per operazioni su indirizzi internet (es. inet_ntoa, htons)
#include <iostream>      // I/O standard C++
#include <netinet/in.h>  // Definizioni per protocolli internet (struct sockaddr_in, AF_INET)
#include <netinet/tcp.h> // Opzioni specifiche per TCP
#include <string.h>      // Funzioni stringhe/memoria (es. memset)
#include <sys/socket.h>  // Funzioni base per i socket (socket, bind, listen, accept)
#include <unistd.h>      // Funzioni standard POSIX (es. close)
```

### 2. Funzione Ausiliaria: `revertBuffer`

Questa funzione serve a invertire l'ordine dei caratteri in un buffer (es. "ciao" -> "oaic").

```cpp
void revertBuffer(char *buf, size_t size) {
  // Itera fino alla metà del buffer.
  // Scambia l'elemento i-esimo con il corrispondente dalla fine (size - i - 1).
  for (int i = 0; i < size / 2; i++) {
    char temp = buf[i];
    buf[i] = buf[size - i - 1]; // Sovrascrive l'inizio con la fine
    buf[size - i - 1] = temp;   // Sovrascrive la fine con l'inizio salvato
    std::cout << buf[i] << std::endl; // Debug: stampa il carattere scambiato
  }
}
```

### 3. Funzione Main

```cpp
int main(int argc, char **argv) {
```

#### Gestione Argomenti (Porta di Ascolto)

```cpp
  // Se non vengono passati argomenti, usa la porta 55555.
  // Altrimenti, converte il primo argomento (argv[1]) in intero e lo usa come porta.
  const int listen_port = argc == 1 ? 55555 : atoi(argv[1]);
```

#### Creazione del Socket di Ascolto (Listening Socket)

```cpp
  // Crea il socket che useremo per accettare le connessioni in entrata.
  // AF_INET: IPv4
  // SOCK_STREAM: TCP
  int scklist = socket(AF_INET, SOCK_STREAM, 0);
  
  // Controllo errori
  if (scklist < 0) {
    std::cout << "ERROR: OPEN SOCKET" << std::endl;
    close(scklist);
    return -1;
  }
```

#### Opzioni Socket

```cpp
  int option(1);
  // Imposta SO_REUSEADDR per poter riutilizzare subito la porta dopo la chiusura del server.
  // Evita l'errore "Address already in use" se riavvii il server immediatamente.
  setsockopt(scklist, SOL_SOCKET, SO_REUSEADDR, (char *)&option, sizeof(option));
```

#### Binding (Associazione Indirizzo e Porta)

Configura l'indirizzo su cui il server ascolterà.

```cpp
  struct sockaddr_in my_addr = {0};
  my_addr.sin_family = AF_INET; // IPv4
  
  // Imposta la porta (convertita in network order con htons).
  my_addr.sin_port = htons(listen_port);
  
  // Accetta connessioni da qualsiasi interfaccia di rete disponibile (INADDR_ANY).
  // htonl (Host TO Network Long) converte l'indirizzo.
  my_addr.sin_addr.s_addr = htonl(INADDR_ANY);

  // Associa il socket 'scklist' all'indirizzo e porta specificati in 'my_addr'.
  if (bind(scklist, (struct sockaddr *)&my_addr, sizeof(my_addr)) < 0) {
    std::cout << "ERROR: BIND SOCKET" << std::endl;
    close(scklist);
    return -2;
  }
```

#### Listen (Messa in Ascolto)

```cpp
  // Mette il socket in modalità passiva (ascolto).
  // 1 rappresenta la lunghezza della coda delle connessioni in attesa (backlog).
  // Se arrivano più connessioni contemporaneamente mentre il server è occupato,
  // solo 1 verrà messa in attesa, le altre rifiutate.
  if (listen(scklist, 1) < 0) {
    std::cout << "ERROR: LISTEN SOCKET" << std::endl;
    close(scklist);
    return -3;
  }
```

#### Loop Principale: Accettazione e Gestione Clienti

Il server entra in un ciclo infinito per gestire i client uno alla volta (sequenzialmente).

```cpp
  struct sockaddr_in client_addr; // Struttura per salvare l'indirizzo del client che si connette
  socklen_t addr_l = sizeof(client_addr);

  while (true) {
    // 1. Accept: Blocca finché non arriva una connessione.
    // Ritorna un NUOVO file descriptor (sockfd) specifico per questa connessione.
    // Riempie client_addr con i dati del client (IP, porta).
    int sockfd = accept(scklist, (struct sockaddr *)&client_addr, &addr_l);
    
    // Controllo errore accept
    if (sockfd < 0) {
      std::cout << "ERROR: ACCEPT CONNECTION" << std::endl;
      // In questo codice, un errore di accept chiude tutto il server.
      close(sockfd);
      close(scklist);
      return -4;
    }
    
    // Stampa l'IP del client connesso (inet_ntoa converte l'IP binario in stringa).
    std::cout << "New connection from " << inet_ntoa(client_addr.sin_addr)
              << std::endl;

    // Preparazione buffer per ricezione dati
    const size_t max_size = 256;
    char buf[max_size] = {0};

    // 2. Receive: Legge i dati inviati dal client.
    int rcv_size = recv(sockfd, buf, max_size, 0);
    
    if (rcv_size < 0) {
      std::cout << "ERROR: RECV" << std::endl;
      close(sockfd);
      close(scklist); // Chiude il server in caso di errore di ricezione
      return -5;
    }
    
    std::cout << buf << std::endl; // Stampa messaggio ricevuto

    // 3. Elaborazione: Inverte il buffer ricevuto.
    revertBuffer(buf, rcv_size);

    // 4. Send: Invia il buffer invertito al client.
    int send_size = send(sockfd, buf, rcv_size, 0);
    if (send_size < 0) {
      std::cout << "ERROR: SEND" << std::endl;
      close(sockfd);
      break; // In questo caso esce solo dal loop, ma poi il main finisce
    }

    // 5. Close Client: Chiude la connessione con questo specifico client.
    // Il server torna all'inizio del 'while(true)' pronto per un nuovo client.
    close(sockfd);
    std::cout << "Connection closed" << std::endl;
  }
```

### 4. Chiusura Server

```cpp
  // Questa parte viene raggiunta solo se si esce dal while (es. break).
  close(scklist); // Chiude il socket di ascolto principale.
}
```

---

# Analisi del file `udp-client.cpp`

Questo documento fornisce una spiegazione dettagliata riga per riga del file sorgente `udp-client.cpp`, che implementa un client UDP.

## Struttura del Codice

### 1. Inclusione delle Librerie

```cpp
#include <arpa/inet.h>   // Definizioni per operazioni su indirizzi internet (es. inet_addr, htons)
#include <iostream>      // STD I/O C++ (std::cout, std::endl)
#include <netinet/in.h>  // Definizioni per protocolli internet (struct sockaddr_in, AF_INET)
#include <netinet/tcp.h> // Header TCP (anche se qui usiamo UDP, spesso incluso per completezza)
#include <string.h>      // Funzioni stringhe/memoria (es. memset)
#include <sys/socket.h>  // Funzioni base socket (socket, sendto, recvfrom)
#include <unistd.h>      // Funzioni POSIX (close)
```

### 2. Funzione Main

```cpp
int main(int argc, char **argv) {
```

#### Gestione Argomenti (IP e Porta)

```cpp
  // Se argc è 1, usa "127.0.0.1" (localhost) come default.
  // Altrimenti, usa il primo argomento (argv[1]) come IP di destinazione.
  const char *dest_ip = argc == 1 ? "127.0.0.1" : argv[1];

  // Se ci sono più di 2 argomenti, usa il secondo come porta.
  // Altrimenti usa 55555 come default.
  const int dest_port = argc > 2 ? atoi(argv[2]) : 55555;
```

#### Apertura del Socket (UDP)

```cpp
  // Crea un socket UDP.
  // AF_INET: IPv4.
  // SOCK_DGRAM: Specifica un socket datagram (non connesso, non affidabile).
  // Nota la differenza con TCP che usava SOCK_STREAM.
  int sckfd = socket(AF_INET, SOCK_DGRAM, 0);
  
  // Controllo errori
  if (sckfd < 0) {
    std::cout << "ERROR: OPEN SOCKET";
    close(sckfd);
    return -1;
  }
```

#### Opzioni Socket

```cpp
  int option(1);
  // Imposta SO_REUSEADDR come buona pratica.
  setsockopt(sckfd, SOL_SOCKET, SO_REUSEADDR, (char *)&option, sizeof(option));
```

#### Configurazione Indirizzo Destinazione

```cpp
  struct sockaddr_in dest_addr = {0};
  dest_addr.sin_family = AF_INET;     // IPv4
  dest_addr.sin_port = htons(dest_port); // Porta in network byte order

  // Converte l'indirizzo IP stringa in formato numerico (obsoleto, meglio inet_pton).
  // inet_addr restituisce INADDR_NONE (-1) in caso di errore.
  dest_addr.sin_addr.s_addr = inet_addr(dest_ip);
  
  if (dest_addr.sin_addr.s_addr < 0) {
    std::cout << "ERROR: conversion host_ip to AF_ADDRESS FAILED";
    close(sckfd);
    return -2;
  }
```

#### Trasmissione Dati (Senza Connessione)

A differenza del TCP, UDP non stabilisce una connessione (`connect`). I dati vengono inviati direttamente specificando il destinatario ogni volta.

```cpp
  const size_t max_size = 256;
  char buffer[max_size] = "ciao"; // Messaggio da inviare
  size_t size = 4;                // Lunghezza messaggio

  // sendto invia il messaggio.
  // Argomenti extra rispetto a send: puntatore a dest_addr e sua dimensione.
  // Questo perché il socket non "sa" a chi è connesso.
  if (sendto(sckfd, buffer, size, 0, (struct sockaddr *)&dest_addr,
             sizeof(dest_addr)) < 0) {
    std::cout << "ERROR SENDING" << std::endl;
    close(sckfd);
    return -3;
  }
```

#### Ricezione Dati

```cpp
  // Pulisce il buffer per la ricezione.
  memset(buffer, 0, max_size);

  // Variabile per memorizzare la lunghezza dell'indirizzo del mittente.
  // Deve essere inizializzata con la dimensione della struttura.
  socklen_t addr_len = sizeof(dest_addr);

  // recvfrom riceve dati e (opzionalmente) salva chi li ha mandati in dest_addr.
  // È bloccante come recv.
  int recv_size = recvfrom(sckfd, buffer, max_size, 0,
                           (struct sockaddr *)&dest_addr, &addr_len);
  
  if (recv_size < 0) {
    std::cout << "ERROR RECV" << std::endl;
    close(sckfd);
    return -4;
  }

  // Stampa il messaggio ricevuto.
  std::cout << buffer << std::endl;

  // Chiude il socket.
  close(sckfd);
}
```

---

# Analisi del file `udp-server.cpp`

Questo documento fornisce una spiegazione dettagliata riga per riga del file sorgente `udp-server.cpp`, che implementa un server UDP "echo" (o meglio, un server che dovrebbe convertire in maiuscolo e rispedire indietro i messaggi, se la funzione `toUpper` fosse implementata).

## Struttura del Codice

### 1. Inclusione delle Librerie

```cpp
#include <arpa/inet.h>   // Definizioni per indirizzi internet
#include <iostream>      // Input/Output C++
#include <netinet/in.h>  // Definizioni protocolli (sockaddr_in)
#include <netinet/tcp.h> // Header TCP (non strettamente necessario per UDP)
#include <string.h>      // Gestione stringhe e memoria
#include <sys/socket.h>  // Funzioni socket
#include <unistd.h>      // Funzioni sistema (close)
```

### 2. Funzione Ausiliaria: `toUpper`

Questa funzione è predisposta per convertire i caratteri del buffer in maiuscolo.
*Nota: Nel codice fornito la funzione è vuota e contiene solo suggerimenti per l'implementazione.*

```cpp
void toUpper(char *buf, size_t size) {
  // ESERCIZIO: Qui andrebbe implementata la logica per iterare
  // sul buffer e usare la funzione 'toupper(char)' su ogni elemento.
}
```

### 3. Funzione Main

```cpp
int main(int argc, char **argv) {
```

#### Gestione Argomenti (Porta di Ricezione)

```cpp
  // Se non ci sono argomenti (argc=1), usa la porta 55555.
  // Altrimenti, converte il primo argomento in intero e usa quello.
  const int recv_port = argc == 1 ? 55555 : atoi(argv[1]);
```

#### Creazione del Socket UDP

```cpp
  // Crea un socket UDP (SOCK_DGRAM) per IPv4 (AF_INET).
  int sckfd = socket(AF_INET, SOCK_DGRAM, 0);
  
  // Controllo errori
  if (sckfd < 0) {
    std::cout << "sckfd < 0";
    return -1;
  }
```

#### Opzioni Socket

```cpp
  int option(1);
  // Imposta SO_REUSEADDR per poter riutilizzare la porta immediatamente.
  setsockopt(sckfd, SOL_SOCKET, SO_REUSEADDR, (char *)&option, sizeof(option));
```

#### Binding (Associazione Indirizzo)

Configura l'indirizzo su cui il server riceverà i datagrammi.

```cpp
  struct sockaddr_in my_addr = {0}; // Indirizzo del server
  struct sockaddr_in srcaddr;       // Struttura per salvare l'indirizzo del mittente
  socklen_t addrlen = sizeof(srcaddr);
  
  my_addr.sin_family = AF_INET;
  my_addr.sin_port = htons(recv_port); // Porta in network byte order
  my_addr.sin_addr.s_addr = htonl(INADDR_ANY); // Ascolta su tutte le interfacce

  // Collega il socket alla porta e all'indirizzo specificati.
  if (bind(sckfd, (struct sockaddr *)&my_addr, sizeof(my_addr)) < 0) {
    std::cout << "bind socket address failed";
    return -2;
  }
```

#### Loop Principale: Ricezione e Risposta

Il server entra in un ciclo infinito per gestire i pacchetti in arrivo.
In UDP non c'è concetto di "connessione persistente", ogni pacchetto è indipendente.

```cpp
  const size_t max_size = 256;
  char buffer[max_size] = {0};

  while (true) {
    // 1. Receive: Riceve un datagramma.
    // recvfrom è bloccante.
    // buffer: dove mettere i dati.
    // srcaddr: viene riempita con l'indirizzo di chi ha mandato il pacchetto.
    // addrlen: dimensione della struttura srcaddr.
    int size = recvfrom(sckfd, buffer, max_size, 0, (struct sockaddr *)&srcaddr,
                        &addrlen);
    
    // Stampa l'IP del mittente
    char *ip = inet_ntoa(srcaddr.sin_addr);
    std::cout << ip << std::endl;
    // Stampa il contenuto del messaggio
    std::cout << buffer << std::endl;

    // 2. Elaborazione: Chiama la funzione per convertire in maiuscolo (se implementata).
    toUpper(buffer, size);

    // 3. Send Back: Invia la risposta allo stesso indirizzo da cui è arrivata (srcaddr).
    // Nota: sendto vuole l'indirizzo destinatario esplicitamente.
    if (sendto(sckfd, buffer, size, 0, (struct sockaddr *)&srcaddr, addrlen) <
        0) {
      std::cout << "sendto failed";
      continue; // Passa al prossimo pacchetto in caso di errore
    }

    // Pulisce il buffer per la prossima lettura
    memset(buffer, 0, max_size); 
  }

  // Chiusura socket (raggiungibile solo se si rompe il while)
  close(sckfd);
}
```

---

Per connettere al server da terminale con netcat:

#### TCP 
```bash
nc -l 55555 //server
nc <ip> <port>  //client
```

#### UDP
```bash
nc –lu 55555 // server
nc -u <ip> <port>  //client
```