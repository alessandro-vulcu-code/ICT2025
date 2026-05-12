# Fattorizzazione tramite Test di Miller-Rabin e Algoritmo $p-1$ di Pollard

## 1.0 Introduzione: Strategie Avanzate di Fattorizzazione
Dopo aver analizzato in dettaglio i test di primalità, il nostro focus si sposta ora su algoritmi di fattorizzazione efficaci. L'obiettivo è scomporre numeri composti che possono superare test di primalità più semplici, come i **numeri di Carmichael**, per i quali il test di Fermat fallisce nel rivelarne la natura composta. La capacità di fattorizzare numeri interi di grandi dimensioni è un pilastro della crittografia moderna, in particolare per la sicurezza di sistemi come **RSA**.



Questi appunti esploreranno due potenti tecniche che sfruttano le proprietà matematiche alla base dei test di primalità per trovare i fattori di un numero. Inizieremo con un metodo che deriva direttamente da una proprietà collaterale dei testimoni di Miller-Rabin.

> [!NOTE] **Nota Didattica**
> Perché i numeri di Carmichael sono così importanti in questo contesto? Essi sono gli "impostori" perfetti del mondo della primalità. Sconfiggono il semplice test di Fermat per ogni base coprima, comportandosi come numeri primi pur essendo composti. Questa debolezza del test di Fermat ci costringe a usare strumenti più sofisticati come il test di Miller-Rabin. La cosa affascinante, che esploreremo a breve, è che proprio il modo in cui il test di Miller-Rabin smaschera questi impostori può essere intelligentemente riutilizzato per fattorizzarli. Si crea così una bella narrazione: un problema (i numeri di Carmichael) porta a una soluzione (il test MR), che a sua volta fornisce uno strumento inaspettato (la fattorizzazione).

---

## 2.0 Fattorizzazione tramite un Testimone di Miller-Rabin
L'approccio di questo metodo si basa su un'osservazione elegante: un numero intero $a$ che soddisfa il test di Fermat (ovvero $a^{N-1} \equiv 1 \pmod{N}$) ma che si rivela essere un testimone di Miller-Rabin, ci fornisce direttamente le informazioni necessarie per calcolare i fattori non banali di $N$.

### Concetti Chiave
* **Testimone di Fermat**: Un intero $a$ è un testimone di Fermat per un numero composto $N$ se $a^{N-1} \not\equiv 1 \pmod{N}$. Se invece $a^{N-1} \equiv 1 \pmod{N}$, si dice che $N$ "passa" il test di Fermat rispetto alla base $a$.
* **Testimone di Miller-Rabin (MR)**: Dato $N-1 = 2^k \cdot q$ con $q$ dispari, un intero $a$ è un testimone di Miller-Rabin per $N$ se:
	1. $a_0 := a^q \not\equiv 1 \pmod{N}$
	2. Nessuno dei quadrati successivi $a_0, a_1, \dots, a_{k-1}$ è congruo a $-1 \pmod N$.



### Teorema: Proposizione di Fattorizzazione
> **PROPOSITION (Factorization via a Miller-Rabin witness that passes Fermat test)**
> Let $N$ odd, $N - 1 = 2^k q$, with $q$ odd, and suppose $a \in \mathbb{N}$ passes the Fermat test: $a^{N-1} \equiv 1 \pmod{N}$. Let $a_j := a^{2^j q} \pmod{N}$, $j=0, \dots, k$. If $a$ is a MR witness for $N$, let $i = \min\{j \in \{0, \dots, k\} : a_j \equiv 1 \pmod{N}\}$. Then $i \ge 1$ and $\gcd(a_{i-1} \pm 1, N)$ are nontrivial factors of $N$.

### Dimostrazione
1. L'insieme degli indici $j$ tali che $a_j \equiv 1 \pmod{N}$ non è vuoto perché $a$ passa il test di Fermat ($a_k \equiv 1 \pmod N$). Esiste quindi un indice minimo $i$.
2. $i \ge 1$ perché $a_0 \not\equiv 1 \pmod{N}$ (condizione MR).
3. Sappiamo che $(a_{i-1})^2 \equiv a_i \equiv 1 \pmod{N}$.
4. $a_{i-1}$ è una radice quadrata di $1 \pmod N$. Analizziamo:
	* $a_{i-1} \not\equiv 1 \pmod{N}$ per minimalità di $i$.
	* $a_{i-1} \not\equiv -1 \pmod{N}$ per la seconda condizione MR.
5. Poiché $(a_{i-1})^2 - 1 \equiv 0 \pmod{N}$, abbiamo che $N$ divide $(a_{i-1} - 1)(a_{i-1} + 1)$. Ma $N$ non divide nessuno dei due singolarmente. Pertanto, $\gcd(a_{i-1} \pm 1, N)$ sono fattori non banali.

### Guida alla Risoluzione: Algoritmo Passo-Passo
1. **Dati Iniziali**: Numero dispari $N$ e base $a$ tale che $a^{N-1} \equiv 1 \pmod N$.
2. **Scomposizione Esponente**: $N-1 = 2^k \cdot q$.
3. **Calcolo Sequenza**: $a_0 \equiv a^q \pmod{N}$, $a_j \equiv a_{j-1}^2 \pmod{N}$.
4. **Identificazione Indice**: Trovare il primo $i$ per cui $a_i \equiv 1 \pmod{N}$.
5. **Calcolo Fattori**: $d_1 = \gcd(a_{i-1} - 1, N)$ e $d_2 = \gcd(a_{i-1} + 1, N)$.

### Esempi Svolti
* **Caso Studio 1: $N = 561, a = 2$**
	* $N-1 = 560 = 2^4 \cdot 35$.
	* $a_0 \equiv 2^{35} \equiv 263$; $a_1 \equiv 263^2 \equiv 166$; $a_2 \equiv 166^2 \equiv 67$; $a_3 \equiv 67^2 \equiv 1$.
	* $i=3 \implies a_{i-1} = 67$.
	* $d_1 = \gcd(66, 561) = 33$; $d_2 = \gcd(68, 561) = 17$.

---

## 3.0 Generalizzazione: Fattorizzazione tramite Test di tipo Miller-Rabin
Quando il test di Fermat fallisce, possiamo usare il Teorema di Eulero: $a^{\phi(N)} \equiv 1 \pmod{N}$. Possiamo usare un qualsiasi esponente pari $L$ tale che $a^L \equiv 1 \pmod N$.

### Teorema: Proposizione di Fattorizzazione Generalizzata
> **PROPOSITION (Factorization via a Miller-Rabin like test)**
> Let $N \in \mathbb{N}_{\ge 1}$. Suppose that $L \ge 1$ is even and such that $a^L \equiv 1 \pmod{N}$. Write $L = 2^k q, 2 \nmid q$. Assume: (i) $a_0 \not\equiv 1 \pmod{N}$, (ii) Let $i = \min\{j \in \{1, \dots, k\} : a_j \equiv 1 \pmod{N}\}$. If $a_{i-1} \not\equiv -1 \pmod{N}$ then $\gcd(a_{i-1} \pm 1, N)$ are nontrivial factors of $N$.

### Esempio Svolto: $N = 32817151$
* $a = 2$, $L = 200 \implies 2^{200} \equiv 1 \pmod N$.
* $L = 2^3 \cdot 25 \implies k=3, q=25$.
* $a_0 \equiv 2^{25} \equiv 737281$; $a_1 \equiv a_0^2 \equiv 32800948$; $a_2 \equiv a_1^2 \equiv 1$.
* $i=2, a_1 \not\equiv -1$.
* $d_1 = \gcd(32800947, 32817151) = 4051$; $d_2 = \gcd(32800949, 32817151) = 8101$.

---

## 4.0 Algoritmo di Fattorizzazione $p-1$ di Pollard
Si fonda sul Piccolo Teorema di Fermat e funziona quando un fattore $p$ di $N$ è tale che $p-1$ è un numero **"liscio" (B-smooth)**.



### Logica dell'Algoritmo
1. Se $p|N$, allora $a^{p-1} \equiv 1 \pmod p$.
2. Se $p-1$ ha fattori piccoli, allora $p-1 | n!$.
3. Allora $a^{n!} \equiv 1 \pmod p$, quindi $p$ divide $a^{n!} - 1$.
4. $p = \gcd(a^{n!} - 1, N)$.

### Guida alla Risoluzione
1. Scegli $a=2$, $n=2$.
2. Calcola $a_n \equiv (a_{n-1})^n \pmod N$.
3. Calcola $d = \gcd(a_n - 1, N)$.
4. Se $1 < d < N$, successo. Se $d=N$, fallimento di Pollard (ma utile per MR).

---

## 5.0 Sinergia tra Metodi: Gestire il caso $\gcd(a^{n!} - 1, N) = N$
Ottenere $N$ significa che $a^{n!} \equiv 1 \pmod N$. Questo ci fornisce l'esponente $L = n!$ per il metodo MR generalizzato.

### Esempi Svolti (Casi Studio)
* **Successo Pivot: $N = 91, a = 2$**
	* Pollard per $n=4$: $2^{24} \equiv 1 \pmod{91} \implies \gcd=91$.
	* Pivot MR: $L=24 = 2^3 \cdot 3$.
	* $a_0 \equiv 2^3 \equiv 8$; $a_1 \equiv 64$; $a_2 \equiv 1$.
	* $i=2, a_1 = 64 \not\equiv -1 \pmod{91}$.
	* $\gcd(63, 91) = 7$; $\gcd(65, 91) = 13$.

* **Fallimento Pivot: $N = 65, a = 2$**
	* Pollard per $n=4$: $2^{24} \equiv 1 \pmod{65} \implies \gcd=65$.
	* Pivot MR: $a_1 \equiv 64 \equiv -1 \pmod{65}$.
	* **Violazione condizione**: $a_{i-1} \equiv -1$, il metodo non trova fattori. Cambiare base $a$.