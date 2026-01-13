# Report di Crittografia: Il Problema del Logaritmo Discreto e Algoritmi di Risoluzione

## 1. Concetti Chiave e Definizioni

Per comprendere la robustezza dei moderni sistemi crittografici, è strategico padroneggiare i concetti fondamentali su cui si basano. Il Problema del Logaritmo Discreto (DLP) e la nozione di complessità computazionale rappresentano due pilastri essenziali. La loro comprensione non è solo un esercizio accademico, ma una necessità per valutare la sicurezza reale di protocolli come lo scambio di chiavi Diffie-Hellman e altri sistemi a chiave pubblica. Questa sezione introduce le definizioni formali che costituiscono le fondamenta di questo campo.

Problema del Logaritmo Discreto (DLP) Il Problema del Logaritmo Discreto consiste nel trovare un intero $x$ che soddisfi la congruenza:

$$g^x \equiv h \pmod{p}$$

Dove $p$ è un numero primo, e $g$ e $h$ sono elementi del campo finito $\mathbb{F}_p^*$. Il valore $x$ è definito come il logaritmo discreto di $h$ in base $g$. A differenza dei logaritmi reali, la soluzione può non esistere o non essere unica; l'insieme di tutte le soluzioni è chiamato logaritmo discreto di $h$. L'esistenza di una soluzione dipende dal fatto che $h$ appartenga al sottogruppo ciclico generato da $g$. La difficoltà computazionale del DLP risiede nella totale assenza di monotonicità: se si prova un valore $x$ e il risultato è lontano da $h$, non c'è alcuna indicazione su come scegliere il tentativo successivo (se aumentare o diminuire $x$), rendendo la ricerca della soluzione un compito arduo per valori di $p$ molto grandi.

**Radice Primitiva** Un elemento $g \in \mathbb{F}_p^*$ è detto radice primitiva (o generatore) se il suo ordine è massimo, ovvero $p-1$. In altre parole, le potenze di $g$ generano tutti gli elementi non nulli di $\mathbb{F}_p^*$. Se $g$ è una radice primitiva, il Problema del Logaritmo Discreto $g^x \equiv h \pmod{p}$ ha sempre una soluzione, e questa soluzione è unica nell'anello degli interi modulo $p-1$, ovvero in $\mathbb{Z}_{p-1}$.

**Complessità Computazionale** La complessità computazionale di un algoritmo misura il numero di operazioni elementari necessarie per la sua esecuzione in funzione della dimensione dell'input. Si utilizza la notazione "Big O", $O(\cdot)$, per descrivere il comportamento asintotico di questa funzione. Si opera una distinzione fondamentale tra:

- **Complessità Polinomiale**: Un algoritmo è considerato "efficiente" o "veloce" se la sua complessità è un polinomio nel logaritmo della dimensione dell'input $n$, ad esempio $O(\log^k(n))$. In termini di numero di bit ($b$) necessari per rappresentare $n$, questo corrisponde a una complessità polinomiale in $b$, come $O(b^k)$.
    
- **Complessità Esponenziale**: Un algoritmo è considerato "difficile" o "lento" se la sua complessità cresce in modo esponenziale con il logaritmo di $n$, ad esempio $O(n^\alpha)$ con $\alpha > 0$. In termini di numero di bit $b$ (dove $n \approx 2^b$), questo corrisponde a una crescita esponenziale, come $O(c^b)$ per una costante $c > 1$ (ad esempio, $c=2^\alpha$). Algoritmi di questo tipo diventano rapidamente impraticabili all'aumentare della dimensione dell'input.
    

Questi concetti di base forniscono il linguaggio e gli strumenti per analizzare formalmente gli algoritmi di risoluzione del DLP, come vedremo nel teorema fondamentale che segue.

## 2. Teoremi e Dimostrazioni Fondamentali

Il teorema di Pohlig-Hellman è uno strumento cruciale per l'analisi del Problema del Logaritmo Discreto. La sua importanza strategica risiede nel dimostrare che la difficoltà del DLP non è assoluta, ma dipende intrinsecamente dalla struttura algebrica dell'ordine del gruppo. Il teorema scompone un problema apparentemente complesso in una serie di sottoproblemi più semplici, basati sulla fattorizzazione prima dell'ordine del gruppo. Questo rivela una potenziale vulnerabilità: se l'ordine ha solo fattori primi piccoli, il DLP può essere risolto in modo efficiente.

Sia $p > 2$ un primo e siano $g, h \in \mathbb{F}_p^*$. Sia $N$ un intero tale che $ord_p(g) \mid N$ (ad esempio, $N = p-1$). Sia $N = p_1^{a_1} \cdot p_2^{a_2} \cdots p_m^{a_m}$ la scomposizione in fattori primi di $N$.

Per ogni $i$ da 1 a $m$, si definiscano $g_i = g^{N/p_i^{a_i}} \pmod{p}$ e $h_i = h^{N/p_i^{a_i}} \pmod{p}$. Il DLP $g^x \equiv h \pmod{p}$ ammette una soluzione se e solo se esistono $y_i$ (per $i=1, \dots, m$) tali che:

$$g_i^{y_i} \equiv h_i \pmod{p}$$

In tal caso, una soluzione $x$ del problema originale $g^x \equiv h \pmod{p}$ è una qualsiasi soluzione del seguente sistema di congruenze:

$$\begin{cases} x \equiv y_1 \pmod{p_1^{a_1}} \\ x \equiv y_2 \pmod{p_2^{a_2}} \\ \vdots \\ x \equiv y_m \pmod{p_m^{a_m}} \end{cases}$$

Questo sistema può essere risolto utilizzando il Teorema Cinese del Resto.

### Dimostrazione del Teorema di Pohlig-Hellman

Per semplicità, dimostriamo il teorema nel caso in cui $N$ abbia solo due fattori primi distinti, ovvero $N = p_1^{a_1} p_2^{a_2}$.

($\Rightarrow$) Se esiste una soluzione $x$ per il DLP originale, allora esistono soluzioni per i sottoproblemi. Assumiamo che esista un intero $x$ tale che $g^x \equiv h \pmod{p}$. Dobbiamo dimostrare che questo stesso $x$, usato come $y_i$, risolve i sottoproblemi. Per $i=1$, calcoliamo $g_1^x$:

$$g_1^x = (g^{N/p_1^{a_1}})^x = (g^x)^{N/p_1^{a_1}}$$

Poiché $g^x \equiv h$, possiamo sostituire:

$$(g^x)^{N/p_1^{a_1}} \equiv h^{N/p_1^{a_1}} \equiv h_1 \pmod{p}$$

Quindi, $g_1^x \equiv h_1 \pmod{p}$. Un ragionamento analogo vale per $i=2$. Pertanto, se una soluzione $x$ esiste, è sufficiente scegliere $y_1 = x$ e $y_2 = x$ per risolvere i sottoproblemi.

($\Leftarrow$) Se esistono soluzioni $y_i$ per i sottoproblemi, allora la soluzione $x$ ottenuta dal Teorema Cinese del Resto risolve il problema originale. Assumiamo che esistano $y_1, y_2$ tali che $g_1^{y_1} \equiv h_1 \pmod{p}$ e $g_2^{y_2} \equiv h_2 \pmod{p}$. Sia $x$ una soluzione del sistema di congruenze:

$$\begin{cases} x \equiv y_1 \pmod{p_1^{a_1}} \\ x \equiv y_2 \pmod{p_2^{a_2}} \end{cases}$$

Poiché $ord_p(g_i)$ è un divisore di $p_i^{a_i}$, dalle congruenze sopra si deduce che $x \equiv y_i \pmod{ord_p(g_i)}$. Questo implica che $g_i^x \equiv g_i^{y_i} \pmod{p}$. Sostituendo la nostra ipotesi, otteniamo:

$$g_i^x \equiv h_i \pmod{p} \quad \text{per } i=1,2$$

I termini $N/p_1^{a_1}$ e $N/p_2^{a_2}$ sono coprimi. Si noti che, dato $N = p_1^{a_1} p_2^{a_2}$, questi due termini sono uguali a $p_2^{a_2}$ e $p_1^{a_1}$ rispettivamente. Poiché $p_1$ e $p_2$ sono primi distinti, questi termini sono coprimi, il che giustifica l'applicazione del Teorema di Bézout. Pertanto, esistono interi $u_1, u_2$ tali che:

$$u_1 \frac{N}{p_1^{a_1}} + u_2 \frac{N}{p_2^{a_2}} = 1$$

Ora, consideriamo $g^x$ e usiamo questa identità sull'esponente:

$$g^x = g^{x(u_1 \frac{N}{p_1^{a_1}} + u_2 \frac{N}{p_2^{a_2}})} = (g^{x \frac{N}{p_1^{a_1}}})^{u_1} \cdot (g^{x \frac{N}{p_2^{a_2}}})^{u_2}$$

Riscriviamo l'espressione usando le definizioni di $g_i$ e $h_i$:

$$(g_1^x)^{u_1} \cdot (g_2^x)^{u_2} \equiv (h_1)^{u_1} \cdot (h_2)^{u_2} = (h^{\frac{N}{p_1^{a_1}}})^{u_1} \cdot (h^{\frac{N}{p_2^{a_2}}})^{u_2} = h^{u_1 \frac{N}{p_1^{a_1}} + u_2 \frac{N}{p_2^{a_2}}} = h^1 = h$$

Abbiamo quindi dimostrato che $g^x \equiv h \pmod{p}$, completando la dimostrazione.

## 3. Guida alla Risoluzione degli Esercizi

Questa sezione fornisce una guida pratica e strutturata per risolvere le diverse tipologie di esercizi sul Problema del Logaritmo Discreto. Padroneggiare questi metodi algoritmici è un passo fondamentale per affrontare con successo le prove d'esame e per comprendere a fondo le implicazioni pratiche della teoria.

### 3.1 Metodo Naive (Forza Bruta)

Questo è l'approccio più diretto e intuitivo, ma anche il meno efficiente.

- **Descrizione**: Si calcolano in sequenza tutte le potenze di $g \pmod{p}$: $g^1, g^2, g^3, \dots$ fino a quando non si trova un esponente $x$ tale che $g^x \equiv h \pmod{p}$.
    
- **Complessità**: La sua complessità computazionale è $O(N)$, dove $N$ è l'ordine di $g$. Questo lo rende computazionalmente impraticabile per valori di $N$ anche moderatamente grandi.
    

### 3.2 Algoritmo Baby-step Giant-step

Questo algoritmo offre un significativo miglioramento rispetto alla forza bruta, riducendo la complessità a spese di un maggiore utilizzo di memoria.

- **Obiettivo**: Risolvere $g^x \equiv h \pmod{p}$ con una complessità di $O(\sqrt{N}\log N)$.
    
- **Passo 1**: Si definisce $n = \lfloor\sqrt{N}\rfloor + 1$, dove $N$ è l'ordine di $g$.
    
- **Passo 2 (Baby Steps)**: Si crea una lista calcolando e memorizzando i valori $g^i \pmod{p}$ per $i$ che va da 0 a $n-1$.
    
- **Passo 3**: Si calcola l'inverso moltiplicativo $g^{-n} \pmod{p}$.
    
- **Passo 4 (Giant Steps)**: Si crea una seconda lista calcolando i valori $h \cdot (g^{-n})^j \pmod{p}$ per $j$ che va da 0 a $n-1$.
    
- **Passo 5**: Si cerca una corrispondenza tra le due liste. Se si trova un valore comune, ovvero $g^i = h \cdot g^{-nj}$, allora la soluzione del DLP è $x = i + nj$.
    
- **Suggerimento pratico**: Per trovare la corrispondenza in modo efficiente, è consigliabile ordinare una delle due liste e poi scorrere la seconda tramite ricerca binaria.
    

### 3.3 Algoritmo di Pohlig-Hellman

Questo algoritmo sfrutta la struttura dell'ordine del gruppo per scomporre il problema in sottoproblemi più semplici.

- **Prerequisito**: Fattorizzazione prima dell'ordine $N$ di $g$: $N = p_1^{a_1} \cdot p_2^{a_2} \cdots p_m^{a_m}$.
    
- **Passo 1**: Per ogni fattore primo $p_i^{a_i}$, si riduce il problema originale a un sottoproblema: $g_i = g^{N/p_i^{a_i}}$ e $h_i = h^{N/p_i^{a_i}}$.
    
- **Passo 2**: Si risolve ogni sottoproblema $g_i^{y_i} \equiv h_i \pmod{p}$ per trovare $y_i$.
    
- **Passo 3**: Si costruisce il sistema di congruenze: $x \equiv y_i \pmod{p_i^{a_i}}$ per $i=1, \dots, m$.
    
- **Passo 4**: Si risolve il sistema utilizzando il Teorema Cinese del Resto.
    

### 3.4 Analisi Comparativa e Scelta Strategica del Metodo

La scelta dell'algoritmo più efficiente dipende criticamente dalla struttura della scomposizione in fattori primi dell'ordine $N$.

|**Metodo**|**Quando Utilizzarlo**|**Motivazione**|
|---|---|---|
|**Baby-step Giant-step**|Quando $N$ ha almeno un grande fattore primo.|La sua complessità $O(\sqrt{N})$ dipende dall'ordine totale $N$. Se $N$ ha un grande fattore primo $q$, PH si avvicina a $O(q)$, rendendo BSGS più gestibile.|
|**Pohlig-Hellman**|Quando tutti i fattori primi di $N$ sono piccoli.|La complessità dipende dalla somma dei fattori primi ($\sum p_i a_i$). Se i $p_i$ sono piccoli, PH è estremamente veloce.|

## 4. Esempi Svolti e Casi di Studio

### Caso di Studio 1: Applicazione del Baby-step Giant-step

**Problema**: Risolvere l'equazione $3^x \equiv 11 \pmod{31}$.

**Risoluzione**: L'ordine è $N = 30$.

1. **Calcolo di $n$**: $n = \lfloor\sqrt{30}\rfloor + 1 = 6$.
    
2. **Baby Steps**: $\{3^0, 3^1, 3^2, 3^3, 3^4, 3^5\} \equiv \{1, 3, 9, 27, 19, 26\} \pmod{31}$.
    
3. **Giant Steps**: $3^{-6} \equiv 2 \pmod{31}$. Calcoliamo $11 \cdot (2)^j$:
    
    - $j=0: 11$
        
    - $j=1: 22$
        
    - $j=2: 13$
        
    - $j=3: 26$
        
4. **Corrispondenza**: Valore 26 trovato per $i=5$ e $j=3$.
    
5. **Soluzione**: $x = 5 + 6 \cdot 3 = \mathbf{23}$.
    

### Caso di Studio 2: Applicazione dell'Algoritmo di Pohlig-Hellman

**Problema**: Risolvere l'equazione $2^x \equiv 7 \pmod{13}$.

**Risoluzione**: L'ordine è $N = 12 = 2^2 \cdot 3$.

1. **Sottoproblema 1 (mod 4)**: $g_1 = 2^3 \equiv 8, h_1 = 7^3 \equiv 5 \pmod{13}$. Risolviamo $8^{y_1} \equiv 5 \rightarrow y_1 = 3$.
    
2. **Sottoproblema 2 (mod 3)**: $g_2 = 2^4 \equiv 3, h_2 = 7^4 \equiv 9 \pmod{13}$. Risolviamo $3^{y_2} \equiv 9 \rightarrow y_2 = 2$.
    
3. **Sistema**: $x \equiv 3 \pmod 4$ e $x \equiv 2 \pmod 3$.
    
4. **Soluzione**: $x = \mathbf{11}$.
    

### Caso di Studio 3: Confronto delle Complessità su Scenari Reali

- **Scenario A (Fattori Primi Piccoli)**: $p=17681, p-1 = 2^4 \cdot 5 \cdot 13 \cdot 17$. Pohlig-Hellman richiede $\sim 58$ operazioni contro le $\sim 1050$ di BSGS. **PH è la scelta ottimale.**
    
- **Scenario B (Grande Fattore Primo)**: $p=20000159, p-1 = 2 \cdot 10000079$. BSGS richiede $\sim 51000$ operazioni contro gli oltre 10 milioni di PH. **BSGS è la scelta obbligata.**
    

**Conclusione Strategica**: La sicurezza basata sul DLP non è monolitica. La robustezza è una funzione della fattorizzazione dell'ordine. Nella pratica, si scelgono gruppi il cui ordine contiene almeno un fattore primo molto grande (usando ad esempio i **Safe Primes**) per costringere l'avversario a usare approcci esponenziali lenti.