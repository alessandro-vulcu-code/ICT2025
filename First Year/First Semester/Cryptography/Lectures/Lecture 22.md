# Teorema Alternativo di Fermat e Test di Miller-Rabin
## 1. Concetti Chiave e Definizioni
Prima di addentrarci nell'enunciato e nella dimostrazione del **Teorema Alternativo di Fermat**, è fondamentale padroneggiare alcuni concetti e definizioni preliminari. Questi elementi costituiscono le fondamenta su cui si basa non solo il teorema stesso, ma anche la sua applicazione pratica più importante: il **test di primalità di Miller-Rabin**. Una chiara comprensione di questi mattoni concettuali è essenziale per applicare correttamente questi potenti strumenti nel campo della crittografia.

Di seguito sono riportate le definizioni dei termini chiave che incontreremo:

* **Decomposizione di $p-1$**: Dato un numero primo dispari $p$, il numero $p-1$ è sempre pari. Possiamo quindi decomporlo in modo univoco come il prodotto di una potenza di $2$ e un numero dispari. Il processo consiste nel "dividere il numero per due finché il quoziente non è più divisibile per due". Il risultato sarà nella forma $p-1 = 2^k q$, dove $q$ è il quoziente finale dispari e $k \ge 1$ è il numero di divisioni effettuate.
* **Sequenza dei quadrati successivi**: Data la decomposizione $p-1 = 2^k q$ e un intero $a$, si definisce una sequenza di $k$ termini calcolati come segue:
    * Il primo termine è $a_0 \equiv a^q \pmod{p}$.
    * Ogni termine successivo è il quadrato del precedente, modulo $p$:
        * $a_1 \equiv a_0^2 \pmod{p}$
        * $a_2 \equiv a_1^2 \pmod{p}$
        * ...
        * $a_{k-1} \equiv a_{k-2}^2 \pmod{p}$
    * Questa sequenza è costruita in modo tale che il termine finale, $a_{k-1} \equiv a^{2^{k-1}q} \pmod{p}$, al quadrato restituisca $a_{k-1}^2 \equiv a^{2^k q} \equiv a^{p-1} \pmod p$. Per il **Piccolo Teorema di Fermat**, questo valore è congruo a $1 \pmod p$ se $\gcd(a,p)=1$.
* **Testimone di Fermat (Fermat Witness)**: Un numero $a$ è un testimone di Fermat per la non primalità di $n$ se $a^{n-1} \not\equiv 1 \pmod n$. Se questa congruenza non è soddisfatta, $n$ è certamente composto.
* **Testimone di Miller-Rabin (Miller-Rabin Witness)**: Un numero $a$ è un testimone di Miller-Rabin per la non primalità di un numero dispari $n$ se nessuna delle condizioni per superare il test è soddisfatta. In altre parole, se si verificano contemporaneamente:
    1.  $a_0 \equiv a^q \not\equiv 1 \pmod n$
    2.  **Nessun** termine della sequenza dei quadrati successivi $a_0, a_1, \dots, a_{k-1}$ è congruo a $-1 \pmod n$.
    > [!IMPORTANT]
    > Se si trova anche un solo testimone di Miller-Rabin, si può concludere con certezza che $n$ è un numero composto.

La distinzione tra questi due tipi di testimoni è cruciale e spiega perché il test di Miller-Rabin sia superiore al test di Fermat. Esistono numeri composti, detti **numeri di Carmichael** (es. $561$), che non hanno testimoni di Fermat (tranne i loro fattori), facendo fallire il test di primalità di Fermat. Il test di Miller-Rabin, invece, supera questo ostacolo: per qualsiasi numero composto dispari $n$, è garantito che almeno il **75%** delle basi $a$ possibili siano testimoni di Miller-Rabin.

---

## 2. Il Teorema Alternativo di Fermat
Il Teorema Alternativo di Fermat rappresenta un importante raffinamento del Piccolo Teorema di Fermat. Mentre il Piccolo Teorema di Fermat stabilisce una condizione necessaria per la primalità, il Teorema Alternativo fornisce una condizione più stringente che deve essere soddisfatta da ogni numero primo.

### **TEOREMA (Fermat's alternative Theorem)**
Sia $p$ un primo dispari, $p-1 = 2^k q$, con $2 \nmid q, k \ge 1$. Sia $a \in \mathbb{Z}$ con $\gcd(a,p)=1$. Allora **almeno una** delle seguenti condizioni è vera:
1.  $a_0 \equiv a^q \equiv 1 \pmod{p}$
2.  **Almeno uno** dei quadrati successivi $a_0 \equiv a^q \pmod{p}, a_1 \equiv a_0^2 \pmod{p}, \dots, a_{k-1} \equiv a_{k-2}^2 \pmod{p}$ è congruo a $-1 \pmod{p}$.

### **Osservazioni Importanti**
* Non è richiesto che l'esponente $q$ nella decomposizione di $p-1$ sia un numero primo.
* Il teorema **non si applica per $p=2$**, poiché in quel caso $p-1=1$ sarebbe dispari e non potrebbe essere scritto nella forma $2^k q$ con $k \ge 1$.
* La condizione $\gcd(a,p)=1$ (ovvero, $p$ non divide $a$) è essenziale.
* Il Teorema Alternativo di Fermat **implica** il Piccolo Teorema di Fermat. Se la condizione (i) è vera ($a^q \equiv 1 \pmod{p}$), elevando alla $2^k$ si ottiene $a^{p-1} \equiv 1 \pmod{p}$. Se la condizione (ii) è vera (es. $a_i \equiv -1 \pmod{p}$), elevando al quadrato ripetutamente si arriverà a $1 \pmod{p}$.

### **Dimostrazione del Teorema**
La dimostrazione si basa su due pilastri: il Piccolo Teorema di Fermat e la proprietà che in $\mathbb{Z}_p$ (se $p$ è primo), l'equazione $x^2 \equiv 1 \pmod{p}$ ha solo due soluzioni: $x \equiv 1$ e $x \equiv -1$.

1.  Dal Piccolo Teorema di Fermat, sappiamo che $a^{p-1} \equiv 1 \pmod{p}$.
2.  Possiamo scrivere $a^{p-1}$ come $a^{2^k q}$. Questo termine è $a_{k-1}^2 \equiv 1 \pmod{p}$.
3.  Quindi, $a_{k-1}$ deve essere congruo a $1$ o $-1 \pmod{p}$.
    * **Caso A**: Se $a_{k-1} \equiv -1 \pmod{p}$, la condizione (ii) è soddisfatta.
    * **Caso B**: Se $a_{k-1} \equiv 1 \pmod{p}$, consideriamo il termine precedente $a_{k-2}$. Poiché $a_{k-1} = a_{k-2}^2 \equiv 1 \pmod{p}$, allora $a_{k-2}$ deve essere $1$ o $-1 \pmod{p}$.
4.  Procedendo a ritroso: se troviamo un $a_i \equiv -1 \pmod{p}$, la condizione (ii) è vera. Se non troviamo mai $-1$, allora tutti i termini devono essere $1$, incluso $a_0 \equiv 1 \pmod{p}$, soddisfacendo la condizione (i).

---

## 3. Guida alla Risoluzione degli Esercizi

### **Algoritmo 1: Trovare $k$ e $q$ per $n-1$**
1.  Dato un numero dispari $n$, calcolare $n-1$.
2.  Dividere $n-1$ per $2$ ripetutamente finché il quoziente non diventa dispari.
3.  $k$ = numero di divisioni effettuate.
4.  $q$ = quoziente finale dispari.

### **Algoritmo 2: Verificare il Teorema Alternativo di Fermat**
*(Si applica quando $p$ è certamente primo)*
1.  Calcolare $k$ e $q$ (Algoritmo 1).
2.  Calcolare $a_0 \equiv a^q \pmod{p}$.
3.  **Se $a_0 \equiv 1 \pmod{p}$**, il teorema è verificato (Condizione i).
4.  **Se $a_0 \not\equiv 1 \pmod{p}$**, calcolare $a_1, a_2, \dots, a_{k-1}$ finché uno di essi non è congruo a $-1 \pmod{p}$ (Condizione ii).

### **Algoritmo 3: Eseguire il Test di Miller-Rabin**
*(Test di primalità per $n$)*
1.  Calcolare $k$ e $q$ (Algoritmo 1).
2.  Calcolare $a_0 \equiv a^q \pmod{n}$.
3.  **Verifica**:
    * Se $a_0 \equiv 1 \pmod{n}$ oppure $a_0 \equiv -1 \pmod{n}$, il test è **superato** ($a$ non è un testimone).
    * Altrimenti, per $i = 1 \dots k-1$:
        * Calcolare $a_i \equiv a_{i-1}^2 \pmod{n}$.
        * Se $a_i \equiv -1 \pmod{n}$, il test è **superato**.
    * Se il ciclo finisce senza mai trovare $-1$, il test è **fallito**: $a$ è un **testimone di Miller-Rabin** e $n$ è **composto**.

---

## 4. Esempi Svolti (Casi Studio)

* **Esempio 1 ($p = 37, a = 5$)**:
    * $p-1 = 36 = 2^2 \cdot 9 \implies k=2, q=9$.
    * $a_0 \equiv 5^9 \equiv 6 \pmod{37}$.
    * $a_1 \equiv 6^2 \equiv 36 \equiv -1 \pmod{37} \implies$ **Condizione (ii) soddisfatta**.

* **Esempio 3 ($p = 13, a = 9$)**:
    * $p-1 = 12 = 2^2 \cdot 3 \implies k=2, q=3$.
    * $a_0 \equiv 9^3 \equiv 729 \equiv 1 \pmod{13} \implies$ **Condizione (i) soddisfatta**.

* **Esempio di Test di Miller-Rabin ($n = 91, a = 3$)**:
    * $n-1 = 90 = 2^1 \cdot 45 \implies k=1, q=45$.
    * $a_0 \equiv 3^{45} \equiv 27 \pmod{91}$.
    * $27 \not\equiv 1$ e $27 \not\equiv -1 \pmod{91}$.
    * Nessun altro termine da calcolare ($k=1$).
    * **Conclusione**: $a=3$ è un testimone, $91$ è **composto**.

---
**Conclusione**: Il Teorema Alternativo di Fermat è il fondamento del Test di Miller-Rabin, lo standard de facto per la sicurezza di protocolli come **RSA**.