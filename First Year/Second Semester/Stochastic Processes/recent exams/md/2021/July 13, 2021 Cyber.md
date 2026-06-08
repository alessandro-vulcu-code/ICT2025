<!-- Pagina 1 -->

Stochastic Processes – AY 2020/2021
written test – July 13, 2021 – part A (90 minutes)

E1 Consider a Go-Back-N protocol over a two-state Markov channel, where the average number of consecutive good slots is 100 and the average number of consecutive bad slots is 100/9. The packet error probability is 1 for a bad slot and 0 for a good slot, respectively. The round-trip time is $m = 2$ slots, i.e., a packet that is erroneous in slot $t$ will be retransmitted in slot $t + 2$.

(a) Compute the throughput that could be obtained if packets were directly transmitted over the channel without using any protocol

(b) Compute the throughput of the Go-Back-N protocol for an error-free feedback channel

(c) Compute the throughput of the Go-Back-N protocol for a feedback channel subject to iid errors with probability 0.1.

E2 Consider a Markov chain $X_n$ with the following transition matrix (states are numbered from 0 to 2):

$$P = \begin{pmatrix}
0.3 & 0.5 & 0.2 \\
0.5 & 0.3 & 0.2 \\
0 & 0 & 1
\end{pmatrix}$$

(a) Draw the transition diagram, and find the probability distribution of $X_1, X_2$ and $X_{1000}$, given $X_0 = 0$

(b) Let $W_{ij}^{(n)} = E \left[ \sum_{k=0}^{n-1} I \{X_k = j\} \mid X_0 = i \right]$ be the average number of visits to state $j$ during the first $n$ time slots, given that the chain starts in state $i$. Compute $\lim_{n \to \infty} W_{0j}^{(n)}$ for $j = 0, 1, 2$.

(c) Compute the average duration of the transient evolution of the chain, i.e., the time index at which the chain is absorbed.

E3 Consider a network node able to handle traffic at 10 Gbps under normal conditions. The node is subject to attacks, that arrive according to a Poisson process of rate $\lambda = 1/T_0$. For each attack, the node has a probability $1 - \alpha$ of being infected, whereas with probability $\alpha$ the attack has no consequence. When a node gets infected, it automatically starts a clean-up process that lasts $T_1$ and occupies 70% of its resources, so that during this phase the node can only handle 3 Gbps. The clean-up process is successful with probability $\beta$ (in which case the node starts working normally), whereas with probability $1 - \beta$ it fails and the node needs to be restored manually by a human operator, which takes $T_2$, during which time the node does not handle any traffic. After being manually restored, the node starts working normally.

(a) By identifying an appropriate renewal cycle, compute the fraction of the time the node is not handling any traffic and the average traffic per unit time (in Gbps) handled by the node,

(b) Compute how often (e.g., how many times a day on average) a human operator’s intervention is needed.

(For all the above quantities, find mathematical expressions as a function of the parameters, and then compute their numerical values for $T_0 = 20$ minutes, $T_1 = 20$ minutes, $T_2 = 3$ hours, $\alpha = 0.98$, $\beta = 0.9$).

E4 Consider an exhibition where visitors arrive according to a Poisson process with rate $\lambda = 12$ customers per hour. Each visitor spends a time uniformly distributed between 10 and 15 minutes, and then leaves. The room in which the exhibition is shown is large enough to ensure there is never a need to block customers at the entrance due to too many people inside. The exhibition is open from 8 AM to 6 PM.

(a) Compute the probability that fewer than two visitors arrive during the first fifteen minutes.

(b) Compute the probability that at 8:15 AM there is only one visitor in the room, and the probability that at closing time (6 PM) the room is empty.

---

<!-- Pagina 2 -->

Stochastic Processes – AY 2020/2021
written test – July 13, 2021 – part B (60 minutes)

T1 For a Poisson process of rate $\lambda$, prove that the interarrival times are iid exponential with mean $1/\lambda$.

T2 State precisely and formally prove the result that establishes that in a Markov chain the period is a class property.

T3 For a renewal process, give an expression for $E[S_{N(t)+1}]$, also providing a formal proof.


Diagram:
```text
0 --0.5--> 1
0 --0.2--> 2
0 --0.3--> 0

1 --0.5--> 0
1 --0.2--> 2
1 --0.3--> 1

2 --1.0--> 2
```

State `2` absorbing; `0,1` transient [[wiki/concepts/absorbing-markov-chain]].

**(a)** With $X_0=0$:
$$
X_1=(1,0,0)P=(0.3,0.5,0.2)
$$

$$
X_2=X_1P=(0.34,0.30,0.36)
$$

Exact:
$$
X_n=\left(\frac{0.8^n+(-0.2)^n}{2},\frac{0.8^n-(-0.2)^n}{2},1-0.8^n\right)
$$

So
$$
X_{1000}\approx (0,0,1).
$$

**(b)** Transient block:
$$
Q=\begin{pmatrix}0.3&0.5\\0.5&0.3\end{pmatrix}
$$

Fundamental matrix [[wiki/concepts/fundamental-matrix]]:
$$
N=(I-Q)^{-1}
=
\begin{pmatrix}
35/12&25/12\\
25/12&35/12
\end{pmatrix}
$$

Thus:
$$
\lim_{n\to\infty}W_{00}^{(n)}=\frac{35}{12}
$$

$$
\lim_{n\to\infty}W_{01}^{(n)}=\frac{25}{12}
$$

Since state `2` is absorbing:
$$
\lim_{n\to\infty}W_{02}^{(n)}=\infty.
$$

**(c)** Mean absorption time = row sum of fundamental matrix [[wiki/theorems/mean-absorption-time]]:
$$
E_0[T]=\frac{35}{12}+\frac{25}{12}=5.
$$

So average absorption time index:  
$$
\boxed{5}
$$


Facciamo tutto con tempo in minuti, partendo da:

$$
8:00 \text{ AM}=t=0
$$

Il rate è:

$$
\lambda=12\text{ clienti/ora}=\frac{12}{60}=0.2\text{ clienti/minuto}
$$

La permanenza di un visitatore è:

$$
S\sim U[10,15]\text{ minuti}
$$

La sala è grande, quindi nessun visitatore viene bloccato: è un modello tipo [[wiki/concepts/m-g-infinity-queue|M/G/infinity Queue]].

## (a) Meno di due arrivi nei primi 15 minuti

Qui conta solo il processo di arrivo, non quanto restano dentro.

Se $N(t)$ è numero di arrivi entro tempo $t$, allora per un [[wiki/concepts/poisson-process|Poisson Process]]:

$$
N(t)\sim \text{Poisson}(\lambda t)
$$

Nei primi 15 minuti:

$$
\lambda t=0.2\cdot15=3
$$

Quindi:

$$
N(15)\sim \text{Poisson}(3)
$$

Chiedono:

$$
P(N(15)<2)=P(N(15)=0)+P(N(15)=1)
$$

Formula Poisson:

$$
P(N=k)=e^{-3}\frac{3^k}{k!}
$$

Quindi:

$$
P(N(15)=0)=e^{-3}
$$

$$
P(N(15)=1)=3e^{-3}
$$

Somma:

$$
P(N(15)<2)=e^{-3}+3e^{-3}=4e^{-3}
$$

Risultato:

$$
\boxed{4e^{-3}\approx0.199}
$$

cioè circa:

$$
\boxed{19.9\%}
$$

## (b1) Probabilità che alle 8:15 ci sia solo un visitatore

Alle 8:15 siamo a:

$$
t=15
$$

Ora non basta contare quanti sono arrivati. Serve contare quanti sono ancora dentro.

Un visitatore arrivato prima resta dentro se:

$$
\text{tempo di permanenza} > \text{età del visitatore}
$$

La formula M/G/∞ dice:

$$
X(t)\sim \text{Poisson}(m(t))
$$

dove:

$$
m(t)=\lambda\int_0^t P(S>u)\,du
$$

Qui $u$ è l’età del visitatore al tempo osservato.

Per $S\sim U[10,15]$:

- se $0\le u<10$, il visitatore è sicuramente ancora dentro;
- se $10\le u\le15$, resta dentro con probabilità decrescente;
- se $u>15$, è sicuramente uscito.

Quindi:

$$
P(S>u)=
\begin{cases}
1, & 0\le u<10,\\
\frac{15-u}{5}, & 10\le u\le15,\\
0, & u>15.
\end{cases}
$$

A $t=15$:

$$
m(15)=0.2\int_0^{15}P(S>u)\,du
$$

Spezzando integrale:

$$
\int_0^{15}P(S>u)\,du
=
\int_0^{10}1\,du+
\int_{10}^{15}\frac{15-u}{5}\,du
$$

Primo pezzo:

$$
\int_0^{10}1\,du=10
$$

Secondo pezzo:

$$
\int_{10}^{15}\frac{15-u}{5}\,du=2.5
$$

Totale:

$$
10+2.5=12.5
$$

Quindi:

$$
m(15)=0.2\cdot12.5=2.5
$$

Allora:

$$
X(15)\sim \text{Poisson}(2.5)
$$

Chiedono:

$$
P(X(15)=1)
$$

Formula:

$$
P(X(15)=1)=e^{-2.5}\frac{2.5^1}{1!}
$$

Quindi:

$$
\boxed{P(X(15)=1)=2.5e^{-2.5}\approx0.205}
$$

cioè circa:

$$
\boxed{20.5\%}
$$

## (b2) Probabilità che alle 6 PM la stanza sia vuota

Dalle 8 AM alle 6 PM passano:

$$
10\text{ ore}=600\text{ minuti}
$$

Quindi vogliamo:

$$
P(X(600)=0)
$$

A 6 PM possono essere ancora dentro solo visitatori arrivati negli ultimi 15 minuti, perché nessuno resta più di 15 minuti.

Per $t\ge15$, la media del numero di visitatori dentro è:

$$
m(t)=\lambda E[S]
$$

La media di una uniforme $U[10,15]$ è:

$$
E[S]=\frac{10+15}{2}=12.5
$$

Quindi:

$$
m(600)=0.2\cdot12.5=2.5
$$

Allora:

$$
X(600)\sim \text{Poisson}(2.5)
$$

Stanza vuota significa:

$$
X(600)=0
$$

Quindi:

$$
P(X(600)=0)=e^{-2.5}\frac{2.5^0}{0!}
$$

$$
P(X(600)=0)=e^{-2.5}
$$

Risultato:

$$
\boxed{e^{-2.5}\approx0.0821}
$$

cioè circa:

$$
\boxed{8.21\%}
$$

Riassunto:

$$
\boxed{P(\text{meno di 2 arrivi nei primi 15 min})=4e^{-3}\approx0.199}
$$

$$
\boxed{P(\text{un solo visitatore alle 8:15})=2.5e^{-2.5}\approx0.205}
$$

$$
\boxed{P(\text{stanza vuota alle 6 PM})=e^{-2.5}\approx0.0821}
$$