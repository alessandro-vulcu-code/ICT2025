# 1.0 Introduzione e Scopo

Nei moderni sistemi di comunicazione ottica ad alta capacità, la gestione degli effetti di propagazione è di importanza strategica per massimizzare la larghezza di banda e la distanza di trasmissione. Tra questi, la **dispersione cromatica** rappresenta uno dei principali fattori limitanti. Questo fenomeno fisico descrive la dipendenza della velocità di gruppo di un segnale ottico dalla sua frequenza (o lunghezza d'onda, $\lambda$). In un impulso ottico, che è intrinsecamente composto da un insieme di frequenze diverse, ciascuna componente spettrale viaggia a una velocità leggermente differente, causando un allargamento temporale dell'impulso stesso e, di conseguenza, potenziale interferenza inter-simbolica.

L'origine fisica della dispersione cromatica risiede nella necessità di approssimare il coefficiente di propagazione della fibra, $\beta$, oltre il primo ordine. Mentre un'approssimazione al primo ordine descrive il ritardo di gruppo medio, è l'inclusione del termine di secondo ordine nell'espansione di Taylor di $\beta$ a rivelare come la velocità di gruppo vari con la frequenza, dando origine al fenomeno dispersivo.

Lo scopo di questa relazione è documentare in modo rigoroso e dettagliato la metodologia e i risultati dell'esperimento condotto per misurare e caratterizzare quantitativamente il parametro di dispersione cromatica di una specifica tratta di fibra ottica. L'analisi che segue descrive l'apparato sperimentale impiegato, la procedura di misurazione adottata e l'elaborazione dei dati raccolti.

---

# 2.0 Apparato Sperimentale

Il setup sperimentale è stato progettato per misurare la variazione del ritardo di gruppo di un segnale modulato che si propaga attraverso la fibra ottica in esame. Il principio di misura si basa sulla determinazione della differenza di fase tra un segnale di riferimento e il segnale di misura, osservando come questa differenza di fase evolva al variare della lunghezza d'onda della sorgente ottica.

## 2.1 Componenti del Setup

L'apparato sperimentale è costituito dai seguenti componenti chiave, ciascuno con una funzione specifica nel processo di misura:

- **Laser Tunabile:** Sorgente ottica coerente la cui lunghezza d'onda di emissione può essere variata con elevata precisione, permettendo di sondare il comportamento della fibra su un ampio spettro.
- **Controllore di Polarizzazione:** Dispositivo critico in questo setup, in quanto il modulatore elettro-ottico impiegato è basato su un'architettura a interferometro di Michelson, intrinsecamente sensibile allo stato di polarizzazione della luce in ingresso. La sua funzione è allineare la polarizzazione della luce laser all'asse principale del modulatore. Un disallineamento, in particolare una polarizzazione ortogonale, comporterebbe una potenza nulla in uscita dal modulatore, rendendo impossibile la misura.
- **Generatore di Radiofrequenza (RF):** Fornisce il segnale elettrico sinusoidale alla frequenza di $F = \mathbf{850\ \text{MHz}}$ utilizzato per la modulazione del segnale ottico.
- **Modulatore Elettro-ottico:** Componente che modula l'intensità della luce proveniente dal laser in accordo con il segnale RF in ingresso.
- **Fibra Ottica in Test (FUT):** La bobina di fibra ottica le cui proprietà dispersive sono l'oggetto della caratterizzazione.
- **Fotodilevatore:** Un fotorivelatore ad alta velocità che riconverte il segnale ottico, indebolito e ritardato dalla propagazione nella FUT, in un segnale elettrico proporzionale.
- **Vector Voltmeter:** Strumento di misura centrale dell'esperimento. Confronta il segnale proveniente dal canale di misura (Canale B) con un segnale di riferimento (Canale A), fornendo in uscita la differenza di ampiezza e, soprattutto, di fase tra i due.

## 2.2 Schema di Funzionamento

Il percorso del segnale si sviluppa lungo due canali distinti, che convergono nel Vector Voltmeter per il confronto di fase.

1. **Canale A (Riferimento):** Una delle uscite del generatore RF è connessa direttamente all'ingresso 'A' del Vector Voltmeter. Questo segnale, non subendo alcun ritardo se non quello del cavo coassiale, costituisce il riferimento di fase stabile ($\Phi_A$) per l'intera misurazione.
2. **Canale B (Misura):** La seconda uscita del generatore RF pilota il modulatore elettro-ottico, il quale impone la modulazione a $850\ \text{MHz}$ sul segnale ottico continuo emesso dal laser. La luce modulata viene quindi iniettata nella Fibra Ottica in Test (FUT). Dopo aver percorso l'intera lunghezza della fibra, il segnale ottico viene riconvertito in un segnale elettrico dal fotodilevatore e infine inviato all'ingresso 'B' del Vector Voltmeter, portando l'informazione di fase $\Phi_B$.

La differenza di fase $\Delta\Phi = \Phi_B - \Phi_A$, misurata dallo strumento, è direttamente correlata al ritardo introdotto dalla FUT alla specifica lunghezza d'onda impostata. La descrizione di questo apparato pone le basi per la procedura di misura dettagliata nella sezione seguente.

---

# 3.0 Procedura di Misurazione

Data l'estrema sensibilità della misura di fase a fattori esterni come le variazioni di temperatura e la deriva termica della strumentazione, l'adozione di una procedura metodica, rigorosa e rapida è fondamentale per ottenere dati affidabili e ripetibili.

## 3.1 Impostazioni Preliminari

Prima di avviare l'acquisizione dei dati, è necessario effettuare un'impostazione preliminare critica. Agendo sul controllore di polarizzazione, si massimizza l'ampiezza del segnale misurato sul Canale B del Vector Voltmeter. Questa operazione garantisce che il modulatore operi nel suo punto di lavoro ottimale e che il segnale in arrivo al fotodilevatore abbia la massima potenza possibile, migliorando così il rapporto segnale/rumore della misura di fase.

## 3.2 Acquisizione del Dato di Fase

L'esperimento si concentra sulla lettura della differenza di fase $\Delta\Phi = \Phi_B - \Phi_A$ fornita dal Vector Voltmeter. La lettura dello strumento, di tipo analogico, richiede l'interpretazione combinata di tre elementi:

- **Lettura dell'indice:** Il valore angolare indicato dall'ago dello strumento sulla scala graduata.
- **Valore di Offset:** Un offset angolare, $\Phi_{\text{offset}}$, regolabile manualmente tramite un selettore, che viene sommato algebricamente alla lettura dell'indice.
- **Range (Scala):** La scala di misura selezionata (es. $\pm 60^\circ$, $\pm 18^\circ$), che determina il fondo scala e la risoluzione della lettura.

L'angolo di fase totale per una data lunghezza d'onda $\lambda$ è quindi calcolato tramite la seguente formula:

$$\Phi_{\text{totale}} = \Phi_{\text{indicato}} + \Phi_{\text{offset}}$$

Le scale di misura consigliate per l'esperimento, con le relative risoluzioni, sono riassunte nella tabella seguente.

| Range Selezionato | Risoluzione per Divisione | Scala di Lettura |
|---|---|---|
| $\pm 60^\circ$ | $2^\circ$ | Superiore (valori x10) |
| $\pm 18^\circ$ | $0.5^\circ$ | Inferiore |
| $\pm 6^\circ$ | $0.2^\circ$ | Superiore |

## 3.3 Svolgimento della Misura

La raccolta dei dati è stata eseguita seguendo una procedura sequenziale:

1. Impostare la lunghezza d'onda iniziale del laser (es. $1550\ \text{nm}$).
2. Leggere e annotare il valore di fase indicato sull'indice e l'offset impostato, calcolando il valore di fase totale.
3. Incrementare la lunghezza d'onda del laser di un passo costante (es. $1\ \text{nm}$).
4. Ripetere la lettura di fase per la nuova lunghezza d'onda.
5. Durante l'acquisizione, sono stati necessari aggiustamenti dinamici per mantenere la misura accurata e all'interno del range dello strumento:
    - **Aggiustamento dell'Offset:** Quando l'indice si avvicinava a uno dei due estremi della scala, l'offset veniva modificato per riportare l'indice in una zona centrale, più comoda e precisa per la lettura, prima di procedere con gli step successivi.
    - **Cambio di Range:** Man mano che la scansione in lunghezza d'onda si avvicinava al vertice della parabola del ritardo di gruppo, la pendenza della curva diminuiva. Di conseguenza, la variazione di fase tra step consecutivi diventava troppo piccola per essere apprezzata sulla scala a bassa risoluzione ($\pm 60^\circ$). In questi casi, è stato necessario passare a una scala con risoluzione maggiore (es. $\pm 18^\circ$) per non perdere accuratezza nella misura.

## 3.4 Raccomandazioni Operative

Per garantire la massima qualità e coerenza dei dati raccolti, sono state seguite tre raccomandazioni operative critiche:

- **Velocità:** È imperativo eseguire la sequenza di letture con la massima celerità possibile per minimizzare l'impatto della deriva termica dello strumento e delle fluttuazioni ambientali, che possono alterare il riferimento di fase nel tempo.
- **Irreversibilità:** Qualsiasi inversione nella scansione della lunghezza d'onda ($\lambda$) è da ritenersi inammissibile. Tale operazione potrebbe alterare le condizioni interne del laser, causando la perdita del riferimento di fase iniziale e invalidando la sequenza di misure. Eventuali dati mancanti devono essere gestiti in fase di post-processing.
- **Lettura Ortogonale:** È necessario posizionarsi sempre perfettamente di fronte allo strumento per la lettura, in modo da non vedere l'ombra dell'indice riflessa sullo specchio presente lungo la scala graduata. Questo previene l'errore di parallasse e assicura una lettura precisa del valore.

Il completamento di questa procedura ha permesso di ottenere una tabella di valori di fase in funzione della lunghezza d'onda, pronta per la successiva fase di analisi.

---

# 4.0 Analisi dei Dati e Risultati

Il processo di analisi ha l'obiettivo di trasformare la serie di misure di fase grezze, ottenute sperimentalmente, in parametri fisici significativi per la fibra ottica: prima il ritardo di gruppo relativo ($\tau$) e, infine, il coefficiente di dispersione cromatica ($D$), che è l'obiettivo finale della caratterizzazione.

## 4.1 Calcolo del Ritardo di Gruppo ($\tau$)

Il ritardo di gruppo relativo ($\tau$) è direttamente proporzionale alla differenza di fase misurata ($\Phi$). La relazione che lega le due grandezze è data dalla seguente formula, dove $\Phi_{\text{rad}}$ deve essere espresso in radianti e $F$ è la frequenza di modulazione ($850\ \text{MHz}$):

$$\tau = \left(\frac{\Phi_{\text{rad}}}{2\pi}\right) \cdot \left(\frac{1}{F}\right)$$

Una volta calcolato il valore di $\tau$ per ogni lunghezza d'onda ($\lambda$), il grafico di $\tau$ in funzione di $\lambda$ ha confermato l'andamento **parabolico** atteso dalla teoria. Un'osservazione importante riguarda la presenza di valori negativi per il ritardo di gruppo. Questo non rappresenta un'impossibilità fisica, ma è una diretta conseguenza del carattere _relativo_ della misura di fase ($\Delta\Phi = \Phi_B - \Phi_A$). Un ritardo $\tau$ negativo indica semplicemente che, per quelle specifiche lunghezze d'onda, il segnale sul canale di misura (B) presenta un _anticipo_ di fase rispetto al segnale sul canale di riferimento (A).

## 4.2 Calcolo del Coefficiente di Dispersione ($D$)

Il coefficiente di dispersione cromatica, $D$, è definito come la derivata del ritardo di gruppo rispetto alla lunghezza d'onda. Esso quantifica la variazione del ritardo per unità di variazione della lunghezza d'onda ed è tipicamente espresso in $\mathbf{\text{ps}/(\text{nm}\cdot\text{km})}$.

$$D = \frac{1}{L} \frac{d\tau}{d\lambda}$$

Operando su un set di dati discreti, la derivata viene approssimata calcolando il rapporto incrementale tra punti adiacenti. Se si considera la lunghezza $L$ della fibra nella normalizzazione:

$$D(\lambda_i) \approx \frac{1}{L} \cdot \frac{\tau(\lambda_i) - \tau(\lambda_{i-1})}{\lambda_i - \lambda_{i-1}}$$

Il coefficiente di dispersione $D$, espresso in $\text{ps}/(\text{nm}\cdot\text{km})$, viene quindi plottato in funzione della lunghezza d'onda ($\lambda$). Il grafico del coefficiente $D$ in funzione di $\lambda$ ha mostrato che i punti si dispongono lungo una **retta**, in accordo con il fatto che la derivata di una parabola è una funzione lineare. Le deviazioni osservate da una retta perfetta sono attribuibili alle inevitabili imprecisioni e agli errori casuali introdotti durante la fase di acquisizione manuale dei dati.

## 4.3 Determinazione della Lunghezza d'Onda a Dispersione Nulla ($\lambda_0$)

Un parametro fondamentale per la caratterizzazione di una fibra ottica è la sua lunghezza d'onda a dispersione nulla ($\lambda_0$), ovvero la lunghezza d'onda alla quale il coefficiente di dispersione si annulla ($\mathbf{D = 0}$). A questa lunghezza d'onda, l'allargamento dell'impulso dovuto alla dispersione cromatica del secondo ordine è minimo.

Graficamente, $\lambda_0$ è stata identificata come il punto di intersezione della retta $D(\lambda)$ con l'asse delle ascisse ($D=0$). Dall'analisi visiva dei dati, questo valore è stato stimato essere nell'intorno di $\mathbf{1580-1581\ \text{nm}}$. Per una stima più accurata e robusta di $\lambda_0$, si raccomanda l'applicazione di un fit lineare ai dati sperimentali di $D(\lambda)$.

Questi risultati quantitativi completano la caratterizzazione della fibra, fornendo i parametri necessari per la sua valutazione e il suo impiego in un sistema di comunicazione.

---

# 5.0 Conclusioni

L'esperimento documentato in questa relazione ha permesso di caratterizzare con successo le proprietà dispersive di una fibra ottica monomodale. Attraverso la misura della variazione di fase ($\Phi$) di un segnale modulato in funzione della lunghezza d'onda ($\lambda$), è stato possibile ricostruire l'andamento del ritardo di gruppo ($\tau$), confermandone la natura parabolica. La successiva derivazione numerica ha fornito una stima del coefficiente di dispersione cromatica ($D$) e del suo andamento lineare.

Il risultato principale dell'analisi è stata la determinazione della lunghezza d'onda a dispersione nulla, $\lambda_0$, stimata attorno a $\mathbf{1580-1581\ \text{nm}}$. Questo valore è cruciale poiché permette di identificare la tipologia di fibra analizzata (ad esempio, una fibra a dispersione spostata non nulla, o NZ-DSF) e di definirne il regime operativo ottimale. Le deviazioni dei dati calcolati di $D$ da un andamento perfettamente lineare evidenziano le fonti di errore intrinseche alla misurazione manuale. Si raccomanda, pertanto, un'analisi di post-processing, come l'esecuzione di un fit lineare sui dati, per migliorare l'accuratezza dei parametri finali e fornire una stima più robusta del coefficiente di dispersione e di $\lambda_0$.