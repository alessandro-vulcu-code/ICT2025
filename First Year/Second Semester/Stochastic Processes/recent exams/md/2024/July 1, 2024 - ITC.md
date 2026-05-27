<!-- Pagina 1 -->

E1 Consider two independent Poisson processes $X_1(t)$ e $X_2(t)$, where $X_i(t)$ is the number of arrivals for process $i$ during $[0, t]$. The average number of arrivals per unit time of the two processes is $\lambda_1 = 0.5$ and $\lambda_2 = 1$, respectively.

(a) Compute $P[X_1(2) = 1|X_1(3) = 2]$ and $P[X_1(3) = 2|X_1(2) = 1]$

(b) Compute $P[X_2(1) = 1|X_1(2) + X_2(2) = 3]$ and $P[X_1(2) + X_2(2) = 3|X_2(1) = 1]$

E2 Consider a two-state Markov channel, where the channel transition probability from the good state to itself is 0.95 and the average number of consecutive bad slots is 5. The packet error probability is 1 for a bad slot and 0 for a good slot, respectively. The round-trip time is $m = 2$ slots, i.e., a packet that is erroneous in slot $t$ is retransmitted in slot $t + 2$ (if a retransmission protocol is used).

(a) Compute the throughput that could be obtained if packets were directly transmitted over the channel without using any protocol

(b) compute the throughput of a Go-Back-N protocol that transmits packets over the Markov channel described above, in the presence of an error-free feedback channel

(c) compute the throughput of a Go-Back-N protocol that transmits packets over the Markov channel described above, with a feedback channel subject to iid errors with probability $\delta = 0.1$.

E3 Consider a Markov chain with the following transition matrix (states are numbered from 0 to 4):

$$P = \begin{pmatrix}
0 & 0 & 1 & 0 & 0 \\
0 & 0.6 & 0 & 0.4 & 0 \\
1 & 0 & 0 & 0 & 0 \\
0 & 0.2 & 0 & 0.8 & 0 \\
0 & 0 & 0.2 & 0.1 & 0.7
\end{pmatrix}$$

(a) Draw the transition diagram, identify the classes, classify the states, and compute the probabilities of absorption in all recurrent classes starting from each transient state

(b) compute $\lim_{n \to \infty} P^n$ and $\lim_{n \to \infty} P^k$

(c) compute the average recurrence time for all states, and the average first passage time from any state to state 1.

E4 Consider a network node able to handle traffic at 10 Gbps under normal conditions. The node is subject to attacks, that arrive according to a Poisson process of rate $\lambda = 1/T_1$. For each attack, the node has a probability $\alpha$ of being infected, whereas with probability $1 - \alpha$ the attack has no consequence. When a node gets infected, it automatically starts a clean-up process that lasts $T_2$ and occupies 50% of its resources, so that during this phase the node can only handle 5 Gbps. The clean-up process is successful with probability $1 - \beta$ (in which case the node starts working normally), whereas with probability $\beta$ it fails and the node needs to be restored manually by a human operator, which takes $T_3$, during which time the node does not handle any traffic. After being manually restored, the node starts working normally.

(a) By identifying an appropriate renewal cycle, compute the fraction of the time the node is not handling any traffic and the average traffic per unit time (in Gbps) handled by the node.

(b) Compute how often (e.g., how many times a day on average) a human operator’s intervention is needed.

(For all the above quantities, find mathematical expressions as a function of the parameters, and then compute their numerical values for $T_1 = 10$ minutes, $T_2 = 10$ minutes, $T_3 = 3$ hours, $\alpha = 0.02$, $\beta = 0.1$.)

---

<!-- Pagina 2 -->

T1 Prove that if states $i$ and $j$ of a Markov chain communicate and $i$ is recurrent, then $j$ is also recurrent.

T2 For a Poisson process of rate $\lambda$, prove that the interarrival times are iid exponential with mean $1/\lambda$.

T3 For a renewal process, state precisely (also providing a formal proof) what is the value of

$$\lim_{t \to \infty} \frac{N(t)}{t}$$