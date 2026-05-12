# Report di Crittografia: Algoritmi per il Logaritmo Discreto (DLP)

## 1.0 Introduzione e Concetti Chiave

Il **Problema del Logaritmo Discreto (DLP)** consiste nel trovare l'esponente intero $x$ tale che:
$$g^x \equiv h \pmod{p}$$
dove $g$ è il generatore e $h$ un elemento del gruppo finito $\mathbb{F}_p^*$. La sicurezza di protocolli come **Diffie-Hellman** si basa sull'intrattabilità computazionale di questo problema.

### Definizioni Fondamentali
- **Ordine di un elemento ($ord_p(g)$)**: Il più piccolo intero positivo $N$ tale che $g^N \equiv 1 \pmod{p}$.
- **Complessità Computazionale**:
    - **Forza Bruta**: $O(N)$ (Esponenziale rispetto ai bit).
    - **Babystep-Giantstep (BSGS)**: $O(\sqrt{N} \log N)$.
    - **Pohlig-Hellman (PH)**: $O(\sum a_i p_i)$ (dipende dalla fattorizzazione di $N$).

---

## 2.0 L'Algoritmo Babystep-Giantstep (BSGS)

Tecnica "meet-in-the-middle" ideata da Daniel Shanks. Riduce lo spazio di ricerca da $N$ a $\sqrt{N}$ sfruttando la scomposizione dell'esponente $x = ni + j$.

### 2.1 Guida alla Risoluzione (Algoritmo)
1. **Calcolo di $n$**: $n = 1 + \lfloor\sqrt{N}\rfloor$.
2. **Lista 1 (Baby steps)**: Calcola $g^j \pmod{p}$ per $j = 0, \dots, n-1$.
3. **Lista 2 (Giant steps)**: 
    - Calcola l'inverso $u = g^{-n} \pmod{p}$.
    - Calcola $h \cdot u^i \pmod{p}$ per $i = 0, \dots, n-1$.
4. **Collisione**: Trova $i, j$ tali che $g^j \equiv h(g^{-n})^i$.
5. **Soluzione finale**: $x = ni + j \pmod{N}$.

### 2.2 Analisi della Complessità
- **Tempo**: $O(\sqrt{N} \log N)$ (grazie all'ordinamento di una lista per la ricerca rapida).
- **Memoria**: $O(\sqrt{N})$ (necessaria per memorizzare la prima lista).

---

## 3.0 L'Algoritmo di Pohlig-Hellman (PH)

Sfrutta la decomposizione dell'ordine $N$ in fattori primi: $N = p_1^{a_1} \cdot p_2^{a_2} \cdot \dots \cdot p_m^{a_m}$. Riduce un DLP grande in tanti piccoli DLP risolvibili più velocemente.



### 3.1 Guida alla Risoluzione
1. **Riduzione**: Per ogni fattore $p_i^{a_i}$, calcola:
   $$g_i = g^{N/p_i^{a_i}} \pmod{p}, \quad h_i = h^{N/p_i^{a_i}} \pmod{p}$$
2. **Risoluzione Sottoproblemi**: Trova $y_i$ tale che $g_i^{y_i} \equiv h_i \pmod{p}$.
3. **Ricostruzione (CRT)**: Risolvi il sistema di congruenze usando il Teorema Cinese del Resto:
   $$\begin{cases} x \equiv y_1 \pmod{p_1^{a_1}} \\ \dots \\ x \equiv y_m \pmod{p_m^{a_m}} \end{cases}$$

### 3.2 Esempio Svolto: $2^x \equiv 7 \pmod{13}$
- **Dati**: $p=13, g=2, h=7$. Ordine $N = 12 = 2^2 \cdot 3$.
- **Sottoproblema 1 ($2^2=4$)**:
    - $g_1 = 2^{12/4} = 2^3 \equiv 8$.
    - $h_1 = 7^{12/4} = 7^3 \equiv 5$.
    - $8^{y_1} \equiv 5 \pmod{13} \rightarrow y_1 = 3$.
- **Sottoproblema 2 ($3^1=3$)**:
    - $g_2 = 2^{12/3} = 2^4 \equiv 3$.
    - $h_2 = 7^{12/3} = 7^4 \equiv 9$.
    - $3^{y_2} \equiv 9 \pmod{13} \rightarrow y_2 = 2$.
- **CRT**:
    - $x \equiv 3 \pmod{4}$ e $x \equiv 2 \pmod{3} \implies \mathbf{x = 11}$.

---

## 4.0 Confronto e Sicurezza

| Caratteristica | Babystep-Giantstep (BSGS) | Pohlig-Hellman (PH) |
| :--- | :--- | :--- |
| **Complessità** | $O(\sqrt{N} \log N)$ | $O(\sum p_i^{a_i})$ |
| **Punto di Forza** | Universale | Velocissimo se $N$ è "friabile" (smooth) |
| **Punto Debole** | Richiede molta memoria | Inefficace se $N$ ha grandi fattori primi |

### Implicazioni per la Sicurezza
Per proteggere Diffie-Hellman dall'attacco di Pohlig-Hellman, si usano i **Safe Primes** (Primi Sicuri).
- Un primo $p$ è sicuro se $p = 2q + 1$, dove $q$ è a sua volta un numero primo grande.
- In questo caso, $N = p-1 = 2q$. Poiché $q$ è enorme, l'algoritmo PH non può ridurre il problema in pezzi piccoli, costringendo l'attaccante a usare algoritmi esponenziali come il BSGS.

> [!WARNING]
> Mai usare un numero primo $p$ tale che $p-1$ sia composto solo da piccoli fattori primi (es. $2, 3, 5, 7$), altrimenti il sistema cade in pochi millisecondi.