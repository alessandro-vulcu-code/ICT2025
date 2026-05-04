# Chapter 2 — Markov Chains

## Table of Contents

- [[#Markov Chains — Definition and Notation|Markov Chains — Definition and Notation]]
  - [[#n-Step Transition Probabilities|n-Step Transition Probabilities]]
- [[#Models|Models]]
  - [[#Discrete Queueing|Discrete Queueing]]
  - [[#Poisson Process|Poisson Process]]
  - [[#M/G/1 Queue|M/G/1 Queue]]
  - [[#G/M/1 Queue|G/M/1 Queue]]
  - [[#Data Transmission Protocols|Data Transmission Protocols]]
- [[#First Step Analysis|First Step Analysis]]
  - [[#Three-State Example|Three-State Example]]
  - [[#Four-State Example|Four-State Example]]
  - [[#General Absorbing Markov Chain (Rewards)|General Absorbing Markov Chain (Rewards)]]
- [[#Two-State Markov Chain|Two-State Markov Chain]]
  - [[#Markov Chains Defined by Independent Random Variables|Markov Chains Defined by Independent Random Variables]]
  - [[#One-Dimensional Random Walks|One-Dimensional Random Walks]]
  - [[#Success Runs and Layer 2 Protocol|Success Runs and Layer 2 Protocol]]
  - [[#First Passage Times|First Passage Times]]
- [[#Alternative First Step Analysis — Matrix Approach|Alternative First Step Analysis — Matrix Approach]]
  - [[#Matrix Approach for Average First Passage Times|Matrix Approach for Average First Passage Times]]
- [[#Summary Table|Summary Table]]

---

## Markov Chains — Definition and Notation

A **Markov process** $\{X_t\}$ is a stochastic process with the property that, given the value of $X_t$, the future values $X_s$ for $s > t$ are not influenced by the past values $X_u$ for $u < t$. All necessary information for predicting the system's future is contained in the present state.

> [!Important] Definition — Markov Chain
> A Markov process with **discrete values** ($X_t$ takes values in a countable set) and **discrete index** (index set $T$ is countable) is called a **Markov chain**. The **Markov property** states:
>
> $$\mathbb{P}\{X_{n+1}=j \mid X_0=i_0,\ldots,X_{n-1}=i_{n-1},X_n=i\} = \mathbb{P}\{X_{n+1}=j \mid X_n=i\}$$
>
> for any possible choice of states $i_0,\ldots,i_n$, $i$, $j$, and for all time points $n$. States are typically labelled by $\mathbb{N}$.

> [!Important] Definition — One-Step Transition Probability and Transition Matrix
> The **one-step transition probability** $P^{n,n+1}_{ij}$ is the probability of going from state $i$ to state $j$ in one step:
>
> $$P^{n,n+1}_{ij} = \mathbb{P}\{X_{n+1}=j \mid X_n=i\}$$
>
> If $P^{n,n+1}_{ij} \equiv P_{ij}$ is independent of $n$, the chain is called **homogeneous** (has stationary transition probabilities).
>
> The entries $P_{ij}$ form the **transition probability matrix** $\mathbf{P}$, where row $i$ gives the distribution of $X_{n+1}$ conditional on $X_n = i$:
>
> $$P_{ij} \geq 0 \quad \forall i,j \in \mathbb{N}; \qquad \sum_{j=0}^{+\infty} P_{ij} = 1 \quad \forall i \in \mathbb{N}$$
>
> **The matrix $\mathbf{P}$ and the initial distribution $\{p_i = \mathbb{P}(X_0=i)\}$ fully specify a Markov chain.**
>
> **Proof of full specification:** The joint probability of any sequence $\{i_0,\ldots,i_n\}$ can be computed as:
> $$\mathbb{P}\{X_0=i_0,X_1=i_1,\ldots,X_n=i_n\} = p_{i_0} P_{i_0,i_1} \cdots P_{i_{n-2},i_{n-1}} P_{i_{n-1},i_n}$$
> This follows by repeated application of the definition of conditional probability and the Markov property, reducing the full joint probability to a product of one-step transition probabilities weighted by the initial distribution.

---

### n-Step Transition Probabilities

> [!Important] Chapman-Kolmogorov Equations
> The **$n$-step transition probability** is:
> $$P_{ij}^{(n)} \equiv \mathbb{P}\{X_{m+n}=j \mid X_m=i\}$$
> (independent of $m$ for a homogeneous chain).
>
> **Recursive formula:**
> $$P_{ij}^{(n)} = \sum_{k=0}^{+\infty} P_{ik} P_{kj}^{(n-1)}$$
> with $P^{(0)}_{ij} = \delta_{ij}$ (the identity).
>
> **Proof:**
> $$P^{(n)}_{ij} = \mathbb{P}\{X_n=j \mid X_0=i\}$$
> Apply the law of total probability, conditioning on $X_1 = k$:
> $$= \sum_{k=0}^{+\infty} \mathbb{P}\{X_n=j, X_1=k \mid X_0=i\} = \sum_{k=0}^{+\infty} \mathbb{P}\{X_n=j \mid X_1=k, X_0=i\}\,\mathbb{P}(X_1=k \mid X_0=i)$$
> By the Markov property, condition $X_0=i$ is irrelevant given $X_1=k$:
> $$= \sum_{k=0}^{+\infty} \underbrace{\mathbb{P}\{X_n=j \mid X_1=k\}}_{P^{(n-1)}_{kj}} \underbrace{\mathbb{P}(X_1=k \mid X_0=i)}_{P_{ik}} = \sum_{k=0}^{+\infty} P_{ik} P^{(n-1)}_{kj} \qquad \square$$
>
> In matrix form this is just matrix multiplication:
> $$\mathbf{P}^{(n)} = \mathbf{P} \times \mathbf{P}^{(n-1)} = \underbrace{\mathbf{P} \times \cdots \times \mathbf{P}}_{n \text{ factors}}$$
>
> **Intuition:** The probability of going from $i$ to $j$ in $n$ steps equals the sum over all possible intermediate states $k$ at step 1, of the probability of going $i \to k$ in one step times the probability of going $k \to j$ in $n-1$ steps.

> [!Example] Example — 3-State Chain
> **Problem:** A Markov chain on states $\{0, 1, 2\}$ has:
> $$\mathbf{P} = \begin{pmatrix} 0.1 & 0.2 & 0.7 \\ 0.9 & 0.1 & 0 \\ 0.1 & 0.8 & 0.1 \end{pmatrix}, \qquad \boldsymbol{p} = (0.3, 0.4, 0.3)^T$$
> Compute $\mathbb{P}\{X_0=0, X_1=1, X_2=1\}$.
>
> **Solution:**
> $$\mathbb{P}\{X_0=0,X_1=1,X_2=1\} = p_0 P_{01} P_{11} = 0.3 \cdot 0.2 \cdot 0.1 = 0.006$$
>
> For non-consecutive states, e.g. $\mathbb{P}\{X_0=0,X_1=1,X_3=1\}$, use 2-step transition probabilities:
> $$\mathbb{P}\{X_0=0,X_1=1,X_3=1\} = p_0 \cdot P_{01} \cdot P^{(2)}_{11} = p_0 P_{01}\sum_{k=0}^2 P_{1k}P_{k1}$$
>
> For conditional probabilities, e.g. $\mathbb{P}[X_3=1,X_1=1 \mid X_0=0]$, the initial distribution drops:
> $$\mathbb{P}[X_3=1,X_1=1 \mid X_0=0] = P_{01} \cdot P^{(2)}_{11}$$
>
> ![[Stochastic_Processes_2020_p30_img3.jpeg]]
> *Figure 2.1 — Markov chain graph for the 3-state example. Arrows show allowed transitions; arc labels show transition probabilities.*
>
> **Takeaway:** Joint probabilities factorise as products of initial distribution and one-step (or $n$-step) transition probabilities. For non-adjacent time indices, compute the appropriate power of $\mathbf{P}$.

---

## Models

### Discrete Queueing

Customers arrive and queue. In each time slot exactly one customer is served (if any). Let $X_n$ = queue size at start of slot $n$, $\xi_n$ = number of arrivals in slot $n$ with $\mathbb{P}[\xi_n=k]=a_k$ (i.i.d.).

**Evolution:**

$$X_{n+1} = (X_n - 1)^+ + \xi_n, \qquad Y^+ \equiv \max(Y,0)$$

This is a Markov chain because $X_{n+1}$ depends only on $X_n$ and $\xi_n$.

**Transition matrix:**

$$\mathbf{P} = \begin{pmatrix} a_0 & a_1 & a_2 & a_3 & \cdots \\ a_0 & a_1 & a_2 & a_3 & \cdots \\ 0 & a_0 & a_1 & a_2 & \cdots \\ 0 & 0 & a_0 & a_1 & \cdots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

The first two rows are identical because: with $X_n=0$ (empty queue), no departure occurs, so $X_{n+1}=\xi_n$; with $X_n=1$, one customer departs, leaving 0 in queue, so again $X_{n+1}=\xi_n$. From row 3 onwards, $n-1>0$ customers remain, so transitions to states $< n-1$ are impossible.

**Stability:** The **arrival rate** is $\langle\xi_k\rangle = \sum_{k=0}^{+\infty} k a_k$.
- $\langle\xi_k\rangle > 1$: queue diverges — system **unstable**.
- $\langle\xi_k\rangle < 1$: queue remains finite — system **stable**.
- $\langle\xi_k\rangle = 1$: boundary case; stable only if arrivals are deterministic (exactly one per slot).

---

### Poisson Process

> [!Important] Definition — Poisson Process
> Let $X_t$ = number of events occurring in $[0,t]$. A **Poisson process** with rate $\lambda$ satisfies:
>
> 1. $X_0 = 0$
> 2. **Independent increments:** $X_{t_2}-X_{t_1}$ and $X_{t_4}-X_{t_3}$ are independent if $[t_1,t_2]\cap[t_3,t_4]=\varnothing$
> 3. **Stationary increments:** $X_{s+t}-X_s \sim X_{s'+t}-X_{s'}$ for disjoint intervals of equal size $t$
> 4. **Poisson distribution for counts:**
> $$\mathbb{P}[X_{t+s}-X_s = n] = \frac{e^{-\lambda t}(\lambda t)^n}{n!}$$
>
> Equivalently, for a small interval $[0,h]$:
> $$\mathbb{P}[X_h \geq 1] = \lambda h + o(h), \qquad \mathbb{P}[X_h \geq 2] = o(h)$$
> where $\lim_{h\to 0} o(h)/h = 0$. This means simultaneous arrivals are negligible.

> [!Important] Theorem — Exponential Inter-Arrival Times
> **Statement:** In a Poisson process with rate $\lambda$, the inter-arrival times $\{S_i\}$ are i.i.d. Exp$(\lambda)$ random variables.
>
> **Proof:**
> Let $W_n = \sum_{i=0}^n S_i$ be the cumulative arrival times. For the first inter-arrival time:
> $$\mathbb{P}[S_0 > t] = \mathbb{P}[0 \text{ arrivals in } [0,t]] = e^{-\lambda t}$$
> so $S_0 \sim \text{Exp}(\lambda)$.
>
> For $S_1$:
> $$\mathbb{P}[S_1 > t \mid S_0 = s] = \mathbb{P}[0 \text{ arrivals in } (s,s+t] \mid S_0=s]$$
> By independent increments, the condition $S_0=s$ can be dropped. By stationarity, the probability depends only on the interval length $t$:
> $$= \mathbb{P}[0 \text{ arrivals in } [0,t]] = e^{-\lambda t}$$
> so $S_1 \sim \text{Exp}(\lambda)$ and is independent of $S_0$.
>
> The same argument applies to any $S_n$:
> $$\mathbb{P}[S_n > t \mid S_i = s_i,\, i=0,\ldots,n-1] = e^{-\lambda t}$$
> by independent and stationary increments. $\square$

---

### M/G/1 Queue

The **M/G/1** model has:
- **M** (Memoryless) interarrival times: arrivals follow a Poisson process with rate $\lambda$
- **G** (General) service time distribution $G(x)$
- **1** server

The process $X(t)$ (queue size at time $t$) is **not** Markovian, because service times are not necessarily memoryless — the time until the next departure depends on how long the current customer has been served, which is not captured by $X_t$ alone.

**Solution — sample at departure times:** Let $t_n$ = time of $n$-th departure, $X_n \equiv X(t_n^+)$ = queue size just after departure $n$. Let $Y_n$ = number of arrivals during the service time of the $n$-th customer.

**Evolution:**

$$X_{n+1} = \begin{cases} X_n - 1 + Y_n & X_n \geq 1 \\ Y_n & X_n = 0 \end{cases} \tag{2.6}$$

![[Stochastic_Processes_2020_p35_img4.jpeg]]
*Figure 2.2 — Example evolution for the M/G/1 queueing system. Time axis shows service intervals; $X_n$ is evaluated just after each departure.*

![[Stochastic_Processes_2020_p36_img5.jpeg]]
*Figure 2.3 — Service times and departure times. $X_1=1$, so $X_2=2$, $X_3=1$, $X_4=0$, $X_5=1$.*

Since service times are random with CDF $G(x)$, the arrival count $Y_n$ during a service has distribution:

$$a_j \equiv \mathbb{P}\{Y_n = j\} = \int_0^\infty e^{-\lambda x} \frac{(\lambda x)^j}{j!}\,\mathrm{d}G(x)$$

This yields the same transition matrix structure as the discrete queueing model.

---

### G/M/1 Queue

The **G/M/1** model has:
- **G** (General) interarrival distribution $G(t)$
- **M** (Memoryless) service times: Exp$(\mu)$
- **1** server

Again $X(t)$ is not Markovian because $G$ is not memoryless — elapsed time since last arrival is needed. **Solution:** sample at **arrival times**.

Let $t_n$ = $n$-th arrival time, $X_n \equiv X(t_n^-)$ = queue size just before $n$-th arrival. Interarrival time $T \sim G(t)$; service times $\alpha_k$ i.i.d. Exp$(\mu)$.

**Transition probabilities** $P_{i,i+1-j} = \mathbb{P}[j \text{ departures during } T \mid X_n=i]$:

- **$j < i+1$ (some customers remain):**
$$\mathbb{P}[j \text{ departures} \mid X_n=i] = \int_0^{+\infty} \frac{e^{-\mu t}(\mu t)^j}{j!}\,\mathrm{d}G(t)$$
*(exactly $j$ Poisson$(\mu)$ events in the random interval $T$)*

- **$j = i+1$ (all customers depart):**
$$\mathbb{P}[i+1 \text{ departures} \mid X_n=i] = 1 - \int_0^{+\infty} \sum_{k=0}^{i} \frac{e^{-\mu t}(\mu t)^k}{k!}\,\mathrm{d}G(t)$$

- **$j > i+1$: impossible** ($P_{i,l}=0$ for $l > i+1$).

---

### Data Transmission Protocols

A buffer receives data and transmits it. Time is slotted with duration $T$. Let $\xi_n$ = data units generated in slot $n$, i.i.d. with $\mathbb{P}[\xi_n=k]=a_k$. Let $X_n$ = data in buffer at start of slot $n$. $\{X_n\}$ is a Markov chain.

#### Protocol 1

Send all buffered data up to max capacity $M$:

$$X_{n+1} = \begin{cases} \xi_n & X_n \leq M \\ X_n - M + \xi_n & X_n > M \end{cases}$$

**Transition matrix:**

$$P_{ij} = \begin{cases} a_j & i \leq M \\ a_{j+M-i} & i > M \end{cases}$$

![[Stochastic_Processes_2020_p40_img6.jpeg]]
*Figure 2.4 — Block diagram for Protocol 1. The first $M$ states all share the same transition row; from state $M+1$ onwards the row shifts.*

#### Protocol 2 (variant a — unlimited capacity, minimum $m$)

Send only if buffer $\geq m$ units; if so, send everything:

$$X_{n+1} = \begin{cases} \xi_n & X_n \geq m \\ X_n + \xi_n & X_n < m \end{cases}$$

![[Stochastic_Processes_2020_p41_img7.jpeg]]
*Figure 2.5 — Block diagram for Protocol 2a. States $0,\ldots,m-1$ accumulate data without sending; from state $m$ onwards all data is transmitted.*

#### Protocol 2 (variant b — finite $M$ and minimum $m$)

Combined: do nothing below $m$, send up to $M$ otherwise:

$$X_{n+1} = \begin{cases} X_n + \xi_n & X_n < m \\ \xi_n & m \leq X_n \leq M \\ X_n - M + \xi_n & X_n > M \end{cases}$$

![[Stochastic_Processes_2020_p42_img8.jpeg]]
*Figure 2.6 — Block diagram for Protocol 2b with minimum $m$ and bandwidth $M$.*

**Timeout extension of Protocol 2:** If data sits in the buffer below threshold $m$ for too many consecutive slots (e.g. 2), it is sent anyway. This is modelled by **replicating states** to track both $X_n$ and a timeout counter.

![[Stochastic_Processes_2020_p42_img9.jpeg]]
*Figure 2.7 — Protocol 2 with timeout: states are replicated to track the waiting counter. When the timeout expires, the buffer is flushed regardless of whether $m$ is reached.*

---

## First Step Analysis

**First step analysis** is a technique to study Markov chains by conditioning on the first transition. We use the law of total probability to write a recursive equation, then apply the Markov property to remove all but the latest condition.

> [!Important] Definition — Absorbing and Transient States
> - An **absorbing state** is one that, once entered, cannot be left: $P_{ii}=1$, $P_{ij}=0$ for $j\neq i$.
> - A **transient state** is one that will eventually be left permanently (with probability 1).

### Three-State Example

$$\mathbf{P} = \bordermatrix{ & 0 & 1 & 2 \cr 0 & 1 & 0 & 0 \cr 1 & \alpha & \beta & \gamma \cr 2 & 0 & 0 & 1 } \tag{2.8}$$

States $0$ and $2$ are **absorbing**; state $1$ is **transient**.

![[Stochastic_Processes_2020_p43_img10.jpeg]]
*Figure 2.8 — Block diagram for chain (2.8). State 1 transitions to 0 with prob $\alpha$, stays with prob $\beta$, goes to 2 with prob $\gamma = 1-\alpha-\beta$.*

**Absorption time:** $T \equiv \min\{n \geq 0 : X_n \in \{0,2\}\}$

**Absorption probability** $u = \mathbb{P}[X_T=0 \mid X_0=1]$:

By first-step analysis (law of total probability + Markov property):
$$u = 1\cdot\alpha + u\cdot\beta + 0\cdot\gamma$$

Interpretation: with prob $\alpha$ we reach 0 immediately (contribution $\alpha\cdot 1$); with prob $\gamma$ we reach 2 (contribution $\gamma\cdot 0$); with prob $\beta$ we return to 1 and the problem restarts (contribution $\beta\cdot u$). Solving:

$$u = \frac{\alpha}{1-\beta} = \frac{\alpha}{\alpha+\gamma}$$

**Mean absorption time** $\nu = \mathbb{E}[T \mid X_0=1]$:

$$\nu = 1 + \alpha\cdot 0 + \beta\cdot\nu + \gamma\cdot 0 = 1 + \beta\nu$$

The "1" counts the first step; absorbing states require no further steps; returning to 1 adds $\nu$ more. Solving:

$$\nu = \frac{1}{1-\beta}$$

**Verification:** the time spent in state 1 is geometrically distributed, so $\mathbb{P}[T>k \mid X_0=1]=\beta^k$, giving $\mathbb{E}[T]=\sum_{k=0}^\infty \beta^k = 1/(1-\beta)$. ✓

### Four-State Example

$$\mathbf{P} = \bordermatrix{ & 0 & 1 & 2 & 3 \cr 0 & 1 & 0 & 0 & 0 \cr 1 & P_{10} & P_{11} & P_{12} & P_{13} \cr 2 & P_{20} & P_{21} & P_{22} & P_{23} \cr 3 & 0 & 0 & 0 & 1 } \tag{2.9}$$

![[Stochastic_Processes_2020_p45_img11.jpeg]]
*Figure 2.9 — Block diagram for the 4-state absorbing chain. States 0 and 3 are absorbing; states 1 and 2 are transient.*

**Absorption probabilities** $u_i = \mathbb{P}[X_T=0 \mid X_0=i]$ for $i=1,2$:

$$u_1 = 1\cdot P_{10} + 0\cdot P_{13} + u_1\cdot P_{11} + u_2\cdot P_{12} \tag{2.10}$$

$$u_2 = 1\cdot P_{20} + 0\cdot P_{23} + u_1\cdot P_{21} + u_2\cdot P_{22} \tag{2.11}$$

Solve the linear system (2.10)–(2.11) for $u_1, u_2$.

**Mean absorption times** $\nu_i = \mathbb{E}[T \mid X_0=i]$:

$$\nu_1 = 1 + \nu_1 P_{11} + \nu_2 P_{12}$$
$$\nu_2 = 1 + \nu_1 P_{21} + \nu_2 P_{22}$$

### General Absorbing Markov Chain (Rewards)

**General setup:** $N+1$ states; states $0,\ldots,r-1$ are **transient**, states $r,\ldots,N$ are **absorbing**. Transition matrix in block form:

$$\mathbf{P} = \begin{pmatrix} \mathbf{Q} & \mathbf{R} \\ \mathbf{0} & \mathbf{I} \end{pmatrix}$$

where $\mathbf{Q}$ governs transitions among transient states and $\mathbf{R}$ governs transitions from transient to absorbing states.

**Absorption probabilities:** $U_{ik} = \mathbb{P}[\text{absorbed at } k \mid X_0=i]$ for $0\leq i<r$, $r\leq k\leq N$:

$$U_{ik} = P_{ik} + \sum_{j=0}^{r-1} P_{ij} U_{jk} \qquad i=0,1,\ldots,r-1$$

---

### General Absorbing Markov Chain (Rewards)

Consider a **reward function** $g: \text{transient states} \to \mathbb{R}$ — visiting state $j$ earns reward $g(j)$. The **expected cumulative reward** before absorption is:

$$w_i = \mathbb{E}\!\left[\sum_{n=0}^{T-1} g(X_n) \;\Big|\; X_0=i\right] \qquad i=0,\ldots,r-1$$

**Special cases:**
- $g(i)=1$ $\forall i$: $w_i = \nu_i$ (mean absorption time).
- $g(i)=\delta_{ik}$ for a fixed transient state $k$: $w_i = W_{ik}$ (expected number of visits to $k$).

**First-step analysis:**

$$w_i = g(i) + \sum_{j=0}^{r-1} P_{ij} w_j \qquad i=0,\ldots,r-1 \tag{2.14}$$

For $g(j)=\delta_{jk}$ this becomes:

$$W_{ik} = \delta_{ik} + \sum_{j=0}^{r-1} P_{ij} W_{jk} \qquad \forall i=0,1,\ldots,r-1 \tag{2.15}$$

---

## Two-State Markov Chain

$$\mathbf{P} = \begin{pmatrix} 1-a & a \\ b & 1-b \end{pmatrix}, \qquad 0 < a,b < 1$$

![[Stochastic_Processes_2020_p48_img12.jpeg]]
*Figure 2.10 — Block diagram for the two-state chain. State 0 transitions to 1 with prob $a$; state 1 transitions to 0 with prob $b$.*

> [!Important] Theorem — $n$-Step Transition Matrix for Two-State Chain
> **Statement:**
> $$\mathbf{P}^n = \frac{1}{a+b}\begin{pmatrix} b & a \\ b & a \end{pmatrix} + \frac{(1-a-b)^n}{a+b}\begin{pmatrix} a & -a \\ -b & b \end{pmatrix} \tag{2.16}$$
>
> Equivalently, with $\mathbf{A} = \begin{pmatrix}b&a\\b&a\end{pmatrix}$ and $\mathbf{B} = \begin{pmatrix}a&-a\\-b&b\end{pmatrix}$:
> $$\mathbf{P}^n = (a+b)^{-1}\left[\mathbf{A} + (1-a-b)^n \mathbf{B}\right] \tag{2.17}$$
>
> **Proof (by induction):**
>
> *Base case $n=1$:*
> $$\mathbf{P}^1 = \frac{1}{a+b}\begin{pmatrix}b+a(1-a-b) & a-a(1-a-b)\\b-b(1-a-b) & a+b(1-a-b)\end{pmatrix}$$
> After algebra:
> $$= \frac{1}{a+b}\begin{pmatrix}(1-a)(a+b) & a(a+b)\\b(a+b) & (1-b)(a+b)\end{pmatrix} = \begin{pmatrix}1-a&a\\b&1-b\end{pmatrix} = \mathbf{P} \checkmark$$
>
> *Induction step:* Assume (2.17) holds for $n$. Then:
> $$\mathbf{P}^{n+1} = \mathbf{P}^n \mathbf{P} = (a+b)^{-1}[\mathbf{A} + (1-a-b)^n\mathbf{B}]\mathbf{P}$$
> Key identities:
> $$\mathbf{AP} = \mathbf{A}; \qquad \mathbf{BP} = (1-a-b)\mathbf{B}$$
> Therefore:
> $$\mathbf{P}^{n+1} = (a+b)^{-1}[\mathbf{A} + (1-a-b)^{n+1}\mathbf{B}] \qquad\square$$
>
> **Asymptotic behaviour:** For $0 < a,b < 1$ we have $|1-a-b|<1$, so $(1-a-b)^n \to 0$:
> $$\lim_{n\to\infty} \mathbf{P}^n = \frac{1}{a+b}\begin{pmatrix}b&a\\b&a\end{pmatrix}$$
> Both rows are identical: the long-run distribution is independent of the initial state.
> - $\mathbb{P}[\text{state }0] = b/(a+b)$
> - $\mathbb{P}[\text{state }1] = a/(a+b)$
>
> **Application — Packet Errors:** Model state 0 = correct transmission, state 1 = error. Then:
> $$P_e = \frac{a}{a+b}, \qquad \langle L\rangle = \frac{1}{b}$$
> where $P_e$ is average error probability and $\langle L\rangle$ is mean burst length.

---

### Markov Chains Defined by Independent Random Variables

Let $\xi_1,\xi_2,\ldots$ be i.i.d. with $\mathbb{P}[\xi_i=k]=a_k$. Three Markov chains can be constructed:

1. **Direct sampling:** $X_n = \xi_n$. All rows of $\mathbf{P}$ are identical $(a_0,a_1,a_2,\ldots)$ since $X_{n+1}=\xi_{n+1}$ is independent of $X_n$.

2. **Successive maxima:** $X_n = \max\{\xi_1,\ldots,\xi_n\}$. Since $X_{n+1}=\max\{X_n,\xi_{n+1}\}$, only $X_n$ matters. Transition matrix:
$$\mathbf{P} = \begin{pmatrix} A_0 & a_1 & a_2 & a_3 & \cdots \\ 0 & A_1 & a_2 & a_3 & \cdots \\ 0 & 0 & A_2 & a_3 & \cdots \\ \vdots & & & \ddots & \end{pmatrix}, \qquad A_k = \sum_{i=0}^k a_i$$
(Upper triangular because the maximum is non-decreasing.)

3. **Partial sums:** $X_n = \xi_1 + \cdots + \xi_n$ with $X_0=0$.

---

### One-Dimensional Random Walks

A particle on a line can: stay at state $i$ with prob $r_i$, move right to $i+1$ with prob $p_i$, or move left to $i-1$ with prob $q_i$. Requires $q_i+r_i+p_i=1$.

**Gambler's Ruin:** States $0$ and $N$ are absorbing (player loses/wins); at every step the score changes ($r_i=0$, $p+q=1$). Starting from state $k$, define $u_k = \mathbb{P}[X_T=0 \mid X_0=k]$ (loss probability).

> [!Important] Gambler's Ruin — Closed Form
> **First-step analysis:**
> $$u_k = pu_{k+1} + qu_{k-1}, \qquad u_0=1,\; u_N=0$$
>
> **Solution:** Introduce $x_k = u_k - u_{k-1}$. The recursion gives $x_{k+1} = (q/p)x_k$, so:
> $$x_k = \left(\frac{q}{p}\right)^{k-1} x_1$$
>
> Since $u_k = 1 + \sum_{i=1}^k x_i$ (using $u_0=1$):
> $$u_k = 1 + x_1\frac{1-(q/p)^k}{1-(q/p)}, \qquad q \neq p$$
>
> Applying $u_N=0$ to find $x_1$ and substituting back:
>
> $$u_k = \begin{cases} \dfrac{N-k}{N} & p=q=\frac{1}{2} \\[8pt] \dfrac{(q/p)^k - (q/p)^N}{1-(q/p)^N} & p \neq q \end{cases} \qquad k=1,\ldots,N-1$$
>
> $$u_0 = 1, \qquad u_N = 0$$
>
> **Infinite opponent ($N\to\infty$):**
> $$u_k \xrightarrow{N\to\infty} \begin{cases} 1 & p \leq q \\ (q/p)^k & p > q \end{cases}$$
>
> **Intuition:** If $p < q$ (player at a disadvantage) ruin is certain. If $p=q$ (fair game) ruin is also certain — any finite initial capital will eventually be lost to fluctuations given infinite time. Only if $p>q$ can the player survive indefinitely, with non-zero survival probability $(1-(q/p)^k) > 0$.

![[Stochastic_Processes_2020_p54_img13.jpeg]]
*Figure 2.11 — $p/q$ defines the drift of the player's score. $p/q<1$: certain ruin. $p/q=1$: no drift, eventual ruin by fluctuations. $p/q>1$: positive drift, finite ruin probability.*

---

### Success Runs and Layer 2 Protocol

A **success run** Markov chain has states $0,1,2,\ldots$ where from state $i$: advance to $i+1$ with prob $q_i$, stay with prob $r_i$, or reset to 0 with prob $p_i$. Transition matrix:

| | 0 | 1 | 2 | 3 | 4 | $\cdots$ |
|---|---|---|---|---|---|---|
| **0** | $p_0$ | $q_0$ | 0 | 0 | 0 | $\cdots$ |
| **1** | $p_1$ | $r_1$ | $q_1$ | 0 | 0 | $\cdots$ |
| **2** | $p_2$ | 0 | $r_2$ | $q_2$ | 0 | $\cdots$ |
| **3** | $p_3$ | 0 | 0 | $r_3$ | $q_3$ | $\cdots$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ |

![[Stochastic_Processes_2020_p54_img14.jpeg]]
*Figure 2.12 — Block diagram for the success run chain. Any state can return to 0 with some probability.*

**Application — Layer 2 Retransmission Protocol:** Send a packet; if unacknowledged, retransmit up to $L+1$ total trials. Let $X_n$ = number of failed transmissions. At each state $i < L$: fail again (prob $\epsilon$) → state $i+1$; succeed (prob $1-\epsilon$) → absorbing state $S$. At state $L$: succeed → $S$; fail → absorbing state $F$ (discard).

![[Stochastic_Processes_2020_p55_img15.jpeg]]
![[Stochastic_Processes_2020_p55_img16.jpeg]]
*Figure 2.13 — Block diagram for the Layer 2 protocol. $S$ = success (packet delivered), $F$ = failure (packet discarded after $L+1$ attempts).*

> [!Example] Layer 2 Protocol Analysis
> **Problem:** Find the success probability $u_0$, mean transmission attempts $\nu_0$, and throughput.
>
> **Solution:**
>
> **Absorption probability** $u_i = \mathbb{P}[X_T=S \mid X_0=i]$:
> $$u_i = \begin{cases} \epsilon u_{i+1} + 1-\epsilon & i < L \\ 1-\epsilon & i=L \end{cases}$$
>
> Iterate backwards from $u_L$:
> $$u_0 = \epsilon^L u_L + \sum_{j=0}^{L-1}\epsilon^j(1-\epsilon) = \epsilon^L(1-\epsilon) + (1-\epsilon)\frac{1-\epsilon^L}{1-\epsilon} = 1-\epsilon^{L+1}$$
>
> This equals the probability of not failing $L+1$ consecutive times. ✓
>
> **Mean number of attempts** $\nu_i$: with $\nu_L = 1$:
> $$\nu_i = \epsilon\nu_{i+1} + 1, \qquad i < L$$
> $$\nu_0 = \epsilon^L + \frac{1-\epsilon^L}{1-\epsilon} = \frac{1-\epsilon^{L+1}}{1-\epsilon}$$
>
> **Throughput:**
> $$\text{Throughput} = \frac{u_0}{\nu_0} = \frac{1-\epsilon^{L+1}}{\frac{1-\epsilon^{L+1}}{1-\epsilon}} = 1-\epsilon$$
>
> **Takeaway:** The throughput equals the single-trial success probability $1-\epsilon$, regardless of $L$. This *intuitive* result will be proven rigorously in a later section.

---

### First Passage Times

> [!Important] Definition — First Passage Time
> The **first passage time** $\theta_{ij}$ from state $i$ to $j$ is the number of transitions to reach $j$ for the first time. Its distribution is:
> $$\mathbb{P}[\theta_{ij}=n] = f_{ij}(n) = \mathbb{P}[X_n=j,\, X_m\neq j,\, m=1,\ldots,n-1 \mid X_0=i]$$
> with $f_{ij}(0) \equiv 0$ for $i \neq j$.
>
> **First-step recursion:**
> $$f_{ij}(n) = P_{ij}\delta(n-1) + \sum_{k\neq j} P_{ik} f_{kj}(n-1)$$
> where $\delta(n)=1$ if $n=0$, else 0. For $n=1$ this gives $P_{ij}$ directly; for $n>1$, the system first moves to some $k\neq j$ and then reaches $j$ in $n-1$ more steps.

> [!Example] First Passage Times in the Two-State Chain
> **Problem:** Compute $f_{01}(n)$, $f_{11}(n)$, and their moments.
>
> **Solution:**
>
> For $f_{01}$:
> $$f_{01}(n) = P_{01}\delta(n-1) + P_{00}f_{01}(n-1) = \begin{cases} a & n=1 \\ (1-a)f_{01}(n-1) & n>1 \end{cases}$$
> Iterating: $f_{01}(n) = a(1-a)^{n-1}$ for $n\geq 1$ (geometric distribution).
>
> For $f_{11}$:
> $$f_{11}(n) = (1-b)\delta(n-1) + bf_{01}(n-1) = \begin{cases}1-b & n=1\\ ab(1-a)^{n-2} & n>1\end{cases}$$
>
> By symmetry ($a \leftrightarrow b$): $f_{10}(n) = b(1-b)^{n-1}$, $f_{00}(n)$ analogously.
>
> **Takeaway:** In the two-state model $f_{01}$ is geometric because: to go from 0 to 1 for the first time, the system must stay at 0 for $n-1$ steps (each with prob $1-a$) and then jump (prob $a$).

**Relation between $f_{ij}$ and $P^{(n)}_{ij}$:**

$$P^{(n)}_{ij} = \sum_{m=1}^n f_{ij}(m) P^{(n-m)}_{jj}$$

*(The chain reaches $j$ for the first time at step $m \leq n$, then stays at $j$ for the remaining $n-m$ steps.)*

Rearranging:

$$f_{ij}(n) = \begin{cases} 0 & n=0 \\ P_{ij} & n=1 \\ P^{(n)}_{ij} - \sum_{m=1}^{n-1} f_{ij}(m) P^{(n-m)}_{jj} & n\geq 2 \end{cases}$$

> [!Important] Mean First Passage Times — Recursive System
> From $\theta_{ij} = 1$ with prob $P_{ij}$, or $1+\theta_{kj}$ with prob $P_{ik}$ ($k\neq j$):
>
> $$\mathbb{E}[\theta_{ij}] = 1 + \sum_{k\neq j}^N P_{ik}\,\mathbb{E}[\theta_{kj}] \qquad \forall i, j \tag{2.28}$$
>
> (Uses normalization $\sum_k P_{ik}=1$.) For fixed $j$, this gives $N$ equations (for $i\neq j$) that determine all $\mathbb{E}[\theta_{ij}]$, then:
> $$\mathbb{E}[\theta_{jj}] = 1 + \sum_{k\neq j} P_{jk}\,\mathbb{E}[\theta_{kj}]$$
>
> **Two-state results:**
> $$\mathbb{E}[\theta_{01}] = \frac{1}{a}, \quad \mathbb{E}[\theta_{10}] = \frac{1}{b}$$
> $$\mathbb{E}[\theta_{00}] = \frac{a+b}{b} = \left(\frac{b}{a+b}\right)^{-1}, \quad \mathbb{E}[\theta_{11}] = \frac{a+b}{a} = \left(\frac{a}{a+b}\right)^{-1}$$
>
> **Key observation:** $\mathbb{E}[\theta_{jj}]$ is the reciprocal of the long-run fraction of time spent in state $j$. The system visits $j$ "once every $\mathbb{E}[\theta_{jj}]$" steps.
>
> **Second moments:** From $\theta_{ij}^2 = 1$ with prob $P_{ij}$, or $(1+\theta_{kj})^2$ with prob $P_{ik}$:
> $$\mathbb{E}[\theta_{ij}^2] = P_{ij}\cdot 1^2 + \sum_{k\neq j}^N P_{ik}\,\mathbb{E}[(1+\theta_{kj})^2]$$
> Expand the square:
> $$= \underbrace{P_{ij} + \sum_{k\neq j}^N P_{ik}}_{1} + 2\sum_{k\neq j}^N P_{ik}\,\mathbb{E}[\theta_{kj}] + \sum_{k\neq j}^N P_{ik}\,\mathbb{E}[\theta_{kj}^2]$$
> Recognise the first sum as 1 (row normalization) and apply (2.28) to the middle sum ($\mathbb{E}[\theta_{ij}]-1 = \sum_{k\neq j}P_{ik}\mathbb{E}[\theta_{kj}]$):
> $$= 1 + 2(\mathbb{E}[\theta_{ij}]-1) + \sum_{k\neq j} P_{ik}\,\mathbb{E}[\theta_{kj}^2] = 2\mathbb{E}[\theta_{ij}] - 1 + \sum_{k\neq j} P_{ik}\,\mathbb{E}[\theta_{kj}^2]$$
>
> **Two-state results:**
> $$\mathbb{E}[\theta_{01}^2] = \frac{2\mathbb{E}[\theta_{01}]-1}{1-P_{00}} = \frac{2/a-1}{a} = \frac{2}{a^2}-\frac{1}{a}; \qquad \operatorname{Var}(\theta_{01}) = \frac{1-a}{a^2}$$
> $$\operatorname{Var}(\theta_{10}) = \frac{1-b}{b^2}$$
> $$\mathbb{E}[\theta_{00}^2] = 2\mathbb{E}[\theta_{00}]-1+P_{01}\mathbb{E}[\theta_{10}^2] = 1+\frac{a}{b}+\frac{2a}{b^2}$$
> $$\operatorname{Var}(\theta_{00}) = \mathbb{E}[\theta_{00}^2]-\mathbb{E}[\theta_{00}]^2 = \frac{a(2-a-b)}{b^2}$$

---

## Alternative First Step Analysis — Matrix Approach

Consider a chain with $N+1$ states: $0,\ldots,r-1$ transient, $r,\ldots,N$ absorbing. In block form:

$$\mathbf{P} = \begin{pmatrix} \mathbf{Q} & \mathbf{R} \\ \mathbf{O} & \mathbf{I} \end{pmatrix}$$

**Powers of $\mathbf{P}$:**

$$\mathbf{P}^n = \begin{pmatrix} \mathbf{Q}^n & (\mathbf{I}+\mathbf{Q}+\cdots+\mathbf{Q}^{n-1})\mathbf{R} \\ \mathbf{O} & \mathbf{I} \end{pmatrix} \tag{2.29}$$

(Proved by induction: $\mathbf{P}^2$, $\mathbf{P}^3$, and generalising.)

> [!Important] Fundamental Matrix $\mathbf{W} = (\mathbf{I}-\mathbf{Q})^{-1}$
> **Mean visit count:** For $0\leq i,j < r$, the mean number of visits to transient state $j$ before absorption, starting from $i$, is:
>
> $$W_{ij} = \mathbb{E}\!\left[\sum_{n=0}^{T-1}\mathbf{1}\{X_n=j\} \;\Big|\; X_0=i\right] = \lim_{n\to\infty}\sum_{l=0}^n Q_{ij}^{(l)}$$
>
> In matrix form, $\mathbf{W} = \mathbf{I} + \mathbf{Q}\mathbf{W}$, so:
> $$(\mathbf{I}-\mathbf{Q})\mathbf{W} = \mathbf{I} \implies \mathbf{W} = (\mathbf{I}-\mathbf{Q})^{-1} \tag{2.33}$$
>
> ![[Stochastic_Processes_2020_p63_img17.jpeg]]
>
> **Mean absorption time** (in vector form, $\boldsymbol{\nu} = (\nu_0,\ldots,\nu_{r-1})^T$):
>
> $$\boldsymbol{\nu} = \mathbf{W} \times \mathbf{1} = (\mathbf{I}-\mathbf{Q})^{-1}\times\mathbf{1} \tag{2.39}$$
>
> (Multiplying $\mathbf{W}$ by the all-ones vector sums each row, giving $\nu_i = \sum_j W_{ij}$.)
>
> **Absorption probabilities** $U_{ik} = \mathbb{P}[X_T=k \mid X_0=i]$:
>
> $$\mathbf{U} = \mathbf{W}\mathbf{R} = (\mathbf{I}-\mathbf{Q})^{-1}\mathbf{R} \tag{2.40}$$
>
> **Proof:** $U^{(n)}_{ik} = P^{(n)}_{ik}$; from (2.29) the top-right block is $(\mathbf{I}+\mathbf{Q}+\cdots+\mathbf{Q}^{n-1})\mathbf{R}$; taking $n\to\infty$ gives $\mathbf{W}\mathbf{R}$.
>
> **Intuition:** $W_{ij}$ counts the average number of times the chain visits transient state $j$ before absorption. The matrix $\mathbf{W}=(I-Q)^{-1}$ is the *fundamental matrix* of the absorbing chain and encodes all relevant quantities.

---

### Matrix Approach for Average First Passage Times

To compute $\mathbb{E}[\theta_{iN}]$ (mean first passage time from any $i$ to state $N$):

1. Treat $N$ as absorbing by replacing its row in $\mathbf{P}$ with $(0,\ldots,0,1)$:
$$\hat{\mathbf{P}} = \begin{pmatrix} \mathbf{Q} & \mathbf{r} \\ \mathbf{0} & 1 \end{pmatrix} \tag{2.42}$$
where $\mathbf{Q}$ is $N\times N$ and $\mathbf{r}$ is $N\times 1$.

2. The mean first arrival time $\mathbb{E}[\theta_{iN}]$ in the original chain equals the mean absorption time $\nu_i$ in $\hat{\mathbf{P}}$:
$$\mathbb{E}[\theta_{iN}] = \nu_i$$

3. Compute from (2.39):
$$\boldsymbol{\nu} = (\mathbf{I}-\mathbf{Q})^{-1}\times\mathbf{1}$$

Any state can be chosen as the "target" by relabelling.

---

## Summary Table

| Concept | Formula / Definition | Notes |
|---|---|---|
| Markov property | $\mathbb{P}\{X_{n+1}=j\mid X_0,\ldots,X_n\} = \mathbb{P}\{X_{n+1}=j\mid X_n\}$ | Future depends only on present |
| Transition matrix | $P_{ij}\geq 0$, $\sum_j P_{ij}=1$ | Each row is a probability distribution |
| Full specification | $\mathbb{P}\{X_0=i_0,\ldots,X_n=i_n\} = p_{i_0}P_{i_0i_1}\cdots P_{i_{n-1}i_n}$ | Requires $\mathbf{P}$ and initial dist. |
| $n$-step transition | $\mathbf{P}^{(n)} = \mathbf{P}^n$ | $n$-th power of transition matrix |
| Poisson process rate | $\mathbb{P}[X_{t+s}-X_s=n] = \frac{e^{-\lambda t}(\lambda t)^n}{n!}$ | Inter-arrivals i.i.d. Exp$(\lambda)$ |
| Two-state $\mathbf{P}^n$ | $(a+b)^{-1}[\mathbf{A}+(1-a-b)^n\mathbf{B}]$ | Decays to stationary distribution |
| Stationary dist. (2-state) | $\pi_0=b/(a+b)$, $\pi_1=a/(a+b)$ | Independent of initial state |
| First step analysis | $u_i = \sum_j P_{ij} u_j + \text{boundary terms}$ | Condition on first transition |
| Gambler's ruin | $u_k=(q/p)^k-(q/p)^N)/(1-(q/p)^N)$ for $p\neq q$ | Certain ruin if $p\leq q$ vs infinite opponent |
| Fundamental matrix | $\mathbf{W} = (\mathbf{I}-\mathbf{Q})^{-1}$ | Mean visits to transient states |
| Mean absorption time | $\boldsymbol{\nu} = \mathbf{W}\mathbf{1}$ | Sum of rows of $\mathbf{W}$ |
| Absorption probabilities | $\mathbf{U} = \mathbf{W}\mathbf{R}$ | Hitting probabilities |
| Mean FPT (general) | $\mathbb{E}[\theta_{ij}] = 1 + \sum_{k\neq j}P_{ik}\mathbb{E}[\theta_{kj}]$ | System of $N$ equations |
| Mean return time | $\mathbb{E}[\theta_{jj}] = 1/\pi_j$ | Inverse of stationary probability |

| Model | When to sample | Reason |
|---|---|---|
| Discrete queue | At start of each time slot | Deterministic slot structure |
| M/G/1 | At departure times | Service completion restores Markov property |
| G/M/1 | At arrival times | Memoryless service times recover Markov property |
| Protocol 1 | At start of each time slot | Fixed slot size |
