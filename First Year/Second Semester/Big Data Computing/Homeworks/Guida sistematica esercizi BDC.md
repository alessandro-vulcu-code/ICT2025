# Guida sistematica agli esercizi di Big Data Computing

Questa guida ricava un metodo di soluzione dagli esercizi ufficiali in `Slides/Exercises/`
e dalle prove in `Slides/Exercises/Exams/`. Non sostituisce teoria: serve per riconoscere
struttura nascosta di esercizio nuovo e costruire risposta breve, completa e verificabile.

Per allenamento puntuale usare anche [[BDC_Exam_Exercises]], che cataloga tracce per
argomento.

## 1. Cosa mostrano gli esami

Prove considerate:

- cinque `ExampleWT`;
- prove/soluzioni del 21/06/2022, 13/07/2022, 08/09/2023 e 18/06/2025;
- domande ricordate del 2023, 2025 e 2026;
- raccolte `EX-MR`, `EX-CTCL`, `EX-STR` ed `EX-SIMSEARCH`.

Struttura ricorrente:

1. domande teoriche brevi, dove contano definizioni e quantificatori esatti;
2. un esercizio MapReduce o clustering/MR;
3. un esercizio streaming o similarity search;
4. una domanda collegata agli homework;
5. almeno una variante nuova ottenuta combinando tecniche già viste.

Conclusione: non conviene memorizzare pseudocodice isolato. Conviene memorizzare pochi
invarianti e mattoni componibili.

## 2. Procedura universale

Prima di calcolare, scrivere queste cinque righe.

1. **Input:** rappresentazione precisa e dimensione dominante.
2. **Output:** coppie, valore o garanzia richiesta.
3. **Ostacolo:** skew, duplicati, troppe collisioni, output grande, spazio locale lineare.
4. **Mattone:** partizione-compressione, indicatori, amplificazione, triangolazione o pruning.
5. **Obiettivi:** esattezza/probabilità, tempo, passate/round, $M_L$, $M_A$.

Poi risolvere in ordine:

1. progettare informazione minima che deve sopravvivere;
2. dimostrare che riassunti locali possono essere fusi;
3. costruire algoritmo;
4. dimostrare correttezza con invariante;
5. analizzare risorse fase per fase;
6. controllare casi estremi.

### 2.1 Albero decisionale rapido

- Dataset distribuito e richiesta $M_L=o(N)$: usare **partiziona, comprimi, raggruppa**.
- Somma, massimo, minimo o conteggio: usare **aggregazione gerarchica**.
- Duplicati/skew senza limite sulla frequenza: spezzare prima per ID, deduplicare dopo.
- Scelta di al massimo $K$ elementi per gruppo: tagliare a $K$ in ogni partizione, poi ancora a $K$.
- Valore atteso/unbiasedness: introdurre **variabili indicatrici**.
- Probabilità costante da portare a $1-1/N$: ripetizioni indipendenti + min/mediana.
- Distanze e clustering: cercare **triangle inequality + pigeonhole principle**.
- LSH: calcolare prima probabilità di collisione, poi scegliere bucket e parametri.
- kd-tree: classificare regioni in disgiunte, contenute, parzialmente intersecanti.
- Bloom filter: ragionare su singolo bit e su operazioni OR.

## 3. MapReduce: schema principale

### 3.1 Obiettivi e modello

Buon algoritmo:

- $R=O(1)$ round, salvo trade-off esplicito;
- $M_L=o(N)$, spesso $O(\sqrt N)$;
- $M_A=O(N)$, salvo problemi con output intrinsecamente quadratico;
- correttezza anche con chiavi/frequenze fortemente sbilanciate.

$M_L$ è massimo spazio usato da una singola applicazione map/reduce. $M_A$ è massimo,
su tutti i round, dello spazio totale di input, output e coppie intermedie. Dimensione del
payload conta: una coppia contenente vettore di $k$ numeri costa $\Theta(k)$, non $O(1)$.

### 3.2 Partizione-compressione-raggruppamento

Per $L$ partizioni:

**Round 1**

- Map: $(i,x)\mapsto(i\bmod L,x)$ se ID distinti e ben distribuiti;
- alternativa: $(i,x)\mapsto(h(i),x)$ o chiave casuale in $[0,L)$;
- Reduce: calcolare riassunto locale per ogni entità logica.

**Round 2**

- usare entità logica come chiave;
- fondere riassunti locali.

Con $L=\sqrt N$, ogni partizione deterministica da ID consecutivi ha dimensione
$O(\sqrt N)$. Con partizione casuale, dimensione $O(\sqrt N)$ vale con alta probabilità,
non deterministicamente.

### 3.3 Condizione decisiva: riassunto mergeable

Serve operatore $\oplus$ tale che

$$
S(A\cup B)=S(A)\oplus S(B).
$$

Esempi:

- somma: somma delle somme;
- massimo/minimo: massimo/minimo dei valori locali;
- conteggio: somma dei conteggi;
- top-$K$ arbitrario per gruppo: top-$K$ dell'unione dei top-$K$ locali;
- presenza colori: stato in $\{0,1,-1\}$, dove $-1$ significa misto;
- punto più lontano da centro: massimo locale delle distanze;
- vettore di statistiche: somma componente per componente.

Non mergeable senza informazione aggiuntiva:

- media delle medie, se partizioni hanno cardinalità diverse;
- insieme esatto di distinti sostituito solo dal numero di distinti locali;
- mediana delle mediane come mediana esatta generale.

### 3.4 Come gestire skew e duplicati

Errore classico: usare subito valore frequente come chiave. Se valore compare $N$ volte,
un reducer riceve $\Theta(N)$ elementi.

Schema corretto:

1. distribuire record tramite ID/casualità;
2. comprimere/deduplicare dentro ogni blocco;
3. usare valore semantico come chiave;
4. fondere al massimo un riassunto per blocco.

Perciò una chiave logica riceve al massimo $L$ riassunti, anche se aveva frequenza $N$.
Questo schema risolve distinct count, celle occupate, coppie frequenti e molti esercizi per
cluster.

### 3.5 Quattro template da memorizzare

#### Template A: aggregato associativo globale

Obiettivo: somma, media, massimo, minimo.

1. dividere in blocchi da $M$;
2. aggregare ciascun blocco;
3. ripetere finché restano al massimo $M$ riassunti;
4. aggregare risultato finale.

Risorse:

$$
M_L=O(M),\qquad M_A=O(N),\qquad R=\Theta(\log_M N).
$$

Per media trasportare `(somma, conteggio)`, oppure somma globale e $N$ noto.

#### Template B: selezione limitata per gruppo

Obiettivo: conservare $\min\{K,f_s\}$ record per gruppo $s$.

1. ogni partizione conserva al massimo $K$ record per $s$;
2. reducer di $s$ riceve al massimo $KL$ record;
3. conserva di nuovo al massimo $K$ record.

Con $L=\sqrt N$:

$$
M_L=O(K\sqrt N),\qquad M_A=O(N).
$$

Per $K=O(1)$ si ottiene $O(\sqrt N)$; per $K=\log N$, $O(\sqrt N\log N)$.

#### Template C: frequenza sopra soglia globale

Obiettivo: trovare coppie $(a,b)$ con frequenza almeno $N/c$.

1. contare $(a,b)$ localmente;
2. sommare conteggi per $(a,b)$ e filtrare soglia;
3. raggruppare per $a$ e produrre un solo output.

Fatto utile: per ogni $a$ esistono al massimo $c$ valori $b$ frequenti, perché frequenze
totali non superano $N$. Quindi terzo reducer riceve $O(c)$ elementi.

#### Template D: tutti i confronti con piccolo insieme globale

Se ogni punto deve essere confrontato con $k$ centri globali:

- costo locale map: $O(k)$;
- ogni blocco emette spesso $O(k)$ riassunti;
- secondo round riceve al massimo $L$ riassunti per centro;
- spazio aggregato deve includere copie/broadcast e numero totale di riassunti.

Se $k$ è costante o $k\le\sqrt N$, scelta $L=\sqrt N$ spesso basta. Se $k$ cresce, bilanciare
termini come $N/L$, $kL$ e $k$ invece di impostare automaticamente $L=\sqrt N$.

### 3.6 Analisi $M_L$ senza errori

Creare tabella mentale per ogni fase:

| Fase | Input massimo per chiamata | Output massimo | Stato ausiliario |
|---|---:|---:|---:|
| Map $r$ | ? | ? | ? |
| Reduce $r$ | ? | ? | ? |

Poi:

$$
M_L=\max_{r,\text{fase}}\{\text{input} + \text{output} + \text{stato}\}.
$$

Per $M_A$, contare volume totale di ogni rappresentazione in ogni round e prendere massimo.
Non sommare automaticamente volumi di round diversi.

Controlli obbligatori:

- mapper che replica record $r$ volte aggiunge $rN$ volume;
- broadcast di $k$ elementi su $W$ worker può costare $kW$ se modello lo conta;
- reducer finale non deve ricevere $N$ elementi;
- numero di chiavi non basta: contare dimensione valori;
- output quadratico rende impossibile $M_A=O(N)$.

### 3.7 Dimostrazione di correttezza MR

Usare tre frasi:

1. **Copertura:** ogni record originale contribuisce a esattamente un riassunto locale
   rilevante, oppure a tutte copie esplicitamente richieste.
2. **Sufficienza:** compressione locale non elimina informazione necessaria.
3. **Fusione:** reducer finale combina tutti e soli riassunti relativi alla stessa entità.

## 4. Clustering e coreset

### 4.1 Motore delle dimostrazioni

Quasi tutte prove usano:

1. assegnare punti a centri ottimi;
2. applicare pigeonhole principle a $k+1$ punti e $k$ cluster;
3. trovare due punti nello stesso cluster ottimo;
4. triangolare attraverso centro ottimo.

Se $p,q$ stanno nello stesso cluster di raggio $\Phi^*$:

$$
d(p,q)\le d(p,c^*)+d(c^*,q)\le 2\Phi^*.
$$

Questa singola disuguaglianza alimenta prova $2$-approssimata di FFT, proprietà di
subset/coreset e inizializzazione di $k$-center con outlier.

### 4.2 Script FFT

Siano $c_1,\ldots,c_k$ centri scelti e $q$ punto più lontano da essi. Considerare
$k+1$ punti $c_1,\ldots,c_k,q$. Due appartengono allo stesso cluster ottimo; loro distanza
è al massimo $2\Phi^*$. Proprietà greedy di FFT implica che raggio finale non supera
quella distanza. Quindi:

$$
\Phi_{k\text{-center}}(P,S)\le2\Phi^*.
$$

Non confondere:

- $k$-center: massimo delle distanze;
- $k$-median: somma delle distanze;
- $k$-means: somma delle distanze al quadrato.

### 4.3 Script coreset + soluzione approssimata

Se ogni $x\in P$ ha proxy $t(x)\in T$ con $d(x,t(x))\le\varepsilon\Phi^*$ e algoritmo su
$T$ garantisce $d(t,S)\le\alpha\Phi^*$, allora:

$$
d(x,S)\le d(x,t(x))+d(t(x),S)\le(\varepsilon+\alpha)\Phi^*.
$$

Per FFT su $T$, tipicamente $\alpha=2$ e rapporto finale $2+\varepsilon$.

### 4.4 Diametro: distinguere tre risultati

1. Da punto arbitrario $x$:

   $$
   \frac{\Delta(P)}2\le\max_{y\in P}d(x,y)\le\Delta(P).
   $$

2. Se $d(x,T)\le R$ per ogni $x\in P$ e proxy appartengono agli stessi cluster indotti da
   centri esterni, spesso:

   $$
   \Delta(T)\le\Delta(P)\le\Delta(T)+4R.
   $$

3. Una rappresentante per cella quadrata di lato $1/c$ in $\mathbb R^2$:

   $$
   \Delta(T)\le\Delta(P)\le\Delta(T)+\frac{2\sqrt2}{c}.
   $$

Errore additivo non implica rapporto moltiplicativo utile se $\Delta(P)$ può essere molto
piccolo.

### 4.5 Amplificare algoritmo randomizzato

Se singola esecuzione è buona con probabilità almeno $1/2$, eseguire $t$ copie indipendenti
e scegliere soluzione con costo minimo. Fallimento simultaneo:

$$
\Pr[\text{tutte cattive}]\le2^{-t}.
$$

Con $t=\lceil\log_2N\rceil$, successo almeno $1-1/N$.

## 5. Streaming: metodo probabilistico

### 5.1 Variabili indicatrici

Per contare eventi casuali, definire

$$
X_i=\begin{cases}1&\text{se evento }i\text{ avviene},\\0&\text{altrimenti.}\end{cases}
$$

Poi:

$$
X=\sum_iX_i,\qquad \mathbb E[X]=\sum_i\Pr(X_i=1).
$$

Indipendenza non serve per linearità dell'aspettativa. Serve invece per moltiplicare
probabilità di fallimenti o applicare certi Chernoff bound.

Applicazioni immediate:

- numero di occorrenze rosse nel reservoir;
- numero di copie di item frequente nel campione;
- termini di collisione in Count Sketch;
- numero di righe cattive.

### 5.2 Reservoir Sampling

Invariante dopo $t$ elementi:

$$
\Pr[x_i\in S_t]=\frac mt\quad\text{per ogni }i\le t.
$$

Per dimostrare proprietà di campione composto, scomporre:

$$
\Pr[x\in S]=\Pr[x\in S_1]\Pr[x\in S\mid x\in S_1].
$$

Per stimatore del numero $R$ di elementi rossi, se $X_S$ è numero di rossi nel reservoir:

$$
\widehat R=\frac nmX_S,qquad \mathbb E[\widehat R]=R.
$$

Dire “almeno una occorrenza in aspettativa” significa $\mathbb E[X]\ge1$, non garantisce
$X\ge1$ in ogni campione né con alta probabilità.

### 5.3 Count-Min contro Count Sketch

**Count-Min:** aggiornamenti non negativi, collisioni aggiungono rumore positivo, query con
minimo tra righe. Stima mai sotto frequenza vera nel modello insertion-only.

**Count Sketch:** usa hash $h_j$ per cella e segno $g_j\in\{-1,+1\}$. Aggiornamento pesato:

$$
C[j,h_j(u)]\mathrel{+}=g_j(u)w.
$$

Stima per riga:

$$
\widetilde f_{u,j}=g_j(u)C[j,h_j(u)],
$$

poi mediana tra righe. Rumore di collisione ha aspettativa zero grazie a segni indipendenti,
quindi singola riga è unbiased. Mediana migliora probabilità d'errore, ma mediana di
stimatori unbiased non è automaticamente unbiased.

Per frequenza pesata, codificare peso direttamente:

- acquisto: $+1$, reso: $-1$;
- rosso: $1/2$, blu: $1/3$;
- sensore: valore misura $w_i$, anche negativo se algebra/hash restano validi.

Se nessun altro item collide con $u$ in una riga, stima è esatta perché moltiplicazione
$g_j(u)^2=1$ annulla segno.

### 5.4 Secondo momento

Per

$$
F_2=\sum_uf_u^2,
$$

una riga Count Sketch produce

$$
\widetilde F_{2,j}=\sum_{k=1}^wC[j,k]^2.
$$

Espandendo quadrati:

- termini diagonali sommano esattamente a $F_2$;
- termini incrociati hanno aspettativa zero.

Quindi $\mathbb E[\widetilde F_{2,j}]=F_2$. Non attribuire automaticamente stessa
unbiasedness alla mediana delle righe.

### 5.5 Median trick e Chernoff

Se riga fallisce con probabilità $p<1/2$, definire $X_j=1$ se riga $j$ è cattiva e
$X=\sum_jX_j$. Mediana è cattiva solo se almeno metà righe sono cattive:

$$
\Pr[\text{mediana cattiva}]\le\Pr[X\ge d/2].
$$

Poi applicare Chernoff usando $\mu=dp$. Passaggi da mostrare:

1. soglia $d/2$ scritta come $(1+\delta)\mu$;
2. bound scelto e ipotesi su $\delta$;
3. sostituzione di $d=\Theta(\log N)$;
4. conclusione $N^{-\Theta(1)}$.

### 5.6 Bloom filter

Probabilità che bit fissato rimanga zero dopo inserimento di $m$ elementi con $k$ hash:

$$
\Pr[A[i]=0]=\left(1-\frac1n\right)^{km}\approx e^{-km/n}.
$$

Unione di filtri costruiti con stessi hash:

$$
A=A_1\operatorname{OR}A_2.
$$

Nessun falso negativo per $S_1\cup S_2$. Nella probabilità usare
$m=|S_1\cup S_2|$, non $|S_1|+|S_2|$ se insiemi si sovrappongono.

Compressione da $n$ a $n/2$ bit:

$$
B[i]=A[i]\operatorname{OR}A[i+n/2],\qquad h'_j(x)=h_j(x)\bmod(n/2),
$$

e $\Pr[B[i]=0]\approx e^{-2km/n}$.

## 6. Similarity search

### 6.1 Prima scrivere definizione con quantificatori

Per $(c,r)$-ANNS:

- se esiste $p^*\in P$ con $d(p^*,q)\le r$,
- restituire con probabilità dichiarata un $p\in P$ con $d(p,q)\le cr$;
- se punto vicino non esiste, comportamento dipende da definizione adottata.

Non confondere:

- NNS: un punto vicino;
- Range Reporting: tutti punti nella regione/raggio;
- ANNS: punto entro distanza rilassata $cr$ sotto promessa di punto entro $r$.

### 6.2 LSH: procedura algebrica

1. scegliere rappresentazione e distanza;
2. calcolare esattamente $\Pr[h(p)=h(q)]$;
3. sostituire condizioni $d(p,q)\le r$ e $d(p,q)\ge cr$;
4. leggere $p_1$ e $p_2$;
5. scegliere parametri per successo e tempo richiesti;
6. descrivere bucket scandito e verifica esatta dei candidati.

Per bit sampling su vettori booleani di dimensione $D$:

$$
\Pr[h(p)=h(q)]=1-\frac{d_H(p,q)}D,
$$

$$
\Pr[h(p)=\operatorname{not}(h(q))]=\frac{d_H(p,q)}D.
$$

Seconda formula trasforma ricerca “vicino” in ricerca “lontano”: scandire bucket
$T[\operatorname{not}(h(q))]$ e verificare $d_H(p,q)\ge r$. Se esiste punto $r$-far,
successo almeno $r/D$ con una tabella.

### 6.3 Tempo atteso con una tabella

Costo tipico:

$$
O(D)+O(D\cdot\text{numero candidati})=O(Dnp_2)
$$

a meno di termine $O(D)$ esplicito. Per ottenere $O(n)$ da $O(Dn)$, scegliere parametri
con $p_2=O(1/D)$ mantenendo $p_1$ costante.

### 6.4 kd-tree

Per query rettangolare, nodo/region può essere:

- disgiunto: potare;
- completamente contenuto: riportare tutto subtree;
- parzialmente intersecante: visitare figli pertinenti.

Range reporting in $\mathbb R^2$ bilanciato:

$$
O(\sqrt n+s),
$$

dove $s$ è output. Se serve un solo punto e ogni nodo conserva rappresentante del proprio
subtree, appena regione nodo è contenuta o rappresentante cade nella query si può fermare;
termine $s$ scompare e costo diventa $O(\sqrt n)$.

## 7. Come affrontare variante mai vista

### 7.1 Tradurre nomi in primitive

Ignorare storia applicativa:

- “slot machine biased” = esiste coppia sopra soglia;
- “customer compulsive” = stesso esercizio con nomi diversi;
- “celle usate per riga” = distinct per coppia, poi count per prima componente;
- “furthest center” = vettore di somme per cluster, poi argmax;
- “weighted closest neighbor” = vettore di somme pesate, poi argmin;
- “colori uniformi” = monoid a tre stati;
- “net sales” = frequency sketch con aggiornamenti firmati.

### 7.2 Comporre mattoni

Esempio generico: “per ogni gruppo $a$, restituire se più di $T$ distinti valori $b$ sono
comparsi, con duplicati arbitrari”.

1. partizionare per ID;
2. deduplicare $(a,b)$ localmente;
3. deduplicare globalmente usando chiave $(a,b)$;
4. raggruppare per $a$;
5. contare $b$ distinti e filtrare soglia.

Questa composizione produce esercizio griglia 2025.

### 7.3 Verifica avversaria

Provare soluzione contro:

- tutti record con stessa chiave logica;
- tutti record distinti;
- un gruppo contiene quasi tutto dataset;
- $K$, $k$, $t$ al massimo consentito;
- partizioni molto sbilanciate;
- insieme vuoto o gruppo vuoto, se ammesso;
- collisioni massime;
- punti coincidenti e tie;
- pesi negativi;
- output grande.

Se uno di questi produce reducer da $\Theta(N)$, soluzione non raggiunge $M_L=o(N)$.

## 8. Struttura risposta da esame

### 8.1 Algoritmo MapReduce

Usare sempre forma:

```text
Input: ...
Output: ...

Round 1
Map: ...
Reduce: ...
Invariant after Round 1: ...

Round 2
Map: ...
Reduce: ...
Invariant after Round 2: ...

Correctness: ...
Local space: ...
Aggregate space: ...
```

### 8.2 Prova probabilistica

```text
Define indicator/random variables.
Compute expectation or bad-event probability for one copy.
State independence exactly where used.
Relate final failure to count/intersection of bad copies.
Apply bound.
Substitute parameters and conclude.
```

### 8.3 Prova geometrica

```text
Fix optimal solution and induced clusters.
Select witness points.
Use pigeonhole principle if k+1 points occur.
Apply triangle inequality with named intermediate points.
Relate resulting distance to algorithm objective.
State approximation/additive guarantee.
```

## 9. Errori frequenti osservati

- Scrivere solo idea senza coppie chiave-valore.
- Non dichiarare cosa è globale.
- Usare chiave frequente nel primo round e ignorare skew.
- Confondere numero di coppie con loro dimensione.
- Analizzare solo reduce, ignorando output del mapper.
- Dire $M_A$ lineare dopo replica non lineare.
- Mediare medie locali senza cardinalità.
- Confondere aspettativa con alta probabilità.
- Usare indipendenza per linearità dell'aspettativa, dove non serve.
- Dichiarare mediana unbiased senza prova.
- Dimenticare verifica della distanza dopo collisione LSH.
- Dare garanzia ANNS senza premessa “se esiste punto entro $r$”.
- Confondere errore additivo e rapporto moltiplicativo.
- Non gestire tie o punti coincidenti.
- Dare risposta teorica lunga ma senza definizione formale.

## 10. Checklist finale da 60 secondi

- [ ] Input/output espliciti.
- [ ] Ogni round ha Map e Reduce, anche se uno è vuoto.
- [ ] Invariante dopo ogni round.
- [ ] Nessun reducer può ricevere $\Theta(N)$ nel caso peggiore.
- [ ] Repliche e payload inclusi in $M_L$/$M_A$.
- [ ] Correttezza separata da analisi spazio.
- [ ] Probabilità: evento, indipendenza, bound e parametri espliciti.
- [ ] Geometria: punti intermedi e triangle inequality espliciti.
- [ ] LSH: collisione, bucket, verifica, garanzia.
- [ ] Risposta termina con risultato richiesto, non con sola derivazione.

## 11. Piano di allenamento

1. Risolvere un esercizio per ciascun template senza guardare soluzione.
2. Riscrivere soluzione in massimo 15 righe per domanda teorica e 35-45 righe per esercizio.
3. Cambiare nomi e soglie: sensori $\leftrightarrow$ clienti, max $\leftrightarrow$ min,
   frequenza $\leftrightarrow$ distinct.
4. Inventare caso avversario e rifare $M_L$, $M_A$.
5. Confrontare con [[BDC_Exam_Exercises]] e soluzioni originali.
6. Simulare prova completa rispettando tempo ufficiale corrente: 2.5 ore, 28 punti.

## 12. Correzioni concettuali da tenere presenti

Materiale contiene alcuni refusi o passaggi da leggere con cautela:

- $L_1$ non è distanza “Euclidean”; distanza euclidea è $L_2$.
- In query Bloom si controlla `B[h'_j(x)] == 1`, non `h'_j(x) == 1`.
- Mediana di stime unbiased non è in generale unbiased; unbiasedness è immediata per
  singola riga Count Sketch/$F_2$.
- Bound da partizionamento casuale è con alta probabilità; con `ID mod L` e ID consecutivi
  è deterministico.
- In unione Bloom, probabilità dipende da $|S_1\cup S_2|$; usare somma cardinalità solo
  se insiemi sono disgiunti o si accetta bound conservativo.
- Esercizi vecchi su fair $k$-means e homework vecchi non definiscono necessariamente
  stessa fairness degli homework correnti.
