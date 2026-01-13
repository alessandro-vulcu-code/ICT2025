# Test di Primalità

## 1. Concetti Chiave e Definizioni
I test di primalità rappresentano uno strumento fondamentale nella crittografia moderna. La sicurezza di molti algoritmi crittografici, come RSA, si basa sulla difficoltà di fattorizzare numeri molto grandi. Per generare le chiavi di questi sistemi, è essenziale poter determinare in modo efficiente se un numero di centinaia di cifre è primo. Questa sezione introduce i concetti e le definizioni che costituiscono le fondamenta teoriche per comprendere come funzionano tali test.

- **Teorema dei Numeri Primi**: Definisce la funzione $\pi(n)$ come il numero di primi $p$ tali che $2 \le p \le n$. Il teorema descrive il comportamento asintotico di questa funzione, affermando che il valore di $\pi(n)$ può essere approssimato da $n/\log n$. In termini più semplici, ci fornisce una stima di quanti numeri primi esistono fino a un certo limite $n$.

- **Ipotesi di Riemann**: Riguarda la funzione zeta di Riemann, definita per numeri reali $s > 1$ come $\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}$. Questa funzione è profondamente legata ai numeri primi, come dimostra la sua formulazione alternativa come prodotto su tutti i numeri primi. L'ipotesi di Riemann è una congettura sugli zeri non banali della funzione quando estesa al piano complesso, affermando che si trovino tutti sulla retta critica con parte reale pari a $1/2$. Sebbene non sia dimostrata, è un'ipotesi centrale nella teoria dei numeri.
- **Test di Primalità di Fermat**: È un test probabilistico la cui forza risiede nel dimostrare che un numero $n$ è composto, piuttosto che nel provare la sua primalità. Dato un intero $n$, si sceglie un intero $a$ (chiamato "base") tale che $\gcd(a, n) = 1$. Si dice che $n$ "passa il test di Fermat" rispetto alla base $a$ se vale la seguente congruenza: $a^{n-1} \equiv 1 \pmod{n}$.

- **Testimone di Fermat (Fermat Witness)**: Un intero $a$ (con $\gcd(a, n) = 1$) è un "testimone di Fermat" per la non-primalità di $n$ se non passa il test di Fermat. In altre parole, se il calcolo di $a^{n-1} \pmod{n}$ produce un risultato diverso da $1$. La scoperta anche di un solo testimone di Fermat è una prova inconfutabile che il numero $n$ è composto.
- **Numeri di Carmichael**: Sono numeri composti $n$ che si "comportano" come numeri primi rispetto al test di Fermat. Un numero di Carmichael è un numero composto per il quale non esiste alcun testimone di Fermat. In altre parole, $n$ è un numero di Carmichael se la congruenza $a^{n-1} \equiv 1 \pmod{n}$ è vera per ogni base $a$ che sia coprima con $n$. Questi numeri rendono il test di Fermat, da solo, non completamente affidabile per provare la primalità.

La comprensione di queste definizioni è cruciale per apprezzare la potenza e i limiti dei test di primalità, i quali si fondano su solidi teoremi matematici che verranno esplorati nella prossima sezione.

## 2. Teoremi e Dimostrazioni Rilevanti
I teoremi in questo campo formalizzano le nostre intuizioni sui numeri primi e forniscono le basi matematiche su cui sono costruiti gli algoritmi di test di primalità. Questi enunciati non sono solo curiosità teoriche, ma strumenti pratici che garantiscono il funzionamento e l'efficienza dei metodi crittografici.

- **Enunciato**: $\lim_{n\to\infty} \frac{\pi(n)}{n/\log n} = 1$.
- **Corollario**: La probabilità che un numero intero scelto casualmente nell'intervallo $[1, n]$ sia primo è asintotica a $1/\log n$.
- **Enunciato (Piccolo Teorema di Fermat)**: Sia $p$ un numero primo. Allora per ogni intero $a$ tale che $\gcd(a, p) = 1$, vale la congruenza $a^{p-1} \equiv 1 \pmod{p}$.
- **Enunciato**: Dato $n \ge 2$ e un intero $a$ con $\gcd(a, n) = 1$, se $a$ è un testimone di Fermat per $n$, allora $n$ è un numero composto.
- **Enunciato**: Esistono infiniti numeri di Carmichael.

### Caso di Studio: Dimostrazione che 561 è un Numero di Carmichael
Per dimostrare che $561$ è un numero di Carmichael, dobbiamo mostrare che è un numero composto e che, per ogni intero $a$ con $\gcd(a, 561) = 1$, vale la congruenza $a^{560} \equiv 1 \pmod{561}$.
Il numero $561$ è chiaramente composto, poiché $561 = 3 \cdot 11 \cdot 17$. Ora, consideriamo un qualsiasi intero $a$ tale che $\gcd(a, 561) = 1$. Questo implica che $a$ non è divisibile per $3, 11$ o $17$.

1.  **Modulo 3**: Poiché $3$ è primo e non divide $a$, per il Piccolo Teorema di Fermat sappiamo che $a^{3-1} \equiv a^2 \equiv 1 \pmod{3}$. L'esponente che ci interessa è $560$. Poiché $560 = 2 \cdot 280$, possiamo scrivere: $a^{560} = (a^2)^{280} \equiv 1^{280} \equiv 1 \pmod{3}$.
2.  **Modulo 11**: Poiché $11$ è primo e non divide $a$, per il Piccolo Teorema di Fermat abbiamo $a^{11-1} \equiv a^{10} \equiv 1 \pmod{11}$. L'esponente $560$ è un multiplo di $10$ ($560 = 10 \cdot 56$), quindi: $a^{560} = (a^{10})^{56} \equiv 1^{56} \equiv 1 \pmod{11}$.
3.  **Modulo 17**: Analogamente, poiché $17$ è primo e non divide $a$, vale $a^{17-1} \equiv a^{16} \equiv 1 \pmod{17}$. L'esponente $560$ è un multiplo di $16$ ($560 = 16 \cdot 35$), quindi: $a^{560} = (a^{16})^{35} \equiv 1^{35} \equiv 1 \pmod{17}$.

Poiché $a^{560} - 1$ è divisibile per $3, 11$ e $17$ (che sono coprimi tra loro), esso deve essere divisibile anche per il loro prodotto $3 \cdot 11 \cdot 17 = 561$. Di conseguenza, $a^{560} \equiv 1 \pmod{561}$. Questo dimostra che $561$ passa il test di Fermat per ogni base $a$ ammissibile, ed è quindi un numero di Carmichael.
Si noti la proprietà fondamentale che rende $561$ un numero di Carmichael: per ogni suo fattore primo $p$ ($3, 11, 17$), vale la relazione $p-1 \mid n-1$ (ovvero $2 \mid 560$, $10 \mid 560$ e $16 \mid 560$). È questa "coincidenza", come sottolineato dal docente, che permette di applicare il Piccolo Teorema di Fermat per dimostrare la congruenza per ogni fattore.

## 3. Guida alla Risoluzione degli Esercizi
Questa sezione è una guida pratica per la preparazione all'esame. L'obiettivo è tradurre i concetti teorici discussi in precedenza in procedure algoritmiche chiare e replicabili, fornendo un metodo strutturato per affrontare le tipologie di esercizi più comuni relative ai test di primalità.

### Come Stimare il Numero di Primi in un Intervallo $[a, b]$
1.  Richiama la formula derivata dal Teorema dei Numeri Primi per l'intervallo $[a, b]$: $\text{Numero di primi} \approx \pi(b) - \pi(a) \approx \frac{b}{\log(b)} - \frac{a}{\log(a)}$
2.  Sostituisci i valori di $a$ e $b$ forniti dal problema nelle rispettive posizioni nella formula.
3.  Calcola il risultato numerico per ottenere la stima richiesta.

### Come Eseguire il Test di Primalità di Fermat per un Numero $n$ e una Base $a$
1.  **Verifica della precondizione**: Calcola $\gcd(a, n)$. Se il risultato è diverso da $1$, allora $n$ è sicuramente composto (avendo trovato un fattore) e $a$ non è una base valida per il test.
2.  **Calcolo della potenza**: Calcola il valore di $a^{n-1} \pmod{n}$. È fondamentale utilizzare un algoritmo efficiente come l'esponenziazione veloce (descritto di seguito) per gestire numeri grandi.
3.  **Interpretazione del risultato**:
    - Se il risultato è $\not\equiv 1 \pmod{n}$, allora hai trovato un testimone di Fermat. Puoi concludere con certezza che $n$ è un numero composto.
    - Se il risultato è $\equiv 1 \pmod{n}$, il test è inconcludente. La base $a$ non è un testimone. Il numero $n$ potrebbe essere primo, ma potrebbe anche essere un numero di Carmichael.

### Come Utilizzare l'Algoritmo di Esponenziazione Veloce (Fast Powering)
Per calcolare $a^k \pmod{n}$ in modo efficiente:

1.  Converti l'esponente $k$ (ad esempio, $n-1$) nella sua rappresentazione binaria.
2.  Esprimi l'esponente $k$ come una somma di potenze di $2$, corrispondente ai bit '1' della sua rappresentazione binaria. (Es: $208_{10} = 11010000_2 = 128 + 64 + 16 = 2^7 + 2^6 + 2^4$).
3.  Calcola le potenze successive della base $a$ tramite quadrati successivi, sempre riducendo il risultato modulo $n$ a ogni passo: $a^1, a^2=(a^1)^2, a^4=(a^2)^2, a^8=(a^4)^2, \dots$
4.  Moltiplica tra loro (sempre modulo $n$) solo le potenze di $a$ che corrispondono ai bit '1' nella rappresentazione binaria dell'esponente $k$.

## 4. Esempi Svolti (Casi di Studio)
Questa sezione mostra l'applicazione pratica delle metodologie descritte in precedenza. Ogni esempio è un'analisi dettagliata di un problema discusso durante la lezione, che illustra come passare dalla teoria alla soluzione numerica.

### Stima: Quanti Primi tra 900.000 e 1.000.000?
- **Problema**: Stimare il numero di primi presenti nell'intervallo $[900.000, 1.000.000]$.
- **Soluzione**: Applichiamo la formula di stima della Sezione 3. $\pi(1.000.000) - \pi(900.000) \approx \frac{1.000.000}{\log(1.000.000)} - \frac{900.000}{\log(900.000)}$
- **Risultato**: Il calcolo fornisce una stima di circa $6737$ numeri primi. Questo valore è un'approssimazione; il numero reale di primi in questo intervallo è $7224$.

### Test di Fermat: $n = 209$ è primo?
- **Problema**: Verificare se la base $a = 2$ è un testimone di Fermat per $n = 209$.
- **Soluzione**: Dobbiamo calcolare $2^{209-1} \pmod{209}$, ovvero $2^{208} \pmod{209}$. Utilizziamo l'algoritmo di Esponenziazione Veloce.
1.  **Esponente in binario**: $208_{10} = 11010000_2$.
2.  **Scomposizione**: $208 = 128 + 64 + 16 = 2^7 + 2^6 + 2^4$.
3.  **Quadrati successivi**: Calcoliamo le potenze di $2$ modulo $209$.

| $i$ | $2^{2^i} \pmod{209}$ |
| :--- | :--- |
| 0 | 2 |
| 1 | 4 |
| 2 | 16 |
| 3 | $16^2 = 256 \equiv 47$ |
| 4 | $47^2 = 2209 \equiv 119$ |
| 5 | $119^2 = 14161 \equiv 158$ |
| 6 | $158^2 = 24964 \equiv 93$ |
| 7 | $93^2 = 8649 \equiv 80$ |

4.  **Prodotto finale**: Moltiplichiamo i termini corrispondenti ai bit '1' dell'esponente.
    $2^{208} = 2^{128} \cdot 2^{64} \cdot 2^{16} \equiv 80 \cdot 93 \cdot 119 \equiv 7440 \cdot 119 \equiv 115 \cdot 119 \equiv 13685 \equiv \mathbf{36} \pmod{209}$

- **Conclusione**: Poiché $36 \not\equiv 1 \pmod{209}$, la base $2$ è un testimone di Fermat. Questo prova in modo definitivo che $209$ è un numero composto.

### Test di Fermat: $N = 30069476293$ è primo?
- **Problema**: Stabilire se $N = 30069476293$ è un numero primo.
- **Contesto**: Il metodo tradizionale di ricerca dei divisori (trial division) richiederebbe di testare tutti i primi fino a $\sqrt{N} \approx 173.406$, un processo estremamente lungo e inefficiente.
- **Soluzione**: Utilizziamo il test di Fermat con base $a = 2$. Calcoliamo $2^{N-1} \pmod N$. 
  $2^{N-1} \equiv 18152503626 \pmod{N}$
- **Conclusione**: Il risultato è chiaramente diverso da $1$. Pertanto, $2$ è un testimone di Fermat per $N$, e possiamo concludere che $N$ è un numero composto. Questo risultato è stato ottenuto con un calcolo di complessità $O(\log N)$, che in questo caso richiede circa $70$ passaggi, dimostrando l'enorme efficienza del test per escludere la primalità.

In sintesi, la lezione dimostra un concetto fondamentale: mentre provare in modo costruttivo la primalità di un numero può essere difficile, i test probabilistici come quello di Fermat offrono un metodo incredibilmente potente ed efficiente per dimostrare la non-primalità. Questa capacità di scartare rapidamente i numeri composti è una pietra miliare su cui si fonda la sicurezza della crittografia moderna.