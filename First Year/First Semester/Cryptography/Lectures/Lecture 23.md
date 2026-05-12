# Metodi di Fattorizzazione
## 1.0 Introduzione: L'Importanza della Fattorizzazione in Crittografia
La fattorizzazione, ovvero la scomposizione di un numero intero nei suoi fattori primi, rappresenta una delle pietre miliari della matematica e, in particolare, della crittografia moderna. La sicurezza di algoritmi crittografici ampiamente utilizzati, come l'**RSA**, si fonda sulla presupposta difficoltà computazionale di fattorizzare numeri molto grandi che sono il prodotto di due numeri primi. Se un avversario fosse in grado di risolvere questo problema in modo efficiente, l'intera infrastruttura di sicurezza basata su tali algoritmi crollerebbe.



L'obiettivo di questi appunti è analizzare in dettaglio tre metodi fondamentali per la fattorizzazione. Partiremo dall'approccio più intuitivo, la **"Trial Division"** (divisione per tentativi), per poi esplorare tecniche più sofisticate come il **metodo di Fermat** e la sua potente generalizzazione, che trasforma il problema della fattorizzazione nella ricerca di una congruenza di quadrati.

La difficoltà storica di questo problema fu notoriamente espressa dall'economista e logico del XIX secolo William S. Jevons, che lanciò questa sfida riguardo a un numero che ora porta il suo nome:
> "Sapevate dire quali due numeri, moltiplicati tra loro, producono il numero 8 616 460 799? Penso sia improbabile che qualcuno, a parte me, lo saprà mai." — *William S. Jevons, The Principles of Science, 1877*

---

## 2.0 Concetti Chiave e Definizioni
Prima di addentrarci negli algoritmi, è essenziale padroneggiare alcune definizioni fondamentali:

* **Fattorizzazione**: Il processo di scomposizione di un numero intero nei suoi divisori primi. Ad esempio, la fattorizzazione di $12$ è $2^2 \cdot 3$.
* **Divisore non banale**: Un fattore di un numero $N$ che è strettamente maggiore di $1$ e strettamente minore di $N$. Trovare un divisore non banale equivale a "rompere" la composizione di $N$.
* **Complessità computazionale esponenziale**: Una classe di algoritmi il cui tempo di esecuzione cresce in modo esponenziale rispetto alla dimensione dell'input. Questo li rende intrinsecamente lenti e del tutto impraticabili per input di grandi dimensioni.

---

## 3.0 Algoritmo 1: Trial Division (Divisione per Tentativi)

### 3.1 Contesto e Principio di Funzionamento
La **"Trial Division"** è l'approccio più diretto e basilare alla fattorizzazione. La sua logica è semplice: per fattorizzare un numero $N$, si tenta di dividerlo iterativamente per tutti i numeri primi, partendo da $2$, fino a un certo limite superiore. Questo limite non è $N$ stesso, ma è sufficiente arrivare fino alla radice quadrata di $N$.

### 3.2 Proposizione Fondamentale e Dimostrazione
**Proposizione**: Se $N > 2$ non è un numero primo, allora ammette un divisore non banale $d \le \sqrt{N}$.

**Dimostrazione (per contraddizione)**:
Poiché $N$ è un numero composto, possiamo scriverlo come $N = ab$, dove $a$ e $b$ sono divisori non banali, ovvero $1 < a, b < N$. Supponiamo per assurdo che entrambi i fattori siano maggiori della radice quadrata di $N$:
$$a > \sqrt{N} \quad \text{e} \quad b > \sqrt{N}$$
Moltiplicando i due fattori, otteniamo:
$$N = ab > \sqrt{N} \cdot \sqrt{N} = N$$
Questo porta alla contraddizione $N > N$. Pertanto, almeno uno dei due fattori ($a$ o $b$) deve essere minore o uguale a $\sqrt{N}$.

### 3.3 Guida alla Risoluzione (Algoritmo)


1.  Dato un intero $N$ da fattorizzare.
2.  Testa la divisibilità di $N$ per ogni numero primo $p$, partendo da $p=2$.
3.  Continua il processo per tutti i numeri primi fino a $\lfloor\sqrt{N}\rfloor$.
4.  Se si trova un primo $p$ che divide $N$, allora $p$ è un fattore non banale di $N$.
5.  Se nessun primo fino a $\lfloor\sqrt{N}\rfloor$ divide $N$, $N$ è un numero primo.

### 3.4 Esempio Svolto: Il Numero di Jevons
* **Numero da fattorizzare**: $J = 8.616.460.799$
* **Limite superiore**: $\sqrt{J} \approx 92.824,8$.
* **Fattorizzazione**: Dopo numerosi tentativi, si scopre che: $J = 89.681 \cdot 96.079$.

### 3.5 Limiti e Complessità Computazionale
La Trial Division ha complessità esponenziale. Per un numero $N$ di 100 cifre:
* Passaggi richiesti: ordine di $10^{50}$.
* Potenza di calcolo (es. Frontier): $1,1 \times 10^{18}$ calcoli al secondo.
* Tempo stimato: circa $3 \times 10^{24}$ anni.

---

## 4.0 Algoritmo 2: Metodo di Fattorizzazione di Fermat

### 4.1 Contesto e Principio Matematico
Si basa sull'identità algebrica della **differenza di quadrati**:
$$N = b^2 - a^2 = (b - a)(b + a)$$
L'idea è cercare due interi $a$ e $b$ tali che $N$ sia espresso come differenza dei loro quadrati.

### 4.2 Proposizione e Dimostrazione
**Proposizione**: Sia $N \ge 3$ un intero dispari. Esistono $x, y \in \mathbb{N}$ tali che $xy = N$ se e solo se esistono $a, b \in \mathbb{N}$ tali che $b^2 - a^2 = N$.

**Dimostrazione**:
* $(\Leftarrow)$: Se $b^2 - a^2 = N$, allora $N = (b-a)(b+a)$. Posto $x=b-a$ e $y=b+a$, abbiamo la fattorizzazione.
* $(\Rightarrow)$: Supponiamo $N = xy$. Poiché $N$ è dispari, $x$ e $y$ sono dispari. Definiamo $b = \frac{x+y}{2}$ e $a = \frac{x-y}{2}$ (entrambi interi). Allora $b^2 - a^2 = \left(\frac{x+y}{2}\right)^2 - \left(\frac{x-y}{2}\right)^2 = xy = N$.

### 4.3 Guida alla Risoluzione (Algoritmo)


1.  Dato un intero dispari $N$.
2.  Inizia con $b = \lfloor\sqrt{N}\rfloor + 1$.
3.  Calcola $a(b) := b^2 - N$.
4.  Se $a(b)$ è un quadrato perfetto ($a^2$), i fattori sono $(b-a)$ e $(b+a)$.
5.  Altrimenti, incrementa $b$ ($b \leftarrow b+1$) e torna al passo 3.

### 4.4 Esempi Svolti
* **Esempio 1 ($N = 25.217$)**:
    * $\sqrt{N} \approx 158,79 \implies b = 159$.
    * $159^2 - 25.217 = 25.281 - 25.217 = 64 = 8^2$.
    * Fattori: $159-8=151$ e $159+8=167$.

---

## 5.0 Algoritmo 3: Metodo di Fermat via GCD (Generalizzazione)

### 5.1 Contesto e Principio Esteso
Si cerca una **congruenza di quadrati**:
$$a^2 \equiv b^2 \pmod{N}$$
con la condizione $a \not\equiv \pm b \pmod{N}$.

### 5.2 Lemma Fondamentale e Conseguenze
**Lemma**: Siano $\alpha, \beta \in \mathbb{Z}$ con $\alpha\beta \equiv 0 \pmod{N}$, ma $\alpha \not\equiv 0 \pmod{N}$ e $\beta \not\equiv 0 \pmod{N}$. Allora $1 < \gcd(\alpha, N) < N$.

Riscritta come $(a-b)(a+b) \equiv 0 \pmod{N}$, se $a \not\equiv \pm b \pmod{N}$, allora $\gcd(a \pm b, N)$ fornisce fattori non banali.

### 5.3 Guida alla Risoluzione (Algoritmo)


1.  Cercare $a, b$ tali che $a^2 \equiv b^2 \pmod{N}$ e $a \not\equiv \pm b \pmod{N}$.
2.  Un metodo pratico: cercare $b$ e $k \ge 1$ tali che $b^2 + kN = a^2$.
3.  Calcolare $d_1 = \gcd(a-b, N)$ e $d_2 = \gcd(a+b, N)$.

---

## 6.0 Equivalenza tra Fattorizzazione e Ricerca di Congruenze di Quadrati
Il problema di trovare una fattorizzazione non banale $N=xy$ è **computazionalmente equivalente** al problema di trovare $a, b$ tali che $a^2 \equiv b^2 \pmod{N}$ e $a \not\equiv \pm b \pmod{N}$.

---

## 7.0 Avvertenza Crittografica Finale
**NOTA IMPORTANTE**: Per garantire la sicurezza in crittografia, è fondamentale **NON** utilizzare numeri primi $p$ tali che $p-1$ sia un prodotto di numeri primi piccoli. Tali numeri primi, il cui predecessore ($p-1$) è **'liscio' (smooth)**, rendono il problema del logaritmo discreto e la fattorizzazione significativamente più facili da risolvere.