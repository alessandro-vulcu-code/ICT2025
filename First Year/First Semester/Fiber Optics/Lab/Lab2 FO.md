# 1.0 Introduzione e Obiettivi

La Dispersione dei Modi di Polarizzazione ($\text{PMD}$) è un fenomeno fisico che rappresenta un fattore limitante critico nelle comunicazioni ottiche ad alta velocità. Essa induce una distorsione del segnale trasmesso che può compromettere l'integrità dei dati, specialmente a velocità di trasmissione elevate. Comprendere e quantificare accuratamente la $\text{PMD}$ è quindi fondamentale per la progettazione e la qualificazione di reti ottiche performanti.

Lo scopo di questa relazione è documentare in dettaglio le metodologie sperimentali e le tecniche di analisi utilizzate per la caratterizzazione della $\text{PMD}$ in due campioni di fibra ottica con proprietà fisiche fondamentalmente diverse, evidenziando come la natura del dispositivo in esame determini l'approccio di misura più appropriato.

---

### 1.1 Contesto Teorico della PMD

Il comportamento della $\text{PMD}$ è governato dalla variazione dello stato di polarizzazione ($\text{SOP}$) del segnale ottico in funzione della sua frequenza angolare ($\omega$). Questa dinamica è descritta dall'equazione vettoriale fondamentale:

$$\dfrac{d\mathbf{s}}{d\omega} = \mathbf{\Omega} \times \mathbf{s}$$

dove $\mathbf{s}$ è il vettore di Stokes, che rappresenta lo stato di polarizzazione sulla sfera di Poincaré, e $\mathbf{\Omega}$ è il vettore di $\text{PMD}$. Per comprendere appieno il fenomeno, è essenziale definire i termini chiave:

- **Vettore di PMD ($\mathbf{\Omega}$):** Questo vettore tridimensionale descrive completamente l'effetto della $\text{PMD}$ a una data frequenza. La sua **direzione** identifica una coppia di stati di polarizzazione ortogonali noti come **Assi Principali di Polarizzazione ($\text{PSP}$)**, definiti come i due stati di polarizzazione in ingresso che si propagano attraverso la fibra senza modificare il proprio stato di polarizzazione in uscita. Il suo **modulo** corrisponde al Ritardo di Gruppo Differenziale.
- **Ritardo di Gruppo Differenziale ($\text{DGD}$, $\Delta\tau$):** Definito come il modulo del vettore di $\text{PMD}$ ($\mathbf{\Delta\tau = |\Omega|}$), il $\text{DGD}$ rappresenta la differenza di tempo di arrivo tra i due stati di polarizzazione principali. È la grandezza scalare che quantifica l'entità dell'effetto di dispersione istantaneo.



Dall'equazione fondamentale si evince che la misurazione della $\text{PMD}$ richiede necessariamente un'analisi accurata di come lo stato di polarizzazione $\mathbf{s}$ evolve al variare della frequenza del segnale ottico.

### 1.2 Obiettivi dell'Esperimento

L'attività di laboratorio si è posta i seguenti obiettivi specifici:

1. **Misurare il Ritardo di Gruppo Differenziale ($\text{DGD}$)** di una fibra a mantenimento di polarizzazione ($\text{PMF}$), caratterizzata da un comportamento deterministico e prevedibile.
2. **Stimare il $\text{DGD}$ medio** di una fibra ottica standard ("reale"), il cui comportamento aleatorio richiede un approccio di analisi statistico.

Questa relazione procederà descrivendo la strumentazione e la configurazione utilizzate per raggiungere tali scopi.

---

# 2.0 Configurazione Sperimentale

L'accuratezza delle misurazioni di $\text{PMD}$ dipende in modo critico da una configurazione sperimentale precisa e, soprattutto, meccanicamente ed termicamente stabile. La sezione seguente illustra i componenti chiave del banco di misura impiegato e i campioni di fibra analizzati.

## 2.1 Strumentazione

Il setup sperimentale è composto dai seguenti strumenti principali:

- **Sorgente Laser:** È stato utilizzato un laser a cavità esterna. Questa tecnologia permette di sintonizzare con elevata precisione la lunghezza d'onda di emissione ($\lambda$), una funzionalità indispensabile per eseguire la scansione in frequenza richiesta dalla misurazione della $\text{PMD}$.
- **Polarimetro:** Questo strumento analizza la luce trasmessa dalla fibra e ne misura lo stato di polarizzazione. Il risultato è visualizzato graficamente su una rappresentazione della sfera di Poincaré e numericamente attraverso le tre componenti del vettore di Stokes ($S_1, S_2, S_3$). Si nota che il display appare leggermente deformato, poiché si tratta di un monitor con aspect ratio $\mathbf{16:9}$, tecnologia non diffusa all'epoca della fabbricazione dello strumento.
- **Controllore di Polarizzazione:** Inserito nel percorso ottico, questo dispositivo permette di modificare manualmente lo stato di polarizzazione del segnale in ingresso alla fibra in esame.

#### Precauzioni Operative

È di fondamentale importanza sottolineare che la $\text{PMD}$ è un fenomeno sensibile alla fase. Qualsiasi perturbazione meccanica (contatto, vibrazione) o variazione termica ("drift termico") applicata alle fibre durante la misurazione altera la birifrangenza locale del mezzo, modificando la relazione di fase tra i modi di polarizzazione. Ciò invalida istantaneamente la ripetibilità della misura e, di conseguenza, l'intero set di dati acquisito.

## 2.2 Campioni in Analisi

L'esperimento è stato condotto su due tipologie di fibra ottica con caratteristiche strutturali opposte:

1. **Fibra a Mantenimento di Polarizzazione ($\text{PMF}$):** Questo campione, noto anche come "fibra panda", è ingegnerizzato con un'asimmetria interna controllata e costante lungo tutta la sua lunghezza. Questa proprietà strutturale ha una conseguenza diretta sul fenomeno della $\text{PMD}$: il vettore $\mathbf{\Omega}$ risulta costante al variare della frequenza ($\omega$).
2. **Fibra Ottica Standard ("Reale"):** A differenza della $\text{PMF}$, questa fibra presenta asimmetrie casuali e non controllate, introdotte come difetti intrinseci durante il processo di produzione. Di conseguenza, il suo vettore di $\text{PMD}$ $\mathbf{\Omega}$ non è costante, ma varia a sua volta in modo complesso con la frequenza ($\omega$).

Le diverse proprietà fisiche di questi due campioni impongono procedure di misura e analisi distinte, come descritto nelle sezioni successive.

---

# 3.0 Procedura di Misura e Acquisizione Dati

Le differenze strutturali tra la fibra $\text{PMF}$ e la fibra standard si traducono in comportamenti della $\text{PMD}$ radicalmente diversi, che richiedono procedure di acquisizione dati specifiche. La costante asimmetria ingegnerizzata della $\text{PMF}$ si traduce in un vettore di $\text{PMD}$ ($\mathbf{\Omega}$) costante, producendo un'evoluzione prevedibile e periodica dello $\text{SOP}$ che si presta a un'analisi deterministica. Al contrario, le asimmetrie casuali e incontrollate della fibra standard generano un vettore $\mathbf{\Omega}$ dipendente dalla frequenza, producendo un'evoluzione disordinata dello $\text{SOP}$ che necessita di un approccio di media statistica per estrarre un $\text{DGD}$ medio significativo.

## 3.1 Esperimento 1: Fibra a Mantenimento di Polarizzazione (PMF)

### 3.1.1 Principio di Misura

Nella fibra $\text{PMF}$, la costanza del vettore di $\text{PMD}$ $\mathbf{\Omega}$ in frequenza implica che la soluzione dell'equazione $d\mathbf{s}/d\omega = \mathbf{\Omega} \times \mathbf{s}$ descrive una rotazione uniforme del vettore di Stokes $\mathbf{s}$ attorno all'asse definito da $\mathbf{\Omega}$. Di conseguenza, al variare della frequenza della sorgente laser, lo stato di polarizzazione in uscita traccia una **traiettoria perfettamente circolare** sulla sfera di Poincaré.

Da questo modello discende una relazione diretta per la stima del $\text{DGD}$: il valore del $\text{DGD}$ ($\Delta\tau$) è l'inverso del periodo in frequenza ($\Delta F$) con cui lo stato di polarizzazione completa una rotazione di $\mathbf{360}$ gradi.

### 3.1.2 Procedura di Acquisizione

Prima di avviare l'acquisizione sistematica, è stata condotta una stima preliminare e grossolana del periodo di rotazione dello $\text{SOP}$. Variando manualmente la lunghezza d'onda del laser e osservando la traccia sulla sfera di Poincaré, è stato possibile determinare che un giro completo veniva compiuto in circa $\mathbf{3\ \text{nm}}$. Questa stima iniziale è stata fondamentale per definire l'intervallo di misura appropriato per l'acquisizione dettagliata.

Per la fibra $\text{PMF}$ è stata quindi seguita la seguente procedura sistematica:

1. **Impostazione Iniziale:** La sorgente laser è stata impostata a una lunghezza d'onda di partenza di $\mathbf{1400\ \text{nm}}$.
2. **Scansione:** La lunghezza d'onda è stata variata a passi discreti di $\mathbf{0.1\ \text{nm}}$.
3. **Intervallo di Misura:** I dati sono stati acquisiti su un intervallo totale di circa $\mathbf{6\ \text{nm}}$. Questo intervallo è stato scelto per coprire almeno due periodi completi di rotazione dello $\text{SOP}$, come determinato dalla stima preliminare.
4. **Registrazione Dati:** Per ogni passo di lunghezza d'onda ($\lambda$), sono stati registrati i valori delle tre componenti del vettore di Stokes: $S_1, S_2, S_3$.
5. **Monitoraggio:** Durante l'acquisizione è stato mantenuto un grafico in tempo reale delle tre componenti. Questa pratica consente l'identificazione immediata di punti dati anomali (ad es. errori di segno o di trascrizione che deviano dall'andamento sinusoidale atteso), garantendo così l'integrità del dataset prima del completamento della misura.

## 3.2 Esperimento 2: Fibra Ottica Standard ("Reale")

### 3.2.1 Principio di Misura

Il comportamento della fibra standard è marcatamente diverso. Poiché il suo vettore di $\text{PMD}$ $\mathbf{\Omega}$ varia con la frequenza ($\omega$), il vettore di Stokes $\mathbf{s}$ ruota attorno a un asse che, a sua volta, si muove sulla sfera di Poincaré. Il risultato è una **traiettoria disordinata e non periodica**.

In questo contesto, la $\text{PMD}$ viene descritta come un fenomeno **aleatorio ma deterministico**:

- È **aleatorio** nel senso che la sua evoluzione è imprevedibile.
- È **deterministico** perché, finché le condizioni ambientali (temperatura, stress meccanici) rimangono costanti, la traiettoria dello $\text{SOP}$ è perfettamente ripetibile.

In condizioni operative reali, le fibre sono soggette a variazioni continue. Il principio di **ergodicità** fornisce il collegamento cruciale tra la misura di laboratorio e il comportamento in campo: esso postula che una media calcolata in frequenza su un intervallo sufficientemente ampio fornisca una stima rappresentativa della media temporale che si osserverebbe sul lungo periodo. Questa misura di laboratorio, quindi, ha un valore ingegneristico pratico, poiché stima il $\text{DGD}$ medio a lungo termine che la fibra esibirebbe una volta installata, soggetta a variazioni stagionali per un periodo di almeno un anno.

### 3.2.2 Procedura di Acquisizione

Per la fibra standard è stata seguita la seguente procedura:

1. **Impostazione Iniziale:** La sorgente laser è stata impostata a una lunghezza d'onda di partenza di $\mathbf{1400\ \text{nm}}$.
2. **Scansione:** La lunghezza d'onda è stata variata a passi discreti di $\mathbf{0.1\ \text{nm}}$.
3. **Intervallo di Misura:** La scansione è stata eseguita su un intervallo di circa $\mathbf{5\ \text{nm}}$.
4. **Registrazione Dati:** Per ogni passo, sono stati registrati i valori delle componenti del vettore di Stokes $S_1, S_2, S_3$.

I dati raccolti con queste due procedure richiedono metodi di analisi specifici per estrarre una stima quantitativa del $\text{DGD}$.

---

# 4.0 Metodologie di Analisi e Stima del DGD

I dataset acquisiti per le due fibre, sebbene formalmente identici (serie di vettori di Stokes in funzione della lunghezza d'onda), devono essere processati con approcci di analisi radicalmente diversi, che riflettono la natura deterministica della $\text{PMF}$ e quella statistica della fibra standard.

## 4.1 Analisi per la Fibra PMF

L'obiettivo dell'analisi per la fibra $\text{PMF}$ è determinare il $\text{DGD}$ attraverso una stima precisa del periodo di rotazione dello stato di polarizzazione. L'acquisizione delle tre componenti quasi-periodiche ($S_1, S_2, S_3$) permette un'analisi più robusta rispetto a una semplice ispezione visiva dei massimi o minimi su un grafico. La procedura si basa sull'elaborazione numerica dei tre segnali acquisiti per estrarre il loro periodo fondamentale comune in termini di lunghezza d'onda ($\Delta\lambda$).

Questo valore deve poi essere convertito nel corrispettivo periodo in frequenza ($\Delta F$) utilizzando la seguente relazione approssimata, valida per piccole variazioni:

$$\Delta F \approx \left(\frac{c}{\lambda_0^2}\right) \Delta\lambda$$

dove $c$ è la velocità della luce nel vuoto e $\lambda_0$ è la lunghezza d'onda centrale dell'intervallo di misura.

Il $\text{DGD}$ ($\Delta\tau$) viene infine calcolato utilizzando la relazione fondamentale:

$$\Delta\tau = \frac{1}{\Delta F}$$

## 4.2 Analisi per la Fibra Standard

Per la fibra standard, la cui traiettoria dello $\text{SOP}$ è disordinata, si adotta una metodologia statistica nota come **"conteggio degli attraversamenti di livello"** (*level-crossing*), considerata uno standard industriale per la caratterizzazione di fibre con $\text{PMD}$ di natura stocastica. Questa tecnica si basa sull'analisi di un segnale ausiliario $\mathbf{T}$, calcolato a partire dai dati misurati:

$$\mathbf{T} = \frac{1}{2} + \mathbf{s} \cdot \mathbf{p}$$

dove $\mathbf{s}$ è il vettore di Stokes misurato e $\mathbf{p}$ è un vettore di Stokes normalizzato che rappresenta un polarizzatore ideale. Intuitivamente, un valore di $\text{DGD}$ più elevato causa un'evoluzione più rapida del vettore $\text{SOP}$ $\mathbf{s}$ con la frequenza sulla sfera di Poincaré. Quando questo vettore viene proiettato su un asse di polarizzazione fisso $\mathbf{p}$, la sua evoluzione più rapida si traduce in oscillazioni più frequenti del segnale $\mathbf{T}$, portando a un maggior numero di attraversamenti di livello in una data banda di frequenza.

Il processo di stima statistica del $\text{DGD}$ medio si articola nei seguenti passaggi:

a. **Generazione dell'Insieme:** Si genera un vettore $\mathbf{p}$ con componenti casuali (es. da una distribuzione gaussiana a media nulla) e lo si normalizza per renderlo un vettore di Stokes valido.

b. **Calcolo e Conteggio:** Si calcola il segnale $\mathbf{T}$ corrispondente all'intero intervallo di frequenza misurato e si conta il numero di volte che $\mathbf{T}$ attraversa un livello predefinito (es. $\mathbf{0.5}$).

c. **Stima Singola del DGD:** Sulla base di modelli statistici, il numero di attraversamenti contati in una data banda di frequenza fornisce una singola stima del $\text{DGD}$ medio.

d. **Costruzione dell'Insieme Statistico:** I passaggi $\mathbf{a-c}$ vengono ripetuti per un numero significativo di vettori $\mathbf{p}$ casuali. Ogni iterazione produce una stima differente del $\text{DGD}$, andando a costruire un insieme statistico di risultati.

e. **Calcolo Finale:** Il $\text{DGD}$ medio effettivo viene calcolato come la **media aritmetica** dell'insieme statistico di stime ottenuto.

Un criterio pratico per determinare un numero sufficiente di iterazioni consiste nel monitorare la varianza della stima del $\text{DGD}$: l'analisi può essere interrotta quando la varianza si stabilizza, indicando che ulteriori iterazioni non modificherebbero significativamente il risultato.

---

# 5.0 Conclusioni

L'attività sperimentale descritta in questa relazione ha permesso di caratterizzare la Dispersione dei Modi di Polarizzazione ($\text{PMD}$) in due tipologie di fibra ottica paradigmatiche, dimostrando come la struttura fisica del mezzo influenzi direttamente la natura del fenomeno e, di conseguenza, la metodologia di misura.

Sono state implementate e confrontate due strategie di analisi distinte, ciascuna adatta a una specifica tipologia di fibra:

- Un approccio **deterministico** per la fibra a mantenimento di polarizzazione ($\text{PMF}$), basato sull'analisi del periodo di rotazione dello stato di polarizzazione ($\text{SOP}$), il quale è direttamente correlato al valore del $\text{DGD}$ ($\Delta\tau$).
- Un approccio **statistico** per la fibra ottica standard, basato sul metodo del conteggio degli attraversamenti di livello (*level-crossing*), necessario per stimare un valore medio di $\text{DGD}$ a partire da un comportamento intrinsecamente aleatorio.

In conclusione, l'esperimento ha illustrato con efficacia la duplice natura, deterministica e stocastica, della $\text{PMD}$ e ha sottolineato l'importanza cruciale di selezionare la metodologia di caratterizzazione più appropriata in base alle proprietà del componente o del sistema ottico in esame.