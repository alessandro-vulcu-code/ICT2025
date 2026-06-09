<!-- Pagina 1 -->

# July 13, 2021

## E3. Consider a network node able to handle traffic at 10 Gbps under normal conditions. The node is subject to attacks, that arrive according to a Poisson process of rate $\lambda = 1/T_0$. For each attack, the node has a probability $1-\alpha$ of being infected, where $\alpha$ is with probability $a$ the attack has no consequence. When a node gets infected, it automatically starts a clean-up process that lasts $T_2$ and occupies 70% of its resources, so that during this phase the node can only handle 3 Gbps.

The clean-up process is successful with probability $B$ (in which case the node starts working normally), whereas with probability $1-B$ fails and the node needs to be restored manually by a human operator which takes $T_2$, during which time the node does not handle any traffic. After manually restored, the node starts working normally.

### (a) By identifying an appropriate renewal cycle, compute the fraction of the time the node is not handling any traffic and the average traffic per unit time (in Gbps) handled by the node. $\lambda =$ arrival rate $T_0'$ cleaning $T_1$ manual $T_2$

$$
\lambda = \frac{\text{rate of infection}}{T_0'} = \frac{1}{\lambda} = \frac{T_0}{(1-\alpha)}
$$

Interarrival time between effective attacks.

$$
P[\text{No traffic}] = \frac{(1-B)T_2}{T_0' + T_1 + BT_2} = \frac{(1-B)T_2}{(T_0' + T_1 + (1-B)T_2)} \quad \text{using min.}
$$

$$
P[N\text{Tr}] = 0.01734
$$

$$
E[\text{traffic}] = \frac{T_0' \times 10\text{Gbps} + T_1 \times 3\text{Gbps} + B \times T_2 \times 0\text{Gbps}}{T_0' + T_1 + T_2(1-B)} = 9.692\text{ Gbps}
$$

### (b) Compute how often (e.g. how many times a day on average) a human operator's intervention is needed.

$$
E[\text{cycle}] = \frac{E[\text{Time Not working}]}{P[\text{No Traffic}]} = \frac{T_2}{P[\text{No traffic}]} = 103\text{ hours/min}
$$

$$
103 \times 0.62 \times \frac{1}{60 \times 24} = 7.2\text{ days}
$$

For all the above quantities, find mathematical expressions as a function of the parameters and then compute their numerical values for $T_0 = 20\text{ min}$ $T_1 = 20\text{ min}$, $T_2 = 3\text{ hours}$, $\alpha = 0.98$, $\beta = 0.4$.

---

<!-- Pagina 2 -->

## E4. Consider an exhibition where visitors arrive according to a Poisson process with rate $\lambda = 12$ customers per hour. Each visitor spends a time uniformly distributed between 10 and 15 min, and then leaves. The room in which the exhibition is shown is large enough to ensure there is never a need to block customers at entrance due to too many people inside. The exhibition is open from 8 AM to 6 PM.

### (a) Compute the probability that fewer than 2 visitors arrive during the first fifteen minutes.

System $M/G/100$
$\lambda = 12$ per hour. $\lambda = \frac{1}{5}$ per min. $\frac{1}{\lambda} = 5$

$$
P[x(0.25) < 2] = P[x(0.25) = 0] + P[x(0.25) = 1]
$$

$$
= \frac{e^{-3}(3)^{0}}{0!} + \frac{e^{-3}(3)^{1}}{1!} = 0.1991
$$

### (b) Compute the probability that at 8:15 AM there is only one visitor in the room, and the probability that at closing time (6 PM) the room is empty.

$\Lambda = \lambda \int_{0}^{12} [1-G(2)] dz = 12 \int_{0}^{0.25} [1-G(z)] dz = 12 \left(\frac{5}{24}\right) = \frac{5}{2}$

$$
P[M(0,25) = 1] = \frac{e^{-\Lambda}}{4!} = \frac{e^{-\frac{5}{2}}}{1} = 0.205
$$

$\Lambda = \lambda \cdot \frac{5}{24} \Lambda = 12 \cdot \left(\frac{5}{24}\right) = 2.5$

$$
P[M(0,25) = 1] = \frac{e^{-25\Lambda}}{1} = 0.205
$$

$$
P[\text{not empty at 6 PM}] = e^{-\Lambda}; \Lambda = \lambda E[\text{service}] = 12(0.2043); e^{-\Lambda} = e^{-0.2043} = 0
$$

$$
E[\text{service}] = E\left(U\left[10^1, 15^1\right]\right) = \frac{25}{2} = 12.5 \text{ min} \rightarrow 0.2083
$$

$$
P[\text{empty at 6 PM}] = e^{-\frac{5}{2}} = 0.8208
$$

---

<!-- Pagina 3 -->

# June 22, 2021

## E2. Consider a two-state Markov channel, where the steady-state probability that the channel is in the bad state is 0.02 and the average number of consecutive good slots is 100. The packet error probability is 1 for a bad slot and 0 for a good slot, respectively. The round-trip time is $m = 2$. i.e. a packet that is erroneous in slot $E$ is retransmitted in slot $+1 + 2$ (if a retransmission protocol is used).

### (a) Compute the throughput that could be obtained if packets were directly transmitted over the channel without using any protocol.

$$
E(G) = 100; \rightarrow P_{01} = \frac{1}{E(G)} = 0.01 \quad \pi_B = 0.02
$$

$$
p = \begin{pmatrix} 0.99 & 0.01 \\ 0.49 & 0.51 \end{pmatrix} \quad \pi_B = \frac{P_{01}}{P_{01} + P_{10}} = 0.02
$$

$$
p^2 = \begin{pmatrix} 0.985 & 0.015 \\ 0.735 & 0.265 \end{pmatrix} \quad \pi_B P_{01} + P_{10} \pi_B = P_{01}
$$

$$
P_{30} = \frac{P_{01} - \pi_B P_{01}}{\pi_B} = \frac{0.01}{0.02} - 0.01
$$

$$
P_{30} = 0.49
$$

$$
T = \pi_G = 0.98
$$

### (b) Compute the throughput of the Go-Back-N protocol for an error-free feedback channel.

$$
T = \frac{P_{10}^{(2)}}{P_{10}^{(2)} + (2) P_{01}} = \frac{0.735}{0.735 + (2)(0.01)} = 0.9735
$$

### (c) Compute the throughput of the Go-Back-N protocol for a feedback channel subject to i.i.d. errors with probability 0.1.

$$
T = \frac{(1 - \delta) P_{10}(m)}{(1 - \delta) P_{10}^{(m)} + m((1 - \delta) P_{01} + \delta P_{10}^{(m)})} = 0.797968
$$

---

<!-- Pagina 4 -->

## E4. Consider a node that contains 2 identical and independent servers, each able to stream data at 1 Gbps. Each server is subject to attacks according to a Poisson process with rate $\lambda = 10$ attacks/hour, and each attack is effective with probability 1/9, whereas it has no consequence with probability 8/9. (Hint: only consider the process of effective attacks. As a result of each effective attack, the server will remain inoperative (i.e. with zero streaming rates) for an exponential time with average $T = 6$ min, during which any arriving attack will have no effect, and then will resume normal operations.

### (a) Compute the fraction of time during which the node doesn't stream data (both servers are inoperative), and the average duration of a period of time during which data is streamed.

$$
\lambda' = 10 \left(\frac{1}{9}\right) = \frac{10}{9} \text{ effective attacks per hour.}
$$

$$
T' = \frac{1}{\lambda'} = \frac{9}{10} \text{ attacks per hour.}
$$

$$
P(1 \text{ serv. down}) = \frac{T}{\frac{1}{\lambda'} + T} = \frac{6 \text{ min}}{54 \text{ min} + 6 \text{ min}} = 0.1
$$

$$
P(2 \text{ serv. down}) = (0.1)^2 = 0.01.
$$

$$
E[\text{Node does not work}] = \frac{1}{2} T = 3 \text{ min}
$$

### (b) By considering an appropriate renewal cycle, compute the average duration of the time interval during which the node is able to stream data without interruption. (There is always at least one server working).

$$
E[\text{cycle}] = \frac{T/2}{P[\text{system down}]} = \frac{3 \text{ min}}{0.01} = 300
$$

### (c) Compute the average total streaming rate of the node in 6 Gbps.

1 server = 1 Gbps (0.9) = 0.9 Gbps
2 server = 1.8 Gbps
2 (0.9) = 1.8

---

<!-- Pagina 5 -->

## E3. Consider a Markov chain $X_n$ with the following transition matrix (states are numbered from 0 to 2):

$$
P = \begin{pmatrix}
0.2 & 0.6 & 0.2 \\
0.6 & 0.2 & 0.2 \\
0 & 0 & 1
\end{pmatrix}
$$

### (a) Draw the transition diagram, and find the probability distribution of $X_1, X_2$ and $X_{1000}$, given $X_0 = 0$.

$$
P = \begin{pmatrix}
0.2 & 0.6 & 0.2 \\
0.6 & 0.2 & 0.2 \\
0 & 0 & 1
\end{pmatrix}
$$

$$
P^2 = \begin{pmatrix}
0.4 & 0.24 & 0.36 \\
0.24 & 0.4 & 0.36 \\
0 & 0 & 1
\end{pmatrix}
$$

$X_1 = (0.2, 0.6, 0.2)$ $X_2 = (0.4, 0.24, 0.36)$

2 is an absorption state then $X_{1000} = (0, 0, 1)$

### (h) Let $W_{ej}^{(n)} = E \left[ \sum_{k=0}^{n-1} I \{X_k = j | X_0 = j \} \right]$ be the average number of visits to state $j$ during the first $n$ time slots, given that the chain starts in state $x$. Compute $\lim_{n \to \infty} W_{ej}^{(n)}$ for $j = 0, 1, 2$.

As $2$ is an absorbing state then $\lim_{n \to \infty} W_{oj}^{(n)} = \infty$.

$$
V_{00} = 1 + P_{00} V_{00} + P_{01} V_{10} = 1 + 0.2 V_{00} + 0.6 V_{10}; V_{00} = \frac{20}{7}; V_{10} = \frac{20}{7}
$$

$$
V_{10} = 0 + P_{10} V_{00} + P_{11} V_{10} = 0 + 0.6 V_{00} + 0.2 V_{10}; V_{10} = \frac{15}{7}; V_{01} = \frac{15}{7}
$$

### (c) Compute the average duration of the transient evolution of the chain, i.e. the time index at which the chain is absorbed.

$$
V_1 = \frac{20}{7} + \frac{15}{7} = 5.
$$

By symmetry, $V_0 = 5$.

---

<!-- Pagina 6 -->

## E. Consider a Markov chain $X_n$ with the following transition matrix (states are numbered from 0 to 2):

$$
P = \begin{pmatrix}
0.2 & 0.4 & 0.4 \\
0.5 & 0.5 & 0 \\
0.4 & 0.4 & 0.2
\end{pmatrix}
$$

### (a) Draw the transition diagram, and find the probability distribution of $X_1, X_2$ and $X_{500}$, given $X_0 = 0$.

$$
P = \begin{pmatrix}
0.2 & 0.4 & 0.4 \\
0.5 & 0.5 & 0 \\
0.4 & 0.4 & 0.2
\end{pmatrix}
$$

$$
P^2 = \begin{pmatrix}
0.4 & 0.44 & 0.16 \\
0.35 & 0.45 & 0.2 \\
0.36 & 0.44 & 0.2
\end{pmatrix}
$$

$$
X_1 = (0.2, 0.4, 0.4)
$$

$$
X_2 = (0.4, 0.44, 0.16)
$$

$$
\pi_0 = 0.2\pi_0 + 0.5\pi_1 + 0.4\pi_2
$$

$$
\pi_0 = 0.3703
$$

$$
\pi_2 = 0.4444
$$

$$
\pi_0 + \pi_1 + \pi_2 = 1
$$

$$
\pi_2 = 0.1851
$$

### (b) Compute the average first passage times from states 0 and 2 state 2.

$$
E[T|X_0 = 2] = \frac{1}{\pi_2} = 5.4
$$

$$
2J_0 = 1 + 2J_0 P_{000} + 2J_1 P_{01} = 1 + 2J_0 0.2 + 2J_1 0.4
$$

$$
2J_1 = 1 + 2J_0 P_{100} + 2J_1 P_{11} = 1 + 2J_0 0.5 + 2J_1 0.5
$$

$$
\frac{a}{2}, \frac{13}{2}, 5
$$

### (c) Let $W_{ij}(n) = E[\sum_{k=0}^{n-1} X_k = j]$ be the average number of visits to state $j$ during the first $n$ time slots, given that the chain starts in state $x$. Compute $W_{ij}(3)$ and $W_{ij}(50000)$ for $j = 0, 1, 2$.

$$
W_{ij}(3) = P_{0j} + P_{0j}(1) + P_{0j}(2) = \begin{cases}
1 + 0.2 + 0.4 = 1.6 & j=0 \\
0 + 0.4 + 0.44 = 0.84 & j=1 \\
0 + 0.4 + 0.16 = 0.56 & j=2
\end{cases}
$$

$$
W_{ij}(50000) \approx 5000\pi_j = \begin{cases}
1852 & j=0 \\
2222 & j=1 \\
926 & j=2
\end{cases}
$$

Average recurrent time $m = \left[ \frac{y\pi_0}{1\pi_1} \right]$

---

<!-- Pagina 7 -->

# June 24, 2022

### (a) $P[X_1(1) = 1 \mid X_2(1) = 2] = P[X_1(1) = 1 \mid X_1(1) = 2] = \binom{2}{1} \left( \frac{\lambda_3}{\lambda_3 + \lambda_2} \right)^4 \left( 1 - \frac{\lambda_3}{\lambda_1 \lambda_2} \right)^{2-1}$

$P[X_2(1) + X_2(1) = 2 \mid X_4(1) = 1] = P[X_1(1) = 2 \mid X_4(1) = 1] = P[X_2(1) = 1] = \frac{e^{-\lambda_2}}{\lambda_2!} = 0.368$

### (b) $P[X_3(1) = 1 \mid X_2(2) + X_2(2) = 4] = P[X_3(1) = 1 \mid X_2(2) = 4]$

$= \binom{4}{2} \left( \frac{1 \lambda_1}{(2) \lambda_1 + \lambda_2} \right)^2 \left( 1 - \frac{(1) \lambda_1}{(2) \lambda_1 + \lambda_2} \right)^{4-1} = 0.4218$

$P[X_1(2) + X_2(2) = 4 \mid X_1(1) = 1]$

$P[X_2(2) = 4 \mid X_1(1) = 1] = P[X_1(2) + X_2(2) - X_1(1) = 3] =$
$= \frac{(2 \lambda_1 + 2 \lambda_2 - \lambda_1)^3 e^{-(2 \lambda_1 + 2 \lambda_2 - \lambda_1)}}{3!} = 0.2240$

---

<!-- Pagina 8 -->

## E3. Consider a Markov chain with the following transition matrix

(states are numbered from 0 to 4)

$$
p \begin{pmatrix}
0 & 0 & 0 & 1 & 0 \\
0 & 0.7 & 0 & 0 & 0.3 \\
0 & 0 & 0.4 & 0.2 & 0.4 \\
1 & 0 & 0 & 0 & 0 \\
0.6 & 0 & 0 & 0.4
\end{pmatrix}
$$

### (a) Draw the transition diagram identify the classes, classify the states and compute the probability absorption in all recurrent classes starting from each transient state.

Positive recurrent
periodic
d=2

$$
\text{[Abs in } \{0,3\} \text{ starting from } \{2\} \}=\frac{0.2}{0.4+0.2}=0.33
$$

$$
P[\text{Abs in } \{4,1\} \text{ from } 3]=\frac{0.4}{0.4+0.2}=0.6
$$

### (b) Compute $\lim_{n \to \infty} p^n$ and $\lim_{n \to \infty} \frac{1}{n} \sum_{k=0}^{n-1} p_k$

$$
\begin{cases}
\pi_1 = 0.7 + 0.6\pi_4 \\
\pi_2 + \pi_4 = 1
\end{cases}
$$

$$
\pi_4 = \frac{1}{3}
$$

$$
\lim_{n \to \infty} p^n = \begin{bmatrix}
x & 0 & 0 & x & 0 \\
0 & \frac{2}{3} & 0 & 0 & \frac{1}{3} \\
x & \frac{3}{3} & 0 & x & \frac{3}{3} \\
x & 0 & 0 & x & 0 \\
0 & \frac{2}{3} & 0 & 0 & \frac{1}{3}
\end{bmatrix}
$$

$$
\sum_{k=0}^{n-1} p^k = \begin{bmatrix}
\frac{1}{2} & 0 & 0 & \frac{1}{2} & 0 \\
0 & \frac{3}{3} & 0 & 0 & \frac{3}{3} \\
0 & 4/3 & 0 & 1/3 & 2/3 \\
0 & 2 & 0 & 0 & 2/3 \\
0 & \frac{2}{3} & 0 & 0 & \frac{1}{3}
\end{bmatrix}
$$

### (c) Compute the average recurrence time for all states, and the average first passage time from any state to state 4.

Average recurrence time

$$
m_4 = \frac{1}{\pi_4} = \frac{3}{2}
$$

$$
m_4 = \frac{1}{\pi_4} = 3
$$

Because they are positive recurrent,

$$
m_0 = m_3 = 2
$$

guaranteed to come back in 2 steps.

$$
m_2 = +\infty
$$

for transient, because won't come back.

$$
m = (2, \frac{3}{2}, +\infty, 2, 3)
$$

Average first passage time from any state to state 4.

$$
V_{04} = V_2, 3 = \infty
$$

because recurrent from different classes.

$$
V_{24} = +\infty
$$

because transient.

$$
V_{44} = \frac{1}{\pi_4} = 3
$$

$$
V_{14} = 1 + P_{11} \cdot V_{14}
$$

$$
V_{14} = \frac{1}{1 - P_{11}} = \frac{1}{0.3} = 3.33
$$

---

<!-- Pagina 9 -->

# 14 July 2006

## E3. Consider an exhibition where visitors arrive according to a Poisson process with rate $\lambda = 10$ customers per hour. Each visitor spends a time uniformly distributed between 20 and 30 min, and then leaves. The room in which the exhibition is shown is large enough to ensure there is never a need to block customers at the entrance due to too many people inside. The exhibition is open 8 AM to 6 PM.

### (a) Compute the probability that fewer than 3 visitors arrive during the first half hour.

$$
P[X(0.5) < 3] = P[X(0.5) = 0] + P[X(0.5) = 1] + P[X(0.5) = 2]
$$

$$
= \frac{e^{-5}(5)^{0}}{0!} + \frac{e^{-5}(5)^{1}}{1!} + \frac{e^{-5}(5)^{2}}{2!} \approx 0.12465
$$

### (b) Compute the probability that at 8:15 AM there is only one visitor in the room.

$$
\Lambda = \lambda \int_{0}^{14} [1-G(2)] dz = 10(0.25) = 2.5
$$

$$
P[M(0.25) = 1] = e^{-1}\Lambda^{1} = e^{-2.5}(2.5) = 0.2052
$$

The integral until is asking 15 min.

### (c) Compute the probability that at closing time (6 PM) the room is empty.

$$
P[empty at 6 PM] = e^{-1} = e^{-25/6} = 0.0155
$$

---

<!-- Pagina 10 -->

## E1. Consider a Go-Back-N protocol over a two-state Markov channel, where the average number of consecutive good slots is 100 and the average number of consecutive bad slots is 100/9. The packet error probability is 1 for a bad slot and 0 for a good slot respectively. The round-trip time is $m = 2$ slots, i.e. packet that is erroneous in slot $E$ will be retransmitted in slot $E+2$.

### (a) Compute the throughput that could be obtained if packets were directly transmitted over the channel without using any protocol.

<!-- Missing image in source: Graph -->

$$
\text{Average good slots} = 100
$$

$$
E(G) = 100
$$

4. Prob. of leaving the good state is $P_{01} = \frac{1}{100} = 0.01$

$$
C = \begin{bmatrix}
P_{00} & P_{01} \\
0.99 & 0.01
\end{bmatrix}
$$

$$
P_{10} = \frac{a}{100}
$$

In this case $T = \frac{P_{10}}{P_{10} + P_{01}} = \frac{0.09}{0.09 + 0.01} = 0.9$

### (b) Compute the throughput of the Go-Back-N Protocol for an error-free feedback channel.

$$
P^2 = \begin{bmatrix}
0.981 & 0.019 \\
0.171 & 0.829
\end{bmatrix}
$$

$$
C = \begin{bmatrix}
P_{00} & P_{01} \\
P_{10}^{(m)} & P_{11}^{(m)}
\end{bmatrix}
$$

$$
C^2 = \begin{bmatrix}
0.99 & 0.01 \\
0.171 & 0.829
\end{bmatrix}
$$

$$
T = \frac{P_{10}^{(m)}}{P_{10}^{(m)} + mP_{01}} = \frac{0.171}{0.171 + (2)(0.01)} = 0.8952
$$

### (c) Compute the throughput of the Go-Back-N protocol for a feedback channel to avoid errors with probability $0.1 = \delta$

$$
T = \frac{(1 - \delta)P_{10}^{(m)}}{(1 - \delta)P_{10}^{(m)} + m((1 - \delta)P_{01} + \delta P_{10}^{(m)})}
$$

$$
= \frac{(1 - .1)(.171)}{(1 - .1).171 + (2 \times (1.9 \times 0.01) + (.1 \times 0.019) + (.1 \times 0.171))}
$$

$$
= 0.7332
$$

---

<!-- Pagina 11 -->

## E2. Consider a Markov chain $X_n$, with the following matrix (states are numbered from 0 to 2)

$$
P = \begin{pmatrix}
0.3 & 0.5 & 0.2 \\
0.5 & 0.3 & 0.2 \\
0 & 0 & 1
\end{pmatrix}
$$

### (a) Draw the transition diagram, and find the probability distribution of $X_1, X_2$, and $X_1000$, given $X_0 = 0$.

$$
p^2 = \begin{pmatrix}
0.34 & 0.5 & 0.36 \\
0.3 & 0.34 & 0.36 \\
0 & 0 & 1
\end{pmatrix}
$$

Distribution of $X_2$ is the first row of $P_2$, $X_2 = (0.34, 0.3, 0.36)$.

Considering a long term run and 2 is an absorbing state, $P_{1000} = (0, 0, 1)$.

### (b) Let $W_{ij}^{(n)} = E \left[ \sum_{k=0}^{n-1} I \left| X_k = j \right| X_0 = j \right]$ be the average number of visits to state $j$ during the first $n$ time slots, given that the chain starts in state $i$. Compute $\lim_{n \to \infty} W_{0j}^{(n)}$ for $j = 0, 1, 2$.

So we can say $\lim_{n \to \infty} W_{02}^{(n)} = \infty$ because that's a recommend state.

$$
V_{ij} = \lim_{n \to \infty} W_{ij}^{(n)} \quad i \neq j
$$

$$
V_{ij} = d_{ij} + P_{10} V_{0j} + P_{21} V_{2j} \quad i, j = 0, 1
$$

If $j = 0$, $V_{00} = 1 + P_{00} V_{00} + P_{01} V_{10} = 1 + 0.2 V_{00} + 0.6 V_{10}$

$$
V_{10} = 0 + P_{30} V_{00} + P_{11} V_{10} = 0.6 V_{00} + 0.2 V_{10}
$$

$$
V_{30} = 15/7
$$

Compute the average duration of the transient evolution of the chain, ie the time index at which the chain is absorbed.

$$
V_1 = E[\text{absorption time } | X_0 = i] = E \left[ \text{visits to } 0 \text{ or } 1 \right| X_0 = i
$$

Length of transient phase

Time the chain spends in 0 or 1 before 2.

$$
V_{00} + V_{10} = \frac{20 + 15}{7}
$$

And just because the transient port is symmetry, it doesn't depend on the initial state.

---

<!-- Pagina 12 -->

# July 13, 2021

## E1. Consider a Go-Back-N protocol over a two-state Markov channel, where the average number of consecutive good slots is 100 and the average number of consecutive bad slots is 100/9. The packet error probability is 1 for a bad slot and 0 for a good slot respectively. The round-trip time is $m = 2$ slots, i.e. packet that is erroneous in slot $E$ will be retransmitted in slot $E + 2$.

### (a) Compute the throughput that could be obtained if packets were directly transmitted over the channel without using any protocol.

$$
\begin{align*}
\text{Average good slots} &= 100 \\
E(G) &= 100 \\
\text{Prob. of leaving the good state} &= P_{01} = \frac{1}{100} = 0.01 \\
\text{Average of bad slots} &= 100 \\
P_{10} = \frac{a}{100}
\end{align*}
$$

In this case $T: \frac{P_{10}}{P_{10} + P_{01}} = \frac{0.09}{0.09 + 0.01} = 0.9$

### (b) Compute the throughput of the Go-Back-N Protocol for an error-free feedback channel.

$$
P^2 = \begin{pmatrix}
0.981 & 0.019 \\
0.171 & 0.829
\end{pmatrix} \quad c = \begin{bmatrix}
P_{00} & P_{01} \\
P_{10}^{(m)} & P_{10}^{(m)}
\end{bmatrix} \quad c^2 = \begin{bmatrix}
0.99 & 0.01 \\
0.171 & 0.829
\end{bmatrix}
$$

$$
T = \frac{P_{10}^{(m)}}{P_{10}^{(m)} + mP_{01}} = \frac{0.171}{0.171 + (2)(0.01)} = 0.8952
$$

### (c) Compute the throughput of the Go-Back-N protocol for a feedback channel to avoid errors with probability $0.1 = \delta$

$$
T = \frac{(1 - \delta) P_{10}^{(m)}}{(1 - \delta) P_{10}^{(m)} + m ((1 - \delta) P_{01} + \delta P_{10}^{(m)} + \delta P_{10}^{(m)})}
$$

$$
= \frac{(1 - .1)(.171)}{(1 - .1).171 + (2 \times (1.9 \times 0.01) + (.1 \times 0.019) + (.1 \times 1.171))}
$$

$$
= 0.7332
$$

---

<!-- Pagina 13 -->

1. Matrix Markov chain.
2. Identical machines with period of time.
3. Semi-Markov network node: sleep, awake, reception.
4. System with Poisson request/service, period and no queue.
5. Network with one node and 2 outgoing links, each one with queue and TX restriction.
6. Node with 2 incoming links: independent Poisson processes and equations.
7. Markov channel with good/bad states and Go-Back-N protocol.
8. Matrix Markov chain.
9. Poisson arrival process with queue and TX restriction; Poisson process with rate $R$; no queue, exponential service; compute people in the system at time $t$.
10. Go-Back-N Protocol.
11. Web server: uniformly distributed, steady condition.
12. CSMA: Poisson process rate, delay, throughput.
13. Matrix Markov chain.
14. Network node normal/alarm condition with limited capacity.

---

<!-- Pagina 14 -->

# Exam 09/07/2007

## E1. Consider a Markov chain $X_n$ with the following transition matrix (states are numbered from 0 to 2, and initial state $X_0 = 0$)

$$
P = \begin{pmatrix}
0.4 & 0.4 & 0.2 \\
0.2 & 0.2 & 0.6 \\
1 & 0 & 0
\end{pmatrix}
$$

### (a) Draw the transition diagram and find the probability distributions of $X_1, X_2$ and $X_{500}$

$$
P(X_1) = (0.4, 0.4, 0.2)
$$

$$
P(X_2) = (0.44, 0.24, 0.32)
$$

$$
P(X_{500}) = \text{We can assume the chain is in long run behavior, so we can use steady state distribution. Then compute:}
$$

$$
\pi_0 = \pi \cdot P
$$

$$
\pi_0 + \pi_4 + \pi_2 = 1
$$

$$
\pi_0(0.4 = P_{00}) + \pi_1(0.2 = P_{10}) + \pi_2(1 = P_{20}) = \pi_0
$$

$$
\pi_0(0.4 = P_{01}) + \pi_1(0.2 = P_{11}) + \pi_2(0 = P_{21}) = \pi_2
$$

$$
\pi_0(0.2 = P_{02}) + \pi_1(0.6 = P_{12}) + \pi_2(0 = P_{22}) = \pi_2
$$

$$
\pi_0 + \pi_1 + \pi_2 = 1
$$

$$
\pi_0 = 0.5 \quad \pi_1 = 0.25 \quad \pi_2 = 0.25
$$

$$
P(X_{500}) = (0.5, 0.25, 0.25)
$$

### (b) Compute the average first passage times from states 0, 1 and 2 to state 2

$$
\mu_0 = 1 + P_{00} \mu_0 + P_{01} \mu_1 = 1 + 0.4 \mu_0 + 0.4 \mu_1
$$

$$
\mu_1 = 1 + P_{10} \mu_0 + P_{11} \mu_1 = 1 + 0.2 \mu_0 + 0.2 \mu_1
$$

$$
V_2 = \frac{1}{\pi_2} = \frac{1}{V_4} = 4
$$

$$
V_2 = 1 + P_{20} \cdot V_0
$$

$$
4 = 1 + P_{20} \cdot V_0 \rightarrow V_0 = 3
$$

$$
3 = 1 + 0.4(3) + 0.4V_2
$$

$$
V_0 = 3 \quad V_2 = 2 \quad V_2 = 4
$$

### (c) Compute $P[X_1 = 1, X_3 = 1 | X_2 = 1]$ and $P[X_2 = 1 | X_1 = 1, X_3 = 1]$

$$
P[X_1 = 1, X_3 = 1 | X_2 = 1] = P[X_1 = 1, X_2 = 1, X_3 = 1 | X_0 = 0]
$$

$$
= \frac{(0.4)(0.2)(0.2)}{0.24} = 0.62
$$

$$
P[X_2 = 1 | X_1 = 1, X_3 = 1] = P[X_2 = 1, X_3 = 1 | X_0 = 0]
$$

$$
= \frac{(0.4)(0.2)(0.2)}{0.24} = 0.53
$$

$$
P[X_1 = 1, X_3 = 1 | X_2 = 1] = P[X_1 = 1, X_2 = 1, X_3 = 1 | X_0 = 0]
$$

$$
= \frac{(0.4)(0.2)(0.2)}{0.24} = 0.53
$$

---

<!-- Pagina 15 -->

## Extra question in other exams

Let $W_{ij}^{(m)} = E[\sum_{k=0}^{n-1} I\{X_k = j\} X_0 = i]$ be the average num of visits to state $j$ during the first $n$ time slots, given that the chain starts in state $i$. Compute $W_{ij}^{(3)}$ and $W_{ij}^{(500)}$ for $j = 0, 1, 2$.

$$
W_{ij}^{(n)} = E[\sum_{k=0}^{n-1} \times \{X_k = j\} |X_0 = i] = \sum_{k=0}^{n-1} P_{ij}^{(k)}
$$

In 3:

$$
= P_{ij}^{(0)} + P_{ij}^{(1)} + P_{ij}^{(2)} \rightarrow W_{00}^{3} = P_{00}^{0} + P_{00}^{1} + P_{00}^{2}
$$

In $W_{ij}^{(500)}$ we can use steady state distribution multiplied by 5000.

$$
W_{00}^{500} = 5000\tau_{ij}
$$

$$
W_{01}^{500} = 5000\tau_{10}
$$

$$
W_{02}^{500} = 5000\tau_{12}
$$

## E2. Consider a factory with 2 identical machines. Each machine alternates periods of time in which it is working or not working, of exponential duration with mean $\frac{1}{\alpha} = 27$ days (working) and $\frac{1}{\beta} = 1/\alpha$ (not working). Each machine, whose operation is independent of the other, can produce 12 pieces per hour when is working.

### (a) Compute the fraction of time in which there is no production (i.e. both machines are not working).

$$
P[\text{Machine not work}] = \frac{1/\beta}{1/\alpha + 1/\beta} = 0.1
$$

$$
P[\text{No production}] = (0.1)^2 = 0.01
$$

### (b) Compute the average number of pieces per hour produced by the factory.

$$
E[\text{NUM PROD}] = (12 \text{ pieces/hour} \cdot (1 - 0.01)) \cdot 2 \text{ machines} = 21.6 \text{ pieces/hour}
$$

### (c) Compute the average number of pieces per hour produced by the factory if the number of pieces produced per hour is 12 when only one machine is working and 30 when they are both working.

$$
E[\text{Produce}] = 0.81 \cdot 30 + 0.18 \cdot 12 + 0.01 \cdot 0 = 26.46
$$

$$
0.9 \cdot 0.9
$$

$$
1 - 0.01
$$

$$
1 - 0.01 - 0.81
$$

---

<!-- Pagina 16 -->

## E3. Consider a network node that works as follows, if there is no traffic, the node alternates between a sleep state for an exponential duration of average $\pi$ an awake state for a fixed duration $\beta T$. When in the awake state, the node can receive it entirely (even if requires it to remain awake for a total time longer than $\beta \pi$) and goes to sleep immediately after. If instead while the node is awake there is no transmission, the node goes back to time at which such transmission starts is uniformly distributed in $[0, \beta \pi]$ and the average packet transmission time is $\gamma \pi$. Develop and solve a semi-Markov model for the node, and in particular:

### (a) Consider the 3 states sleep(s), listening (L) and receiving (R), determine the matrix of the trans. probability of the embedded Markov Chain and draw its transition diagram.

<!-- Missing image in source: transition diagram -->

### (b) Determine the matrix of the average times associated to each transmission, $\tau$, and the average times associated to the visits to each state $s$, $M_s$, $M_r$.

$$
\begin{align*}
T &= S \begin{matrix} S & L & R \\ - & T & - \\ \beta T & - & \beta T \end{matrix} \\
M_i &= \sum_j P_{ij} T_{ij} \\
M_r &= \gamma T
\end{align*}
$$

### (c) Find an expression for the fraction of time the node spends in each of the 3 states and find its numerical value for $\alpha = 0.5$, $\beta = 0.1$, $\gamma = 0.2$.

$$
\frac{Fraction\ of\ time\ given\ by}{Fraction\ of\ time\ given\ by} = \frac{(2 + \alpha)(\pi M_i)}{T(1 + \beta - \frac{\alpha \beta}{2} + \alpha \gamma)}
$$

$$
P_s = \frac{T}{2 + \alpha} \frac{2 + \alpha}{T(1 + \beta - \frac{\alpha \beta}{2} + \alpha \gamma)} = 0.851
$$

$$
P_l = \frac{(2 - \alpha) \beta T}{2 + \alpha} \frac{2 + \alpha}{T(1 + \beta - \frac{\alpha \beta}{2} + \alpha \gamma)} = 0.064
$$

$$
P_o = \frac{2 + \alpha}{T \alpha} \frac{2 + \alpha}{T(1 + \beta - \frac{\alpha \beta}{2} + \alpha \gamma)} = 0.085
$$

---

<!-- Pagina 17 -->

## Exercise. Consider a system which receives service requests according to a Poisson process of rate $\lambda = 20$ requests per hour. Each request remains in the system for a service time equal to 6 minutes, and there is no limit to the number of requests simultaneously in service. Assume that the system started its operation at time $t = 0$,

### (a) Compute the probability that the system is empty at time $t = 30$ min.

$$
\lambda = 20 \text{ req/min}
$$

The service time $V$ is deterministic, $G_y(x) = \begin{cases} 1 & x \geq 6 \\ 0 & x \leq 6 \end{cases}$

If $M(t)$ is the r.v. that counts the users in the system at time $t$,

$$
\Pr[M(0.5) = 0] = \frac{e^{-\lambda}}{0!} \text{ where } \lambda = \lambda \int_{0}^{0.5}[1-G(x)]dx = \frac{\lambda}{10} = 2
$$

$$
\Lambda = \lambda E[y] = \frac{20}{60} \cdot G = 2 \rightarrow \Pr[M(0.5) = 0] = e^{-2} = 0.135
$$

### (b) Compute the probability that the system is empty at time $t = 30$ min, conditioned on the fact there were 10 arrivals between 0 and $t$.

$$
\Pr[M(t) = m | X(t) = n] = \binom{n}{m} p^m (1-p)^{n-m}
$$

$$
\Pr[M(0.5) = 0 | X(0.5) = 10] = \binom{10}{0} (0.2)^0 (0.8)^{10} = 0.10737
$$

where $p = \frac{1}{t} \int_{0}^{t}[1-G(y)]dx = 0.2$

$$
1-p = \frac{1}{30} \int_{0}^{30} 1dx = \frac{24}{30}
$$

Alternative computations:

$P(M(t) = 0] = e^{-2pt} = e^{-2 \times 0.2 \times 30} = e^{-1.6} = 0.135$

$$
= e^{-x_3} = e^{-2} = 0.135
$$

$P[M(t) = 0 | X(t) = 10] = \binom{10}{0} p^0(1-p)^{10} = \left(\frac{4}{5}\right)^{10} = 0.107$

$$
F = \frac{1}{6} \int_{1}^{6}[1-G(2)]dx = \frac{1}{30}(6) = \frac{1}{5}
$$

$$
= \frac{1}{30} \int_{1}^{30}[1-G(2)]dx = \frac{6}{30} = \frac{1}{5}
$$

---

<!-- Pagina 18 -->

## E2*.

Consider a network node with 2 outgoing links $L_1$ and $L_2$. The two links have a capacity of 1 Mbps, and are fed by 2 separate queues $Q_1$ and $Q_2$ which can contain rules $\lambda_1 = \lambda_2 = \lambda = 500$ pk/s, and that flow $\lambda_2$ is released only to link $L_2$ (and therefore queue $Q_1$), $i = 1, 2$. Two packets are transmitted simultaneously when both queues are full 1 part. When there is a packet in one of the queues, the node waits until the other queue also receives a packet, and only then does it send both packets, each on its own link. (Note that a time interval in which both queues are empty is followed by one in which one queue is empty and the other is full, which in turn followed by another in which both packets are being transmitted.) Furthermore, assume that when $Q_1$ is full (i.e. when there is a packet waiting to be transmitted) one arriver of flow $\lambda_2$ is rejected. All packets are 2000 bits long.

### (a) Compute the throughput of the node in terms of total bps transmitted

$$
\text{Throughput} = \frac{\text{Pixel TX}}{\text{Temperature}} = \frac{1000(2)}{4\text{ms}} = 0.5\text{ Mbps}
$$

### (b) Compute the fraction of the total traffic that is rejected.

Use PASTA

$$
\text{REJECTION PROB} = \frac{1}{4} \cdot 0 + \frac{1}{2} \cdot \frac{1}{4} \cdot 1 = \frac{1}{2}
$$

Fraction the time of the process proportional to the internal traffic.

### (c) Repeat the previous calculations if the length of the packets, instead of being fixed to 2000 bits, has exponential duration with mean 2000 bits. In this case, assume that the 2 queues are considered empty (and therefore the system again can accept incoming packets) only when both packets have completely tx. (i.e. the queue that need shorter packet will be able to accept packets only when the other queue is also empty.

$$
\text{Throughput} = \frac{2000}{4.5\text{ ms}} = 0.44\text{ Mbps}
$$

Fraction of rejectable tx. $0 + \left(\frac{2}{4.5}\right) \frac{1}{2} + \left(\frac{2.5}{4.5}\right) 1 = \frac{5}{4} = 0.556$

Average of 2 exponential with the same parameter $= 1.5$

---

<!-- Pagina 19 -->

## E3. Consider a network node with 2 incoming links, through which packets are received according to 2 independent Poisson process with rates $\lambda_1 = \lambda_2 = 500$ packets per second.

### (a) Compute the probability that in a 3-ms interval the node receives 2 packets from the first link and one from the second.

$$
P[X_1(0,003) = 2] = e^{-500} \cdot (0.003)^2 = 0.25
$$

$$
P[X_2(0,003) = 1] = 0.335
$$

$$
P_T = (0.335)(0.25) = 0.0837
$$

### (b) Compute the probability that in a 3-ms interval the node receives 3 packets in total.

$$
\lambda_{TOT} = \lambda_1 + \lambda_2 = 1000
$$

$$
P[X_{TOT}(0,003) = 3] = e^{-(1000) \cdot (0.003)} \cdot \frac{3}{3!} = 0.224
$$

### (c) Compute the probability that in a 3-ms interval the node receives 2 packets from the first link, given that it received 3 packets in total.

$$
P[X_1(0,000) = 2|X(0,003) = 3] = \binom{3}{2} \left(\frac{2\lambda_1}{3(\lambda_1 + \lambda_2)}\right)^2 \left(1 - \frac{3\lambda_1}{3(\lambda_1 + \lambda_2)}\right)^{2-2}
$$

---

<!-- Pagina 20 -->

## E2. Consider a network node that under normal conditions can handle a traffic equal to 16bps. This node works normally for an exponential time with mean 99 T, and then enters an alarm state during which its capacity is reduced to 290 Mbps. After being for a time T in the alarm state, the node is instantaneously repaired and starts again to work normally.

### (a) Compute the fraction of time the node spends in the alarm state, and the average traffic handled ( suppose that the queues are always full . . . there always packets to transmit.

$$
P[\text{alarm}] = \frac{T}{99T + T} = 0.01
$$

$$
16b \cdot 99T + 0.256bps \cdot 1T = 0.01
$$

Throughput = 0.99 \cdot 1 + 0.01 \cdot 0.025 = 992.5 Mbps

### (b) Suppose now that once entering the alarm state the node completely stops working after an exponential time of mean 2T. Unless it is repaired earlier (as before the repairs requires exactly a time T from when the node enters the alarm state). If the node stops working, it needs to be replaced and this takes a time 20 T, during which the node cannot handle any traffic. (Note that this replacement is different from the simple repaired considered in the previous case)

#### (i) Compute the average time between 2 subsequent substitutions.

$$
E = \int_{1-T}^{T} e^{-\frac{y}{2T}} dt = 2T(1-e^{-\frac{y}{2T}})
$$

Average time between substitutions = 99T + 2T(1-e^{-\frac{y}{2T}}) + 20T \cdot (1-e^{-\frac{y}{2T}})

#### (ii) The fraction of time in which the node is not working

$$
P[\text{NOT working}] = \frac{E[\text{NOTWORK}]}{E[\text{CYCLE}]} = \frac{20T \cdot (1-e^{-\frac{y}{2T}})}{99T + 2T(1-e^{-\frac{y}{2T}}) + 20T \cdot (1-e^{-\frac{y}{2T}})} = 0.0731
$$

#### (iii) The average system throughput.

$$
Throughput = \frac{99T \cdot 16bps + 2T(1-\beta) \cdot 0.25 + 20(1-\beta) \cdot 0}{99T + 2T(1-\beta) + 20(1-\beta)} = 0.92146bps
$$

---

<!-- Pagina 21 -->

# 12/12/20X

## E A. Consider a Markov Chain with the following transition matrix

States are from 0 to 5.

$$
\begin{pmatrix}
0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0.1 & 0 & 0.7 & 0 & 0.2 \\
0 & 0.3 & 0.5 & 0 & 0.2 & 0 \\
0 & 0.7 & 0 & 0.2 & 0 & 0.1 \\
1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0.2 & 0 & 0.1 & 0 & 0.7
\end{pmatrix}
$$

### (a) Draw the transition diagram, classify the states and identify the classes

Transit

Absorbing class
period $d=2$

Positive recurrent aperiodic ($d=1$)

### (b) Compute $\lim_{n \to \infty} p^n$

Since absorbing class has a ping-pong behavior, the limiting distribution is not defined for the whole chain.

And $\pi_2 = 0$ because it is transient.

The submatrix induced by class $\{1, 3, 5\}$ is doubly stochastic, meaning that each row and column sums one. Then, $\pi_1 = \pi_3 = \pi_0 = 1/3$

$\pi_3(\{0, 43\}) = \frac{0.2}{0.5} = 0.4$ $\pi_3(\{1, 3, 5\}) = \frac{0.3}{0.5} = 0.6 = \frac{1}{3}$

Prob of being absorbed starting from 3

### (c) Compute $\lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^{n} p^k$

In periodic states is the average fraction time the chain spends in those states

### (d) Compute $P[X_4 = 5, X_2 = 3 | X_3 = 1, X_1 = 3] = \frac{P_{33} P_{31} P_{35}}{P_{32}(2)}$

$P(X_4 = 5, X_2 = 3 | X_3 = 1, X_1 = 3] = \frac{P[X_4 = 5, X_3 = 1, X_2 = 3]}{P[X_3 = 1 | X_1 = 3]} = \frac{P_{33} P_{31} P_{35}}{P_{32}(2)}$

---

<!-- Pagina 22 -->

## E2. Consider a link with capacity 1 Mbps, shared among many users who collectively produce packets according to a Poisson process with rate $\lambda = 500$ packets per second. All packets are of the same length equal to 400 bits. The access protocol is an ideal CSMA, when a packet generated when the channel is idle gets immediate access, whereas a packet that finds the channel busy is rescheduled after an exponential time of average 100/$\lambda$.

If this new access attempt again finds a busy channel the protocol keeps trying after random times until success. Assume that the total traffic (new packets plus all retransmissions) can be approximated as Poisson with rate $\lambda$.

### (a) Compute the throughput (average traffic handled) on the link.

This system can be modeled as an alternating process, where the renewal instant is the first arrival since the link is empty

$$
E[Tx\ time] = \frac{Packet}{L} = \frac{1000\ bits}{1\times10^6} = 1\ ms.
$$

Average waiting time is $\frac{100}{200\ ms} = 0.5\ ms$.

Fraction of time the link is empty is distributed as an exp of mean $\frac{1}{\lambda} = 2\ ms$.

$$
E[cycle\ time] = E[tx\ time] + E[empty\ time] = 3\ ms
$$

### (b) Compute the average access delay from when a packet is generated to when it finally gets access to the channel.

Let $\beta$ be the probability of finding the system busy

$$
\beta = \frac{E[tx\ time]}{E[cycle\ time]} = \frac{1}{3}
$$

The number of consecutive failed attempts before a successful transmission; where is a r.v., with geometric distribution

$$
P[N \ge k] = \beta^k
$$

and

$$
E[N] = \sum_{k=1}^{\infty} \beta^k = \frac{B}{1-\beta} = \frac{1}{2}
$$

Average delay $E[delay] = E[N]E[wait\ time] = \frac{1}{2} \frac{100}{\lambda} = 100\ ms$

### (c) If a transmission corresponds to a gain of 1 unit and each failed attempt packet finding the channel busy corresponds to a cost of 0.2 units, compute the total gain of the system in units per second.

$$
E[gain\ per\ arrival] = 1 \cdot P[idle] - 0.2P[Busy] = 1 \cdot \frac{2}{3} - 0.2 \cdot \frac{1}{3} = 0.6
$$

$$
E[gain\ per\ unit\ time] = \lambda \cdot E[gain\ per\ arrival] = 300\ unit\ /sec
$$

$$
E[\text{gain in cycle}] = \frac{1 - 0.2E[\text{corr. in }1\text{ ms}]}{E[\text{cycle time}]} = \frac{1 - 0.2\lambda 10^{-3}}{E[\text{cycle time}]} = 300\text{ units}
$$

---

<!-- Pagina 23 -->

## E1. Consider a web server which receives download requests according to a Poisson process with rate $7 = 20$ requests per second. Each request, after a fixed processing time of 20 ms, triggers the transfer of a file with size uniformly distributed between 1 and 2 MB bytes. A request is said to be active from when it arrives to when the corresponding file transfer is completed. Assume that the server capacity, in terms of how many simultaneous requests it can handle, is infinite, and that the transfer rate for each file is 100 MBits, regardless of the number of files that are being transferred at any given time.

### (a) Assuming that the server is switched on at time $= 0$, when does the statistics of the number of active requests in the system reach its steady-state condition? In such condition express $P[k]$ active requests.

Let processing time be $T_{proc} = 0.02$ s.
And the packet length be $L = \cup(8 \cdot 10^6, 16 \cdot 10^6)$ bits.
Server capacity $C = 100 \cdot 10^6$ bits.
Time required for a transmission is $T_{tx} = T_{proc} + \frac{L}{C} \sim \cup(0.1, 0.18)$ using $8 \cdot 10^6$ for the minimum $T_{tx}$ and $16 \cdot 10^6$ for the maximum $T_{tx}$.
$E[T_{tx}] = 0.14$ s
$\frac{a + b}{2} = 0.1 + 0.18 = 0.14$

Problem asks the first $E$ for which the system can be considered in steady-state condition. Clearly $E$ is the first instant from which the function $1-G(z)$ becomes zero, by inspection $E = 0.18$ s.
$\Lambda = \lambda E[T_{tx}] = 2.8$
$jPr[k]$ requests at $t > 0.18] = \frac{e^{-\lambda N} K!}{k!}$

### (b) Given that in an interval of duration $\pi$ the system received $N$ requests, find the probability that at the end of such interval there are no active requests in the 2 cases (b1) $T = 0.15$ s, $N = 2$.

As $x(f)$ is a Binomial r.v. $P_1[M(T) = m]X(T) = N] = \binom{N}{m} p^m (1-p)^{N-m}$ where $p = \frac{1}{T} \int_0^T [1-G_T(x(2))] dz$.

In case $a$ is impossible to have these conditions, then $p = 0$.
$Pr[M(0.1) = 0]X(0.1) = 2] = \binom{2}{1} 1^0 0^{2-0} = 0$

(b2) $T = 1.5$ s, $N = 20$.
$P[M(1) = 0]X(1) = 20] = \binom{20}{0} (0.14)^0 (0.86)^{20-0} = 0.048$ s

---

<!-- Pagina 24 -->

### (c) Repeat the previous calculations assuming that the call duration is uniformly distributed in [2, 10] minutes.

The port of the integrand is computed graphically

$$
E = 6 \rightarrow A = 5 = 2 + (M - 1)
$$

$$
G = 10 \rightarrow A = G = 2 + 4
$$

$$
\Lambda = \begin{cases} \frac{100}{60} (s) = 8.33 & E = 6 \\ \frac{100}{6} (6) = 10 & E = 10, \infty \end{cases}
$$

$$
P[x(4) = 10] = \frac{\Lambda^{10} e^{-1}}{10} = \begin{cases} 0.109 & E = 6 \\ 0.125 & E = 10 \end{cases}
$$

## E. Consider a Go-Back-N Protocol over a two-state Markov channel with transition probability 0.99 (from the good state to itself) and 0.1 (from the bad state to the good state). The packet error probability is $\pm$ for a bad slot and 0 for a good slot, respectively. The round-trip time is $m = 2$ slots, i.e. packet that is erroneous in slot $t$ will be transmitted in slot $t + 2$.

### (a) Compute the throughput of the protocol for an error-free feedback channel

Transition matrix is $P = \begin{bmatrix} 0.00 & 0.01 \\ 0.1 & 0.0 \end{bmatrix}$

Reward vector $R = \begin{bmatrix} R_6 \\ R_0 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$

Time vector $T = \begin{bmatrix} T_6 \\ T_0 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$

Throughput $= \frac{\sum_i \pi_i R_i}{Z_i \pi_i R_i} = \frac{\pi_6}{\pi_6 + 2\pi_0} = \frac{P_{10}^{(2)}}{P_{10}^{(2)} + 2P_{01}}$

### (b) Compute the throughput of the protocol for a feedback channel subject to i.i.d. errors with probability 0.1 = $\delta$

$$
\text{throughput} = \frac{(1 - \delta) P_{10}^{(2)}}{(1 - \delta) P_{10}^{(2)} + 2((1 - \delta) P_{01}^{(2)} + \delta P_{10}^{(2)})}
$$

---

<!-- Pagina 25 -->

## E2. Consider a queue where packets arrive according to a Poisson process with rate $\lambda = 1$ packet per second. All packets in the queue are transmitted when either of the following events occurs: (i) there are two packets in the queue, or (ii) there is one packet in the queue and its waiting time reaches two seconds.

Transmissions is instantaneous, i.e. the queue employs every time there is packet arrival when one packet is already in the queue, or when the only packet in the queue has been there for enough time.

### (a) Compute the fraction of time which the queue is empty.

The distribution of the first arrival is exponential, $E[\text{empty}] = \frac{1}{\lambda}$. After the first arrival we wait until another arrival or up to 2 seconds, then send. The distribution is a truncated exponential.

$$
E[\text{busy}] = \int_0^2 e^{-\lambda t} dt = \frac{1-e^{-2\lambda}}{\lambda} = 0.8646
$$

Fraction of time spent empty is $P_{\text{empty}} = \frac{E[\text{empty}]}{E[\text{empty}]+E[\text{busy}]} = 0.536$

### (b) Compute the average delay (i.e. the average time a packet spends in the queue).

If a packet finds the queue non empty, the transmission is immediate. Otherwise, it has to wait $\frac{1-e^{-2\lambda}}{\lambda}$ on average. By the law of total probability we have:

$$
E[\text{delay}] = E[\text{delay}|\text{empty}]P_{\text{empty}} + E[\text{delay}|\text{busy}]P_{\text{busy}}
$$

$$
= (0.864)(0.536) = 0.463
$$

## E3. Consider a frequency division transmission system in which the number of channels is so large that the probability they are all occupied is negligible.

Such system receives connection requests according to a Poisson process with rate $\lambda = 100$ calls per hour, and the duration of each call is exponential with mean 6 minutes. Let $X(t)$ be the number of occupied channels at time $t$.

### (a) Compute the average of $X(t)$ at $t = 6, 10$ minutes and for $t = \infty$.

$$
\lambda = \int_0^t [1-6(2)] dz = \lambda \int_0^t e^{-\lambda t} = \lambda (1-e^{-\lambda t}) = \begin{cases} 10(1-e^{-\frac{10}{10}}) t = 6 \\ 10(1-e^{-\frac{10}{10}}) t = 10 \end{cases}
$$

### (b) Compute $P[X(t) = 10]$ for $t = 6$ and $t = \infty$.

Very important: using the values from the previous point

$$
P[X(t) = 10] = \frac{\lambda^{20} e^{-\lambda}}{10} = \begin{cases} 0.05 & t = 6 \\ 0.102 & t = 10 \\ 0.125 & t = \infty \end{cases}
$$

---

<!-- Pagina 26 -->

## E1. Consider a Markov chain $X_n$, with states 1, 2 and 3. $x(0) = 3$ and transition matrix

$$
P = \begin{pmatrix}
0.5 & 0.3 & 0.2 \\
0.2 & 0.2 & 0.6 \\
1 & 0 & 0
\end{pmatrix}
$$

### (a) Compute the steady-state probability and the average recurrence time of all states.

The question is asking for $\pi$ and $\theta_{11}, \theta_{22}, \theta_{33}$.

$$
\rightarrow \pi_1 0.5 + \pi_2 0.2 + \pi_3 1 = \pi_1 \quad \pi_1 = \frac{5}{9}
$$

$$
\rightarrow \pi_1 0.3 + \pi_2 0.2 + \pi_3 0 = \pi_2 \quad \pi_2 = \frac{5}{24}
$$

$$
\rightarrow \pi_1 0.2 + \pi_2 0.6 + \pi_3 0 = \pi_3 \quad \pi_3 = \frac{17}{42}
$$

with the basic limit theorem we have

$$
\theta_{11} = m_1 = \frac{1}{\pi_1} = \frac{9}{5}
$$

$$
\theta_{22} = m_2 = \frac{1}{\pi_2} = \frac{24}{5}
$$

$$
\theta_{33} = m_3 = \frac{1}{\pi_3} = \frac{72}{17}
$$

### (b) Compute mean and variance of the first passage time from state 3 to state 1

$$
\theta_{31} = 1 + P_{32} \theta_{21} + P_{33} \theta_{31} = 1
$$

$$
\theta_{12} = 1 + P_{22} \theta_{21} + P_{23} \theta_{31};
$$

Use equation (1) in equation (2).

$$
\theta_{12} = \frac{P_{23}}{1 - P_{22}} = \frac{0.6}{1 - 0.2} = \frac{3}{4}
$$

For the variance we need to compute the second moment $\theta_{22}^2 = 2\theta_{12} - 1 + \sum_{k \neq j} P_{ik} \theta_{kj}$

Then the variance is $\text{var}(\theta_{ij}) = \theta_{22}^2 - (\theta_{ij})^2$

The variance $\text{var}(\theta_{31}) = 0$ since this step is deterministic.

### (c) Compute mean and variance of the first passage time from state 1 to state 3

$$
\begin{cases}
\theta_{13} = 1 + P_{14} \theta_{13} + P_{12} \theta_{23} \\
\theta_{23} = 1 + P_{21} \theta_{13} + P_{22} \theta_{23}
\end{cases} \rightarrow \begin{cases}
-1 = (0.5) \theta_{13} + 0.3 \theta_{23} \quad x = \frac{55}{17}? \\
-1 = 0.2 \theta_{13} + (0.2-1)\theta_{23}
\end{cases}
$$

### (d) Compute $P[x(1) = 1, x(3) = 1 \mid x(2) = 2]$ and $P[x(2) = 2 \mid x(1) = 1, x(3) = 1]$

$$
P[x(1) = 1, x(3) = 1 \mid x(2) = 2] = \frac{P[x(1) = 1, x(2) = 2, x(3) = 1 \mid x(0) = 3]}{P[x(2) = 2 \mid x(0) = 3]} = \frac{P_{31} P_{12} P_{21}}{P_{32}(2)}
$$

$$
P[x(2) = 2 \mid x(1) = 1, x(3) = 1] = \frac{P[x(1) = 1, x(2) = 3, x(3) = 1 \mid x(0) = 3]}{P[x(1) = 1, x(3) = 1 \mid x(0) = 3]} = \frac{P_{31} P_{12} P_{21}}{P_{32}(2)}
$$

---

<!-- Pagina 27 -->

## E. Consider a queue where packets arrive according to a Poisson process with rate $\lambda = 1$ packet per second. All packets in the queue are transmitted when either of the following events occurs: (i) there are two packets in the queue, or (ii) there is one packet in the queue and its waiting time reaches two seconds.

Transmissions is instantaneous, i.e. the queue employs every time there is a packet arrival when one packet is already in the queue, or when the only packet in the queue has been there for enough time.

### (a) Compute the fraction of time which the queue is empty.

The distribution of the first arrival is exponential, $E[\text{empty}] = \frac{1}{e^{\lambda}}$.

After the first arrival we wait until another arrival or up to 2 seconds, then send the distribution is a truncated exponential.

$$
E[\text{busy}] = \int_0^2 e^{-\lambda t} dt = \frac{1-e^{-2\lambda}}{\lambda} = 0.8646
$$

Fraction of time spent empty is $P_{\text{empty}} = \frac{E[\text{empty}]}{E[\text{empty}]+E[\text{busy}]} = 0.536$

### (b) Compute the average delay (i.e. the average time a packet spends in the queue).

If a packet finds the queue non empty, the transmission is immediate. Otherwise, it has to wait $\frac{1-e^{-2\lambda}}{\lambda}$ on average. By the law of total probability, we have:

$$
E[\text{delay}] = E[\text{delay}|\text{empty}]P_{\text{empty}} + E[\text{delay}|\text{busy}]P_{\text{busy}} = (0.864) \times (0.536) = 0.463
$$

## E3. Consider a frequency division transmission system in which the number of channels is so large that the probability they are all occupied is negligible.

Such system receives connection requests according to a Poisson process with rate $\lambda = 100$ calls per hour, and the duration of each call is exponential with mean 6 minutes. Let $X(t)$ be the number of occupied channels at time $t$.

### (a) Compute the average of $X(t)$ at $t = 6, 10$ minutes and for $t = \infty$.

$$
\lambda = \frac{100 \text{ calls}}{60 \text{ min}} = \frac{10}{6} \text{ call/min} = \frac{1}{6}
$$

This scheme is $M/G/\infty$ queue.

Let $X(t)$ be the number of occupied channel at time $t$. $X(t) \sim P(\lambda)$

$$
E[X(t)] = \lambda, \text{ where } \lambda = \lambda \int_0^t [1-G(z)] dz = \lambda \int_0^t e^{-\lambda t} = \frac{\lambda}{\mu} (1-e^{-\mu t}) = \begin{cases} 10(1-e^{-2\lambda}) t = 6 \\ 10(1-e^{-10\lambda}) t = 10 \end{cases}
$$

### (b) Compute $P[X(t) = 10]$ for $t = 6$ and $t = \infty$.

$$
P[X(t) = 10] = \frac{\lambda^{10} e^{-\lambda}}{10} = \begin{cases} 0.05 & t = 6 \\ 0.102 & t = 10 \\ 0.125 & t = \infty \end{cases}
$$

---

<!-- Pagina 28 -->

## E3. Consider two independent Poisson process $X_1(t)$ and $X_2(t)$ where $X_1(t)$ is the number of arrivals for process $t$ during $[0, t]$. The average number of arrivals per unit of time of the 2 process is $\lambda_1 = 0.5$ and $\lambda_2 = 1$ respectively.

### (a) Compute $P[X_1(3) = 1 \mid X_2(3) + X_2(5) = 3]$ and $P[X_1(3) + X_2(3) = 3 \mid X_2(3) + X_2(1)]$ with $X(t)$ as the sum of the 2 processes.

$$
P[X_1(3) = 3 \mid X_2(3) = 3] = \left(\frac{3}{1}\right)\left(\frac{3\lambda_1}{3(\lambda_1 + \lambda_2)}\right)^1 \left(1 - \frac{3\lambda_1}{3(\lambda_1 + \lambda_2)}\right)^3 - 1 = \frac{4}{9}
$$

$$
P[X(3) = 3 \mid X_1(3) = 1] = P[X_2(3) = 2] = \frac{e^{-3\lambda_2}(3\lambda_2)^2}{21} = 0.224
$$

### (b) Compute $P[X_1(2) = 3 \mid X_2(3) = 3]$ and $P[X_1(3) = 3 \mid X_2(2) = 1]$.

$$
P[X_1(2) = 3 \mid X_2(3) = 3] = \left(\frac{3}{1}\right)\left(\frac{2\lambda_1}{3(\lambda_1 + \lambda_2)}\right)\left(1 - \frac{2\lambda_1}{3(\lambda_1 + \lambda_2)}\right)^3 - 1 = \frac{2}{9}
$$

$$
P[X_1(3) = 3 \mid X_2(2) = 1] = \frac{e^{-3\lambda_1 - 2\lambda_2}(3\lambda_1 - 2\lambda_2)^2}{21} = 0.0758
$$

$$
P[X(3) = 3 \mid X_1(2) = 1] = P\left(X_1(1) + X_2(3) = 2\right)\left(X_1(3) - X_1(2)\right).
$$

## E4. Consider a two state Markov channel with transition probabilities 0.98 (from the good state to itself) and 0.1 (from the bad state to the good state). The packet error probability is 1 for a bad slot and 0 for a good slot respectively.

### (a) Compute the throughput (average number of successes per slot) of a protocol that transmits packets directly on the channel, with no retransmissions.

Transition matrix $P = \begin{bmatrix} 0.98 & 0.02 \\ 0.1 & 0.9 \end{bmatrix}$

$$
R = \begin{bmatrix} R_6 \\ R_8 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}
$$

$$
T = \begin{bmatrix} T_6 \\ T_8 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
$$

$$
\frac{\sum_i \pi_i R_i}{\sum_i \pi_i T_i} = \frac{\pi_6}{\pi_6 + \pi_0}
$$

$$
\frac{P_{10}}{P_{10} + P_{01}} = \frac{0.1}{0.1 + 0.02} = 0.833
$$

### (b) Compute the throughput of a Go-Back-N protocol if the round-trip time is $m = 2$ slots (i.e., a packet that is erroneous in slot $t$ is retransmitted in slot $t + 2$), in the presence of an error-free feedback scheme.

$$
P^2 = \begin{bmatrix} 0.9624 & 0.376 \\ 0.188 & 0.812 \end{bmatrix}
$$

Protocol matrix $C = \begin{bmatrix} P_{00} & P_{01} \\ P_{10} & P_{11} \end{bmatrix}$

$$
m = 2 \Rightarrow \begin{bmatrix} 0.98 & 0.02 \\ 0.188 & 0.812 \end{bmatrix}
$$

$$
\frac{T}{T_0} = \frac{P_{10}^{(m)}}{P_{10}^{(m)} + mP_{01}} = \frac{0.188}{0.188 + (2)(0.02)} = 0.8245
$$

---

<!-- Pagina 29 -->

### (c) Same as in the previous point, with the difference that now the feedback channel is subject to i.i.d. errors with probability 0.1.

$$
\tau = \frac{(1-\delta)P_{10}^{(m)}}{(1-\delta)P_{30}^{(m)} + m((1-\delta)P_{01} + \delta P_{01}^{(m)} + \delta P_{10}^{(m)})}
$$

# 05/09/2007

Consider now a system where a channel behavior as in point (a) (Markov model for the forward channel and error-free feedback channel) alternates with a channel behavior in which the forward channel is subject to i.i.d. errors with probability $\varepsilon = 0.01$. In particular the channel follows the Markov model for a geometric number of slots with mean 2000000 slots, then again the Markov model and so on. Compute the overall average throughput of the Go-Back-N protocol in this case.

we can model the system as an alternating process in the first phase we have a Markov behavior while in the second one we have the forward i.i.d. errors behavior.

$$
\tau_{\text{iid}} = \frac{1-\varepsilon}{1-\varepsilon + m\varepsilon} = 0.98
$$

$$
\tau = \tau_{Markov} \frac{EC Markov behavior}{E Cycle duration} + \tau_{\text{iid}} \frac{EC IID behavior}{E Cycle duration}
$$

$$
= \frac{\tau_{Markov}}{Previous} \frac{1}{3} + \frac{\tau_{\text{iid}}}{New} \frac{2}{3} = \frac{1}{3} 0.825 + \frac{2}{3} 0.98 = 0.928
$$

---

<!-- Pagina 30 -->

## T3. Prove that a Markov chain with a finite number of states can’t have any null recurrent state.

Null recurrent class
1: this class is MC
2: this class is finite

State space, finite

Suppose there is one no recurrent state, and then we find the class where this one recurrent state belongs. All the states in that class will be no recurrent, (because transitivity is class property).

Note: a recurrent class is Markov chain by itself, because if start in a recurrent class, I never leave. Not the same with transient class that will be left at some point.

Contradiction we find a Markov chain with finite states with no positive recurrent states on this violates the following result which says:
In a finite Markov chain we must have a positive recurrent state, at least one.

Proof by contradiction: No positive recurrent state.

Then $\sum_{j=1}^{N} P_{ij}^{(n)} = 1 \forall i, \forall n$.

In the limits to infinity

$$
1 = \lim_{n \to \infty} \sum_{j=1}^{N} P_{ij}^{(n)} \quad \text{since, the number of states is finite, then we can write}
$$

$$
1 = \sum_{j=1}^{N} \lim_{n \to \infty} P_{ij}^{(n)} \quad \text{given the assumption there are not positive recurrent states, all these limits are = 0.}
$$

Because the limit is positive only for recurrent states

$$
1 \neq 0 \quad \text{Contradiction}
$$

---

<!-- Pagina 31 -->

# 12/12/2006

## T1. State and prove the elementary renewal theorem

*Page. 107 ROSS*  NOT SEEN IN CLASS (THE PROOF) WAS
SAID AS OPTIONAL

Ross 3.8 theorem 2nd edition

$$
\lim_{t \to \infty} \frac{m(t)}{t} \to \frac{1}{\mu}
$$

**Proof:**
Suppose $\mu < \infty$

$$
SN(t) + 1 \ge \epsilon
$$

By the corollary

$$
E[SN(t) + 1] = \mu(1 + M(t))
$$

then

$$
\mu(m(t) + 1) \ge \epsilon
$$

On the limit

$$
\lim_{t \to \infty} \frac{m(t)}{t} \ge \frac{1}{\mu}
$$

You need to prove this
that is another question
in the exam, so you only
said is already proved.
Otherwise, write it
at the end.

---

<!-- Pagina 32 -->

# 05/09/2007

## T3. Prove that for a Markov chain the n-step transition probabilities,

$$
P_{ij}^{(n)} \text{ satisfy the relationship}
P_{ij}^{(n)} = \sum P_{im}^{(k)} P_{mj}^{(n-k)}, \quad k=0, 1, \dots, n
$$

For a generic $K$

$$
P_{ij}^{(n)} = P[X_n = j | X_0 = i] = \sum_{m}^{\infty} P[X_n = j, X_k = m | X_0 = i]
$$

$$
= \sum_{m} P[X_n = j | X_k = m], X_0 = i] P[X_k = m | X_0 = i]
$$

$$
= \sum_{m} P[X_n = j | X_k = m] P[X_k = m | X_0 = i]
$$

$$
= \sum_{m} P_{im}^{(k)} P_{mj}^{(n-k)}
$$

---

<!-- Pagina 33 -->

## T3. For a renewal process state precisely (with proof) the value of:

Ross book 2nd Edition Page 102 Position 3.3.1 or class 18

$$
\lim_{t \to \infty} \frac{N(t)}{t} = \frac{1}{\mu} \text{ w.p. 1.}
$$

Proof since $S_{N(t)} \leq t \leq S_{N(t)+1}$, we see that

$$
\frac{S_{N(t)}}{N(t)} \leq \frac{1}{N(t)} < \frac{S_{N(t)+1}}{N(t)}
$$

However since

$$
\frac{S_{N(t)}}{N(t)}
$$

is the average of the first $N(f)$ interarrivals time, it follows by the strong law of large numbers that

$$
\frac{S_{N(t)}}{N(t)} \to \mu \text{ as } N(t) \to \infty
$$

where $N(t) \to \infty$ when $t \to \infty$ then:

$$
\lim_{t \to \infty} \frac{S_{N(t)}}{N(t)} \to \mu
$$

Furthermore

$$
\frac{S_{N(t)+1}}{N(t)} = \left[ \frac{S_{N(t)+1}}{N(t)+1} \right] \left[ \frac{N(t)+1}{N(t)} \right]
$$

we have then

$$
\frac{S_{N(t)+1}}{N(t)} \to \mu \text{ as } t \to \infty
$$

Since

$$
\frac{t}{N(t)}
$$

is between 2 numbers, each of which converges to $\mu$ as $t \to \infty$

then

$$
\lim_{t \to \infty} \frac{t}{N(t)} = \mu \to \lim_{t \to \infty} \frac{N(t)}{t} = \frac{1}{\mu}
$$

## T2. If $i < j$ and if $i$ is recurrent, then $j$ is recurrent.

class 9 or corollary 3.1 (Samuel Karlin 3rd edition page 242)

Since $i < j$, there exists $m, n \geq 1$ such that $P_{ij}^{(n)} > 0$ and $P_{ji}^{(m)} > 0$

Let $k > 0$

$$
\sum_{k=0}^{\infty} P_{jj}^{(m+n+k)} \geq \sum_{k=0}^{\infty} P_{ji}^{(m)} P_{ii}^{(k)} P_{ij}^{(n)}
$$

Both must be explained.

Both must be explained.

Hence $i$ is recurrent

$$
\sum_{k=0}^{\infty} P_{ii}^{(k)} = +\infty
$$

also needs proof.

that implies

$$
\sum_{k=0}^{\infty} P_{jj}^{(k)} = +\infty
$$

; this implies that $j$ is recurrent

---

<!-- Pagina 34 -->

## T2. For a Poisson process $X(t)$ of rate $\lambda$, state and derive the expression of $P[X(0) = k \mid X(t) = n]$ for the 2 cases

(i) $0 < t < 0, 0 \leq k \leq n$

$$
P \{X(0) = k \mid X(t) = n\} = \frac{P \{X(0) = k, X(t) = n\}}{P \{X(t) = n\}}
$$

$$
= P \{X(0) = k, X(t) - X(0) = n - k\}
$$

$$
= \frac{e^{-\lambda t} (\lambda t)^k / k!}{e^{-\lambda t} (\lambda t)^n / n!}
$$

$$
= \frac{n!}{k!(n - k)!} \frac{o^k (t - 0)^{n - k}}{t^n}
$$

(ii) $0 < t < 0, 0 \leq n \leq k$

$$
P[X(0) = k \mid X(t) = n] =
$$

$$
\frac{P[X(0) = k, X(t) = n]}{P[X(t) = n]} = \frac{P[X(t) = n, X(0) - X(t) = k - n]}{P[X(t) = n]}
$$

By independent interarrivals

$$
\frac{P[X(t) = n] P[X(s) - X(t) = k - n]}{P[X(t) = n]} = \frac{e^{-\lambda (0 - t)} (\lambda (0 - t))^{k - n}}{(k - n)!}
$$

---

<!-- Pagina 35 -->

## T3. Prove that for a Poisson process $X(t)$ the statistics of $X(s)$ conditioned on $X(t)$, $s < t$, is binomial and provide the expression of $P[X(s) = k \mid X(t) = n]$

$$
P[X(s) = k \mid X(t) = n] = \binom{n}{k} \left(\frac{s}{t}\right)^k (1 - \frac{s}{t})^{n-k}
$$

Between 0 and $t$ we have arrivals, which are said according to a uniform random variable $U[0, t]$. The probability that each falls in $[0, s]$ is $\frac{s}{t}$. Therefore $X(s)$ can be seen as a binomial random variable with parameters $n, \frac{s}{t}$.

---

<!-- Pagina 36 -->

## T1. For a Poisson process of rate $\lambda$, prove that the interarrival times are i.i.d. with mean $\lambda$

Ross book Interim and waiting distribution

If $X_n$ is denote as the time from $n-1$ s$^+$ to the $n$th event, the sequence $\{X_n, n=1, 2, \ldots\}$ is the sequence of interarrival times.

Note that

$$
P\{X_3 > t\} = P\{N(t) = 0\} = e^{-\lambda t}
$$

$X_1$ has an exponential distribution with mean $\lambda$.

$$
P\{X_2 > t\} = E[P\{X_2 > t|X_1\}]
$$

But

$$
P\{X_2 > t|X_1 = s\} = P\{0 \text{ events in } (S, s+t] | X_1 = s)
$$

$$
= P\{0 \text{ events in } (S, s+t]\}
$$

$$
= c\lambda t
$$

The previous equations followed from independent and stationary increments.

From equation (4), we conclude $X_2$ is an exponential r.v. with mean $\lambda$ and $X_2$ is independent of $X_1$.

## T2. State precisely and formally prove the result that establishes that in a Markov chain the period is a class property.

Class 8, Ross Book pag. 66 2nd edition

if $i < j$, then $d(i) = d(j)$.

Assume $i < j$ communicates, then exists $(m, n)$ such that $P_{ji} > 0$ $P_{ji}^{(m)} > 0$ Very important

Then

$$
P_{jj}^{(m+n)} \ge P_{ji}^{(n)} \cdot P_{ij}^{(m)} > 0
$$

strictly positive

Let se $\{n \ge 1 : P_{ii}^{(n)} > 0\}$ state why inequality

$$
P_{jj}^{(m+s+n)} \ge P_{ji}^{(n)} \cdot P_{ii}^{(s)} P_{ji}^{(m)} > 0
$$

Careful, in theory professors

can be deadly precise.

You could lose points just for not explaining why you use an inequality.

Similar way can be proved that $d(i)$ divides $d(j)$ then $d(i) = d(j)$

recommended to prove it

---

<!-- Pagina 37 -->

# 14/07/2006

## T1. Similar as 13/07/21 T1

## T2. Prove that in a Markov chain the period is a class property.

Same as T2 13/07/21

## T3. Prove that for a renewal process $E[S_{N(t)+1}] = E[x](M(t)+1)$

we know the renewal equation $A(t) = a(t) + \int_{0}^{t} A(t-x) dF(x)$ if $a(t)$ is bounded, the solution of that equation is

$$
A(t) = a(t) + \int_{0}^{t} a(t-x) dM(x)
$$

Let's suppose $A(t) = E[S_{N(t)+1}]$
we can derive $E[S_{N(t)+1}|X_1=x] = \begin{cases} x & \text{if } x > t \\ x + A(t-x) & \text{if } x \leq t \end{cases}$

$$
A(t) = E[S_{N(t)+1}] = \int_{0}^{\infty} E[S_{N(t)+1}|X_1=x] dF(x)
$$

$$
= \int_{0}^{\infty} x dF(x) + \int_{0}^{t} x + A(t-x) dF(x) = \int_{0}^{\infty} x dF(x) + \int_{0}^{t} A(t-x) dF(x)
$$

If $E[x]$ is bounded $E[S_{N(t)+1}] = A(t) = E[x] + \int_{0}^{t} E[x] dM(x)$

$$
= E[x] (1 + \int_{0}^{t} dM(x))
$$

$$
= E[x] (1 + M(t))
$$
