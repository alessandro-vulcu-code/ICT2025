## Introduzione

Questo manuale è stato concepito come una guida di riferimento completa per la stesura di report di laboratorio che siano tecnici, professionali e di alta qualità. L'obiettivo primario della comunicazione scientifica nel campo delle fibre ottiche è trasmettere i risultati di un'indagine in modo efficace e riproducibile. Per questo, è fondamentale porre la massima attenzione alla chiarezza espositiva, alla struttura logica del documento e alla corretta analisi dei dati raccolti. Un report ben scritto non si limita a presentare dei numeri, ma costruisce una narrazione coerente che guida il lettore dalla premessa teorica all'interpretazione dei risultati.

Nel corso di questo documento, affronteremo nel dettaglio la struttura standard richiesta per ogni report, le norme essenziali per la presentazione di dati e risultati attraverso figure e tabelle, la metodologia di analisi statistica basata sul metodo dei minimi quadrati (LSE) e, infine, le linee guida specifiche per l'analisi dei dati relativi a ciascuna delle quattro esperienze di laboratorio previste.

---

## 1. Struttura e Formato del Report di Laboratorio

L'adozione di una struttura standardizzata è di importanza cruciale per garantire la leggibilità, la riproducibilità e una valutazione professionale del lavoro svolto. Una struttura chiara e coerente non è un mero formalismo, ma il fondamento su cui si costruisce un documento tecnico efficace, permettendo a chi legge di orientarsi rapidamente e di comprendere appieno ogni fase del vostro lavoro, dalla metodologia ai risultati finali.

### 1.1 Struttura Generale

Il report di laboratorio deve consistere in un documento di circa **3 pagine di contenuto effettivo**, a cui si aggiunge un frontespizio. La relazione deve essere organizzata nelle seguenti quattro sezioni obbligatorie, ciascuna con uno scopo preciso.

- **Frontespizio** Deve contenere le informazioni essenziali per l'identificazione del lavoro: il titolo del report, i nomi completi degli autori e il numero del gruppo di appartenenza.
    
- **Introduzione** Questa sezione ha lo scopo di fornire il contesto dell'esperimento. Deve riassumere la logica alla base dell'esperienza e richiamare brevemente il pertinente background teorico. È fondamentale che indichi i parametri chiave che sono stati misurati durante l'attività di laboratorio. L'introduzione **non deve contenere né risultati né conclusioni**. La lunghezza ideale è di circa mezza pagina.
    
- **Risultati e Discussione** Questa è la sezione centrale del report. I risultati devono essere presentati in una sequenza logica, utilizzando una combinazione di testo, tabelle e figure, evitando di presentare gli stessi dati in forme diverse (ad esempio, sia in una tabella che in un grafico). La discussione deve andare oltre la semplice reiterazione dei dati: deve interpretarli, metterli in relazione con le ipotesi formulate nell'introduzione e fornire commenti critici sulla qualità dei risultati ottenuti. Per esempio, nel caso della misura della frequenza di taglio, questa sezione deve contenere il grafico finale con la curva di differenza spettrale da cui si ricava il cut-off, non gli spettri grezzi (raw) misurati. La sezione 'Risultati e Discussione' presenta il prodotto finale dell'analisi, mentre 'Materiali e Metodi' documenta il processo e i dati grezzi che hanno portato a quel risultato.
    
- **Materiali e Metodi** In questa sezione occorre descrivere l'apparato sperimentale e le procedure di analisi dei dati con un livello di dettaglio tale da permettere a un altro ricercatore di riprodurre il vostro lavoro. È qui che si devono specificare le modalità con cui i risultati sono stati ottenuti. Ad esempio, si menzionerà che i dati della dispersione cromatica sono stati analizzati tramite un fitting basato sul metodo dei minimi quadrati (LSE) o si descriverà brevemente l'assetto sperimentale utilizzato.
    

### 1.2 Formato di Consegna

Il report può essere preparato con un editor di vostra scelta (es. Microsoft Word, $\LaTeX$). Tuttavia, il file finale deve essere consegnato esclusivamente in formato **PDF**.

Il file deve essere nominato seguendo una convenzione precisa per facilitarne l'identificazione e l'archiviazione. Il nome del file deve includere il numero del gruppo e un riferimento breve e chiaro all'esperimento, evitando codici generici.

**Esempio di nome file corretto:** `gruppo2_chromatic.pdf`

L'adesione a questa struttura formale è il primo passo per la creazione di un documento professionale. La sezione seguente affronterà come presentare i contenuti al suo interno in modo altrettanto efficace.

---

## 2. Norme di Presentazione: Figure, Tabelle ed Equazioni

La presentazione visiva dei dati e delle formule matematiche è cruciale per la chiarezza e l'impatto di un report tecnico. Una figura ben realizzata può comunicare un'informazione complessa in modo più immediato ed efficace di un lungo paragrafo. Questa sezione fornisce regole pratiche ed esempi concreti per evitare gli errori più comuni e massimizzare la comprensibilità del vostro lavoro.

### 2.1 Gestione delle Figure

Le figure non sono elementi decorativi, ma strumenti di comunicazione. Devono rispettare le seguenti regole fondamentali:

- **Chiarezza e Leggibilità:** Le figure devono essere chiare, nitide e dimensionate in modo appropriato rispetto al testo. Le etichette, i numeri e le legende devono essere facilmente leggibili.
    
- **Assi e Unità di Misura:** Gli assi dei grafici devono sempre essere etichettati con il nome della grandezza rappresentata e la sua unità di misura. Le scale devono essere scelte in modo da evidenziare le caratteristiche salienti dei dati.
    
- **Numerazione e Didascalie (Caption):** Ogni figura deve avere un numero progressivo (es. Figura 1, Figura 2, ...) e una didascalia concisa ma descrittiva, che ne spieghi il contenuto.
    
- **Riferimenti nel Testo:** Nel corpo del testo, ci si deve sempre riferire alle figure tramite il loro numero (es. "come mostrato in Figura 1"). Vanno evitate espressioni ambigue come "nella figura sottostante" o "nel grafico qui sopra".
    

#### Esempi di Errori da Evitare

Un errore comune è rappresentare sullo stesso grafico due grandezze con ordini di grandezza completamente diversi utilizzando una sola scala verticale. L'esempio seguente mostra i dati grezzi di potenza (in dBm, con valori intorno a $-60 \text{ dBm}$) e la loro differenza (in $\text{dB}$, con valori intorno a $1 \text{ dB}$) tracciati sulla stessa scala. Il risultato è un grafico illeggibile, in cui la curva di interesse (la differenza) è completamente schiacciata e incomprensibile.

La soluzione corretta a questo problema è utilizzare **due scale verticali distinte**, una a sinistra e una a destra, oppure, più semplicemente, creare due figure separate.

Un altro esempio di cattiva presentazione è l'inclusione di grafici "tagliati" direttamente da un foglio di calcolo. Questi grafici spesso mancano di etichette e unità di misura sugli assi, hanno un aspetto poco professionale e utilizzano una formattazione numerica "inutilmente macchinosa" (ad esempio, `8.00E+02` invece del più leggibile `800`).

#### Esempio di Buona Presentazione

Le figure seguenti sono un esempio di presentazione quasi corretta. I grafici sono ben inquadrati, le etichette sono leggibili e, correttamente, sono state utilizzate due scale verticali per rappresentare grandezze con ordini di grandezza differenti.

Tuttavia, anche qui persistono degli errori: manca la numerazione progressiva delle figure e la didascalia è stata formattata erroneamente su due colonne. Una didascalia unica e corretta sarebbe stata:

**_Figura 2._** _Lunghezza d'onda di cut-off della fibra (a) non-zero dispersion shifted e (b) a basse perdite per curvatura ($\text{low-bending loss fiber}$)._

### 2.2 Utilizzo di Tabelle e Equazioni

Le **tabelle** sono lo strumento ideale per riassumere dati in modo ordinato, specialmente quando si devono confrontare parametri relativi a diversi campioni o condizioni sperimentali. Ad esempio, per riportare lunghezza e attenuazione di diverse fibre, una tabella è molto più chiara di una descrizione testuale.

Anche le tabelle devono avere **un numero progressivo e una didascalia**, e nel testo ci si deve riferire ad esse tramite il loro numero (es. "i parametri delle fibre sono riportati in Tabella 2").

Per quanto riguarda le **equazioni**, è importante ricordare che le equazioni esposte (quelle su una riga a sé stante) sono **parte integrante della frase** e non oggetti flottanti come le figure.

- **Formattazione corretta:** "La lunghezza d'onda di un'onda è data da:
    
    $$\lambda = \frac{c}{f}$$
    
    dove $c$ è la velocità della luce nel vuoto e $f$ è la frequenza."
    
- **Formattazione errata:** "La lunghezza d'onda è data dalla formula:
    
    $$\lambda = \frac{c}{f}$$
    
    dove $c$ è la velocità della luce nel vuoto e $f$ è la frequenza."
    

È obbligatorio utilizzare un **editor di equazioni** per una corretta formattazione tipografica (es. si scrive $a \times b$, non $a \text{ x } b$). Infine, le equazioni vanno numerate se è necessario farvi riferimento in altri punti del testo.

Dopo aver visto come presentare correttamente i dati, la prossima sezione affronterà il metodo fondamentale per analizzarli quantitativamente.

---

## 3. Metodologia di Analisi: Il Metodo dei Minimi Quadrati (LSE)

Il metodo dei minimi quadrati, o LSE (Least Square Error), è una tecnica fondamentale per l'analisi dei dati sperimentali. Il suo scopo è stimare i parametri di un modello teorico che si presume descriva i dati raccolti. La tecnica agisce trovando i valori dei parametri che minimizzano la discrepanza (l'errore quadratico) tra il modello matematico e le misurazioni effettive.

### 3.1 Principio Generale

Consideriamo un set di $M$ misurazioni $(x_j, y_j)$, dove $x$ è la variabile indipendente (impostata da noi, es. la lunghezza d'onda) e $y$ è la grandezza misurata (es. il ritardo di gruppo). Assumiamo che questi dati seguano un modello teorico descritto dalla funzione $y = f(x; p_1, \dots, p_N)$, dove $p_1, \dots, p_N$ sono gli $N$ parametri del modello che vogliamo stimare.

Il metodo LSE consiste nel trovare quel set di parametri $p_j$ che minimizza l'errore quadratico residuo, $\rho^2$, definito come la somma dei quadrati delle differenze tra i valori misurati e i valori predetti dal modello:

$$\rho^2 = \sum_{j=1}^{M} [y_j - f(x_j; p_1, \dots, p_N)]^2$$

La minimizzazione si ottiene matematicamente risolvendo il sistema di equazioni che si ottiene imponendo che le derivate parziali di $\rho^2$ rispetto a ciascun parametro $p_i$ siano uguali a zero.

In generale, la soluzione di questo sistema richiede metodi numerici. I software di calcolo più comuni mettono a disposizione funzioni specifiche per questo scopo, come `lsqcurvefit` in Matlab e `scipy.optimize.curve_fit` in Python.

### 3.2 Il Caso Lineare

Esiste un'importante eccezione in cui la soluzione può essere trovata in forma chiusa (cioè tramite una formula diretta): quando il modello $f$ è **lineare rispetto ai parametri** $p_i$. Attenzione: questo non significa che debba essere lineare rispetto alla variabile $x$.

La forma generale di un modello lineare nei parametri è:

$$y = \sum_{i=1}^{N} c_i(x) p_i$$

In questo caso, se il numero di misure $M$ è maggiore o uguale al numero di parametri $N$ e la matrice $\mathbf{C}^T\mathbf{C}$ è ben condizionata, la soluzione per il vettore dei parametri ottimali $\mathbf{\bar{p}}$ è data dalla seguente espressione matriciale:

$$\mathbf{\bar{p}} = (\mathbf{C}^T\mathbf{C})^{-1}\mathbf{C}^T \mathbf{\bar{y}}$$

dove $\mathbf{\bar{y}}$ è il vettore colonna delle $M$ misure e $\mathbf{C}$ è la matrice $M \times N$ costruita valutando le funzioni $c_i(x)$ in corrispondenza di ciascun punto di misura $x_j$.

### 3.3 Il Caso Polinomiale

Un caso speciale di grande importanza pratica, che rientra nel modello lineare, è il fitting polinomiale. In questo caso, il modello è un polinomio nella variabile $x$:

$$y = \sum_{i=0}^{N-1} p_i x^i$$

Anche questo modello è lineare rispetto ai parametri (i coefficienti del polinomio $p_i$) e non lineare rispetto alla variabile $x$. Data la sua frequenza d'uso, esistono funzioni pre-compilate che risolvono direttamente questo problema, come polyfit in Matlab e numpy.polyfit in Python.

Il metodo LSE è quindi uno strumento potente per estrarre parametri fisicamente significativi dai dati sperimentali. La prossima sezione mostrerà come applicarlo concretamente alle diverse esperienze di laboratorio.

---

## 4. Guida all'Analisi per Esperienza di Laboratorio

In questa sezione verranno fornite indicazioni specifiche per l'analisi dei dati e la stesura del report per ciascuna delle quattro esperienze di laboratorio. L'obiettivo è applicare i principi generali di struttura, presentazione e analisi discussi in precedenza al contesto di ogni singolo esperimento.

### 4.1 Frequenza di Taglio e Attenuazione Spettrale

- **Analisi dei Dati:** Questa esperienza richiede un'analisi prevalentemente qualitativa piuttosto che un fitting numerico. L'obiettivo principale è determinare le lunghezze d'onda di cut-off, che vengono identificate come i punti in cui la curva di attenuazione differenziale incrocia la soglia di $\mathbf{0.1 \text{ dB}}$.
    
- **Discussione e Commenti:** È richiesta una discussione approfondita dei risultati. Per quanto riguarda l'attenuazione spettrale, è necessario identificare e spiegare le caratteristiche notevoli osservate, come il picco di assorbimento dell'ossidrile ($\text{OH}$) intorno a $1380 \text{ nm}$. Per le lunghezze d'onda di cut-off, si deve ricordare che ogni picco corrisponde alla perdita di un modo specifico. Il vostro compito è associare i valori di cut-off misurati ai rispettivi modi $\text{LP}$, utilizzando come riferimento i diagrammi di dispersione delle fibre $\text{step-index}$ visti a lezione.
    

### 4.2 Dispersione Cromatica

- **Analisi dei Dati:** Questa esperienza rappresenta un'applicazione chiave del metodo **LSE**. È necessario utilizzare tale metodo per effettuare il fitting dei dati di ritardo di gruppo in funzione della lunghezza d'onda.
    
- **Struttura del Report:** La divisione dei contenuti deve essere netta. Nella sezione "Materiali e Metodi" vanno descritti i dati misurati (il ritardo di gruppo) e la procedura di fitting LSE utilizzata (specificando il modello polinomiale e la funzione software impiegata). Nella sezione "Risultati e Discussione" va invece presentato il risultato finale, ovvero il grafico della dispersione cromatica totale $D_{\text{TOT}}$ in funzione della lunghezza d'onda, e l'analisi dei parametri estratti dal fit.
    
- **Discussione e Commenti:** La discussione deve vertere sui parametri chiave ottenuti dal fitting, come la lunghezza d'onda a dispersione nulla ($\text{zero dispersion wavelength}$) e la pendenza della curva in quel punto ($\text{slope}$). Queste informazioni devono essere usate per argomentare e identificare il tipo di fibra analizzata. Si richiede inoltre di commentare il significato e l'origine delle barre di errore mostrate nei grafici, riflettendo sulla precisione della misura.
    

### 4.3 EDFA (Erbium-Doped Fiber Amplifier)

- **Analisi dei Dati:** Per questo esperimento non è richiesto un fitting numerico complesso, in quanto non è disponibile un modello teorico semplice e trattabile. L'analisi è quindi di tipo qualitativo.
    
- **Discussione e Commenti:** È necessario analizzare i grafici di guadagno ($\text{Gain}$) e figura di rumore ($\text{Noise Figure}$) per riconoscere e commentare le caratteristiche e i comportamenti visti durante le lezioni. Dai dati raccolti è possibile e richiesto derivare parametri ausiliari significativi, come le **potenze di saturazione** in ingresso e in uscita. È inoltre fondamentale commentare la relazione osservata tra andamento del guadagno e andamento della figura di rumore.
    

### 4.4 PMD (Polarization Mode Dispersion)

L'analisi per questo esperimento si differenzia a seconda del tipo di fibra esaminata.

#### Fibra a Mantenimento di Polarizzazione (PMF)

- **Analisi:** In una fibra $\text{PMF}$, le componenti dello stato di polarizzazione ($\text{SOP}$) in uscita variano in modo periodico con la frequenza della luce. Il metodo **LSE** può essere utilizzato per determinare con alta precisione il periodo di questa variazione sinusoidale.
    
- **Discussione:** L'inverso di questo periodo, misurato nel dominio della frequenza, corrisponde direttamente al $\text{Differential Group Delay (DGD)}$ della fibra.
    

#### Fibra Standard

- **Analisi:** In una fibra standard, la variazione del $\text{SOP}$ con la frequenza è disordinata (casuale). Il $\text{DGD}$ medio deve quindi essere stimato tramite l'**analisi del level crossing-rate**.
    
- **Metodologia:** La procedura consiste nel calcolare la funzione $T(\omega) = 1/2 [1 + \hat{s}(\omega) \cdot \hat{p}]$ e contare il numero di volte $n(\nu)$ che tale funzione attraversa un dato livello $\nu$ (es. $\nu = 0.5$) per unità di banda di frequenza.
    
- Calcolo: Una stima del $\text{DGD}$ medio $\Delta\tau$ può essere ottenuta in modo semplificato considerando solo il livello $\nu = 1/2$, usando la formula: $\Delta\tau = 4 n(1/2)$. Una stima più robusta e accurata si ottiene utilizzando più livelli e applicando nuovamente l'analisi LSE. Il modello teorico in questo caso è:
    
    $$n(\nu) = \frac{\Delta\tau}{2} \sqrt{\nu(1-\nu)}$$
    
    Questo è un problema $\text{LSE}$ in cui la variabile indipendente è il livello $\nu$ da noi scelto, la grandezza misurata è il numero di attraversamenti $n(\nu)$ e il parametro da stimare è il $\text{DGD}$ medio $\Delta\tau$. Poiché il modello è lineare rispetto al parametro $\Delta\tau$, il problema può essere risolto agevolmente. La formula completa per $\Delta\tau$ che ne deriva è:
    
    $$\Delta\tau = 2 \frac{\sum_{i=1}^{M} n(\nu_i) \sqrt{\nu_i(1-\nu_i)}}{\sum_{i=1}^{M} \nu_i(1-\nu_i)}$$
    
    Seguendo queste linee guida specifiche, ogni report potrà contenere un'analisi approfondita e pertinente, dimostrando una solida comprensione teorica e sperimentale dei fenomeni studiati.
    

---

## 5. Considerazioni Finali e Buone Pratiche

Questo manuale ha fornito una struttura e un insieme di regole per la produzione di report di laboratorio di livello professionale. L'obiettivo finale è comunicare il vostro lavoro in modo chiaro, rigoroso e convincente. Prestare attenzione ai dettagli è ciò che distingue un documento amatoriale da uno professionale. A conclusione, ecco due raccomandazioni finali.

- **Accuratezza Terminologica:** Utilizzate sempre una terminologia precisa e corretta. Errori concettuali come scrivere "bending loss fiber" (fibra a perdita per curvatura) invece di "low-bending loss fiber" (fibra a basse perdite per curvatura) denotano una mancanza di attenzione e possono compromettere la credibilità del vostro lavoro.
    
- **Cifre Significative:** Gli strumenti di calcolo forniscono risultati con un numero elevato di cifre decimali, ma solo alcune di esse sono fisicamente significative. È essenziale riflettere sull'incertezza intrinseca delle misure e riportare i risultati finali con un numero ragionevole di cifre. Dichiarare un $\text{DGD}$ di $2.175 \text{ ps}$ implica, ad esempio, una precisione al femtosecondo, una pretesa probabilmente irrealistica data la strumentazione e la metodologia. Chiedetevi sempre se la precisione che state riportando è giustificata.
    

Buon lavoro.