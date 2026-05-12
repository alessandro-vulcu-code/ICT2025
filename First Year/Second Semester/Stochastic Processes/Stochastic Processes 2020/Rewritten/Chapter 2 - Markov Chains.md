# Chapter 2 — Markov Chains

## Table of Contents

- [[#Introduction|Introduction]]
  - [[#Definition — Markov Chain and Transition Matrix|Definition — Markov Chain and Transition Matrix]]
  - [[#Theorem — Markov Chain Fully Specified by P and Initial Distribution|Theorem — Markov Chain Fully Specified by P and Initial Distribution]]
  - [[#Theorem — n-Step Transition Probabilities (Chapman-Kolmogorov)|Theorem — n-Step Transition Probabilities (Chapman-Kolmogorov)]]
  - [[#Example 2.1 — Joint and Conditional Probabilities|Example 2.1 — Joint and Conditional Probabilities]]
- [[#2.1 Models|2.1 Models]]
  - [[#2.1.1 Discrete Queueing|2.1.1 Discrete Queueing]]
- [[#2.2 Poisson Process|2.2 Poisson Process]]
  - [[#Theorem — Inter-Arrival Times are Exponential|Theorem — Inter-Arrival Times are Exponential]]
- [[#2.3 M/G/1 Queue|2.3 M/G/1 Queue]]
- [[#2.4 G/M/1 Queue|2.4 G/M/1 Queue]]
- [[#2.5 Data Transmission Protocols|2.5 Data Transmission Protocols]]
  - [[#Protocol 1|Protocol 1]]
  - [[#Protocol 2|Protocol 2]]
- [[#2.6 First Step Analysis|2.6 First Step Analysis]]
  - [[#Example — Three-State Absorbing Chain|Example — Three-State Absorbing Chain]]
  - [[#Example — Four-State Absorbing Chain|Example — Four-State Absorbing Chain]]
- [[#2.7 General Absorbing Markov Chain|2.7 General Absorbing Markov Chain]]
- [[#2.8 Two-State Markov Chain|2.8 Two-State Markov Chain]]
  - [[#Theorem — n-Step Transition Matrix for the Two-State Chain|Theorem — n-Step Transition Matrix for the Two-State Chain]]
  - [[#2.8.1 Markov Chains Defined by Independent Random Variables|2.8.1 Markov Chains Defined by Independent Random Variables]]
  - [[#2.8.2 One-Dimensional Random Walks|2.8.2 One-Dimensional Random Walks]]
    - [[#Example — Gambler's Ruin|Example — Gambler's Ruin]]
  - [[#2.8.3 Success Runs|2.8.3 Success Runs]]
    - [[#Example — Layer 2 Protocol|Example — Layer 2 Protocol]]
  - [[#2.8.4 First Passage Times|2.8.4 First Passage Times]]
    - [[#Definition — First Passage Time|Definition — First Passage Time]]
    - [[#Theorem — Mean First Passage Time (First-Step Analysis)|Theorem — Mean First Passage Time (First-Step Analysis)]]
- [[#2.9 Alternative First Step Analysis|2.9 Alternative First Step Analysis]]
  - [[#Theorem — Fundamental Matrix W|Theorem — Fundamental Matrix W]]
  - [[#Theorem — Mean Absorption Time via W|Theorem — Mean Absorption Time via W]]
  - [[#Theorem — Absorption Probabilities via W|Theorem — Absorption Probabilities via W]]
  - [[#2.9.1 Matrix Approach for Average First Passage Time|2.9.1 Matrix Approach for Average First Passage Time]]
- [[#Summary Table|Summary Table]]

---

## Introduction

A **Markov process** $\{X_t\}$ is a stochastic process with the property that, given the value of $X_t$, the values of the process in the future, i.e. $X_s$ for $s > t$, are not influenced by the values of $X_u$ in the past $u < t$. In other words, all the necessary information for predicting the system's future is contained in the present state.

A Markov process with discrete values ($X_t$ assumes values in a countable set) and discrete index (i.e. the index set $T$ is countable too) is called a **Markov chain**. In this case the **Markov property** states:

$$
\mathbb{P}\{X_{n+1}=j \mid X_0=i_0,\ldots,X_{n-1}=i_{n-1},X_n=i\} = \mathbb{P}\{X_{n+1}=j \mid X_n=i\}
$$

for any possible choice of the states $i_0,\ldots,i_n$, $i$, $j$, and for all time points $n$. We will usually label the states (i.e. values of $X_t$) with the non-negative integers $\mathbb{N}$.

The probability of $X_{n+1}$ being in state $j$ given that the previous state $X_n$ is in state $i$ is called the **one-step transition probability** and is denoted with $P^{n,n+1}_{ij}$:

$$
P^{n,n+1}_{ij} = \mathbb{P}\{X_{n+1}=j \mid X_n=i\}
$$

If $P^{n,n+1}_{ij} \equiv P_{ij}$ independent of $n$, then the Markov chain is called **homogeneous**, or that it has *stationary transition probabilities*. Most of the interesting cases have this property.

We can interpret $P_{ij}$ as entries in a matrix $\mathbf{P}$, which is called the **transition probability matrix**. Each row $i$ contains the probability distribution of the values of $X_{n+1}$ given that the present state is $X_n = i$. So, all elements in any row must sum to unity:

$$
P_{ij} \geq 0 \quad \forall\, i,j \in \mathbb{N}; \qquad \sum_{j=0}^{+\infty} P_{ij} = 1 \quad \forall\, i \in \mathbb{N}
$$

The matrix $\mathbf{P}$ and the initial state $X_0$ (or, in general, the initial probability distribution over all states) fully specify a Markov chain.

---

> [!Important] Theorem — Markov Chain Fully Specified by P and Initial Distribution
> **Statement:** The matrix $\mathbf{P}$ and the initial distribution $\{p_i\} = \mathbb{P}(X_0 = i)$ fully specify a Markov chain, in the sense that they allow computing the joint probability of any sequence of states.
>
> **Proof:**
> Suppose that the initial distribution is given by $\mathbb{P}(X_0 = i) = p_i$. The Markov chain is *fully specified* if we can compute the (joint) probability of *any sequence of states* $\{i_0,\ldots,i_n\}$:
> $$
> \mathbb{P}\{X_0=i_0, X_1=i_1, \ldots, X_n=i_n\} \tag{2.1}
> $$
> Then the probability of any event $E$ will be the *sum* of the probabilities associated with the sequences *contained* in that event. For example, if we wish to compute the probability of $X_i = j$, we sum the probabilities of all possible *evolutions* of the system that verify this equation, which are always in the form (2.1).
>
> By definition of conditional probabilities we can rewrite (2.1) as follows:
> $$
> \mathbb{P}\{X_0=i_0,\ldots,X_n=i_n\} = \mathbb{P}\{X_n=i_n \mid X_0=i_0,\ldots,X_{n-1}=i_{n-1}\} \cdot \mathbb{P}\{X_0=i_0,\ldots,X_{n-1}=i_{n-1}\} \tag{2.2}
> $$
>
> Then we apply the Markov property:
> $$
> \mathbb{P}\{X_n=i_n \mid X_0=i_0,\ldots,X_{n-1}=i_{n-1}\} = \mathbb{P}\{X_n=i_n \mid X_{n-1}=i_{n-1}\} = P_{i_{n-1},i_n} \tag{2.3}
> $$
>
> Substituting (2.3) in (2.2) we obtain:
> $$
> \mathbb{P}\{X_0=i_0,\ldots,X_n=i_n\} = P_{i_{n-1},i_n}\,\mathbb{P}\{X_0=i_0,\ldots,X_{n-1}=i_{n-1}\}
> $$
>
> Reiterating this factorization step by step down to $n=0$:
> $$
> \mathbb{P}\{X_0=i_0,X_1=i_1,\ldots,X_n=i_n\} = p_{i_0} P_{i_0,i_1} \cdots P_{i_{n-2},i_{n-1}} P_{i_{n-1},i_n}
> $$
>
> And so all joint probabilities can be computed if we know $\{p_i\}_{i\in\mathbb{N}}$ and the transition matrix $\mathbf{P}$. $\square$
>
> **Intuition:** The Markov property means that the chain has no memory beyond its current state. Knowing $\mathbf{P}$ and $p_0$ is therefore equivalent to knowing the full stochastic dynamics: each trajectory probability factors into an initial probability and a product of one-step transition probabilities.

---

To understand the behaviour of a Markov Chain we may inspect the **$n$-step transition probabilities**, i.e. the probabilities of the process going from a certain state $i$ to a state $j$ in exactly $n$ transitions:

$$
P_{ij}^{(n)} \equiv \mathbb{P}\{X_{m+n}=j \mid X_m=i\}
$$

which is independent of $m$ for a homogeneous Markov chain.

> [!Important] Theorem — n-Step Transition Probabilities (Chapman-Kolmogorov)
> **Statement:** The $n$-step transition probabilities of a Markov chain can be written recursively as:
> $$
> P_{ij}^{(n)} = \sum_{k=0}^{+\infty} P_{ik}\, P_{kj}^{(n-1)}
> $$
> where:
> $$
> P^{(0)}_{ij} \equiv \begin{cases} 1 & \text{if } i=j \\ 0 & \text{if } i\neq j \end{cases}
> $$
>
> **Proof:**
> We start from the definition, taking $m=0$ (as the process is homogeneous):
> $$
> P^{(n)}_{ij} = \mathbb{P}\{X_n=j \mid X_0=i\}
> $$
>
> We consider the state $X_1$ at time $1$, and apply the law of total probability, noting that events $X_1=k$ for different values of $k$ are both mutually exclusive and exhaustive:
> $$
> = \sum_{k=0}^{+\infty} \mathbb{P}\{X_n=j,\, X_1=k \mid X_0=i\}
> $$
>
> Recall that $\mathbb{P}(AB) = \mathbb{P}(A|B)\mathbb{P}(B)$. Equivalently, conditioning on any event $C$:
> $$
> \mathbb{P}(AB \mid C) = \mathbb{P}(A \mid B,C)\,\mathbb{P}(B \mid C)
> $$
>
> And so:
> $$
> P^{(n)}_{ij} = \sum_{k=0}^{+\infty} \mathbb{P}\{X_n=j \mid X_1=k,X_0=i\}\, \mathbb{P}(X_1=k \mid X_0=i)
> $$
>
> Applying the Markov property we can *remove* the condition $X_0=i$ in the first term, as all the information about the *past* is still contained in $X_1$:
> $$
> = \sum_{k=0}^{+\infty} \underbrace{\mathbb{P}\{X_n=j \mid X_1=k\}}_{P^{(n-1)}_{kj}} \underbrace{\mathbb{P}(X_1=k \mid X_0=i)}_{P_{ik}} = \sum_{k=0}^{+\infty} P_{ik}\, P^{(n-1)}_{kj} \quad \square
> $$
>
> Note that this recursion is a **matrix multiplication**:
> $$
> \mathbf{P}^{(n)} = \mathbf{P} \times \mathbf{P}^{(n-1)}
> $$
> Reiterating:
> $$
> \mathbf{P}^{(n)} = \underbrace{\mathbf{P} \times \cdots \times \mathbf{P}}_{n\text{ factors}} = \mathbf{P}^n
> $$
>
> **Intuition:** The $n$-step probability of going from $i$ to $j$ can be computed by summing over all possible intermediate states $k$ visited at step 1. This is the probabilistic analog of matrix exponentiation: the $(i,j)$ entry of $\mathbf{P}^n$ gives the probability of a path of length $n$ from $i$ to $j$.

---

![[Stochastic_Processes_2020_p30_img3.jpeg]]
*Figure 2.1 — Markov chain graph for Exercise 2.1. Nodes represent states; directed edges are labelled with transition probabilities.*

> [!Example] Example 2.1 — Computing Joint and Conditional Probabilities
> **Problem:** (From exercise 3.1.1 in the textbook.) A Markov chain $\{X_i\}_{i\in\mathbb{N}}$ on states $0, 1, 2$ has the transition probability matrix:
> $$
> \mathbf{P} = \begin{pmatrix} 0.1 & 0.2 & 0.7 \\ 0.9 & 0.1 & 0 \\ 0.1 & 0.8 & 0.1 \end{pmatrix}
> $$
> and initial distribution:
> $$
> \boldsymbol{p} = (p_0, p_1, p_2)^T = \begin{pmatrix} 0.3 \\ 0.4 \\ 0.3 \end{pmatrix}
> $$
> Determine $\mathbb{P}\{X_0=0, X_1=1, X_2=2\}$.
>
> **Approach:** Use the joint probability factorization from the theorem above: $\mathbb{P}\{X_0=i_0, X_1=i_1, X_2=i_2\} = p_{i_0} P_{i_0 i_1} P_{i_1 i_2}$.
>
> **Solution:**
> 1. Follow the diagram. The probability of starting at $X_0 = 0$ is $p_0 = 0.3$, then we multiply by each transition probability:
> $$
> \mathbb{P}\{X_0=0, X_1=1, X_2=2\} = p_0\, P_{01}\, P_{12} = 0.3 \cdot 0.2 \cdot 0 = 0
> $$
> *(Note: The source actually computes $\mathbb{P}\{X_0=0, X_1=1, X_2=1\}$ in the example:)*
> $$
> \mathbb{P}\{X_0=0, X_1=1, X_2=1\} = p_0\, P_{01}\, P_{11} = 0.3 \cdot 0.2 \cdot 0.1 = 0.006
> $$
>
> 2. For non-consecutive states, e.g. $\mathbb{P}\{X_0=0, X_1=1, X_3=1\}$, we need the 2-step transition probability — summing over all intermediate states:
> $$
> \mathbb{P}\{X_0=0, X_1=1, X_3=1\} = p_0 \cdot P_{01}\, P_{11}^{(2)} = \sum_{k=0}^{2} p_0\, P_{01}\, P_{1k}\, P_{k1} = p_0\, P_{01} \sum_{k=0}^{2} P_{1k}\, P_{k1}
> $$
> The last sum is the scalar product between row 1 and column 1 of $\mathbf{P}$.
>
> 3. For conditional probabilities, e.g. $\mathbb{P}[X_3=1, X_1=1 \mid X_0=0]$: since we already know the initial state, we do not need to account for its probability, meaning that:
> $$
> \mathbb{P}[X_3=1, X_1=1 \mid X_0=0] = P_{01} \cdot P_{11}^{(2)}
> $$
>
> **Takeaway:** Joint probabilities factor as a product of initial distribution and one-step (or multi-step) transition probabilities. When conditioning on the initial state, drop $p_{i_0}$ and use $P_{ij}^{(n)}$ directly. The $n$-step matrix $\mathbf{P}^n$ handles non-consecutive time indices.

---

## 2.1 Models

Many natural physical processes can be approximately modelled by Markov chains, leading to several interesting analytical results. In this section we will study some of such examples.

### 2.1.1 Discrete Queueing

Consider a situation when customers arrive for service. In each time slot a single customer can be served, if there is one — otherwise nothing happens. If several people arrive at the same time, they will queue and wait for their turn.

Let's denote with $X_n$ the number of users in the system at the beginning of slot $n$. At any time slot we will have a certain (random) number of arrivals $\xi_n$, which is a random variable with probability distribution:

$$
\mathbb{P}[\xi_n = k] = a_k
$$

where we assume that $a_k$ is independent of $n$ (the arrival rate is uniform, and arrivals are uncorrelated). If the system contains at least one customer at time slot $n$ (i.e. $X_n > 0$), we will have a departure, otherwise not:

$$
X_{n+1} = \begin{cases} X_n - 1 + \xi_n & X_n > 0 \\ \xi_n & X_n = 0 \end{cases}
$$

We can rewrite this more compactly as:

$$
X_{n+1} = (X_n - 1)^+ + \xi_n
$$

where $Y^+ \equiv \max(Y, 0)$. Note that if we know $X_n$, we can fully characterize $X_{n+1}$ without knowing the states $X_u$ with $u < n$ — and so this is indeed a Markov chain.

The **transition probability matrix** is given by:

$$
\mathbf{P} = \begin{pmatrix} a_0 & a_1 & a_2 & a_3 & a_4 & \cdots \\ a_0 & a_1 & a_2 & a_3 & a_4 & \cdots \\ 0 & a_0 & a_1 & a_2 & a_3 & \cdots \\ 0 & 0 & a_0 & a_1 & a_2 & \cdots \\ 0 & 0 & 0 & a_0 & a_1 & \cdots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}
$$

The first row ($n=0$) is given by the probability distribution $\{a_i\}_{i\in\mathbb{N}}$: the system starts empty, $k$ customers enter with probability $a_k$, and so the system moves to state $X_k$.

For the second row ($n=1$), we start with 1 customer, who is served and goes away. So, at the end we will just have the $k$ new arrivals — recreating the same situation as the first row.

The situation changes from the third row ($n=2$) onward, as now $n-1 > 0$ customers remain in the queue, and so the system cannot transition to states $X_k$ with $k < n-1$, meaning that $0$s appear in $\mathbf{P}$. All transitions to the other states have probabilities $\{a_k\}$, shifted to the right by the queue size $n-1$.

The **arrival rate** is defined by the average:

$$
\langle \xi_k \rangle = \sum_{k=0}^{+\infty} k\, a_k
$$

If $\langle \xi_k \rangle > 1$, the queue size will diverge, as at every time slot more customers arrive than depart. We say that, in this case, the system is **unstable**. On the other hand, if $\langle \xi_k \rangle < 1$, the queue size will remain finite. The boundary case $\langle \xi_k \rangle = 1$ is trickier to analyse. We will see that if the arrivals are deterministic (exactly one customer arrives at every time slot), the system will be stable. But as soon as the arrivals are non-deterministic, the system exhibits instability.

---

## 2.2 Poisson Process

An important class of Markov chains is given by **Poisson processes**, which can be used to model situations where independent events occur at random points in time.

Let $X_t$ be the number of events (e.g. arrivals) occurring in $[0, t]$. Then we define:

1. $X_0 = 0$, meaning that no events can happen if the "experiment" is run for 0 time.
2. Increments are both **stationary** and **independent**. With increments we denote differences of random variables, such as $X_{t_2} - X_{t_1}$ for $t_2 > t_1$, representing the number of events contained in $[0, t_2]$ which are not present in $[0, t_1]$. Equivalently, $X_{t_2} - X_{t_1}$ is the number of events happening in $[t_1, t_2]$.

   *Independent increments* means that, if we take disjoint intervals $I_1 = [t_1, t_2]$ and $I_2 = [t_3, t_4]$, with $I_1 \cap I_2 = \varnothing$, then the number of events happening in $I_1$ and $I_2$ are independent:
   $$
   X_{t_2} - X_{t_1} \text{ and } X_{t_4} - X_{t_3} \text{ are independent r.v.} \Leftrightarrow [t_1,t_2] \cap [t_3,t_4] = \varnothing
   $$

   *Stationary increments* means that the numbers of events occurring in (disjoint) time intervals of the same size follow the same distribution:
   $$
   X_{s+t} - X_s \sim X_{s'+t} - X_{s'} \quad \text{if } [s,s+t] \cap [s',s'+t] = \varnothing
   $$
   In other words, the distribution of the number of events inside an interval depends only on that interval's size $t$.

3. The probability of $n$ events occurring inside an interval of size $t$, regardless of its position, is given by a Poisson distribution:
   $$
   \mathbb{P}[X_{t+s} - X_s = n] = \frac{e^{-\lambda t}(\lambda t)^n}{n!} \tag{2.5}
   $$
   where $\lambda$ represents the average number of events occurring per unit time.

Equivalently, we can specify the distribution by requiring that:

$$
\mathbb{P}[X_h \geq 1] = \lambda h + o(h)
$$
$$
\mathbb{P}[X_h \geq 2] = o(h)
$$

with $o(h)$ denoting a function such that $\lim_{h \to 0} \frac{o(h)}{h} = 0$.

*(Note: the source has a possible OCR artifact on the first line, reading "$=\lambda h + o(k) = p(k)$"; the correct expression is $\lambda h + o(h)$.)*

This means that in a *very small interval* $[0, h]$, the probability of at least one event happening (i.e. $X_h \geq 1$) is linear in $h$, whereas the probability of 2 or more events happening in that interval is negligible. In other words, "simultaneous arrivals" — events occurring "really close to each other" — are very rare and can be neglected (events are "rare").

(The proof of the equivalence between these two definitions is omitted.)

> [!Important] Theorem — Inter-Arrival Times are Exponential
> **Statement:** In a Poisson process, the inter-arrival times (i.e. the time between two consecutive events) are i.i.d. exponential random variables with parameter $\lambda$.
>
> **Proof:**
> Let $\{S_i\}_{i\in\mathbb{N}}$ be the inter-arrival times, and $W_n$ the *cumulative* arrival times, defined as:
> $$
> W_n = \sum_{i=0}^{n} S_i
> $$
>
> Let's consider the first inter-arrival time $S_0$. The probability that $S_0 > t$ is the probability of no arrivals in $[0,t]$:
> $$
> \mathbb{P}[S_0 > t] = \mathbb{P}[0 \text{ arrivals in } [0,t]] \underset{(2.5)}{=} e^{-\lambda t}
> $$
> and so $S_0$ follows an exponential distribution with parameter $\lambda$.
>
> We now consider the next inter-arrival time $S_1$:
> $$
> \mathbb{P}[S_1 > t \mid S_0 = s] = \mathbb{P}[0 \text{ arrivals in } (s, s+t] \mid S_0 = s]
> $$
>
> The number of arrivals in disjoint intervals are independent, and so we can drop the condition $S_0 = s$. Applying stationarity we know that this probability depends only on the size of the interval, which is the same as that of $[0, t]$, and so we get the same result as before:
> $$
> = e^{-\lambda t}
> $$
> This means that also $S_1$ follows an exponential distribution with parameter $\lambda$, and is independent of $S_0$.
>
> The same argument can be repeated for any given $S_n$:
> $$
> \mathbb{P}[S_n > t \mid S_i = s_i,\, i=0,\ldots,n-1] = \mathbb{P}[0 \text{ arrivals in } (s_0+\cdots+s_{n-1},\, s_0+\cdots+s_{n-1}+t) \mid S_i = s_i] = e^{-\lambda t}
> $$
> which completes the proof. $\square$
>
> **Intuition:** The exponential distribution is the continuous analog of the geometric distribution, and it is the unique memoryless distribution on $\mathbb{R}^+$. Since Poisson arrivals are independent and stationary, the time until the next event carries no memory of the past — exactly the property that characterizes the exponential distribution.

---

## 2.3 M/G/1 Queue

A more complex model for the queueing system is given by considering different service times for each customer, and treating arrivals as a Poisson process. This leads to the **M/G/1** model.

- The first letter denotes the type of the interarrival distribution, which in this case is intended to be "*Memoryless*", and thus exponential.
- The second letter describes the distribution of the service time. $G$ stands for "*general*", meaning that we don't make any assumption on that pdf.
- The $1$ at the end is the number of servers, i.e. the number of clients that can be served at once.

As in the previous case, a customer arriving when the server is free will go immediately to service, while others will wait their turn in an orderly queue. If at any time there are no customers being served and no arrivals, no service will be given.

We could be tempted to define $X(t)$ as the number of customers in the system at $t$, and then consider the stochastic process $\{X(t), t \geq 0\}$. Unfortunately, this is **not a Markovian process**, as it does not satisfy the Markov property. The amount of time elapsed from the last arrival *does not matter* for the distribution of arrival times (as it is memoryless). However, the departure times *do* depend on past information. As we assume a *generic* distribution for the service time, it won't necessarily be memoryless, meaning that the time until the next departure depends on how much time has passed from the service's start, which is information *not contained* in just the state $X_t$.

Note that in the previous example we circumvented this problem by fixing a definite, deterministic duration for the service: one customer is served in a single time slot. Here we are not making such an assumption.

To reduce the system to a Markov process, we can just include the necessary information (how much time the user currently being served has been there) in the current state. However, this will make the model much more complex.

Another way is to **discretize time**, by sampling $X_t$ just at the departure times. This is a variation of the "time slots" we used in the first examples — however in this case the time slots are not all of the same size, and their duration is not deterministic.

In fact, when a customer departs at instant $\bar{t}$, the behaviour of the system is fully specified by the $X_{\bar{t}}$ at that time. If $X_{\bar{t}} > 0$, then the next user in queue will be served; if $X_{\bar{t}} = 0$, nothing happens.

This is one example of a more general trick: often a process $\{X_t\}_{t \in \mathbb{R}^+}$ is not a Markov process, but a "discretized sample" $\{X_{t_i}\}_{i\in\mathbb{N}}$ for a certain "good" choice of instants $\{t_i\}$ is a Markov process.

![[Stochastic_Processes_2020_p35_img4.jpeg]]
*Figure 2.2 — Example of evolution for the M/G/1 queuing system, showing departures at times $t_1, t_2, \ldots$ and the queue size just after each departure.*

So, let's denote with $t_n$ the time of the $n$-th departure, and with $X_n \equiv X(t_n^+)$ ($n \geq 1$) the number of customers in the system left behind by the $n$-th departure, as illustrated in fig. 2.2.

We also denote with $Y_n$ ($n \geq 0$) the number of arrivals occurring during the service time for the $n$-th customer, which is given by the difference between $t_n$ and the arrival time of that customer. If the queue size is $> 0$, then the latter will simply be $t_{n-1}$, as illustrated in fig. 2.3.

![[Stochastic_Processes_2020_p36_img5.jpeg]]
*Figure 2.3 — Service times and departure times for the M/G/1 queuing system. Note that $X_1 \equiv X(t_1^+) = 1$, and so $X_2 = 2$, $X_3 = 1$, $X_4 = 0$ and $X_5 = 1$.*

With this notation, we can describe the system's evolution:

$$
X_{n+1} = \begin{cases} X_n - 1 + Y_n & X_n \geqslant 1 \\ Y_n & X_n = 0 \end{cases} \tag{2.6}
$$

The system starts empty ($X_0 = 0$). One customer arrives, is served, and then departs, meaning that he/she will not count towards $X_1$, which is evaluated after their departure. What we need to count is the number of arrivals $Y_1$ in that service time, and so $X_1 = Y_1$, which equals 1 in the case of fig. 2.3.

If the system is not empty at time $t_n$, then one customer from the queue will immediately enter service, meaning that $X_{n+1} = (X_n - 1)$, plus the number of arrivals $Y_n$ in the previous service time. For example, in fig. 2.3, we have $X_1 = 1$, $Y_1 = 2$ (2 arrivals in that service time), and so $X_2 = 1 - 1 + 2 = 2$.

So, the only difference of (2.6) from the previous simpler case is that now $Y_n$ is the number of arrivals during an interval of *random* size. If the interval's size $X$ had a fixed value $x$, we could write:

$$
\mathbb{P}\{Y_n = j\} = e^{-\lambda x} \frac{(\lambda x)^j}{j!}
$$

But since $X$ is not fixed, but a random variable with cdf $G(x)$, we need to construct an average:

$$
a_j \equiv \mathbb{P}\{Y_n = j\} = \int_0^\infty e^{-\lambda x} \frac{(\lambda x)^j}{j!}\, \mathrm{d}G(x) \qquad j \in \mathbb{N}
$$

These probabilities represent the $a_j$ from the previous example, and as the evolution equation is also the same, we obtain the same transition probability matrix:

$$
\mathbf{P} = \begin{pmatrix} a_0 & a_1 & a_2 & a_3 & a_4 & \dots \\ a_0 & a_1 & a_2 & a_3 & a_4 & \dots \\ 0 & a_0 & a_1 & a_2 & a_3 & \dots \\ 0 & 0 & a_0 & a_1 & a_2 & \dots \\ 0 & 0 & 0 & a_0 & a_1 & \dots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}
$$

---

## 2.4 G/M/1 Queue

Suppose now that the interarrival times are i.i.d. random variables with a **generic distribution** $G$ (not necessarily memoryless), while the service times follow a memoryless distribution, which we suppose to be exponential with rate $\mu$.

Again, if we denote with $X_t$ the number of customers in the system at time $t$, $\{X(t)\}_{t \geq 0}$ is not a Markov process, due to the fact that $G$ is, in general, not memoryless. In particular, the elapsed time from the previous arrival is necessary information for constructing the distribution of the next arrival time, and it is not contained in the state $X_t$.

So, the idea is to consider — as before — a discrete subset $\{X_{t_i}\}_{i\in\mathbb{N}}$, choosing the instants $t_i$ such that the information missing in $X_t$ becomes irrelevant. In this case, the correct choice is to identify the $t_i$ with the **arrival times**: if we know that a customer has just arrived and the queue is free, then they will be served; otherwise they will wait in line. As the service time follows a memoryless distribution — meaning that it is completely characterized by the state at any time — the resulting $\{X_{t_i}\}$ is indeed a Markov process.

So, let's fix $t_n$ to be the time of the $n$-th arrival, and $X_n \equiv X(t_n^-)$ the number of customers in the system just before the $n$-th arrival. The interarrival time is denoted by $T \sim G(t)$, while the service times are $\alpha_k$ i.i.d. r.v. with exponential distribution $\exp(\mu)$.

We then consider the transition probabilities:

$$
P_{i,\, i+1-j} = \mathbb{P}[j\text{ departures}] \qquad j = 0, 1, \ldots, i+1 \tag{2.7}
$$

In other words, if a customer arrives at $t_n$, while there are $i$ customers in the system ($X_n = i$), then the number of customers just before the next arrival $X_{n+1}$ will be $i$ (customers initially in queue) $+1$ (the customer just arrived) $-j$ (the departures during the interarrival time $T$). Note that there cannot be more departures than the number of clients $i+1$, and so $j \leq i+1$.

To compute the transition probabilities (2.7) we distinguish between three cases:

**Case $j < i+1$ (some customers remain):**

We rewrite (2.7) noting that if $j$ departures occur during the time interval $T$, it means that the sum of $j$ inter-departure times $\alpha_k$ "fits" in $T$, but adding one more departure time would surpass $T$:

$$
\mathbb{P}[j\text{ departures} \mid X_n=i] = \mathbb{P}\left[\sum_{k=1}^{j}\alpha_k \leq T < \sum_{k=1}^{j+1}\alpha_k\right]
$$

This is the probability of observing exactly $j$ Poisson events in the interval $T$. Averaging over the distribution of $T$:

$$
= \int_0^{+\infty} \frac{e^{-\mu t}(\mu t)^j}{j!}\, \mathrm{d}G(t)
$$

**Case $j = i+1$ (all users depart):**

There is no "next departure" to consider, leading to:

$$
\mathbb{P}[i+1\text{ departures} \mid X_n=i] = \mathbb{P}\left[\sum_{k=1}^{i+1}\alpha_k \leq T\right] = \mathbb{P}[\text{at least } i+1 \text{ Poisson events in } [0,T]]
= \int_0^{+\infty} \sum_{k=i+1}^{+\infty} \frac{e^{-\mu t}(\mu t)^k}{k!}\, \mathrm{d}G(t)
$$

We can rewrite the infinite sum by normalization. Since the full Poisson sum equals 1:

$$
1 = \int_0^{+\infty} \sum_{k=0}^{+\infty} \frac{e^{-\mu t}(\mu t)^k}{k!}\, \mathrm{d}G(t) = \int_0^{+\infty} \sum_{k=0}^{i} \frac{e^{-\mu t}(\mu t)^k}{k!}\, \mathrm{d}G(t) + \int_0^{+\infty} \sum_{k=i+1}^{+\infty} \frac{e^{-\mu t}(\mu t)^k}{k!}\, \mathrm{d}G(t)
$$

and so:

$$
\mathbb{P}[i+1\text{ departures} \mid X_n=i] = 1 - \int_0^{+\infty} \sum_{k=0}^{i} \frac{e^{-\mu t}(\mu t)^k}{k!}\, \mathrm{d}G(t)
$$

**Case $j > i+1$ (more departures than clients):**

As previously commented, this is impossible:

$$
\mathbb{P}[\text{more than } i+1 \text{ departures} \mid X_n=i] = P_{i,l} = 0 \qquad l > i+1
$$

---

## 2.5 Data Transmission Protocols

Another example of a system that can be modelled by Markov processes is given by **data transmission protocols**.

In particular, we consider a buffer that receives some data, and relays it to some other machine. For simplicity, we discretize time in equal slots of $T$ seconds each, and specify that during each slot data is transmitted (if available).

Denote with $\xi_k$ the amount of data generated during time slot $n$. The $\xi_k$ are random variables with statistics given by:

$$
\mathbb{P}[k\text{ data units generated in slot } n] \equiv \mathbb{P}[\xi_k = k] = a_k \qquad k \geq 0
$$

We consider two different protocols for sending data:

1. At the beginning of each slot, all data is scheduled for transmission, up to a max of $M$ units (link capacity), which is given by the product of the output speed and the time slot duration $T$. All remaining data will be left in the buffer, and will be served during next slots.

2. In a real case, sending data requires attaching headers and controls to packets, introducing a certain amount of overhead. If the amount of data sent is sufficiently high, this overhead is relatively small. However, if the buffer sends only a few bytes, the overhead will be significant, and the procedure inefficient.

   So, a better protocol will prevent the sending of "too little" data by specifying a **minimum data size** $m$ for transmission. In other words, the buffer will wait for at least $m$ units of data before sending them. So, at the start of each time slot:
   - (a) If there is less than $m$ data in the buffer, do nothing.
   - (b) If more than $m$ data: send all data, up to a max of $M$ units.

Note that in both protocols, the choice of what data to send is scheduled at the start of each time slot. In this way, all data that arrives during a slot will be sent at best during the next time slot.

So, let's denote with $X_n$ the amount of data in the buffer at the beginning of the $n$-th time slot. $\{X_n\}_{n\in\mathbb{N}}$ is a Markov chain, because the buffer status at any given time $X_{n+1}$ depends only on the content at the previous step ($X_n$) and the amount of data $(\xi_n)$ arriving during time slot $n$, with $\{\xi_n\}$ being i.i.d. random variables.

### Protocol 1

If at the beginning of time slot $n$ there is less than $M$ data in the buffer, we send all of it, and the buffer at the next time will only contain the newly arrived data $\xi_n$. Otherwise, we send $M$ units of data, leaving $X_n - M$ in the buffer, plus the newly arrived data $\xi_n$. So the system's evolution is:

$$
X_{n+1} = \begin{cases} \xi_n & X_n \leq M \\ X_n - M + \xi_n & X_n > M \end{cases}
$$

The full transition matrix becomes:

$$
P_{ij} = \begin{cases} a_j & i \leq M \\ a_{j+M-i} & i > M \end{cases} \qquad
\mathbf{P} = \begin{pmatrix}
a_0 & a_1 & a_2 & \dots & \dots & \dots & \dots & \dots \\
a_0 & a_1 & a_2 & \dots & \dots & \dots & \dots & \dots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
a_0 & a_1 & a_2 & \dots & \dots & \dots & \dots & \dots \\
0 & a_0 & a_1 & a_2 & \dots & \dots & \dots & \dots \\
0 & 0 & a_0 & a_1 & a_2 & \dots & \dots & \dots \\
\vdots & \ddots & \ddots & \ddots & \ddots & \ddots & \ddots & \ddots
\end{pmatrix}
$$

and is represented by the block diagram in fig. 2.4.

![[Stochastic_Processes_2020_p40_img6.jpeg]]
*Figure 2.4 — Block diagram for Protocol 1. The transition probabilities between the first $M$ states are all the same, and "start to change" for the $M+1$ state onwards.*

### Protocol 2

We examine two variants: one where $M = +\infty$ (case 2a), and one with finite $M$ (case 2b).

**Case (2a)** — unlimited bandwidth. The evolution becomes:

$$
X_{n+1} = \begin{cases} \xi_n & X_n \geq m \\ X_n + \xi_n & X_n < m \end{cases}
$$

In other words, if the data is enough ($\geq m$), we send it all (as there is no size limit), and the next state will hold just the newly arrived data $\xi_n$. Otherwise, we keep all current data $X_n$, without sending anything, and also add the newly arrived data $\xi_n$.

The transition matrix becomes:

$$
P_{ij} = \begin{cases} a_j & X_n \geq m \\ a_{j-i} & X_n < m \end{cases}
$$

The first $m$ rows (states $0, \ldots, m-1$, below the threshold) shift the distribution by $i$: from state $i$, the system goes to state $i + k$ with probability $a_k$. From state $m$ onward (above threshold), the distribution resets to $\{a_j\}$ as in Protocol 1 (row $\leq M$).

![[Stochastic_Processes_2020_p41_img7.jpeg]]
*Figure 2.5 — Block diagram for Protocol (2a), with minimum transfer size $m$ and unlimited bandwidth.*

**Case (2b)** — minimum size $m$ with finite bandwidth $M$. This is a combination of Protocol 1 and case (2a). The system's evolution is:

$$
X_{n+1} = \begin{cases} X_n + \xi_n & X_n < m \\ \xi_n & m \leq X_n \leq M \\ X_n - M + \xi_n & X_n > M \end{cases}
$$

The transition matrix is:

| State | $0$ | $1$ | $2$ | $\cdots$ | $m{-}2$ | $m{-}1$ | $\cdots$ |
|-------|-----|-----|-----|----------|---------|---------|---------|
| $0$ | $a_0$ | $a_1$ | $a_2$ | $\cdots$ | $\cdots$ | $\cdots$ | $\cdots$ |
| $1$ | $0$ | $a_0$ | $a_1$ | $\cdots$ | $\cdots$ | $\cdots$ | $\cdots$ |
| $\vdots$ | $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ | $\vdots$ |
| $m{-}1$ | $0$ | $0$ | $0$ | $\cdots$ | $0$ | $a_0$ | $\cdots$ |
| $m$ | $a_0$ | $a_1$ | $a_2$ | $a_3$ | $\cdots$ | $\cdots$ | $\cdots$ |
| $m{+}1$ | $a_0$ | $a_1$ | $a_2$ | $a_3$ | $\cdots$ | $\cdots$ | $\cdots$ |
| $\vdots$ | $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ | $\vdots$ |
| $M$ | $a_0$ | $a_1$ | $a_2$ | $a_3$ | $\cdots$ | $\cdots$ | $\cdots$ |
| $M{+}1$ | $0$ | $a_0$ | $a_1$ | $a_2$ | $\cdots$ | $\cdots$ | $\cdots$ |
| $M{+}2$ | $0$ | $0$ | $a_0$ | $a_1$ | $\cdots$ | $\cdots$ | $\cdots$ |
| $\vdots$ | $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ | $\cdot$ | $\vdots$ |

with the block diagram represented in fig. 2.6.

![[Stochastic_Processes_2020_p42_img8.jpeg]]
*Figure 2.6 — Block diagram for Protocol (2b), with minimum transfer size $m$ and limited bandwidth $M$.*

Protocol 2, while more realistic than version 1, may lead to problems. For example, suppose that we receive too little data to send, and for many consecutive time slots we do not receive any more data. In this situation, the buffer's content will be sent after a long time — and so, paradoxically, the optimization we considered to make the system more efficient now leads to a very inefficient behaviour. We can fix this by limiting the maximum number of consecutive empty slots when the queue is not empty. In other words, if we have some data ($\leq m$) in the buffer, and do not receive enough data to surpass $m$ for a certain number of time slots (e.g. 2), we will send all the buffer's content anyway. This leads to the block diagram of fig. 2.7, where we "replicate states", as we are keeping track of both $X_n$ and a "timeout counter" for sending data.

![[Stochastic_Processes_2020_p42_img9.jpeg]]
*Figure 2.7 — Block diagram for Protocol 2, with minimum transfer size $m$ and a "timeout" for sending data of 2 time slots. If the $m$ threshold is not reached after 2 time slots, then the buffer's content is sent anyway.*

---

## 2.6 First Step Analysis

A very useful technique for studying Markov chains is the so-called **first step analysis**, where essentially we study the probabilities conditioned on the initial state, and write recursive relations for the system's state.

> [!Example] Example — Three-State Absorbing Chain
> **Problem:** Consider the Markov chain with transition probability matrix:
> $$
> \mathbf{P} = \begin{array}{c|ccc} & 0 & 1 & 2 \\ \hline 0 & 1 & 0 & 0 \\ 1 & \alpha & \beta & \gamma \\ 2 & 0 & 0 & 1 \end{array} \tag{2.8}
> $$
> *(Note: the source OCR shows only 2 data columns; the third column with $\gamma$ for row 1 and $0$ for rows 0 and 2 is reconstructed from prose context.)*
>
> The relative block diagram is represented in fig. 2.8.
>
> ![[Stochastic_Processes_2020_p43_img10.jpeg]]
> *Figure 2.8 — Block diagram for the Markov chain (2.8).*
>
> States 0 and 2 do not admit transitions to other states, and so they are called **absorbing states**: if the system enters one of them, it can never leave. On the other hand, state 1 does not admit transitions *from* other states, and so is called a **transient state**: the system can be in state 1 for a time, but after that it will never return there.
>
> **Problem:** What is the probability that the system will get "trapped" in state 0? How long will it take to reach an absorbing state?
>
> **Approach:** First step analysis. Define:
> - Absorption time: $T \equiv \min\{n \geq 0 : X_n \in \{0, 2\}\}$
> - Absorption probability of state 0: $u = \mathbb{P}[X_T = 0 \mid X_0 = 1]$
> - Average absorption time: $\nu = \mathbb{E}[T \mid X_0 = 1]$
>
> **Solution — absorption probability $u$:**
>
> In first step analysis we condition on the possible values $X_1$ the system can take after the first step:
> $$
> u = \mathbb{P}[X_T=0 \mid X_0=1] = \sum_{k=0}^{2} \mathbb{P}[X_T=0 \mid X_0=1,\, X_1=k]\, \mathbb{P}[X_1=k \mid X_0=1]
> $$
>
> Applying the Markov property to remove all conditions but the latest:
> $$
> = \sum_{k=0}^{2} \mathbb{P}[X_T=0 \mid X_1=k]\, \mathbb{P}[X_1=k \mid X_0=1]
> $$
>
> Expanding the sum using the transition probabilities from (2.8):
> $$
> = 1 \cdot \alpha + u \cdot \beta + 0 \cdot \gamma
> $$
>
> - From $X_0=1$ we may go to $X_1=0$ with probability $\alpha$: absorption probability is 1.
> - From $X_0=1$ we could go to $X_1=2$ with probability $\gamma$: absorption probability is 0.
> - With probability $\beta$ the system stays at $X_1=1$: by the Markov property the system "forgets" its past, and the absorption probability is again $u$.
>
> Rearranging $u = \alpha + \beta u$:
> $$
> u = \frac{\alpha}{1-\beta} = \frac{\alpha}{\alpha + \gamma}
> $$
>
> **Solution — mean absorption time $\nu$:**
>
> Applying the same reasoning:
> $$
> \nu = 1 + \alpha \cdot 0 + \beta \cdot \nu + \gamma \cdot 0 = 1 + \beta\nu
> $$
>
> We need to count the first step; with probability $\alpha+\gamma$ the system moves to an absorbing state (no more steps required), and with probability $\beta$ the system remains in 1 with expected remaining time $\nu$. Rearranging:
> $$
> \nu = \frac{1}{1-\beta}
> $$
>
> We can verify this: the amount of time spent in state 1 has a **geometric distribution**. Since every transition to other states from 1 leads to an absorbing state, the absorption time equals the time spent in state 1:
> $$
> \mathbb{P}[T > k \mid X_0=1] = \beta^k \Rightarrow \mathbb{E}[T \mid X_0=1] = \sum_{k=0}^{+\infty} \mathbb{P}[T>k \mid X_0=1] = \frac{1}{1-\beta}
> $$
>
> However, this direct computation will be impossible in more complex cases, while the first-step approach will still remain feasible.
>
> **Takeaway:** First-step analysis converts absorption probability / mean absorption time into a linear equation (or system) that can be solved algebraically. The key step is conditioning on $X_1$ and applying the Markov property.

> [!Example] Example — Four-State Absorbing Chain
> **Problem:** Consider the slightly more complex 4-state system:
> $$
> \mathbf{P} = \begin{array}{c|cccc} & 0 & 1 & 2 & 3 \\ \hline 0 & 1 & 0 & 0 & 0 \\ 1 & P_{10} & P_{11} & P_{12} & P_{13} \\ 2 & P_{20} & P_{21} & P_{22} & P_{23} \\ 3 & 0 & 0 & 0 & 1 \end{array} \tag{2.9}
> $$
> *(Note: the source OCR drops one column from each data row; the 4×4 structure is reconstructed from equations (2.10)–(2.11).)*
>
> ![[Stochastic_Processes_2020_p45_img11.jpeg]]
> *Figure 2.9 — Block diagram for the Markov chain (2.9). States 0 and 3 are absorbing; states 1 and 2 are transient.*
>
> **Approach:** First step analysis on both transient states simultaneously. Define:
> $$
> u_i = \mathbb{P}[X_T = 0 \mid X_0 = i] \qquad i = 1,2 \qquad T = \min\{n \geq 0 : X_n \in \{0,3\}\}
> $$
> $$
> \nu_i = \mathbb{E}[T \mid X_0 = i] \qquad i = 1,2
> $$
>
> **Solution:**
>
> First-step analysis applied to initial state 1:
> $$
> u_1 = 1 \cdot P_{10} + 0 \cdot P_{13} + u_1 \cdot P_{11} + u_2 \cdot P_{12} \tag{2.10}
> $$
>
> Similarly, for initial state 2:
> $$
> u_2 = 1 \cdot P_{20} + 0 \cdot P_{23} + u_1 \cdot P_{21} + u_2 \cdot P_{22} \tag{2.11}
> $$
>
> Equations (2.10) and (2.11) form a linear system that can be solved to find $u_1$ and $u_2$.
>
> The same reasoning applied to $\nu_i$:
> $$
> \nu_1 = 1 + 0 \cdot (P_{10}+P_{13}) + \nu_1 \cdot P_{11} + \nu_2 \cdot P_{12}
> $$
> $$
> \nu_2 = 1 + 0 \cdot (P_{20}+P_{23}) + \nu_1 \cdot P_{21} + \nu_2 \cdot P_{22}
> $$
>
> **Takeaway:** With multiple transient states, first-step analysis produces a *system* of linear equations (one per transient state), which is solved simultaneously. Absorbing states contribute known boundary values (0 or 1 for probabilities, 0 for expected additional time).

---

In a more general case, we will have states $0, 1, \ldots, N$. Suppose that $0, 1, \ldots, r-1$ are transient states, and $r, \ldots, N$ are absorbing. The transition matrix has the form:

$$
\mathbf{P} = \begin{pmatrix} \mathbf{Q} & \mathbf{R} \\ \mathbf{0} & \mathbf{I} \end{pmatrix}
$$

where $\mathbf{Q}$ regulates transitions between transient states, $\mathbf{R}$ the ones between transient and absorbing states, and the last $N-r$ rows have $0$s for the first $r$ entries with exactly a single $1$ in the rest.

As in general there are more than 2 absorbing states, we need to specify which one we are considering for the absorption probabilities. For absorbing state $k$:

$$
U_{ik} = \mathbb{P}[\text{Absorption in } k \mid X_0 = i] = P_{ik} + \sum_{j=0}^{r-1} P_{ij} U_{jk} \qquad i = 0, 1, \ldots, r-1
$$

---

## 2.7 General Absorbing Markov Chain

Consider some kind of **metric** $g(X)$, a function mapping each transient state to a real number. We suppose that every time the chain visits a state $j$, the metric rises by the value of $g(j)$. In other words, $g(j)$ is the "reward" earned by the process by visiting $j$.

As before, we label all states so that the first $r$ are transient, and the last $N-r$ are absorbing.

Denoting with $T$ the absorption time for a process starting in state $i$, the **average cumulative value** of the metric is given by:

$$
w_i = \mathbb{E}\left[\sum_{n=0}^{T-1} g(X_n) \,\Big|\, X_0=i\right] \qquad i = 0, \ldots, r-1
$$

**Special case $g(i) = 1\ \forall i$:** The cumulative value equals the lifetime of the process:

$$
\sum_{n=0}^{T-1} g(X_n) = \sum_{n=0}^{T-1} 1 = T
$$

And so $\nu_i = \mathbb{E}[T \mid X_0=i]$ is the mean time until absorption.

**Special case $g(i) = \delta_{ik}$ for a transient state $k$:** We are only counting visits to state $k$. In this case, $w_i$ is the **expected number of visits** $W_{ik}$ from initial state $i$ to state $k$ before absorption.

We compute the explicit values by first-step analysis:

$$
w_i = g(i) + \sum_{j=0}^{r-1} P_{ij}\, w_j \qquad i = 0, \ldots, r-1 \tag{2.14}
$$

As the process starts from $i$, the "reward" $g(i)$ is always earned. Then the process moves to a transient state $j$, earning an average reward of $w_j$. We get a system of $r$ equations in $r$ unknowns.

In the case of $g(j) = \delta_{jk}$, equation (2.14) reduces to:

$$
W_{ik} = \delta_{ik} + \sum_{j=0}^{r-1} P_{ij}\, W_{jk} \qquad \forall\, i = 0, 1, \ldots, r-1 \tag{2.15}
$$

---

## 2.8 Two-State Markov Chain

Consider the Markov chain with transition matrix:

$$
\mathbf{P} = \begin{array}{c|cc} & 0 & 1 \\ \hline 0 & 1-a & a \\ 1 & b & 1-b \end{array} \qquad 0 < a, b < 1
$$

![[Stochastic_Processes_2020_p48_img12.jpeg]]
*Figure 2.10 — Block diagram for the two-state Markov chain. State 0 transitions to 1 with probability $a$; state 1 transitions to 0 with probability $b$.*

In this particular case we can compute analytically the $n$-step transition matrix:

$$
\mathbf{P}^n = \frac{1}{a+b}\begin{pmatrix} b & a \\ b & a \end{pmatrix} + \frac{(1-a-b)^n}{a+b}\begin{pmatrix} a & -a \\ -b & b \end{pmatrix} \tag{2.16}
$$

We can rewrite it in a more compact form by introducing:

$$
\mathbf{A} = \begin{pmatrix} b & a \\ b & a \end{pmatrix} \qquad \mathbf{B} = \begin{pmatrix} a & -a \\ -b & b \end{pmatrix}
$$

So that (2.16) becomes:

$$
\mathbf{P}^n = (a+b)^{-1}\left[\mathbf{A} + (1-a-b)^n \mathbf{B}\right] \tag{2.17}
$$

> [!Important] Theorem — n-Step Transition Matrix for the Two-State Chain
> **Statement:** For the two-state chain with transition matrix $\mathbf{P} = \begin{pmatrix}1-a & a \\ b & 1-b\end{pmatrix}$, the $n$-step matrix is given by (2.16)/(2.17).
>
> **Proof:**
> By induction. We start with proving the $n=1$ base case, and then show that if (2.16) holds up to $n$, then it holds also for $n+1$.
>
> **Base case $n=1$:**
> $$
> \mathbf{P}^1 = \frac{1}{a+b}\begin{pmatrix}b & a \\ b & a\end{pmatrix} + \frac{1-a-b}{a+b}\begin{pmatrix}a & -a \\ -b & b\end{pmatrix}
> = \frac{1}{a+b}\begin{pmatrix}b+a-a^2-ab & a-a+a^2+ab \\ b-b+ab+b^2 & a+b-ab-b^2\end{pmatrix}
> $$
> $$
> = \frac{1}{a+b}\begin{pmatrix}(1-a)(a+b) & a(a+b) \\ b(a+b) & (1-b)(a+b)\end{pmatrix}
> = \begin{pmatrix}1-a & a \\ b & 1-b\end{pmatrix} = \mathbf{P} \quad \checkmark
> $$
>
> **Induction step:** Assuming (2.17) holds for $n$:
> $$
> \mathbf{P}^{n+1} = \mathbf{P}^n \mathbf{P} \underset{(2.17)}{=} (a+b)^{-1}[\mathbf{A} + (1-a-b)^n \mathbf{B}]\mathbf{P}
> $$
>
> We compute $\mathbf{AP}$ and $\mathbf{BP}$ separately:
> $$
> \mathbf{AP} = \begin{pmatrix}b & a \\ b & a\end{pmatrix}\begin{pmatrix}1-a & a \\ b & 1-b\end{pmatrix} = \begin{pmatrix}b & a \\ b & a\end{pmatrix} = \mathbf{A}
> $$
> $$
> \mathbf{BP} = \begin{pmatrix}a & -a \\ -b & b\end{pmatrix}\begin{pmatrix}1-a & a \\ b & 1-b\end{pmatrix} = (1-a-b)\mathbf{B}
> $$
>
> Therefore:
> $$
> \mathbf{P}^{n+1} = (a+b)^{-1}[\mathbf{A} + (1-a-b)^{n+1}\mathbf{B}] \quad \square
> $$
>
> **Asymptotic behaviour:** Suppose that $|1-a-b| < 1$ (always true in the non-trivial cases $0 < a,b < 1$). Then $(1-a-b)^n \xrightarrow[n\to\infty]{} 0$, and:
> $$
> \lim_{n\to\infty} \mathbf{P}^n = \frac{1}{a+b}\begin{pmatrix}b & a \\ b & a\end{pmatrix}
> $$
>
> The two rows are equal, meaning that the asymptotic probability distribution does **not depend on the initial state**: the system will be in state 0 with probability $b/(a+b)$, and in 1 with probability $a/(a+b)$. In other words, the system "forgets" its initial condition. This is a typical behaviour for many Markov chains.
>
> **Intuition:** $\mathbf{A}$ captures the stationary component (time-independent), while $\mathbf{B}$ captures the transient component that decays geometrically. The decay rate is $|1-a-b|$: smaller $a+b$ (slower mixing) means slower convergence to stationarity.

**Application — Packet transmission and the two-state model.** One possible application of the two-state model is given by modelling the error rate of a packet transmission system with memory. Denote with state 0 the event of a correct transmission, and with 1 that of an error. Then the average packet error probability is:

$$
P_e = \frac{a}{a+b}
$$

Another interesting quantity is the **mean length of a burst of errors**, i.e. how long (on average) does the system spend in state 1. The mean length $L$ of such a sequence of erroneous states is a geometric random variable, whose average is the inverse of the probability of moving out of state 1:

$$
\langle L \rangle = \frac{1}{P_{10}} = \frac{1}{b}
$$

In a real scenario, we will need to provide redundancy so that the system can tolerate $\langle L \rangle$ consecutive errors.

### 2.8.1 Markov Chains Defined by Independent Random Variables

Let $\xi$ denote a discrete-valued random variable whose possible values are the non-negative integers, with $\mathbb{P}[\xi_i = i] = a_i \geq 0$ for $i \in \mathbb{N}$, and $\sum_{i=0}^{n} a_i = 1$. Let $\xi_1, \xi_2, \ldots, \xi_n, \ldots$ represent independent measurements of $\xi$.

We can use that sequence to construct Markov chains:

1. **Direct assignment:** We let $X_n = \xi_n$. The probability transition matrix then becomes:
   $$
   \mathbf{P} = \begin{pmatrix} a_0 & a_1 & a_2 & \cdots \\ a_0 & a_1 & a_2 & \cdots \\ a_0 & a_1 & a_2 & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}
   $$
   All rows are equal because all the $\xi_n$ are independent of each other.

2. **Successive maxima.** We define $X_n$ to be the maximum value assumed by the first $n$ random variables $\xi_i$:
   $$
   X_n = \max\{\xi_1, \ldots, \xi_n\} \qquad n = 1, 2, \ldots
   $$
   This is a Markov chain. In fact, any future state $X_{n+1}$ is completely determined by the current state $X_n$ and the outcome of the next r.v. $\xi_{n+1}$, which is i.i.d.:
   $$
   X_{n+1} = \max\{X_n, \xi_{n+1}\}
   $$
   The transition probability matrix is then:
   $$
   \mathbf{P} = \begin{pmatrix} A_0 & a_1 & a_2 & a_3 & \cdots \\ 0 & A_1 & a_2 & a_3 & \cdots \\ 0 & 0 & A_2 & a_3 & \cdots \\ 0 & 0 & 0 & A_3 & \cdots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}
   $$
   where $A_k = \sum_{i=0}^{k} a_i$.

3. **Partial sums.** Similarly to the previous example, we define:
   $$
   X_n = \xi_1 + \cdots + \xi_n \qquad n = 1, 2, \ldots
   $$
   with $X_0 \equiv 0$.

### 2.8.2 One-Dimensional Random Walks

Consider a particle moving on a line, such that, at any given time, it can only remain in the current state $i$ with probability $r_i$, or move to the neighbouring states with probability $q_i$ (left) or $p_i$ (right). This process is a special Markov chain called a **random walk**, with transition matrix:

$$
\mathbf{P} = \begin{array}{c|ccccccc} & 0 & 1 & 2 & \cdots & i-1 & i & i+1 \\ \hline 0 & r_0 & p_0 & 0 & \cdots & 0 & 0 & 0 \\ 1 & q_1 & r_1 & p_1 & \cdots & 0 & 0 & 0 \\ 2 & 0 & q_2 & r_2 & \cdots & 0 & 0 & 0 \\ \vdots & & & & & & & \\ i & 0 & 0 & 0 & \cdots & q_i & r_i & p_i \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \ddots \end{array}
$$

To "keep the walk going" we need $p_i, q_i > 0$, while $r_i \geq 0$. All rows sum to 1, meaning that $q_i + r_i + p_i = 1\ \forall i$.

**Random walks and games.** Random walks can be used to model games, by identifying the state $i$ with the player's score at a given time. If the player wins the next match, their score will go up. Conversely, if they lose, the state will decrease. Note that draws can be modelled by the player remaining in the same state.

Similarly, the state can model the amount of resources available to the player (i.e. wealth, or "health points"). If the player runs out of resources (they reach state 0), they lose. Conversely, the same holds for the opponent, so the state $N$ (maximum resources for the player) corresponds to the loss of the opponent. In this situation there are two absorbing states. We will study the asymptotic behaviour in the next sections.

#### Example — Gambler's Ruin

> [!Example] Example — Gambler's Ruin
> **Problem:** Suppose we are modelling a game's score with a random walk. States 0 and $N$ correspond respectively to the player losing or winning, and so they are absorbing states. We also suppose that, at each turn, the score always changes. The transition matrix is:
> $$
> \mathbf{P} = \begin{array}{c|cccccc} & 0 & 1 & 2 & 3 & \cdots & N \\ \hline 0 & 1 & 0 & 0 & \cdots & \cdots & 0 \\ 1 & q & 0 & p & 0 & \cdots & 0 \\ 2 & 0 & q & 0 & p & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & & \vdots & \vdots \\ N & 0 & 0 & 0 & \cdots & \cdots & 1 \end{array} \qquad p + q = 1
> $$
>
> If the initial state (i.e. initial amount of resources) is $k$, find the probability of losing:
> $$
> u_k = \mathbb{P}[X_T = 0 \mid X_0 = k] \tag{2.18}
> $$
> where $T = \min\{n \geq 0;\, X_n \in \{0,N\}\}$.
>
> **Approach:** First-step analysis yields the recursion $u_k = p u_{k+1} + q u_{k-1}$ with boundary conditions $u_0 = 1$, $u_N = 0$. Solve by substitution.
>
> **Solution:**
>
> 1. First-step analysis gives:
> $$
> u_k = p u_{k+1} + q u_{k-1} \qquad k = 1, \ldots, N-1
> $$
>
> 2. Rewrite using $p+q=1$:
> $$
> u_k = (p+q)u_k = p u_k + q u_k = p u_{k+1} + q u_{k-1}
> \Rightarrow q\underbrace{(u_k - u_{k-1})}_{x_k} = p(u_{k+1} - u_k)
> $$
>
> 3. Introduce the change of variables $x_k \equiv u_k - u_{k-1}$:
> $$
> k=1: \quad 0 = p(u_2 - u_1) - q(u_1 - u_0) = px_2 - qx_1
> $$
> $$
> k=2: \quad 0 = p(u_3 - u_2) - q(u_2 - u_1) = px_3 - qx_2
> $$
> $$
> \vdots
> $$
> $$
> k=N-1: \quad 0 = p(u_N - u_{N-1}) - q(u_{N-1} - u_{N-2}) = px_N - qx_{N-1}
> $$
>
> 4. Express each $x_{k+1}$ in terms of $x_k$:
> $$
> x_2 = \frac{q}{p}x_1 \Rightarrow x_3 = \left(\frac{q}{p}\right)^2 x_1 \Rightarrow \cdots \Rightarrow x_N = \left(\frac{q}{p}\right)^{N-1} x_1
> $$
>
> 5. Invert the change of variables (using $u_0 = 1$):
> $$
> u_k = 1 + \sum_{i=1}^{k} x_i \underset{(2.20)}{=} 1 + x_1 \sum_{i=1}^{k}\left(\frac{q}{p}\right)^{i-1} = 1 + x_1 \frac{1-(q/p)^k}{1-(q/p)} \qquad q \neq p \tag{2.22}
> $$
>
> 6. Apply $u_N = 0$ to find $x_1$:
> $$
> 0 \underset{(2.22)}{=} 1 + x_1 \frac{1-(q/p)^N}{1-(q/p)} \Rightarrow x_1 = -\frac{1-q/p}{1-(q/p)^N}
> $$
>
> 7. Substitute back in (2.22):
> $$
> u_k = 1 - \frac{1-(q/p)^k}{1-(q/p)}\cdot\frac{1-q/p}{1-(q/p)^N} = \frac{(q/p)^k - (q/p)^N}{1-(q/p)^N} \qquad q \neq p
> $$
>
> **Special case $p = q = 1/2$:** The geometric sum collapses to:
> $$
> u_k = 1 + kx_1 \qquad \text{with } x_1 = -\frac{1}{N} \Rightarrow u_k = 1 - \frac{k}{N} = \frac{N-k}{N}
> $$
>
> **Result:**
> $$
> u_k = \begin{cases} (N-k)/N & p=q=1/2 \\ \dfrac{(q/p)^k-(q/p)^N}{1-(q/p)^N} & p \neq q \end{cases} \qquad k=1,\ldots,N-1
> $$
> $$
> u_0 = 1 \qquad u_N = 0
> $$
>
> If we fix $k$, a larger $N$ leads to a higher probability of losing $u_k$, as the resources $N-k$ available to the opponent rise. Conversely, for $N$ fixed, $u_k$ vanishes for large $k$.
>
> For $N \to \infty$ (opponent "infinitely rich", as a casino):
> $$
> u_k \xrightarrow[N\to\infty]{} \begin{cases} 1 & p \leq q \\ (q/p)^k & p > q \end{cases}
> $$
>
> This means that if the player is at a disadvantage ($p < q$), they will certainly lose. However, if the player is likely to win each game ($p > q$), they may (in principle) continue playing indefinitely. Note that for any finite $k$ there is still a finite non-zero probability of losing equal to $(q/p)^k$, which vanishes for $k \to +\infty$.
> Note that the player will certainly lose even if the game is fair ($p=q$).
>
> ![[Stochastic_Processes_2020_p54_img13.jpeg]]
> *Figure 2.11 — The ratio $p/q$ defines the slope of the trend followed by the player's score. If $p/q < 1$, the player will certainly lose after some time. If $p/q = 1$ (fair game), the average player's score remains fixed at the initial state, and given infinite time a sufficiently high fluctuation will bring the player to ruin. If $p/q > 1$, the player can still lose, but on average their score will rise.*
>
> **Takeaway:** The gambler's ruin is the canonical first-step analysis problem. The key insight: even in a fair game ($p=q$), eventual ruin is certain for any finite starting capital against an infinitely rich opponent. The substitution $x_k = u_k - u_{k-1}$ converts the second-order recursion into a geometric ratio.

### 2.8.3 Success Runs

Consider the Markov chain with the following transition matrix:

| State | $0$ | $1$ | $2$ | $3$ | $4$ | $\cdots$ |
|-------|-----|-----|-----|-----|-----|---------|
| $0$ | $p_0$ | $q_0$ | $0$ | $0$ | $0$ | $\cdots$ |
| $1$ | $p_1$ | $r_1$ | $q_1$ | $0$ | $0$ | $\cdots$ |
| $2$ | $p_2$ | $0$ | $r_2$ | $q_2$ | $0$ | $\cdots$ |
| $3$ | $p_3$ | $0$ | $0$ | $r_3$ | $q_3$ | $\cdots$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\cdots$ |

Starting at state $i$, the system can move to $i+1$ with probability $q_i$, remain at $i$ with probability $r_i$, or go back to the starting state 0 with probability $p_i$.

![[Stochastic_Processes_2020_p54_img14.jpeg]]
*Figure 2.12 — Block diagram for the success run Markov chain. From any state, the chain either advances, stays, or resets to 0.*

**Timeouts.** This kind of chain can be used to model, for example, **timeout processes** — processes where a reset happens after a certain time, except when something else prevents it.

#### Example — Layer 2 Protocol

> [!Example] Example — Layer 2 Protocol
> **Problem:** We apply the success run model to a layer 2 protocol, where we want to send data packets between nodes connected by a link. The receiving node confirms the success of transmission by returning an acknowledgment message. If this does not happen, the packet needs to be re-transmitted. In practice, this is done for a maximum of $L+1$ total trials (including the first transmission), after which the packet is discarded.
>
> We denote with $X_n$ the number of failed transmissions of a packet. At every state $i < L$, there can be another transmission failure with probability $\epsilon$, leading to state $i+1$, or the packet can be correctly sent with probability $1-\epsilon$, leading to the final state $S$ (success). If the system reaches $L$ and fails one more time, it evolves to the final state $F$, where data is discarded.
>
> The transition probability matrix is given by:
>
> ![[Stochastic_Processes_2020_p55_img15.jpeg]]
>
> ![[Stochastic_Processes_2020_p55_img16.jpeg]]
> *Figure 2.13 — Block diagram for the layer 2 protocol. States $0$ through $L$ are transient; $S$ (success) and $F$ (failure/discard) are absorbing.*
>
> **Approach:** First-step analysis from the last state backward, using the recursion for $u_i = \mathbb{P}[X_T = S \mid X_0 = i]$.
>
> **Solution — success probability $u_0$:**
>
> First-step analysis gives:
> $$
> u_i = \mathbb{P}[X_T = S \mid X_0 = i] = \begin{cases} \epsilon\, u_{i+1} + 1-\epsilon & i < L \\ 1-\epsilon & i = L \end{cases}
> $$
>
> We know $u_L$, and from $u_{i+1}$ we can determine $u_i$. Starting from the last state and working backwards:
> $$
> u_0 = \epsilon u_1 + 1-\epsilon = \epsilon(\epsilon u_2 + 1-\epsilon) + 1-\epsilon = \epsilon^2 u_2 + (1-\epsilon)\epsilon + (1-\epsilon)
> $$
> $$
> = \epsilon^L u_L + \sum_{j=0}^{L-1} \epsilon^j(1-\epsilon) = \epsilon^L(1-\epsilon) + (1-\epsilon)\frac{1-\epsilon^L}{1-\epsilon} = 1 - \epsilon^{L+1}
> $$
>
> This makes sense: the probability of at least one success in $L+1$ trials is the probability of not failing $L+1$ consecutive times, which is $1 - \epsilon^{L+1}$.
>
> **Solution — mean number of attempts $\nu_0$:**
>
> The mean absorption time satisfies:
> $$
> \nu_i = \epsilon\,\nu_{i+1} + 1 \qquad i < L \qquad \nu_L = 1
> $$
>
> Iterating backwards:
> $$
> \nu_0 = \epsilon\nu_1 + 1 = \epsilon^2\nu_2 + \epsilon + 1 = \cdots = \epsilon^L\nu_L + \sum_{j=0}^{L-1}\epsilon^j = \epsilon^L + \frac{1-\epsilon^L}{1-\epsilon} = \frac{1-\epsilon^{L+1}}{1-\epsilon}
> $$
>
> **Result — Throughput:**
>
> Let's consider a sequence of transmissions. Each packet has probability $u_0 = 1-\epsilon^{L+1}$ of being correctly sent, and the mean sending time is $\nu_0 = (1-\epsilon^{L+1})/(1-\epsilon)$. The ratio of these two averages is the mean **throughput** of the channel:
> $$
> \text{Throughput} = \frac{u_0}{\nu_0} = 1 - \epsilon
> $$
>
> We will prove this intuitive result in a later section.
>
> **Takeaway:** For a retransmission protocol with $L+1$ trials and per-trial error probability $\epsilon$: success probability $= 1-\epsilon^{L+1}$, mean attempts $= (1-\epsilon^{L+1})/(1-\epsilon)$, throughput $= 1-\epsilon$. The throughput is independent of $L$; increasing $L$ only reduces discard probability, not effective bandwidth.

### 2.8.4 First Passage Times

> [!Important] Definition — First Passage Time
> **Statement:** The **first passage time** $\theta_{ij}$ from state $i$ to $j$ is the number of transitions needed to reach $j$ from $i$ for the first time. Its distribution is given by:
> $$
> \mathbb{P}[\theta_{ij} = n] = f_{ij}(n) = \mathbb{P}[X_n=j,\, X_m \neq j,\, m=1,\ldots,n-1 \mid X_0=i]
> $$
>
> We define $f_{ij}(0) \equiv 0\ \forall i \neq j$, as the probability of reaching $j$ from a different state without moving is null.
>
> We can compute $f_{ij}$ by first-step analysis:
> $$
> f_{ij}(n) = P_{ij}\,\delta(n-1) + \sum_{k\neq j} P_{ik}\, f_{kj}(n-1) \qquad \delta(n) = \begin{cases}1 & n=0\\ 0 & n\neq 0\end{cases} \tag{2.24}
> $$
>
> In fact, $f_{ij}$ equals $P_{ij}$ if $n=1$ (direct transition in one step). Otherwise, the system goes to a different state $k \neq j$ (with probability $P_{ik}$), where the first passage time to $j$ becomes $f_{kj}(n-1)$.
>
> By reiterating (2.24) we can express $f_{ij}(n)$, for any $n$, as a function of $\mathbf{P}$ only.
>
> **Relation to multi-step probabilities:**
> $$
> P_{ij}^{(n)} = \sum_{m=1}^{n} f_{ij}(m)\, P_{jj}^{(n-m)} \qquad n \geq 1 \tag{2.26}
> $$
>
> This holds because we can consider all paths reaching $j$ for the first time in $m \leq n$ steps, then transitioning from $j$ to $j$ in the remaining $n-m$ steps. Highlighting the last term:
> $$
> f_{ij}(n) = \begin{cases} 0 & n=0 \\ P_{ij} & n=1 \\ P_{ij}^{(n)} - \sum_{m=1}^{n-1} f_{ij}(m)\, P_{jj}^{(n-m)} & n \geq 2 \end{cases}
> $$
> which can be solved by recursion.
>
> **Example — two-state chain:**
> $$
> f_{01}(n) = P_{01}\,\delta(n-1) + P_{00}\,f_{01}(n-1) = \begin{cases} a & n=1 \\ (1-a)\,f_{01}(n-1) & n>1 \end{cases}
> $$
> $$
> \Rightarrow f_{01}(n) = (1-a)^{n-1}a \qquad n \geq 1
> $$
>
> Similarly:
> $$
> f_{11}(n) = P_{11}\,\delta(n-1) + P_{10}\,f_{01}(n-1) = \begin{cases} 1-b & n=1 \\ ab(1-a)^{n-2} & n>1 \end{cases}
> $$
>
> And by substituting $a \leftrightarrow b$ (by symmetry) we obtain $f_{10}$ and $f_{00}$.
>
> **Intuition:** $f_{ij}(n)$ is a geometric-like distribution when the chain has few states. In general, first-step analysis turns the first-passage distribution into a recursive formula involving only one-step transition probabilities.

> [!Important] Theorem — Mean First Passage Time (First-Step Analysis)
> **Statement:** The mean first passage time $\mathbb{E}[\theta_{ij}]$ satisfies:
> $$
> \mathbb{E}[\theta_{ij}] = 1 + \sum_{k \neq j}^{N} P_{ik}\,\mathbb{E}[\theta_{kj}] \qquad \forall\, i, j \tag{2.28}
> $$
>
> **Proof:**
> Note that:
> $$
> \theta_{ij} = \begin{cases} 1 & \text{with probability } P_{ij} \\ 1 + \theta_{kj} & \text{with probability } P_{ik},\, k \neq j \end{cases} \tag{2.27}
> $$
>
> If we reach $j$ in one step (probability $P_{ij}$), then $\theta_{ij} = 1$. Otherwise, with probability $P_{ik}$ we travel to another state $k \neq j$, meaning that $\theta_{ij} = 1$ (the step just taken) plus the remaining $\theta_{kj}$ steps.
>
> Averaging both sides of (2.27):
> $$
> \mathbb{E}[\theta_{ij}] = P_{ij} + \sum_{k \neq j}^{N} P_{ik}(1 + \mathbb{E}[\theta_{kj}]) = \underbrace{\sum_{k=0}^{N} P_{ik}}_{1} + \sum_{k \neq j}^{N} P_{ik}\,\mathbb{E}[\theta_{kj}] \underset{(a)}{=} 1 + \sum_{k \neq j}^{N} P_{ik}\,\mathbb{E}[\theta_{kj}]
> $$
>
> where in (a) we used the fact that all rows of $\mathbf{P}$ sum to 1 due to normalization. $\square$
>
> For a fixed $j$ and $i \neq j$, we have $N$ equations:
> $$
> \mathbb{E}[\theta_{ij}] = 1 + \sum_{k \neq j} P_{ik}\,\mathbb{E}[\theta_{kj}] \qquad i \neq j
> $$
> After solving for all $\mathbb{E}[\theta_{ij}]$ with $i \neq j$, we compute:
> $$
> \mathbb{E}[\theta_{jj}] = 1 + \sum_{k \neq j} P_{jk}\,\mathbb{E}[\theta_{kj}]
> $$
>
> **Example — two-state model:**
> $$
> \mathbb{E}[\theta_{01}] = 1 + P_{00}\,\mathbb{E}[\theta_{01}] \Rightarrow \mathbb{E}[\theta_{01}] = \frac{1}{a}
> $$
> $$
> \mathbb{E}[\theta_{10}] = 1 + P_{11}\,\mathbb{E}[\theta_{10}] \Rightarrow \mathbb{E}[\theta_{10}] = \frac{1}{b}
> $$
>
> And the return times:
> $$
> \mathbb{E}[\theta_{00}] = 1 + P_{01}\,\mathbb{E}[\theta_{10}] = 1 + \frac{a}{b} = \frac{a+b}{b} = \left(\frac{b}{a+b}\right)^{-1}
> $$
> $$
> \mathbb{E}[\theta_{11}] = 1 + P_{10}\,\mathbb{E}[\theta_{01}] = 1 + \frac{b}{a} = \frac{a+b}{a} = \left(\frac{a}{a+b}\right)^{-1}
> $$
>
> Note that $\mathbb{E}[\theta_{00}]$ and $\mathbb{E}[\theta_{11}]$ are the **reciprocals of the long-run probabilities** of remaining respectively in state 0 or 1. Intuitively, if the system returns from state 0 to state 0 after, on average, $(a+b)/b$ time units, then the fraction of time spent on state 0 is the inverse of that quantity — because the system visits 0 "once every $\mathbb{E}[\theta_{00}]$" steps. This is a property of many Markov chains, as we will see in a later section.
>
> **Second moments:**
> $$
> \mathbb{E}[\theta_{ij}^2] = P_{ij} \cdot 1^2 + \sum_{k \neq j}^{N} P_{ik}\,\mathbb{E}[(1+\theta_{kj})^2]
> $$
> Expanding the square:
> $$
> = \underbrace{P_{ij} + \sum_{k \neq j}^{N} P_{ik}}_{1} + 2\sum_{k \neq j}^{N} P_{ik}\,\mathbb{E}[\theta_{kj}] + \sum_{k \neq j}^{N} P_{ik}\,\mathbb{E}[\theta_{kj}^2]
> \underset{(2.28)}{=} 2\mathbb{E}[\theta_{ij}] - 1 + \sum_{k \neq j} P_{ik}\,\mathbb{E}[\theta_{kj}^2]
> $$
>
> In the two-state case:
> $$
> \mathbb{E}[\theta_{01}^2] = 2\mathbb{E}[\theta_{01}] - 1 + P_{00}\,\mathbb{E}[\theta_{01}^2] \Rightarrow \mathbb{E}[\theta_{01}^2] = \frac{2/a - 1}{a} = \frac{2}{a^2} - \frac{1}{a}
> $$
> $$
> \mathrm{Var}(\theta_{01}) = \frac{1-a}{a^2}
> $$
> *(which matches the geometric distribution result.)*
>
> Similarly:
> $$
> \mathbb{E}[\theta_{10}^2] = 2\mathbb{E}[\theta_{10}] - 1 + P_{11}\,\mathbb{E}[\theta_{10}^2] \Rightarrow \mathrm{Var}(\theta_{10}) = \frac{1-b}{b^2}
> $$
>
> For the $i=j$ case, for example:
> $$
> \mathbb{E}[\theta_{00}^2] = 2\mathbb{E}[\theta_{00}] - 1 + P_{01}\,\mathbb{E}[\theta_{10}^2] = 2\left(1+\frac{a}{b}\right) - 1 + a\left(\frac{2}{b^2}-\frac{1}{b}\right) = 1 + \frac{a}{b} + \frac{2a}{b^2}
> $$
> $$
> \mathrm{Var}(\theta_{00}) = \mathbb{E}[\theta_{00}^2] - \mathbb{E}[\theta_{00}]^2 = 1+\frac{a}{b}+\frac{2a}{b^2} - \left(1+\frac{2a}{b}+\frac{a^2}{b^2}\right) = \frac{2a-a^2}{b^2} - \frac{a}{b} = \frac{a(2-a-b)}{b^2}
> $$
>
> **Intuition:** $\mathbb{E}[\theta_{jj}]$ (mean return time to $j$) equals the reciprocal of the stationary probability $\pi_j$. This is a fundamental relationship that connects first passage times to the long-run behaviour of the chain.

---

## 2.9 Alternative First Step Analysis

All the results obtained from first-step analysis (average first passage times, mean absorption time, absorption probabilities) can be re-derived using the $n$-step probability matrix, at the cost of a lengthier computation. The idea is to compute the value of each quantity for an $n$-long evolution, and then study the asymptotic behaviour for $n \to \infty$.

Consider a Markov chain with $N+1$ states labelled $0, 1, \ldots, N$. Suppose that the first $r$ ones (i.e. $0, 1, \ldots, r-1$) are **transient** — meaning that, given sufficient time, $P_{ij}^{(n)} \xrightarrow[n\to\infty]{} 0$ for $0 \leq i, j < r$ — while the remaining states $(r, \ldots, N)$ are **absorbing** ($P_{ii} = 1$ for $r \leq i \leq N$).

The resulting transition matrix is decomposed in 4 blocks:

$$
\mathbf{P} = \begin{pmatrix} \mathbf{Q} & \mathbf{R} \\ \mathbf{O} & \mathbb{1} \end{pmatrix}
$$

Explicitly computing the $n$-th power of $\mathbf{P}$:

$$
\mathbf{P}^2 = \begin{pmatrix} \mathbf{Q}^2 & \mathbf{R} + \mathbf{Q}\mathbf{R} \\ \mathbf{O} & \mathbb{1} \end{pmatrix}
$$

$$
\mathbf{P}^3 = \begin{pmatrix} \mathbf{Q} & \mathbf{R} \\ \mathbf{O} & \mathbb{1} \end{pmatrix} \times \begin{pmatrix} \mathbf{Q}^2 & \mathbf{R} + \mathbf{Q}\mathbf{R} \\ \mathbf{O} & \mathbb{1} \end{pmatrix} = \begin{pmatrix} \mathbf{Q}^3 & \mathbf{R} + \mathbf{Q}\mathbf{R} + \mathbf{Q}^2\mathbf{R} \\ \mathbf{O} & \mathbb{1} \end{pmatrix}
$$

Generalizing:

$$
\mathbf{P}^n = \begin{pmatrix} \mathbf{Q}^n & (\mathbb{1} + \mathbf{Q} + \cdots + \mathbf{Q}^{n-1})\mathbf{R} \\ \mathbf{O} & \mathbb{1} \end{pmatrix} \tag{2.29}
$$

Suppose the system starts in state $i$ and makes a total of $n$ transitions. Given this time window, the **mean number of visits** to a certain state $j$ is:

$$
W_{ij}^{(n)} = \mathbb{E}\left[\sum_{l=0}^{n} \mathbf{1}\{X_l=j\} \,\Big|\, X_0=i\right] \qquad \mathbf{1}\{X_l=j\} = \begin{cases}1 & X_l=j\\0 & X_l\neq j\end{cases}
$$

Bringing the expectation inside the sum by linearity, and noting that $\mathbb{E}[\mathbf{1}\{X_l=j\}|X_0=i] = P_{ij}^{(l)}$:

$$
W_{ij}^{(n)} = \sum_{l=0}^{n} P_{ij}^{(l)} \tag{2.30}
$$

The only interesting case is when $i$ and $j$ are both transient ($0 \leq i,j < r$), so $P_{ij}^{(l)} = Q_{ij}^{(l)}$:

$$
W_{ij}^{(n)} = Q_{ij}^{(0)} + Q_{ij}^{(1)} + \cdots + Q_{ij}^{(n)} \qquad 0 \leq i,j < r
$$

In matrix notation:

$$
\mathbf{W}^{(n)} = \mathbb{1} + \mathbf{Q} + \mathbf{Q}^2 + \cdots + \mathbf{Q}^n = \mathbb{1} + \mathbf{Q}\mathbf{W}^{(n-1)} \tag{2.31, 2.32}
$$

> [!Important] Theorem — Fundamental Matrix W
> **Statement:** In the limit $n \to \infty$, the mean number of visits matrix converges to the **fundamental matrix**:
> $$
> \mathbf{W} \equiv \lim_{n\to\infty} \mathbf{W}^{(n)} = (\mathbb{1} - \mathbf{Q})^{-1}
> $$
> with $W_{ij} = \mathbb{E}[\text{Total visits to } j \mid X_0=i]$ for $0 \leq i,j < r$.
>
> **Proof:**
> Since $\lim_{n\to\infty} \mathbf{W}^{(n)} = \lim_{n\to\infty} \mathbf{W}^{(n-1)} \equiv \mathbf{W}$, equation (2.32) gives:
> $$
> \mathbf{W} = \mathbb{1} + \mathbf{Q}\mathbf{W} \tag{2.33}
> $$
>
> Rearranging:
> $$
> \mathbf{W} - \mathbf{Q}\mathbf{W} = (\mathbb{1} - \mathbf{Q})\mathbf{W} = \mathbb{1} \Rightarrow \mathbf{W} = (\mathbb{1} - \mathbf{Q})^{-1} \quad \square
> $$
>
> In terms of matrix entries, (2.33) is the same result as (2.15) obtained via first-step analysis:
> $$
> W_{ij} = \delta_{ij} + \sum_{l=0}^{r-1} P_{il}\, W_{lj} \qquad \forall\, i,j = 0,\ldots,r-1 \tag{2.34}
> $$
>
> Moreover, the connection to absorption time: let $T$ be the number of steps for a specific evolution to go from initial state $i$ to any absorbing state $r,\ldots,N$ for the first time:
> $$
> T = \min\{n \geq 0;\, r \leq X_n \leq N\}
> $$
>
> Then:
> $$
> W_{ij} = \mathbb{E}\left[\sum_{n=0}^{T-1} \mathbf{1}\{X_n=j\} \,\Big|\, X_0=i\right] \quad 0 \leq i,j < r \tag{2.35}
> $$
>
> In fact, for every $n \geq T$, we have $r \leq X_n \leq N$, and so $X_n \neq j$, meaning that $\mathbf{1}\{X_n=j\} = 0$.
>
> ![[Stochastic_Processes_2020_p63_img17.jpeg]]
> *(Figure — before absorption, the system evolves only through transient states; the indicator sums truncate at $T$.)*
>
> **Intuition:** $(\mathbb{1}-\mathbf{Q})^{-1}$ is the analog of the geometric series sum $(1-q)^{-1} = 1+q+q^2+\cdots$ for matrices. The $(i,j)$ entry counts the expected total number of visits to transient state $j$ starting from $i$ before absorption.

> [!Important] Theorem — Mean Absorption Time via W
> **Statement:** The mean time to absorption starting from transient state $i$ is:
> $$
> \boldsymbol{\nu} = \mathbf{W} \times \mathbf{1} = (\mathbb{1} - \mathbf{Q})^{-1} \times \mathbf{1} \tag{2.39}
> $$
> where $\boldsymbol{\nu} = (\nu_0, \ldots, \nu_{r-1})^T$ and $\mathbf{1} = (1,\ldots,1)^T \in \mathbb{R}^{r-1}$.
>
> **Proof:**
> Summing (2.35) over all transient states $j$ and applying linearity:
> $$
> \sum_{j=0}^{r-1} W_{ij} = \mathbb{E}\left[\sum_{j=0}^{r-1}\sum_{n=0}^{T-1} \mathbf{1}\{X_n=j\} \,\Big|\, X_0=i\right] \underset{(2.36)}{=} \mathbb{E}[T \mid X_0=i] \equiv \nu_i \tag{2.37}
> $$
>
> All that's left is to substitute the expression for $W_{ij}$ from (2.34) in (2.37):
> $$
> \nu_i = \sum_{j=0}^{r-1} W_{ij} \underset{(2.34)}{=} \underbrace{\sum_{j=0}^{r-1}\delta_{ij}}_{1} + \sum_{j=0}^{r-1}\sum_{k=0}^{r-1} P_{ik}\, W_{kj} = 1 + \sum_{k=0}^{r-1} P_{ik}\, \nu_k \tag{2.38}
> $$
>
> which is again the same result that can be obtained by first-step analysis.
>
> Note that matrix multiplication with a column vector of ones results in a column vector with entries equal to the sum of all entries in each row of the original matrix. $\square$
>
> **Intuition:** The row sum of $\mathbf{W}$ counts the total expected visits to *all* transient states — which is exactly the expected time before absorption.

> [!Important] Theorem — Absorption Probabilities via W
> **Statement:** The probability of being absorbed in state $k \in \{r,\ldots,N\}$ starting from transient state $i$ is:
> $$
> \mathbf{U} = \mathbf{W}\mathbf{R} \Leftrightarrow U_{ik} = \sum_{j=0}^{r-1} W_{ij}\, R_{jk} \quad 0 \leq i < r;\, r \leq k \leq N
> $$
>
> **Proof:**
> We focus on the probability $U^{(n)}_{ik}$ of the system being absorbed in state $k$ during the first $n$ steps given it started at $i$. As state $k$, once entered, cannot be left, if the system reaches it before the $n$-th step then $X_n = k$, and so:
> $$
> U^{(n)}_{ik} = P^{(n)}_{ik} = \mathbb{P}\{X_n=k \mid X_0=i\}
> $$
>
> As $i$ is transient and $k$ is absorbing, we know the form of $P^{(n)}_{ik}$ from (2.29), and so in matrix form:
> $$
> \mathbf{U}^{(n)} = (\mathbb{1} + \mathbf{Q} + \cdots + \mathbf{Q}^{n-1})\mathbf{R} \underset{(2.31)}{\equiv} \mathbf{W}^{(n-1)}\mathbf{R} \tag{2.40}
> $$
>
> Taking the limit $n \to \infty$:
> $$
> U_{ik} \equiv \lim_{n\to\infty} U^{(n)}_{ik} = \mathbb{P}\{X_T=k \mid X_0=i\}
> $$
>
> And from the limit of (2.40): $\mathbf{U} = \mathbf{W}\mathbf{R}$. $\square$

### 2.9.1 Matrix Approach for Average First Passage Time

We can elaborate a matrix approach for computing the average first passage times from any state $i \neq N$ to state $N$. The idea is to consider the $N$-th state as absorbing — discarding all chain evolution after reaching $N$ for the first time.

Explicitly, we start from a transition matrix $\mathbf{P}$ in the form:

$$
\mathbf{P} = \begin{array}{c|cc} & 0\cdots N-1 & N \\ \hline 0\cdots N-1 & \mathbf{Q} & \mathbf{r} \\ N & \ast & \ast \end{array} \tag{2.41}
$$

and replace the last row with:

$$
\hat{\mathbf{P}} = \begin{array}{c|cc} & 0\cdots N-1 & N \\ \hline & \mathbf{Q} & \mathbf{r} \\ & \mathbf{0} & 1 \end{array} \tag{2.42}
$$

In the expressions above, $\mathbf{Q}$ is a $N \times N$ matrix, $\mathbf{r}$ is a $N \times 1$ vector, and $\mathbf{0}$ is $1 \times N$.

Note that (2.41) and (2.42) describe exactly the same system until state $N$ is visited, and so are completely equivalent in the regime we are interested in. The average first arrival time $\mathbb{E}[\theta_{iN}]$ from any state $i$ to $N$ in (2.41) is exactly the mean absorption time $\nu_i$ from state $i$ in (2.42):

$$
\mathbb{E}[\theta_{iN}] = \nu_i
$$

which can be computed using (2.39):

$$
\boldsymbol{\nu} \equiv \begin{pmatrix}\nu_0 \\ \vdots \\ \nu_{N-1}\end{pmatrix} = (\mathbb{1} - \mathbf{Q})^{-1} \times \mathbf{1}
$$

Finally, note that there is nothing special about the choice of state $N$ — we can always relabel states so that the one we are interested in is the $N$-th.

---

## Summary Table

| Concept | Definition / Formula | Conditions / Notes |
|---------|---------------------|--------------------|
| **Markov property** | $\mathbb{P}\{X_{n+1}=j \mid X_0,\ldots,X_n\} = \mathbb{P}\{X_{n+1}=j \mid X_n\}$ | Discrete time, discrete state |
| **Homogeneous chain** | $P_{ij}^{n,n+1} = P_{ij}$ independent of $n$ | Most cases of interest |
| **Joint probability** | $p_{i_0}P_{i_0 i_1}\cdots P_{i_{n-1}i_n}$ | Fully specified by $\mathbf{P}$ and $p_0$ |
| **$n$-step TPM** | $\mathbf{P}^{(n)} = \mathbf{P}^n$ (matrix power) | Chapman-Kolmogorov recursion |
| **Poisson process** | $\mathbb{P}[X_{t+s}-X_s=n]=\frac{e^{-\lambda t}(\lambda t)^n}{n!}$ | Stationary, independent increments |
| **Inter-arrival times** | $S_i \sim \mathrm{Exp}(\lambda)$ i.i.d. | Memoryless property of Poisson |
| **M/G/1 queue** | $X_n$ sampled at departures; $a_j = \int e^{-\lambda x}\frac{(\lambda x)^j}{j!}\mathrm{d}G(x)$ | Service time $\sim G$, arrivals Poisson |
| **G/M/1 queue** | $X_n$ sampled at arrivals; $P_{i,i+1-j} = \int\frac{e^{-\mu t}(\mu t)^j}{j!}\mathrm{d}G(t)$ | Service time $\sim \mathrm{Exp}(\mu)$, arrivals $\sim G$ |
| **Absorbing state** | $P_{ii} = 1$ | System cannot leave once entered |
| **Transient state** | $P_{ij}^{(n)} \to 0$ as $n \to \infty$ | System visits only finitely often |
| **First-step analysis** | $u_i = \sum_j P_{ij} u_j + P_{ik}\cdot 1$ | Linear system; $N+1$ states $\to$ $r$ eqs |
| **Absorption probability** | $U_{ik} = P_{ik} + \sum_{j<r} P_{ij} U_{jk}$ | State $k$ absorbing, $i$ transient |
| **Mean absorption time** | $\nu_i = 1 + \sum_{j<r} P_{ij}\nu_j$ | First-step analysis |
| **Two-state $\mathbf{P}^n$** | $(a+b)^{-1}[\mathbf{A}+(1-a-b)^n\mathbf{B}]$ | Limit: rows $\to (b/(a+b),\, a/(a+b))$ |
| **Gambler's ruin $u_k$** | $(N-k)/N$ for $p=q$; $\;\frac{(q/p)^k-(q/p)^N}{1-(q/p)^N}$ for $p\neq q$ | Absorbing at 0 and $N$ |
| **L2 protocol throughput** | $1 - \epsilon$ | $L+1$ retries, per-trial error $\epsilon$ |
| **First passage time** | $f_{ij}(n) = P_{ij}\delta(n{-}1) + \sum_{k\neq j}P_{ik}f_{kj}(n-1)$ | First-step recursion |
| **Mean FPT** | $\mathbb{E}[\theta_{ij}] = 1 + \sum_{k\neq j}P_{ik}\mathbb{E}[\theta_{kj}]$ | $\mathbb{E}[\theta_{jj}] = 1/\pi_j$ at stationarity |
| **Fundamental matrix** | $\mathbf{W} = (\mathbb{1}-\mathbf{Q})^{-1}$ | $W_{ij}$ = expected visits to $j$ from $i$ |
| **Mean absorption (matrix)** | $\boldsymbol{\nu} = (\mathbb{1}-\mathbf{Q})^{-1}\mathbf{1}$ | Row sums of $\mathbf{W}$ |
| **Hitting probabilities** | $\mathbf{U} = \mathbf{W}\mathbf{R}$ | $U_{ik}$ = prob. absorbed at $k$ from $i$ |
