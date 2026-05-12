# Sintesi Informativa: Algebra Modulare, Congruenze Lineari e Applicazioni Crittografiche

## Executive Summary

Questo documento sintetizza i concetti fondamentali dell'algebra modulare, le tecniche per la risoluzione di congruenze lineari e le loro applicazioni pratiche, in particolare nello schema di condivisione dei segreti. L'analisi si basa sulla definizione di congruenza modulo `m` (`a ≡ b [m]`), che stabilisce una relazione di equivalenza sull'insieme degli interi, portando alla costruzione dell'insieme quoziente `Z/mZ`. Questa struttura algebrica è un anello commutativo con addizione e moltiplicazione.

Un concetto centrale è quello di invertibilità: un elemento `a` è invertibile in `Z/mZ` se e solo se il suo massimo comune divisore con il modulo `m` è 1 (`gcd(a,m) = 1`). L'insieme di tali elementi, denotato con `(Z/mZ)⇤`, forma un gruppo commutativo rispetto alla moltiplicazione. Nel caso speciale in cui il modulo `p` sia un numero primo, `Z/pZ` (noto anche come `Fp`) acquisisce la struttura di un campo, dove ogni elemento non nullo è invertibile.

Il documento esamina in dettaglio la risoluzione di congruenze lineari della forma `ax ≡ b[m]`. Si dimostra che una soluzione esiste se e solo se `gcd(a,m)` divide `b`. Se questa condizione è soddisfatta, esistono esattamente `d = gcd(a,m)` soluzioni distinte modulo `m`. Infine, viene presentata un'applicazione crittografica, lo schema di condivisione dei segreti di Shamir, che sfrutta i principi dell'algebra modulare per distribuire un segreto tra più persone, richiedendo la cooperazione per la sua ricostruzione.

--------------------------------------------------------------------------------

## 1. Fondamenti di Algebra Modulare

### Definizione di Congruenza

Dati gli interi `a`, `b` e un intero `m > 1`, si dice che `a` è **congruo** a `b` modulo `m`, e si scrive `a ≡ b [m]`, se `m` divide la differenza `(a-b)`. Questo è equivalente ad affermare che `a` e `b` hanno lo stesso resto quando vengono divisi per `m`.

**Esempi:**

- `6 + 9 = 15 ≡ 3 [12]`, poiché `12` divide `15 - 3 = 12`.
- `2 - 3 = -1 ≡ 11 [12]`, poiché `12` divide `-1 - 11 = -12`.
- `17 ≡ 7 [10]`.
- `19 ≠ 6 [11]`.

La relazione di congruenza modulo `m` è una **relazione di equivalenza**, in quanto soddisfa le seguenti proprietà:

- **Riflessiva:** `∀a ∈ Z, a ≡ a [m]`
- **Simmetrica:** `∀a,b ∈ Z, a ≡ b [m] ⇒ b ≡ a [m]`
- **Transitiva:** `∀a,b,c ∈ Z, a ≡ b [m]` e `b ≡ c [m] ⇒` a ≡ c [m]`

### L'Insieme Quoziente Z/mZ

Essendo una relazione di equivalenza, la congruenza partiziona l'insieme degli interi `Z` in `m` classi di equivalenza disgiunte. L'insieme di queste classi è chiamato **insieme quoziente** e viene denotato con `Z/mZ`.

`Z/mZ` contiene `m` elementi, che sono le classi di resto modulo `m`: `Z/mZ = { [0], [1], [2], ..., [m-1] }`

Per semplicità, si scrive spesso `Z/mZ = { 0, 1, 2, ..., m-1 }`.

### Operazioni in Z/mZ

Sull'insieme `Z/mZ` sono definite le operazioni di somma e prodotto, che sono compatibili con la congruenza. Dati `a₁, a₂, b₁, b₂ ∈ Z` tali che `a₁ ≡ a₂ [m]` e `b₁ ≡ b₂ [m]`, allora:

- `a₁ + b₁ ≡ a₂ + b₂ [m]`
- `a₁b₁ ≡ a₂b₂ [m]`

Questo permette di definire le operazioni direttamente sulle classi di equivalenza:

1. **Somma:** `(a) + (b) := (a + b)`
2. **Prodotto:** `(a)(b) := (ab)`

Queste operazioni sono "ben definite" perché il risultato non dipende dai rappresentanti scelti per le classi.

## 2. Strutture Algebriche in Z/mZ

### Il Gruppo Additivo e l'Anello Commutativo

La struttura `(Z/mZ, +)` è un **gruppo commutativo**. Le sue proprietà sono:

- **Commutatività:** `a + b = b + a`
- **Associatività:** `a + (b + c) = (a + b) + c`
- **Elemento neutro:** `0` è l'elemento neutro, tale che `a + 0 = 0 + a = a`.
- **Elemento inverso (opposto):** Per ogni `a`, esiste `(-a)` tale che `a + (-a) = 0`.

Considerando entrambe le operazioni, la struttura `(Z/mZ, +, ·)` è un **anello commutativo**.

### Invertibilità e il Gruppo delle Unità (Z/mZ)⇤

Un elemento `a ∈ Z/mZ` è detto **invertibile** rispetto al prodotto se esiste un elemento `a'` tale che `a · a' = 1`. Tale `a'` è unico ed è chiamato l'inverso di `a`.

**Proposizione (Caratterizzazione dell'Invertibilità):** Un elemento `a ∈ Z/mZ` è invertibile se e solo se `gcd(a, m) = 1`.

- **Dimostrazione (schizzo):** `a` è invertibile `⇔ ∃u, k ∈ Z : au = 1 + mk ⇔ ∃u, v ∈ Z : au + mv = 1` (con `v = -k`). Quest'ultima equazione, per il teorema di Bézout, ha soluzioni intere se e solo se `gcd(a,m) = 1`.

L'insieme degli elementi invertibili di `Z/mZ` è denotato con `**(Z/mZ)⇤**` ed è chiamato il **gruppo delle unità modulo m**. La struttura `((Z/mZ)⇤, ·)` è un **gruppo commutativo**.

**Esempi:**

- `(Z/5Z)⇤ = {1, 5, 7, 11}`
- `(Z/12Z)⇤ = {1, 5, 7, 11}`
- In `Z/7Z`, l'elemento `5` è invertibile. Usando l'algoritmo Euclideo, si trova che `3 · 5 = 15 ≡ 1 [7]`. Pertanto, l'inverso di `5` è `3`.
- `214` non è invertibile in `Z/1024Z` perché `gcd(214, 1024) ≠ 1`.

## 3. Campi Finiti e Proprietà Speciali

### Il Campo Fp

Quando il modulo `p` è un numero primo, la struttura `(Z/pZ, +, ·)` è un **campo**, comunemente denotato con `Fp`. Un campo è un anello commutativo in cui ogni elemento non nullo è invertibile.

Le proprietà di un campo `Fp` sono:

1. `(Fp, +)` è un gruppo commutativo.
2. `(Fp \ {0}, ·)`, ovvero `(Fp)⇤`, è un gruppo commutativo.
3. La proprietà distributiva del prodotto rispetto alla somma è valida: `a · (b + c) = a · b + a · c`.

Se `p` è primo, ogni intero `a` tale che `1 ≤ a < p` è coprimo con `p`. Di conseguenza, `(Z/pZ)⇤ = (Z/pZ) \ {0}`.

### Soluzioni di x² = 1 in Fp

**Corollario:** Se `p > 2` è un numero primo, l'equazione `x² = 1` ha esattamente due soluzioni distinte in `Fp`.

- **Dimostrazione:** L'equazione `x² ≡ 1 [p]` è equivalente a `x² - 1 ≡ 0 [p]`, che significa `p | (x² - 1)`. Fattorizzando, si ottiene `p | (x - 1)(x + 1)`. Poiché `p` è primo, deve dividere almeno uno dei due fattori: `p | (x - 1)` o `p | (x + 1)`.
    - Se `p | (x - 1)`, allora `x ≡ 1 [p]`.
    - Se `p | (x + 1)`, allora `x ≡ -1 [p]`, che è `x ≡ p - 1 [p]`. Le due soluzioni sono `x = 1` e `x = p - 1`.

## 4. Risoluzione di Congruenze Lineari

### Formulazione e Condizioni di Esistenza

Il problema generale è trovare tutte le soluzioni `x` della congruenza lineare `ax ≡ b [m]`. Questa equazione è equivalente all'equazione diofantea `ax + mv = b` per un qualche intero `v`.

**Proposizione Fondamentale:** La congruenza `ax ≡ b[m]` ammette almeno una soluzione se e solo se `d = gcd(a, m)` divide `b`.

- Se questa condizione è soddisfatta, l'equazione ha esattamente `d` soluzioni distinte in `Z/mZ`.
- Se la condizione non è soddisfatta, non esistono soluzioni.

### Metodi di Risoluzione

**Caso 1: Soluzione Unica (gcd(a,m) = 1)** Se `a` e `m` sono coprimi, `a` è invertibile in `Z/mZ`. La congruenza ha una soluzione unica data da: `x ≡ a⁻¹ · b [m]`

- **Esempio:** Risolvere `62x ≡ 5 [7]`.
    - `62 ≡ 6 [7]`, quindi l'equazione è `6x ≡ 5 [7]`.
    - `gcd(6, 7) = 1`, quindi esiste una soluzione unica.
    - L'inverso di `6` mod `7` è `6` stesso (poiché `6 · 6 = 36 ≡ 1 [7]`).
    - `x ≡ 6⁻¹ · 5 ≡ 6 · 5 ≡ 30 ≡ 2 [7]`.
- **Esempio:** Risolvere `709x = 12 [800]`.
    - `gcd(709, 800) = 1`. L'inverso di `709` mod `800` è `589`.
    - `x ≡ 709⁻¹ · 12 ≡ 589 · 12 = 7068`.
    - `7068 ≡ 668 [800]`. La soluzione è `x = 668`.

**Caso 2: Soluzioni Multiple (gcd(a,m) = d > 1)** Se `d = gcd(a,m) | b`, si può dividere l'intera congruenza per `d`: `(a/d)x ≡ (b/d) [m/d]`

Questa nuova congruenza ha una soluzione unica `x₀` modulo `m/d`, poiché `gcd(a/d, m/d) = 1`. Le `d` soluzioni dell'equazione originale in `Z/mZ` sono date da: `x = x₀ + k * (m/d)`, per `k = 0, 1, ..., d - 1`.

- **Esempio:** Risolvere `4x ≡ 6 [10]`.
    - `d = gcd(4, 10) = 2`. Poiché `2 | 6`, esistono 2 soluzioni.
    - Dividendo per 2: `2x ≡ 3 [5]`.
    - L'inverso di `2` mod `5` è `3`. `x₀ ≡ 3 · 3 ≡ 9 ≡ 4 [5]`.
    - Le soluzioni in `Z/10Z` sono `x = 4 + k·(10/2) = 4 + 5k`.
        - Per `k = 0`: `x = 4`.
        - Per `k = 1`: `x = 9`.
- **Esempio:** Risolvere `10x ≡ 15 [45]`.
    - `d = gcd(10, 45) = 5`. Poiché `5 | 15`, esistono 5 soluzioni.
    - Dividendo per 5: `2x ≡ 3 [9]`.
    - L'inverso di `2` mod `9` è `5`. `x₀ ≡ 5 · 3 ≡ 15 ≡ 6 [9]`.
    - Le soluzioni in `Z/45Z` sono `x = 6 + k·(45/5) = 6 + 9k`.
        - Per `k=0,1,2,3,4`: `x = 6, 15, 24, 33, 42`.

## 5. Applicazione: Schema di Condivisione dei Segreti di Shamir

### Il Problema

Si desidera condividere un segreto (es. una combinazione di una serratura) tra un gruppo di amici in modo tale che qualsiasi coppia di amici possa ricostruire il segreto, ma nessun singolo amico possieda informazioni sufficienti per farlo da solo.

### L'Analogia Geometrica

L'idea fondamentale si basa sul principio geometrico che **"due punti determinano una linea"**. Il segreto viene codificato come un parametro di una retta (ad esempio, l'intercetta con l'asse y), e a ogni persona viene dato un punto diverso su quella retta. Un singolo punto non rivela la retta, ma due punti sono sufficienti per determinarla univocamente e quindi rivelare il segreto.

### Esempio di Implementazione

Si supponga di voler condividere un segreto lavorando nel campo finito `Z/pZ` con `p = 941` (un numero primo).

1. **Generazione dei Punti:** Vengono generati dei punti su una retta segreta. A due amici, A e B, vengono dati i seguenti punti:
    - Amico A: `(23, 401)`
    - Amico B: `(58, 368)`
2. **Ricostruzione del Segreto:** Per ricostruire un parametro della retta (come la pendenza), A e B devono collaborare. La pendenza `m` è calcolata come `Δy / Δx` in `Z/941Z`.
3. `m = (368 - 401) · (58 - 23)⁻¹ [941]` `m = (-33) · (35)⁻¹ [941]`
4. **Calcolo dell'Inverso Modulare:** Per completare il calcolo, è necessario trovare l'inverso di `35` modulo `941`. L'algoritmo di Euclide esteso o un calcolatore possono essere usati per trovare che `35⁻¹ ≡ 242 [941]`.
5. **Calcolo finale:** `m = (-33) · 242 = -7986 [941]` `-7986 ≡ 483 [941]`

La collaborazione ha permesso di calcolare un parametro della retta segreta. Con un'informazione aggiuntiva (come un'altra coppia di punti o il segreto stesso legato all'intercetta), il segreto può essere completamente svelato. Questo esempio dimostra l'importanza pratica dei calcoli di inversi modulari in un contesto crittografico.