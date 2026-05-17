# How To Stochastic Processes

Transcription from `How To Stochastic Processes _240630_183444 (1).pdf`.

Some hand-written values are kept exactly as visible. Ambiguous parts are marked as
`unclear`.

## Markov chain

### Example: steady state and average recurrence time

Given:

$$
P =
\begin{pmatrix}
0.5 & 0.3 & 0.2 \\
0.2 & 0.2 & 0.6 \\
1 & 0 & 0
\end{pmatrix},
\qquad X(0)=3.
$$

First draw the graph with the given probabilities:

- State 1:
  - $1 \to 1$ with probability $0.5$
  - $1 \to 2$ with probability $0.3$
  - $1 \to 3$ with probability $0.2$
- State 2:
  - $2 \to 1$ with probability $0.2$
  - $2 \to 2$ with probability $0.2$
  - $2 \to 3$ with probability $0.6$
- State 3:
  - $3 \to 1$ with probability $1$

The steady-state vector is obtained from:

$$
\pi = \pi P.
$$

That gives:

$$
\begin{cases}
\pi_2 = 0.3\pi_1 + 0.2\pi_2, \\
\pi_3 = 0.2\pi_1 + 0.6\pi_2, \\
\pi_1 + \pi_2 + \pi_3 = 1.
\end{cases}
$$

Solution:

$$
\pi_1 = \frac{5}{9},
\qquad
\pi_2 = \frac{5}{24},
\qquad
\pi_3 = \frac{17}{72}.
$$

Average recurrence times:

$$
\theta_{11}=m_1=\frac{1}{\pi_1}=\frac{9}{5},
$$

$$
\theta_{22}=m_2=\frac{1}{\pi_2}=\frac{24}{5},
$$

$$
\theta_{33}=m_3=\frac{1}{\pi_3}=\frac{72}{17}.
$$

### Mean and variance of first passage times

For $i \ne j$:

$$
\theta_{ij} = 1 + \sum_{k \ne j} p_{ik}\theta_{kj}.
$$

Example for first passage from $3$ to $1$:

$$
\begin{cases}
\theta_{31}=1+p_{32}\theta_{21}+p_{33}\theta_{31}, \\
\theta_{21}=1+p_{22}\theta_{21}+p_{23}\theta_{31}.
\end{cases}
$$

For the second moment / variance:

$$
\overline{\theta^2}_{ij}
= 2\theta_{ij}-1+\sum_{k \ne j}p_{ik}(1+\theta_{kj}),
$$

and:

$$
\operatorname{Var}(\theta_{ij})
= \overline{\theta^2}_{ij}-(\theta_{ij})^2.
$$

### Conditional probability on a trajectory

Example:

$$
P[X(1)=1,\ X(3)=1 \mid X(2)=2],
$$

with start:

$$
X(0)=3.
$$

Numerator path:

| $t$ | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| state | 3 | 1 | 2 | 1 |

Numerator:

$$
p_{31}p_{12}p_{21}.
$$

Denominator:

$$
p^{(2)}_{32}.
$$

Therefore:

$$
P[X(1)=1,\ X(3)=1 \mid X(2)=2]
=
\frac{p_{31}p_{12}p_{21}}{p^{(2)}_{32}}.
$$

Second example:

$$
P[X(2)=2 \mid X(1)=1,\ X(3)=1].
$$

Numerator:

$$
p_{31}p_{12}p_{21}.
$$

Denominator:

$$
p_{31}p^{(2)}_{11}.
$$

Therefore:

$$
P[X(2)=2 \mid X(1)=1,\ X(3)=1]
=
\frac{p_{31}p_{12}p_{21}}{p_{31}p^{(2)}_{11}}.
$$

### Example: transition diagram and $X_1$, $X_2$

Exercise type: draw the transition diagram and find $X_1$, $X_2$, $X_{500}$, given $X_0=0$.

The first-step distribution is:

$$
X_1 = (0.2,\ 0.4,\ 0.4).
$$

The second-step distribution is:

$$
X_2 = X_1P
= (0.4,\ 0.44,\ 0.16).
$$

For large $n$:

$$
X_{500} = \pi = \pi P.
$$

### Average first passage times from state 0

Exercise type: compute the average first passage times from $0$ to $0,1,2$.

General formula:

$$
\theta_{ij}=1+\sum_{k\ne j}p_{ik}\theta_{kj}.
$$

Exercise type: let $W_{ij}^{(m)}$ be the expected number of visits to $j$ by time $m$.
Compute $W_{0j}^{(3)}$ for $j=0,1,2$.

Initial matrix:

$$
P^0 =
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
= I.
$$

One-step matrix:

$$
P =
\begin{pmatrix}
0.2 & 0.4 & 0.4 \\
0.5 & 0.5 & 0 \\
0.4 & 0.4 & 0.2
\end{pmatrix}.
$$

Two-step matrix:

$$
P^2 =
\begin{pmatrix}
0.4 & 0.44 & 0.16 \\
0.35 & 0.45 & 0.2 \\
0.36 & 0.44 & 0.2
\end{pmatrix}.
$$

In general:

$$
W_{ij}^{(m)}=\sum_{\ell=0}^{m}p_{ij}^{(\ell)}.
$$

For $m=3$ as written in the notes:

$$
W_{0j}^{(3)}
= p_{0j}^{(0)}+p_{0j}^{(1)}+p_{0j}^{(2)}
=
\begin{pmatrix}
1.6 \\
0.84 \\
0.56
\end{pmatrix}.
$$

Equivalently:

$$
\begin{cases}
j=0: & 1+0.2+0.4, \\
j=1: & 0+0.4+0.44, \\
j=2: & 0+0.4+0.16.
\end{cases}
$$

For large $m$:

$$
W_{0j}^{(5000)}
\simeq W_{0j}^{(\infty)}
\simeq 5000\pi_j.
$$

Using:

$$
\pi =
\left(
\frac{10}{27},
\frac{4}{9},
\frac{5}{27}
\right),
$$

the notes give:

$$
W_{0j}^{(5000)}
\simeq
\begin{pmatrix}
\frac{10}{27}\cdot 5000 \\
\frac{4}{9}\cdot 5000 \\
\frac{5}{27}\cdot 5000
\end{pmatrix}
=
\begin{pmatrix}
1852 \\
2222 \\
926
\end{pmatrix}.
$$

### Case with an absorbing state

If one state is absorbing:

$$
\lim_{m\to \infty}W_{0j}^{(m)}
\simeq
\begin{cases}
\star, & j=0, \\
\star, & j=1, \\
\infty, & j=2 \text{ absorbing}.
\end{cases}
$$

Example matrix:

$$
P =
\begin{pmatrix}
0.2 & 0.6 & 0.2 \\
0.6 & 0.2 & 0.2 \\
0 & 0 & 1
\end{pmatrix}.
$$

For:

$$
W_{ij}=\lim_{m\to\infty}W_{ij}^{(m)},
$$

the recurrence is:

$$
W_{ij}=\delta_{ij}+p_{i0}W_{0j}+p_{i1}W_{1j}.
$$

For $i=0,1$:

$$
\begin{cases}
W_{00}=0.2W_{00}+0.6W_{10}+1, \\
W_{10}=0.6W_{00}+0.2W_{10}.
\end{cases}
$$

Solution:

$$
W_{00}=\frac{20}{7},
\qquad
W_{10}=\frac{15}{7}.
$$

By symmetry:

$$
W_{11}=\frac{20}{7},
\qquad
W_{01}=\frac{15}{7}.
$$

Average time before absorption, with $X_0=0$:

$$
E[\text{absorption time}\mid X_0=0]
= W_{00}+W_{01}
= \frac{35}{7}=5.
$$

The same result can also be obtained from:

$$
V_i=1+p_{i0}V_0+p_{i1}V_1.
$$

That is:

$$
\begin{cases}
V_0=1+p_{00}V_0+p_{01}V_1=5, \\
V_1=1+p_{10}V_0+p_{11}V_1=5.
\end{cases}
$$

### Big Markov chain example

Exercise type: big Markov chain example.

Matrix shown in the notes:

$$
P =
\begin{pmatrix}
0 & 0 & 0 & 1 & 0 \\
0 & 0.4 & 0 & 0 & 0.6 \\
0 & 0 & 0.5 & 0.2 & 0.3 \\
1 & 0 & 0 & 0 & 0 \\
0 & 0.3 & 0 & 0 & 0.7
\end{pmatrix}.
$$

Classes:

- $A$: positive recurrent periodic class, period $d=2$.
- $B$: transient class.
- $C$: positive recurrent aperiodic class.

It always has this structure.

Probability of absorption:

$$
\pi_2(A)=\frac{2}{5},
\qquad
\pi_2(C)=\frac{3}{5}.
$$

Exercise type: compute

$$
\lim_{m\to\infty}\frac{1}{m}\sum_{k=0}^{m-1}P^k.
$$

The limiting average matrix written in the notes is:

$$
\lim_{m\to\infty}\frac{1}{m}\sum_{k=0}^{m-1}P^k
=
\begin{pmatrix}
\frac12 & 0 & 0 & \frac12 & 0 \\
0 & \frac13 & 0 & 0 & \frac23 \\
\frac15 & \frac15 & 0 & \frac15 & \frac25 \\
\frac12 & 0 & 0 & \frac12 & 0 \\
0 & \frac13 & 0 & 0 & \frac23
\end{pmatrix}.
$$

In the handwritten note: the $x$ in $\lim_{m\to\infty}P^m$ is counted as $x$
because of periodicity.

For the closed class $C=\{1,4\}$:

$$
\pi_1,\pi_4
\quad\Rightarrow\quad
\pi_j=\sum_{i\in C}\pi_i p_{ij},
\qquad j\in C.
$$

Equations:

$$
\begin{cases}
\pi_1 = \pi_1p_{11}+\pi_4p_{41}, \\
\pi_4 = \pi_1p_{14}+\pi_4p_{44}, \\
\pi_1+\pi_4=1.
\end{cases}
$$

In numbers:

$$
\begin{cases}
\pi_1=0.4\pi_1+0.3\pi_4, \\
\pi_4=0.6\pi_1+0.7\pi_4.
\end{cases}
$$

Solution:

$$
\pi_1=\frac13,
\qquad
\pi_4=\frac23.
$$

Absorption-weighted probabilities:

$$
\pi_{21}=\frac35\cdot\frac13,
\qquad
\pi_{24}=\frac35\cdot\frac23.
$$

Exercise type: any state to $4$ first passage time in the big Markov chain.

Any state that does not have a path to $4$ has infinite first-passage time. For
the others:

$$
m_{i4}=
\left[
\infty,\ \frac{1}{1-0.4},\ \infty,\ \infty,\ \frac{1}{\pi_4}
\right]
=
\left[
\infty,\ \frac53,\ \infty,\ \infty,\ \frac32
\right].
$$

It can also be calculated as:

$$
\theta_{ij}=1+\sum_{k\ne j}p_{ik}\theta_{kj}.
$$

For state $1$ to $4$:

$$
V_{14}=1+p_{11}V_{14}+p_{14}\cdot 0
\quad\Rightarrow\quad
V_{14}=\frac{1}{1-p_{11}}=\frac53.
$$

For state $4$:

$$
V_{44}=1+\frac53\cdot\frac{3}{10}=1.5.
$$

## Go-Back-N

Exercise type: transition probabilities are all given, with $m$.

Example with $m=2$.

First draw the diagram. States:

- $G$: good state.
- $B$: bad state.

Transition matrix:

$$
P =
\begin{pmatrix}
0.98 & 0.02 \\
0.1 & 0.9
\end{pmatrix}.
$$

Two-step transition matrix:

$$
P^2 =
\begin{pmatrix}
0.9624 & 0.0376 \\
0.188 & 0.812
\end{pmatrix}.
$$

Exercise type: error-free throughput.

$$
\mu =
\frac{p_{10}^{(2)}}{p_{10}^{(2)}+2p_{01}}
\simeq 824.56\cdot 10^{-3}.
$$

Exercise type: i.i.d. error with probability $\delta$, e.g. $\delta=0.1$.

The notes give:

$$
\mu =
\frac{(1-\delta)p_{10}^{(m)}}
{(1-\delta+m\delta)p_{10}^{(m)}
+m\left[(1-\delta)p_{01}+\delta p_{01}^{(m)}\right]}.
$$

Exercise type: channel that alternates between:

- First: $1,000,000$ slots, Markov.
- Second: $2,000,000$ slots, i.i.d.

Given:

$$
\varepsilon = 0.01.
$$

i.i.d. throughput:

$$
T_{\text{i.i.d.}}
=
\frac{1-\varepsilon}{1-\varepsilon+m\varepsilon}
\simeq 0.98.
$$

Markov throughput:

$$
T_{\text{Markov}}=\mu_{\text{error-free}}.
$$

Final average:

$$
\mu_{\text{final}}
=\frac13T_{\text{Markov}}+\frac23T_{\text{i.i.d.}}
=0.928.
$$

### Consecutive slots example

Exercise type: data given in consecutive slots.

Given in the notes:

$$
p_B=\pi_1=0.02,
\qquad
p_{01}=\frac{1}{100}=0.01,
\qquad
m=2.
$$

Question:

$$
p_{10}=?
$$

Using:

$$
\pi_1=\frac{p_{01}}{p_{01}+p_{10}},
$$

we obtain:

$$
(p_{10}+p_{01})\pi_1=p_{01}
\quad\Rightarrow\quad
p_{10}\pi_1+p_{01}\pi_1=p_{01}.
$$

Therefore:

$$
p_{10}=\frac{p_{01}(1-\pi_1)}{\pi_1}=0.49.
$$

Also:

$$
p_{11}=0.51.
$$

The graph can now be drawn:

- $G \to G$: $0.99$
- $G \to B$: $0.01$
- $B \to G$: $0.49$
- $B \to B$: $0.51$

Exercise type: transition in the channel without any protocol.

No protocol throughput:

$$
\pi_0=\frac{p_{10}}{p_{10}+p_{01}}\simeq 0.98.
$$

## Poisson processes

State:

$$
t,\qquad 0\le k\le m.
$$

More than one condition may be present.

### Single Poisson process conditioned on the count at a later time

Example:

$$
P[X(\mu)=k \mid X(t)=m].
$$

Formula:

$$
P[X(\mu)=k \mid X(t)=m]
=
\binom{m}{k}
\left(\frac{\mu}{t}\right)^k
\left(1-\frac{\mu}{t}\right)^{m-k},
$$

with:

$$
0<\mu<t,
\qquad
0\le k\le m.
$$

### Two independent Poisson processes

Example:

$$
P[X_1(\mu)=k \mid X_1(t)+X_2(t)=m].
$$

Formula:

$$
P[X_1(\mu)=k \mid X_1(t)+X_2(t)=m]
=
\binom{m}{k}
\left(\frac{d_1\mu}{(d_1+d_2)t}\right)^k
\left(\frac{d_1(t-\mu)+d_2t}{(d_1+d_2)t}\right)^{m-k}.
$$

Exercise type:

$$
P[X_1(t)+X_2(t)=k \mid X_1(\mu)=m],
$$

with:

$$
0\le m\le k.
$$

Same $t$ appears on the left side.

### Example with $d_1=d_2=1$

Given:

$$
d_1=1,
\qquad
d_2=1.
$$

Example:

$$
P[X_1(2)+X_2(2)=4 \mid X_1(1)=1].
$$

Equivalent event:

$$
P[X_1(2)+X_2(2)-X_1(1)=3].
$$

The notes highlight that terms cancel out, giving the parameter:

$$
(d_1+d_2)t-d_1\mu = 2\cdot 2 - 1\cdot 1 = 3.
$$

Thus:

$$
P[X_1(2)+X_2(2)-X_1(1)=3]
=
e^{-3}\frac{3^3}{3!}.
$$

### Conditional examples

Example:

$$
P[X_2(1)=2 \mid X_1(1)+X_2(1)=2,\ X_1(2)=0].
$$

The note simplifies this to:

$$
P[X_2(1)=2]
=
e^{-1}\frac{1^2}{2!}.
$$

Example:

$$
P[X_1(1)+X_2(1)=2 \mid X_1(2)=1].
$$

There are two cases. Up to time $t$, $X_1$ has one arrival. The $X_1$ arrival can
occur either in $(0,1]$ or in $(1,2]$, each with probability $1/2$.

Therefore:

$$
(0,1]\Rightarrow X_1(1)=1,\ X_1(2)=0
\quad\Rightarrow\quad \frac12 \text{ probability},
$$

$$
(1,2]\Rightarrow X_1(1)=0,\ X_1(2)=1
\quad\Rightarrow\quad \frac12 \text{ probability}.
$$

Finally:

$$
P[X_2(1)=1]\cdot\frac12
+P[X_2(1)=2]\cdot\frac12
=0.27.
$$

Example:

$$
P[X_1(\mu)=k \mid X_2(t)=m],
\qquad
0<t<\mu,
\qquad
0\le m\le k.
$$

Example:

$$
P[X_1(3)=3 \mid X_1(2)=1].
$$

Equivalent:

$$
P[X_1(3)-X_1(2)=2].
$$

The notes indicate checking only $X_1$:

$$
d_1=0.5,
\qquad
d_2=1,
$$

and:

$$
(d_1+d_2)t-d_1\mu=\frac32-1=\frac12.
$$

### Poisson calculations: visitors

Exercise type: exhibition with visitor arrival rate.

Given:

$$
\lambda = 10/\text{h}.
$$

Time spent:

$$
Y\sim U[20,30]\ \text{min}.
$$

Open from 8 AM to 6 PM.

#### Fewer than three visitors during the first half hour

Question:

> Compute the probability that fewer than three visitors arrive during the first
> half hour.

For a half hour:

$$
\lambda t = 10\cdot \frac12 = 5.
$$

Therefore:

$$
P[X(0.5)<3]
=
\sum_{k=0}^{2}P[X(0.5)=k]
$$

$$
=
e^{-5}\frac{5^0}{0!}
+e^{-5}\frac{5^1}{1!}
+e^{-5}\frac{5^2}{2!}
\simeq 0.125.
$$

#### One visitor in the room at 8:15 AM

Question:

> Compute the probability that at 8:15 AM there is only one visitor in the room.

At 8:15:

$$
t=\frac14\text{ h}.
$$

The notes write:

$$
P[X(1/4)=1]
=
e^{-5/2}\frac{(5/2)^1}{1!}
=0.205.
$$

Usually:

$$
P[N(t)=m]
=
e^{-\lambda pt}
\frac{(\lambda pt)^m}{m!},
$$

where:

$$
\lambda pt
=
\lambda\int_0^t [1-G(z)]\,dz.
$$

#### Empty room at closing time

Question:

> Compute the probability that at closing time (6 PM) the room is empty.

The notes use:

$$
d=100/\text{h}
\quad\text{(as written)}
$$

and:

$$
U[20\text{ min},30\text{ min}]
=
\left[\frac13,\frac12\right]\text{ h}.
$$

Average:

$$
E[Y]
=
\frac{\frac12+\frac13}{2}
=
\frac{5}{12}
=
\frac{25}{60}.
$$

Thus:

$$
E[N(t)]
= dE[Y]
= 10\cdot\frac{5}{12}
=\frac{25}{6}.
$$

Since:

$$
t=10\text{ h} > U[20,30],
$$

the system is in steady state. Therefore:

$$
P[N(t)=0]
=
e^{-25/6}\frac{(25/6)^0}{0!}
=0.015.
$$

### Network with two incoming links

Exercise type: network with two incoming links.

Given:

$$
d_1=d_2=500\ \text{packets/s}.
$$

Exercise:

> Compute the probability that in a $3$ ms interval the node receives two packets
> from the first link and one from the second.

Compute:

$$
dt = 500\cdot 0.003 = 1.5.
$$

Since the two links are independent:

$$
P[X_1(3\text{ ms})=2 + X_2(3\text{ ms})=1]
$$

$$
=
e^{-1.5}\frac{1.5^2}{2!}
\cdot
e^{-1.5}\frac{1.5^1}{1!}
\simeq 0.084.
$$

Exercise:

> Compute the probability that in a $3$ ms interval the node receives three
> packets in total.

Total rate:

$$
d=d_1+d_2=1000.
$$

Then:

$$
dt = 1000\cdot 0.003 = 3.
$$

Therefore:

$$
P[X(3\text{ ms})=3]
=
e^{-3}\frac{3^3}{3!}
\simeq 0.224.
$$

Exercise:

> Compute the probability that in a $3$ ms interval the node receives two packets
> from the first link, given that it received three packets in total.

Question:

$$
P[X_1(3\text{ ms})=2 \mid X_2(3\text{ ms})=3].
$$

Classic formula:

$$
\binom{3}{2}
\left(\frac12\right)^2
\left(\frac12\right)^{3-2}
=
\frac38.
$$

### Web server with received download request

Exercise type: web server with received download request.

Given:

$$
\lambda = 20/\text{s}.
$$

File size:

$$
U=\{1,2\}\ \text{MB}.
$$

Service rate:

$$
\mu = 100\ \text{Mbps}.
$$

Fixed component:

$$
20\text{ ms}.
$$

Minimum service time:

$$
\frac{1\text{ MB}\cdot 8}{100\text{ Mbps}}+20\text{ ms}
=100\text{ ms}.
$$

Maximum service time:

$$
\frac{2\text{ MB}\cdot 8}{100\text{ Mbps}}+20\text{ ms}
=180\text{ ms}.
$$

Steady-state average:

$$
\frac{100+180}{2}=140\text{ ms}.
$$

For steady state:

$$
P[k\text{ active requests in steady state}]
=P[N(t)=k].
$$

Mean:

$$
dE[Y]=20\cdot 0.14 = 2.8.
$$

Answer:

$$
P[N(t)=k]
=
e^{-2.8}\frac{2.8^k}{k!}.
$$

Question:

> Given that in an interval of duration $T$ the system received $N$ requests,
> find the probability that at the end of such interval there are no active
> requests.

Case:

$$
T=0.1\text{ s},
\qquad
N=2.
$$

The notes mark this as impossible because the minimum service time is $0.1$ s, so
in an interval of $0.1$ s it would not be possible to serve all requests.

Example type: system that receives service requests.

Given:

$$
d=20/\text{s}
=\frac13/\text{min},
\qquad
S.T.=6\text{ min}.
$$

For:

$$
P[N(t)=0]\quad\text{in }30\text{ min},
$$

the notes say it takes $6$ min, so it is the same as having no requests in:

$$
24 \to 30 = 6\text{ min}.
$$

Then:

$$
dt=\frac13\cdot 6=2
\quad\Rightarrow\quad
e^{-2}\frac{2^0}{0!}=e^{-2}.
$$

For an empty system at $t=30$ min given $10$ arrivals in $[0,30]$:

$$
P[N(t)=0 \mid X(t)=10].
$$

Using:

$$
P(S)=\frac{T[\text{empty}]}{T[\text{whole time}]}
=\frac{24}{30}
=\frac45.
$$

Therefore:

$$
P[N(t)=0 \mid X(t)=10]
=
\left(\frac45\right)^{10}.
$$

## Renewal

### Queue emptied by either second packet or timeout

Exercise type:

> Consider a queue where packets arrive according to a Poisson process with rate
> $\lambda=1$ packet per second. All packets in the queue are transmitted when
> either of the following events occurs:
>
> 1. there are two packets in the queue, or
> 2. there is one packet in the queue and its waiting time reaches two seconds.
>
> Transmission is instantaneous.

The queue empties every time:

- there is a packet arrival when one packet is already in the queue, or
- the only packet in the queue has been there long enough.

Exercise type: when is the system empty?

The notes show the renewal cycle:

```text
empty -- first packet arrives -- 1 packet waits -- transmit packets
```

with:

$$
\lambda = 1/\text{s}.
$$

Probability / fraction of time empty:

$$
P[\text{empty}]
=
\frac{E[\text{first arrival}]}{E[\text{cycle}]}
=
\frac{E[F.A.]}{E[F.A.]+E[\text{truncated exponential}]}.
$$

For the truncated exponential up to $2$:

$$
E[\min(A,2)]
=
\int_0^2 e^{-\lambda t}\,dt
=
1-e^{-2}.
$$

Therefore:

$$
P[\text{empty}]
=
\frac{1/\lambda}{1/\lambda+(1-e^{-2})}
=
\frac{1}{1+(1-e^{-2})}
=0.536.
$$

The notes also write:

$$
1-e^{-2}=0.864.
$$

### Average packet delay

Exercise type: average packet delay.

The notes start from:

$$
E[\text{time in queue}]
=
E[\text{time}\mid \text{empty}]P[\text{empty}]
+E[\text{time}\mid \text{not empty}]P[\text{not empty}].
$$

The visible numeric product is:

$$
0.864\cdot 0.536.
$$

### CSMA-like link example

Exercise type:

> Consider a link with capacity $1$ Mbps, shared among many users who collectively
> produce packets according to a Poisson process with rate $\lambda=500$ packets
> per second. All packets have length $1000$ bits. The access protocol is ideal
> CSMA, where a packet generated when the channel is idle gets immediate access,
> whereas a packet that finds the channel busy is rescheduled after an exponential
> time of average $100/\lambda$. If this new attempt again finds a busy channel,
> the protocol keeps trying after random times until success. Assume total traffic
> can be approximated as Poisson with rate $\lambda$.

Question:

$$
\mu ?\quad\text{average traffic handled}
$$

Given:

$$
P_{\text{size}}=1000\text{ b},
\qquad
C=1\text{ Mbps}.
$$

Idle / busy cycle:

$$
\frac{1}{\lambda}
=
\frac{1}{500}
=0.002\text{ s}
=2\text{ ms}.
$$

Transmission time:

$$
T_x=\frac{1000}{1\text{ Mbps}}
=0.001\text{ s}
=1\text{ ms}.
$$

The notes mark:

$$
\text{idle fraction}=\frac23,
\qquad
\text{handling fraction}=\frac13.
$$

The final line is written as:

$$
\mu =
\frac{\frac23}{3\text{ ms}}\cdot 0
+
\frac{\frac13}{3\text{ ms}}\cdot 1\text{ Mbps}
\simeq 933\ \text{Mbps}
$$

as transcribed from the handwritten note. The unit/value looks ambiguous in the
source.

