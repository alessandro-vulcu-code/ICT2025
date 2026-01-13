# Report di Crittografia: Cifrari Simmetrici ed Encoding

## 1.0 Concetti Fondamentali dei Cifrari Simmetrici

La crittografia simmetrica è un pilastro della sicurezza informatica moderna. La sua caratteristica distintiva è l'uso di una **singola chiave segreta condivisa** sia per la cifratura del testo in chiaro (plaintext) che per la decifratura del testo cifrato (ciphertext). La sicurezza del sistema dipende interamente dalla riservatezza di questa chiave.

Formalmente, un cifrario simmetrico è definito come una 5-upla composta da:

- **K**: Lo spazio di tutte le chiavi possibili.
- **M**: Lo spazio di tutti i messaggi possibili (plaintexts).
- **C**: Lo spazio di tutti i crittogrammi possibili (ciphertexts).
- **e**: La funzione di cifratura, $e: K \times M \rightarrow C$.
- **d**: La funzione di decifratura, $d: K \times C \rightarrow M$.

### Proprietà Fondamentale
La decifratura deve essere l'inverso della cifratura. Per ogni chiave $k \in K$ e ogni messaggio $m \in M$:
$$d(k, e(k, m)) = m \quad \text{o, in forma contratta,} \quad d_k(e_k(m)) = m$$

---

## 2.0 Principi di Sicurezza e Caratteristiche

### Il Principio di Kerckhoffs
Formulato nel XIX secolo, questo principio stabilisce che la sicurezza di un sistema crittografico deve risiedere esclusivamente nella **segretezza della chiave**, e non nella segretezza dell'algoritmo. Questo approccio è strategico perché è più pratico proteggere o cambiare una chiave corta che ridisegnare un intero algoritmo se compromesso.

### Requisiti di un Cifrario "Successful" (Efficace)
Un cifrario simmetrico è considerato efficace se soddisfa quattro condizioni basate sulla complessità computazionale:
1. **Efficienza in Cifratura**: $\forall k, m$ deve essere "facile" calcolare $e_k(m)$.
2. **Efficienza in Decifratura**: $\forall k, c$ deve essere "facile" calcolare $d_k(c)$.
3. **Resistenza al Ciphertext-Only Attack**: Senza conoscere $k$, deve essere "molto difficile" ottenere $m$ da $c$.
4. **Resistenza al Known-Plaintext Attack (KPA)**: Anche conoscendo diverse coppie $(m_1, c_1), ..., (m_n, c_n)$, deve essere "molto difficile" trovare $d_k(c)$ per un nuovo crittogramma.

> [!IMPORTANT]
> Per rendere impraticabile un attacco brute-force (provare ogni chiave), la dimensione della chiave deve essere di almeno 80 bit ($2^{80}$ chiavi possibili).

---

## 3.0 Il Ruolo dell'Encoding

L'**encoding** è la conversione dei dati (testo, immagini) in una rappresentazione numerica. È un processo pubblico, standardizzato e reversibile che non richiede chiavi segrete.

### Esempio: ASCII
Il sistema ASCII usa 1 byte (8 bit) per carattere, permettendo 256 combinazioni.
- **Esempio di Encoding per "Bed bug."**:
    - **B** $\rightarrow 66 \rightarrow$ `01000010`
    - **e** $\rightarrow 101 \rightarrow$ `01100101`
    - **d** $\rightarrow 100 \rightarrow$ `01100100`
    - **(spazio)** $\rightarrow 32 \rightarrow$ `00100000`
    - **b** $\rightarrow 98 \rightarrow$ `01100010`
    - **u** $\rightarrow 117 \rightarrow$ `01110101`
    - **g** $\rightarrow 103 \rightarrow$ `01100111`
    - **.** $\rightarrow 46 \rightarrow$ `00101110`

---

## 4.0 Analisi degli Algoritmi e Guida agli Esercizi



[Image of a symmetric key encryption diagram]


### 4.1 Cifrario di Cesare (Somma Modulo p)
Generalizzazione del metodo di Giulio Cesare, basato sull'addizione modulare.
- **Spazi**: $K = M = C = \mathbb{Z}/p\mathbb{Z}$.
- **Cifratura**: $e_k(m) = m + k \pmod{p}$.
- **Decifratura**: $d_k(c) = c - k \pmod{p}$.

**Guida all'Attacco (KPA)**: 
Se conosci una coppia $(m_i, c_i)$, trovi la chiave risolvendo: $k = c_i - m_i \pmod{p}$.

---

### 4.2 Cifrario Moltiplicativo
- **Cifratura**: $e_k(m) = m \cdot k \pmod{p}$.
- **Decifratura**: $d_k(c) = m \cdot k^{-1} \pmod{p}$.
- **Vincolo**: La chiave $k$ deve essere invertibile modulo $p$ ($gcd(k, p) = 1$).

**Guida all'Esercizio (Attacco GCD in $\mathbb{N}$)**:
Se la cifratura avviene sui numeri naturali senza modulo ($c = k \cdot m$), la chiave $k$ è un divisore comune.
1. Intercetta più crittogrammi $c_1, c_2, ...$.
2. Calcola $GCD(c_1, c_2, ...)$.
3. Il risultato rivelerà probabilmente la chiave $k$ o un suo multiplo.

---

### 4.3 Cifrario Affine
Combina i due metodi precedenti. Chiave $k = (k_1, k_2)$.
- **Cifratura**: $e_k(m) = k_1 \cdot m + k_2 \pmod{p}$.
- **Decifratura**: $d_k(c) = k_1^{-1} \cdot (c - k_2) \pmod{p}$.

**Esercizio tipo**: "Cifra 'sparky' con $p=26$ e $k=(3, 5)$".
1. Converti lettere in numeri (A=0, S=18, ...).
2. Applica $3m + 5 \pmod{26}$.
3. Riconverti in lettere.

---

### 4.4 Cifrario XOR (Stream Cipher)
Opera bit-a-bit su stringhe binarie usando l'operazione di OR esclusivo ($\oplus$).
- **Cifratura/Decifratura**: $c = m \oplus k$ e $m = c \oplus k$.
- **Proprietà**: Lo XOR è l'inverso di se stesso. La funzione di cifratura e decifratura sono identiche.

**Esercizio tipo**: "Dati $c = 100101$ e $m = 001101$, trova $k$".
- Soluzione: $k = c \oplus m = 101000$.

---

### 4.5 Cifrario di Hill (Block Cipher)
Primo cifrario a usare l'algebra lineare e le matrici.
- **Cifratura**: $\vec{c} = K \cdot \vec{m} \pmod{p}$
- **Decifratura**: $\vec{m} = K^{-1} \cdot \vec{c} \pmod{p}$



**Guida allo svolgimento (Decifratura)**:
1. Dividi il testo in blocchi (vettori).
2. Calcola il determinante della matrice $K$.
3. Trova l'inverso del determinante modulo $p$ (usando Euclide Esteso).
4. Calcola la matrice inversa $K^{-1} \pmod{p}$.
5. Moltiplica $K^{-1}$ per ogni vettore $\vec{c}$.