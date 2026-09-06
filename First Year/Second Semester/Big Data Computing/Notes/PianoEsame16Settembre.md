# Piano di studio - Esame Big Data Computing, 16 settembre

## Obiettivo e ipotesi

Piano dal 4 al 15 settembre, assumendo circa 5 ore nette al giorno. Se il tempo disponibile è
minore, conserva l'ordine delle attività e riduci il numero di esercizi, non le simulazioni.

Obiettivo prudente: arrivare a una prestazione stabile da almeno 20/28, sopra la soglia di 16/28.

## Struttura dello scritto

Secondo `Slides/Exercises/Exams/exam rules.txt`:

- 28 punti in 2 ore e 30 minuti;
- domande di teoria ed esercizi;
- soglia minima di 16 punti nello scritto;
- struttura uguale ai cinque `ExampleWT`, con possibile lieve aumento della lunghezza;
- eventuali domande sugli homework riguarderanno gli homework di quest'anno.

I cinque esempi hanno una struttura estremamente regolare:

- Parte 1: quattro domande brevi, normalmente da 3, 3, 3 e 4 punti;
- Parte 2: due esercizi lunghi, normalmente da 7 e 6 punti;
- un esercizio lungo di MapReduce compare in tutti i cinque esempi;
- il secondo esercizio lungo riguarda quasi sempre streaming/sketch, con similarity search come
  variante possibile;
- MapReduce/Spark, clustering/coreset e streaming compaiono in tutti i cinque esempi;
- similarity search compare in quattro esempi su cinque.

## Priorità

### Priorità A - padronanza obbligatoria

1. **Progettazione MapReduce e analisi di spazio**
   - specifica di input e output;
   - coppie emesse da map e reduce in ogni round;
   - partizionamento deterministico o casuale in $\sqrt{N}$ gruppi;
   - deduplicazione, conteggio parziale e aggregazione finale;
   - dimostrazione separata di $M_L=o(N)$ e $M_A=O(N)$;
   - effetto di parametri come $K$, $k$, $L$ o $t$.

2. **Streaming e sketch**
   - Reservoir Sampling e probabilità condizionate;
   - Sticky Sampling: algoritmo, $r$, memoria, false positive/negative e garanzie;
   - probabilistic counting per $F_0$ e median trick;
   - Count-Min: update, query con minimo, errore unilaterale;
   - Count Sketch: segni casuali, stima non distorta, mediana;
   - stima di $F_2$ come somma dei quadrati dei contatori;
   - Bloom filter: inizializzazione, query, assenza di falsi negativi, probabilità di zero.

3. **Clustering, coreset e homework Fair k-Center**
   - obiettivi di $k$-center, $k$-means e $k$-median;
   - FFT e prova della 2-approssimazione;
   - MR-FFT: due round, coreset, $M_L$, $M_A$, qualità 4-approssimata;
   - diametro: $\Delta(T)\leq\Delta(P)\leq\Delta(T)+2R$;
   - coreset composabili: vantaggi, limiti e confronto con campionamento casuale;
   - Fair-FFT e MR-Fair-FFT: quote $k_A,k_B$, oversampling, dimensione del coreset,
     `mapPartitions`, costo e limiti implementativi.

### Priorità B - punti relativamente economici

4. **Similarity search**
   - differenze tra $r$-NNS, Range Reporting e $(c,r)$-ANNS;
   - kd-tree: definizione, query RR, spazio $O(n)$ e tempo $O(\sqrt n+k)$ in $\mathbb{R}^2$;
   - definizione LSH $(p_1,p_2,c,r)$;
   - tabella LSH base, garanzia di successo e tempo atteso $O(Dnp_2)$;
   - bit sampling per Hamming e costruzioni AND/OR.

5. **Spark, Word Count e homework Frequent Items**
   - RDD, lineage, trasformazioni, azioni e lazy evaluation;
   - perché una misura di tempo senza action è ingannevole;
   - `groupByKey`, `reduceByKey`, `mapPartitions` e shuffle;
   - micro-batch Spark Streaming e stato aggiornato sul driver;
   - confronto operativo Sticky Sampling/Count-Min dell'homework;
   - ruolo di $\epsilon,\delta,\phi,d,w$ e trend sperimentali.

### Priorità C - studiare solo dopo A e B

- catalogo completo delle distanze: basta saper scegliere e definire quelle principali;
- dettagli storici, piattaforme, deployment mode e API secondarie di Spark;
- dimostrazioni complete di tutti i risultati su diversity maximization;
- Lloyd e PAM oltre a definizione, limite principale e versione pesata;
- famiglie hash pratiche e aritmetica dei primi di Mersenne;
- vecchi homework su outlier, node coloring, silhouette o fair itemset: non sono homework 2025-26;
- dettagli di codice riga per riga: servono flusso, costi, scelte progettuali e limiti.

## Metodo giornaliero

Ogni giornata usa quattro blocchi:

1. 75 minuti: richiamo attivo della teoria, partendo da foglio bianco;
2. 120 minuti: esercizi, senza guardare le soluzioni per i primi 45-60 minuti;
3. 75 minuti: una o due prove scritte in forma corta;
4. 30-45 minuti: correzione e aggiornamento del registro errori.

Non rileggere passivamente un intero file. Per ogni argomento:

1. leggi la sezione pertinente e la tabella finale della nota primaria;
2. chiudi la nota e scrivi definizione, algoritmo, garanzia e costo;
3. risolvi almeno un esercizio ufficiale;
4. consulta `TheoremsDefinitionsProofs.md` o `BDC_proofs.md` solo per correggere lacune;
5. rispondi a 2-3 domande da `ExamStyleQuestions.md` con limite di tempo.

## Calendario 4-15 settembre

### 4 settembre - diagnostica e formato

- Leggi regole e tutti i cinque test senza svolgerli.
- Rispondi, in 50 minuti, a quattro domande brevi miste da `ExamStyleQuestions.md`.
- In 40 minuti, abbozza un esercizio MapReduce e uno sketch.
- Crea un registro con quattro colonne: errore, causa, risposta corretta, data di riesame.
- Ripassa solo prerequisiti emersi come mancanti.

Risultato atteso: sapere quali aree sono rosse, gialle e verdi.

### 5 settembre - MapReduce fondamentale

- Studia `1.MapReduce2526.md`: round, $R$, $M_L$, $M_A$, design goals.
- Impara i due schemi di partizionamento in $\sqrt N$ gruppi.
- Svolgi `EX-MR2526`, esercizi 1-3.
- Scrivi da memoria prova del load bound casuale: variabile, aspettativa, Chernoff, union bound.

Risultato atteso: progettare aggregazioni in 2-3 round senza creare un reducer da $\Theta(N)$.

### 6 settembre - Spark, Word Count e homework 1

- Studia `2.Spark2526.md` e `3.WordCountSpark.md` solo sulle sezioni ad alta priorità.
- Prepara risposte da 3 punti su RDD, lazy evaluation, shuffle e `mapPartitions`.
- Studia `PROJECT_DESCRIPTIONS_EXAM.md`, Project 1.
- Spiega Fair-FFT e MR-Fair-FFT senza codice; calcola dimensione del coreset e costi.
- Rispondi a una variante: cosa cambia aumentando numero di partizioni $L$?

Risultato atteso: collegare modello MapReduce, implementazione Spark e progetto svolto.

### 7 settembre - clustering e FFT

- Studia `4.Coreset2526-1.md`.
- Memorizza tre funzioni obiettivo e nozione di $c$-approssimazione.
- Scrivi prova FFT 2-approx senza note.
- Scrivi schema MR-FFT, prova del coreset e derivazione della 4-approx.
- Svolgi `EX-CTCL2526`, esercizi 2-5.

Risultato atteso: risposte corte precise e una prova completa in 12-15 minuti.

### 8 settembre - coreset avanzati e diametro

- Studia `5.Coreset2526-2.md`: diametro, k-means pesato e MR-kmeans.
- Dai meno spazio a diversity, Lloyd e PAM.
- Svolgi `EX-CTCL2526`, esercizi 6-9 e 11-13; scegline almeno tre, privilegiando MR.
- Prova da memoria $\Delta(T)\leq\Delta(P)\leq\Delta(T)+2R$.
- Ripeti Fair k-Center confrontandolo con k-center standard.

Risultato atteso: gestire domande 2025 su diametro e varianti MR di clustering.

### 9 settembre - streaming, campionamento e Sticky Sampling

- Studia `6. Streaming2526-1.md`.
- Scrivi algoritmo e prova di Reservoir Sampling.
- Scrivi algoritmo, memoria e garanzie di Sticky Sampling.
- Svolgi `EX-STR2526`, esercizi 1-6.
- Studia `PROJECT_DESCRIPTIONS_EXAM.md`, Project 2: pipeline Spark Streaming e confronto
  Sticky/Count-Min.

Risultato atteso: distinguere chiaramente stima, errore, probabilità e memoria.

### 10 settembre - sketch e Bloom filter

- Studia `7.Streaming2526-2.md` fino a Bloom filter incluso.
- Ricostruisci da memoria tabelle Count-Min e Count Sketch.
- Scrivi prove corte: Count Sketch non distorto; stima $F_2$ non distorta; Bloom senza falsi
  negativi.
- Svolgi `EX-STR2526`, esercizi 7-11.
- Dedica massimo 30 minuti a hash universali e fingerprinting.

Risultato atteso: riconoscere quale sketch usare e derivarne update, query e garanzia.

### 11 settembre - similarity search

- Studia `8.SimSearch2526-1.md` e `9SimSearch2526-2.md`.
- Impara definizioni RR, NNS, ANNS, kd-tree e LSH.
- Scrivi prova del tempo atteso $O(Dnp_2)$ della LSH base.
- Svolgi tutti e tre gli esercizi di `EX-SIMSEARCH2526.pdf`.
- Chiudi con quattro risposte da 3-4 punti, massimo 12 minuti ciascuna.

Risultato atteso: ottenere punti rapidi su definizioni e garanzie, senza confondere problemi.

### 12 settembre - giornata mista e progetti

- Risolvi due esercizi MapReduce non ancora svolti: uno da `EX-MR2526`, uno da
  `EX-CTCL2526`.
- Risolvi un esercizio Count-Min/Count Sketch e uno LSH/Bloom.
- Prepara otto domande possibili sugli homework: quattro per Fair k-Center, quattro per
  Frequent Items.
- Per ogni progetto prepara una risposta da 90 secondi e una da 4 punti.
- Ripassa solo errori registrati almeno due volte.

Risultato atteso: passare tra argomenti senza bisogno di riscaldamento.

### 13 settembre - simulazione 1

- Svolgi `ExampleWT-2.pdf` in 120 minuti, senza note.
- Usa 30 minuti aggiuntivi per rileggere e completare motivazioni, simulando formato nuovo.
- Correggi con note e soluzioni degli esercizi ufficiali.
- Riscrivi interamente ogni risposta sotto metà punteggio.

Obiettivo: almeno 18/26 usando una valutazione severa.

### 14 settembre - simulazione 2

- Svolgi `ExampleWT-4.pdf` in 120 minuti, senza note.
- Nei 30 minuti restanti, sostituisci domanda sul vecchio homework con una domanda su uno dei
  progetti 2025-26.
- Correggi subito; ripassa solo i tre errori con maggiore perdita di punti.

Obiettivo: almeno 20/26 e nessun esercizio lasciato senza struttura.

### 15 settembre - prova finale e consolidamento

- Svolgi `ExampleWT-5.pdf` in 120 minuti: è particolarmente importante perché coincide quasi
  interamente con lo scritto del 18/06/2025.
- Usa 20 minuti per controllo finale e 10 minuti per una domanda sul progetto corrente.
- Correggi, poi ripeti formule e schemi dal registro errori.
- Termina studio pesante entro sera; niente nuovi argomenti.

Obiettivo: almeno 21/26, risposte concise, analisi di spazio completa.

## Prove da sapere ricostruire

Ordine di rendimento:

1. FFT è una 2-approssimazione;
2. partizionamento casuale bilanciato con Chernoff e union bound;
3. bound del diametro tramite coreset e disuguaglianza triangolare;
4. garanzie e memoria di Sticky Sampling;
5. Count Sketch e stima di $F_2$ non distorte;
6. Count-Min: errore additivo e amplificazione con minimo;
7. Bloom filter: nessun falso negativo e false-positive rate;
8. LSH base: correttezza probabilistica e tempo atteso;
9. MR-FFT: qualità del coreset e 4-approssimazione;
10. Reservoir Sampling: probabilità uniforme $m/t$.

Per ogni prova memorizza struttura, non testo: ipotesi, variabili casuali o punti scelti,
disuguaglianza chiave, conclusione.

## Template per esercizi MapReduce

Scrivi sempre in questo ordine:

1. input e output;
2. Round 1: map, chiave di partizione, reduce, coppie emesse;
3. Round successivi nello stesso formato;
4. perché output è corretto;
5. massimo input/output di ogni singolo reducer, quindi $M_L$;
6. numero totale di coppie per ogni round, quindi $M_A$;
7. effetto dei parametri o caso limite richiesto.

Errore tipico da evitare: affermare $M_A=O(N)$ senza contare coppie intermedie, oppure usare un
reducer finale che può ricevere $N$ elementi.

## Strategia nei 150 minuti

- 5 minuti: leggi tutto e marca domande sicure, medie e rischiose.
- 50 minuti: Parte 1; circa 11-13 minuti per domanda.
- 80 minuti: Parte 2; circa 40 minuti per esercizio.
- 15 minuti: controllo di formule, indici, soglie, $M_L$, $M_A$ e risposte mancanti.

Se un esercizio lungo blocca per oltre 8 minuti, scrivi almeno input/output, round plausibili e
analisi parziale; poi passa oltre. Una struttura corretta può ottenere punti anche senza soluzione
perfetta.

Risposte brevi: definizione, formula/algoritmo, garanzia o costo, una motivazione. Gli esempi
avvertono che risposte eccessivamente lunghe vengono penalizzate.

## Checklist finale

Alla sera del 15 settembre dovresti saper fare senza note:

- [ ] progettare un MR in 2-3 round con $M_L=o(N)$ e $M_A=O(N)$;
- [ ] spiegare RDD, lazy evaluation, shuffle e `mapPartitions`;
- [ ] scrivere obiettivi di k-center, k-means, k-median e fair k-center;
- [ ] provare FFT 2-approx e bound del diametro;
- [ ] descrivere MR-FFT, Fair-FFT e MR-Fair-FFT con costi;
- [ ] distinguere Reservoir, Sticky, Count-Min, Count Sketch e probabilistic counting;
- [ ] derivare query e garanzia di Bloom filter;
- [ ] definire RR, NNS, ANNS, kd-tree e LSH;
- [ ] spiegare entrambi gli homework 2025-26, inclusi parametri e limiti;
- [ ] completare almeno due simulazioni consecutive sopra 18/26.

## Materiali da usare come indice, non da rileggere integralmente

- `ExamStyleQuestions.md`: banca di domande per richiamo attivo;
- `TheoremsDefinitionsProofs.md`: formulario completo e correzione delle prove;
- `BDC_proofs.md`: seconda spiegazione quando una prova non è chiara;
- `PROJECT_DESCRIPTIONS_EXAM.md`: preparazione mirata agli homework.

Le note 8 e 9 di Similarity Search non hanno, al momento, PDF corrispondenti nella cartella
`Slides/`; per quel modulo usa note ed esercizi `EX-SIMSEARCH2526.pdf`.
