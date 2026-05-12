![[unnamed.png]]
### 1. Condizione di Esistenza

Per il Teorema Cinese del Resto (o le sue estensioni per moduli non coprimi), un sistema di due congruenze:

$$x \equiv a \pmod{m_1}$$
$$x \equiv b \pmod{m_2}$$
ammette soluzione se e solo se:

$$a \equiv b \pmod{\text{gcd}(m_1, m_2)}$$

dove $\text{gcd}(m_1, m_2)$ è il massimo comun divisore tra $m_1$ e $m_2$.

Nel tuo caso abbiamo:

- $a = 4$, $m_1 = 6$
- $b = 3$, $m_2 = 9$

Calcoliamo il massimo comun divisore:

$$\text{gcd}(6, 9) = 3$$

Verifichiamo la condizione di esistenza:

$$4 \equiv 3 \pmod{3}$$

Questa è vera? Dobbiamo verificare se $4 - 3$ è divisibile per 3.

$$4 - 3 = 1$$

$1$ non è divisibile per $3$.

Quindi, la condizione di esistenza **non è soddisfatta**.

---
### 2. Conclusione
Poiché la condizione necessaria e sufficiente per l'esistenza di una soluzione non è soddisfatta, il sistema di congruenze lineari:

$$x \equiv 4 \pmod{6}$$

$$x \equiv 3 \pmod{9}$$

non ammette alcuna soluzione.

---

### 3. Risposta

La risposta corretta è la **a**.

- **a. No solution.** (Nessuna soluzione)

---

### Approfondimento (Perché è importante il modulo 54?)

Anche se il sistema non ha soluzioni, se ne avesse avute, il numero di soluzioni sarebbe stato conteggiato modulo $mcm(6, 9) = 18$. Tuttavia, le opzioni ti chiedono un conteggio modulo 54.

Se un sistema ha $k$ soluzioni modulo $\text{mcm}(m_1, m_2)$, avrà anche $k \cdot \frac{54}{\text{mcm}(m_1, m_2)}$ soluzioni distinte modulo 54.

- $\text{mcm}(6, 9) = 18$
    
- Il fattore moltiplicativo sarebbe $\frac{54}{18} = 3$.
    

Quindi, se il sistema avesse avuto 1 soluzione modulo 18, avrebbe avuto $1 \times 3 = 3$ soluzioni modulo 54. Questo spiega l'opzione **c**. Tuttavia, poiché il sistema non ha **nessuna soluzione** modulo 18 (e quindi modulo $mcm(6, 9)$), non ne ha nemmeno modulo 54.

---

![[Senza titolo.png]]

Trovare $x$ tale che:

1. $x \equiv 2 \pmod{3}$
2. $x \equiv 3 \pmod{5}$

### Prerequisito: Moduli Coprimi

Il Teorema Cinese del Resto (CRT) si applica nella sua forma base quando i moduli (i numeri tra parentesi) sono **coprimi**, cioè il loro Massimo Comun Divisore è 1.

- $\text{gcd}(3, 5) = 1$
- Perfetto, possiamo usarlo.

Il teorema ci garantisce due cose:

1. Esiste una soluzione.
2. La soluzione è **unica** modulo il prodotto dei moduli (cioè modulo $3 \times 5 = 15$).

Questo combacia con la nostra scoperta precedente: 8 era l'unica soluzione nell'intervallo $\{0, \dots, 14\}$.

---

### Metodo 1: La Sostituzione (Il più facile da capire)

Questo è il modo più diretto per risolvere sistemi con due equazioni.

Passo 1: Esprimi la prima equazione come un'equazione standard.

$x \equiv 2 \pmod{3}$

significa "x è un numero che è 2 più di un multiplo di 3".

Possiamo scriverlo come:

$$x = 3k + 2 \quad \text{(per un qualche intero } k\text{)}$$

Passo 2: Sostituisci questa espressione di $x$ nella seconda equazione.

La seconda equazione è $x \equiv 3 \pmod{5}$.

Sostituiamo $x$ con $(3k + 2)$:

$$(3k + 2) \equiv 3 \pmod{5}$$

Passo 3: Risolvi la nuova congruenza per $k$.

Adesso abbiamo un'equazione con solo $k$. Isoliamolo.

$$3k \equiv 3 - 2 \pmod{5}$$

$$3k \equiv 1 \pmod{5}$$

Dobbiamo trovare quel numero $k$ che, moltiplicato per 3, dà resto 1 se diviso per 5.

- $3 \times 1 = 3 \equiv 3 \pmod{5}$
    
- $3 \times 2 = 6 \equiv 1 \pmod{5}$
    
- $3 \times 3 = 9 \equiv 4 \pmod{5}$
    
    Abbiamo trovato! $k = 2$ è una soluzione.
    

(Più formalmente, stavamo cercando l'"inverso moltiplicativo" di 3 modulo 5, che è 2, e poi abbiamo moltiplicato entrambi i lati per 2: $2 \cdot 3k \equiv 2 \cdot 1 \implies 6k \equiv 2 \implies 1k \equiv 2 \pmod{5}$. Quindi $k \equiv 2 \pmod{5}$ ).

Passo 4: Sostituisci $k$ nell'equazione del Passo 1.

Sapevamo che $k=2$ era una soluzione. Per trovare la forma generale di $k$, scriviamo:

$$k = 5j + 2 \quad \text{(per un qualche intero } j\text{)}$$

Ora sostituiamo questa espressione completa di $k$ nella nostra equazione per $x$:

$$x = 3k + 2$$

$$x = 3(5j + 2) + 2$$

$$x = 15j + 6 + 2$$

$$x = 15j + 8$$

Passo 5: Conclusione.

L'equazione $x = 15j + 8$ significa, in notazione di congruenza:

$$x \equiv 8 \pmod{15}$$

Questa è la soluzione generale! Ci dice che tutte le soluzioni sono numeri che danno resto 8 se divisi per 15.

Il problema originale chiedeva "il più piccolo $x$ positivo". Questo si ottiene impostando $j=0$:

$$x = 15(0) + 8 \implies \mathbf{x = 8}$$

---

### Metodo 2: La Formula "Classica" del Teorema Cinese

Questo è il metodo da manuale, utilissimo quando hai 3 o più equazioni.

La soluzione $x$ è data dalla formula:

$$x \equiv (a_1 \cdot M_1 \cdot y_1 + a_2 \cdot M_2 \cdot y_2) \pmod{M}$$

Sembra complicato, ma non lo è. Analizziamolo:

- $a_1 = 2$, $a_2 = 3$ (i resti che vogliamo)
- $m_1 = 3$, $m_2 = 5$ (i moduli)

1. Calcola $M$ (il modulo totale):
    $M = m_1 \times m_2 = 3 \times 5 = \mathbf{15}$
2. **Calcola i $M_i$:**
    - $M_1 = M / m_1 = 15 / 3 = \mathbf{5}$
    - $M_2 = M / m_2 = 15 / 5 = \mathbf{3}$
3. Calcola gli inversi $y_i$:
    Qui sta il cuore del metodo. Dobbiamo trovare:
    - $y_1$ tale che $M_1 \cdot y_1 \equiv 1 \pmod{m_1}$
        $$5y_1 \equiv 1 \pmod{3}$$
        Siccome $5 \equiv 2 \pmod{3}$, l'equazione è $2y_1 \equiv 1 \pmod{3}$.
        Si vede che $y_1 = 2$ funziona ($2 \times 2 = 4 \equiv 1 \pmod{3}$).
        Quindi $\mathbf{y_1 = 2}$.
    - $y_2$ tale che $M_2 \cdot y_2 \equiv 1 \pmod{m_2}$
        $$3y_2 \equiv 1 \pmod{5}$$

        Si vede che $y_2 = 2$ funziona ($3 \times 2 = 6 \equiv 1 \pmod{5}$).
        Quindi $\mathbf{y_2 = 2}$.
4. Metti tutto nella formula:
$$x \equiv (a_1 \cdot M_1 \cdot y_1 + a_2 \cdot M_2 \cdot y_2) \pmod{15}$$
    $$x \equiv (2 \cdot 5 \cdot 2 + 3 \cdot 3 \cdot 2) \pmod{15}$$
    
    $$x \equiv (20 + 18) \pmod{15}$$
    
    $$x \equiv 38 \pmod{15}$$
    
5. Riduci il risultato:
    
    Quanto fa $38 \pmod{15}$?
    
    $38 = (2 \times 15) + 8$. Il resto è 8.
    
    $$x \equiv \mathbf{8} \pmod{15}$$
    

Entrambi i metodi ci danno la stessa identica soluzione. Il Metodo 1 (Sostituzione) è spesso più rapido per due equazioni, mentre il Metodo 2 (Formula) è più sistematico per tre o più equazioni.

---

![[Senza titolo 1.png]]
### Metodo 1: Ricerca Rapida (Il più veloce per numeri piccoli)

Iniziamo con l'equazione che ha il modulo più grande, $x \equiv 3 \pmod{9}$, e testiamo i numeri che la soddisfano.

1. **Elenca i numeri** che soddisfano $x \equiv 3 \pmod{9}$ (partendo dal più piccolo positivo):
    
    - $x = 3$
        
    - $x = 3 + 9 = 12$
        
    - $x = 12 + 9 = 21$
        
    - $x = 21 + 9 = 30$
        
    - ...e così via.
        
2. **Testa questi numeri** con l'altra equazione, $x \equiv 1 \pmod{4}$:
    
    - **È $x = 3$?** $\implies 3 \div 4$ dà resto 3. (No, vogliamo resto 1).
        
    - **È $x = 12$?** $\implies 12 \div 4$ dà resto 0. (No).
        
    - **È $x = 21$?** $\implies 21 \div 4 = 5$ con resto **1**. (**Sì!**).
        

Abbiamo trovato. La più piccola soluzione positiva è 21.

---

### Metodo 2: Sostituzione (Il metodo sistematico del CRT)

Questo è il metodo che abbiamo analizzato in dettaglio prima.

1. Dalla prima equazione, $x \equiv 1 \pmod{4}$, possiamo scrivere $x$ come:
    
    $$x = 4k + 1 \quad \text{(per un qualche intero } k\text{)}$$
    
2. Sostituisci questa espressione nella seconda equazione, $x \equiv 3 \pmod{9}$:
    
    $$(4k + 1) \equiv 3 \pmod{9}$$
    
3. Risolvi per $k$:
    
    $$4k \equiv 3 - 1 \pmod{9}$$
    
    $$4k \equiv 2 \pmod{9}$$
    
4. **Trova l'inverso di 4 (mod 9).** Dobbiamo trovare un numero che, moltiplicato per 4, dia resto 1 (mod 9).
    
    - $4 \times 1 = 4$
        
    - $4 \times 2 = 8 \equiv -1$
        
    - ...
        
    - $4 \times 7 = 28 \equiv 1 \pmod{9}$
        
        L'inverso è $7$.
        
5. Moltiplica entrambi i lati di $4k \equiv 2 \pmod{9}$ per l'inverso ($7$):
    
    $$(7 \cdot 4)k \equiv (7 \cdot 2) \pmod{9}$$
    
    $$28k \equiv 14 \pmod{9}$$
    
    $$1k \equiv 5 \pmod{9} \quad \text{(perché } 28 \equiv 1 \text{ e } 14 \equiv 5\text{)}$$
    
    Quindi, $k \equiv 5 \pmod{9}$.
    
6. Trova $x$. Il valore più piccolo (positivo) per $k$ è $5$. Sostituiscilo nella nostra equazione del passo 1:
    
    $$x = 4k + 1$$
    
    $$x = 4(5) + 1$$
    
    $$x = 20 + 1$$
    
    $$x = 21$$
    

Entrambi i metodi confermano che la più piccola soluzione positiva modulo 36 è **21**.

---

![[Senza titolo 2.png]]
### Passo 1: Risolvi le prime due equazioni

Per prima cosa, troviamo un numero che soddisfa $x \equiv 2 \pmod{5}$ e $x \equiv 1 \pmod{7}$.

- Dalla prima equazione: $x = 5k + 2$ (per un qualche intero $k$).
    
- Sostituisci questo nella seconda equazione:
    
    $$(5k + 2) \equiv 1 \pmod{7}$$
    
- Risolvi per $k$:
    
    $$5k \equiv 1 - 2 \pmod{7}$$
    
    $$5k \equiv -1 \pmod{7}$$
    
    $$5k \equiv 6 \pmod{7}$$
    
- Per isolare $k$, dobbiamo trovare l'inverso di 5 (mod 7). Cerchiamo un numero $y$ tale che $5y \equiv 1 \pmod{7}$. Troviamo che $y=3$ funziona ($5 \times 3 = 15 \equiv 1 \pmod{7}$).
    
- Moltiplica entrambi i lati di $5k \equiv 6 \pmod{7}$ per $3$:
    
    $$(3 \cdot 5)k \equiv (3 \cdot 6) \pmod{7}$$
    
    $$15k \equiv 18 \pmod{7}$$
    
    $$1k \equiv 4 \pmod{7} \quad \text{(perché } 15 \equiv 1 \text{ e } 18 \equiv 4\text{)}$$
    
- Quindi, $k \equiv 4 \pmod{7}$. Possiamo scrivere $k = 7j + 4$.
    
- Ora sostituisci questo $k$ nella nostra equazione originale per $x$:
    
    $$x = 5(7j + 4) + 2$$
    
    $$x = 35j + 20 + 2$$
    
    $$x = 35j + 22$$
    
- **Risultato intermedio:** Qualsiasi numero che soddisfa le prime due equazioni deve essere della forma $x \equiv 22 \pmod{35}$.
    

---

### Passo 2: Combina il risultato con la terza equazione

Ora dobbiamo risolvere un sistema più semplice:

1. $x \equiv 22 \pmod{35}$
    
2. $x \equiv 3 \pmod{8}$
    

- Dalla prima equazione: $x = 35j + 22$ (per un qualche intero $j$).
    
- Sostituisci questo nella seconda equazione:
    
    $$(35j + 22) \equiv 3 \pmod{8}$$
    
- **Consiglio:** Riduci i numeri grandi (35 e 22) modulo 8 _prima_ di risolvere:
    
    - $35 \div 8 = 4$ con resto $3 \implies 35 \equiv 3 \pmod{8}$
        
    - $22 \div 8 = 2$ con resto $6 \implies 22 \equiv 6 \pmod{8}$
        
- L'equazione diventa molto più semplice:
    
    $$(3j + 6) \equiv 3 \pmod{8}$$
    
- Risolvi per $j$:
    
    $$3j \equiv 3 - 6 \pmod{8}$$
    
    $$3j \equiv -3 \pmod{8}$$
    
    $$3j \equiv 5 \pmod{8}$$
    
- Per isolare $j$, troviamo l'inverso di 3 (mod 8). Vediamo che $3 \times 3 = 9 \equiv 1 \pmod{8}$. L'inverso è 3.
    
- Moltiplica entrambi i lati di $3j \equiv 5 \pmod{8}$ per $3$:
    
    $$(3 \cdot 3)j \equiv (3 \cdot 5) \pmod{8}$$
    
    $$9j \equiv 15 \pmod{8}$$
    
    $$1j \equiv 7 \pmod{8} \quad \text{(perché } 9 \equiv 1 \text{ e } 15 \equiv 7\text{)}$$
    

---

### Passo 3: Calcola la soluzione finale

Abbiamo trovato $j \equiv 7 \pmod{8}$.

La più piccola soluzione positiva per $j$ è $j = 7$.

Sostituisci questo valore nell'equazione del Passo 2 per $x$:

$$x = 35j + 22$$

$$x = 35(7) + 22$$

$$x = 245 + 22$$

$$x = \mathbf{267}$$

**Verifica:**

- $267 \div 5 = 53$ resto **2**. (Corretto)
    
- $267 \div 7 = 38$ resto **1**. (Corretto)
    
- $267 \div 8 = 33$ resto **3**. (Corretto)
    

---

Solve x≡2[6] and x≡5[9]. Enter the smallest positive solution x (mod 18).
### Passo 1: Verificare la Condizione di Esistenza

Un sistema di congruenze:

$$x \equiv a \pmod{m_1}$$
$$x \equiv b \pmod{m_2}$$

ammette soluzione se e solo se $a \equiv b \pmod{\text{gcd}(m_1, m_2)}$.

- $a = 2$, $m_1 = 6$
    
- $b = 5$, $m_2 = 9$
    
- $\text{gcd}(6, 9) = 3$
    

Controlliamo la condizione: $2 \equiv 5 \pmod{3}$?

- Questo significa: "2 e 5 hanno lo stesso resto se divisi per 3?"
    
- $2 \div 3$ dà resto 2.
    
- $5 \div 3$ dà resto 2.
    
- Sì, la condizione è soddisfatta. Quindi, **una soluzione esiste**.
    

Il teorema ci dice anche che la soluzione è unica modulo $\text{mcm}(6, 9)$, che è $\text{mcm}(6, 9) = 18$. Questo è il motivo per cui la domanda ti chiede la soluzione (mod 18).

---

### Passo 2: Trovare la Soluzione

Esistono due modi rapidi per trovarla.

#### Metodo 1: Elencare i candidati (Il più veloce)

Inizia con l'equazione con il modulo più grande:

$$x \equiv 5 \pmod{9}$$

Questo significa che $x$ deve essere in questo elenco:

- $x = 5$
    
- $x = 5 + 9 = \mathbf{14}$
    
- $x = 14 + 9 = 23$
    
- ...e così via.
    

Ora testa questi numeri con l'altra equazione, $x \equiv 2 \pmod{6}$:

- Test $x = 5$:
    
    $5 \div 6$ dà resto 5. (Volevamo resto 2. Fallito.)
    
- Test $x = 14$:
    
    $14 \div 6 = 2$ con resto 2. (Volevamo resto 2. Successo!)
    

La più piccola soluzione positiva è **14**.

#### Metodo 2: Sostituzione Algebrica

1. Dalla seconda equazione, scrivi $x$ come:
    
    $$x = 9k + 5$$
    
2. Sostituisci questo $x$ nella prima equazione:
    
    $$(9k + 5) \equiv 2 \pmod{6}$$
    
3. Risolvi per $k$. Riduci i numeri modulo 6:
    
    - $9 \equiv 3 \pmod{6}$
        
    - $5 \equiv -1 \pmod{6}$
        
    
    L'equazione diventa:
    
    $$(3k - 1) \equiv 2 \pmod{6}$$
    
    $$3k \equiv 3 \pmod{6}$$
    
4. Questa congruenza $3k \equiv 3 \pmod{6}$ significa che $3k - 3$ deve essere un multiplo di 6.
    
    $$3k - 3 = 6j$$
    
    Dividendo tutto per 3:
    
    $$k - 1 = 2j \implies k = 2j + 1$$
    
    Questo significa che $k$ deve essere un numero dispari.
    
5. Per trovare la più piccola soluzione positiva per $x$, usiamo il più piccolo valore intero positivo per $k$, che è $k = 1$.
    
    Sostituisci $k = 1$ nella nostra equazione del passo 1:
    
    $$x = 9(1) + 5$$
    
    $$x = 14$$
    

---

![[Senza titolo 3.png]]
### Passo 1: Risolvi le equazioni 1 e 2

- **Da (1):** $x = 3k + 2$
    
- **Sostituisci in (2):** $(3k + 2) \equiv 1 \pmod{4}$
    
- Risolvi per $k$:
    
    $$3k \equiv 1 - 2 \pmod{4}$$
    
    $$3k \equiv -1 \pmod{4}$$
    
    $$3k \equiv 3 \pmod{4}$$
    
    Dividendo per 3 (che è coprimo con 4), otteniamo:
    
    $$k \equiv 1 \pmod{4}$$
    
- Trova la nuova $x$: Sostituisci $k = 4j + 1$ nell'equazione $x = 3k + 2$:
    
    $$x = 3(4j + 1) + 2$$
    
    $$x = 12j + 3 + 2$$
    
    $$x = 12j + 5$$
    
- **Risultato Intermedio A:** $x \equiv 5 \pmod{12}$
    

---

### Passo 2: Combina il Risultato A con l'equazione 3

Ora abbiamo un sistema più semplice:

- $x \equiv 5 \pmod{12}$
    
- $x \equiv 3 \pmod{5}$
    
- **Da (A):** $x = 12j + 5$
    
- **Sostituisci in (3):** $(12j + 5) \equiv 3 \pmod{5}$
    
- Riduci i numeri (mod 5) per semplificare: $12 \equiv 2 \pmod{5}$ e $5 \equiv 0 \pmod{5}$.
    
    $$(2j + 0) \equiv 3 \pmod{5}$$
    
    $$2j \equiv 3 \pmod{5}$$
    
- Per isolare $j$, moltiplica per l'inverso di 2 (mod 5), che è 3 (poiché $2 \times 3 = 6 \equiv 1 \pmod{5}$).
    
    $$(3 \cdot 2)j \equiv (3 \cdot 3) \pmod{5}$$
    
    $$1j \equiv 9 \pmod{5}$$
    
    $$j \equiv 4 \pmod{5}$$
    
- Trova la nuova $x$: Sostituisci $j = 5m + 4$ nell'equazione $x = 12j + 5$:
    
    $$x = 12(5m + 4) + 5$$
    
    $$x = 60m + 48 + 5$$
    
    $$x = 60m + 53$$
    
- **Risultato Intermedio B:** $x \equiv 53 \pmod{60}$
    

---

### Passo 3: Combina il Risultato B con l'equazione 4

Ora abbiamo l'ultimo sistema:

- $x \equiv 53 \pmod{60}$
    
- $x \equiv 5 \pmod{7}$
    
- **Da (B):** $x = 60m + 53$
    
- **Sostituisci in (4):** $(60m + 53) \equiv 5 \pmod{7}$
    
- Riduci i numeri (mod 7):
    
    - $60 \div 7 = 8$ resto 4. ($60 \equiv 4 \pmod{7}$)
        
    - $53 \div 7 = 7$ resto 4. ($53 \equiv 4 \pmod{7}$)
        
- L'equazione diventa:
    
    $$(4m + 4) \equiv 5 \pmod{7}$$
    
    $$4m \equiv 1 \pmod{7}$$
    
- Per isolare $m$, moltiplica per l'inverso di 4 (mod 7), che è 2 (poiché $4 \times 2 = 8 \equiv 1 \pmod{7}$).
    
    $$(2 \cdot 4)m \equiv (2 \cdot 1) \pmod{7}$$
    
    $$1m \equiv 2 \pmod{7}$$
    
- Trova la $x$ finale: Sostituisci $m = 7n + 2$ nell'equazione $x = 60m + 53$:
    
    $$x = 60(7n + 2) + 53$$
    
    $$x = 420n + 120 + 53$$
    
    $$x = 420n + 173$$
    

### Conclusione

La soluzione generale è $x \equiv 173 \pmod{420}$.

La più piccola soluzione positiva è 173.

**Verifica:**

- $173 \div 3 = 57$ resto **2** (OK)
    
- $173 \div 4 = 43$ resto **1** (OK)
    
- $173 \div 5 = 34$ resto **3** (OK)
    
- $173 \div 7 = 24$ resto **5** (OK)

---

![[Senza titolo 4.png]]
### 1. Cos'è la Funzione $\varphi$ (Phi) di Eulero?

La funzione $\varphi(n)$ (o _funzione totiente_) conta il numero di interi positivi minori o uguali a $n$ che sono **relativamente primi** (o coprimi) con $n$. Due numeri sono coprimi se il loro massimo comun divisore (MCD) è 1.

Per trovare la risposta corretta, dobbiamo calcolare $\varphi(24)$, $\varphi(4)$ e $\varphi(6)$.

### 2. Calcolo di $\varphi(24)$

Esistono due modi per calcolarlo:

- Metodo A: Elenco
    
    Dobbiamo trovare tutti i numeri $k$ tra 1 e 24 tali che $\text{MCD}(k, 24) = 1$. I fattori primi di 24 sono 2 e 3. Quindi, cerchiamo i numeri che non sono divisibili né per 2 né per 3.
    
    L'elenco è: {1, 5, 7, 11, 13, 17, 19, 23}.
    
    Contandoli, troviamo che ci sono 8 numeri.
    
    Quindi, $\varphi(24) = 8$.
    
- Metodo B: Formula
    
    Se la scomposizione in fattori primi di $n$ è $n = p_1^{k_1} \cdot p_2^{k_2} \cdots$, allora:
    
    $$\varphi(n) = n \left(1 - \frac{1}{p_1}\right) \left(1 - \frac{1}{p_2}\right) \cdots$$
    
    La scomposizione di 24 è $24 = 8 \times 3 = 2^3 \times 3^1$. I fattori primi sono 2 e 3.
    
    $$\varphi(24) = 24 \left(1 - \frac{1}{2}\right) \left(1 - \frac{1}{3}\right)$$
    
    $$\varphi(24) = 24 \left(\frac{1}{2}\right) \left(\frac{2}{3}\right) = 24 \left(\frac{1}{3}\right) = 8$$
    

Questo risultato ($\varphi(24) = 8$) ci dice che l'opzione **a** è falsa, e che la risposta deve essere la **b** o la **c**.

### 3. Calcolo di $\varphi(4)$ e $\varphi(6)$

- Calcolo di $\varphi(4)$:
    
    I numeri coprimi con 4 (tra 1 e 4) sono {1, 3}.
    
    Quindi, $\varphi(4) = 2$.
    
    (Questo ci dice che l'opzione d è falsa, poiché afferma $\varphi(4) = 4$).
    
- Calcolo di $\varphi(6)$:
    
    I numeri coprimi con 6 (tra 1 e 6) sono {1, 5}.
    
    Quindi, $\varphi(6) = 2$.
    

### 4. Valutazione delle Opzioni Rimanenti (b e c)

Ora abbiamo tutti i valori:

- $\varphi(24) = 8$
    
- $\varphi(4) = 2$
    
- $\varphi(6) = 2$
    

Dobbiamo verificare la seconda parte delle affermazioni:

- Calcoliamo $\varphi(4) \times \varphi(6) = 2 \times 2 = 4$.
    

Confrontiamo i due risultati:

- $\varphi(24) = 8$
    
- $\varphi(4)\varphi(6) = 4$
    

È chiaro che $8 \neq 4$, quindi **$\varphi(24) \neq \varphi(4)\varphi(6)$**.

Analizziamo le opzioni:

- **b. $\varphi(24) = 8$ but $\varphi(24) \neq \varphi(4)\varphi(6)$:** Questa affermazione è $8 = 8$ E $8 \neq 4$. Entrambe le parti sono vere. **Questa è la risposta corretta.**
    
- **c. $\varphi(24) = 8$ and $\varphi(24) = \varphi(4)\varphi(6)$:** Questa affermazione è $8 = 8$ E $8 = 4$. La seconda parte è falsa.
    

---

### 💡 Spiegazione Aggiuntiva: Perché $\varphi(24) \neq \varphi(4)\varphi(6)$?

La funzione $\varphi$ è una **funzione moltiplicativa**. Questo significa che $\varphi(m \cdot n) = \varphi(m)\varphi(n)$ se e solo se $m$ e $n$ sono **coprimi** ($\text{MCD}(m, n) = 1$).

Nel nostro caso, $m=4$ e $n=6$.

- $\text{MCD}(4, 6) = 2$.
    
    Poiché 4 e 6 non sono coprimi, la proprietà moltiplicativa non vale, ed è per questo $\varphi(24) \neq \varphi(4)\varphi(6)$.
    

Se avessimo scomposto 24 in fattori coprimi, come $24 = 3 \times 8$ (dove $\text{MCD}(3, 8) = 1$), la proprietà avrebbe funzionato:

- $\varphi(3) = 2$ (numeri coprimi: {1, 2})
    
- $\varphi(8) = 4$ (numeri coprimi: {1, 3, 5, 7})
    
- $\varphi(3) \times \varphi(8) = 2 \times 4 = 8$
    
- Questo corrisponde a $\varphi(24) = 8$.
    

---

![[Senza titolo 5.png]]
### 1. Cosa significa la domanda?

La domanda ti chiede di "mappare" un numero dal mondo "modulo 36" a un mondo "modulo 4 e modulo 9".

- Dominio (da dove partiamo): $r: \mathbb{Z}/(36)\mathbb{Z}$
    
    Questo è l'insieme dei resti quando si divide per 36 (i numeri da 0 a 35). L'elemento $(11)_{36}$ è semplicemente il numero 11 in questo insieme.
    
- Codominio (dove arriviamo): $(\mathbb{Z}/4\mathbb{Z}) \times (\mathbb{Z}/9\mathbb{Z})$
    
    Questo è l'insieme di tutte le possibili coppie $(a, b)$, dove $a$ è un resto modulo 4 e $b$ è un resto modulo 9.
    
- La "remainder map" (mappa dei resti) $r$:
    
    Questa funzione $r$ prende un numero $x$ da modulo 36 e ti dice quali resti si ottengono dividendo quello stesso numero $x$ per 4 e per 9.
    
    In formula:
    
    $$r(x) = (x \pmod{4}, x \pmod{9})$$
    

### 2. Il Calcolo

Dobbiamo calcolare $r((11)_{36})$. Questo significa che dobbiamo prendere $x = 11$ e calcolare la coppia:

$$(11 \pmod{4}, 11 \pmod{9})$$

1. **Calcola il primo componente (modulo 4):**
    
    - Quanto fa $11 \div 4$?
        
    - $11 = (4 \times 2) + 3$
        
    - Il resto è **3**.
        
    - Quindi, $11 \equiv 3 \pmod{4}$.
        
2. **Calcola il secondo componente (modulo 9):**
    
    - Quanto fa $11 \div 9$?
        
    - $11 = (9 \times 1) + 2$
        
    - Il resto è **2**.
        
    - Quindi, $11 \equiv 2 \pmod{9}$.
        

### 3. Conclusione

La coppia risultante è $(3, 2)$. Usando la notazione della domanda, questa è:

$$((3)_4, (2)_9)$$

Questo corrisponde esattamente all'opzione **a**.

---

### 💡 Collegamento al Teorema Cinese del Resto

Questa "mappa dei resti" è l'esatto meccanismo alla base del **Teorema Cinese del Resto (CRT)**. Poiché 4 e 9 sono coprimi (il loro $\text{MCD}$ è 1) e il loro prodotto è $4 \times 9 = 36$, il teorema ci garantisce che questa mappa è una _corrispondenza biunivoca_ (un isomorfismo).

Ogni numero in $\mathbb{Z}/36\mathbb{Z}$ corrisponde a _una e una sola_ coppia unica in $(\mathbb{Z}/4\mathbb{Z}) \times (\mathbb{Z}/9\mathbb{Z})$, e viceversa.

---

![[Senza titolo 6.png]]
### 1. Comprendere la Mappa

La "mappa dei resti" $r$ prende un numero dall'insieme $\{0, 1, \dots, 23\}$ e lo trasforma in una coppia di resti:

$$r(x) = (x \pmod{4}, x \pmod{6})$$

- **Dominio:** $\mathbb{Z}/(24)\mathbb{Z}$. Questo insieme ha **24** elementi (i numeri da 0 a 23).
    
- **Codominio:** $(\mathbb{Z}/4\mathbb{Z}) \times (\mathbb{Z}/6\mathbb{Z})$. Questo insieme è composto da tutte le possibili coppie di resti. Il numero totale di coppie è $4 \times 6 = \mathbf{24}$.
    

Dato che il dominio e il codominio hanno la stessa dimensione finita (24 elementi), la mappa $r$ può essere solo una delle due seguenti:

- O è **biettiva** (sia iniettiva che suriettiva).
    
- O **non è né iniettiva né suriettiva**.
    

Per trovare la risposta, dobbiamo solo testare una delle due proprietà.

---

### 2. Testare l'Iniettività (One-to-One)

Una mappa è iniettiva se input diversi producono sempre output diversi.

La domanda è: possiamo trovare due numeri diversi (mod 24), diciamo $x$ e $y$, che mappano allo stesso output?

$$r(x) = r(y) \implies (x \pmod{4}, x \pmod{6}) = (y \pmod{4}, y \pmod{6})$$

Cerchiamo un $x \neq 0 \pmod{24}$ tale che $r(x) = r(0)$.

- $r(0) = (0 \pmod{4}, 0 \pmod{6}) = \mathbf{(0, 0)}$
    

Ora cerchiamo un altro numero $x$ (diverso da 0 e 24) che dia anch'esso $(0, 0)$.

- $x \equiv 0 \pmod{4}$ (significa che $x$ è un multiplo di 4)
    
- $x \equiv 0 \pmod{6}$ (significa che $x$ è un multiplo di 6)
    

Qual è il numero più piccolo (diverso da 0) che è sia un multiplo di 4 che di 6? È il **minimo comune multiplo** (mcm).

- $\text{mcm}(4, 6) = 12$
    

Proviamo $x = 12$:

- $r(12) = (12 \pmod{4}, 12 \pmod{6}) = \mathbf{(0, 0)}$
    

Abbiamo trovato che $r(0) = (0, 0)$ e $r(12) = (0, 0)$.

Poiché due input diversi ($0$ e $12$) producono lo stesso output, la mappa non è iniettiva.

---

### 3. Conclusione

Dato che la mappa è tra due insiemi finiti della stessa dimensione (24 elementi) e abbiamo dimostrato che **non è iniettiva**, deve essere anche **non suriettiva**.

Pertanto, l'unica affermazione vera è **d. $r$ is not injective and not surjective.**

---

### 💡 Approfondimento (Perché non è suriettiva?)

Una mappa è **suriettiva** (onto) se ogni possibile output nel codominio viene "colpito" da almeno un input.

Abbiamo stabilito che $r$ non è suriettiva, il che significa che ci sono delle coppie $(a, b)$ nel codominio che non sono l'immagine di nessun $x$.

- Quali coppie non vengono colpite?
    
    Il Teorema Cinese del Resto (generalizzato) ci dice che il sistema
    
    $$x \equiv a \pmod{4}$$
    
    $$x \equiv b \pmod{6}$$
    
    ha una soluzione se e solo se $a \equiv b \pmod{\text{gcd}(4, 6)}$.
    
- $\text{gcd}(4, 6) = 2$.
    
- Quindi, una coppia $(a, b)$ può essere un output _solo se_ $a \equiv b \pmod{2}$ (cioè, $a$ e $b$ hanno la stessa parità: entrambi pari o entrambi dispari).
    

Prendiamo una coppia che **viola** questa condizione, ad esempio **(1, 0)**.

- $a = 1$ (dispari)
    
- $b = 0$ (pari)
    
    Poiché $1 \not\equiv 0 \pmod{2}$, questa coppia non può essere generata da nessun $x$. $x \equiv 1 \pmod{4}$ significa che $x$ è dispari, ma $x \equiv 0 \pmod{6}$ significa che $x$ è pari, il che è una contraddizione.
    

La coppia $(1, 0)$ è un elemento del codominio che non viene mai "colpito", quindi la mappa **non è suriettiva**.

---

![[Senza titolo 7.png]]
La risposta è **1152**.

Ecco il calcolo passo dopo passo per trovare il valore della **Funzione Totiente di Eulero**, $\varphi(3456)$.

### 1. Definizione e Formula

La funzione $\varphi(n)$ (phi di Eulero) conta il numero di interi positivi minori o uguali a $n$ che sono **coprimi** con $n$ (cioè, il loro massimo comun divisore è 1).

Il modo più efficiente per calcolarla è usare la scomposizione in fattori primi di $n$. Se $n = p_1^{k_1} \cdot p_2^{k_2} \cdots p_r^{k_r}$, la formula è:

$$\varphi(n) = n \left(1 - \frac{1}{p_1}\right) \left(1 - \frac{1}{p_2}\right) \cdots \left(1 - \frac{1}{p_r}\right)$$

### 2. Scomposizione in Fattori Primi di 3456

Per prima cosa, scomponiamo 3456 nei suoi fattori primi.

- $3456$ è divisibile per 2 (è pari).
    
- $3456 \div 2 = 1728$
    
- $1728 \div 2 = 864$
    
- $864 \div 2 = 432$
    
- $432 \div 2 = 216$
    
- $216 \div 2 = 108$
    
- $108 \div 2 = 54$
    
- $54 \div 2 = 27$
    
- $27 = 3^3$
    

Quindi, la scomposizione in fattori primi è: $3456 = 2^7 \times 3^3$.

### 3. Calcolo di $\varphi(3456)$

Ora applichiamo la formula usando i fattori primi che abbiamo trovato (2 e 3):

$$\varphi(3456) = 3456 \left(1 - \frac{1}{2}\right) \left(1 - \frac{1}{3}\right)$$

1. Calcola le parti tra parentesi:
    
    - $\left(1 - \frac{1}{2}\right) = \frac{1}{2}$
        
    - $\left(1 - \frac{1}{3}\right) = \frac{2}{3}$
        
2. Moltiplica tutto insieme:
    
    $$\varphi(3456) = 3456 \times \left(\frac{1}{2}\right) \times \left(\frac{2}{3}\right)$$
    
    $$\varphi(3456) = 3456 \times \left(\frac{2}{6}\right)$$
    
    $$\varphi(3456) = 3456 \times \left(\frac{1}{3}\right)$$
    
3. Esegui la divisione finale:
    
    $$\varphi(3456) = \frac{3456}{3} = \mathbf{1152}$$
    

---

### Metodo Alternativo (Usando la Proprietà Moltiplicativa)

Poiché $\varphi$ è una funzione moltiplicativa, $\varphi(m \cdot n) = \varphi(m) \cdot \varphi(n)$ se $m$ e $n$ sono coprimi.

Possiamo calcolare $\varphi(2^7)$ e $\varphi(3^3)$ separatamente.

La formula per una potenza di un primo è: $\varphi(p^k) = p^k - p^{k-1}$

1. Calcola $\varphi(2^7)$:
    
    $\varphi(2^7) = 2^7 - 2^6 = 128 - 64 = 64$
    
2. Calcola $\varphi(3^3)$:
    
    $\varphi(3^3) = 3^3 - 3^2 = 27 - 9 = 18$
    
3. Moltiplica i risultati:
    
    $\varphi(3456) = \varphi(2^7) \times \varphi(3^3) = 64 \times 18 = \mathbf{1152}$
    

---
