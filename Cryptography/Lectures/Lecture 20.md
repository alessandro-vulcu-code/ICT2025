# Teorema di Eulero e Applicazioni RSA

## 1. Concetti Chiave e Definizioni
Il **Teorema di Eulero** rappresenta una pietra miliare nella teoria dei numeri e costituisce una potente generalizzazione del **Piccolo Teorema di Fermat**. La sua importanza va ben oltre l'ambito puramente teorico, poiché fornisce le fondamenta matematiche per la crittografia a chiave pubblica moderna, in particolare per il sistema **RSA**, uno degli algoritmi più diffusi e influenti per la protezione delle comunicazioni digitali. Per comprendere appieno il teorema, è essenziale padroneggiare alcuni concetti preliminari.

### Funzione Totiente di Eulero ($\phi$)
La **funzione totiente di Eulero**, indicata con $\phi(n)$, conta il numero di interi positivi minori o uguali a $n$ che sono coprimi con $n$. Formalmente, questo equivale alla cardinalità dell'insieme degli elementi invertibili in $\mathbb{Z}/n\mathbb{Z}$.



**Proprietà e Metodi di Calcolo:**
Il calcolo di $\phi(n)$ dipende dalla fattorizzazione in numeri primi di $n$. I casi fondamentali per le nostre applicazioni sono:

1. **Quando $p$ è un numero primo:** Poiché tutti i numeri da $1$ a $p-1$ sono coprimi con $p$, la funzione è semplicemente: 
   $$\phi(p) = p - 1$$
2. **Quando $n = pq$, con $p$ e $q$ primi distinti:** La funzione è moltiplicativa, quindi il calcolo si scompone nel prodotto dei totienti dei suoi fattori: 
   $$\phi(pq) = \phi(p)\phi(q) = (p-1)(q-1)$$
3. **Quando $n$ è un prodotto di primi distinti $n = p_1 \cdot \dots \cdot p_r$:** La proprietà moltiplicativa si estende a tutti i fattori: 
   $$\phi(n) = \phi(p_1) \cdot \dots \cdot \phi(p_r)$$

### Massimo Comun Divisore ($gcd$)
La condizione $gcd(a, n) = 1$ (**Massimo Comun Divisore**, in inglese *Greatest Common Divisor*), indica che l'intero $a$ e il modulo $n$ sono coprimi. Questo prerequisito è essenziale per l'applicazione diretta del Teorema di Eulero, in quanto garantisce che $a$ sia un elemento invertibile nell'anello delle classi di resto modulo $n$. Essere invertibile significa che esiste un altro intero tale che il loro prodotto è congruo a $1$ modulo $n$, permettendo di effettuare operazioni analoghe alla "divisione" in aritmetica modulare, un concetto cruciale per le operazioni crittografiche.

Se questa condizione non è soddisfatta, il teorema nella sua forma base non è valido.

**Controesempio:** Siano $a=3$ e $n=6$. Abbiamo che $\phi(6)=2$. Il teorema non si applica perché $gcd(3, 6) = 3 \neq 1$. Infatti, $3^2 \equiv 9 \equiv 3 \pmod{6}$, che non è congruo a $1$.

È importante notare che il Teorema di Eulero generalizza il Piccolo Teorema di Fermat, che richiede che il modulo sia un numero primo. Il teorema di Eulero funziona anche per moduli composti, a patto che la base sia coprima con essi. Per esempio, se $a=2$ e $n=9$, $gcd(2,9)=1$ ma $n$ non è primo. Il Piccolo Teorema di Fermat non si applica, ma il Teorema di Eulero sì.

Questi due concetti sono i pilastri su cui si costruisce l'enunciato e la dimostrazione del Teorema di Eulero.

---

## 2. Teoremi e Dimostrazioni Fondamentali
Questa sezione rappresenta il nucleo teorico della lezione. Analizzeremo in dettaglio il Teorema di Eulero, la sua dimostrazione formale, i suoi corollari più importanti e un lemma fondamentale che ne estende l'applicabilità, gettando le basi per le sue applicazioni pratiche nella crittografia.

### 2.1. Il Teorema di Eulero
Sia $n \in \mathbb{N}_{\ge 1}$ e sia $a \in \mathbb{Z}$ con $gcd(a, n) = 1$. Allora: 
$$a^{\phi(n)} \equiv 1 \pmod{n}$$

**Dimostrazione:**
La dimostrazione ricalca quella del Piccolo Teorema di Fermat, operando sull'insieme degli elementi invertibili modulo $n$.

1. **Definizione dell'insieme $T$:** Consideriamo l'insieme $T$ delle classi di resto degli interi coprimi con $n$. Questo insieme è l'insieme degli elementi invertibili in $\mathbb{Z}/n\mathbb{Z}$: 
   $$T := \{(i)_n : 1 \le i \le n, gcd(i, n) = 1\}$$ 
   La cardinalità (il numero di elementi) di questo insieme è, per definizione, $|T| = \phi(n)$.
2. **Moltiplicazione dell'insieme $T$:** Moltiplichiamo ogni elemento di $T$ per $(a)_n$. Poiché $gcd(a, n)=1$, $a$ è invertibile modulo $n$, e la moltiplicazione per $(a)_n$ è una biezione (una mappatura uno-a-uno e suriettiva) sull'insieme finito $T$. Pertanto, questa operazione semplicemente riorganizza (permuta) gli elementi di $T$, restituendo lo stesso insieme. 
   $$T \cdot (a)_n := \{(ia)_n : (i)_n \in T\} = T$$
3. **Uguaglianza dei prodotti:** Dato che i due insiemi contengono gli stessi elementi, il prodotto di tutti gli elementi deve essere uguale: 
   $$\prod_{(i)_n \in T} (ia)_n = \prod_{(i)_n \in T} (i)_n$$
4. **Semplificazione e conclusione:** Utilizzando le proprietà dell'aritmetica modulare, possiamo riscrivere il prodotto a sinistra, raccogliendo i termini $(a)_n$: 
   $$(a)_n^{\phi(n)} \cdot \prod_{(i)_n \in T} (i)_n = \prod_{(i)_n \in T} (i)_n$$ 
   Poiché ogni elemento $(i)_n \in T$ è invertibile, anche il loro prodotto è invertibile. Possiamo quindi moltiplicare entrambi i lati per l'inverso del prodotto (cioè "semplificarlo"), ottenendo la tesi: 
   $$a^{\phi(n)} \equiv 1 \pmod{n}$$

### 2.2. Corollari e Conseguenze Pratiche
Una delle conseguenze più utili del teorema riguarda la riduzione di esponenti molto grandi nei calcoli di potenze modulari.

**Corollario:** Siano $n \in \mathbb{N}_{\ge 1}$ e $a \in \mathbb{Z}$ con $gcd(a, n) = 1$. Se $x \equiv y \pmod{\phi(n)}$, allora: 
$$a^x \equiv a^y \pmod{n}$$

**Dimostrazione:** Dall'ipotesi $x \equiv y \pmod{\phi(n)}$, sappiamo che esiste un intero $k$ tale che $x = y + k\phi(n)$. Sostituendo nell'espressione $a^x$: 
$$a^x = a^{y + k\phi(n)} = a^y \cdot a^{k\phi(n)} = a^y \cdot (a^{\phi(n)})^k$$ 
Applicando il Teorema di Eulero, sappiamo che $a^{\phi(n)} \equiv 1 \pmod{n}$. Quindi: 
$$a^x \equiv a^y \cdot (1)^k \pmod{n} \implies a^x \equiv a^y \pmod{n}$$

### 2.3. Un Lemma Fondamentale: Estensione del Teorema
Il corollario precedente richiede la condizione $gcd(a, n) = 1$. Tuttavia, in contesti come RSA, è necessario un risultato più generale. Il seguente lemma è il meccanismo critico che rende RSA robusto, poiché garantisce che la decifratura funzioni anche nel caso non coprimo ($gcd(m,N) > 1$), una necessità pratica. Estende il corollario a patto che $n$ sia un prodotto di primi distinti.

**Lemma Fondamentale:** Siano $p_1, \dots, p_r$ primi distinti, $n = p_1 \cdot \dots \cdot p_r$ e $a \in \mathbb{Z}$. Se $x, y \in \mathbb{N}_{\ge 1}$ e $x \equiv y \pmod{\phi(n)}$, allora: 
$$a^x \equiv a^y \pmod{n}$$

**Limitazioni del Lemma:** È cruciale notare che questo lemma non è valido se $n$ non è un prodotto di primi distinti (ovvero, se $n$ ha fattori primi ripetuti).

**Controesempio:** Sia $n=12=2^2 \cdot 3$. In questo caso $\phi(12)=4$. Prendiamo gli esponenti $x=5$ e $y=1$. Abbiamo che $5 \equiv 1 \pmod{4}$, quindi le condizioni del lemma sull'esponente sono soddisfatte. Tuttavia, se scegliamo la base $a=6$ (notare che $gcd(6, 12) \neq 1$), il lemma fallisce:
1. $6^5 = 7776 \equiv 0 \pmod{12}$
2. $6^1 \equiv 6 \pmod{12}$ 
Poiché $0 \not\equiv 6 \pmod{12}$, il lemma non si applica.

---

## 3. Guida alla Risoluzione degli Esercizi
Questa sezione ha un'importanza pratica fondamentale. Fornisce metodologie algoritmiche passo-passo per risolvere due tipologie di esercizi comuni basate sul Teorema di Eulero.

### 3.1. Tipologia 1: Calcolo di Potenze Modulari Grandi
**Obiettivo:** Calcolare $a^x \pmod{n}$ dove $x$ è un esponente molto grande.

**Guida Algoritmica:**
1. **Analisi Preliminare:** Controllare il valore di $gcd(a, n)$. Il percorso risolutivo dipende da questo risultato.
2. **Caso 1: $gcd(a, n) = 1$ (base e modulo sono coprimi)**
   - a. Calcolare la funzione totiente del modulo: $\phi(n)$.
   - b. Ridurre l'esponente $x$ calcolando il resto della divisione per $\phi(n)$. Sia $y = x \pmod{\phi(n)}$. **Nota:** se il resto è $0$, si deve usare $\phi(n)$ come nuovo esponente, non $0$. Questo perché la congruenza si basa su $a^{\phi(n)} \equiv 1 \pmod{n}$, che è anche il valore di $a^0 \pmod{n}$.
   - c. Calcolare $a^y \pmod{n}$. Il risultato ottenuto è la soluzione finale.
3. **Caso 2: $gcd(a, n) > 1$ (base e modulo non sono coprimi)**
   - a. Verificare se il modulo $n$ è un prodotto di numeri primi distinti.
   - b. Se $n$ è un prodotto di primi distinti e gli esponenti sono $\ge 1$, è possibile applicare il **Lemma Fondamentale**. La procedura è identica al Caso 1.
   - c. Se $n$ non è un prodotto di primi distinti (es. $n=12=2^2 \cdot 3$), il metodo non è direttamente applicabile. Potrebbero essere necessarie altre tecniche, come il **Teorema Cinese del Resto**.

### 3.2. Tipologia 2: Decifratura in un Sistema RSA
**Obiettivo:** Dato un testo cifrato $c$, una chiave pubblica $(N, e)$ e una chiave segreta $d$, calcolare il messaggio originale $m$.

**Guida Algoritmica:**
1. **Formula di Decifratura:** La relazione fondamentale della decifratura RSA è: 
   $$m \equiv c^d \pmod{N}$$
2. **Processo di Calcolo:** Si applica la stessa tecnica del calcolo di potenza modulare efficiente (Tipologia 1).
3. **Giustificazione Teorica:** La correttezza del processo di decifratura RSA, ovvero che $(m^e)^d \equiv m \pmod{N}$, è garantita dai teoremi analizzati:
   - Se **$gcd(m, N) = 1$**, deriva dal Corollario del Teorema di Eulero, poiché $ed \equiv 1 \pmod{\phi(N)}$.
   - Se **$gcd(m, N) > 1$**, è garantita dal **Lemma Fondamentale**. Questo è possibile perché in RSA il modulo $N$ è sempre costruito come prodotto di due primi distinti ($N=pq$).

---

## 4. Esempi Svolti e Casi di Studio

### 4.1. Calcolo della Funzione $\phi(n)$
**Esempio: Calcolo di $\phi(15)$** Dato che $15 = 3 \cdot 5$, dove 3 e 5 sono primi distinti, applichiamo la proprietà moltiplicativa: 
$$\phi(15) = \phi(3 \cdot 5) = \phi(3)\phi(5) = (3-1)(5-1) = 2 \cdot 4 = 8$$

### 4.2. Caso di Studio: Scambio Crittografico RSA
Questo esempio illustra il processo di un intero ciclo di cifratura e decifratura RSA.



**Setup (Alice)**
1. Alice sceglie due numeri primi distinti molto grandi, $p$ e $q$, e li mantiene segreti.
2. Calcola il modulo pubblico: $N = pq$. (Es. $p=1223$, $q=1987 \implies N = 2430101$).
3. Calcola il valore segreto: $\phi(N) = (p-1)(q-1)$.
4. Sceglie un esponente di cifratura pubblico $e$ tale che $1 < e < \phi(N)$ e $gcd(e, \phi(N)) = 1$.
5. Calcola l'esponente di decifratura segreto $d$ tale che $ed \equiv 1 \pmod{\phi(N)}$.
6. Alice rende pubblica la sua chiave: $(N, e)$. Mantiene segreti $p, q, d$ e $\phi(N)$.

**Cifratura (Bob)**
1. Bob utilizza la chiave pubblica di Alice per calcolare il testo cifrato $c$: 
   $$c \equiv m^e \pmod{N}$$

**Decifratura (Alice)**
1. Alice riceve $c$ e calcola: 
   $$m \equiv c^d \pmod{N}$$
**Giustificazione:** $$c^d \equiv (m^e)^d \equiv m^{ed} \pmod{N}$$ 
Poiché $ed \equiv 1 \pmod{\phi(N)}$, per il Corollario del Teorema di Eulero o per il Lemma Fondamentale, riduciamo l'esponente: 
$$m^{ed} \equiv m^1 \equiv m \pmod{N}$$