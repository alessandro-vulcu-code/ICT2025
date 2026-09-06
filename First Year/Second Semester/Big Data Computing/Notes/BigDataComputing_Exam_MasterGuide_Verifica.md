# Verifica della Big Data Computing Exam Master Guide

Data: 6 settembre 2026.

Documento verificato: [[BigDataComputing_Exam_MasterGuide]], versione di 3061 righe.
I numeri di riga riportati sotto si riferiscono a questa versione, lasciata invariata.

## Esito

**Le dimostrazioni presenti in `Slides/Theory/BDC_proofs.pdf` sono tutte coperte nella guida,
con i passaggi matematici essenziali. Non ho trovato una dimostrazione del PDF mancante
o ridotta al solo enunciato.** Il confronto comprende l'ispezione visiva delle 24 pagine:
il PDF è composto da scansioni e non contiene testo estraibile utile.

**La guida non è però una sostituzione integralmente completa di `Notes/`.** Sono assenti
alcune applicazioni, definizioni, dettagli Spark e limitazioni dei progetti. Ho inoltre
individuato due formulazioni concettuali da correggere e una condizione asintotica da precisare.
Le prove centrali di clustering, streaming e similarity search risultano solide nelle ipotesi
esplicitate. Questo esito distingue la copertura delle prove dalla copertura di tutti i contenuti.

## Correzioni e precisazioni

### 1. `reduceByKey`: manca la commutatività

- **Guida:** riga 561, sezione 4.3.
- **Fonte locale:** [[3.WordCountSpark#More Efficient: reduceByKey]], righe 205-211;
  [[TheoremsDefinitionsProofs#Definition - `reduceByKey`]].
- **Problema:** la tabella richiede un merge associativo, ma omette la commutatività.
  Una funzione associativa come la concatenazione di stringhe non garantisce un risultato
  indipendente dall'ordine delle aggregazioni distribuite.
- **Correzione proposta:** specificare «associative and commutative merge».

Il requisito è confermato dalla
[documentazione ufficiale di `RDD.reduceByKey`](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.reduceByKey.html).

### 2. Definizione di sketch troppo restrittiva

- **Guida:** righe 1369-1371, sezione 6.1.
- **Fonte:** [[7.Streaming2526-2#Sketching]].
- **Problema:** «sketching ... stores randomized linear summaries» presenta la linearità
  come proprietà generale. Count-Min e Count Sketch sono lineari nel vettore delle frequenze;
  il registro di Probabilistic Counting, aggiornato tramite massimo, non lo è.
- **Correzione proposta:** definire gli sketch come riassunti compatti per stimare proprietà
  dei dati, spesso randomizzati; specificare separatamente che gli sketch di frequenza trattati
  sono lineari e possono essere sommati quando parametri e hash coincidono.

### 3. La scelta `L ~ N/k` richiede un'ipotesi aggiuntiva

- **Guida:** righe 1333-1334, esercizio sulle query globali del 08/09/2023.
- **Problema:** la frase «For k=o(N) ... O(k+N/k)=o(N)» è troppo generale se letta da sola.
  Occorre anche che `k` tenda all'infinito. Per `k=1`, la scelta proposta dà `L=N`;
  il reducer dell'unica query riceve `N` candidati e usa spazio lineare.
- **Precisazione:** nel ramo precedente `k > sqrt(N)` la conclusione è corretta.
  Basta dichiarare che il retuning riguarda quel ramo.
- **Alternativa valida per ogni `1 <= k = o(N)`:** mantenere `L` dell'ordine di
  `min(sqrt(N), N/k)`. Si ottengono spazio locale `O(max(sqrt(N),k))` e aggregato `O(N)`.

## Omissioni rispetto agli appunti

### 4. Count-Min per stimare la dimensione di un join

- **Fonte:** [[7.Streaming2526-2#Applications]], righe 400-420.
- **Guida:** sezione 6.6, applicazione assente.
- **Impatto:** manca un impiego dello sketch diverso dalla singola frequenza.

Per un equijoin su un attributo, con frequenze `a_u` e `b_u`, la dimensione esatta è
la somma dei prodotti delle frequenze della stessa chiave. Due Count-Min compatibili,
con gli stessi hash, permettono la stima:

$$
\widehat J=\min_j\sum_{b=0}^{w-1}C_A[j,b]C_B[j,b].
$$

Espandendo una riga, i prodotti della stessa chiave danno il join esatto; le collisioni
fra chiavi diverse aggiungono termini nonnegativi. Questo spiega la sovrastima e il minimo
fra righe. Gli appunti presentano l'applicazione, non una nuova prova nel PDF manoscritto.

### 5. Spark e Word Count: copertura operativa parziale

Fonti: [[2.Spark2526]], [[3.WordCountSpark]] e domande dedicate in [[ExamStyleQuestions]].
Nel capitolo 4 mancano o sono solo impliciti:

- `SparkContext` e la sua funzione nell'architettura;
- differenza fra persistenza `MEMORY_ONLY` e `MEMORY_AND_DISK`, soprattutto quando la RAM
  non basta;
- `repartition(L)`, costo dello shuffle e perdita di bilanciamento dopo trasformazioni;
- `mapValues` e pipeline `groupByKey` seguita da `mapValues`;
- pipeline concrete delle due varianti Word Count: chiavi casuali e `mapPartitions`;
- distinzione Java fra `mapToPair`/`flatMapToPair` e metodi Python;
- definizione di Dataset, oltre al breve riferimento ai DataFrame;
- passaggio di funzioni nominate e lambda, trattato negli appunti di Word Count.

Non serve riprodurre tutti gli esempi Java e Python per conservare le prove. Servono però
integrazioni se la guida deve consentire di rispondere a tutte le domande Spark già presenti
nel workspace. Ad esempio, la domanda sul comportamento della cache con RAM insufficiente
non trova una risposta esplicita nella guida.

### 6. Homework: mancano limitazioni concrete già documentate

Fonte: [[PROJECT_DESCRIPTIONS_EXAM]], sezioni sui dettagli implementativi dei due progetti.

**HW1, sezione 8.1 della guida:** vengono descritte precondizioni e selezione di centri distinti,
ma non sono riportate le differenze rispetto al codice descritto negli appunti:

- assenza di un controllo esplicito delle quote globali;
- mancata esclusione esplicita dei punti già selezionati;
- possibili quote locali superiori ai punti disponibili di un gruppo;
- interpretazione di etichette diverse da `A` come `B`;
- esperimento `AllA` con quota B positiva e nessun punto B, quindi non ammissibile.

La fattibilità globale non implica quella delle quote `2*k_A`, `2*k_B` in ogni partizione.
La guida dovrebbe specificare il comportamento desiderato nei gruppi locali insufficienti
e distinguere algoritmo ideale da limiti dell'implementazione descritta nella fonte.
Le osservazioni qui sono verificate rispetto agli appunti, non tramite una nuova esecuzione
del codice degli homework.

**HW2, sezione 8.2 della guida:** manca il limite dell'hash
`((a*x+b) mod 8191) mod w`. Due chiavi congruenti modulo 8191 collidono in ogni riga.
Per esempio `1` e `8192` non possono essere distinte da questo schema.
Sul dominio di interi arbitrari non si può quindi trasferire automaticamente il teorema
di universalità della sezione 6.10. Aumentare il numero di righe non elimina queste collisioni.

### 7. Definizioni e costi secondari da integrare

| Contenuto | Fonte in Notes | Stato nella guida |
|---|---|---|
| Formula generale della distanza di Minkowski | `4.Coreset2526-1`, distanza `L_r` | Presenti solo i casi 1, 2 e infinito; per una metrica generale richiedere `r >= 1` |
| Definizione formale di problema di ottimizzazione e di partizione in k cluster | `4.Coreset2526-1`; `TheoremsDefinitionsProofs` | Obiettivi e fattore di approssimazione presenti, definizioni astratte abbreviate |
| k-nearest neighbors, r-near neighbor reporting, similarity join | `8.SimSearch2526-1`, Related Problems | Non definiti; k-nearest neighbors compare solo fra le confusioni da evitare |
| Costi di Count Sketch per frequenza e secondo momento | `7.Streaming2526-2`, Performance Metrics | Mancano le dichiarazioni esplicite `O(d)` e `O(dw)` per le due query standard |
| Tempo di Probabilistic Counting nel modello di costo del corso | `7.Streaming2526-2`, High-Probability Guarantees | Memoria discussa, tempo `O(log |U|)` non riportato |
| Costo di una query Bloom | `7.Streaming2526-2`, Initialization and Query | Procedura presente, tempo `O(k)` non esplicitato |
| Batches di Sticky con n sconosciuto | `6. Streaming2526-1`, Extension to Unknown n | Idea presente, omesse formule delle dimensioni `2^i*r` e del rate `2^-i` |
| Bucket secondari per LSH euclideo | `9SimSearch2526-2`, Practical Bucket Implementation | Non descritti |
| Silhouette media, domanda di un vecchio esame | `ExamStyleQuestions`, riferimento 29/06/2023 | Assente; la fonte riporta la domanda, non la soluzione |

La silhouette non appartiene alle prove di `Slides/Theory`. La sua assenza è però rilevante
per la dichiarazione della sezione 11 che la guida copra le vecchie domande disponibili.
Il calendario di [[PianoEsame16Settembre]] è materiale organizzativo: non occorre duplicarlo
per rendere completa la teoria.

## Mappa delle 24 pagine di Slides/Theory

In questa cartella è presente un solo file: `BDC_proofs.pdf`.
«Completa» indica che la guida contiene enunciato o problema, ipotesi necessarie e passaggi
essenziali della dimostrazione, anche con notazione diversa o tramite un lemma già provato.
Gli esempi numerici e le figure delle pagine non sono tutti riprodotti.

| Pagina PDF | Contenuto | Sezione guida | Verifica |
|---|---|---|---|
| 1 | MTBF e analisi Word Count a un round | 3.2; 4.3 | Complete |
| 2 | Class Count, skew e partizionamento deterministico | 3.1; 3.3; 3.4 | Coperto tramite schema generale di aggregazione |
| 3 | Class Count con partizionamento casuale | 3.3; 3.4 | Completa l'analisi del massimo carico |
| 4 | Indicatori, Chernoff sul singolo carico | 2; 3.3 | Completa |
| 5 | Union bound sui carichi | 3.3 | Completa |
| 6 | Separazione dei punti scelti da FFT | 5.3 | Completa |
| 7 | Pigeonhole e fattore 2 di FFT | 5.3 | Completa |
| 8 | Lemma di qualità dei coreset locali | 5.4 | Completa |
| 9 | Spazio MR-FFT e percorso tramite proxy | 5.5 | Completa |
| 10 | Fattore 4 di MR-FFT | 5.5 | Completa |
| 11 | Controesempio al campionamento uniforme | 5.6 | Completo, anche senza replacement |
| 12 | Diametro da un punto e copertura con rappresentanti | 5.7 | Entrambe complete |
| 13 | Proxy iniettivi per diversity e perdita per coppia | 5.10 | Completa |
| 14 | Dalla perdita additiva al coreset moltiplicativo | 5.10 | Completa, conversione del fattore precisata |
| 15 | Boyer-Moore: esempio e invariante | 6.2; STR-1 | Invariante provato; traccia numerica non riprodotta |
| 16 | Contraddizione con l'esistenza della maggioranza | 6.2 | Completa |
| 17 | Induzione per Reservoir Sampling | 6.3 | Completa; forma equivalente con probabilità di sopravvivenza |
| 18 | Sticky: spazio atteso e correttezza simultanea | 6.4 | Completa, inclusi ceiling e probabilità limitata a 1 |
| 19 | Probabilistic Counting: trailing zeros e intuizione | 6.5 | Coperta; la guida aggiunge prove delle code |
| 20 | Count-Min: errore atteso, Markov e righe indipendenti | 6.6 | Completa |
| 21 | Count Sketch: contributi firmati e attesa nulla | 6.7 | Completa |
| 22 | Linearità e non distorsione della singola riga | 6.7 | Completa |
| 23 | Bloom: probabilità di bit zero e falso positivo | 6.9 | Derivazione completa nel modello approssimato dichiarato |
| 24 | LSH: correttezza e costo atteso con arresto anticipato | 7.3 | Completa, incluso il termine additivo del costo |

Non sono lacune della guida le prove originali di k-means++, dell'algoritmo sequenziale
di diversity e del rapporto delle famiglie euclidee migliorate: le fonti locali ne danno
gli enunciati senza svilupparle, e la guida lo dichiara. La prova MR-kmeans presente in
[[BDC_proofs]] è inclusa in 5.9, con maggior attenzione al dominio ammissibile dei centri.

## Copertura tematica dei nove appunti principali

| Fonte | Destinazione | Valutazione |
|---|---|---|
| `1.MapReduce2526.md` | Capitoli 2-4 | Modello, algoritmi e prove coperti; contesto DFS/cloud abbreviato |
| `2.Spark2526.md` | Capitolo 4 | Concetti centrali coperti; integrazioni operative necessarie |
| `3.WordCountSpark.md` | Capitolo 4 | Logica e spazio coperti; implementazioni e proprietà API parziali |
| `4.Coreset2526-1.md` | Capitolo 5 | Prove centrali complete; alcune definizioni introduttive abbreviate |
| `5.Coreset2526-2.md` | Capitolo 5 | Diametro, diversity e k-means coperti; prove e ipotesi curate |
| `6. Streaming2526-1.md` | Capitolo 6 | Prove complete; estensione a n ignoto abbreviata come indicato sopra |
| `7.Streaming2526-2.md` | Capitolo 6 | Prove coperte; mancano join e alcuni costi espliciti |
| `8.SimSearch2526-1.md` | Capitolo 7 | kd-tree e relative prove coperti; problemi correlati non tutti definiti |
| `9SimSearch2526-2.md` | Capitolo 7 | LSH e amplificazione coperti; dettaglio dei bucket secondari omesso |

## Aspetti già corretti da conservare

- La distinzione fra centri discreti e centri esterni evita confronti non giustificati
  fra ottimi su insiemi diversi.
- I diametri con copertura diretta e con rappresentanti di centri esterni usano correttamente
  le perdite additive rispettivamente `2R` e `4R`.
- La prova diversity preserva la cardinalità attraverso proxy distinti e converte correttamente
  la perdita relativa nel fattore moltiplicativo.
- La guida distingue non distorsione delle righe e accuratezza della mediana di Count Sketch.
- La stima del secondo momento usa errore relativo `epsilon*F2`, coerente con la varianza
  derivata; non ripete la formula incoerente degli appunti.
- Le probabilità di Bloom sono dichiarate approssimazioni; non vengono presentate come
  uguaglianze esatte per tutte le configurazioni.
- La prova LSH conta i candidati scartati e al massimo uno accettato, evitando ipotesi
  aggiuntive sull'ordine del bucket.
- Le code di Probabilistic Counting distinguono hash pienamente indipendenti e pairwise
  independent. Il bound più debole nel secondo caso è presentato come ciò che la prova
  fornita garantisce, non come una copia identica dell'enunciato degli appunti.

## Controlli effettuati e limiti

- Lettura della guida, confronto tematico con i nove appunti, indice delle raccolte
  [[BDC_proofs]] e [[TheoremsDefinitionsProofs]], domande e descrizioni dei progetti.
- Ispezione visiva di tutte le 24 pagine del PDF manoscritto.
- Controllo di tutti gli 11 riferimenti a immagini della guida: file presenti.
- Controllo strutturale di delimitatori di codice e matematica; non equivale a una revisione
  visuale completa del rendering Obsidian.
- Nessuna modifica alla guida; questo rapporto contiene gli interventi proposti.
- Non è una nuova verifica delle regole amministrative dell'esame né un confronto indipendente
  di tutti gli esercizi con i PDF esterni a `Slides/Theory`.
