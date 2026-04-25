# Chapter 2 — Markov Chains

---

## Introduction

A **Markov process** $\{X_t\}$ is a stochastic process satisfying the *Markov property*: given the present state $X_t$, the future states $X_s$ (for $s > t$) are statistically independent of all past states $X_u$ (for $u < t$). Informally, *the present contains all the information needed to predict the future*; the history of how the system arrived at its current state is irrelevant.

A **Markov chain** is a Markov process with:
- **Discrete state space**: $X_t$ takes values in a countable set (usually labelled $\mathbb{N} = \{0, 1, 2, \ldots\}$)
- **Discrete index set**: the parameter $t$ is also countable (usually $t \in \mathbb{N}$, representing discrete time steps)

The Markov property for a chain reads: for any states $i_0, \ldots, i_{n-1}, i, j$ and any time $n$,

$$
\mathbb{P}\{X_{n+1} = j \mid X_0 = i_0, \ldots, X_{n-1} = i_{n-1}, X_n = i\} = \mathbb{P}\{X_{n+1} = j \mid X_n = i\}
$$

Only the current state $X_n = i$ matters; the entire history $(X_0, \ldots, X_{n-1})$ can be discarded.

---

## Transition Probabilities

The **one-step transition probability** is the probability of moving from state $i$ to state $j$ in one step:

$$
P_{ij}^{n,n+1} = \mathbb{P}\{X_{n+1} = j \mid X_n = i\}
$$

If $P_{ij}^{n,n+1} \equiv P_{ij}$ is independent of $n$, the chain is called **homogeneous** (or has *stationary transition probabilities*). We focus on this case, which covers most interesting models.

The transition probabilities form the **transition probability matrix** $\mathbf{P}$, where entry $(i,j)$ is $P_{ij}$. Row $i$ gives the probability distribution over the next state, starting from state $i$:

$$
P_{ij} \geq 0 \quad \forall\, i,j \in \mathbb{N}; \qquad \sum_{j=0}^{+\infty} P_{ij} = 1 \quad \forall\, i \in \mathbb{N}
$$

A matrix with non-negative entries whose rows each sum to 1 is called a **stochastic matrix**.

> **Claim:** The initial distribution $\{p_i = \mathbb{P}(X_0 = i)\}$ and the transition matrix $\mathbf{P}$ fully specify the Markov chain.

**Proof.** A stochastic process is fully specified if we can compute the joint probability of any sequence of states:

$$
\mathbb{P}\{X_0 = i_0, X_1 = i_1, \ldots, X_n = i_n\} \tag{2.1}
$$

Once we have these, we can compute the probability of any event $E$ by summing over all sequences belonging to $E$.

Applying the definition of conditional probability repeatedly:

$$
\mathbb{P}\{X_0 = i_0, \ldots, X_n = i_n\} = \mathbb{P}\{X_n = i_n \mid X_0 = i_0, \ldots, X_{n-1} = i_{n-1}\} \cdot \mathbb{P}\{X_0 = i_0, \ldots, X_{n-1} = i_{n-1}\} \tag{2.2}
$$

Applying the Markov property to the first factor:

$$
\mathbb{P}\{X_n = i_n \mid X_0 = i_0, \ldots, X_{n-1} = i_{n-1}\} = \mathbb{P}\{X_n = i_n \mid X_{n-1} = i_{n-1}\} = P_{i_{n-1}, i_n} \tag{2.3}
$$

Substituting (2.3) into (2.2) and iterating all the way back to $n=0$:

$$
\mathbb{P}\{X_0 = i_0, X_1 = i_1, \ldots, X_n = i_n\} = p_{i_0}\,P_{i_0,i_1}\,P_{i_1,i_2}\cdots P_{i_{n-1},i_n} \qquad \square
$$

The joint probability is just the initial probability of the starting state multiplied by the product of the transition probabilities along the path. $\mathbf{P}$ and $\{p_i\}$ are all we need.

---

## $n$-Step Transition Probabilities

The **$n$-step transition probability** is the probability of being in state $j$ after exactly $n$ transitions, starting from state $i$:

$$
P_{ij}^{(n)} \equiv \mathbb{P}\{X_{m+n} = j \mid X_m = i\}
$$

which is independent of $m$ for a homogeneous chain.

> **Theorem (Chapman-Kolmogorov).** The $n$-step transition probabilities satisfy the recursion:
> $$P_{ij}^{(n)} = \sum_{k=0}^{+\infty} P_{ik}\,P_{kj}^{(n-1)} \tag{2.4}$$
> with boundary condition $P_{ij}^{(0)} = \delta_{ij}$ (the identity: 0 if $i \neq j$, 1 if $i = j$).

**Proof.** Starting from the definition with $m = 0$:

$$
P_{ij}^{(n)} = \mathbb{P}\{X_n = j \mid X_0 = i\}
$$

We introduce the intermediate state $X_1 = k$ via the law of total probability (the events $\{X_1 = k\}$ for different $k$ are mutually exclusive and exhaustive):

$$
= \sum_{k=0}^{+\infty} \mathbb{P}\{X_n = j,\, X_1 = k \mid X_0 = i\}
$$

Using the conditional product rule $\mathbb{P}(AB \mid C) = \mathbb{P}(A \mid B, C)\,\mathbb{P}(B \mid C)$:

$$
= \sum_{k=0}^{+\infty} \mathbb{P}\{X_n = j \mid X_1 = k, X_0 = i\}\,\mathbb{P}\{X_1 = k \mid X_0 = i\}
$$

By the Markov property, knowledge of $X_1 = k$ already captures all information about the past ($X_0 = i$ becomes redundant):

$$
= \sum_{k=0}^{+\infty} \underbrace{\mathbb{P}\{X_n = j \mid X_1 = k\}}_{P_{kj}^{(n-1)}} \underbrace{\mathbb{P}\{X_1 = k \mid X_0 = i\}}_{P_{ik}} = \sum_{k=0}^{+\infty} P_{ik}\,P_{kj}^{(n-1)} \qquad \square
$$

**Matrix interpretation.** Equation (2.4) is exactly matrix multiplication:

$$
\mathbf{P}^{(n)} = \mathbf{P} \cdot \mathbf{P}^{(n-1)} \implies \mathbf{P}^{(n)} = \underbrace{\mathbf{P} \cdot \mathbf{P} \cdots \mathbf{P}}_{n \text{ factors}} = \mathbf{P}^n
$$

The $n$-step transition matrix is the $n$-th matrix power of $\mathbf{P}$.

---

**Worked Example.** A Markov chain on states $\{0, 1, 2\}$ has transition matrix:

$$
\mathbf{P} = \begin{pmatrix} 0.1 & 0.2 & 0.7 \\ 0.9 & 0.1 & 0 \\ 0.1 & 0.8 & 0.1 \end{pmatrix}
$$

and initial distribution $\boldsymbol{p} = (0.3,\, 0.4,\, 0.3)^T$.

**Computing $\mathbb{P}\{X_0=0, X_1=1, X_2=2\}$:**

$$
\mathbb{P}\{X_0=0, X_1=1, X_2=2\} = p_0 \cdot P_{01} \cdot P_{12} = 0.3 \times 0.2 \times 0 = 0
$$

*(Note: $P_{12} = 0$, so this transition is impossible.)*

**Computing $\mathbb{P}\{X_0=0, X_1=1, X_2=1\}$:**

$$
\mathbb{P}\{X_0=0, X_1=1, X_2=1\} = p_0 \cdot P_{01} \cdot P_{11} = 0.3 \times 0.2 \times 0.1 = 0.006
$$

**For non-consecutive times** (e.g. $\mathbb{P}\{X_0=0, X_1=1, X_3=1\}$), we need the 2-step probability $P_{11}^{(2)}$:

$$
\mathbb{P}\{X_0=0, X_1=1, X_3=1\} = p_0 \cdot P_{01} \cdot P_{11}^{(2)} = p_0 \cdot P_{01} \cdot \sum_{k=0}^{2} P_{1k}\,P_{k1}
$$

**Conditional probabilities** like $\mathbb{P}[X_3=1, X_1=1 \mid X_0=0]$ do not require the initial distribution $p_0$ (the initial state is already known):

$$
\mathbb{P}[X_3=1, X_1=1 \mid X_0=0] = P_{01} \cdot P_{11}^{(2)}
$$

![[Stochastic_Processes_2020_p30_img3.jpeg]]
*Figure 2.1 — Markov chain graph for the worked example.*

---

## 2.1 Models

Many physical and engineering processes can be approximated as Markov chains, yielding analytically tractable results. Below we study the key examples.

### 2.1.1 Discrete Queueing

Consider a system where customers arrive for service. In each time slot, at most one customer is served (if any are present); all others wait in a queue.

Let $X_n$ denote the number of customers in the system at the *beginning* of slot $n$. During slot $n$, a random number $\xi_n$ of customers arrive, with:

$$
\mathbb{P}[\xi_n = k] = a_k \quad (k \geq 0)
$$

where $a_k$ is independent of $n$ (stationary, uncorrelated arrivals). The system evolves as:

$$
X_{n+1} = \begin{cases} X_n - 1 + \xi_n & X_n > 0 \\ \xi_n & X_n = 0 \end{cases}
$$

This can be written compactly as:

$$
X_{n+1} = (X_n - 1)^+ + \xi_n
$$

where $Y^+ \equiv \max(Y, 0)$. Since $X_{n+1}$ depends only on $X_n$ and the i.i.d. random variable $\xi_n$, the process is indeed a Markov chain.

**Transition matrix:**

$$
\mathbf{P} = \begin{pmatrix} a_0 & a_1 & a_2 & a_3 & a_4 & \cdots \\ a_0 & a_1 & a_2 & a_3 & a_4 & \cdots \\ 0 & a_0 & a_1 & a_2 & a_3 & \cdots \\ 0 & 0 & a_0 & a_1 & a_2 & \cdots \\ 0 & 0 & 0 & a_0 & a_1 & \cdots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}
$$

- **Row 0 ($X_n = 0$):** Queue empty; $k$ arrivals bring the system to state $k$, probability $a_k$.
- **Row 1 ($X_n = 1$):** One customer departs; net state is just the $k$ arrivals, same as row 0.
- **Row $n \geq 2$:** After departure, $n-1 > 0$ customers remain; transitions to states $< n-1$ are impossible (those entries are 0). The remaining columns shift accordingly.

**Stability.** The average arrival rate is $\langle \xi_k \rangle = \sum_{k=0}^{+\infty} k\,a_k$.
- If $\langle \xi_k \rangle > 1$: more arrivals per slot than departures → queue diverges (**unstable**).
- If $\langle \xi_k \rangle < 1$: queue remains bounded (**stable**).
- If $\langle \xi_k \rangle = 1$: boundary case — deterministic arrivals (exactly one per slot) yield stability, but any randomness causes instability.

---

## 2.2 Poisson Process

The **Poisson process** is a fundamental continuous-time model for random, independent events (arrivals, emissions, etc.).

Let $X_t$ count the number of events in the interval $[0, t]$. We define the Poisson process by three axioms:

1. **$X_0 = 0$**: no events before the experiment begins.

2. **Independent and stationary increments:**
   - *Independent*: for disjoint intervals $[t_1, t_2]$ and $[t_3, t_4]$, the counts $X_{t_2} - X_{t_1}$ and $X_{t_4} - X_{t_3}$ are independent random variables.
   - *Stationary*: the distribution of $X_{s+t} - X_s$ depends only on the length $t$ of the interval, not its position $s$.

3. **Poisson distribution of counts:** For any interval of length $t$:
   $$\mathbb{P}[X_{s+t} - X_s = n] = \frac{e^{-\lambda t}(\lambda t)^n}{n!} \tag{2.5}$$
   where $\lambda > 0$ is the **rate** (average events per unit time).

**Equivalent infinitesimal formulation.** For a very small interval $[0, h]$:

$$
\mathbb{P}[X_h \geq 1] = \lambda h + o(h), \qquad \mathbb{P}[X_h \geq 2] = o(h)
$$

where $o(h)$ denotes any function satisfying $\lim_{h \to 0} o(h)/h = 0$. This says: in a tiny interval, the probability of one event is proportional to $h$, while simultaneous events are negligible. The two formulations are equivalent.

---

> **Theorem.** In a Poisson process with rate $\lambda$, the **inter-arrival times** (times between consecutive events) are i.i.d. $\mathrm{Exp}(\lambda)$ random variables.

**Proof.** Let $\{S_i\}_{i \in \mathbb{N}}$ be the inter-arrival times and $W_n = \sum_{i=0}^n S_i$ the cumulative arrival times.

**For $S_0$:** The first inter-arrival time exceeds $t$ if and only if no events occur in $[0, t]$:

$$
\mathbb{P}[S_0 > t] = \mathbb{P}[0 \text{ arrivals in } [0,t]] \overset{(2.5)}{=} e^{-\lambda t}
$$

So $S_0 \sim \mathrm{Exp}(\lambda)$.

**For $S_1$** (and by induction, all $S_n$):

$$
\mathbb{P}[S_1 > t \mid S_0 = s] = \mathbb{P}[0 \text{ arrivals in } (s, s+t] \mid S_0 = s]
$$

By independent increments, the count in $(s, s+t]$ is independent of $S_0 = s$. By stationarity, the count in $(s, s+t]$ has the same distribution as in $[0, t]$:

$$
= \mathbb{P}[0 \text{ arrivals in } [0, t]] = e^{-\lambda t}
$$

Thus $S_1 \sim \mathrm{Exp}(\lambda)$ and $S_1 \perp S_0$. The argument repeats for all $S_n$. $\square$

---

## 2.3 M/G/1 Queue

The **M/G/1 queue** generalises the discrete model by allowing random service times and Poisson arrivals:
- **M** (Memoryless): inter-arrival times are i.i.d. $\mathrm{Exp}(\lambda)$ — equivalently, arrivals form a Poisson process with rate $\lambda$.
- **G** (General): service times have an arbitrary distribution $G$ with CDF $G(x)$.
- **1**: a single server.

Customers arriving to an empty server begin service immediately; others queue and wait. Let $X(t)$ be the number of customers in the system at time $t$.

**Why $\{X(t)\}$ is not Markovian.** The departure rate depends on how long the current customer has been in service — information not captured by $X(t)$ alone (since $G$ is not necessarily memoryless). Arrival times *are* memoryless, but departure times are not.

**Restoring the Markov property by sampling at departure times.** When a customer departs at time $\bar{t}$, the state $X(\bar{t})$ *fully* determines the future: if $X(\bar{t}) > 0$, the next customer immediately begins service; if $X(\bar{t}) = 0$, the server idles until the next arrival. This observation motivates observing the chain only at departure times.

![[Stochastic_Processes_2020_p35_img4.jpeg]]
*Figure 2.2 — Example evolution of the M/G/1 queue; $X_n \equiv X(t_n^+)$ is the queue size left behind by the $n$-th departure.*

Let $t_n$ be the time of the $n$-th departure and $X_n \equiv X(t_n^+)$ the number of customers remaining after the $n$-th departure. Let $Y_n$ be the number of arrivals during the service time of the $n$-th customer.

![[Stochastic_Processes_2020_p36_img5.jpeg]]
*Figure 2.3 — Service times and departure times for the M/G/1 queue. $X_1 = 1$, so $X_2 = 2$, $X_3 = 1$, $X_4 = 0$, $X_5 = 1$.*

The evolution equation is identical to the discrete queueing model:

$$
X_{n+1} = \begin{cases} X_n - 1 + Y_n & X_n \geq 1 \\ Y_n & X_n = 0 \end{cases} \tag{2.6}
$$

The key difference is that now $Y_n$ counts arrivals during a **random** service duration. If the service time were fixed at $x$, the number of Poisson arrivals would be:

$$
\mathbb{P}\{Y_n = j\} = e^{-\lambda x}\,\frac{(\lambda x)^j}{j!}
$$

Since the service time has CDF $G(x)$, we average over it:

$$
a_j \equiv \mathbb{P}\{Y_n = j\} = \int_0^{\infty} e^{-\lambda x}\,\frac{(\lambda x)^j}{j!}\,\mathrm{d}G(x) \qquad j \in \mathbb{N}
$$

With these $\{a_j\}$, the transition matrix is exactly the same form as for the discrete queue (Section 2.1.1), now with $Y_n$ taking the role of $\xi_n$.

---

## 2.4 G/M/1 Queue

The **G/M/1 queue** reverses the assumptions:
- **G** (General): inter-arrival times are i.i.d. with generic distribution $G$ (not necessarily memoryless).
- **M** (Memoryless): service times are i.i.d. $\mathrm{Exp}(\mu)$.
- **1**: single server.

Again, $\{X(t)\}$ is not Markovian because $G$ may retain memory of the elapsed time since the last arrival. The time until the next arrival is not captured by $X(t)$ alone.

**Fix: sample at arrival times.** At the instant of an arrival, the state is fully informative: the service time distribution is memoryless ($\mathrm{Exp}(\mu)$), so the residual service time at any moment is again $\mathrm{Exp}(\mu)$. No past history is needed.

Let $t_n$ be the $n$-th arrival time, $X_n \equiv X(t_n^-)$ the queue size *just before* the $n$-th arrival (so $X_n$ does not include the arriving customer). Let $T \sim G$ be the generic inter-arrival time, and $\alpha_k \overset{\text{i.i.d.}}{\sim} \mathrm{Exp}(\mu)$ the service times.

**Transition probabilities.** If there are $i$ customers present when the $n$-th customer arrives ($X_n = i$), then between $t_n$ and $t_{n+1}$ there are $i + 1$ customers to serve. The count $j$ of departures during the inter-arrival time $T$ satisfies:

$$
P_{i,\,i+1-j} = \mathbb{P}[j \text{ departures} \mid X_n = i], \qquad j = 0, 1, \ldots, i+1
$$

There are three cases:

**Case 1: $j < i+1$ (some customers remain).**
Exactly $j$ departures occur in $T$, meaning the sum of $j$ service times fits within $T$ but adding one more would exceed it. This is equivalent to exactly $j$ events of a Poisson process with rate $\mu$ occurring in $[0, T]$:

$$
\mathbb{P}[j \text{ departures} \mid X_n = i] = \int_0^{+\infty} \frac{e^{-\mu t}(\mu t)^j}{j!}\,\mathrm{d}G(t)
$$

**Case 2: $j = i+1$ (all customers depart).**
All $i+1$ customers finish service before the next arrival. There is no constraint on a "next departure", so this becomes:

$$
\mathbb{P}[i+1 \text{ departures} \mid X_n = i] = \int_0^{+\infty} \sum_{k=i+1}^{+\infty} \frac{e^{-\mu t}(\mu t)^k}{k!}\,\mathrm{d}G(t)
$$

Using normalization $\sum_{k=0}^{\infty} \frac{e^{-\mu t}(\mu t)^k}{k!} = 1$, this simplifies to:

$$
= 1 - \int_0^{+\infty} \sum_{k=0}^{i} \frac{e^{-\mu t}(\mu t)^k}{k!}\,\mathrm{d}G(t)
$$

**Case 3: $j > i+1$ (impossible).**

$$
P_{i,l} = 0 \qquad l > i+1
$$

---

## 2.5 Data Transmission Protocols

Discrete-time Markov chains naturally model data buffers and network protocols.

Consider a buffer that accumulates data and transmits it over a link. Time is divided into equal slots of $T$ seconds. Let $\xi_n$ be the data generated in slot $n$:

$$
\mathbb{P}[\xi_n = k] = a_k \qquad k \geq 0
$$

with $\{\xi_n\}$ i.i.d. Let $X_n$ = data in buffer at the **start** of slot $n$. Since $X_{n+1}$ depends only on $X_n$ and the current i.i.d. arrival $\xi_n$, this is a Markov chain.

### Protocol 1 — Bounded Transmission (capacity $M$)

Send all buffered data each slot, up to a maximum of $M$ units:

$$
X_{n+1} = \begin{cases} \xi_n & X_n \leq M \\ X_n - M + \xi_n & X_n > M \end{cases}
$$

**Transition matrix:**

$$
P_{ij} = \begin{cases} a_j & i \leq M \\ a_{j+M-i} & i > M \end{cases}
$$

The first $M+1$ rows are identical (all data is cleared); from row $M+1$ onwards, the distribution shifts right by the backlog.

![[Stochastic_Processes_2020_p40_img6.jpeg]]
*Figure 2.4 — Block diagram for Protocol 1. The first $M$ states share identical outgoing distributions.*

### Protocol 2a — Minimum Transfer Size $m$, Unlimited Bandwidth

To avoid overhead from tiny packets, set a minimum threshold $m$: transmit only if $X_n \geq m$; otherwise hold.

$$
X_{n+1} = \begin{cases} X_n + \xi_n & X_n < m \\ \xi_n & X_n \geq m \end{cases}
$$

![[Stochastic_Processes_2020_p41_img7.jpeg]]
*Figure 2.5 — Block diagram for Protocol 2a.*

### Protocol 2b — Minimum Size $m$, Bounded Bandwidth $M$

Combining both constraints:

$$
X_{n+1} = \begin{cases} X_n + \xi_n & X_n < m \\ \xi_n & m \leq X_n \leq M \\ X_n - M + \xi_n & X_n > M \end{cases}
$$

![[Stochastic_Processes_2020_p42_img8.jpeg]]
*Figure 2.6 — Block diagram for Protocol 2b.*

**Pathological case of Protocol 2.** If the buffer holds a small amount ($< m$) and no new data arrives for many slots, the data sits indefinitely — the optimization intended to reduce overhead paradoxically increases latency. The fix is a **timeout**: if data has waited more than $T_\mathrm{max}$ slots without reaching the threshold, transmit anyway. This is modelled by extending the state to include a "timeout counter", effectively replicating states:

![[Stochastic_Processes_2020_p42_img9.jpeg]]
*Figure 2.7 — Protocol 2 with a 2-slot timeout: if the threshold $m$ is not reached after 2 consecutive slots, the buffer transmits regardless.*

---

## 2.6 First Step Analysis

**First step analysis** is a general technique for computing quantities of interest (absorption probabilities, expected times, etc.) for Markov chains. The idea is to condition on the first transition and use the Markov property to write a *self-referential equation*, then solve it.

### Illustrative Example — Three-State Absorbing Chain

Consider the chain:

$$
\mathbf{P} = \bordermatrix{ & 0 & 1 & 2 \cr 0 & 1 & 0 & 0 \cr 1 & \alpha & \beta & \gamma \cr 2 & 0 & 0 & 1 } \tag{2.8}
$$

![[Stochastic_Processes_2020_p43_img10.jpeg]]
*Figure 2.8 — Block diagram for chain (2.8). States 0 and 2 are absorbing; state 1 is transient.*

- **Absorbing states (0 and 2):** once entered, the chain never leaves. $P_{00} = 1$, $P_{22} = 1$.
- **Transient state (1):** the chain visits state 1 temporarily, but eventually leaves forever.

**Question 1:** What is the probability $u$ of being absorbed at state 0, starting from state 1?

$$
u = \mathbb{P}[X_T = 0 \mid X_0 = 1]
$$

where $T = \min\{n \geq 0 : X_n \in \{0, 2\}\}$ is the **absorption time**.

**First-step analysis:** Apply the law of total probability over the first step:

$$
u = \sum_{k=0}^{2} \mathbb{P}[X_T = 0 \mid X_0 = 1,\, X_1 = k]\,\mathbb{P}[X_1 = k \mid X_0 = 1]
$$

By the Markov property, $X_0$ becomes irrelevant once $X_1$ is known:

$$
u = \sum_{k=0}^{2} \mathbb{P}[X_T = 0 \mid X_1 = k]\,P_{1k}
$$

Expanding:
- $k=0$: chain is already at absorbing state 0, so $\mathbb{P}[X_T = 0 \mid X_1 = 0] = 1$; this occurs with probability $\alpha$.
- $k=2$: chain is at absorbing state 2, so $\mathbb{P}[X_T = 0 \mid X_1 = 2] = 0$; this occurs with probability $\gamma$.
- $k=1$: chain is back in state 1. By the Markov property, the future is exactly the same problem we started with — so $\mathbb{P}[X_T = 0 \mid X_1 = 1] = u$; this occurs with probability $\beta$.

$$
u = 1 \cdot \alpha + u \cdot \beta + 0 \cdot \gamma
$$

Solving for $u$:

$$
\boxed{u = \frac{\alpha}{1-\beta} = \frac{\alpha}{\alpha + \gamma}}
$$

**Question 2:** What is the expected absorption time $\nu = \mathbb{E}[T \mid X_0 = 1]$?

First-step analysis: the first step always costs 1. After that:
- With probability $\alpha$: at state 0 (absorbing), no more steps needed.
- With probability $\gamma$: at state 2 (absorbing), no more steps needed.
- With probability $\beta$: back at state 1, where the expected remaining time is again $\nu$.

$$
\nu = 1 + \alpha \cdot 0 + \beta \cdot \nu + \gamma \cdot 0 = 1 + \beta\nu
$$

Solving:

$$
\boxed{\nu = \frac{1}{1 - \beta}}
$$

**Sanity check.** The time spent in state 1 follows a geometric distribution: in each step, the chain leaves state 1 with probability $1 - \beta$. The expected number of visits to state 1 (equivalently, the expected absorption time) is:

$$
\mathbb{E}[T \mid X_0 = 1] = \sum_{k=0}^{+\infty} \mathbb{P}[T > k \mid X_0 = 1] = \sum_{k=0}^{+\infty} \beta^k = \frac{1}{1-\beta} \qquad \checkmark
$$

---

### Four-State System

For a system with states $\{0, 1, 2, 3\}$ where 0 and 3 are absorbing and 1, 2 are transient:

$$
\mathbf{P} = \bordermatrix{ & 0 & 1 & 2 & 3 \cr 0 & 1 & 0 & 0 & 0 \cr 1 & P_{10} & P_{11} & P_{12} & P_{13} \cr 2 & P_{20} & P_{21} & P_{22} & P_{23} \cr 3 & 0 & 0 & 0 & 1 } \tag{2.9}
$$

![[Stochastic_Processes_2020_p45_img11.jpeg]]
*Figure 2.9 — Block diagram for chain (2.9).*

Absorption probabilities (to state 0):
$$
u_1 = 1 \cdot P_{10} + 0 \cdot P_{13} + u_1 \cdot P_{11} + u_2 \cdot P_{12} \tag{2.10}
$$
$$
u_2 = 1 \cdot P_{20} + 0 \cdot P_{23} + u_1 \cdot P_{21} + u_2 \cdot P_{22} \tag{2.11}
$$

Equations (2.10) and (2.11) form a $2 \times 2$ linear system in $(u_1, u_2)$.

Expected absorption times:
$$
\nu_1 = 1 + \nu_1 \cdot P_{11} + \nu_2 \cdot P_{12}
$$
$$
\nu_2 = 1 + \nu_1 \cdot P_{21} + \nu_2 \cdot P_{22}
$$

---

### General Absorbing Chain — Matrix Form

Consider a chain with $N+1$ states. Suppose states $\{0, 1, \ldots, r-1\}$ are **transient** and states $\{r, \ldots, N\}$ are **absorbing**. The transition matrix has the block structure:

$$
\mathbf{P} = \begin{pmatrix} \mathbf{Q} & \mathbf{R} \\ \mathbf{0} & \mathbf{I} \end{pmatrix}
$$

where $\mathbf{Q}$ ($r \times r$) governs transitions among transient states, $\mathbf{R}$ ($r \times (N-r+1)$) governs transitions from transient to absorbing states, $\mathbf{0}$ reflects that absorbing states cannot leave, and $\mathbf{I}$ is the identity.

The absorption probability $U_{ik} = \mathbb{P}[\text{absorbed at } k \mid X_0 = i]$ (for transient $i$, absorbing $k$) satisfies:

$$
U_{ik} = P_{ik} + \sum_{j=0}^{r-1} P_{ij}\,U_{jk} \qquad i = 0, 1, \ldots, r-1
$$

In matrix form: $\mathbf{U} = \mathbf{R} + \mathbf{Q}\mathbf{U}$, giving:

$$
\mathbf{U} = (\mathbf{I} - \mathbf{Q})^{-1}\mathbf{R}
$$

The matrix $\mathbf{N} = (\mathbf{I} - \mathbf{Q})^{-1}$ is the **fundamental matrix**: its entry $N_{ij}$ is the expected number of times the chain visits transient state $j$ before absorption, starting from transient state $i$.

---

## 2.7 General Absorbing Markov Chain — Reward Framework

Consider a **reward function** $g : \{0,\ldots,r-1\} \to \mathbb{R}$ assigning a real value $g(j)$ to each transient state $j$. Each time the chain visits state $j$, it accumulates reward $g(j)$.

The **expected total reward** accumulated before absorption, starting from state $i$, is:

$$
w_i = \mathbb{E}\!\left[\sum_{n=0}^{T-1} g(X_n) \;\Big|\; X_0 = i\right] \qquad i = 0, \ldots, r-1
$$

**First-step analysis** gives:

$$
w_i = g(i) + \sum_{j=0}^{r-1} P_{ij}\,w_j \qquad i = 0, \ldots, r-1 \tag{2.14}
$$

The term $g(i)$ is the reward earned immediately (at the current visit), and $\sum_j P_{ij}\,w_j$ is the expected future reward.

**Special cases:**

| Choice of $g$ | $w_i$ gives |
|---------------|-------------|
| $g(j) = 1\ \forall j$ | $w_i = \nu_i =$ expected absorption time |
| $g(j) = \delta_{jk}$ (1 only at state $k$) | $w_i = W_{ik} =$ expected number of visits to $k$ before absorption |

For $g(j) = \delta_{jk}$, equation (2.14) becomes:

$$
W_{ik} = \delta_{ik} + \sum_{j=0}^{r-1} P_{ij}\,W_{jk}
$$

which in matrix form is $\mathbf{W} = \mathbf{I} + \mathbf{Q}\mathbf{W}$, giving again $\mathbf{W} = (\mathbf{I} - \mathbf{Q})^{-1} = \mathbf{N}$.

---

## 2.8 Two-State Markov Chain

The simplest non-trivial Markov chain has two states:

$$
\mathbf{P} = \bordermatrix{ & 0 & 1 \cr 0 & 1-a & a \cr 1 & b & 1-b } \qquad 0 < a, b < 1
$$

![[Stochastic_Processes_2020_p48_img12.jpeg]]
*Figure 2.10 — Block diagram for the two-state Markov chain.*

### Exact $n$-Step Transition Matrix

> **Theorem.** The $n$-step transition matrix of the two-state chain is:
> $$\mathbf{P}^n = \frac{1}{a+b}\begin{pmatrix} b & a \\ b & a \end{pmatrix} + \frac{(1-a-b)^n}{a+b}\begin{pmatrix} a & -a \\ -b & b \end{pmatrix} \tag{2.16}$$

Defining $\mathbf{A} = \begin{pmatrix} b & a \\ b & a \end{pmatrix}$ and $\mathbf{B} = \begin{pmatrix} a & -a \\ -b & b \end{pmatrix}$, this reads:

$$
\mathbf{P}^n = (a+b)^{-1}\bigl[\mathbf{A} + (1-a-b)^n\,\mathbf{B}\bigr] \tag{2.17}
$$

**Proof by induction.**

*Base case ($n=1$):*

$$
\mathbf{P}^1 = \frac{1}{a+b}\begin{pmatrix} b + a(1-a-b) & a - a(1-a-b) \\ b - b(1-a-b) & a + b(1-a-b) \end{pmatrix} = \frac{1}{a+b}\begin{pmatrix}(1-a)(a+b) & a(a+b) \\ b(a+b) & (1-b)(a+b)\end{pmatrix} = \begin{pmatrix}1-a & a \\ b & 1-b\end{pmatrix} = \mathbf{P} \checkmark
$$

*Inductive step:* Assume (2.17) holds for $n$. Compute $\mathbf{P}^{n+1} = \mathbf{P}^n \cdot \mathbf{P}$:

$$
\mathbf{AP} = \begin{pmatrix} b & a \\ b & a \end{pmatrix}\begin{pmatrix}1-a & a \\ b & 1-b\end{pmatrix} = \begin{pmatrix} b & a \\ b & a \end{pmatrix} = \mathbf{A}
$$

$$
\mathbf{BP} = \begin{pmatrix} a & -a \\ -b & b \end{pmatrix}\begin{pmatrix}1-a & a \\ b & 1-b\end{pmatrix} = (1-a-b)\begin{pmatrix} a & -a \\ -b & b \end{pmatrix} = (1-a-b)\mathbf{B}
$$

Therefore:

$$
\mathbf{P}^{n+1} = (a+b)^{-1}[\mathbf{A} + (1-a-b)^{n+1}\mathbf{B}] \qquad \square
$$

### Asymptotic Behaviour

Since $0 < a, b < 1$ implies $|1-a-b| < 1$, we have $(1-a-b)^n \to 0$ as $n \to \infty$:

$$
\lim_{n\to\infty} \mathbf{P}^n = \frac{1}{a+b}\begin{pmatrix} b & a \\ b & a \end{pmatrix}
$$

Both rows are identical: **the long-run distribution is independent of the initial state**. The chain converges to the stationary distribution:

$$
\pi_0 = \frac{b}{a+b}, \qquad \pi_1 = \frac{a}{a+b}
$$

The system "forgets" where it started. This memory loss is characteristic of ergodic Markov chains (see Chapter 3).

### Application: Packet Transmission Error Model

Model packet transmission with state 0 = correct and state 1 = error. Then:
- **Average error probability:** $P_e = \frac{a}{a+b}$
- **Mean burst length** (consecutive errors): the chain stays in state 1 each step with probability $1-b$, so the burst length is geometric with mean $\langle L \rangle = 1/b$.

---

### 2.8.1 Markov Chains from Independent Random Variables

Let $\{\xi_n\}$ be i.i.d. random variables on $\mathbb{N}_0$ with $\mathbb{P}[\xi_i = i] = a_i$. Three natural Markov chains:

**1. $X_n = \xi_n$.** Each state is the current i.i.d. observation; all rows of $\mathbf{P}$ are identical (rows equal $\{a_k\}$).

**2. Running maximum:** $X_n = \max\{\xi_1, \ldots, \xi_n\}$.

Since $X_{n+1} = \max\{X_n, \xi_{n+1}\}$, the future depends only on $X_n$ (and the next i.i.d. draw) — Markov. The transition matrix has entries $P_{ij} = a_j$ for $j > i$ and $P_{ii} = A_i = \sum_{k=0}^i a_k$ (the chain stays at $i$ if the new draw is $\leq i$):

$$
\mathbf{P} = \begin{pmatrix} A_0 & a_1 & a_2 & a_3 & \cdots \\ 0 & A_1 & a_2 & a_3 & \cdots \\ 0 & 0 & A_2 & a_3 & \cdots \\ \vdots & \vdots & \vdots & \ddots & \end{pmatrix}
$$

**3. Partial sums:** $X_n = \xi_1 + \cdots + \xi_n$ (with $X_0 = 0$). This is a random walk on $\mathbb{N}_0$.

---

### 2.8.2 One-Dimensional Random Walk

A **random walk** models a particle at position $i$ that:
- moves right to $i+1$ with probability $p_i$,
- moves left to $i-1$ with probability $q_i$,
- stays at $i$ with probability $r_i = 1 - p_i - q_i$.

The transition matrix has nonzero entries only on the main diagonal and the two adjacent diagonals.

**Gambler's Ruin Problem.** A gambler starts with $k$ units and plays against an opponent with $N-k$ units. Each round: the gambler gains 1 unit with probability $p$ or loses 1 with probability $q = 1-p$. The game ends when either player is bankrupt.

States 0 and $N$ are absorbing. Define:

$$
u_k = \mathbb{P}[X_T = 0 \mid X_0 = k] \quad \text{(probability of the gambler going bankrupt)}
$$

**First-step analysis:**

$$
u_k = p\,u_{k+1} + q\,u_{k-1}, \qquad k = 1, \ldots, N-1
$$

with boundary conditions $u_0 = 1$ and $u_N = 0$.

**Solution.** Rewrite using $p + q = 1$:

$$
p\,u_k + q\,u_k = p\,u_{k+1} + q\,u_{k-1} \implies q(u_k - u_{k-1}) = p(u_{k+1} - u_k)
$$

Define $x_k = u_k - u_{k-1}$. This gives the recursion $x_{k+1} = (q/p)\,x_k$, so:

$$
x_k = \left(\frac{q}{p}\right)^{k-1} x_1
$$

**Case $p \neq q$:**

Summing the telescoping series $u_k - u_0 = \sum_{i=1}^k x_i$ and using $u_0 = 1$:

$$
u_k = 1 + x_1\,\frac{1 - (q/p)^k}{1 - (q/p)}
$$

Applying $u_N = 0$ determines $x_1 = -(1-q/p)/(1-(q/p)^N)$. Substituting:

$$
\boxed{u_k = \frac{(q/p)^k - (q/p)^N}{1 - (q/p)^N}} \qquad (p \neq q)
$$

**Case $p = q = 1/2$:**

The recursion $x_{k+1} = x_k$ means all $x_k$ are equal. Then $u_k = 1 + k\,x_1$, and $u_N = 0$ gives $x_1 = -1/N$:

$$
\boxed{u_k = \frac{N - k}{N}} \qquad (p = q)
$$

**Summary:**

$$
u_k = \begin{cases} \dfrac{N-k}{N} & p = q = \tfrac{1}{2} \\[8pt] \dfrac{(q/p)^k - (q/p)^N}{1 - (q/p)^N} & p \neq q \end{cases} \qquad k = 1, \ldots, N-1
$$

with $u_0 = 1$, $u_N = 0$.

**Infinite opponent ($N \to \infty$):**

$$
u_k \xrightarrow{N \to \infty} \begin{cases} 1 & p \leq q \\ (q/p)^k & p > q \end{cases}
$$

- If $p \leq q$ (game unfair or fair): the gambler certainly goes bankrupt with probability 1 — even in a *fair* game, infinite play leads to certain ruin!
- If $p > q$ (game favours the gambler): there is still a non-zero ruin probability $(q/p)^k$, but it decays as the starting capital $k$ grows.

![[Stochastic_Processes_2020_p54_img13.jpeg]]
*Figure 2.11 — The ratio $p/q$ determines the trend. At $p/q = 1$ (fair game) the mean trajectory is flat, but fluctuations eventually ruin the player given enough time.*

---

### 2.8.3 Success Runs

The **success run** chain has transition matrix:

| | 0 | 1 | 2 | 3 | 4 | $\cdots$ |
|---|---|---|---|---|---|---|
| 0 | $p_0$ | $q_0$ | 0 | 0 | 0 | $\cdots$ |
| 1 | $p_1$ | $r_1$ | $q_1$ | 0 | 0 | $\cdots$ |
| 2 | $p_2$ | 0 | $r_2$ | $q_2$ | 0 | $\cdots$ |
| 3 | $p_3$ | 0 | 0 | $r_3$ | $q_3$ | $\cdots$ |

From state $i$: advance to $i+1$ (probability $q_i$), stay (probability $r_i$), or reset to 0 (probability $p_i$).

![[Stochastic_Processes_2020_p54_img14.jpeg]]
*Figure 2.12 — Block diagram for the success run chain.*

**Application: Layer-2 Retransmission Protocol.**

Let $X_n$ = number of failed transmissions of the current packet. Each transmission succeeds with probability $1-\varepsilon$ (moving to absorbing state $S$) or fails with probability $\varepsilon$ (advancing to $X_n + 1$). After $L+1$ total failures, the packet is discarded (absorbing state $F$).

![[Stochastic_Processes_2020_p55_img15.jpeg]]
![[Stochastic_Processes_2020_p55_img16.jpeg]]
*Figure 2.13 — Block diagram for the layer-2 protocol.*

**Absorption probability** (success) by first-step analysis:

$$
u_i = \begin{cases} \varepsilon\,u_{i+1} + (1-\varepsilon) & i < L \\ 1 - \varepsilon & i = L \end{cases}
$$

Starting from $u_L$ and iterating backwards:

$$
u_0 = \varepsilon^L(1-\varepsilon) + (1-\varepsilon)\,\frac{1-\varepsilon^L}{1-\varepsilon} = 1 - \varepsilon^{L+1}
$$

This equals the probability of not failing $L+1$ times in a row — which is the obvious combinatorial answer. $\checkmark$

**Expected number of transmissions per packet:**

$$
\nu_i = \varepsilon\,\nu_{i+1} + 1 \quad (i < L), \qquad \nu_L = 1
$$

Iterating backwards:

$$
\nu_0 = \varepsilon^L + \frac{1 - \varepsilon^L}{1 - \varepsilon} = \frac{1 - \varepsilon^{L+1}}{1 - \varepsilon}
$$

**Throughput** (fraction of transmissions carrying successfully delivered packets):

$$
\mathrm{Throughput} = \frac{u_0}{\nu_0} = \frac{1 - \varepsilon^{L+1}}{\dfrac{1 - \varepsilon^{L+1}}{1 - \varepsilon}} = 1 - \varepsilon
$$

Intuitively, $1-\varepsilon$ is the per-transmission success probability. This confirms that the throughput equals the probability of a single successful transmission — independent of the retry limit $L$.

---

### 2.8.4 First Passage Times

The **first passage time** $\theta_{ij}$ from state $i$ to state $j$ is the number of transitions to reach $j$ for the first time, starting from $i$:

$$
f_{ij}(n) = \mathbb{P}[\theta_{ij} = n] = \mathbb{P}[X_n = j,\, X_m \neq j\ \forall m = 1,\ldots,n-1 \mid X_0 = i]
$$

By convention, $f_{ij}(0) = 0$ for $i \neq j$ (cannot reach $j$ without moving).

**First-step recursion:**

$$
f_{ij}(n) = P_{ij}\,\delta(n-1) + \sum_{k \neq j} P_{ik}\,f_{kj}(n-1) \tag{2.24}
$$

where $\delta(n) = \mathbf{1}[n=0]$. The first term handles the direct $i \to j$ transition (possible only at $n=1$); the second handles the case where the chain first visits some intermediate state $k \neq j$ (after one step), and then reaches $j$ for the first time in the remaining $n-1$ steps.

**Two-state example.** With the standard two-state chain ($P_{01} = a$, $P_{00} = 1-a$, $P_{10} = b$, $P_{11} = 1-b$):

$$
f_{01}(n) = P_{01}\,\delta(n-1) + P_{00}\,f_{01}(n-1) = \begin{cases} a & n=1 \\ (1-a)\,f_{01}(n-1) & n > 1 \end{cases}
$$

Iterating: $f_{01}(n) = a(1-a)^{n-1}$ for $n \geq 1$. This is a geometric distribution with success probability $a$ — the chain must stay in state 0 for $n-1$ steps before transitioning to state 1 on step $n$.

Similarly (using the recursion (2.24)):

$$
f_{11}(n) = P_{11}\,\delta(n-1) + P_{10}\,f_{01}(n-1) = \begin{cases} 1-b & n=1 \\ ab(1-a)^{n-2} & n > 1 \end{cases}
$$

For $f_{11}$: on the first step the chain either stays in 1 (probability $1-b$, so $\theta_{11} = 1$), or moves to 0 (probability $b$) and then must return to 1 for the first time — taking $n-1$ additional steps.

By symmetry ($a \leftrightarrow b$), $f_{10}$ and $f_{00}$ follow analogously.

> **Remark.** In the two-state case, first passage times reduce to geometric distributions and can be read off directly. In general chains with more states, direct reasoning fails and the first-step recursion (2.24) is indispensable.
