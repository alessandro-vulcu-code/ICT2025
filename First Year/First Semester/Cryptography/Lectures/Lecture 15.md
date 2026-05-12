# Report di Crittografia: Crittografia Asimmetrica e Diffie-Hellman

## 1.0 Introduzione alla Crittografia Asimmetrica

La crittografia asimmetrica (o a chiave pubblica) rappresenta un cambiamento di paradigma: invece di una singola chiave condivisa, si utilizza una **coppia di chiavi** matematicamente correlate:
- **Chiave Pubblica ($k_{pub}$)**: Distribuibile liberamente, serve per cifrare.
- **Chiave Privata ($k_{priv}$)**: Segreta, serve per decifrare.

**Analogia**: Immagina una cassetta delle lettere con una fessura. Chiunque può imbucare un messaggio (usando la posizione pubblica della cassetta), ma solo il proprietario con la chiave fisica (privata) può aprire la cassetta e leggere i messaggi.

### 1.1 Definizione Formale
Un cifrario asimmetrico è definito dalla 5-upla $(K, M, C, e, d)$:
- **M**: Spazio dei messaggi (plaintext).
- **C**: Spazio dei testi cifrati (ciphertext).
- **K**: Spazio delle chiavi, dove $K \subseteq K_{priv} \times K_{pub}$.
- **e**: Funzione di cifratura $\rightarrow e: K_{pub} \times M \to C$.
- **d**: Funzione di decifrazione $\rightarrow d: K_{priv} \times C \to M$.

**Proprietà Fondamentale**:
$$d(k_{priv}, e(k_{pub}, m)) = m$$

### 1.2 Criteri di Successo
Un cifrario asimmetrico è considerato efficace se:
1. **Cifratura facile**: È semplice calcolare $e_{kpub}(m)$.
2. **Decifratura facile**: È semplice calcolare $d_{kpriv}(c)$ per chi ha la chiave.
3. **Resistenza Ciphertext-Only**: È difficile risalire a $m$ conoscendo solo $c$ e $k_{pub}$.
4. **Resistenza Known-Plaintext**: È difficilissimo trovare la funzione di decifrazione anche conoscendo molte coppie $(m_i, c_i)$.

Principali algoritmi: **RSA, Elgamal, ECC (Elliptic Curve), NTRU**.

---

## 2.0 Il Problema del Logaritmo Discreto (DLP)

La sicurezza di questi sistemi si basa su problemi matematici "difficili". Il principale è il DLP.

### 2.1 Teorema Fondamentale
**Proposizione**: Sia $p$ un numero primo, $g \in \mathbb{F}_p^*$ e $x, y \in \mathbb{Z}$.
$$g^x \equiv g^y \pmod{p} \iff x \equiv y \pmod{ord_p(g)}$$

**Dimostrazione (Sintesi)**:
Se $g^x \equiv g^y$, allora $g^{x-y} \equiv 1 \pmod{p}$. Per la definizione di ordine, l'esponente $x-y$ deve essere un multiplo dell'ordine di $g$. Quindi $x - y = q \cdot ord_p(g)$, che equivale a $x \equiv y \pmod{ord_p(g)}$.

### 2.2 Definizione di Logaritmo Discreto
Dati $p, g, h$, l'insieme del logaritmo discreto di $h$ in base $g$ è:
$$\log_g(h) = \{x \in \mathbb{Z}/(p-1)\mathbb{Z} : g^x \equiv h \pmod{p}\}$$

- Se $g$ è una **radice primitiva**, esiste sempre un'unica soluzione in $\mathbb{Z}/(p-1)\mathbb{Z}$.
- Se $g$ non è primitiva, l'insieme potrebbe essere vuoto o contenere più elementi.

### 2.3 Guida alla Risoluzione ed Esempi
**Esempio 1: Calcoli in $\mathbb{F}_7^*$ con $g=2$**
Le potenze di $2 \pmod{7}$ sono: $2^0=1, 2^1=2, 2^2=4, 2^3=1 \dots$
- $\log_2(3) = \emptyset$ (il 3 non compare mai).
- $\log_2(1) = \{0, 3\}$ (in $\mathbb{Z}/6\mathbb{Z}$).

**Esempio 2: Complessità**
Calcolare $\log_3(23586) \pmod{43889}$. Se $p$ è grande, l'approccio "brute force" (provare ogni esponente) richiede troppi passaggi ($p-1$ nel caso peggiore), rendendo il problema computazionalmente intrattabile.

---

## 3.0 Scambio di Chiavi Diffie-Hellman

Permette ad Alice e Bob di stabilire una chiave segreta su un canale pubblico senza che l'attaccante (Eve) possa scoprirla.



### 3.1 Algoritmo Passo-Passo
1. **Parametri Pubblici**: Si scelgono un grande primo $p$ e un generatore $g$.
2. **Segreti Privati**:
   - Alice sceglie $a$ segreto.
   - Bob sceglie $b$ segreto.
3. **Calcolo e Scambio Pubblico**:
   - Alice invia a Bob: $A = g^a \pmod{p}$.
   - Bob invia ad Alice: $B = g^b \pmod{p}$.
4. **Calcolo della Chiave Comune ($K$)**:
   - Alice calcola: $K = B^a \pmod{p} = (g^b)^a = g^{ab} \pmod{p}$.
   - Bob calcola: $K = A^b \pmod{p} = (g^a)^b = g^{ab} \pmod{p}$.

**Perché è sicuro?** Eve conosce $p, g, A, B$. Per trovare $K$, dovrebbe calcolare $a$ o $b$, risolvendo quindi il Problema del Logaritmo Discreto, che è impossibile in tempi ragionevoli per numeri grandi.

### 3.2 Esempio Svolto
**Dati**: $p=11, g=6$.
- Alice sceglie $a=3 \rightarrow A = 6^3 = 216 \equiv 7 \pmod{11}$.
- Bob sceglie $b=5 \rightarrow B = 6^5 = 7776 \equiv 10 \pmod{11}$.
- **Chiave Comune**:
  - Alice: $10^3 = 1000 \equiv 10 \pmod{11}$.
  - Bob: $7^5 = 16807 \equiv 10 \pmod{11}$.
- La chiave segreta condivisa è **10**.