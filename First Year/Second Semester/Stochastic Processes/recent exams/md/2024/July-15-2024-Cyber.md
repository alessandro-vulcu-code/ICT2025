E1 Consider two independent Poisson processes $X_1(t)$ e $X_2(t)$, where $X_i(t)$ is the number of arrivals for process $i$ during $[0, t]$. The average number of arrivals per unit time of the two processes is $\lambda_1 = 0.5$ and $\lambda_2 = 1$, respectively.

(a) Compute $P[X_2(2) = 1|X_1(2) + X_2(2) = 2]$ and $P[X_1(2) + X_2(2) = 2|X_2(2) = 1]$
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

(a) Draw the transition diagram, identify the classes, classify the states, and compute the probabilities in all recurrent classes starting from each transient state

$$P = \begin{pmatrix}
0 & 0 & 1 & 0 & 0 \\
0 & 0.6 & 0 & 0.4 & 0 \\
1 & 0 & 0 & 0 & 0 \\
0 & 0.2 & 0 & 0.8 & 0 \\
0 & 0 & 0.2 & 0.1 & 0.7
\end{pmatrix}$$

(a) Draw the transition diagram, identify the classes, classify the states, and compute the probabilities of absorption in all recurrent classes starting from each transient state.

(b) compute $\lim_{n \to \infty} P^n$ and $\lim_{n \to \infty} \frac{1}{n} \sum_{k=0}^{n-1} P^k$.

(c) compute the average recurrence time for all states, and the average first passage time from any state to state 3.

E4 Consider a node that contains two identical and independent servers, each able to stream data at rate $R$. Each server is subject to attacks according to a Poisson process with rate $\lambda$, and each attack is effective with probability $\alpha$, whereas it has no consequences with probability $1 - \alpha$ (Hint: only consider the process of effective attacks). As a result of each effective attack, the server will remain inoperational (i.e., with zero streaming rate) for an exponential time with average $T$, during which any arriving attack will have no effect, and then will resume normal operations.

(a) Compute the fraction of time during which the node does not stream any data (i.e., both servers are inoperational), and the average duration of a period of time during which no data is streamed.

(b) by considering an appropriate renewal cycle, compute the average duration of the time interval during which the node is able to stream data without interruptions (i.e., there is always at least one server working).

(c) compute the average total streaming rate of the node in Gbps.

(For all the above quantities, find mathematical expressions as a function of the parameters, and then compute their numerical values for $R = 2.5$ Gbps, $\lambda = 20$ attacks/hour, $\alpha = 1/9$ and $T = 3$ minutes.)
