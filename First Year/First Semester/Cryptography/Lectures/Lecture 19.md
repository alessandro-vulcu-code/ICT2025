# Il Crittosistema a Chiave Pubblica di ElGamal

## 1. Contesto e Concetti Fondamentali
Il crittosistema ElGamal, formulato da **Taher Elgamal** nel 1984-1985, rappresenta una pietra miliare nella crittografia a chiave asimmetrica. Sviluppato circa sette anni dopo il celebre algoritmo RSA, ElGamal si distingue per essere strettamente correlato allo **scambio di chiavi Diffie-Hellman**, estendendone i principi per creare un sistema completo di cifratura e decifratura. 

La sua importanza strategica risiede nel fondare la propria sicurezza sulla difficoltà computazionale di un problema matematico ben definito: il **problema del logaritmo discreto**. 

### Concetti Chiave
- **Crittografia a Chiave Pubblica (Asimmetrica)**: Paradigma che utilizza una coppia di chiavi matematicamente correlate: una **chiave pubblica** ($k_{pub}$) e una **chiave privata** ($k_{priv}$). La chiave pubblica può essere distribuita liberamente per cifrare, mentre la privata deve rimanere segreta per decifrare.
- **Problema del Logaritmo Discreto (DLP)**: Pilastro della sicurezza di ElGamal. Data l'equazione di congruenza $g^x \equiv h \pmod{p}$, dove $p$ è un numero primo, $g$ è il generatore e $h$ è il risultato noto, è computazionalmente difficile trovare l'esponente segreto $x$.



---

## 2. L'Algoritmo di ElGamal: Funzionamento Dettagliato
L'algoritmo si articola in tre fasi sequenziali: **Setup**, **Encryption** e **Decryption**.

### 2.1 Fase di Setup (Generazione delle Chiavi)
Responsabilità di Alice (la destinataria):
1. Alice sceglie un numero primo $p$ di grandi dimensioni e un generatore $g$ del gruppo moltiplicativo $\mathbb{F}_p^*$.
2. Sceglie un intero segreto $a$ tale che $1 < a < p-1$.
3. Calcola $A \equiv g^a \pmod{p}$.
4. **Parametri PUBBLICI**: $(p, g, A)$.
5. **Chiave PRIVATA**: $a$.

### 2.2 Fase di Cifratura (Compito di Bob)
Bob vuole inviare un messaggio $m$ ad Alice:
1. Rappresenta il messaggio come intero $m$ ($1 < m < p$).
2. Sceglie un intero casuale $k$ (**nonce**), tale che $1 < k < p-1$. Questo valore deve essere usato una sola volta.
3. Calcola la coppia di valori $(c_1, c_2)$ che costituisce il testo cifrato:
   - $c_1 \equiv g^k \pmod{p}$
   - $c_2 \equiv m \cdot A^k \pmod{p}$
4. Invia $(c_1, c_2)$ ad Alice.

### 2.3 Fase di Decifratura (Compito di Alice)
Alice riceve $(c_1, c_2)$ e usa la sua chiave privata $a$:
1. Calcola l'inverso di $c_1^a \pmod{p}$.
2. Recupera il messaggio: $m \equiv (c_1^a)^{-1} \cdot c_2 \pmod{p}$.

### 2.4 Prova di Correttezza
Perché la decifratura funziona?
$$(c_1^a)^{-1} \cdot c_2 \equiv ((g^k)^a)^{-1} \cdot (m \cdot A^k) \pmod{p}$$
Dato che $A = g^a$, allora $(g^k)^a = (g^a)^k = A^k$. Sostituendo:
$$(A^k)^{-1} \cdot m \cdot A^k \equiv m \cdot (A^k)^{-1} \cdot A^k \equiv m \cdot 1 \equiv m \pmod{p}$$

---

## 3. Guida alla Risoluzione degli Esercizi e Tecniche di Attacco

### 3.1 Procedura di Cifratura (Bob)
- **Dati**: $(p, g, A)$.
- **Step**: Scegli $k$ casuale, calcola $c_1 = g^k$ e $c_2 = m \cdot A^k$.

### 3.2 Procedura di Decifratura (Alice)
- **Metodo Efficiente (un passo)**:
  Per calcolare l'inverso della maschera $(c_1^a)^{-1}$, si può usare il Piccolo Teorema di Fermat:
  $$(c_1^a)^{-1} \equiv c_1^{p-1-a} \pmod{p}$$
- **Step finale**: $m \equiv c_1^{p-1-a} \cdot c_2 \pmod{p}$.

### 3.3 Analisi della Sicurezza e Tecniche di Attacco (Eve)
1. **Attacco DLP**: Eve tenta di ricavare $a$ da $A = g^a$ o $k$ da $c_1 = g^k$. Se risolve il logaritmo discreto, il sistema è rotto.
2. **Attacco a Testo Noto (Riutilizzo di $k$)**: Se Bob usa lo stesso $k$ per due messaggi $m$ e $m'$, conoscendo $m$ Eve può trovare $m'$:
   $$m' \equiv c_2' \cdot c_2^{-1} \cdot m \pmod{p}$$

---

## 4. Esempi Svolti e Casi di Studio

### 4.1 Caso di Studio 1 (Esempio Numerico)
- **Setup**: $p = 467, g = 2$. Alice sceglie $a = 153$.
- **Chiave Pubblica**: $A = 2^{153} \equiv 224 \pmod{467}$.
- **Cifratura**: $m = 331, k = 197$.
  - $c_1 = 2^{197} \equiv 87 \pmod{467}$
  - $c_2 = 331 \cdot 224^{197} \equiv 57 \pmod{467}$
- **Decifratura**: Alice calcola $87^{467-1-153} = 87^{313} \equiv 14 \pmod{467}$.
- **Recupero**: $14 \cdot 57 = 798 \equiv 331 \pmod{467}$.

### 4.2 Caso di Studio 2 (Vulnerabilità del Nonce $k$)
**Scenario**: $p = 4127, g = 5, A = 1345$.
- Bob invia $m = 1234$ con un certo $k$ ottenendo $(c_1, c_2) = (1518, 540)$.
- Bob invia $m'$ sconosciuto con lo **stesso** $k$ ottenendo $(c_1, c_2') = (1518, 840)$.

**Attacco di Eve**:
1. Calcola l'inverso di $c_2$: $540^{-1} \pmod{4127}$.
2. Tramite Algoritmo di Euclide Esteso: $540^{-1} \equiv 2117 \pmod{4127}$.
3. Applica la formula: $m' \equiv 840 \cdot 2117 \cdot 1234 \pmod{4127}$.
4. Risultato: $m' = 854$.

> [!WARNING]
> **Regola d'oro**: Non riutilizzare mai il parametro casuale $k$.