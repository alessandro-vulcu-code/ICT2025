# Report di Crittografia: Complessità Computazionale e Babystep-Giantstep

## 1.0 Introduzione alla Complessità Computazionale

In crittografia, la sicurezza si basa sulla distinzione tra problemi **"facili"** (risolvibili rapidamente) e problemi **"difficili"** (intrattabili in tempi ragionevoli). Un sistema è sicuro se la cifratura è facile per l'utente legittimo, ma la decifrazione è difficile per un attaccante.

### 1.1 Notazione Big O ($O$)
Descrive come cresce il numero di operazioni al crescere dell'input ($n$).
- **Definizione**: $a_n = O(b_n)$ se esiste una costante $K$ tale che $|a_n| \le K|b_n|$ per ogni $n$ sufficientemente grande.
- **Esempi**:
    - $\log n = O(n)$ (Crescita lenta)
    - $n \log n = O(n^2)$ (Crescita moderata)
    - $n^4 = O(2^n)$ (Il polinomio è sempre più lento dell'esponenziale)

### 1.2 Polinomiale vs Esponenziale
La dimensione dell'input è misurata in **bit ($B$)**, dove $B \approx \log_2 n$.

| Classe | Complessità (Valore $n$) | Complessità (Bit $B$) | Classificazione |
| :--- | :--- | :--- | :--- |
| **Polinomiale** | $O((\log n)^A)$ | $O(B^A)$ | **Facile/Veloce** |
| **Esponenziale** | $O(n^A)$ | $O(2^B)$ | **Difficile/Lento** |

---

## 2.0 Classificazione degli Algoritmi

### 2.1 Algoritmi Veloci (Polinomiali)
Questi algoritmi sono efficienti e utilizzati per le operazioni quotidiane:
- **Conversione in base 2**: $O(\log m)$.
- **Operazione di Modulo**: $O(1)$.
- **Fast Powering (Esponenziazione Veloce)**: Riduce il calcolo di $g^n \pmod p$ da $n$ prodotti a $O(\log n)$ prodotti.
- **Algoritmo di Euclide (MCD)**: $O(\log n)$.
- **Inverso Modulare**: Tramite Euclide Esteso, $O(\log N)$.
- **Teorema Cinese del Resto (CRT)**: Risoluzione di sistemi di congruenze in tempo polinomiale.

### 2.2 Algoritmi Lenti (Esponenziali)
- **Forza Bruta per il Logaritmo Discreto (DLP)**: Richiede $O(N)$ passaggi (dove $N$ è l'ordine del gruppo). Se $N \approx 2^B$, l'attacco è esponenziale rispetto ai bit.
- **Fattorizzazione di grandi numeri**: Problema alla base di RSA.

---

## 3.0 Il Problema del Logaritmo Discreto (DLP)

Dati $g, h \in \mathbb{F}_p^*$, trovare $x$ tale che:
$$g^x \equiv h \pmod p$$

L'esponenziazione è facile, ma il logaritmo è difficile. 
**Forza Bruta**: Testare $g^1, g^2, g^3, \dots, g^N$ fino a trovare $h$. 
- **Complessità**: $O(N)$. Se $p$ è un numero di 1000 bit, $2^{1000}$ operazioni sono impossibili per qualsiasi computer attuale.

---

## 4.0 Algoritmo Babystep-Giantstep (BSGS)

Ideato da Daniel Shanks, è un algoritmo di tipo "meet-in-the-middle" che riduce drasticamente i tempi di calcolo.

### 4.1 Guida Passo-Passo
1. **Calcolo di $n$**: Scegli $n = 1 + \lfloor \sqrt{N} \rfloor$, dove $N$ è l'ordine di $g$.
2. **Lista 1 (Babysteps)**: Calcola e memorizza $g^i \pmod p$ per $i = 0, 1, \dots, n-1$.
3. **Lista 2 (Giantsteps)**: 
    - Calcola $u = g^{-n} \pmod p$.
    - Calcola $h \cdot u^j \pmod p$ per $j = 0, 1, \dots, n-1$.
4. **Collisione**: Cerca un valore comune tra le due liste. Se $g^i = h \cdot u^j$, allora:
$$x = i + jn \pmod N$$

**Complessità**: $O(\sqrt{N} \log N)$. È molto più veloce della forza bruta ($O(N)$), ma richiede memoria $O(\sqrt{N})$ per la prima lista.

### 4.2 Esempio Svolto: $3^x \equiv 11 \pmod{31}$
- **Dati**: $g=3, h=11, p=31, N=30$.
- **Step 1**: $n = 1 + \lfloor \sqrt{30} \rfloor = 6$.
- **Step 2 (Babysteps)**:
    - $3^0=1, 3^1=3, 3^2=9, 3^3=27, 3^4=19, 3^5=26$.
- **Step 3 (Giantsteps)**:
    - Calcoliamo $u = 3^{-6} \equiv 2 \pmod{31}$.
    - $j=0: 11 \cdot 2^0 = 11$
    - $j=1: 11 \cdot 2^1 = 22$
    - $j=2: 11 \cdot 2^2 = 44 \equiv 13$
    - $j=3: 11 \cdot 2^3 = 88 \equiv 26$ $\rightarrow$ **Collisione!**
- **Step 4 (Soluzione)**:
    - Abbiamo $i=5$ (dalla prima lista) e $j=3$.
    - $x = 5 + 3(6) = 5 + 18 = 23$.
- **Verifica**: $3^{23} \equiv 11 \pmod{31}$.

---

## 5.0 Considerazioni Pratiche per l'Esame
- **Riusabilità**: Se la base $g$ non cambia, la Lista 1 può essere calcolata una sola volta per molti attacchi diversi.
- **Memoria**: BSGS è limitato dalla memoria. Per gruppi enormi, si usano varianti come l'algoritmo $\rho$ di Pollard.
- **Pre-condizione**: Per calcolare $u = g^{-n}$, assicurati che $g$ sia invertibile mod $p$ (sempre vero se $p$ è primo e $g \neq 0$).