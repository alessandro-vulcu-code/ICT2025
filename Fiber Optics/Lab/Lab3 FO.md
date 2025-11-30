# 1. Introduzione e Obiettivi

Gli amplificatori a fibra drogata con erbio (EDFA, *Erbium-Doped Fiber Amplifier*) rappresentano una tecnologia fondamentale nei moderni sistemi di comunicazione ottica, consentendo la rigenerazione del segnale direttamente nel dominio ottico su lunghe distanze. La loro capacità di amplificare simultaneamente un ampio spettro di lunghezze d'onda li rende indispensabili nelle reti WDM (*Wavelength Division Multiplexing*). Questa relazione tecnica descrive in dettaglio la procedura sperimentale eseguita in laboratorio per la caratterizzazione di un EDFA, focalizzandosi sulla misurazione del guadagno e sull'analisi del rumore intrinseco.

---

### 1.1. Obiettivi dell'Esperimento

Le attività di laboratorio sono state condotte con i seguenti scopi principali:

* Misurare in modo sistematico la potenza del segnale ottico in ingresso ($P_{\text{in}}$) e in uscita ($P_{\text{out}}$) dall'amplificatore, al fine di determinarne il **Guadagno** ($G$) in diverse condizioni operative, dove $G$ è espresso come:
    $$G = \frac{P_{\text{out}}}{P_{\text{in}}}$$
* Osservare e quantificare il rumore di **Emissione Spontanea Amplificata (ASE, *Amplified Spontaneous Emission*)**, un fenomeno intrinseco al processo di amplificazione ottica.
* Comprendere la relazione fisica tra la presenza di un segnale di ingresso e la variazione del livello di rumore $\text{ASE}$, collegando le osservazioni sperimentali ai principi di funzionamento del sistema a tre livelli energetici.

Per interpretare correttamente i risultati ottenuti, è essenziale richiamare i principi teorici che governano il comportamento di questi dispositivi, come illustrato nella sezione successiva.

---

# 2. Richiami Concettuali

Una solida comprensione dei meccanismi fisici sottostanti è indispensabile non solo per eseguire correttamente la procedura sperimentale, ma soprattutto per analizzare in modo critico i dati raccolti e validare le conclusioni. Questa sezione riassume i due concetti chiave per la comprensione di questo esperimento: il principio di funzionamento dell'EDFA e la natura del rumore $\text{ASE}$.

## 2.1. Principio di Funzionamento: Il Sistema a Tre Livelli

Il funzionamento di un $\text{EDFA}$ si basa sul modello quantistico del **sistema a tre livelli energetici** degli ioni di erbio dispersi nella matrice di silice della fibra. Un laser di pompa eccita gli ioni portandoli a un livello energetico superiore ($E_3$). Da qui, essi decadono rapidamente a un livello metastabile ($E_2$). Quando un fotone del segnale di ingresso, con un'energia appropriata, interagisce con uno ione in questo stato eccitato, stimola il suo decadimento al livello fondamentale ($E_1$). Questo processo, noto come **emissione stimolata**, genera un nuovo fotone identico a quello incidente (stessa frequenza, fase e polarizzazione), producendo di fatto un'amplificazione coerente del segnale ottico.



## 2.2. Il Rumore di Emissione Spontanea Amplificata (ASE)

In assenza di un segnale di ingresso da stimolare, gli ioni eccitati al livello metastabile ($E_2$) possono comunque decadere al livello fondamentale ($E_1$) in modo spontaneo. Questo **decadimento spontaneo** genera fotoni con fase e direzione casuali, dando origine a un rumore ottico a larga banda che viene a sua volta amplificato lungo la fibra. Questo fenomeno è noto come **Emissione Spontanea Amplificata (ASE)**. Le osservazioni sperimentali hanno confermato le seguenti caratteristiche:

* L'ASE è chiaramente visibile sull'analizzatore di spettro ottico non appena l'EDFA viene acceso, anche in totale assenza di un segnale di ingresso.
* Lo spettro dell'ASE non è piatto, ma presenta un andamento caratteristico dipendente dal materiale della fibra drogata. Nel caso specifico, è stato osservato un picco pronunciato intorno a $\mathbf{1533\ \text{nm}}$.
* La conoscenza dello spettro $\text{ASE}$ è di grande importanza pratica, poiché permette di progettare filtri ottici da posizionare a valle dell'amplificatore per sopprimere il rumore fuori banda. Questo migliora il rapporto segnale/rumore ottico ($\text{OSNR}$) del sistema, filtrando le componenti di rumore distanti dalla lunghezza d'onda del segnale.

Con questi concetti in mente, è possibile ora descrivere la metodologia pratica adottata per la raccolta dei dati sperimentali.

---

# 3. Procedura Sperimentale

L'esecuzione di misure accurate e affidabili richiede l'adozione di una metodologia rigorosa e sequenziale. Di seguito sono riportati i passaggi chiave seguiti durante l'attività di laboratorio per la caratterizzazione dell'EDFA.

1.  **Accensione e Osservazione Iniziale**: Inizialmente, con l'EDFA e il laser di segnale spenti, è stato osservato lo spettro di base sull'analizzatore. Questo ha permesso di identificare il rumore di fondo intrinseco dello strumento di misura, caratterizzato da un livello di potenza **esattamente $-60\ \text{dBm}$**.
2.  **Isolamento e Osservazione del Rumore ASE**: Mantenendo il laser di segnale spento, l'EDFA è stato acceso tramite l'apposita chiavetta di sicurezza. Sull'analizzatore di spettro si è immediatamente osservato un significativo innalzamento del livello di rumore su un'ampia banda di lunghezze d'onda, corrispondente all'emissione spontanea amplificata ($\text{ASE}$) generata dall'amplificatore, **con una potenza che si estende in un intervallo approssimativo da $-50\ \text{dBm}$ a $-10\ \text{dBm}$, come visualizzato sull'analizzatore.**
3.  **Protocollo Operativo Fondamentale**: È stata seguita una regola operativa critica: **non accendere mai il laser di segnale quando l'EDFA è già in funzione**. Questa precauzione serve a **evitare che l'amplificatore, carico di energia accumulata in assenza di segnale, rilasci un transitorio di potenza elevata ('colpo') all'arrivo del segnale, con potenziale rischio per i componenti a valle.** La sequenza corretta prevede di attivare prima il segnale ottico in ingresso e solo successivamente accendere l'amplificatore.
4.  **Impostazione dei Parametri di Misura**: Per la prima serie di misurazioni, sono stati impostati i seguenti parametri:
    * Lunghezza d'onda del laser di segnale: $\mathbf{1533\ \text{nm}}$.
    * Potenza del segnale in ingresso: $\mathbf{-25\ \text{dBm}}$, regolata tramite un attenuatore variabile.
5.  **Acquisizione Dati su Analizzatore di Spettro**: Per ogni punto di misura, è stata seguita una procedura di acquisizione standardizzata:
    * Lo *span* dell'analizzatore di spettro è stato regolato per visualizzare un intervallo ristretto attorno al segnale (es. da $\mathbf{1530\ \text{nm}}$ a $\mathbf{1536\ \text{nm}}$), consentendo una visualizzazione dettagliata. Questa operazione di 'zoom' è fondamentale non solo per posizionare con precisione i marker, ma anche per **identificare correttamente il picco del segnale, specialmente a bassi livelli di potenza dove potrebbe essere meno distinguibile dal rumore ASE circostante.**
    * È stata utilizzata la funzione $\text{Peak Search}$ per identificare con precisione la potenza di picco del segnale, corrispondente alla potenza in uscita dall'amplificatore ($P_{\text{out}}$).
    * Sono stati impostati due marker, posizionati rispettivamente a $\mathbf{1\ \text{nm}}$ **prima** e $\mathbf{1\ \text{nm}}$ **dopo** la lunghezza d'onda del picco del segnale, per misurare i livelli di potenza del rumore $\text{ASE}$ in prossimità del segnale.
6.  **Registrazione dei Dati**: Per ogni configurazione di potenza in ingresso, sono stati registrati i seguenti valori: la potenza di ingresso ($P_{\text{in}}$) **impostata tramite l'attenuatore variabile e letta direttamente dal power meter dedicato**, la potenza di uscita ($P_{\text{out}}$) identificata dal $\text{Peak Search}$, e i due valori di potenza del rumore $\text{ASE}$ misurati tramite i marker.

I dati raccolti attraverso questa procedura sono stati successivamente elaborati per l'analisi delle prestazioni dell'amplificatore.

---

# 4. Analisi e Discussione dei Risultati

Questa sezione si concentra sull'interpretazione dei dati raccolti, collegando le osservazioni quantitative alla fisica del dispositivo e valutandone le prestazioni complessive.

## 4.1. Stima del Rumore ASE e Motivazione Concettuale

Una delle decisioni metodologiche più importanti riguarda la stima del rumore $\text{ASE}$. Sarebbe concettualmente errato misurare il livello di $\text{ASE}$ alla lunghezza d'onda del segnale una sola volta in assenza di segnale e poi utilizzare questo valore fisso per tutte le misurazioni successive. La motivazione risiede nel principio stesso del sistema a tre livelli. **In altre parole, come evidenziato dal modello fisico, gli ioni non possono essere impegnati simultaneamente nel processo di emissione stimolata e in quello di emissione spontanea.**

Gli atomi di erbio eccitati non possono essere simultaneamente impegnati in due processi distinti: l'emissione stimolata (che amplifica il segnale) e l'emissione spontanea (che genera rumore $\text{ASE}$). La presenza di un segnale di ingresso di intensità non trascurabile "impegna" una frazione significativa della popolazione di ioni eccitati nel processo di emissione stimolata. Di conseguenza, il numero di ioni disponibili per decadere spontaneamente si riduce, portando a una **diminuzione del livello di rumore ASE**.

Pertanto, la misurazione dell'ASE a $\mathbf{+1\ \text{nm}}$ e $\mathbf{-1\ \text{nm}}$ dal picco del segnale non è una semplice complicazione procedurale, ma una **interpolazione necessaria**. Essa permette di stimare in modo più accurato il reale livello di rumore $\text{ASE}$ presente *alla lunghezza d'onda del segnale e in sua effettiva presenza*, tenendo conto della competizione tra i due meccanismi di emissione.

## 4.2. Andamento del Guadagno e Fenomeno della Saturazione

Dall'analisi dei dati raccolti è emerso un comportamento caratteristico dell'amplificatore. In particolare, è stata osservata una **saturazione iniziale del guadagno**. Questo fenomeno, perfettamente in linea con il comportamento atteso per gli $\text{EDFA}$, si verifica quando la potenza del segnale in ingresso ($P_{\text{in}}$) aumenta al punto da esaurire una parte significativa degli ioni eccitati disponibili, riducendo l'efficienza di amplificazione per i fotoni successivi.

Queste analisi confermano la validità del modello teorico e forniscono una caratterizzazione quantitativa delle prestazioni del dispositivo sotto esame.

---

# 5. Conclusioni

Questa relazione ha descritto in dettaglio la metodologia e l'analisi relative a un esperimento di laboratorio per la caratterizzazione di un amplificatore a fibra drogata con erbio ($\text{EDFA}$). L'attività ha permesso di raggiungere con successo gli obiettivi prefissati.

In sintesi, i principali risultati e le comprensioni acquisite sono:

* È stata eseguita con successo la caratterizzazione dell'$\text{EDFA}$, misurando il suo guadagno ($G$) e il livello di rumore $\text{ASE}$ in funzione della potenza del segnale di ingresso ($P_{\text{in}}$).
* È stata confermata sperimentalmente l'esistenza del rumore di Emissione Spontanea Amplificata ($\text{ASE}$), osservandone le caratteristiche spettrali previste dalla teoria, incluso il picco caratteristico a $\mathbf{1533\ \text{nm}}$.
* È stata compresa e applicata la metodologia corretta per la stima del rumore $\text{ASE}$ in presenza di segnale, giustificandola attraverso il modello fisico del sistema a tre livelli e il principio di competizione tra emissione stimolata e spontanea.

In conclusione, l'esperimento ha fornito una chiara e quantitativa dimostrazione dei principi di funzionamento e delle performance di un componente cruciale per le moderne reti di comunicazione ottica.