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