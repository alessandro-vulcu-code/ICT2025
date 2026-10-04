# Guida operativa agli esercizi d’esame di Big Data Computing

## 1. Come usare questa guida

Gli esercizi raccolti in `Slides/Exercises/` si possono affrontare sistematicamente:
cambiano oggetti e nomi, ma ricorrono pochi schemi di costruzione e dimostrazione.
Questa guida spiega **come riconoscere lo schema, costruire la soluzione e verificarla**.
Le ricorrenze descrivono il materiale disponibile; non garantiscono il contenuto del prossimo esame.

Materiale esaminato: tutti i 12 PDF della cartella, quattro immagini, quattro
trascrizioni testuali di domande, il file delle regole e i due audio. I ricordi
informali e le trascrizioni automatiche degli audio sono distinti dalle tracce ufficiali.

Percorso consigliato:

1. Leggi la tabella decisionale e la procedura universale.
2. Studia gli schemi MapReduce e gli esempi svolti: ricorrono in molte prove.
3. Studia sketch, probabilità e geometria, ricostruendo le dimostrazioni senza guardare.
4. Usa la mappa finale per scegliere una traccia originale e risolverla a tempo.
5. Confronta la soluzione con la checklist, prima di leggere quella ufficiale.

Riferimenti interni:

- [[#2. Riconoscere il problema in un minuto]]
- [[#3. MapReduce costruire un algoritmo che rispetti lo spazio]]
- [[#4. MapReduce esempi svolti e varianti]]
- [[#5. Clustering e coreset costruire le dimostrazioni]]
- [[#6. Streaming scegliere e adattare lo stimatore]]
- [[#7. Probabilità quattro dimostrazioni riutilizzabili]]
- [[#8. Similarity search dai bucket alle garanzie]]
- [[#9. Domande brevi teoria Spark e homework]]
- [[#10. Errori nelle fonti e trappole da evitare]]
- [[#11. Mappa completa degli esercizi letti]]
- [[#12. Allenamento e checklist da esame]]

Notazione: $N$ indica solitamente la dimensione del dataset distribuito; $n$ la lunghezza
dello stream; $D$ la dimensione dei punti; $L$ il numero di partizioni; $k$ il numero
di centri. Quando uno spazio è espresso in parole, un punto costa $O(1)$ solo se $D$
è costante o se la traccia lo assume esplicitamente.

## 2. Riconoscere il problema in un minuto

| Indizio nella traccia | Domanda da farsi | Metodo |
| --- | --- | --- |
| $M_L=o(N)$, nessun limite alle occorrenze di una chiave | Una chiave può raccogliere tutto? | Partiziona, comprimi localmente, poi raggruppa |
| Somma, media, massimo globale | Posso fondere riassunti piccoli? | Albero di aggregazione |
| Esattamente $K$ record per sensore | Posso conservare $K$ candidati per partizione? | Taglio locale e taglio globale |
| Celle utilizzate, utenti distinti | Sto contando eventi o identità? | Deduplica prima di contare |
| Confronto con centri globali | Quanti valori produce ogni partizione? | Minimi/massimi/somme parziali per centro |
| Diametro, coreset, approssimazione | Quale cammino passa per i rappresentanti? | Disuguaglianza triangolare |
| $k+1$ punti, oppure $k+z+1$ | Due punti devono stare nello stesso cluster? | Principio dei cassetti |
| Vendite/resi, colori con pesi | Quale incremento definisce la frequenza richiesta? | Count Sketch con aggiornamenti pesati |
| Somma di quadrati delle frequenze | Quali termini misti si annullano in media? | Quadrati dei contatori con segni casuali |
| Unbiased, valore atteso | Posso scrivere una somma di indicatori? | Linearità dell’attesa |
| Probabilità $1-1/N$ | Che evento rende cattivo il risultato finale? | Ripetizioni indipendenti, min o mediana |
| Bloom filter da unire o ridurre | Quali bit deve poter ritrovare ogni elemento? | OR e probabilità di un bit zero |
| LSH, bit-sampling | Quali coordinate causano collisione? | Conta coordinate favorevoli su $D$ |
| kd-tree e rettangolo | Regione esclusa, contenuta o parziale? | Potatura geometrica |

### 2.1 Le sei righe da scrivere in brutta copia

1. **Input:** record e dimensione; ID consecutivi o chiavi arbitrarie?
2. **Output:** valore, coppie, insieme o multinsieme; soluzione esatta o approssimata?
3. **Ipotesi:** $k$ costante? Centri globali? Pesi negativi? Hash indipendenti?
4. **Vincoli:** round, spazio locale e aggregato; probabilità; tempo di query.
5. **Informazione da preservare:** conteggio, presenza, candidato, somma o distanza.
6. **Prova:** invariante di aggregazione, indicatori, triangolazione o cassetti.

Prima di usare una tecnica, prova il caso estremo: tutte le chiavi uguali, tutte diverse,
un solo gruppo, un solo item, distanza zero. Molti algoritmi apparentemente corretti
falliscono proprio lì.

## 3. MapReduce costruire un algoritmo che rispetti lo spazio

Fonti principali: [[Slides/Exercises/EX-MR2526.pdf]],
[[Slides/Exercises/EX-CTCL2526.pdf]] ed esercizi 1 delle prove `ExampleWT`.

### 3.1 Il modello di costo da usare

Nel modello degli esercizi, $M_L$ considera input, output e memoria di una singola
applicazione map/reduce. Un reducer che riceve $N$ valori usa spazio locale lineare,
anche se una somma potrebbe essere implementata con un solo accumulatore.

$M_A$ è il massimo spazio aggregato richiesto da una fase, considerando le strutture
e i dati pertinenti. Non coincide con il solo output finale, né con la somma dei costi
su tutti i round. Numero di record e dimensione dei loro valori vanno contati entrambi.

Obiettivi tipici:

$$
R=O(1),\qquad M_L=o(N),\qquad M_A=O(N).
$$

Un algoritmo sequenziale eseguito in un unico reducer ha un round, ma conserva
$M_L=\Theta(N)$: non raggiunge l’obiettivo di distribuzione del lavoro.

### 3.2 Partizionamento deterministico e casuale

Con ID distinti che coprono $0,\ldots,N-1$, scegli $L=\lceil\sqrt N\rceil$ e usa

$$
(i,x_i)\longmapsto(i\bmod L,x_i).
$$

Ogni partizione contiene al massimo $\lceil N/L\rceil$ record. La garanzia dipende
dagli **ID consecutivi**, non dalla sola unicità: ID distinti possono avere tutti lo
stesso resto modulo $L$.

Con URL o altre chiavi arbitrarie, assegna ciascun record indipendentemente a una
partizione uniforme. Per una partizione $j$, se $X_j$ è la sua dimensione:

$$
\mathbb E[X_j]=N/L.
$$

Per $L\simeq\sqrt N$, Chernoff e union bound danno

$$
\Pr\left(\max_jX_j\geq2N/L\right)
\leq L\exp\left(-\frac{N}{3L}\right).
$$

Quindi dimensione massima $O(\sqrt N)$ con alta probabilità. Scrivere solo l’attesa
di una partizione non dimostra il limite sul massimo. Una hash generica, senza
ipotesi sufficienti d’indipendenza, non giustifica automaticamente questa Chernoff.

### 3.3 Lo schema fondamentale in due round

**Idea:** una chiave frequente può avere $N$ occorrenze, ma dopo la compressione locale
può avere al massimo un riassunto per partizione.

```text
Round 1
  Map(i, record):
    emetti (i mod L, record)

  Reduce(partizione, lista):
    per ogni gruppo g presente nella lista:
      calcola riassunto H(g, lista)
      emetti (g, H(g, lista))

Round 2
  Map: identità

  Reduce(g, riassunti):
    fondi i riassunti
    emetti il risultato richiesto per g
```

Serve una proprietà di composizione:

$$
H(A\cup B)=\operatorname{merge}(H(A),H(B)),
$$

oppure una proprietà che garantisca almeno un output ammissibile, come nel taglio a $K$.

| Informazione richiesta | Riassunto locale | Fusione |
| --- | --- | --- |
| Frequenza | Conteggio | Somma |
| Media | Somma e numero di elementi | Somma delle due componenti, poi divisione |
| Esistenza | Un bit | OR |
| Minimo/massimo | Valore e ID del candidato | Min/max, conservando il candidato |
| Colore uniforme | $0$, $1$ oppure $-1$ per misto | Uniforme solo se tutti concordano |
| $K$ record arbitrari | Al massimo $K$ record con ID | Mantieni al massimo $K$ candidati |
| Score rispetto a $k$ centri | $k$ somme parziali | Somma per coordinata, poi argmin/argmax |

**Mai fare la media delle medie locali** senza pesare per le cardinalità.

### 3.4 Formula di spazio e scelta delle partizioni

Se ogni gruppo emette al massimo $b$ parole per partizione, una forma ricorrente è

$$
M_L=O\left(\frac NL+bL+G\right),
$$

dove $G$ è lo spazio delle variabili globali necessarie. Controlla separatamente
che costruzione e output del riassunto locale stiano nello stesso budget.

Con $b=O(1)$, $L\simeq\sqrt N$ bilancia i due round. Se $b$ cresce, risolvi

$$
\frac NL\simeq bL
\quad\Longrightarrow\quad
L\simeq\sqrt{N/b},\qquad M_L=O(\sqrt{Nb}+G).
$$

La formula è uno strumento di progetto, non una dimostrazione automatica di $M_A$:
se replichi ogni record $k$ volte, lo spazio aggregato può diventare $O(Nk)$.

### 3.5 Come scrivere correttezza e costi

Per ogni round scrivi:

1. chiave e valore emessi dalla Map;
2. cosa contiene esattamente la lista del reducer;
3. output e proprietà vera alla fine del round;
4. dimensione massima della lista e dell’output locale;
5. numero totale di parole prodotte.

La correttezza si chiude spiegando perché la proprietà finale coincide con l’output
richiesto. Per i costi usa il massimo sui round, includendo anche le Map che replicano dati.

## 4. MapReduce esempi svolti e varianti

### 4.1 Media globale e aggregazione gerarchica

Fonte: EX-MR, esercizio 1.

**Due round:** partiziona per $i\bmod L$, calcola una somma per partizione e inviala
con chiave $0$. Il reducer finale somma al massimo $L$ contributi e divide per $N$.

$$
M_L=O(N/L+L),\qquad M_A=O(N).
$$

Per $M_L=O(N^{1/4})$, aggrega gruppi di $N^{1/4}$ valori a ogni livello:

$$
N\longrightarrow N^{3/4}\longrightarrow N^{1/2}
\longrightarrow N^{1/4}\longrightarrow1.
$$

Servono quattro round. Per un budget $M\geq2$, servono
$\lceil\log_MN\rceil$ livelli, con gli opportuni arrotondamenti. Con $M=N^\alpha$
e $\alpha>0$ costante, il numero di round resta costante.

**Trasferimento:** stesso schema per massimo, minimo e altre aggregazioni associative.

### 4.2 Slot machine e clienti compulsivi

Fonti: ExampleWT-1, parte 2 esercizio 1; `sol210622`, varianti A e B.

Input $(i,(s_i,o_i))$. Un esito è frequente se appare almeno $N/50$ volte per quella
macchina. Output: una sola coppia $(s,\mathrm{null})$ per macchina con almeno un esito frequente.

1. **Round 1:** partiziona gli ID in $L=\lceil\sqrt N\rceil$ gruppi. Per ogni coppia
   $(s,o)$ della partizione emetti $((s,o),c_j(s,o))$.
2. **Round 2:** raggruppa per $(s,o)$, somma e, solo se la somma è almeno $N/50$,
   emetti $(s,o)$ con chiave $s$.
3. **Round 3:** per ogni $s$ che riceve almeno un valore, emetti $(s,\mathrm{null})$.

**Correttezza:** i conteggi del secondo round sommano occorrenze su una partizione
dell’input. Il filtro seleziona esattamente le coppie frequenti. L’ultimo round
proietta sulle macchine ed elimina duplicati.

**Spazio:** round 1 riceve $O(\sqrt N)$ record per reducer; round 2 al massimo $L$
conteggi per coppia. In tutto il dataset possono esserci al massimo 50 coppie con
frequenza almeno $N/50$, perché le loro frequenze sommano al massimo a $N$.
Il round 3 riceve quindi al massimo 50 valori per macchina.

$$
M_L=O(\sqrt N),\qquad M_A=O(N).
$$

**Variante:** sostituire macchina con cliente ed esito con prodotto non cambia algoritmo
o prova. Se la soglia diventa $\varphi N$, sopravvivono al massimo $1/\varphi$ coppie:
quel fattore va contato se $\varphi$ non è costante.

### 4.3 Sensori con al massimo K misurazioni

Fonti: EX-MR, esercizio 5; ExampleWT-3, parte 2 esercizio 1.

Conserva gli ID delle occorrenze, anche se due misurazioni hanno lo stesso valore.

1. Partiziona per ID; per ogni sensore conserva fino a $K$ record locali.
2. Raggruppa i candidati per sensore; restituiscine fino a $K$.

Se il sensore compare $f_s$ volte, il risultato deve avere $\min(K,f_s)$ record.
Quando $f_s\leq K$, nessuna partizione ne elimina. Quando $f_s>K$, se una partizione
ne ha almeno $K$ fornisce già abbastanza candidati; altrimenti nessuna occorrenza
viene eliminata localmente e la loro unione ne contiene più di $K$.

Con $L=\sqrt N$:

$$
M_L=O(\sqrt N+K\sqrt N),\qquad M_A=O(N).
$$

Per $K$ costante ottieni $O(\sqrt N)$; per $K=\log_2N$ ottieni
$O(\sqrt N\log N)=o(N)$. Lo spazio aggregato resta lineare perché filtri senza replicare.

**Ottimizzazione facoltativa:** scegliendo $L\simeq\sqrt{N/K}$, se $1\leq K\leq N$,
ottieni $O(\sqrt{NK})$. Per $K=\log N$ è $O(\sqrt{N\log N})$.
Indica chiaramente se stai analizzando lo schema originale o una sua modifica.

### 4.4 Griglia di celle utilizzate

Fonti: ExampleWT-5 e prova del 18/06/2025, parte 2 esercizio 1.

Input: $N$ connessioni $(a,(i,j))$ su griglia $t\times t$, con $t=O(\sqrt N)$.
Output: righe che hanno più di $t/2$ **celle distinte** utilizzate.

1. **Round 1:** partiziona per $a\bmod L$ e deduplica localmente le celle; emetti
   una coppia $((i,j),0)$ per cella locale.
2. **Round 2:** deduplica globalmente per $(i,j)$; emetti $(i,j)$ con chiave $i$.
3. **Round 3:** conta i valori ricevuti per riga: ora sono colonne distinte.
   Emetti $(i,t_i)$ se $t_i>t/2$.

Il primo round limita ogni cella a $L$ candidati. Il terzo riceve al massimo $t$
colonne per riga. Pertanto

$$
M_L=O(\sqrt N+t)=O(\sqrt N),\qquad M_A=O(N).
$$

**Controllo:** un milione di connessioni alla stessa cella deve contribuire esattamente 1.
Non creare le celle inutilizzate: non servono per decidere quali righe superano la soglia.

### 4.5 Numero totale di elementi distinti

Fonte: EX-MR, esercizio 2.

Deduplicare direttamente per valore può raccogliere $N$ copie in un reducer.
Deduplicare e poi mandare tutti i distinti a un unico reducer può raccogliere $N$
valori diversi. Servono due protezioni.

1. Partiziona per ID in $L=\sqrt N$ gruppi; emetti $(j,x)$ per ogni distinto locale.
2. Raggruppa per $x$, scegli **un indice di origine** $j$ tra quelli ricevuti;
   emetti $(j,x)$.
3. Raggruppa per $j$ e conta i distinti assegnati a quella origine; emetti $(0,c_j)$.
4. Somma i conteggi.

Perché il round 3 è piccolo? Una partizione può ricevere solo valori che vi
comparivano originariamente: al massimo $N/L$. Scegliere un’origine arbitraria tra
quelle ricevute mantiene questa proprietà; assegnare tutti i distinti a $j=0$ la distrugge.

Risultato: quattro round, $M_L=O(\sqrt N)$ e $M_A=O(N)$.

### 4.6 Confronti con un insieme globale di punti

Fonti: prova 08/09/2023, parte 2 esercizio 1; EX-CTCL, esercizi 11 e 13;
ExampleWT-4, parte 2 esercizio 1.

**Caso A: per ogni query $q\in Q$, il punto di $P$ più vicino.**

Con $k=|Q|\leq\sqrt N$, partiziona $P$. In ogni partizione trova un minimo per
ciascuna query e invia $(q,p_{j,q})$. Nel secondo round, per ogni $q$, scegli il
minimo tra i $L$ candidati.

La distanza minima globale è il minimo delle distanze minime locali. Per dimensione
costante:

$$
M_L=O(N/L+k+L),\qquad M_A=O(N+kL).
$$

Con $L=\sqrt N$ e $k\leq\sqrt N$, si ottengono i vincoli richiesti. Le copie di $Q$
necessarie ai $L$ reducer sono anch’esse comprese nel termine $kL$.

Se mantieni $L=\sqrt N$ ma fai crescere $k$, lo stesso algoritmo richiede
$M_L=O(\sqrt N+k)$ e $M_A=O(N+k\sqrt N)$: non resta automaticamente lineare.
Come variante, per $\sqrt N<k=o(N)$ scegli $L\simeq N/k$ per recuperare
$M_A=O(N)$ e $M_L=O(k+N/k)=o(N)$.

**Caso B: punto più lontano dal proprio centro.** Conserva un massimo locale
per cluster e fondi con max. Ogni punto contribuisce al solo cluster assegnato.

**Caso C: centro più lontano in media da un cluster.** Per cluster $i$ e centro $c_j$
calcola localmente la somma delle distanze e poi somma i contributi. Per un $i$ fissato,
il divisore $|C_i|$ è uguale per tutti i centri: l’argmax della media coincide con
l’argmax della somma. Con $k$ costante, il riassunto ha dimensione costante.

**Caso D: vicino pesato di un cluster.** Usa invece

$$
A_{i,j}=\sum_{x\in C_i}w_xd(x,c_j)^2,
\qquad j_i=\arg\min_{j\ne i}A_{i,j}.
$$

Escludi $j=i$ se la traccia lo richiede. Con chiavi arbitrarie, come in EX-CTCL 13,
usa partizionamento casuale e dichiara che il limite locale vale con alta probabilità.

### 4.7 Un rappresentante per cluster e colore uniforme

Fonti: EX-CTCL, esercizi 6 e 12; ricordo del 29/06/2023.

**Rappresentante:** assegna ogni punto al centro globale più vicino, conserva un
punto per cluster in ogni partizione, poi uno tra i candidati globali. Il centro
globale potrebbe non appartenere a $P$: non restituirlo se è richiesto $T\subseteq P$.
Non produrre rappresentanti per cluster vuoti.

**Colore:** riassumi un cluster locale con $0$, $1$ o $-1$ se contiene entrambi.
Nel secondo round restituisci il colore solo se tutti i riassunti coincidono con
quel colore; altrimenti $-1$. Se si richiede un output anche per cluster vuoti,
occorre una convenzione esplicita e un modo per crearne le chiavi: non è determinata
dall’input dei soli punti.

### 4.8 Prodotto matrice-vettore

Fonte: EX-MR, esercizio 4.

Per $A\in\mathbb R^{m\times n}$ e $V\in\mathbb R^n$, con $m\leq\sqrt n$:

1. Dividi ogni riga e il vettore in blocchi di lunghezza $\lceil\sqrt n\rceil$.
2. Usa chiave $(i,b)$: invia il blocco $b$ della riga $i$ e una copia del blocco
   corrispondente di $V$. Conserva gli indici delle coordinate per accoppiare i valori.
3. Il reducer calcola un prodotto scalare parziale e lo invia con chiave $i$.
4. Nel secondo round somma i $O(\sqrt n)$ prodotti parziali per riga.

$$
M_L=O(\sqrt n),\qquad M_A=O(mn).
$$

Ogni elemento di $V$ viene replicato $m$ volte: il vincolo su $m$ serve anche alla
Map. Se $m>\sqrt n$, distribuisci la replicazione in livelli con fan-out
$O(\sqrt n)$. Per $m$ polinomiale in $n$, bastano un numero costante di livelli.

### 4.9 Diametro esatto e approssimato in MapReduce

Fonti: EX-CTCL, esercizi 7 e 8.

**Esatto:** genera tutte le coppie di punti tramite replicazione gerarchica. Ogni
record può essere replicato prima $\sqrt N$ volte e poi ancora $\sqrt N$ volte.
Raggruppa con chiave $(\min(i,j),\max(i,j))$ e calcola la distanza; sulla diagonale
la distanza è zero, anche se arriva un solo punto. Aggrega il massimo delle
$O(N^2)$ distanze con fan-in $\sqrt N$ in quattro livelli.

Si ottengono sette round nella costruzione dettagliata della fonte,
$M_L=O(\sqrt N)$ e $M_A=O(N^2)$.

**Approssimato:** scegli $x\in P$ e calcola $\Delta_x=\max_{y\in P}d(x,y)$.
Se è noto solo l’ID di $x$, replica il suo record verso tutte le $L=\sqrt N$
partizioni nel primo round. Ogni reducer calcola un massimo locale; il secondo
round fonde i massimi.

$$
M_L=O(\sqrt N),\qquad M_A=O(N),\qquad
\Delta_x\leq\Delta(P)\leq2\Delta_x.
$$

L’ultima disuguaglianza segue da $d(u,v)\leq d(u,x)+d(x,v)$.

### 4.10 WordCount e dimensione del record

Fonte: EX-MR, esercizio 3.

Per ogni documento, conta localmente le parole; assegna ogni coppia parola-conteggio
a una partizione casuale. Somma per parola dentro ogni partizione; nel secondo
round somma i contributi della stessa parola.

Se $N$ è il numero totale di occorrenze e $N_{\max}$ la lunghezza massima di un documento:

$$
M_L=O(N_{\max}+\sqrt N)\quad\text{con alta probabilità},
\qquad M_A=O(N).
$$

Un documento enorme rimane un problema per la Map iniziale: partizionare le coppie
successive non elimina il costo di leggere il record originale.

## 5. Clustering e coreset costruire le dimostrazioni

### 5.1 Parti dall’obiettivo e dal dominio dei centri

Scrivi prima $d(x,S)=\min_{s\in S}d(x,s)$, poi identifica l’obiettivo:

$$
\Phi_{\mathrm{center}}(P,S)=\max_{x\in P}d(x,S),
$$

$$
\Phi_{\mathrm{median}}(P,S)=\sum_{x\in P}d(x,S),
\qquad
\Phi_{\mathrm{means}}(P,S)=\sum_{x\in P}d(x,S)^2.
$$

Se la convenzione usa la media, cambia il fattore $1/|P|$, non il minimizzatore.
Una soluzione $\alpha$-approssimata per un problema di minimizzazione è ammissibile
e soddisfa $\Phi(P,S)\leq\alpha\Phi^*(P,k)$.

**Il dominio conta:** centri in $P$, nel coreset o liberi nello spazio non sono
vincoli equivalenti. A centri fissati, assegna ogni punto al più vicino, rompendo
i pareggi in modo coerente.

### 5.2 Il percorso attraverso i rappresentanti

Fonti: EX-CTCL, esercizi 6 e 10; ExampleWT-5, parte 1 domanda 2.

Supponi $T\subseteq P$ e, per ogni $x\in P$, esista $t(x)\in T$ con
$d(x,t(x))\leq\rho$. Prendi gli estremi $u,v$ del diametro e scrivi il cammino
$u\to t(u)\to t(v)\to v$:

$$
\Delta(P)=d(u,v)
\leq d(u,t(u))+d(t(u),t(v))+d(t(v),v)
\leq2\rho+\Delta(T).
$$

Poiché $T\subseteq P$:

$$
\boxed{\Delta(T)\leq\Delta(P)\leq\Delta(T)+2\rho.}
$$

Tre casi da riconoscere:

| Ipotesi | Distanza punto-rappresentante | Errore additivo sul diametro |
| --- | --- | --- |
| $d(x,T)\leq R$ | $\rho=R$ | $2R$ |
| Un punto per cluster di raggio $R$ rispetto a un centro esterno | $\rho=2R$ | $4R$ |
| Una rappresentante per cella quadrata di lato $1/c$ | $\rho=\sqrt2/c$ | $2\sqrt2/c$ |

Nel secondo caso, punto e rappresentante sono entrambi a distanza al massimo $R$
dal centro: serve una triangolazione aggiuntiva. Un errore additivo non è un rapporto
di approssimazione costante, salvo un ulteriore legame tra $R$ e $\Delta(P)$.

### 5.3 Farthest-First Traversal in tempo O(Nk)

Fonte: EX-CTCL, esercizio 3.

Mantieni $a_x=d(x,S)$ per ogni punto. Dopo aver scelto un nuovo centro $c$:

$$
a_x\leftarrow\min(a_x,d(x,c)).
$$

Scegli il prossimo centro che **massimizza** $a_x$. Ogni iterazione usa una scansione
di $N$ punti: $O(Nk)$ tempo se una distanza costa $O(1)$, oppure $O(NkD)$ in dimensione $D$.
La memoria addizionale delle distanze è $O(N)$.

### 5.4 FFT è una 2-approssimazione

Fonte: ExampleWT-3, parte 1 domanda 3.

Sia $S=\{c_1,\ldots,c_k\}$ l’output FFT, $q$ il punto peggio coperto e
$r=d(q,S)=\Phi(P,S)$. Le distanze tra tutte le coppie di punti in $S\cup\{q\}$
sono almeno $r$: quando FFT sceglie un centro, il raggio corrente non è minore
del raggio finale.

Distribuisci questi $k+1$ punti nei $k$ cluster ottimi. Due punti $a,b$ devono
appartenere allo stesso cluster, di centro $c^*$ e raggio $r^*$:

$$
r\leq d(a,b)\leq d(a,c^*)+d(c^*,b)\leq2r^*.
$$

**Schema da ricordare:** separazione dei punti scelti + $k+1$ punti in $k$ cluster
+ triangolazione attraverso il centro ottimo.

### 5.5 FFT su un coreset e ottimo di un sottoinsieme

Fonti: EX-CTCL, esercizi 4 e 5.

Se $T\subseteq P$ soddisfa $d(x,T)\leq\varepsilon r^*$ per ogni $x$, FFT su $T$
produce centri $S$ che coprono $T$ entro $2r^*$. La prova precedente funziona usando
i cluster ottimi di **P**, perché anche i punti di $T$ appartengono a quei cluster.
Per ogni $x\in P$:

$$
d(x,S)\leq d(x,t(x))+d(t(x),S)
\leq(\varepsilon+2)r^*.
$$

Quindi $\Phi(P,S)\leq(2+\varepsilon)r^*$.

**Trappola:** nel k-center discreto non è sempre vero che
$\Phi^*(T,k)\leq\Phi^*(P,k)$, perché eliminare punti può eliminare centri ammissibili.
È sempre possibile mostrare

$$
\Phi^*(T,k)\leq2\Phi^*(P,k)
$$

scegliendo un punto di $T$ da ogni cluster ottimo che lo interseca. Per $k=1$,
$P=\{-1,0,1\}$ e $T=\{-1,1\}$ hanno ottimi rispettivamente 1 e 2: fattore stretto.
Per $k>1$, aggiungi $k-1$ punti isolati molto distanti.

Non concatenare inutilmente due fattori 2 per EX-CTCL 4: il confronto diretto con
i cluster di $P$ dà $2+\varepsilon$, mentre la concatenazione dà solo $4+\varepsilon$.

### 5.6 MR-FFT e coreset componibili

Fonti: ExampleWT-4, parte 1 domanda 2; fotografia del 19/07/2023.

1. Suddividi $P$ in $L$ parti; esegui FFT con $k$ centri su ogni parte non troppo piccola.
   Se una parte ha meno di $k$ punti, conservali tutti.
2. Unisci i rappresentanti in $T$, con $|T|\leq kL$; esegui FFT su $T$.

Per partizioni bilanciate:

$$
M_L=O(N/L+kL),\qquad M_A=O(N),
$$

quando i riassunti sono sottoinsiemi delle partizioni. Il bilanciamento
$L\simeq\sqrt{N/k}$ dà $M_L=O(\sqrt{Nk})$, sublineare se $k=o(N)$.

La prima FFT copre ogni partizione entro $2r^*$, la seconda copre $T$ entro $2r^*$,
sempre confrontandosi con i cluster ottimi globali. La triangolazione dà fattore 4
per questa versione standard. Vantaggio: calcolo distribuito su parti piccole;
svantaggio: garanzia peggiore di FFT sequenziale, che ha fattore 2.

Un coreset è **componibile** quando l’unione dei riassunti locali conserva la
proprietà richiesta. Per essere utile deve essere abbastanza piccolo da consentire
il passo finale e abbastanza accurato da trasferire una buona soluzione all’input.

### 5.7 Outlier e k+z+1 punti

Fonte: `sol130722`, esercizio 1.

Da un insieme $X$ di $k+z+1$ punti, al massimo $z$ sono outlier ottimi. Restano
almeno $k+1$ inlier in $k$ cluster: due inlier stanno nello stesso cluster.

$$
d_{\min}(X)\leq d(a,b)\leq2r^*,
\qquad r_{\min}=d_{\min}(X)/2\leq r^*.
$$

Questo dimostra che il guess iniziale non supera l’ottimo. Non dimostra da solo
che un algoritmo successivo abbia una certa approssimazione. Se $d_{\min}=0$,
un procedimento che raddoppia il guess deve gestire esplicitamente il caso zero.

### 5.8 Costruire una soluzione per limitare l’ottimo

Fonte: ExampleWT-2, parte 2 esercizio 1.

Ogni intervallo $[(i-1)/k,i/k]$ contiene almeno un punto. Scegli un punto di $P$
in ciascun intervallo: ogni punto ha un centro a distanza al massimo $1/k$.
Se un estremo condiviso causa scelte coincidenti, conserva i centri distinti e,
quando $|P|\geq k$, aggiungi altri punti fino a $k$; aggiungere centri non aumenta il costo.

$$
\Phi^*(P,k)\leq\Phi(P,S)\leq1/k.
$$

Non devi trovare l’ottimo: basta esibire una soluzione ammissibile con quel costo.
Il limite $1/(2k)$ basato sui punti medi richiede centri liberi, non necessariamente in $P$.

### 5.9 k-means pesato e fairness

Fonti: ExampleWT-1, parte 1 domanda 2; ExampleWT-2, parte 1 domanda 2;
ExampleWT-5, parte 1 domanda 4; [[Homeworks/BDC_HW1]].

In un coreset pesato, un rappresentante $q$ ha peso pari al numero di punti
assegnati a lui, oppure alla somma dei loro pesi se l’input è già pesato.
Nel modello a rappresentanti, ogni punto originale va assegnato esattamente una volta:
per input non pesato, $\sum_{q\in T}w(q)=N$.

Per costruirlo in MapReduce, suddividi $P$ in partizioni e applica a ciascuna un
algoritmo sequenziale di k-means, per esempio k-means++, per scegliere i rappresentanti
locali. Assegna ogni punto al rappresentante locale più vicino e calcolane il peso.
Il coreset globale è l’unione di questi rappresentanti pesati; su di esso il secondo
round esegue l’algoritmo pesato per ottenere i centri finali. Vedi [[5.Coreset2526-2]].

Con centri correnti $S$, k-means++ pesato sceglie $y$ con probabilità

$$
\Pr(y)=\frac{w(y)d(y,S)^2}{\sum_xw(x)d(x,S)^2}.
$$

Il primo centro è estratto proporzionalmente ai pesi. Se il denominatore è zero,
tutti i punti di peso positivo sono già coperti a costo zero: gestisci il caso
senza dividere per zero.

**Fair k-means dei vecchi esami:** minimizza

$$
\max\left\{
\frac1{|A|}\sum_{x\in A}d(x,C)^2,
\frac1{|B|}\sum_{x\in B}d(x,C)^2
\right\}.
$$

Per $n-1$ punti A in 0 e un punto B in 1, con centro libero $c$:

- k-means standard: $(n-1)c^2+(1-c)^2$, minimo in $c=1/n$, che tende a 0;
- fair k-means: $\max\{c^2,(1-c)^2\}$, minimo in $c=1/2$.

**Fair k-center dell’HW1 2025/26:** minimizza $\max_xd(x,S)$ con $S\subseteq U$,
esattamente $k_A$ centri A e $k_B$ centri B. È un vincolo sui centri selezionati,
non una media dei costi per gruppo. Per $k=1$, una quota A forza un centro A e una
quota B forza un centro B. Non trasferire la risposta $1/2$ al problema discreto con quote.

La trascrizione del 18/06/2025 usa il nome “fair k-centers”, ma ExampleWT-5 presenta
formalmente il problema fair k-means: all’esame parti sempre dall’obiettivo scritto.

### 5.10 Dimostrare che una distanza è una metrica

Fonte: EX-CTCL, esercizio 1.

Verifica non negatività, identità degli indiscernibili, simmetria e disuguaglianza
triangolare. Per $L_1$, i primi tre seguono dalle proprietà del valore assoluto;
per l’ultimo usa coordinata per coordinata

$$
|x_i-z_i|\leq|x_i-y_i|+|y_i-z_i|
$$

e somma su $i$. $L_1$ è Manhattan; la distanza euclidea è $L_2$.
La distanza euclidea **al quadrato** non è una metrica: su $0,1,2$,
$4>1+1$ viola la disuguaglianza triangolare.

## 6. Streaming scegliere e adattare lo stimatore

### 6.1 La scelta fondamentale

| Quantità richiesta | Struttura | Operazione finale |
| --- | --- | --- |
| Campione di occorrenze | Reservoir Sampling | Restituisci le posizioni campionate |
| Maggioranza, se esiste | Boyer-Moore | Candidato, con verifica se necessaria |
| Tutti gli item frequenti con fascia grigia | Sticky Sampling | Filtra i contatori sottostimanti |
| Frequenza con errore solo in eccesso, conteggi non negativi | Count-Min | Minimo delle righe |
| Frequenza pesata anche con incrementi negativi | Count Sketch | Stima con segni; mediana o media secondo la richiesta |
| Somma di quadrati delle frequenze | Count Sketch / contatore AMS | Somma dei quadrati per riga |
| Numero di distinti | Probabilistic Counting | $2^R$ |
| Appartenenza approssimata | Bloom filter | AND dei bit interrogati |

Per ogni algoritmo specifica **stato, inizializzazione, update, query, memoria,
tempo e garanzia**. Una sola formula finale non descrive un algoritmo streaming.

### 6.2 Count Sketch universale per pesi e resi

Fonti: ExampleWT-2 e ExampleWT-4, parte 2 esercizio 2; EX-STR, esercizio 9.

Riscrivi ogni evento come $(u,a)$, dove $a$ è il contributo alla quantità cercata:

- vendita: $a=+1$; reso: $a=-1$, quindi $a=2\gamma-1$;
- item rosso: $a=1/2$; item blu: $a=1/3$;
- misura di sensore $(u,w)$: $a=w$.

La frequenza generalizzata è $f_u=\sum_{t:u_t=u}a_t$.
Usa $d$ righe di $w$ contatori inizializzati a zero, con hash

$$
h_j:U\to\{0,\ldots,w-1\},\qquad g_j:U\to\{-1,+1\}.
$$

Assumi segni uniformi almeno pairwise independent tra item, indipendenti dagli
hash dei bucket; per amplificare, scegli righe indipendenti.

```text
Update(u, a):
  per ogni riga j:
    C[j, h_j(u)] += a * g_j(u)

QueryRiga(u, j):
  restituisci g_j(u) * C[j, h_j(u)]
```

Per una riga:

$$
\widehat f_{u,j}
=f_u+\sum_{v\ne u}f_vg_j(u)g_j(v)
\mathbf1_{\{h_j(v)=h_j(u)\}}.
$$

Ogni termine di rumore ha attesa zero; quindi $\mathbb E[\widehat f_{u,j}]=f_u$.
La **media** delle righe resta certamente unbiased. La mediana è la scelta usuale
per amplificare accuratezza: la sola unbiasedness delle righe non basta a provare
quella della mediana. Con rumore congiuntamente simmetrico e una convenzione di
mediana simmetrica si può giustificare anche questo caso, ma va dimostrato.

**Scelta sicura quando la traccia chiede esplicitamente una stima unbiased:** usa una
riga oppure la media delle righe, indicando questa scelta.

**Caso speciale:** se nessun altro item collide con $u$, la somma di rumore è vuota
e la stima è esatta. Se lo stream contiene solo un prodotto $p$, tutte le righe
restituiscono esattamente il saldo vendite-resi, anche se è zero o negativo.

Memoria $O(dw)$ parole; update $O(d)$; query puntuale $O(d)$ per media o per selezione
lineare della mediana. Non creare una chiave distinta per colore se vuoi stimare
una sola frequenza pesata dello stesso item.

### 6.3 Secondo momento pesato

Fonti: EX-STR, esercizi 8 e 9; ExampleWT-1, parte 2 esercizio 2.

Obiettivo:

$$
H_2=\sum_uf_u^2,\qquad f_u=\sum_{t:u_t=u}a_t.
$$

Con gli aggiornamenti precedenti, considera una riga e definisci

$$
Z_j=\sum_{b=0}^{w-1}C[j,b]^2.
$$

Espandi separando termini diagonali e coppie non ordinate $u<v$:

$$
Z_j=\sum_uf_u^2+
2\sum_{u<v}f_uf_vg_j(u)g_j(v)
\mathbf1_{\{h_j(u)=h_j(v)\}}.
$$

I termini misti hanno attesa zero, quindi $\mathbb E[Z_j]=H_2$. Vale anche con
pesi negativi: la prova è algebrica e non richiede di trasformare un peso in copie
di un elemento.

**Risposta completa unbiased:** restituisci $\overline Z=d^{-1}\sum_jZ_j$.
Memoria $O(dw)$, update $O(d)$, query $O(dw)$.
Se basta uno stimatore semplice, una sola cella con segno casuale produce
$Z=(\sum_ug(u)f_u)^2$, ancora unbiased; precisione e varianza richiedono analisi aggiuntiva.

**Attenzione:** la mediana dei $Z_j$ non è in generale unbiased. È un’operazione
di amplificazione della concentrazione, non una trasformazione che preserva l’attesa.
Per bounds sulla varianza servono ipotesi di indipendenza più forti dei soli segni pairwise.

### 6.4 Count-Min e collisione con un item dominante

Fonte: EX-STR, esercizio 10.

Count-Min aggiorna senza segni e restituisce il minimo dei contatori interrogati.
Per frequenze finali non negative, ogni riga è almeno $f_u$. Con frequenze che
possono diventare negative questa proprietà non è disponibile.

Nell’esercizio $f_a=f_b=n/2-5$ e gli altri item hanno massa totale 10. Con due
bucket, se $a$ e $b$ non collidono:

$$
f_a\leq\widehat f_{a,j}\leq f_a+10,
\qquad
\frac{\widehat f_{a,j}-f_a}{f_a}
\leq\frac{10}{n/2-5}=R.
$$

L’evento favorevole ha probabilità $1/2$. Con righe indipendenti, il minimo è buono
se almeno una riga è buona:

$$
\Pr\left(\frac{\widehat f_a-f_a}{f_a}\leq R\right)\geq1-2^{-d}.
$$

È un **limite inferiore**, non automaticamente un’uguaglianza: potrebbero esserci
altre configurazioni favorevoli. Per la garanzia additiva generale, con $w\geq e/\varepsilon$
e $d\geq\ln(1/\delta)$ si ottiene errore al massimo $\varepsilon n$ con probabilità
almeno $1-\delta$, nel modello standard di stream di inserimenti.

### 6.5 Bloom filter unione e dimezzamento

Fonti: ExampleWT-3, parte 2 esercizio 2; `sol210622`, esercizio 2;
EX-STR, esercizio 11.

Usiamo $B$ bit, $m$ elementi distinti e $k$ hash per evitare conflitti di notazione.
Inizializza tutti i bit a zero; per inserire $x$, imposta a 1 i bit $A[h_j(x)]$.
La query risponde “possibilmente presente” se tutti i $k$ bit sono 1.

**Assenza di falsi negativi:** l’inserimento di $x$ imposta tutti i bit che la sua
query controllerà; nessun inserimento successivo li azzera.

**Unione:** con stessi hash e stessa lunghezza, poni

$$
A[i]=A_1[i]\operatorname{OR}A_2[i].
$$

È il filtro di $S_1\cup S_2$. Con hash ideali indipendenti, per $m=|S_1\cup S_2|$:

$$
\Pr(A[i]=0)=\left(1-\frac1B\right)^{km}
\simeq e^{-km/B}.
$$

Non usare $|S_1|+|S_2|$ se i due insiemi si sovrappongono: lo stesso elemento,
con gli stessi hash, scrive gli stessi bit. La probabilità di falso positivo è
approssimativamente $(1-e^{-km/B})^k$, assumendo l’approssimazione d’indipendenza dei bit.

**Dimezzamento:** per $B$ pari, poni

$$
A'[i]=A[i]\operatorname{OR}A[i+B/2],
\qquad h'_j(x)=h_j(x)\bmod(B/2).
$$

La query deve usare $A'[h'_j(x)]$, non il solo valore dell’hash. Il nuovo filtro
si costruisce in $O(B)$ tempo senza conoscere gli elementi originali e soddisfa

$$
\Pr(A'[i]=0)=\left(1-\frac2B\right)^{km}\simeq e^{-2km/B}.
$$

La compressione conserva l’assenza di falsi negativi, ma aumenta l’occupazione
dei bit e quindi tende a peggiorare i falsi positivi.

### 6.6 Boyer-Moore e numeri mancanti

Fonti: EX-STR, esercizi 1, 2 e 6.

**Boyer-Moore:** mantieni candidato e contatore. Se il contatore è zero, il nuovo
item diventa candidato con contatore 1; se coincide incrementa; altrimenti decrementa.

Invariante: il prefisso si decompone in `count` copie **non cancellate** del candidato
e coppie di elementi diversi. Non significa che `count` sia la frequenza vera.
Verifica l’invariante separando i tre casi dell’update. Una maggioranza stretta
non può essere cancellata completamente, quindi, se esiste, coincide con il candidato.
Senza promessa di esistenza, serve un secondo conteggio per certificarla.

Con Sticky Sampling a soglia $\varphi=1/2$, restituire il candidato solo se è nel
set filtrato recupera una maggioranza esistente con probabilità almeno $1-\delta$.
In sua assenza può restituire un item con frequenza almeno $(1/2-\varepsilon)n$:
non certifica una maggioranza esatta.

**Un numero mancante:** per $n$ interi distinti da $1$ a $n+1$, mantieni la somma $S$:

$$
x_{\mathrm{mancante}}=\frac{(n+1)(n+2)}2-S.
$$

Una passata, $O(1)$ parole, update e query $O(1)$. Se $n$ è ignoto, conta anche
gli elementi. Per due mancanti $a,b$, nell’universo noto $1,\ldots,n+2$, mantieni
somma e somma dei quadrati. Dalle differenze con i totali teorici ricavi

$$
s=a+b,\qquad q=a^2+b^2,\qquad ab=(s^2-q)/2.
$$

$a,b$ sono le radici di $z^2-sz+(s^2-q)/2=0$. “Spazio costante” significa
costante numero di parole di dimensione sufficiente, non costante numero di bit.

## 7. Probabilità quattro dimostrazioni riutilizzabili

### 7.1 Indicatori e Reservoir Sampling

Fonti: EX-STR, esercizi 3, 4 e 5; ExampleWT-1, parte 1 domanda 3.

Reservoir conserva un campione uniforme di $m$ **posizioni**: dopo le prime $m$,
all’istante $t$ accetta il nuovo elemento con probabilità $m/t$ e sostituisce una
posizione uniforme del reservoir. Ogni posizione del prefisso appartiene al
campione con probabilità $m/t$.

Per un item con $f_a$ occorrenze, usa un indicatore $I_i$ per ogni sua occorrenza:

$$
X_a=\sum_{i=1}^{f_a}I_i,
\qquad \mathbb E[X_a]=f_a\frac mn.
$$

Se $f_a\geq\varphi n$ e $m\geq1/\varphi$, allora $\mathbb E[X_a]\geq1$.
Questo **non** garantisce presenza nel campione. Per un reservoir uniforme:

$$
\Pr(X_a=0)=\frac{\binom{n-f_a}{m}}{\binom nm}
\leq(1-f_a/n)^m\leq e^{-\varphi m}.
$$

Se ci sono $R$ occorrenze rosse e $X$ è il numero di rosse campionate:

$$
\widehat R=\frac nmX,
\qquad \mathbb E[\widehat R]=R.
$$

La linearità dell’attesa non richiede indipendenza tra gli indicatori.

**Probabilità condizionata:** se $t>m$ e sai che $x_t$ è entrato nel reservoir,
un vecchio elemento $x_i$, $i<t$, deve essere stato presente e non essere stato espulso:

$$
\Pr(x_i\in S_t\mid x_t\in S_t)
=\frac{m}{t-1}\left(1-\frac1m\right)
=\frac{m-1}{t-1}.
$$

**Unione di due campioni:** per due stream di uguale lunghezza $n$, campionare
uniformemente $m$ posizioni dall’unione dei due campioni di taglia $m$ dà a ciascuna
posizione probabilità $(m/n)(1/2)=m/(2n)$. È sufficiente per la definizione di
“m-sample” usata in EX-STR 4, basata sulle sole probabilità marginali.
Non produce in generale un campione uniforme fra tutti i sottoinsiemi di taglia $m$
dei $2n$ elementi. Per ottenere quest’ultima proprietà, estrai il numero $K$ di
elementi dal primo stream secondo la distribuzione ipergeometrica con popolazione
$2n$, $n$ elementi del primo stream e $m$ estrazioni; poi scegli $K$ elementi
uniformi da $S_1$ e $m-K$ da $S_2$.

### 7.2 Sticky Sampling memoria e garanzie

Fonti: ExampleWT-2, parte 1 domanda 3; ExampleWT-5, parte 1 domanda 3.

Per lunghezza nota $n$, parametri $0<\varepsilon<\varphi<1$ e $0<\delta<1$:

$$
r=\frac{\ln(1/(\delta\varphi))}{\varepsilon},
\qquad p=\min(1,r/n).
$$

Se l’item è già nel dizionario, incrementa il contatore. Altrimenti inseriscilo
con probabilità $p$, partendo da 1. Filtra alla fine con soglia $(\varphi-\varepsilon)n$.

Per la memoria, sia $I_t$ l’indicatore di creazione di una nuova voce:

$$
\mathbb E[|S|]=\sum_{t=1}^n\Pr(I_t=1)
\leq np\leq r.
$$

Quindi memoria $O(r)$ **in attesa**. Non affermare un limite deterministico $O(r)$
sulla sola base di questa prova.

Garanzie del set filtrato $F$:

- Con probabilità almeno $1-\delta$, tutti gli item con $f_u\geq\varphi n$ sono in $F$.
- Nessun item con $f_u<(\varphi-\varepsilon)n$ viene restituito: i contatori
  sottostimano sempre la frequenza.
- Nella fascia grigia, tra le due soglie, presenza e assenza sono entrambe ammesse.

Prova della prima proprietà: un item frequente viene perso solo se non è campionato
abbastanza presto. Non campionare nessuna delle sue prime $\lceil\varepsilon n\rceil$
occorrenze ha probabilità al massimo $e^{-\varepsilon r}=\delta\varphi$, nel caso
$r<n$; se $r\geq n$ si conta esattamente. Ci sono al massimo $1/\varphi$ item
frequenti, quindi l’union bound limita a $\delta$ la probabilità di perderne almeno uno.

### 7.3 Ripetere e prendere la soluzione migliore

Fonte: EX-CTCL, esercizio 9.

Se una singola esecuzione di k-means++ produce una soluzione sufficientemente buona
con probabilità almeno $1/2$, esegui $t$ istanze indipendenti e scegli quella con
il costo più basso, valutato sullo stesso dataset e con lo stesso obiettivo.

L’output è cattivo solo se tutte le esecuzioni sono cattive:

$$
\Pr(\text{fallimento})\leq2^{-t}.
$$

Per fallimento al massimo $1/N$, basta $t=\lceil\log_2N\rceil$.
Non fare la media dei centri. Il minimo funziona perché puoi valutare e confrontare
direttamente la qualità delle soluzioni ammissibili.

### 7.4 Mediana e Chernoff

Fonti: EX-STR, esercizio 7; prova 08/09/2023, parte 2 esercizio 2.

Per stimatori che possono sbagliare da entrambi i lati, usa la mediana. Definisci
$I_j=1$ quando la riga $j$ è cattiva e $X=\sum_jI_j$. Con righe indipendenti e
probabilità di errore $1/12$:

$$
\mu=\mathbb E[X]=d/12.
$$

Nella traccia $d=2\log_2N$, trascurando gli arrotondamenti. Allora $d/2=6\mu$.
Applicando la forma fornita nella traccia,
$\Pr(X\geq a\mu)\leq2^{-a\mu}$ per $a\geq6$:

$$
\Pr(X\geq d/2)\leq2^{-d/2}=1/N.
$$

Se $X<d/2$, più di metà delle stime appartiene a
$[(1-\varepsilon)f_u,(1+\varepsilon)f_u]$, quindi anche la mediana vi appartiene.
Per $d$ pari vale anche usando la media dei due valori centrali. L’evento di
mediana cattiva è dunque contenuto nell’evento appena limitato.

Per Probabilistic Counting, applica lo stesso metodo separatamente a stime sotto
$F_0/16$ e sopra $16F_0$, con probabilità per lato al massimo $1/16$.
Con $\ell=\Theta(\log|U|)$ righe ottieni errore al massimo $1/|U|$ per lato;
per entrambi i lati insieme l’union bound dà $2/|U|$. Se vuoi $1/|U|$ complessivo,
porta ciascun lato a $1/(2|U|)$ aumentando la costante nelle ripetizioni.

**Regola di scelta:** media per preservare l’attesa; minimo per errori solo in
eccesso; mediana per concentrazione con errori da entrambi i lati.

## 8. Similarity search dai bucket alle garanzie

Fonti: [[Slides/Exercises/EX-SIMSEARCH2526.pdf]] e domande di teoria `ExampleWT`.

### 8.1 Definizioni senza ambiguità

- **Range Reporting:** restituisce tutti i punti nella regione di query; se sono
  $z$, il costo di produrli include $\Omega(z)$.
- **r-Near Neighbor Search:** dato $q$, restituisce un punto a distanza al massimo
  $r$, se esiste, altrimenti null.
- **(c,r)-Approximate Near Neighbor Search:** con $c>1$, se esiste un punto entro
  $r$, deve restituire un punto entro $cr$ con la probabilità di successo prevista.
  Se non esistono punti entro $cr$, restituisce null; nella zona intermedia può
  restituire null oppure un punto ammissibile.

Qui NNS significa **Near Neighbor Search**. Se una traccia usa invece “Nearest”,
chiede il punto di distanza minima: verifica sempre la definizione.

### 8.2 Una tabella LSH

Una famiglia $(p_1,p_2,c,r)$-sensibile soddisfa, per ogni coppia fissata $x,y$:

$$
d(x,y)\leq r\Longrightarrow\Pr_h(h(x)=h(y))\geq p_1,
$$

$$
d(x,y)>cr\Longrightarrow\Pr_h(h(x)=h(y))\leq p_2,
\qquad p_1>p_2.
$$

Usa la convenzione stretta/non stretta agli estremi adottata nella traccia.
Estrai $h$, memorizza ogni punto nel bucket $T[h(x)]$, e per una query scandisci
$T[h(q)]$ fino al primo punto con distanza al massimo $cr$.

Se esiste un vicino $x$ entro $r$, la sua collisione basta a garantire il successo:
probabilità almeno $p_1$. Verifica comunque la distanza reale dei candidati:
una collisione non certifica vicinanza.

I punti rifiutati sono oltre $cr$. Il loro numero atteso nel bucket è al massimo
$np_2$; può servire anche un ultimo confronto con il punto accettato. Con distanza
di costo $O(D)$:

$$
\mathbb E[T_q]=O(D(1+np_2)),
$$

oltre all’eventuale costo di calcolo dell’hash. La forma abbreviata $O(Dnp_2)$
usata nelle fonti presuppone che il termine costante sia assorbibile.

### 8.3 Bit-sampling per vicino e lontano

Per vettori booleani, scegli una coordinata uniforme $i$ e poni $h_i(x)=x_i$.
Se la distanza di Hamming è $s$, ci sono $D-s$ coordinate uguali e $s$ diverse:

$$
\Pr(h(p)=h(q))=1-\frac{s}{D},
\qquad
\Pr(h(p)\ne h(q))=\frac{s}{D}.
$$

**Vicino:** cerca nello stesso bucket. Se la soglia è $r$ e l’accettazione è entro
$cr$, ottieni $p_1=1-r/D$ e $p_2=1-cr/D$, per parametri nel dominio ammesso.

**Lontano:** cerca nel bucket $T[1-h(q)]$ e restituisci il primo candidato con
$d_H(p,q)\geq r$. Se esiste un punto $x$ sufficientemente lontano, il suo ingresso
in quel bucket ha probabilità almeno $r/D$; quindi il successo è almeno $r/D$.
Il risultato restituito è sempre valido grazie al controllo della distanza;
null può derivare da una scelta sfortunata della coordinata.

Controlli veloci: per $p=q$ la collisione nello stesso bucket vale 1; per vettori
complementari vale 0. La query nel bucket opposto può ancora costare $O(Dn)$:
la garanzia di successo da sola non dimostra un tempo sublineare.

### 8.4 Scegliere parametri per una query O(n)

Fonte: EX-SIMSEARCH, esercizio 2.

Rappresenta i documenti con vettori di presenza/assenza delle $D$ parole rilevanti,
adottando la distanza di Hamming richiesta dalla soluzione dell’esercizio.

Vuoi $p_1\geq1/2$ e $Dnp_2=O(n)$. Quindi imponi

$$
r=D/2,\qquad cr=D-a,
\qquad c=2(1-a/D),
$$

con $a>1$ costante e $D>2a$ per avere $c>1$. Allora
$p_1=1/2$ e $p_2=a/D$.

Con il termine completo, il tempo è $O(D+n)$, che diventa $O(n)$ se $D=O(n)$
o se il costo additivo della singola verifica viene assorbito dalla convenzione
dell’esercizio. Non nascondere un costo $D$ quando la dimensione può dominare $n$.

### 8.5 kd-tree e query rettangolari

Fonti: EX-SIMSEARCH, esercizio 1; domande del 19/07/2023 e appunto fotografico 2026.

Un kd-tree bilanciato alterna le coordinate di split e divide i punti tramite
mediane. Se $v$ divide verticalmente in $x=s$, le regioni dei figli sono la regione
di $v$ intersecata rispettivamente con i semipiani $x\leq s$ e $x\geq s$,
con una convenzione coerente per i punti sul confine. Per split orizzontali usa $y$.

Per una regione di query $Q$:

1. Regione del nodo disgiunta da $Q$: pota il sottoalbero.
2. Regione contenuta in $Q$: riporta tutti i punti del sottoalbero.
3. Intersezione parziale: visita i figli pertinenti.

In due dimensioni, spazio $O(n)$ e query rettangolare $O(\sqrt n+z)$, dove $z$
è il numero di punti riportati; costruzione standard $O(n\log n)$.

Se basta **un solo punto**, conserva in ogni nodo un rappresentante del sottoalbero.
Quando il rappresentante cade nella query, restituiscilo subito. Non devi
enumerare un sottoalbero interamente contenuto: il suo rappresentante basta.
Il costo è $O(\sqrt n)$.

Nella figura di EX-SIMSEARCH, pagina 2, con visita del figlio sinistro prima del
destro, vengono visitati $\ell_1,\ell_2,\ell_4$ e la foglia $p_3$; tornando alla
radice si visita $\ell_3$, il cui rappresentante $p_7$ è nella query, e si termina.
I nodi successivi non sono necessari. Durante un esercizio grafico annota
per ogni nodo regione, rappresentante e motivo della visita o della potatura.

### 8.6 Amplificare LSH con AND e OR

Tema ricordato nell’audio del 09/07/2026; per il metodo vedi
[[9SimSearch2526-2#Concatenation AND Construction]].

**OR:** costruisci $L_h$ tabelle con hash indipendenti e cerca nei bucket di tutte
le tabelle. Un vicino collide in almeno una con probabilità almeno

$$
1-(1-p_1)^{L_h}.
$$

Il successo cresce, ma crescono anche memoria e candidati da controllare.

**AND:** per una tabella, concatena $K_h$ hash indipendenti in una sola chiave
$g(x)=(h_1(x),\ldots,h_{K_h}(x))$. Un vicino collide con probabilità almeno
$p_1^{K_h}$, un punto lontano con probabilità al massimo $p_2^{K_h}$.
Diminuiscono entrambe: la concatenazione da sola non aumenta il successo.

**Combinazione:** con $0<p_2<p_1<1$, scegli

$$
K_h=\left\lceil\log_{1/p_2}n\right\rceil,
\qquad
L_h=\left\lceil\frac{\ln(1/\delta)}{p_1^{K_h}}\right\rceil.
$$

Ogni tabella ha al massimo 1 candidato lontano in attesa e la probabilità di
non trovare un vicino fissato è al massimo
$(1-p_1^{K_h})^{L_h}\leq e^{-L_hp_1^{K_h}}\leq\delta$.
Per parametri LSH costanti, ponendo
$\rho=\ln(1/p_1)/\ln(1/p_2)<1$, servono
$O(n^\rho\ln(1/\delta))$ tabelle. Con hash elementari di costo $O(D)$, il costo
atteso di query è $O(DK_hL_h)$, includendo hash e verifiche. La memoria comprende
i dati e le repliche dei riferimenti nelle tabelle: almeno $O(Dn+nL_h)$,
oltre alla rappresentazione delle chiavi concatenate e degli hash.

## 9. Domande brevi teoria Spark e homework

### 9.1 Risposta in tre parti

Per domande da pochi punti scrivi: **definizione precisa, meccanismo, conseguenza**.
Se è richiesta una prova, aggiungi il passaggio decisivo; evita una pagina di contesto.

### 9.2 RAM, dischi e capacità del cluster

Fonti: ExampleWT-1 e ExampleWT-4, parte 1 domanda 1.

La RAM disponibile per un task deve sostenere $M_L$; lo storage distribuito deve
sostenere $M_A$. Nell’esempio con 10 macchine, 8 GB RAM e 128 GB disco ciascuna,
con dati tra le fasi su HDFS, il limite ideale è

$$
M_L\leq8\ \mathrm{GB},\qquad M_A\leq1280\ \mathrm{GB}.
$$

Questo usa il modello semplificato della traccia, senza overhead e con una sola
copia logica dei dati. La somma delle RAM non sostituisce la RAM locale; in un
cluster reale replicazione HDFS e task concorrenti riducono le capacità utilizzabili.

### 9.3 RDD, lazy evaluation e misure di tempo

Fonti: ExampleWT-2 e ExampleWT-5; prova 08/09/2023, parte 1.

Un RDD è una collezione distribuita e partizionata; le trasformazioni registrano
un piano di calcolo, eseguito quando un’azione richiede il risultato. Cronometrare
solo le trasformazioni misura principalmente la costruzione del piano.

Per misurare il calcolo, includi un’azione. Se vuoi escludere lettura e preprocessing,
materializza prima l’input persistito tramite un’azione; poi cronometra l’algoritmo
e l’azione che lo esegue. Dichiarare `cache` o `persist` non materializza subito i dati.

`mapPartitions` riceve un iteratore degli elementi di una partizione e restituisce
un iteratore di output: consente riassunti locali, non un raggruppamento globale
per chiave. Un round MR su RDD combina trasformazione dei record, shuffle per
chiave e aggregazione. Un RDD da solo non equivale a un round.

### 9.4 Spark Streaming e metriche

Fonti: ExampleWT-4, parte 1 domanda 4; fotografia del 19/07/2023.

Nel modello DStream degli esercizi, uno stream viene diviso in micro-batch,
rappresentati da RDD. Una callback per batch scorre gli elementi e aggiorna uno
stato persistente tra batch. Non reinizializzare lo sketch a ogni callback se
la richiesta riguarda l’intero stream.

Le metriche degli algoritmi streaming sono numero di passate, memoria di lavoro,
tempo di update, tempo di query e accuratezza/probabilità d’errore. Se un’implementazione
raccoglie un intero batch sul driver, quella memoria va distinta dalla memoria
teorica del solo sketch.

### 9.5 Probabilistic Counting

Fonte: ExampleWT-3, parte 1 domanda 4; prova 08/09/2023, parte 1 domanda 3.

Scegli una hash uniforme con le ipotesi d’indipendenza del corso; mantieni il massimo
$R$ del numero di zeri finali di $h(x)$ sugli item letti. Stima $F_0$ con $2^R$.
Le ripetizioni dello stesso item producono lo stesso hash e non aumentano di per sé
la stima. Gestisci stream vuoto separatamente restituendo 0 e usa una convenzione
finita per gli zeri finali dell’hash zero.

Lo stato comprende anche la descrizione della hash: il bound del corso è
$O(\log|U|)$ bit. Il solo contatore $R$ richiede meno bit, ma non è tutto lo stato.
Per maggiore probabilità di successo usa istanze indipendenti e mediana.

### 9.6 Homework vecchi e attuali

Le prove includono richiami a homework di anni differenti. Per rispondere identifica
la formulazione richiesta; non attribuire un vecchio progetto all’anno attuale.

- **HW1 attuale:** Fair-FFT seleziona il punto ammissibile più lontano; esaurita la
  quota di un gruppo, non seleziona altri centri di quel gruppo. MR-Fair-FFT costruisce
  rappresentanti sulle partizioni e seleziona i centri finali sulla loro unione.
  La garanzia 2 di FFT standard non si trasferisce automaticamente alla variante con quote.
- **Vecchio k-center con outlier:** ogni partizione può emettere fino a $k+z$
  rappresentanti pesati nella versione del corso; il secondo round lavora su
  $O(L(k+z))$ punti e risolve il problema pesato. Aumentare $L$ riduce le partizioni
  ma ingrandisce il coreset finale. Usa la dimensione prevista dalla variante richiesta.
- **Vecchio silhouette:** per $x$ in un cluster non singleton, $a(x)$ è la distanza
  media dagli altri punti del suo cluster; $b(x)$ è il minimo delle distanze medie
  verso un altro cluster. Si definisce
  $s(x)=(b(x)-a(x))/\max\{a(x),b(x)\}$, con convenzioni per singleton e denominatore zero.
  La silhouette media è $|P|^{-1}\sum_xs(x)$: alta indica coesione interna e separazione.
- **Frequent items:** confronta i contatori sottostimanti di Sticky Sampling con
  le stime sovrastimanti di Count-Min. Un dizionario di frequenze esatte usato per
  valutare sperimentalmente gli errori non fa parte del risparmio di memoria degli sketch.

Per ripassare i progetti locali: [[PROJECT_DESCRIPTIONS_EXAM]] e [[Homeworks/BDC_HW1]].

### 9.7 Itemset frequenti fair nelle prove storiche

Fonte: `sol130722`, esercizio 2. Argomento presente nell’archivio; la sua presenza
nel programma corrente non è stabilita dal solo vecchio esame.

Obiettivo: dimostrare $F_{2k+2}\subseteq C_{2k+2}$. Parti da un elemento arbitrario
$Z\in F_{2k+2}$, con $k+1$ item di ciascuno dei due gruppi. Scegli due item distinti
$a_1,a_2$ del primo gruppo e due $b_1,b_2$ del secondo, e poni

$$
X=Z\setminus\{a_1,b_1\},\qquad
Y=Z\setminus\{a_2,b_2\}.
$$

Entrambi hanno $k$ item per gruppo e sono frequenti per antimonotonia del supporto:
un sottoinsieme compare in tutte le transazioni che contengono $Z$.
Condividono esattamente $k-1$ item per gruppo, quindi sono compatibili, e $X\cup Y=Z$.
Questo certifica che $Z$ è generato tra i candidati. Non dimostra che ogni candidato
sia frequente: la verifica del supporto resta necessaria.

## 10. Errori nelle fonti e trappole da evitare

Le soluzioni ufficiali sono utili per capire lo schema atteso, ma alcune contengono
refusi o passaggi che richiedono ipotesi aggiuntive. Qui sono esplicitamente corretti.

| Fonte o situazione | Punto da correggere o precisare |
| --- | --- |
| EX-CTCL 1 | $L_1$ è Manhattan, non euclidea |
| EX-CTCL 3 | FFT seleziona il **massimo** della distanza dal centro più vicino |
| EX-CTCL 6 | I bound sul diametro sono non stretti: $\Delta(T)\leq\Delta(P)\leq\Delta(T)+4R$ |
| EX-MR 5 | Per selezionare record, conserva le occorrenze; deduplicare temperature può eliminare misurazioni valide |
| EX-STR 9 | Un peso negativo non rappresenta un numero di copie; usa la prova algebrica |
| EX-STR 9 | L’unbiasedness delle righe non dimostra quella della mediana dei secondi momenti; usa la media |
| EX-STR 10 | La probabilità finale garantita è almeno $1-2^{-d}$; il testo finale della soluzione riporta un’uguaglianza incoerente |
| EX-STR 11 | La query controlla $A'[h'_j(x)]=1$, non $h'_j(x)=1$ |
| EX-STR 4 | Probabilità marginali uniformi non equivalgono a uniformità su tutti i sottoinsiemi |
| LSH, una tabella | Considera anche un possibile confronto finale: $O(D(1+np_2))$ |
| Trascrizione 18/06/2025 | Fair k-means e fair k-center con quote hanno obiettivi diversi |

Un controesempio alla mediana unbiased dei secondi momenti: tre item di frequenza
1 in un’unica cella, con segni indipendenti. Allora $Z=(g_1+g_2+g_3)^2$
vale 1 con probabilità $3/4$ e 9 con probabilità $1/4$,
con attesa 3. La mediana di tre repliche vale 9 con probabilità
$3(1/4)^2(3/4)+(1/4)^3=5/32$, quindi la sua attesa è
$1+8(5/32)=9/4\ne3$. Per questo la guida usa la media quando richiede unbiasedness.

## 11. Mappa completa degli esercizi letti

### 11.1 Raccolte tematiche

| Fonte | Esercizi | Dove trovare il metodo |
| --- | --- | --- |
| [[Slides/Exercises/EX-MR2526.pdf]] | 1: media e trade-off round/spazio | §4.1 |
| EX-MR | 2: distinti | §4.5 |
| EX-MR | 3: WordCount | §4.10 |
| EX-MR | 4: matrice-vettore | §4.8 |
| EX-MR | 5: K misurazioni per sensore | §4.3 |
| [[Slides/Exercises/EX-CTCL2526.pdf]] | 1: metrica; 2: assegnamento ai centri | §5.10; §5.1 e §3.1 |
| EX-CTCL | 3: implementazione FFT; 4: coreset fine; 5: ottimo di sottoinsieme | §5.3; §5.5 |
| EX-CTCL | 6: rappresentanti e diametro | §4.7 e §5.2 |
| EX-CTCL | 7: diametro esatto; 8: diametro approssimato | §4.9 |
| EX-CTCL | 9: amplificazione k-means++; 10: griglia geometrica | §7.3; §5.2 |
| EX-CTCL | 11: più lontano del cluster; 12: colore; 13: vicino pesato | §4.6; §4.7; §4.6 |
| [[Slides/Exercises/EX-STR2526.pdf]] | 1: Boyer-Moore; 2: mancanti | §6.6 |
| EX-STR | 3: frequenti nel campione; 4: unione campioni; 5: stima dei rossi | §7.1 |
| EX-STR | 6: Boyer-Moore e Sticky; 7: mediana | §6.6; §7.4 |
| EX-STR | 8: secondo momento; 9: misure pesate | §6.3 |
| EX-STR | 10: Count-Min con due dominanti; 11: Bloom dimezzato | §6.4; §6.5 |
| [[Slides/Exercises/EX-SIMSEARCH2526.pdf]] | 1: un punto nel rettangolo; 2: documenti; 3: punto lontano | §8.5; §8.4; §8.3 |

Per EX-CTCL 2 l’assegnamento è una sola Map: ogni $(ID_x,x)$ produce
$(ID_x,(x,\arg\min_{c\in S}d(x,c)))$. Con $k$ centri globali e dimensione costante,
$M_L=O(k)$; le copie dei centri contribuiscono allo spazio aggregato. Se ci sono
$W$ copie, il costo è $O(N+Wk)$, lineare quando $Wk=O(N)$.

### 11.2 Prove complete e soluzioni

| Fonte | Parte 1 | Parte 2 |
| --- | --- | --- |
| [[Slides/Exercises/Exams/ExampleWT-1.pdf]] | RAM/HDFS §9.2; coreset pesato §5.9; reservoir condizionato §7.1; ANNS §8.1 | Slot machine §4.2; secondo momento pesato §6.3 |
| [[Slides/Exercises/Exams/ExampleWT-2.pdf]] | mapPartitions §9.3; k-means++ pesato §5.9; memoria Sticky §7.2; RR/kd-tree §8.1 e §8.5 | Intervalli §5.8; vendite-resi §6.2 |
| [[Slides/Exercises/Exams/ExampleWT-3.pdf]] | Obiettivi MR §3.1; outlier/MR §9.6; FFT 2-approx §5.4; distinti stream §9.5 | Sensori §4.3; Bloom unione §6.5 |
| [[Slides/Exercises/Exams/ExampleWT-4.pdf]] | Capacità cluster §9.2; MR-FFT §5.6; tempo LSH §8.2; streaming §9.4 | Centro più lontano in media §4.6; frequenze colorate §6.2 |
| [[Slides/Exercises/Exams/ExampleWT-5.pdf]] | Lazy evaluation §9.3; diametro §5.2; Sticky §7.2; fair k-means §5.9 | Griglia §4.4; bucket opposto §8.3 |
| [[Slides/Exercises/Exams/sol210622.pdf]] | Non inclusa nel PDF | Slot machine/clienti §4.2; Bloom unione §6.5 |
| [[Slides/Exercises/Exams/sol130722.pdf]] | Non inclusa nel PDF | Outlier e guess iniziale §5.7; itemset fair §9.7 |
| [[Slides/Exercises/Exams/18-06-25.pdf]] | Disponibile separatamente come ricordo testuale | Griglia §4.4; bucket opposto §8.3 |
| [[Slides/Exercises/Exams/Questions/Part 1.jpg\|08/09/2023 parte 1]] | Spark §9.3; obiettivi clustering §5.1; F0 §9.5; LSH §8.2 | Vedi riga successiva |
| [[Slides/Exercises/Exams/08-09-2023/Part 2.jpg\|08/09/2023 parte 2]] | Vedi riga precedente | Minimo per query globale §4.6; mediana e Chernoff §7.4 |

Le varianti A/B del 21/06/2022 sono lo stesso schema con nomi diversi. ExampleWT-5
e la parte 2 del 18/06/2025 ripropongono gli stessi due problemi: non contarli come
evidenze indipendenti della frequenza futura di quelle tipologie.

### 11.3 Ricordi testuali e fotografie

- [[Slides/Exercises/Exams/Questions/29-06-2023/Questions.txt]]: MR con colori,
  silhouette, memoria Sticky, ANNS (§9.6, §7.2, §8.1); rappresentanti e diametro
  (§4.7, §5.2); vendite-resi (§6.2). La ricostruzione degli esercizi è incompleta:
  usa il testo formale corrispondente delle raccolte per fissare le ipotesi.
- [[Slides/Exercises/Exams/Questions/19-07-2023/Questions.jpg]]: partizioni casuali
  (§3.2), Spark Streaming (§9.4), coreset componibili (§5.6), RR/kd-tree (§8.1, §8.5).
- [[Slides/Exercises/Exams/Questions/18-06-2025.txt]]: lazy evaluation (§9.3),
  diametro (§5.2), Sticky (§7.2), fairness (§5.9, con la distinzione segnalata).
- [[Slides/Exercises/Exams/Questions/14-07-2025.txt]]: partizioni (§3.2), MR-FFT
  (§5.6), Bloom senza falsi negativi (§6.5), kd-tree (§8.5).
- [[Slides/Exercises/Audio/WhatsApp Image 2026-07-17 at 17.54.55.jpeg]]: $M_L/M_A$
  (§3.1), k-means pesato e coreset (§5.9), Bloom (§6.5), regioni dei figli kd-tree (§8.5).
- [[Slides/Exercises/Audio/WhatsApp Ptt 2026-07-09 at 10.26.54.ogg]]:
  dalla trascrizione automatica emergono `foreachRDD` nell’homework (§9.4),
  m-sample e Reservoir Sampling (§7.1), amplificazione LSH (§8.6).
- [[Slides/Exercises/Audio/WhatsApp Ptt 2026-07-17 at 17.58.42.ogg]]:
  dalla trascrizione automatica emerge la formulazione del problema Fair-FFT
  dell’homework (§5.9 e §9.6). Le considerazioni personali sulla difficoltà e sulla
  valutazione non sono trattate come regole ufficiali dell’esame.

I riferimenti servono a tornare alle tracce originali: questa guida è una
rielaborazione didattica, non una trascrizione delle soluzioni.

## 12. Allenamento e checklist da esame

### 12.1 Ordine di studio suggerito dal materiale

1. **MapReduce:** svolgi griglia, sensori e query globali; ripeti ogni analisi
   sostituendo $\sqrt N$ con $L$ prima di fissarlo.
2. **Sketch:** svolgi vendite-resi, colori pesati e secondo momento; scrivi
   l’espansione “segnale + rumore” senza consultare la guida.
3. **Geometria:** dimostra diametro con rappresentanti, FFT e caso con outlier.
   Disegna il cammino usato dalla triangolare.
4. **Probabilità:** ricostruisci reservoir condizionato, memoria Sticky e mediana
   dell’08/09/2023; specifica sempre l’evento di fallimento.
5. **Similarity:** risolvi bucket opposto, parametri per documenti e visita kd-tree.
6. **Simulazione:** scegli un ExampleWT completo e rispondi anche alle domande brevi.

Nel file locale [[Slides/Exercises/Exams/exam rules.txt]] sono indicati 150 minuti,
28 punti per lo scritto, almeno 16 nello scritto e almeno 18 con homework/progetto.
Gli esempi vecchi riportano 120 minuti e 26 punti. È una differenza documentata
nell’archivio, non una verifica di eventuali comunicazioni successive.

Per allenarti su 150 minuti: 10 minuti di lettura, circa 45 per la parte teorica,
40 per il primo esercizio, 40 per il secondo e 15 di controllo. Adatta i tempi
ai punti effettivi e passa oltre se un passaggio blocca il resto della prova.

### 12.2 Tre varianti per verificare il trasferimento

**Variante A:** nell’esercizio griglia, restituisci le righe con almeno $q$ celle usate.
Quali parti cambiano? Solo il filtro finale, purché $q>0$ e la richiesta riguardi
righe osservate; per $q=0$, anche righe mai apparse vanno considerate e generate.

**Variante B:** ogni evento è $(u,\gamma,v)$, con valore $v\geq0$, vendita o reso.
Quale update stima il saldo monetario? $a=(2\gamma-1)v$ nel Count Sketch; la prova
unbiased è identica. Se lo stesso item non ha collisioni, il saldo è esatto.

**Variante C:** ogni punto dista al massimo $R$ dal suo centro, ma il rappresentante
scelto dista dal centro al massimo $R/2$. Quale bound sul diametro?
$d(x,t(x))\leq3R/2$, quindi $\Delta(P)\leq\Delta(T)+3R$.

### 12.3 Checklist finale

- Ho definito input e output, distinguendo record, valori e occorrenze?
- Ho indicato ogni chiave MapReduce e cosa contiene la lista del reducer?
- Ho controllato anche l’ultimo reducer e le Map che replicano dati?
- Ho contato dimensione dei valori, variabili globali e loro copie?
- Il limite sullo spazio è deterministico, in attesa o con alta probabilità?
- Ho usato una proprietà che dimostra la correttezza dei riassunti?
- Lo stimatore richiesto è unbiased, concentrato o solo esatto in un caso speciale?
- Ho dichiarato le ipotesi d’indipendenza e contato gli eventi dell’union bound?
- Il coreset contiene centri ammissibili? Sto usando $2R$ oppure $4R$ con la giusta ipotesi?
- Ho incluso costo della distanza e numero di punti riportati, quando pertinenti?
- Le disuguaglianze rispettano soglie strette/non strette della traccia?
- La risposta finale contiene algoritmo, prova e costi richiesti, senza risultati non dimostrati?
