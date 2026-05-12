# 1.0 Introduzione e Scopo dell'Esperienza

La qualificazione delle fibre ottiche per l'impiego in sistemi di telecomunicazione moderni richiede una caratterizzazione accurata dei loro parametri fondamentali di trasmissione. Tra questi, la **lunghezza d'onda di taglio** ($\lambda_c$) e il profilo di **attenuazione spettrale** ($\alpha(\lambda)$) sono cruciali per determinare il regime operativo della fibra e la sua idoneità per applicazioni specifiche. La lunghezza d'onda di taglio ($\lambda_c$) definisce il limite al di sopra del quale la fibra opera in regime monomodale ($\text{single-mode}$), condizione essenziale per la trasmissione di segnali ad alta velocità su lunghe distanze. L'attenuazione, d'altra parte, quantifica la perdita di potenza del segnale ottico lungo il percorso e ne determina la portata massima. Lo scopo strategico di questa attività di laboratorio è stato quello di misurare questi parametri chiave su diverse tipologie di fibra, consolidando la comprensione teorica attraverso l'applicazione pratica di metodologie di misura standard.

Gli obiettivi specifici dell'esperienza sono stati i seguenti:

* Misurare la **lunghezza d'onda di taglio** ($\lambda_c$) su diverse tipologie di fibra ottica, applicando il metodo della perturbazione indotta da curvatura.
* Misurare il **profilo di attenuazione spettrale** ($\alpha(\lambda)$) per tre diverse bobine di fibra, caratterizzate da lunghezze e proprietà fisiche differenti.
* Documentare le procedure operative, le configurazioni strumentali e le problematiche pratiche riscontrate durante l'utilizzo dell'analizzatore di spettro ottico ($\text{OSA}$).

La presente relazione descrive in dettaglio la strumentazione impiegata, le metodologie di misura adottate, le caratteristiche delle fibre analizzate e presenta un'analisi critica dei risultati ottenuti.

---

# 2.0 Strumentazione e Setup Sperimentale

L'affidabilità delle misure ottiche dipende in modo critico dalla precisione e dalla stabilità del setup sperimentale. Per questa attività si è allestito un banco di misura controllato, progettato per caratterizzare le Fibre Ottiche Sotto Test ($\text{DUT}$ - *Device Under Test*) in modo sistematico.

L'apparato sperimentale principale era costituito dai seguenti componenti:

* **Analizzatore di Spettro Ottico ($\text{OSA}$):** Si è impiegato il modello $\mathbf{ANDO\ AQ-6315A}$. Questo strumento è il cuore del sistema di misura, in grado di analizzare lo spettro ottico misurando la potenza del segnale in ingresso per ogni lunghezza d'onda all'interno del suo range operativo (da $\mathbf{750\ \text{nm}}$ a $\mathbf{1750\ \text{nm}}$).
* **Sorgente Ottica:** Una sorgente a banda larga, integrata nel setup e direttamente connessa all'$\text{OSA}$, è stata utilizzata per iniettare il segnale ottico nelle fibre da analizzare.
* **Fibre Ottiche sotto test ($\text{DUT}$):** Sono state analizzate diverse bobine e spezzoni di fibra, incluse tipologie standard, a dispersione modificata e resistenti alla curvatura, i cui dettagli sono forniti nelle sezioni successive.

La configurazione del banco ottico prevedeva il collegamento in cascata della sorgente ottica, della fibra sotto test e dell'analizzatore. Per l'interfacciamento tra i vari componenti sono stati utilizzati specifici cavi di connessione (*patch cord*) dotati di connettori differenti. In particolare, si è osservata la presenza di connettori $\mathbf{PC}$ (*Physical Contact*), tipicamente di colore nero o blu, e connettori $\mathbf{APC}$ (*Angled Physical Contact*), di colore verde. La differenza fondamentale risiede nella lavorazione della ferula: nei connettori $\text{PC}$, la superficie è levigata perpendicolarmente all'asse della fibra, mentre nei connettori $\text{APC}$ è inclinata di circa $\mathbf{7-8}$ gradi. Questa angolazione è progettata per minimizzare le riflessioni di potenza all'interfaccia, deviando la luce riflessa al di fuori del $\text{core}$ della fibra. L'uso di connettori $\text{APC}$ è cruciale non solo per preservare l'integrità del segnale ma anche per **proteggere sorgenti laser sensibili da *back-reflection* che potrebbero causarne instabilità o danneggiamento**. L'accoppiamento tra connettori di tipo diverso è stato reso possibile dall'uso di appositi adattatori.



La descrizione della strumentazione e del suo corretto assemblaggio è propedeutica alla comprensione delle metodologie di misura applicate, descritte nella sezione seguente.

---

# 3.0 Metodologia di Misura

L'esperienza di laboratorio ha impiegato due procedure distinte e complementari per una caratterizzazione completa delle fibre ottiche: una per la determinazione della lunghezza d'onda di taglio ($\lambda_c$) e una per la misura dell'attenuazione spettrale ($\alpha(\lambda)$).

## 3.1 Misura della Lunghezza d'Onda di Taglio tramite Metodo della Curvatura

Questa metodologia si basa su un principio fisico ben preciso: una curvatura imposta alla fibra ottica introduce delle perdite di potenza che sono selettive per i modi di propagazione. In particolare, i modi di ordine superiore (come il modo $\text{LP}_{11}$ in una fibra standard) sono meno confinati nel $\text{core}$ e, in prossimità della loro lunghezza d'onda di taglio, diventano estremamente sensibili alle piegature. Inducendo una curvatura, si causa un'attenuazione significativa di questi modi, rendendo possibile l'identificazione della loro lunghezza d'onda di taglio ($\lambda_c$).

La procedura operativa, supportata dalle funzionalità dell'$\text{OSA}$, è stata la seguente:

1. **Acquisizione Riferimento (Traccia A):** Si acquisisce e si memorizza (*fix*) una prima traccia spettrale con la fibra in condizioni di riposo, non perturbata. Questa traccia rappresenta il riferimento del sistema.
2. **Acquisizione Misura (Traccia B):** Mantenendo fissa la Traccia A, si introduce manualmente una curvatura controllata sulla fibra e si acquisisce una nuova traccia spettrale.
3. **Analisi Differenziale (Traccia C):** L'analizzatore calcola in tempo reale la differenza tra le due tracce ($\text{Traccia}\ \mathbf{C = A - B}$). Questa traccia differenziale mostra dei picchi positivi in corrispondenza delle lunghezze d'onda dove la curvatura ha indotto un'attenuazione. Il picco più significativo a lunghezza d'onda maggiore corrisponde alla lunghezza d'onda di taglio ($\lambda_c$) del primo modo di ordine superiore.

L'obiettivo operativo consisteva nel regolare l'intensità della curvatura fino a ottenere un picco sulla Traccia C con un'ampiezza di circa $\mathbf{1\ \text{dB}}$. Questo valore rappresenta un compromesso ottimale: una curvatura eccessiva (picchi $> \mathbf{1-2\ \text{dB}}$) potrebbe fondere in un unico picco i contributi di modi quasi degeneri, mascherando la loro reale presenza, mentre una curvatura troppo debole produrrebbe un segnale indistinguibile dal rumore di fondo.



## 3.2 Misura dell'Attenuazione Spettrale

Questa misura mira a quantificare la perdita di potenza del segnale ottico in funzione della lunghezza d'onda ($\lambda$), espressa in $\mathbf{\text{dB/km}}$.

La procedura seguita è stata:

1. **Acquisizione Potenza di Ingresso (Traccia A):** Si effettua una misura di riferimento collegando direttamente la sorgente ottica all'analizzatore tramite dei *patch cord*. La traccia risultante rappresenta la potenza spettrale in ingresso al sistema ($P_{\text{in}}$).
2. **Inserimento DUT:** Si apre il circuito ottico e si inserisce la bobina di fibra da misurare ($\text{DUT}$).
3. **Acquisizione Potenza di Uscita (Traccia B):** Si esegue una seconda misura, che rappresenta la potenza spettrale in uscita dalla fibra ($P_{\text{out}}$).

L'attenuazione totale della bobina, in $\text{dB}$, è data dalla differenza tra le due tracce ($P_{\text{in}} - P_{\text{out}}$). Per ottenere il **coefficiente di attenuazione spettrale ($\alpha$)**, espresso in $\mathbf{\text{dB/km}}$, è necessario normalizzare questo valore per la lunghezza ($L$) della fibra, secondo la formula:

$$\alpha = \frac{P_{\text{in}} (\text{dBm}) - P_{\text{out}} (\text{dBm})}{L (\text{km})}$$

La prossima sezione elenca le specifiche delle diverse fibre ottiche che sono state sottoposte a queste procedure di misura.

---

# 4.0 Fibre Ottiche Analizzate

Una parte fondamentale dell'esperienza è stata l'analisi di diverse tipologie di fibra, selezionate per evidenziare un'ampia gamma di comportamenti fisici e rispondere a esigenze applicative differenti. La selezione includeva fibre a dispersione modificata, fibre progettate per resistere alle curvature e fibre specialistiche per la compensazione della dispersione.

La tabella seguente riassume le fibre utilizzate nelle rispettive prove sperimentali, basandosi sui dati disponibili in laboratorio.

| Prova Sperimentale | Tipo di Fibra | Lunghezza ($L$) | Note Aggiuntive |
| :--- | :--- | :--- | :--- |
| **Misura $\lambda_c$** | $\text{Non-Zero Dispersion Shifted Fiber}$ | $\text{N/A}$ | Fibra con caratteristiche di dispersione particolari. |
| **Misura $\lambda_c$** | $\text{Bending Loss Fiber}$ | $\text{N/A}$ | Progettata per essere molto resistente alle perdite indotte da curvatura. |
| **Misura $\alpha(\lambda)$** | Fibra "Gialla" | $\mathbf{4.4\ \text{km}}$ | Prima fibra analizzata per l'attenuazione. |
| **Misura $\alpha(\lambda)$** | $\text{Non-Zero Dispersion Shifted Fiber}$ | $\mathbf{13.7\ \text{km}}$ | Fibra di lunghezza considerevole per valutare l'attenuazione su lunga distanza. |
| **Misura $\alpha(\lambda)$** | $\text{Dispersion Compensating Fiber (DCF)}$ | $\mathbf{2.0\ \text{km}}$ | Fibra speciale progettata per compensare la dispersione cromatica. |

Dopo aver descritto le caratteristiche statiche delle fibre, la sezione successiva illustra il flusso di lavoro dinamico seguito per l'acquisizione dei dati.

---

# 5.0 Procedura Operativa e Acquisizione Dati

Il flusso di lavoro seguito in laboratorio ha richiesto un approccio metodico, che ha messo in evidenza la necessità di **pazienza e abilità manuale**, specialmente nel processo iterativo di determinazione della lunghezza d'onda di taglio ($\lambda_c$).

La sequenza operativa può essere riassunta nei seguenti passaggi chiave:

1. **Impostazione Iniziale:** Accensione e configurazione dell'analizzatore di spettro ottico $\text{ANDO\ AQ-6315A}$, definendo il range spettrale e i parametri di visualizzazione.
2. **Acquisizione Riferimento:** Esecuzione di una scansione singola (*single sweep*) per registrare la traccia di riferimento (Traccia A) e successivo fissaggio (*fix*) del dato per prevenire sovrascritture accidentali.
3. **Applicazione della Perturbazione:** Nel caso della misura di *cut-off*, la fibra veniva piegata manualmente. Si è posta attenzione a localizzare la curvatura in un punto specifico, mantenendo il resto della fibra il più fermo possibile per non alterare le condizioni di riferimento.
4. **Acquisizione Misura:** Esecuzione di una nuova scansione per registrare la risposta del sistema perturbato sulla Traccia B.
5. **Analisi e Iterazione:** Osservazione in tempo reale della Traccia C (differenza $\text{A-B}$) e aggiustamento iterativo della curvatura manuale per raggiungere l'ampiezza del picco target di circa $\mathbf{1\ \text{dB}}$.
6. **Salvataggio Dati:** Una volta ottenuto un risultato soddisfacente, si è proceduto al salvataggio tramite una **procedura "vintage"** su **floppy disk**. Sono stati salvati sia gli *screenshot* dello schermo dell'analizzatore (come file $\mathbf{G0, G1, G2}$, etc.) sia i dati numerici delle tracce. Questi ultimi sono stati esportati in formato testo ($\mathbf{.TXT}$) contenente due colonne (lunghezza d'onda e ampiezza), assicurandosi di evitare il formato proprietario $\mathbf{.Win}$.

I dati così raccolti costituiscono la base per l'analisi quantitativa e qualitativa presentata nella sezione successiva.

---

# 6.0 Risultati e Analisi

In questa sezione vengono presentati e interpretati i dati raccolti durante le sessioni di misura, collegando le osservazioni quantitative alle proprietà fisiche intrinseche delle fibre ottiche esaminate.

## 6.1 Analisi della Lunghezza d'Onda di Taglio

L'applicazione del metodo della curvatura ha permesso di osservare chiaramente le differenze comportamentali tra le fibre analizzate.

* Un'osservazione qualitativa di rilievo riguarda la $\text{Bending Loss Fiber}$. Per indurre un'attenuazione misurabile su questa fibra, è stato necessario applicare una curvatura **"bella stretta" e "più pronunciata"** rispetto alla fibra $\text{Non-Zero Dispersion Shifted}$. Questo risultato conferma sperimentalmente la sua progettazione specifica, finalizzata a renderla altamente resistente alle perdite indotte da piegatura. Tale resistenza non è solo una proprietà teorica, ma una caratteristica critica per l'installazione in ambienti con vincoli di spazio, come **condotti e $\text{canaline}$** (*conduits and cable trays*), dove una fibra standard subirebbe perdite di segnale inaccettabili.
* La procedura di regolazione manuale per stabilizzare il picco a $\mathbf{1\ \text{dB}}$ si è rivelata un'operazione **macchinosa e non banale**, richiedendo numerosi tentativi iterativi per ottenere una misura stabile e affidabile. A basse attenuazioni, inoltre, è stata osservata la comparsa di più picchi distinti ma vicini, un'indicazione della presenza di modi quasi degeneri che, con curvature più intense, tendono a fondersi in un unico picco più largo.

## 6.2 Analisi dell'Attenuazione Spettrale

Le misure di attenuazione hanno fornito risultati coerenti con le caratteristiche note delle tre bobine di fibra.

* Il confronto tra la fibra "Gialla" da $\mathbf{4.4\ \text{km}}$ e la $\text{Non-Zero Dispersion Shifted}$ da $\mathbf{13.7\ \text{km}}$ ha mostrato, come atteso, un'attenuazione totale significativamente maggiore per la seconda, evidenziando la chiara dipendenza delle perdite dalla lunghezza ($L$) del collegamento.
* L'analisi più interessante riguarda la $\text{Dispersion Compensating Fiber (DCF)}$. Sebbene la sua lunghezza fosse di soli $\mathbf{2.0\ \text{km}}$, la sua attenuazione totale è risultata confrontabile con quella di fibre standard molto più lunghe. Questo comportamento, apparentemente anomalo, è in realtà perfettamente giustificato dalla funzione specialistica di questa fibra. La sua progettazione è ottimizzata non per minimizzare le perdite, ma per compensare la dispersione cromatica accumulata lungo un collegamento. Questo obiettivo viene raggiunto tramite tecniche di fabbricazione specialistiche che includono specifici **profili di drogaggio** (*dopants*), i quali, come *trade-off* ingegneristico, ne aumentano intrinsecamente il coefficiente di attenuazione ($\alpha$).

Le scoperte principali di questa fase analitica sono state riassunte e consolidate nelle conclusioni finali.

---

# 7.0 Conclusioni

L'esperienza di laboratorio si è conclusa con successo, raggiungendo tutti gli obiettivi prefissati e fornendo una comprensione pratica e approfondita delle tecniche di caratterizzazione delle fibre ottiche.

Le conclusioni tecniche più importanti possono essere sintetizzate come segue:

* L'efficacia del **metodo della curvatura** per identificare la lunghezza d'onda di taglio ($\lambda_c$) è stata pienamente verificata. Le misure hanno permesso di distinguere chiaramente il comportamento di fibre standard da quello di fibre specialistiche come la $\text{Bending Loss Fiber}$, la cui elevata resistenza alle piegature è stata confermata sperimentalmente.
* I **profili di attenuazione spettrale** ($\alpha(\lambda)$) misurati sono risultati coerenti con le caratteristiche teoriche e applicative delle fibre analizzate. In particolare, è stato dimostrato che l'elevata attenuazione della $\text{Dispersion Compensating Fiber (DCF)}$ non è un difetto, ma una caratteristica intrinseca legata alla sua funzione di compensazione della dispersione.
* L'esperienza ha confermato come, anche con strumentazione "vintage", la meticolosità dell'operatore e una profonda comprensione della metodologia siano essenziali per superare le limitazioni $\text{hardware}$ e ottenere dati di misura affidabili.

In conclusione, l'esperimento ha avuto un elevato valore formativo, non solo per i risultati tecnici ottenuti, ma anche per aver offerto una visione concreta delle complessità e delle sfumature che caratterizzano l'attività di misurazione in un ambiente di laboratorio reale.