# Task 1.B — Firewall con Netfilter

Le prove sono state svolte sulla macchina Arch Linux che ospita Docker. Il modulo
`seedFilter` è stato caricato nel kernel dell'host. Sulla rete del laboratorio,
`10.9.0.1` è l'indirizzo dell'host Docker e `10.9.0.5` è quello del container
`HostA`.

## 1. Blocco delle query DNS

Il modulo di esempio registra `blockUDP` su `NF_INET_POST_ROUTING`. La regola
scarta i datagrammi UDP diretti a `8.8.8.8` sulla porta `53`.

Ho compilato il modulo e verificato la versione del kernel indicata nel file
`.ko`. Ho usato la stessa query prima e dopo il caricamento del modulo.

```bash
make
uname -r
modinfo -F vermagic ./seedFilter.ko

dig -4 @8.8.8.8 www.example.com +notcp +ignore +tries=1 +time=2

sudo insmod ./seedFilter.ko
dig -4 @8.8.8.8 www.example.com +notcp +ignore +tries=1 +time=2
sudo dmesg | tail -n 25
sudo rmmod seedFilter
```

Con la versione attuale del modulo, il comando di caricamento per
questa prova è `sudo insmod ./seedFilter.ko task=1`.

L'output salvato mostra che la query è scaduta:

```text
;; communications error to 8.8.8.8#53: timed out
;; no servers could be reached
```

Negli appunti compare un solo esito della query e l'estratto di `dmesg` contiene
solo righe `LOCAL_OUT` relative a connessioni TCP. La prova resta inconcludente
perché manca sia il confronto documentato con la query di controllo sia la riga
di drop per `8.8.8.8:53`.

## 2. Tracciamento dei cinque hook IPv4

Ho registrato `printInfo` su tutti e cinque gli hook IPv4. Per ogni
pacchetto, la callback registra hook, sorgente, destinazione e protocollo,
poi restituisce `NF_ACCEPT`. Gli estratti sotto mostrano le richieste ICMP
dei tre ping.

### Traffico destinato all'host Docker

```bash
docker compose exec -T HostA ping -c 1 -W 2 10.9.0.1
```

```text
[27100.950519] seedFilter: PRE_ROUTING 10.9.0.5 -> 10.9.0.1 (ICMP)
[27100.950535] seedFilter: LOCAL_IN 10.9.0.5 -> 10.9.0.1 (ICMP)
```

La richiesta di HostA attraversa `PRE_ROUTING` prima della decisione di routing.
Poiché la destinazione è un indirizzo dell'host Docker, il pacchetto prosegue
verso `LOCAL_IN` per la consegna locale.

### Traffico generato dall'host Docker

```bash
ping -c 1 -W 2 10.9.0.5
```

```text
[27106.506631] seedFilter: LOCAL_OUT 10.9.0.1 -> 10.9.0.5 (ICMP)
[27106.506641] seedFilter: POST_ROUTING 10.9.0.1 -> 10.9.0.5 (ICMP)
```

La richiesta è generata sull'host Docker e attraversa `LOCAL_OUT`. Passa
poi per `POST_ROUTING` prima di uscire verso HostA.

### Traffico inoltrato verso Internet

```bash
docker compose exec -T HostA ping -c 1 -W 2 1.1.1.1
```

```text
[27111.753191] seedFilter: PRE_ROUTING 10.9.0.5 -> 1.1.1.1 (ICMP)
[27111.753205] seedFilter: FORWARD 10.9.0.5 -> 1.1.1.1 (ICMP)
[27111.753210] seedFilter: POST_ROUTING 10.9.0.5 -> 1.1.1.1 (ICMP)
```

La richiesta entra da HostA tramite `PRE_ROUTING`. L'host Docker la inoltra
verso `1.1.1.1` tramite `FORWARD`. Il pacchetto attraversa `POST_ROUTING`
prima di uscire.

## 3. Blocco di ping e Telnet

Ho usato due callback distinte sullo stesso hook, `NF_INET_LOCAL_IN`, perché
le regole riguardano pacchetti destinati all'host Docker (`10.9.0.1`).

- `blockPing` scarta le richieste ICMP Echo.
- `blockTelnet` scarta i pacchetti TCP diretti alla porta `23`.

Ho avviato un listener TCP temporaneo sulla porta `23`. Quando accetta una
connessione, invia il messaggio `Lab TCP port 23` e chiude la connessione.
Ho ripetuto gli stessi comandi prima del caricamento, con `task=3` attivo
e dopo aver scaricato il modulo.

```bash
docker compose exec -T HostA ping -c 2 -W 2 10.9.0.1
docker compose exec HostA timeout 5 telnet 10.9.0.1 23
```

| Stato del modulo | Ping | Telnet |
|---|---|---|
| Prima del caricamento | 2 risposte su 2, perdita 0% | Connessione riuscita e messaggio `Lab TCP port 23` ricevuto. |
| Caricato con `task=3` | 0 risposte su 2, perdita 100% | Il client si ferma a `Trying 10.9.0.1...` fino al timeout di 5 secondi. |
| Dopo `sudo rmmod seedFilter` | 2 risposte su 2, perdita 0% | Connessione riuscita e messaggio `Lab TCP port 23` ricevuto. |

Entrambe le prove falliscono con il filtro caricato e tornano a funzionare
dopo la sua rimozione. La riga `Connection closed by foreign host.` nelle
prove riuscite indica che il listener ha chiuso una connessione già stabilita.
