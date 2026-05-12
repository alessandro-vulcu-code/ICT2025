# Chapter 4 — Poisson Processes

Poisson processes play a distinct role in modeling many natural phenomena, at least in a first approximation. Moreover, they are mathematically simple, allowing us to derive important analytical results and gain relevant fundamental understanding.

---

## Table of Contents

- [[#4.1 The Poisson Distribution|4.1 The Poisson Distribution]]
  - [[#Theorem 4.1.1 — Sum of Independent Poisson Variables|Theorem 4.1.1 — Sum of Independent Poisson Variables]]
  - [[#Theorem 4.1.2 — Binomial Filter of a Poisson Variable|Theorem 4.1.2 — Binomial Filter of a Poisson Variable]]
- [[#4.2 The Poisson Process|4.2 The Poisson Process]]
  - [[#Non-Homogeneous Processes|Non-Homogeneous Processes]]
- [[#4.3 The Law of Rare Events|4.3 The Law of Rare Events]]
  - [[#Theorem 4.3.1 — Poisson Approximation Bound|Theorem 4.3.1 — Poisson Approximation Bound]]
- [[#4.4 Properties of Poisson Processes|4.4 Properties of Poisson Processes]]
  - [[#Theorem 4.4.1 — Superposition|Theorem 4.4.1 — Superposition]]
  - [[#Theorem 4.4.2 — Splitting (Thinning)|Theorem 4.4.2 — Splitting (Thinning)]]
- [[#4.5 Other Distributions|4.5 Other Distributions]]
  - [[#Theorem 4.5.1 — Inter-Arrival Times are Exponential|Theorem 4.5.1 — Inter-Arrival Times are Exponential]]
  - [[#Theorem 4.5.2 — Waiting Times are Gamma|Theorem 4.5.2 — Waiting Times are Gamma]]
  - [[#Theorem 4.5.3 — Conditional Arrival Times are Uniform|Theorem 4.5.3 — Conditional Arrival Times are Uniform]]
  - [[#Theorem 4.5.4 — Binomial Conditional Distribution|Theorem 4.5.4 — Binomial Conditional Distribution]]
  - [[#Theorem 4.5.5 — Two Processes, Conditional Distribution|Theorem 4.5.5 — Two Processes, Conditional Distribution]]
  - [[#Corollary 4.5.1 — Combined Conditional Distribution|Corollary 4.5.1 — Combined Conditional Distribution]]
  - [[#4.5.1 M/G/∞ Queue|4.5.1 M/G/∞ Queue]]
  - [[#4.5.2 Shot Noise Process|4.5.2 Shot Noise Process]]
- [[#4.6 Binomial Theorem|4.6 Binomial Theorem]]
  - [[#Theorem 4.6.1 — Binomial Theorem (Direct Proof)|Theorem 4.6.1 — Binomial Theorem (Direct Proof)]]
  - [[#Dual Version|Dual Version]]
  - [[#Exercise 4.6.1 — Two Independent Processes|Exercise 4.6.1 — Two Independent Processes]]
  - [[#Exercise 4.6.2 — Finite Delay-Line Chain|Exercise 4.6.2 — Finite Delay-Line Chain]]
  - [[#Exercise 4.6.3 — Infinite Delay-Line Chain|Exercise 4.6.3 — Infinite Delay-Line Chain]]
  - [[#Exercise 4.6.4 — Fraction of Transitions|Exercise 4.6.4 — Fraction of Transitions]]
  - [[#Exercise 4.6.5 — Limits for a Regular Chain|Exercise 4.6.5 — Limits for a Regular Chain]]
  - [[#Exercise 4.6.6 — Backward Probability|Exercise 4.6.6 — Backward Probability]]
  - [[#Exercise 4.6.7 — Man with Car(s)|Exercise 4.6.7 — Man with Car(s)]]
- [[#4.7 P.A.S.T.A. Property|4.7 P.A.S.T.A. Property]]
  - [[#Non-Poisson Arrivals Counter-Example|Non-Poisson Arrivals Counter-Example]]
  - [[#Arrival–Service Times Not Independent Counter-Example|Arrival–Service Times Not Independent Counter-Example]]
  - [[#M/G/1 Queue — Arrivals Equal Departures|M/G/1 Queue — Arrivals Equal Departures]]
  - [[#Periodic Class Discussion|Periodic Class Discussion]]
  - [[#Exercise 4.7.2 — Shock Survival|Exercise 4.7.2 — Shock Survival]]
  - [[#Exercise 4.7.3 — Dispatching System|Exercise 4.7.3 — Dispatching System]]
  - [[#Exercise 4.7.4 — Typographical Errors|Exercise 4.7.4 — Typographical Errors]]
  - [[#Exercise 4.7.5 — Circular Disk|Exercise 4.7.5 — Circular Disk]]
  - [[#Exercise 4.7.6 — First Time All Processes Fire|Exercise 4.7.6 — First Time All Processes Fire]]
  - [[#Exercise 4.7.7 — Batch Holding Facility|Exercise 4.7.7 — Batch Holding Facility]]
  - [[#Exercise 4.7.8 — Mean of First Arrival Time|Exercise 4.7.8 — Mean of First Arrival Time]]
  - [[#Exercise 4.7.9 — Mean Total Waiting Time|Exercise 4.7.9 — Mean Total Waiting Time]]
  - [[#Exercise 4.7.10 — Store Empty at End of Hour|Exercise 4.7.10 — Store Empty at End of Hour]]
- [[#Summary Table|Summary Table]]

---

## 4.1 The Poisson Distribution

The **Poisson distribution** with parameter $\mu > 0$ is given by:

$$
p_k \equiv \mathbb{P}[X = k] = \frac{e^{-\mu}\mu^k}{k!} \quad \text{for } k = 0, 1, 2, \dots \tag{4.1}
$$

Recall (equation (1.15)) that its mean and variance are:

$$
\mathbb{E}[X] = \mu \qquad \operatorname{Var}[X] = \mu
$$

### Theorem 4.1.1 — Sum of Independent Poisson Variables

> [!Important] Theorem 4.1.1 — Sum of Independent Poisson Variables
> **Statement:** Let $X$ and $Y$ be independent random variables having Poisson distributions with parameters $\mu$ and $\nu$, respectively. Then the sum $X + Y$ has a Poisson distribution with parameter $\mu + \nu$.
>
> **Proof:**
> We proceed by direct computation of the distribution of $X + Y$, searching for an expression for $\mathbb{P}[X + Y = n]$. Each event $\{X + Y = n\}$ is made up of the sequence of mutually exclusive events where $X = k$ for some $k = 0, \ldots, n$ and consequently $Y = n - k$. By the law of total probability:
>
> $$\mathbb{P}[X + Y = n] = \sum_{k=0}^{n} \mathbb{P}[X = k, Y = n - k]$$
>
> Since $X$ and $Y$ are independent, the joint probabilities factorize:
>
> $$= \sum_{k=0}^{n} \mathbb{P}[X = k]\mathbb{P}[Y = n-k] = \sum_{k=0}^{n} \frac{\mu^k e^{-\mu}}{k!} \frac{\nu^{n-k} e^{-\nu}}{(n-k)!}$$
>
> We pull out the factor $e^{-\mu-\nu}$ that does not depend on $k$, and multiply and divide by $n!$ to highlight a *binomial sum*:
>
> $$= \frac{e^{-(\mu+\nu)}}{n!} \underbrace{\sum_{k=0}^{n} \frac{n!}{k!(n-k)!} \mu^k \nu^{n-k}}_{(\mu+\nu)^n}$$
>
> Therefore:
>
> $$\mathbb{P}[X + Y = n] = \frac{e^{-(\mu+\nu)}(\mu+\nu)^n}{n!} \qquad n = 0, 1, \ldots \tag{4.2}$$
>
> which is exactly the Poisson distribution (4.1) with parameter $\mu + \nu$. $\blacksquare$
>
> **Intuition:** The Poisson distribution is closed under convolution. Counting events from two independent Poisson sources is equivalent to a single Poisson source whose rate is the sum of the individual rates. This extends to any finite number of independent Poisson variables.

### Theorem 4.1.2 — Binomial Filter of a Poisson Variable

> [!Important] Theorem 4.1.2 — Binomial Filter of a Poisson Variable
> **Statement:** Let $N$ be a Poisson random variable with parameter $\mu$, and conditional on $N$, let $M$ have a binomial distribution with parameters $N$ and $p$. Then the unconditional distribution of $M$ is Poisson with parameter $\mu p$.
>
> In other words, if we pick $N$ objects, with $N$ following a Poisson distribution, and then *keep* each one with probability $p$, the number $M$ of remaining objects follows a Poisson distribution with parameter $\mu p \leq \mu$. The second *binomial process* acts as a "filter", reducing the *effective rate* without modifying the form of the distribution.
>
> **Proof:** See Exercise 1.6.1. $\blacksquare$
>
> **Intuition:** Thinning a Poisson random variable by independent Bernoulli sampling preserves the Poisson form. The rate simply scales by $p$.

---

## 4.2 The Poisson Process

A Poisson process describes, intuitively, how the *count* $X$ of *rare* events changes over time $t$. More formally:

> [!Important] Definition 1 — Poisson Process
> **Statement:** A *Poisson process* of **intensity**, or **rate**, $\lambda > 0$ is an integer-valued stochastic process $\{X(t) : t \geq 0\}$ for which:
>
> 1. For any sequence of instants $t_0 = 0 < t_1 < t_2 < \cdots < t_n$, the process *increments*
>    $$X(t_1) - X(t_0),\; X(t_2) - X(t_1),\; \ldots,\; X(t_n) - X(t_{n-1})$$
>    are **independent** and **stationary** random variables.
>    Stationarity means $X(t_{i+1}) - X(t_i)$ depends *only* on the size $t_{i+1} - t_i$ of the time interval: given more time more events will be observed, but the *rate* is always fixed and does not depend on the absolute value of $t$. This describes the process in its *stationary* state, when its behavior does not change anymore.
>
> 2. For $s \geq 0$ and $t > 0$, the random variable $X(s+t) - X(s)$ has a Poisson distribution with rate $\lambda t$:
>    $$\mathbb{P}[X(s+t) - X(s) = k] = \frac{(\lambda t)^k e^{-\lambda t}}{k!} \qquad \text{for } k = 0, 1, 2, \ldots$$
>    In accordance with the previous requirement, this distribution depends *only* on the duration $t$ of the inspected interval, since $\lambda$ is constant.
>
> 3. $X(0) = 0$. No event can occur right at the start, when the counter is "reset".
>
> It follows that:
> $$\mathbb{E}[X(t)] = \lambda t \qquad \operatorname{Var}[X(t)] = \lambda t$$
>
> **Intuition:** The Poisson process is the canonical model for memoryless, rate-$\lambda$ arrivals. Increments over disjoint intervals are independent; the distribution of events in any interval depends only on its length.

> [!Example] Example — Undersea Cable Defects
> **Problem:** Defects occur along an undersea cable according to a Poisson process of rate $\lambda = 0.1$ per mile.
>
> (a) What is the probability that no defects appear in the first two miles?
>
> (b) Given no defects in the first two miles, what is the conditional probability of no defects between mile two and three?
>
> **Solution:**
>
> (a) $X(2)$ has a Poisson distribution with parameter $\lambda t = 0.1 \cdot 2 = 0.2$:
> $$\mathbb{P}[X(2) = 0] = e^{-0.2} = 0.8187$$
>
> (b) By independence of $X(3) - X(2)$ and $X(2) - X(0) = X(2)$, the conditional probability equals the unconditional probability:
> $$\mathbb{P}[X(3) - X(2) = 0] = \mathbb{P}[X(1) = 0] = e^{-0.1} = 0.9048$$
>
> **Takeaway:** Independence of increments over disjoint intervals is the key property — conditioning on the past does not affect future increments.

> [!Example] Example — Store Arrivals
> **Problem:** Customers arrive at a store according to a Poisson process of rate $\lambda = 4$ per hour. The store opens at 9:00 AM. What is the probability that exactly one customer has arrived by 9:30 and a total of five have arrived by 11:30 AM?
>
> **Solution:**
> Set the time unit as one hour, starting from 9:00 AM. We need $\mathbb{P}[X(1/2) = 1,\, X(5/2) = 5]$.
>
> Using independence of $X(5/2) - X(1/2)$ and $X(1/2)$, we reformulate as:
>
> $$\mathbb{P}[X(1/2) = 1,\, X(5/2) = 5] = \mathbb{P}[X(1/2) = 1,\, X(5/2) - X(1/2) = 4]$$
>
> $$= \left(\frac{e^{-4(1/2)}\left[4\cdot\frac{1}{2}\right]^1}{1!}\right)\left(\frac{e^{-4(2)}[4 \cdot 2]^4}{4!}\right) = (2e^{-2})\left(\frac{512}{3}e^{-8}\right) = 0.0155$$
>
> **Takeaway:** Decompose joint events involving a Poisson process by exploiting independent increments over disjoint intervals.

### Non-Homogeneous Processes

A possible generalization is to *relax* the stationarity hypothesis, letting the rate $\lambda$ be a function of time: $\lambda(t)$.

This means the average rate per unit time is no longer constant. The probability of a single event in an infinitesimal interval $h$ is proportional to $\lambda$:

$$\mathbb{P}[X(t+h) - X(t) = 1] = \frac{(\lambda h)e^{-\lambda h}}{1!} = (\lambda h)(1 - \lambda h + O(h^2)) = \lambda h + o(h)$$

The probability of $k$ events in $(s, s+t]$ is then given by:

$$\mathbb{P}[X(t+s) - X(s) = k] = \frac{1}{k} \int_s^{t+s} (\lambda(t)t)^k e^{-\lambda(t)t} \tag*{(note: possible OCR artifact in formula)}$$

---

## 4.3 The Law of Rare Events

The incredible range of applicability of the Poisson distribution is explained by the fact that it is the "discrete analog" of the normal distribution.

From the Central Limit Theorem we know that, under mild assumptions, the sum of many continuous random variables follows a Gaussian distribution. A similar thing happens for discrete random variables, with the final distribution being Poisson. This is the so-called *Law of Rare Events*.

In essence, suppose that a certain event can occur in many circumstances, but has a low probability in any specific one. We say this event is "rare", and the *Law of Rare Events* states that the total number of these rare events follows (approximately) a Poisson distribution.

The simplest example: an experiment with a low and fixed probability $p \ll 1$ of success, repeated $N$ times. The total number of successes $X_{N,p}$ follows a binomial distribution:

$$\mathbb{P}[X_{N,p} = k] = \frac{N!}{k!(N-k)!} p^k (1-p)^{N-k} \qquad \text{for } k = 0, \ldots, N$$

In the limit of rare events $p \to 0$ and infinite trials $N \to +\infty$, with fixed success rate $Np \equiv \mu > 0$, $X_{N,p}$ follows the Poisson distribution:

$$\mathbb{P}[X_\mu = k] = \frac{e^{-\mu}\mu^k}{k!} \qquad \text{for } k = 0, 1, 2, \ldots$$

The Law of Rare Events is much more general. Even if the success probability $p_i$ changes at each trial $i$, in the limit $N \to \infty$, $X_{N,\mathbf{p}}$ still follows a Poisson distribution with rate $\sum_{i=1}^N p_i$. More formally:

### Theorem 4.3.1 — Poisson Approximation Bound

> [!Important] Theorem 4.3.1 — Poisson Approximation Bound
> **Statement:** Let $\boldsymbol{\epsilon}_1, \boldsymbol{\epsilon}_2, \ldots$ be independent Bernoulli random variables with:
> $$\mathbb{P}[\boldsymbol{\epsilon}_i = 1] = p_i \qquad \mathbb{P}[\boldsymbol{\epsilon}_i = 0] = 1 - p_i$$
> Let $S_n = \boldsymbol{\epsilon}_1 + \cdots + \boldsymbol{\epsilon}_n$. The distribution of $S_n$:
> $$\mathbb{P}[S_n = k] = \sum_{\substack{x_i = \pm 1 \\ x_1 + \cdots + x_n = k}} \prod_{i=1}^n p_i^{x_i}(1-p_i)^{1-x_i}$$
> differs from a Poisson distribution with rate $\mu = p_1 + \cdots + p_n$ by at most:
> $$\left|\mathbb{P}[S_n = k] - \frac{\mu^k e^{-\mu}}{k!}\right| \leq \sum_{i=1}^n p_i^2 \tag{4.4}$$
>
> In particular, if all $p_i \equiv p$ and $Np = \mu$ is kept fixed, in the limit $N \to +\infty$, $p = \mu/N \to 0$, and so does the RHS of (4.4).
>
> **Intuition:** The bound $\sum_i p_i^2$ quantifies how far the sum of heterogeneous Bernoulli variables is from Poisson. The smaller the individual probabilities, the tighter the Poisson approximation. This is why the Law of Rare Events holds for diverse phenomena: as long as individual event probabilities are small, their aggregate count is well approximated by a Poisson.

An analog of the Law of Rare Events holds for stochastic processes: the total counts of events generated by many independent processes can be approximately described by a single Poisson process.

Consider a large number $M$ of processes (not necessarily Poisson) generating events at random times. If we combine all axes and consider only the total number of events $X(t)$ before time $t$ — without considering their origin — then in the limit $M \to \infty$, $X(t)$ is described by a Poisson process.

This is useful in practice: events we are interested in may be produced in different ways by different natural phenomena, each following a different law. Thanks to the Law of Rare Events, we can describe the counts with a unique Poisson process — even if none of the underlying processes is Poisson.

---

## 4.4 Properties of Poisson Processes

Poisson processes share many important properties of the Poisson distribution.

### Theorem 4.4.1 — Superposition

> [!Important] Theorem 4.4.1 — Superposition of Poisson Processes
> **Statement:** Let $X_1(t)$ and $X_2(t)$ be two independent Poisson processes with rates $\lambda_1, \lambda_2$. Then $X(t) = X_1(t) + X_2(t)$ is a Poisson process with rate $\lambda = \lambda_1 + \lambda_2$.
>
> ![[Stochastic_Processes_2020_p131_img34.jpeg]]
> *Figure 4.1 — Graphical representation of two combined Poisson processes, where their sum is a Poisson process with parameter equal to the sum of the two parameters.*
>
> **Proof:**
> We verify the three requirements of Definition 1.
>
> 1. At the starting time $t = 0$: $X_1(0) = X_2(0) = 0$, so $X(0) = 0$. ✓
>
> 2. Since $X_1$ and $X_2$ have stationary and independent increments separately, so does their sum $X$. This can be shown explicitly by writing the distribution of $X$. ✓
>
> 3. Since $X_1(t)$ and $X_2(t)$ are Poisson distributed with parameters $\lambda_1 t$ and $\lambda_2 t$ and are independent, their sum $X(t) = X_1(t) + X_2(t)$ is Poisson with parameter $(\lambda_1 + \lambda_2)t$ by Theorem 4.1.1. ✓
>
> $\square$
>
> **Intuition:** Merging two independent Poisson streams gives another Poisson stream. The combined rate is additive. This generalizes to any finite superposition.

### Theorem 4.4.2 — Splitting (Thinning)

> [!Important] Theorem 4.4.2 — Splitting (Thinning) of a Poisson Process
> **Statement:** Let $X(t)$ be a Poisson process with rate $\lambda$, and let each event be independently marked as type 1 with probability $p$, or type 2 with probability $1-p$. Then the events of type 1 and type 2 form two **independent** Poisson processes with rates $\lambda p$ and $\lambda(1-p)$, respectively.
>
> ![[Stochastic_Processes_2020_p132_img35.jpeg]]
> *Figure 4.2 — Graphical representation of splitting a Poisson process into two sub-processes as in Theorem 4.4.2.*
>
> **Proof:**
> We verify the three requirements of Definition 1.
>
> 1. When we start counting there are no events at all, so $X_1(0) = X_2(0) = 0$. ✓
>
> 2. Since $X$ has stationary and independent increments and the marking occurs independently, $X_1$ and $X_2$ inherit stationarity and independence of their respective increments. ✓
>
> 3. The joint distribution of arrivals in the two sub-processes before time $t$ is:
>    $$\mathbb{P}[X_1(t) = n, X_2(t) = m] = \mathbb{P}[X_1(t) = n \mid X(t) = n+m]\,\mathbb{P}[X(t) = n+m]$$
>    since if $X(t) = n+m$ and $X_1(t) = n$ then $X_2(t) = m$. The conditional probability $\mathbb{P}[X_1(t)=n \mid X(t)=n+m]$ is binomial (probability $p$ of accepting each of $n+m$ events):
>    $$= \binom{n+m}{n} p^n (1-p)^m \frac{e^{-\lambda t}(\lambda t)^{n+m}}{(n+m)!}$$
>    $$= \frac{(n+m)!}{n!\,m!} p^n(1-p)^m e^{-\lambda pt} e^{-\lambda(1-p)t} \frac{(\lambda t)^{n+m}}{(n+m)!}$$
>    $$= \frac{(\lambda pt)^n e^{-\lambda pt}}{n!} \cdot \frac{(\lambda(1-p)t)^m e^{-\lambda(1-p)t}}{m!}$$
>    which is the product of two Poisson distributions with rates $\lambda pt$ and $\lambda(1-p)t$. ✓
>
> From point 3 we know that $X_1(t)$ and $X_2(t)$ are independent at each fixed $t$. To prove independence of $X_1$ and $X_2$ as processes, we must show increments $X_1(t_3)-X_1(t_1)$ and $X_2(t_4)-X_2(t_2)$ are independent for every choice of intervals $[t_1,t_3]$ and $[t_2,t_4]$.
>
> There are three cases (see fig. 4.3):
>
> - **Case (a): $t_1 < t_2 < t_3 < t_4$** (partial overlap $[t_2,t_3]$). Split:
>   $$X_1(t_3)-X_1(t_1) = [X_1(t_3)-X_1(t_2)] + [X_1(t_2)-X_1(t_1)]$$
>   $$X_2(t_4)-X_2(t_2) = [X_2(t_4)-X_2(t_3)] + [X_2(t_3)-X_2(t_2)]$$
>   Since $X_1(t)$ and $X_2(t)$ are independent at the same time, the increments on the overlap $[t_2,t_3]$ are independent. The increments on disjoint intervals $[t_1,t_2]$ and $[t_3,t_4]$ are independent by the Poisson property. Sums of pairwise independent variables are independent. ✓
>
> - **Case (b): $t_1 < t_2 < t_4 < t_3$** (one interval inside the other). Split into three regions: two non-overlapping and one overlapping. Proceed as in case (a). ✓
>
> - **Case (c): disjoint intervals.** Trivially independent. ✓
>
> ![[Stochastic_Processes_2020_p133_img36.jpeg]]
> *(a) — The two time intervals may partially overlap.*
>
> ![[Stochastic_Processes_2020_p133_img37.jpeg]]
> *(b) — One interval fully contains the other.*
>
> ![[Stochastic_Processes_2020_p133_img38.jpeg]]
> *(c) — The two intervals are disjoint.*
> *Figure 4.3 — All possible overlaps of intervals $[t_1,t_3]$ and $[t_2,t_4]$.*
>
> $\square$
>
> **Intuition:** Each arrival independently "chooses" its type, so the type-1 stream and type-2 stream are independent Poisson processes. The rates split proportionally to $p$ and $1-p$. This is the continuous-time analog of Theorem 4.1.2.

---

## 4.5 Other Distributions

A Poisson process is much more than a collection of Poisson-distributed increments $X(t_n) - X(t_{n-1})$. Depending on which aspect of the process we focus on, different distributions emerge.

Let the **arrival times** (or *waiting times*) $W_i$ be the instants at which a new event occurs, and the **interarrival times** (or *sojourn times*) $S_i$ be the differences between consecutive arrival times:

$$S_i \equiv W_{i+1} - W_i$$

Clearly:

$$W_i = \sum_{k=0}^{i-1} S_k$$

![[Stochastic_Processes_2020_p134_img39.jpeg]]
*Figure 4.4 — A typical sample path of a Poisson process showing the waiting times $W_i$ and the sojourn times $S_n$.*

### Theorem 4.5.1 — Inter-Arrival Times are Exponential

> [!Important] Theorem 4.5.1 — Inter-Arrival Times are i.i.d. Exponential
> **Statement:** Inter-arrival times $S_i$ are i.i.d. exponential random variables with rate $\lambda$.
>
> **Proof:** See the proof of Theorem 2.2.1. $\blacksquare$
>
> **Intuition:** The memoryless property of the exponential distribution is the continuous-time analog of the Markov property. The time until the next arrival does not depend on when the last arrival occurred.

### Theorem 4.5.2 — Waiting Times are Gamma

> [!Important] Theorem 4.5.2 — Waiting Times have the Gamma Distribution
> **Statement:** The waiting time $W_n$, i.e. the time for the $n$-th event to occur, has the Gamma distribution:
> $$f_{W_n}(t) = \frac{\lambda^n t^{n-1}}{(n-1)!} e^{-\lambda t} \qquad n = 1, 2, \ldots \quad t \geq 0$$
>
> **Proof:**
> The Gamma distribution with parameters $n, \lambda$ (defined in §1.5.4) is the distribution of the sum of $n$ i.i.d. exponential random variables with parameter $\lambda$. Since:
> $$W_n = \sum_{i=0}^{n-1} S_i$$
> where each $S_i$ is exponential with rate $\lambda$ (by Theorem 4.5.1), the sum $W_n$ follows a Gamma distribution. $\blacksquare$
>
> **Intuition:** Waiting for the $n$-th event means waiting through $n$ successive exponential inter-arrival times. The Gamma distribution is the natural result.

### Theorem 4.5.3 — Conditional Arrival Times are Uniform

Suppose we fix the number $n$ of events in $(0,t)$. Then the joint probability of the arrival times $\{W_i\}_{i=1,\ldots,n}$ equals that of an ordered sequence of uniformly chosen points.

To derive this, suppose we choose independently $n$ points $U_i$ uniformly in $(0,t)$ (fig. 4.5). The joint distribution of $\{U_i\}_{i=1,\ldots,n}$ is the product of $n$ uniform pdfs.

![[Stochastic_Processes_2020_p135_img40.jpeg]]
*Figure 4.5 — Draw $n$ uniform points $U_i$ in $(0,t)$. Consider their ordered version $W_i$. The goal is to compute the statistics of the ordered points.*

Let $\{W_i\}$ be the ordered sequence with $0 \leq W_1 < W_2 < \cdots < W_n \leq t$. The $W_i$ are not independent (they must be in ascending order), which complicates their joint probability.

We start with $n=2$. Consider the probability that $W_1 \in [w_1, w_1 + \Delta w_1]$ and $W_2 \in [w_2, w_2 + \Delta w_2]$ (fig. 4.6):

![[Stochastic_Processes_2020_p135_img41.jpeg]]
*Figure 4.6 — Two intervals $[w_i, w_i + \Delta w_i]$. Either $U_1$ or $U_2$ may occupy each interval; there are two permutations.*

In the limit $\Delta w_1, \Delta w_2 \to 0$:

$$f_{W_1,W_2}(w_1,w_2)\,\Delta w_1\,\Delta w_2 = \mathbb{P}[w_1 \leq W_1 \leq w_1+\Delta w_1,\; w_2 \leq W_2 \leq w_2+\Delta w_2] \tag{4.5}$$

This equals the probability of $U_1$ (or $U_2$) being in $[w_1, w_1+\Delta w_1]$ and the other in $[w_2, w_2+\Delta w_2]$ — every permutation of the same $\{U_i\}$, once ordered, yields the same $\{W_i\}$, so we count all of them:

$$= \mathbb{P}[w_1 \leq U_1 \leq w_1+\Delta w_1,\; w_2 \leq U_2 \leq w_2+\Delta w_2] + \mathbb{P}[w_1 \leq U_2 \leq w_1+\Delta w_1,\; w_2 \leq U_1 \leq w_2+\Delta w_2]$$

We may sum the probabilities of all different permutations since they are mutually exclusive.

Since $U_1$ and $U_2$ are both uniform and independent:

$$\mathbb{P}[w_1 \leq U_1 \leq w_1+\Delta w_1,\; w_2 \leq U_2 \leq w_2+\Delta w_2] = \frac{\Delta w_1}{t} \cdot \frac{\Delta w_2}{t}$$

and the same holds for every other permutation, leading to:

$$f_{W_1,W_2}(w_1,w_2)\,\Delta w_1\,\Delta w_2 = 2\left(\frac{\Delta w_1}{t}\right)\left(\frac{\Delta w_2}{t}\right) = 2t^{-2}\,\Delta w_1\,\Delta w_2 \tag{4.6}$$

Dividing both (4.5) and (4.6) by $\Delta w_1\,\Delta w_2$ and passing to the limit:

$$f_{W_1,W_2}(w_1,w_2) = 2t^{-2}$$

The factor 2 comes from the two possible arrangements of $U_1$ and $U_2$. Generalizing to $n$ elements: there are $n!$ permutations, and the joint pdf is proportional to $t^{-n}$. Thus:

$$f_{W_1,W_2,\ldots,W_n}(w_1,w_2,\ldots,w_n) = n!\,t^{-n} \qquad \text{for } 0 < w_1 < w_2 < \cdots < w_n \leq t$$

Note the domain is not all of $(0,t)^n$ since the $w_i$ must be in ascending order. In contrast, for $n$ uniform points in $(0,t)$:

$$f_{U_1,U_2,\ldots,U_n}(w_1,w_2,\ldots,w_n) = t^{-n} \qquad \text{over entire } (0,t)^n$$

We can now formally state the link between Poisson processes and ordered uniform distributions:

> [!Important] Theorem 4.5.3 — Conditional Arrival Times are Ordered Uniforms
> **Statement:** Let $W_1, W_2, \ldots$ be the ordered occurrence times in a Poisson process of rate $\lambda > 0$. Conditioned on $X(t) \equiv N(t) = n$ (exactly $n$ events in $(0,t)$), the arrival times $\{W_1, W_2, \ldots, W_n\}$ have joint probability density function:
> $$f_{W_1,\ldots,W_n | X(t)=n}(w_1,\ldots,w_n) = n!\,t^{-n} \qquad \text{for } 0 < w_1 < \cdots < w_n \leq t$$
> In other words: given their number, the $n$ arrival times have the same joint distribution as an ordered sequence of $n$ independent uniform random variables on $(0,t)$.
>
> **Proof:**
> Assume all $w_i$ are distinct (in a Poisson process, simultaneous events have probability zero — in an infinitesimal interval the only relevant events are one arrival or none).
>
> Choose intervals $[w_i, w_i + \Delta w_i]$ that are all disjoint (possible since $\Delta w_i$ can be arbitrarily small). Consider the probability that the $i$-th arrival $W_i$ lies inside the $i$-th interval:
>
> $$\mathbb{P}[w_i \leq W_i \leq w_i + \Delta w_i,\; i=1,\ldots,n \mid X(t)=n] \tag{4.11}$$
>
> In the limit $\Delta w_i \to 0$, this is linear in the joint density:
> $$= f_{W_1,\ldots,W_n|X(t)=n}(w_1,\ldots,w_n)\,\Delta w_1\cdots\Delta w_n + o(\Delta w_1,\ldots,\Delta w_n)$$
>
> ![[Stochastic_Processes_2020_p137_img42.jpeg]]
> *Figure 4.7 — Expression (4.11) requires exactly one arrival in each interval $[w_i, w_i+\Delta w_i]$ and zero arrivals outside. Each increment over a disjoint interval is independent.*
>
> We compute (4.11): probability of exactly one arrival in each $[w_i, w_i+\Delta w_i]$ and zero arrivals elsewhere in $[0,t]$, given $n$ events have occurred. By independence of Poisson increments over disjoint intervals:
>
> $$= \frac{\lambda\Delta w_1 e^{-\lambda\Delta w_1}\cdots\lambda\Delta w_n e^{-\lambda\Delta w_n}\cdot e^{-\lambda(t - \sum_{i=1}^n \Delta w_i)}}{e^{-\lambda t}(\lambda t)^n/n!}$$
>
> The numerator factors are: probability of exactly one event in each $\Delta w_i$, and no events in the remaining $(t - \sum_i \Delta w_i)$. The denominator is $\mathbb{P}[X(t)=n]$ (conditioning on $n$ events). At the numerator, $e^{-\lambda\Delta w_1}\cdots e^{-\lambda\Delta w_n} = e^{-\lambda\sum_i \Delta w_i}$ cancels with $e^{-\lambda(t-\sum_i\Delta w_i)}$ to give $e^{-\lambda t}$, and $\lambda^n$ cancels the $\lambda^n$ from the denominator. We obtain:
>
> $$f_{W_1,\ldots,W_n|X(t)=n}(w_1,\ldots,w_n)\,\Delta w_1\cdots\Delta w_n + o(\cdots) = n!\,t^{-n}\,\Delta w_1\cdots\Delta w_n$$
>
> Dividing by $\Delta w_1\cdots\Delta w_n$ and taking the limit completes the proof:
> $$f_{W_1,\ldots,W_n|X(t)=n}(w_1,\ldots,w_n) = n!\,t^{-n} \qquad \blacksquare$$
>
> **Intuition:** If we know exactly how many arrivals occurred in a Poisson process, all that remains is *where* they fell. The Poisson process "places" each arrival independently and uniformly — the ordering structure arises automatically.

### Theorem 4.5.4 — Binomial Conditional Distribution

> [!Important] Theorem 4.5.4 — Binomial Conditional Distribution
> **Statement:** Let $X(t)$ be a Poisson process with rate $\lambda$. Given $X(t) = n$, the number of arrivals in the subset $(0,u)$ with $0 < u < t$ and $0 \leq k \leq n$ is:
> $$\mathbb{P}[X(u) = k \mid X(t) = n] = \binom{n}{k}\left(\frac{u}{t}\right)^k\left(1 - \frac{u}{t}\right)^{n-k}$$
>
> ![[Stochastic_Processes_2020_p138_img43.jpeg]]
> *Figure 4.8 — Given $n$ events in $(0,t)$, each arrival time is uniform in $(0,t)$, so each falls in $(0,u)$ with probability $p = u/t$. The number of events in $(0,u)$ is binomial$(n, u/t)$.*
>
> **Proof:**
> By Theorem 4.5.3, given $X(t) = n$, the $n$ arrival times are i.i.d. uniform on $(0,t)$. The probability that each falls in $[0,u]$ is $u/t$. Therefore $X(u) \mid X(t)=n$ is Binomial$(n, u/t)$. $\blacksquare$
>
> **Intuition:** Knowing the total count reduces the problem to a binomial: each event independently "decides" to fall in $(0,u)$ with probability $u/t$.

### Theorem 4.5.5 — Two Processes, Conditional Distribution

> [!Important] Theorem 4.5.5 — Conditional Distribution for Two Concurrent Processes
> **Statement:** Let $X_1(t), X_2(t)$ be independent Poisson processes with rates $\lambda_1, \lambda_2$. Given $X_1(t) + X_2(t) = n$, the probability of $k$ arrivals in process 1 is:
> $$\mathbb{P}[X_1(t) = k \mid X_1(t)+X_2(t) = n] = \binom{n}{k}\left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^k\left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k} \tag{4.12}$$
>
> As expected, this is binomial. The probability $p_1 = \lambda_1/(\lambda_1+\lambda_2)$ that a generic event belongs to process 1 is the ratio of $\lambda_1$ to the total rate. If $\lambda_1 = \lambda_2$, then $p_1 = 1/2$.
>
> **Proof:**
> By the definition of conditional probability:
> $$\mathbb{P}[X_1(t)=k \mid X_1(t)+X_2(t)=n] = \frac{\mathbb{P}[X_1(t)=k,\; X_1(t)+X_2(t)=n]}{\mathbb{P}[X_1(t)+X_2(t)=n]}$$
>
> If $X_1(t)+X_2(t)=n$ and $X_1(t)=k$, then $X_2(t)=n-k$. Since $X_1$ and $X_2$ are independent:
>
> $$= \frac{\mathbb{P}[X_1(t)=k]\,\mathbb{P}[X_2(t)=n-k]}{\mathbb{P}[X_1(t)+X_2(t)=n]}$$
>
> $$= \frac{\dfrac{e^{-\lambda_1 t}(\lambda_1 t)^k}{k!} \cdot \dfrac{e^{-\lambda_2 t}(\lambda_2 t)^{n-k}}{(n-k)!}}{\dfrac{e^{-(\lambda_1+\lambda_2)t}[(\lambda_1+\lambda_2)t]^n}{n!}}$$
>
> $$= \binom{n}{k}\left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^k\left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k} \qquad \blacksquare$$
>
> **Intuition:** Given a total of $n$ arrivals from two independent Poisson streams, each arrival independently "belongs" to stream 1 with probability proportional to $\lambda_1$. The result is binomial.

### Corollary 4.5.1 — Combined Conditional Distribution

> [!Important] Corollary 4.5.1 — Combined Conditional Distribution
> **Statement:** Let $X_1(t)$ and $X_2(t)$ be independent Poisson processes with rates $\lambda_1, \lambda_2$ in $(0,t)$. Let $0 < s < t$. Given $X_1(t)+X_2(t) = n$, the probability of $0 \leq k \leq n$ events from process 1 in the subset $(0,s)$ is:
> $$\mathbb{P}[X_1(s)=k \mid X_1(t)+X_2(t)=n] = \frac{n!}{k!(n-k)!}\left(\frac{\lambda_1 s}{(\lambda_1+\lambda_2)t}\right)^k\left(\frac{\lambda_1(t-s)+\lambda_2 t}{(\lambda_1+\lambda_2)t}\right)^{n-k}$$
>
> **Proof:**
> By definition of conditional probability:
> $$\mathbb{P}[X_1(s)=k \mid X_1(t)+X_2(t)=n] = \frac{\mathbb{P}[X_1(s)=k,\; X_1(t)+X_2(t)=n]}{\mathbb{P}[X_1(t)+X_2(t)=n]}$$
>
> If $n$ events occurred in $X_1+X_2$ during $(0,t)$, with $k$ belonging to process 1 in $(0,s)$, then $n-k$ events must have occurred in $X_2$ during $(0,t)$ or in $X_1$ during $(s,t)$: $X_1(t)-X_1(s)+X_2(t) = n-k$. These random variables are all independent, so the joint probability factorizes:
>
> $$= \frac{\mathbb{P}[X_1(s)=k]\,\mathbb{P}[X_1(t)-X_1(s)+X_2(t)=n-k]}{\mathbb{P}[X_1(t)+X_2(t)=n]}$$
>
> ![[Stochastic_Processes_2020_p140_img44.jpeg]]
>
> ![[Stochastic_Processes_2020_p140_img45.jpeg]]
> *Figure 4.9 — The situation has a geometric interpretation: the term $(\lambda_1 s / ((\lambda_1+\lambda_2)t))^k$ is the ratio between the small rectangle (representing the event we seek) and the larger rectangle (the conditional event). The product of the two sides of each rectangle returns the Poisson parameter.*
>
> This result has a geometric interpretation (fig. 4.9): the parameter $\frac{\lambda_1 s}{(\lambda_1+\lambda_2)t}$ is the ratio between the small area in the figure (the event we are looking for) and the larger area (the conditional event). $\blacksquare$

---

### 4.5.1 M/G/∞ Queue

We now apply the above theorems to an example involving a radioactive mass (or equivalently, a service station with infinitely many servers).

A service station: each user arrives according to a Poisson process at time $W_k$, remains for a duration $Y_k$, then departs. Unlike $M/G/1$ or $G/M/1$, there is **no waiting time for service**: once a customer enters the system they are immediately served regardless of how many are already being served. We describe this as an **M/G/∞ queue**: $M$ denotes Poisson arrivals, $G$ denotes generic service-time distribution, $\infty$ means infinitely many servers.

> [!Example] Example — Radioactive Particles (M/G/∞ Queue)
> **Problem:** Alpha particles appear according to a Poisson process of intensity $\lambda$. Each particle exists for a random duration before annihilation; successive lifetimes $Y_1, Y_2, \ldots$ are i.i.d. with common distribution function $G(y) = \Pr\{Y_k \leq y\}$. Let $X(t)$ be the total number of particles created up to time $t$, and $M(t)$ count the number existing at time $t$. Find the distribution of $M(t)$ given $M(0) = 0$.
>
> ![[Stochastic_Processes_2020_p141_img46.jpeg]]
> *Figure 4.10 — Particle created at time $W_k \leq t$ still exists at time $t$ if $W_k + Y_k \geq t$.*
>
> **Approach:** Condition on $X(t)=n$, invoke Theorem 4.5.3 to replace ordered arrival times by i.i.d. uniforms, then marginalize.
>
> **Solution:**
>
> Condition on $X(t) = n$ with creation times $W_1, \ldots, W_n \leq t$. Particle $k$ still exists at time $t$ iff $W_k + Y_k \geq t$. Introduce the indicator:
> $$\mathbf{1}\{W_k + Y_k \geq t\} = \begin{cases} 1 & \text{if } W_k + Y_k \geq t \\ 0 & \text{if } W_k + Y_k < t \end{cases}$$
>
> Then:
> $$\Pr\{M(t)=m \mid X(t)=n\} = \Pr\left\{\sum_{k=1}^n \mathbf{1}\{W_k+Y_k \geq t\} = m \;\Big|\; X(t)=n\right\} \tag{4.13}$$
>
> The expression $\{W_k + Y_k \geq t\}$ is symmetric (invariant under permutation of the $W$'s), so by Theorem 4.5.3 we may replace each $W_i$ with an i.i.d. uniform $U_i$ on $(0,t]$:
>
> $$= \Pr\left\{\sum_{k=1}^n \mathbf{1}\{U_k + Y_k \geq t\} = m\right\}$$
>
> Since both $U_k$ and $Y_k$ are i.i.d., each indicator is a binary variable independent of all others. Their sum is Binomial$(n,p)$ where:
>
> $$p = \Pr\{U_k + Y_k \geq t\} = \frac{1}{t}\int_0^t \Pr\{Y_k \geq t-u\}\,du = \frac{1}{t}\int_0^t [1-G(t-u)]\,du = \frac{1}{t}\int_0^t [1-G(z)]\,dz$$
>
> (substituting $z = t-u$). Therefore:
>
> $$\Pr\{M(t)=m \mid X(t)=n\} = \frac{n!}{m!(n-m)!} p^m (1-p)^{n-m}$$
>
> To remove the condition $X(t)=n$, marginalize over the Poisson distribution of $X(t)$. Composing a Binomial$(n,p)$ with Poisson$(n=\lambda t)$ gives a Poisson with scaled rate (by Theorem 4.1.2):
>
> $$\Pr\{M(t)=m\} = \sum_{n=m}^\infty \frac{n!}{m!(n-m)!} p^m(1-p)^{n-m} \frac{(\lambda t)^n e^{-\lambda t}}{n!}$$
>
> $$= e^{-\lambda t}\frac{(\lambda pt)^m}{m!} \sum_{n=m}^\infty \frac{(1-p)^{n-m}(\lambda t)^{n-m}}{(n-m)!}$$
>
> The sum is a geometric/exponential series:
> $$\sum_{n=m}^\infty \frac{(1-p)^{n-m}(\lambda t)^{n-m}}{(n-m)!} = \sum_{j=0}^\infty \frac{[\lambda t(1-p)]^j}{j!} = e^{\lambda t(1-p)}$$
>
> Therefore:
>
> $$\boxed{\Pr\{M(t)=m\} = \frac{e^{-\lambda pt}(\lambda pt)^m}{m!} \qquad m = 0, 1, \ldots} \tag{4.14}$$
>
> The number of existing particles at time $t$ has a **Poisson distribution** with mean:
>
> $$\lambda pt = \lambda \int_0^t [1-G(y)]\,dy$$
>
> **Long-run behavior:** As $t \to \infty$, $\int_0^t[1-G(y)]\,dy \to \int_0^\infty[1-G(y)]\,dy = 1/\mu$ (the mean service time). So in the long run:
>
> $$\lambda pt \xrightarrow{t\to\infty} \frac{\lambda}{\mu}$$
>
> The asymptotic mean depends only on the mean $\mu$ of the lifetime distribution, not its shape. This implies that two different distributions $G(y)$ with the same mean will converge to the same stationary distribution. Moreover, if the lifetime has a finite maximum $t_\text{MAX}$, the tail $[1-G(y)] \to 0$ for $y > t_\text{MAX}$, so the asymptotic behavior is reached already for $t > t_\text{MAX}$.
>
> **Takeaway:** For M/G/∞ queues, the Poisson form is preserved. The steady-state mean equals $\lambda/\mu$ — Little's Law: mean number in system = arrival rate × mean service time.

### 4.5.2 Shot Noise Process

A **Shot Noise process** models electrical effects produced by the random arrival of electrons to an anode.

**Hypotheses:**
- Electrons arrive according to a Poisson process $\{X(t); t \geq 0\}$ with rate $\lambda$.
- An arriving electron produces a current pulse with intensity per unit time given by the impulse response function $h(x)$.

![[Stochastic_Processes_2020_p144_img47.jpeg]]
*Figure 4.11 — Different pulses generated by electrons arriving at different times. The total current is $I(t) = \sum_{k=1}^{X(t)} h(t-W_k)$.*

The total current intensity $I(t)$ is the superposition of all impulse responses from electrons that have arrived up to time $t$:

$$I(t) = \sum_{k=1}^{X(t)} h(t - W_k)$$

Each pulse is shifted by the arrival time $W_k$ of the $k$-th electron. We want the statistics of $I(t)$:

$$\Pr\{I(t) \leq x\} = \Pr\left\{\sum_{k=1}^{X(t)} h(t-W_k) \leq x\right\}$$

Conditioning on the total number $n$ of arrivals and marginalizing:

$$= \sum_{n=0}^\infty \Pr\left\{\sum_{k=1}^n h(t-W_k) \leq x \;\Big|\; X(t)=n\right\} \Pr\{X(t)=n\}$$

The expression $\sum_k h(t-W_k) \leq x$ is symmetric in the $W_k$'s (all response functions are equal; order of summation irrelevant), so by Theorem 4.5.3 we replace $W_k$ with i.i.d. uniforms $U_k$:

$$= \sum_{n=0}^\infty \Pr\left\{\sum_{k=1}^n h(t-U_k) \leq x\right\} \Pr\{X(t)=n\}$$

Since $U_k$ and $t-U_k$ share the same distribution, we may write $h(U_k)$:

$$= \sum_{n=0}^\infty \Pr\left\{\sum_{k=1}^n h(U_k) \leq x\right\} \Pr\{X(t)=n\}$$

Converting back to a random sum:

$$\Pr\{I(t) \leq x\} = P\left\{\sum_{k=1}^{X(t)} h(U_k) \leq x\right\}$$

The $U_k$'s are i.i.d. and independent of $X(t)$, so the statistics of the random sum can be found via generating or characteristic functions, or via the first two moments.

**Mean:** The expected value of a random sum is the product of the expected number of terms times the common expected value of each term:

$$\mathbb{E}[I(t)] = \mathbb{E}[X(t)]\,\mathbb{E}[h(U_k)] = \lambda t \cdot \frac{1}{t}\int_0^t h(u)\,du = \lambda\int_0^t h(u)\,du$$

**Variance:** The variance of a random sum is:

$$\operatorname{Var}(I(t)) = \lambda t\,\operatorname{Var}(h(U_k)) + \lambda t\,\mathbb{E}[h(U_k)]^2 = \lambda t\Big(\operatorname{Var}(h(U_k)) + \mathbb{E}[h(U_k)]^2\Big)$$

$$= \lambda t\,\mathbb{E}[(h(U_k))^2] = \lambda t \cdot \frac{1}{t}\int_0^t h^2(u)\,du = \lambda\int_0^t h^2(u)\,du$$

where we used $\mathbb{E}[X^2] = \operatorname{Var}(X) + \mathbb{E}[X]^2$.

**Long-run behavior:** As $t \to \infty$ (integrating beyond the pulse duration), the integral becomes the area under the pulse in figure 4.11. In the limit, both $\mathbb{E}[I(t)]$ and $\operatorname{Var}(I(t))$ depend only on the area $\int_0^\infty h(u)\,du$, not on the pulse shape. Pulses of different shapes but the same area produce, on average, the same current.


---

## 4.6 Binomial Theorem

We recall a theorem already seen at page 138:

### Theorem 4.6.1 — Binomial Theorem (Direct Proof)

> [!Important] Theorem 4.6.1 — Binomial Theorem
> **Statement:** Let $[X(t)]$ be a Poisson process of rate $\lambda > 0$. Then for $0 < u < t$ and $0 \leq k \leq n$:
> $$\Pr\{X(u)=k \mid X(t)=n\} = \frac{n!}{k!(n-k)!}\left(\frac{u}{t}\right)^k\left(1-\frac{u}{t}\right)^{n-k}$$
>
> We have already proved this using Theorem 4.5.3. There is also a direct proof, often requested on written tests.
>
> **Proof (direct):**
> By the definition of conditional probability:
> $$\Pr\{X(u)=k \mid X(t)=n\} = \frac{\Pr\{X(u)=k \text{ and } X(t)=n\}}{\Pr\{X(t)=n\}}$$
> $$= \frac{\Pr\{X(u)=k \text{ and } X(t)-X(u)=n-k\}}{\Pr\{X(t)=n\}}$$
>
> ![[Stochastic_Processes_2020_p146_img48.jpeg]]
> *Figure 4.12 — The two intervals $(0,u)$ and $(u,t)$ are disjoint, so their increments are independent. Note: $(0,u)$ and $(0,t-u)$ overlap and are NOT independent (though they share the same statistics).*
>
> The numerator expresses the joint probability of $k$ events in $(0,u)$ and $n-k$ events in $(u,t)$. The two intervals $(0,u)$ and $(u,t)$ are **disjoint**, so the corresponding increments are **independent**. Moreover, the increment in $(u,t)$ has the same distribution as the increment in $(0,t-u)$ by stationarity. We can only substitute $X(t)-X(u) \to X(t-u)$ **after** factorizing — failing to do so would conflate $X(u)$ and $X(t-u)$, which are **not** independent (their intervals overlap). After factorization:
>
> $$= \frac{\Pr\{X(u)=k\}\,\Pr\{X(t-u)=n-k\}}{\Pr\{X(t)=n\}}$$
>
> Substituting the Poisson distributions:
>
> $$= \frac{\left\{e^{-\lambda u}(\lambda u)^k/k!\right\}\left\{e^{-\lambda(t-u)}[\lambda(t-u)]^{n-k}/(n-k)!\right\}}{e^{-\lambda t}(\lambda t)^n/n!}$$
>
> Simplifying:
>
> $$= \frac{n!}{k!(n-k)!}\frac{u^k(t-u)^{n-k}}{t^n} \qquad \square$$
>
> **Intuition:** The two sub-intervals partition $[0,t]$. Each arrival independently falls in $(0,u)$ with probability $u/t$ — the result is binomial.

### Dual Version

> [!Important] Dual Version of Theorem 4.6.1
> **Statement:** (Dual version)
> $$\Pr\{X(s)=k \mid X(t)=n\} \qquad 0 \leq n \leq k,\quad 0 < t < s$$
> Here we want the probability of $k$ arrivals in the *larger* interval $(0,s)$, conditioned on $n$ arrivals in the *smaller* interval $(0,t)$. This is equivalent to having $k-n$ arrivals in the interval $(t,s)$.
>
> **Proof:**
> By the definition of conditional probability:
> $$\frac{\Pr\{X(s)=k,\; X(t)=n\}}{\Pr\{X(t)=n\}} = \frac{\Pr\{X(t)=n,\; X(s)-X(t)=k-n\}}{\Pr\{X(t)=n\}}$$
>
> Since $X(t)$ and $X(s)-X(t)$ refer to **disjoint** intervals $(0,t)$ and $(t,s)$, they are independent and factorize:
>
> $$= \frac{\Pr\{X(t)=n\}\,\Pr\{X(s)-X(t)=k-n\}}{\Pr\{X(t)=n\}} = \Pr\{X(s)-X(t)=k-n\}$$
>
> By stationarity (this substitution is valid only **after** factorization):
>
> $$= \Pr\{X(s-t)=k-n\} = \frac{e^{-\lambda(s-t)}(\lambda(s-t))^{k-n}}{(k-n)!} \qquad \square$$
>
> **Intuition:** Conditioning on events in the past only "uses up" $n$ arrivals, leaving $k-n$ more to occur in the future interval $(t,s)$.

---

> [!Example] Exercise 4.6.1 — Two Independent Processes (Written Test, June 27, 2016)
> **Problem:** Consider two independent Poisson processes $X_1(t)$ and $X_2(t)$, where $X_i(t)$ counts arrivals of process $i$ during $[0,t]$. Rates: $\lambda_1 = 0.5$, $\lambda_2 = 1$.
>
> 1. Compute $P[X_1(2)=1 \mid X_1(3)=2]$ and $P[X_1(3)=2 \mid X_1(2)=1]$
> 2. Compute $P[X_1(1)=1 \mid X_1(2)+X_2(2)=3]$ and $P[X_1(2)+X_2(2)=3 \mid X_1(1)=1]$
> 3. Compute $P[X_1(2)+X_2(2)=3 \mid X_1(3)=0]$ and $P[X_1(2)+X_2(2)=3 \mid X_1(3)=1]$
>
> **Solution:**
>
> **Part 1.** The first probability: given $n=2$ arrivals in the large interval $[0,3]$, the number of arrivals in the smaller interval $[0,2]$ is Binomial$(n=2, p=2/3)$ (ratio of interval lengths):
>
> $$P[X_1(2)=1 \mid X_1(3)=2] = \binom{2}{1}\left(\frac{2}{3}\right)^1\left(\frac{1}{3}\right)^{2-1} = \frac{4}{9} \approx 0.44$$
>
> For the second: given $X_1(2)=1$, we need $X_1(3)=2$, which requires $X_1(3)-X_1(2)=1$. By the dual version:
>
> $$P[X_1(3)=2 \mid X_1(2)=1] = P[X_1(3)-X_1(2)=1] = P[X_1(1)=1] = 0.5\,e^{-0.5} \approx 0.3$$
>
> **Part 2.** The first probability involves $X_1$ given the sum $X_1+X_2$. Using Theorem 4.5.5 with the geometric interpretation (fig. 4.9): the combined process has rate $\lambda_1+\lambda_2=1.5$ over interval $[0,2]$. The event $X_1(1)=1$ corresponds to process 1 having 1 arrival in $[0,1]$. This is Binomial$(n=3, p)$ where $p$ is the ratio of areas:
>
> $$P[X_1(1)=1 \mid X(2)=3] = \binom{3}{1}\left(\frac{1}{6}\right)^1\left(\frac{5}{6}\right)^{3-1} = \frac{25}{72} \approx 0.347$$
>
> *(Note: $p = \lambda_1 \cdot 1 / [(\lambda_1+\lambda_2) \cdot 2] = 0.5/3 = 1/6$; here $X(t) = X_1(t)+X_2(t)$).*
>
> For the second: given $X_1(1)=1$, we need $X_2(2)+X_1(2)-X_1(1)=2$. This is a Poisson with parameter equal to the area of the remaining region $[\lambda_1+\lambda_2]\times[0,2] - \lambda_1\times[0,1] = 2.5$:
>
> $$P[X(2)=3 \mid X_1(1)=1] = P[X_2(2)+X_1(2)-X_1(1)=2] = \frac{(2.5)^2 e^{-2.5}}{2} \approx 0.2565$$
>
> **Part 3.** This case is different: neither the event $(X_1(2)+X_2(2)=3)$ nor the condition $(X_1(3)=k)$ fully contains the other — the intervals partially overlap.
>
> *First sub-part* ($X_1(3)=0$): the condition means no arrivals from $X_1$ in all of $[0,3]$, hence no arrivals from $X_1$ in $[0,2]$ either. All 3 arrivals must come from $X_2$ in $[0,2]$:
>
> $$P[X_1(2)+X_2(2)=3 \mid X_1(3)=0] = P[X_2(2)=3] = \frac{2^3 e^{-2}}{3!} = \frac{4}{3}e^{-2} \cdot \frac{1}{2} = \frac{4}{9}e^{-2} \approx 0.06$$
>
> *(Note: $\lambda_2 t = 1 \cdot 2 = 2$, so $P[X_2(2)=3] = 2^3 e^{-2}/6 = 4e^{-2}/3 \approx 0.180$. The text gives $4/9\,e^{-2}$ but the calculation yields $4/3\,e^{-2}/2 = 4e^{-2}/3$; following the source as given.)*
>
> *Second sub-part* ($X_1(3)=1$): the single $X_1$-arrival may be in $(0,2)$ or $(2,3)$. Apply the law of total probability conditioning on $X_1(2) \in \{0,1\}$:
>
> $$P[X_1(2)+X_2(2)=3 \mid X_1(3)=1] = \sum_{i=0}^1 P[X_1(2)+X_2(2)=3 \mid X_1(2)=i]\,P[X_1(2)=i \mid X_1(3)=1]$$
>
> Given $X_1(2)=i$, we need $X_2(2)=3-i$. The weights are binomial with $p=2/3$ (ratio $2/3$):
>
> $$= \underbrace{P[X_2(2)=3] \cdot \frac{1}{3}}_{i=0} + \underbrace{P[X_2(2)=2] \cdot \frac{2}{3}}_{i=1}$$
>
> $$= \frac{2^3 e^{-2}}{3!}\cdot\frac{1}{3} + \frac{2^2 e^{-2}}{2!}\cdot\frac{2}{3} = \frac{4}{9}e^{-2} + \frac{4}{3}e^{-2} = \frac{16}{9}e^{-2} \approx 0.24$$
>
> ![[Stochastic_Processes_2020_p150_img49.jpeg]]
> *Figure 4.13 — Graph for part (c) of Exercise 4.6.1.*
>
> **Takeaway:** When intervals partially overlap, use the law of total probability to condition on an intermediate event that decouples the overlap.

> [!Example] Exercise 4.6.2 — Finite Delay-Line Markov Chain
> **Problem:** A Markov chain has the transition probability:
>
> |   | 0 | 1 | 2 | 3 | 4 | 5 |
> |---|---|---|---|---|---|---|
> | 0 | α₁ | α₂ | α₃ | α₄ | α₅ | α₆ |
> | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
> | 2 | 0 | 1 | 0 | 0 | 0 | 0 |
> | 3 | 0 | 0 | 1 | 0 | 0 | 0 |
> | 4 | 0 | 0 | 0 | 1 | 0 | 0 |
> | 5 | 0 | 0 | 0 | 0 | 1 | 0 |
>
> where $\alpha_i \geq 0$, $i=1,\ldots,6$, and $\sum_{i=1}^6 \alpha_i = 1$.
>
> Determine the limiting probability of being in state 0.
>
> ![[Stochastic_Processes_2020_p151_img50.jpeg]]
> *Figure 4.14 — Transition diagram for Exercise 4.6.2.*
>
> **Solution:**
>
> Write the stationary equations $\vec{\pi} = \vec{\pi}\mathbf{P}$ (one per column):
>
> | $\pi_0 = \pi_0\alpha_1 + \pi_1$ |
> | $\pi_1 = \pi_0\alpha_2 + \pi_2$ |
> | $\pi_2 = \pi_0\alpha_3 + \pi_3$ |
> | $\pi_3 = \pi_0\alpha_4 + \pi_4$ |
> | $\pi_4 = \pi_0\alpha_5 + \pi_5$ |
> | $\pi_5 = \pi_0\alpha_6$ |
>
> Starting from the last row and substituting recursively upward:
>
> | $\pi_0 = (\alpha_1+\alpha_2+\alpha_3+\alpha_4+\alpha_5+\alpha_6)\pi_0 = \pi_0$ |
> | $\pi_1 = (\alpha_2+\alpha_3+\alpha_4+\alpha_5+\alpha_6)\pi_0$ |
> | $\pi_2 = (\alpha_3+\alpha_4+\alpha_5+\alpha_6)\pi_0$ |
> | $\pi_3 = (\alpha_4+\alpha_5+\alpha_6)\pi_0$ |
> | $\pi_4 = (\alpha_5+\alpha_6)\pi_0$ |
> | $\pi_5 = \alpha_6\pi_0$ |
>
> Each $\pi_i$ equals $\left(\sum_{k=i+1}^6 \alpha_k\right)\pi_0$, i.e. $1 - \sum_{k=1}^i\alpha_k$ times $\pi_0$. Applying the normalization $\sum_{i=0}^5 \pi_i = 1$:
>
> $$\left(\sum_{k=1}^6 k\alpha_k\right)\pi_0 = 1$$
>
> Therefore:
>
> $$\pi_0 = \frac{1}{\sum_{i=1}^6 k\alpha_k} = \frac{1}{\text{mean of } \alpha \text{ distribution}}$$
>
> **Intuition:** From state 0, the chain jumps to state $i$ with probability $\alpha_{i+1}$ and then deterministically returns to 0 in exactly $i+1$ steps. The mean return time to 0 is $\sum_{k=1}^6 k\alpha_k$, and $\pi_0$ is its reciprocal — consistent with the positive recurrence criterion.
>
> **Takeaway:** $\pi_0 = 1/\mathbb{E}[\text{return time to 0}]$. For delay-line chains this equals the reciprocal of the mean of the "jump distribution".

> [!Example] Exercise 4.6.3 — Infinite Delay-Line Chain
> **Problem:** Let $\{\alpha_i : i = 1, 2, \ldots\}$ be a probability distribution. Consider the same delay-line Markov chain extended to infinite states:
>
> |   | 0 | 1 | 2 | 3 | ... |
> |---|---|---|---|---|-----|
> | 0 | α₁ | α₂ | α₃ | α₄ | ... |
> | 1 | 1 | 0 | 0 | 0 | ... |
> | 2 | 0 | 1 | 0 | 0 | ... |
> | 3 | 0 | 0 | 1 | 0 | ... |
> | ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮ |
>
> Assume $\alpha_1 > 0$ and $\alpha_2 > 0$ (so the chain is aperiodic). What condition on $\{\alpha_i\}$ is necessary and sufficient for a limiting distribution to exist, and what is this distribution?
>
> **Solution:**
>
> The same substitution as Exercise 4.6.2 gives:
>
> $$\pi_n = \left(\sum_{k=n+1}^\infty \alpha_k\right)\pi_0$$
>
> Applying the normalization $\sum_{n=0}^\infty \pi_n = 1$:
>
> $$\pi_0 = \left(\sum_{n=0}^\infty \sum_{k=n+1}^\infty \alpha_k\right)^{-1} = \left(\sum_{n=0}^\infty P[X > n]\right)^{-1}$$
>
> The double sum $\sum_{n=0}^\infty \sum_{k=n+1}^\infty \alpha_k = \sum_{n=0}^\infty P[X > n]$ is precisely $\mathbb{E}[X]$ — the mean of the distribution $\{\alpha_k\}$. For $\pi_0 > 0$ this must be **finite**. Therefore:
>
> **Necessary and sufficient condition:** $\mathbb{E}[X] = \sum_{k=1}^\infty k\alpha_k < \infty$.
>
> The limiting distribution is:
>
> $$\pi_0 = \frac{1}{\mathbb{E}[X]}, \qquad \pi_n = \frac{P[X > n]}{\mathbb{E}[X]}$$
>
> **Takeaway:** A limiting distribution exists iff the mean return time is finite, i.e. iff $\mathbb{E}[X] < \infty$. This is the infinite-state version of positive recurrence.

> [!Example] Exercise 4.6.4 — Fraction of Transitions Between Two States
> **Problem:** A finite-state regular Markov chain has transition matrix $\mathbf{P} = |P_{ij}|$ and limiting distribution $\pi = |\pi_i|$. In the long run, what fraction of transitions are from state $k$ to state $m$?
>
> **Solution:**
>
> In the long run, the probability of being in state $k$ is $\pi_k$. From state $k$, the probability of transitioning to $m$ is $P_{km}$. Therefore the fraction of transitions from $k$ to $m$ is:
>
> $$\pi_k P_{km} = \lim_{n\to\infty} P[X_n = k,\; X_{n+1} = m]$$
>
> Since the chain is regular, the initial state is irrelevant.

> [!Example] Exercise 4.6.5 — Limits for a Regular Chain
> **Problem:** Determine the following limits in terms of $\mathbf{P}$ and $\pi$ for a finite-state regular Markov chain $\{X_n\}$:
>
> 1. $\lim_{n\to\infty} P[X_{n+1} = j \mid X_0 = i]$
> 2. $\lim_{n\to\infty} P[X_n = k,\; X_{n+1} = j \mid X_0 = i]$
> 3. $\lim_{n\to\infty} P[X_{n-1} = k,\; X_n = j \mid X_0 = i]$
>
> **Solution:**
>
> **1.** Since the chain is regular, the limit is independent of the starting state and the exact index $n$ vs $n+1$:
>
> $$\lim_{n\to\infty} P[X_{n+1} = j \mid X_0 = i] = \pi_j$$
>
> **2.** Using the definition of conditional probability and dropping the initial condition (Markov property):
>
> $$\lim_{n\to\infty} P[X_n = k,\; X_{n+1} = j \mid X_0 = i] = \lim_{n\to\infty} P[X_{n+1} = j \mid X_n = k,\; X_0 = i]\,P[X_n = k \mid X_0 = i]$$
>
> The first factor is $P_{kj}$ (one-step transition); the second factor converges to $\pi_k$:
>
> $$= \pi_k P_{kj}$$
>
> **3.** This is just a time-shifted version of (2):
>
> $$\lim_{n\to\infty} P[X_{n-1} = k,\; X_n = j \mid X_0 = i] = \pi_k P_{kj}$$

> [!Example] Exercise 4.6.6 — Backward Probability
> **Problem:** A Markov chain has transition probability matrix:
>
> $$\mathbf{P} = \begin{array}{c|ccc} & 0 & 1 & 2 \\ \hline 0 & 0.4 & 0.4 & 0.2 \\ 1 & 0.6 & 0.2 & 0.2 \\ 2 & 0.4 & 0.2 & 0.4 \end{array}$$
>
> After a long time, the chain is observed in state 1. Find:
> $$\lim_{n\to\infty} P[X_{n-1} = 2 \mid X_n = 1]$$
>
> **Solution:**
>
> This requires looking at the chain *backwards*. By the definition of conditional probability:
>
> $$P[X_{n-1}=2 \mid X_n=1] = \frac{P[X_{n-1}=2,\; X_n=1]}{P[X_n=1]} = \frac{P[X_n=1 \mid X_{n-1}=2]\,P[X_{n-1}=2]}{P[X_n=1]} = P_{21}\,\frac{P[X_{n-1}=2]}{P[X_n=1]}$$
>
> In the limit $n \to \infty$, both $P[X_{n-1}=2]$ and $P[X_n=1]$ converge to $\pi_2$ and $\pi_1$ respectively:
>
> $$\lim_{n\to\infty} P[X_{n-1}=2 \mid X_n=1] = P_{21}\frac{\pi_2}{\pi_1} = \frac{6}{35} \approx 0.1714$$
>
> where $P_{21} = 0.2$ and $\pi_1, \pi_2$ are obtained by solving the stationary equations.

> [!Example] Exercise 4.6.7 — Man with Car(s)
> **Problem:** A man either drives or walks between home and office. He drives if it is raining and his car is at his current location; otherwise he walks. Each morning and afternoon it rains independently with probability $p$. In the long run, on what fraction of *trips* does the man walk in the rain? What if he owns two cars?
>
> **Solution — One Car:**
>
> Define states:
> - $X_n = 1$: car is at man's current location (available)
> - $X_n = 0$: car is not available
>
> Transition matrix: if the man has no car ($X_n=0$), he walks and arrives where the car is, so $X_{n+1}=1$ with probability 1. If he has the car ($X_n=1$), he drives (if raining, prob $p$) and keeps the car, or walks (prob $1-p$) and leaves the car:
>
> $$\mathbf{P} = \begin{array}{c|cc} & 0 & 1 \\ \hline 0 & 0 & 1 \\ 1 & 1-p & p \end{array}$$
>
> Stationary distribution (proportional to incoming rates, normalized):
>
> $$\pi_0 = \frac{1-p}{2-p}, \qquad \pi_1 = \frac{1}{2-p}$$
>
> Probability of walking in the rain on a given trip (condition on car availability):
>
> $$\pi_0 \cdot p + \pi_1 \cdot (1-p) \cdot p = \frac{2p(1-p)}{2-p}$$
>
> The first term: man has no car (prob $\pi_0$) and it rains (prob $p$) → he walks in the rain. The second term: man has the car (prob $\pi_1$), it doesn't rain in the morning (prob $1-p$), so he walks to the office; if it rains in the afternoon (prob $p$), he has no car there → walks in the rain.
>
> **Solution — Two Cars:**
>
> Define $X_n$ = number of cars at man's current location ($0, 1$, or $2$):
>
> $$\mathbf{P} = \begin{array}{c|ccc} & 0 & 1 & 2 \\ \hline 0 & 0 & 0 & 1 \\ 1 & 0 & 1-p & p \\ 2 & 1-p & p & 0 \end{array}$$
>
> Stationary distribution:
>
> $$\pi_0 = \frac{1-p}{3-p}, \qquad \pi_1 = \frac{1}{3-p}, \qquad \pi_2 = \frac{1}{3-p}$$
>
> Probability of walking in the rain:
>
> $$\pi_0 \cdot p + \pi_2 \cdot (1-p) \cdot p = \frac{2p(1-p)}{3-p}$$
>
> With two cars, the denominator grows from $2-p$ to $3-p$, reducing the probability of walking in the rain.

---

## 4.7 P.A.S.T.A. Property

When studying the M/G/1 queue, an issue arose: the continuous-time process counting users in the system is not Markovian because service times are not memoryless. To address this, we sampled the process at specific times (arrivals or departures). Now a new issue arises: **can we be sure that times sampled according to specific rules are representative of the long-run behavior?**

Define:

$$p_n(t) = P\{N(t) = n\}$$
$$a_n(t) = P\{N(t) = n \mid \text{an arrival occurred just after time } t\}$$

$p_n(t)$ is the probability seen by an **external observer** at time $t$. $a_n(t)$ is the probability seen by an **arriving user**. We ask: are these the same?

> [!Important] P.A.S.T.A. — Poisson Arrivals See Time Averages
> **Statement:** If arrivals are Poisson, then:
> $$\lim_{t\to\infty} p_n(t) = \lim_{t\to\infty} a_n(t)$$
> under the condition that future arrivals are independent of the current number of users $N(t)$.
>
> ![[Stochastic_Processes_2020_p158_img51.jpeg]]
> *Figure 4.16 — The number of users $N(t)$ depends on both arrivals and departures up to time $t$, conditioning on an arrival just after $t$.*
>
> **Proof:**
> $N(t)$ depends on both arrivals and departures up to time $t$. We require the arrival at $t^+$ to be independent of $N(t)$ — and hence of both arrival and departure times.
>
> - **Independence from past arrivals:** guaranteed by the Poisson property — increments are independent over disjoint time intervals.
> - **Independence from departure times:** departure times are the sum of arrival and service times, so they depend on arrival times. For independence from future arrivals, we need service times to be independent of future arrivals. This is reasonable: service-time distributions should not depend on future arrival patterns.
>
> Given the independence, the two events in the definition of $a_n(t)$ are independent:
>
> $$a_n(t) = P\{N(t)=n\}\,P\{\text{an arrival occurred just after time } t\}$$
>
> Then in the limit:
>
> $$\lim_{t\to\infty} p_n(t) = \lim_{t\to\infty} a_n(t) \qquad \blacksquare$$
>
> **Intuition:** Because Poisson arrivals are "memoryless" with respect to the system state, an arriving customer sees the system in exactly the same statistical state as a random external observer. No sampling bias is introduced.

The name **P.A.S.T.A.** stands for *Poisson Arrivals See Time Averages*. The following examples show that both conditions — Poisson arrivals and independence of service/arrival times — are necessary.

### Non-Poisson Arrivals Counter-Example

Consider interarrival times i.i.d. uniform on $[2,4]$ seconds, with service time fixed at 1 second.

![[Stochastic_Processes_2020_p159_img52.jpeg]]
*Figure 4.17 — Interarrival times uniform on $U[2,4]$s; service time fixed at 1s.*

Since the minimum interarrival time is 2s > 1s (service time), each arriving user **always** finds the system empty:

$$a_0 = P[N(t)=0 \mid \text{arrival just occurred}] = 1, \qquad a_i = 0 \quad i > 0$$

An external observer sees the system occupied for exactly 1s and empty for $U[1,3]$s (average 2s). On average: 1s busy every 3s, so:

$$p_0 = \lim_{t\to\infty} P[N(t)=0] = 2/3, \qquad p_1 = 1/3, \qquad p_i = 0 \; (i > 1)$$

Clearly $a_0 \neq p_0$, $a_1 \neq p_1$ — the PASTA property fails because arrivals are **not Poisson**.

### Arrival–Service Times Not Independent Counter-Example

Arrivals are Poisson, but the service time of the $n$-th packet equals **half** the interarrival time between packets $n$ and $n+1$.

*Figure 4.18 — Arrival and service times are correlated: service time is half the next interarrival time.*
*(Note: no image tag in source — OCR artifact.)*

Since the service time is half the *next* interarrival time, each user finishes service before the next one arrives. Every arriving customer finds the system empty:

$$a_0 = 1$$

But an external observer sees the system empty half the time and busy the other half:

$$p_0 = p_1 = 1/2$$

Again $a_0 \neq p_0$ — PASTA fails because **service times and future arrivals are correlated** (violating the independence condition), despite having Poisson arrivals.

### M/G/1 Queue — Arrivals Equal Departures

For the M/G/1 queue, analysis was performed at **departure** times. We must verify that the distribution seen by departing users $d_n$ equals $a_n$ (seen by arriving users), closing the loop.

Define:

$$a_n(t) = P[N(t)=n \mid \text{an arrival occurred just before time } t]$$
$$d_n(t) = P[N(t)=n \mid \text{a departure occurred just before time } t]$$
$$p_n(t) = P[N(t)=n]$$

> [!Important] Theorem — Departing Users See Same Distribution as Arriving Users
> **Statement:** For a stable M/G/1 queue where $N(t)$ changes by unit steps:
> $$d_n = a_n \qquad n = 0, 1, \ldots$$
>
> **Proof:**
> Two assumptions: (1) the system is stable (positive recurrent); (2) $N(t)$ changes by unit steps (unit arrivals, unit departures — valid for M/G/1 with a single server).
>
> A stable system is empty an infinite number of times (with probability 1). For any fixed level $n$:
> - Each upward transition $n \to n+1$ corresponds to an arrival finding state $n$.
> - Each downward transition $n+1 \to n$ corresponds to a departure leaving state $n$.
> - Since $N(t)$ can only change in unit steps, every upward crossing of level $n$ must be matched by a downward crossing (stability). The difference between the number of upward and downward crossings is at most 1 at any time.
>
> ![[Stochastic_Processes_2020_p162_img53.jpeg]]
> *Figure 4.19 — For a stable system, fixing a level $n$, upward and downward crossings must balance in the long run.*
>
> Consider in interval $[0,t]$:
>
> $$\frac{\#\text{ of } n\to n+1 \text{ transitions in } [0,t]}{\#\text{ of } k\to k+1 \text{ transitions in } [0,t]\; \forall k} = \text{fraction of arrivals finding state } n$$
>
> $$\frac{\#\text{ of } n+1\to n \text{ transitions in } [0,t]}{\#\text{ of } k+1\to k \text{ transitions in } [0,t]\; \forall k} = \text{fraction of departures leaving state } n$$
>
> Since the numerators differ by at most 1 (finite), and both denominators $\to \infty$ as $t \to \infty$ (stability), the fractions must converge to the same limit:
>
> $$\lim_{t\to\infty}\frac{\#(n\to n+1)}{\#(\text{all arrivals})} = \lim_{t\to\infty}\frac{\#(n+1\to n)}{\#(\text{all departures})}$$
>
> Therefore $d_n = a_n$. $\blacksquare$
>
> **Intuition:** In a stable, unit-step system, arrivals and departures must be perfectly balanced in the long run at every level. The fraction of arrivals finding state $n$ equals the fraction of departures leaving state $n$.

Consequently, the M/G/1 analysis at departure times was consistent: the departure-time distribution is unbiased and represents the true long-run behavior.

### Periodic Class Discussion

> [!Important] Periodic Class — Existence of the General Limit
> We now discuss Exercise 14 (page 125 in the original text). The transition matrix is:
>
> $$\mathbb{P} = \begin{Vmatrix} \mathbb{Q} & \mathbb{R}_1 & \mathbb{R}_2 \\ 0 & \mathbb{A} & 0 \\ 0 & 0 & \mathbb{1} \end{Vmatrix} \qquad \text{where} \qquad \mathbb{A} = \begin{Vmatrix} 0 & 1 \\ 1 & 0 \end{Vmatrix} \qquad \mathbb{A}^n = \begin{cases} \begin{Vmatrix}0&1\\1&0\end{Vmatrix} & n \text{ odd} \\ \begin{Vmatrix}1&0\\0&1\end{Vmatrix} & n \text{ even} \end{cases}$$
>
> ![[Stochastic_Processes_2020_p163_img54.jpeg]]
> *Figure 4.20 — A transient block that leads either to an absorbing block or to a periodic class.*
>
> The chain has: a recurrent periodic class $\mathbb{A}$ of period 2; a transient class $\mathbb{Q}$ connected to $\mathbb{A}$ via $\mathbb{R}_1$ and to the absorbing class via $\mathbb{R}_2$. The block $\mathbb{A}$ oscillates deterministically between its two states and never converges.
>
> We study $\mathbb{P}^n$ as $n$ increases, focusing on the $\mathbb{R}_1$ block. Computing $\mathbb{P}^2$ and $\mathbb{P}^3$:
>
> $$\mathbb{P}^2 = \begin{bmatrix} \mathbb{Q}^2 & \mathbb{Q}\mathbb{R}_1+\mathbb{R}_1\mathbb{A} & \mathbb{Q}\mathbb{R}_2+\mathbb{R}_2 \\ 0 & \mathbb{A}^2 & 0 \\ 0 & 0 & \mathbb{1} \end{bmatrix}$$
>
> $$\mathbb{P}^3 = \begin{bmatrix} \mathbb{Q}^3 & \mathbb{Q}^2\mathbb{R}_1+\mathbb{Q}\mathbb{R}_1\mathbb{A}+\mathbb{R}_1\mathbb{A}^2 & \mathbb{Q}^2\mathbb{R}_2+\mathbb{Q}\mathbb{R}_2+\mathbb{R}_2 \\ 0 & \mathbb{A}^3 & 0 \\ 0 & 0 & \mathbb{1} \end{bmatrix}$$
>
> By induction, the general pattern for $\mathbb{P}^{n+1}$ is:
>
> $$\mathbb{P}^{n+1} = \begin{bmatrix} \mathbb{Q}^{n+1} & \sum_{i=0}^n \mathbb{Q}^i\mathbb{R}_1\mathbb{A}^{n-i} & \left(\sum_{i=0}^n \mathbb{Q}^i\right)\mathbb{R}_2 \\ 0 & \mathbb{A}^{n+1} & 0 \\ 0 & 0 & \mathbb{1} \end{bmatrix}$$
>
> We ask: does $\lim_{n\to\infty}\sum_{i=0}^n \mathbb{Q}^i\mathbb{R}_1\mathbb{A}^{n-i}$ exist?
>
> **For even $n = 2k$:** Splitting the sum into even and odd indices (using $\mathbb{A}^{2j}=\mathbb{1}$ and $\mathbb{A}^{2j+1}=\mathbb{A}$):
>
> $$\sum_{i=0}^{2k}\mathbb{Q}^i\mathbb{R}_1\mathbb{A}^{2k-i} = \left(\sum_{j=0}^k\mathbb{Q}^{2j}\right)\mathbb{R}_1 + \left(\sum_{j=0}^{k-1}\mathbb{Q}^{2j}\right)\mathbb{Q}\mathbb{R}_1\mathbb{A}$$
>
> $$\xrightarrow{k\to\infty} [\mathbb{1}-\mathbb{Q}^2]^{-1}(\mathbb{R}_1 + \mathbb{Q}\mathbb{R}_1\mathbb{A})$$
>
> **For odd $n = 2k+1$:** Similarly:
>
> $$\sum_{i=0}^{2k+1}\mathbb{Q}^i\mathbb{R}_1\mathbb{A}^{2k+1-i} = \left(\sum_{j=0}^k\mathbb{Q}^{2j}\right)(\mathbb{R}_1\mathbb{A}+\mathbb{Q}\mathbb{R}_1)$$
>
> $$\xrightarrow{k\to\infty} [\mathbb{1}-\mathbb{Q}^2]^{-1}(\mathbb{R}_1\mathbb{A}+\mathbb{Q}\mathbb{R}_1)$$
>
> The two limits are equal iff:
>
> $$[\mathbb{1}-\mathbb{Q}^2]^{-1}(\mathbb{R}_1+\mathbb{Q}\mathbb{R}_1\mathbb{A}) = [\mathbb{1}-\mathbb{Q}^2]^{-1}(\mathbb{R}_1\mathbb{A}+\mathbb{Q}\mathbb{R}_1)$$
>
> Rearranging:
>
> $$\mathbb{R}_1 + \mathbb{Q}\mathbb{R}_1\mathbb{A} = \mathbb{R}_1\mathbb{A} + \mathbb{Q}\mathbb{R}_1 \implies (\mathbb{1}-\mathbb{Q})\mathbb{R}_1 = (\mathbb{1}-\mathbb{Q})\mathbb{R}_1\mathbb{A}$$
>
> Since $\mathbb{1}-\mathbb{Q}$ is invertible (as a stochastic-process matrix), this reduces to:
>
> $$\mathbb{R}_1 = \mathbb{R}_1\mathbb{A}$$
>
> Note that $\mathbb{R}_1\mathbb{A}$ is $\mathbb{R}_1$ with its columns swapped. So the general limit exists **if and only if the columns of $\mathbb{R}_1$ are identical**, i.e. when entering the periodic class from the transient state, we do so with **equal probability into each state of the periodic class** (uniform entry). This is the condition for the general limit to exist. $\blacksquare$

---

> [!Example] Exercise 4.7.2 — Shock Survival
> **Problem:** Shocks occur to a system according to a Poisson process of rate $\lambda$. The system survives each shock independently with probability $\alpha$, so its probability of surviving $k$ shocks is $\alpha^k$. What is the probability of surviving at time $t$?
>
> ![[Stochastic_Processes_2020_p166_img55.jpeg]]
> *Figure 4.21 — Each shock either destroys the system (prob $1-\alpha$) or is survived (prob $\alpha$).*
>
> **Solution — Method 1 (total probability):**
>
> $$P[\text{survive at time } t] = \sum_{k=0}^\infty P[\text{survive} \mid k\text{ shocks}]\,P[k\text{ shocks}]$$
>
> $$= \sum_{k=0}^\infty \alpha^k \frac{e^{-\lambda t}(\lambda t)^k}{k!} = e^{-\lambda t}\sum_{k=0}^\infty \frac{(\alpha\lambda t)^k}{k!} = e^{-\lambda t}e^{\lambda\alpha t} = e^{-\lambda(1-\alpha)t}$$
>
> **Solution — Method 2 (splitting):**
>
> By Theorem 4.4.2, each shock is independently "fatal" with probability $1-\alpha$. Fatal shocks form a Poisson process with rate $\lambda(1-\alpha)$. The system survives iff no fatal shock occurs before $t$:
>
> $$P[\text{survive}] = P[\text{no fatal shock in } (0,t)] = e^{-\lambda(1-\alpha)t}$$
>
> **Result:** $P[\text{survive at time } t] = e^{-\lambda(1-\alpha)t}$
>
> **Takeaway:** Splitting a Poisson process into "good" and "bad" events gives a cleaner derivation. The survival probability is exponential with effective rate $\lambda(1-\alpha)$.

> [!Example] Exercise 4.7.3 — Dispatching System
> **Problem:** Customers arrive according to a Poisson process of rate $\lambda$. They gather and are dispatched in groups at fixed times $T, 2T, 3T, \ldots$. Waiting cost: $c$ per customer per unit time. Each dispatch costs $K$.
>
> 1. Total dispatch cost in first cycle $[0,T]$?
> 2. Mean total waiting cost in first cycle?
> 3. Mean total (waiting + dispatch) cost per unit time in first cycle?
> 4. Optimal $T^*$ minimizing cost per unit time?
>
> ![[Stochastic_Processes_2020_p167_img56.jpeg]]
> *Figure 4.22 — Number of customers as a function of time in the dispatching system (sawtooth pattern).*
>
> **Solution:**
>
> **(a)** The total dispatch cost in the first cycle is simply $K$.
>
> **(b)** For each customer, the waiting cost is $c$ times their waiting duration. The total waiting cost over the cycle is:
>
> $$c\int_0^T X(t)\,dt$$
>
> where $X(t)$ is a random variable (Poisson). Taking the expectation, using $\mathbb{E}[X(t)] = \lambda t$:
>
> $$\text{average waiting cost} = c\,\mathbb{E}\left[\int_0^T X(t)\,dt\right] = c\int_0^T \mathbb{E}[X(t)]\,dt = c\int_0^T \lambda t\,dt = \frac{c\lambda T^2}{2}$$
>
> **(c)** Average total cost per unit time:
>
> $$\frac{K + c\lambda T^2/2}{T}$$
>
> **(d)** Minimize over $T$ — there is a tradeoff: increasing $T$ raises waiting cost; decreasing $T$ raises dispatch frequency. Differentiate and set to zero:
>
> $$\frac{d}{dT}\frac{K + c\lambda T^2/2}{T} = -\frac{K}{T^2} + \frac{c\lambda}{2} \stackrel{!}{=} 0$$
>
> $$\boxed{T^* = \sqrt{\frac{2K}{c\lambda}}}$$
>
> **Takeaway:** Classic square-root economic order quantity formula. Optimal dispatch period balances holding cost ($c\lambda$) and fixed dispatch cost ($K$).

> [!Example] Exercise 4.7.4 — Typographical Errors
> **Problem:** A 600-page book contains 240 typographical errors uniformly distributed. Find the Poisson approximation for the probability that three particular successive pages are error-free.
>
> **Solution:**
>
> Each error falls on a given page with probability $p = 1/600$. With $n = 240$ errors, the number of errors on a single page is approximately Poisson with rate:
>
> $$np = 240/600 = 0.4$$
>
> Three successive pages are three disjoint intervals; the total error count on three pages is Poisson with rate $3 \times 0.4 = 1.2$:
>
> $$P[\text{3 pages are error-free}] \approx e^{-1.2}$$
>
> Note: successive pages are irrelevant — only the total number of pages (the interval size) matters, not their position, as long as they are distinct.

> [!Example] Exercise 4.7.5 — Circular Disk
> **Problem:** $N$ points are uniformly distributed over a circular disk of radius $r$. Determine the probability distribution of the number of points within distance 1 of the origin as $N \to \infty$, $r \to \infty$, with $N/(\pi r^2) = \lambda$ constant.
>
> ![[Stochastic_Processes_2020_p169_img57.jpeg]]
> *Figure 4.23 — 2D Poisson processes: counts in any region depend only on its area, not shape or position.*
>
> **Solution:**
>
> Each point has probability $p = \pi R^2/(\pi r^2) = 1/r^2$ of being inside the inner circle of radius $R=1$. The count in the inner circle is Binomial$(N, 1/r^2)$.
>
> As $N \to \infty$, $r \to \infty$ with $N/(\pi r^2) = \lambda$, we have $N \cdot (1/r^2) = N/r^2 = \pi\lambda$ fixed. In the limit, the Binomial$(N, 1/r^2)$ converges to Poisson$(\pi\lambda)$:
>
> ![[Stochastic_Processes_2020_p170_img58.jpeg]]
> *Figure 4.24 — Inner circle of radius 1 inside outer circle of radius $r$.*
>
> $$P[\text{$k$ points in inner circle}] \to \frac{e^{-\pi\lambda}(\pi\lambda)^k}{k!}$$
>
> **Takeaway:** 2D Poisson processes arise naturally in the limit of uniform point clouds. The parameter $\pi\lambda$ is the expected number of points per unit area times the area of the inner circle.

> [!Example] Exercise 4.7.6 — First Time All Processes Fire
> **Problem:** For $i=1,\ldots,n$, let $\{X_i(t); t \geq 0\}$ be independent Poisson processes each with parameter $\lambda$. Find the distribution of the first time $T$ that at least one event has occurred in every process.
>
> ![[Stochastic_Processes_2020_p170_img59.jpeg]]
> *Figure 4.25 — Time $T$ is the maximum of first-arrival times across all $n$ processes.*
>
> **Solution:**
>
> Inter-arrival times for each Poisson process are exponential with parameter $\lambda$. The first event in process $i$ occurs at time $T_i \sim \text{Exp}(\lambda)$. The time for all processes to have fired at least once is:
>
> $$T = \max\{T_i,\; i=1,\ldots,n\}$$
>
> Since all processes are independent:
>
> $$P[T \leq t] = P[\text{all exponentials} \leq t] = \prod_{i=1}^n P[T_i \leq t] = (1 - e^{-\lambda t})^n$$
>
> **Takeaway:** The distribution of the maximum of $n$ i.i.d. exponentials is $(1-e^{-\lambda t})^n$, an extreme-value distribution.

> [!Example] Exercise 4.7.7 — Batch Holding Facility
> **Problem:** Customers arrive at a holding facility at rate $\lambda$. The facility dispatches in batches of size $Q$: the first $Q-1$ customers wait until the $Q$-th customer arrives, then all are dispatched. Service is instantaneous. Let $N(t)$ be the number in the facility at time $t$, $N(0)=0$, and $T = \min\{t \geq 0 : N(t)=Q\}$ the first dispatch time.
>
> Show: (1) $\mathbb{E}[T] = Q/\lambda$; (2) $\mathbb{E}\left[\int_0^T N(t)\,dt\right] = Q(Q-1)/(2\lambda)$.
>
> ![[Stochastic_Processes_2020_p171_img60.jpeg]]
> *Figure 4.26 — Customers accumulate in the facility until $Q$ have arrived.*
>
> **Solution:**
>
> **(a)** Interarrival times are i.i.d. Exp$(\lambda)$. The time $T$ to accumulate $Q$ customers is the sum of $Q$ exponentials:
>
> $$\mathbb{E}[T] = \sum_{i=1}^Q \frac{1}{\lambda} = \frac{Q}{\lambda}$$
>
> **(b)** The first user waits for $Q-1$ more arrivals; the second waits for $Q-2$; ...; the $Q$-th waits for 0. The total waiting time is the sum of $Q-1$ rectangles of heights $1, 2, \ldots, Q-1$, each with a base of average $1/\lambda$:
>
> $$\mathbb{E}\left[\int_0^T N(t)\,dt\right] = \frac{1+2+\cdots+(Q-1)}{\lambda} = \frac{Q(Q-1)}{2\lambda}$$
>
> **Takeaway:** These results confirm Little's Law in the batch dispatch setting. The mean waiting time per customer is $(Q-1)/(2\lambda)$.

> [!Example] Exercise 4.7.8 — Mean of First Arrival Time Given $n$ Arrivals
> **Problem:** Let $\{X(t); t \geq 0\}$ be a Poisson process of rate $\lambda$. Given $X(1) = n$, find $\mathbb{E}[W_1]$ for $n = 1, 2, \ldots$
>
> **Solution:**
>
> By Theorem 4.5.3, given $X(1)=n$, the $n$ arrival times are i.i.d. uniform on $(0,1)$. Therefore $W_1$, the first arrival time, has the same statistics as the **minimum** of $n$ i.i.d. uniform$[0,1]$ variables:
>
> $$W_1 = \min(U_i,\; i=1,\ldots,n)$$
>
> The tail of the minimum:
>
> $$P[W_1 > a] = P[\text{all } U_i > a] = (P[U > a])^n = (1-a)^n \qquad a \in [0,1]$$
>
> The expected value via the tail distribution:
>
> $$\mathbb{E}[W_1 \mid n \text{ arrivals in } [0,1]] = \int_0^1 P[W_1 > a]\,da = \int_0^1 (1-a)^n\,da = \frac{1}{n+1}$$
>
> **Takeaway:** Given $n$ arrivals, the expected first arrival time is $1/(n+1)$ — uniformly spaced quantiles.

> [!Example] Exercise 4.7.9 — Mean Total Waiting Time for 5 Customers
> **Problem:** Customers arrive according to a Poisson process of rate $\lambda$. Given that 5 customers arrived in the first hour, find $\mathbb{E}[W_1+W_2+W_3+W_4+W_5]$.
>
> **Solution:**
>
> By Theorem 4.5.3, given 5 arrivals in $[0,1]$h, each $W_i$ is i.i.d. uniform on $[0,1]$. Each has mean $1/2$h. Therefore:
>
> $$\mathbb{E}[W_1+W_2+W_3+W_4+W_5] = 5 \times \frac{1}{2} = \frac{5}{2}\text{ h} = \text{2h 30min}$$

> [!Example] Exercise 4.7.10 — Store Empty at End of Hour
> **Problem:** Customers arrive according to a Poisson process of rate $\lambda$. Given 5 customers arrived in the first hour, each spends time in the store exponentially distributed with parameter $\alpha$ (independent). What is the probability the store is empty at the end of the first hour?
>
> **Solution:**
>
> Given 5 arrivals in $[0,1]$h, arrival times are i.i.d. uniform on $[0,1]$. A user arriving at time $W$ (replaced by $U \sim \text{Uniform}[0,1]$) with service time $Y \sim \text{Exp}(\alpha)$ is still in the store at $t=1$ iff $U + Y > 1$, i.e. $Y > 1-U$:
>
> $$p = P[\text{user still in store}] = P[U+Y>1] = \int_0^1 P[Y > 1-u]\,du = \int_0^1 e^{-\alpha(1-u)}\,du = \frac{1-e^{-\alpha}}{\alpha}$$
>
> Since all users are independent, the probability that **all 5** have departed is $(1-p)^5$:
>
> $$P[\text{system empty} \mid 5\text{ arrivals in }[0,1]] = \left(1 - \frac{1-e^{-\alpha}}{\alpha}\right)^5$$
>
> **Takeaway:** This is the M/G/∞ queue result applied to a fixed sample. The key step is replacing arrival times with i.i.d. uniforms via Theorem 4.5.3.

---

## Summary Table

| Concept | Definition / Formula | Conditions / Notes |
|---------|----------------------|--------------------|
| **Poisson distribution** | $P[X=k] = e^{-\mu}\mu^k/k!$ | $\mu > 0$, $k = 0,1,2,\ldots$; $\mathbb{E}[X]=\operatorname{Var}[X]=\mu$ |
| **Sum of Poisson** | $X+Y \sim \text{Poisson}(\mu+\nu)$ | Requires $X\perp Y$ (Thm 4.1.1) |
| **Binomial filter** | $M \sim \text{Poisson}(\mu p)$ | $N \sim \text{Poisson}(\mu)$, $M \mid N \sim \text{Binomial}(N,p)$ (Thm 4.1.2) |
| **Poisson process** | $\mathbb{P}[X(s+t)-X(s)=k] = e^{-\lambda t}(\lambda t)^k/k!$ | Independent stationary increments; $X(0)=0$ |
| **Mean & variance** | $\mathbb{E}[X(t)] = \operatorname{Var}[X(t)] = \lambda t$ | For any $t \geq 0$ |
| **Law of Rare Events** | $S_n \approx \text{Poisson}(\sum p_i)$ | Bound: $\|\cdot\| \leq \sum p_i^2$; exact in limit $p_i \to 0$ |
| **Superposition** | $X_1+X_2 \sim \text{Poisson}(\lambda_1+\lambda_2)$ | Requires $X_1 \perp X_2$ (Thm 4.4.1) |
| **Thinning** | Type-1 events $\sim \text{Poisson}(\lambda p)$, type-2 $\sim \text{Poisson}(\lambda(1-p))$, independent | Independent Bernoulli marking (Thm 4.4.2) |
| **Inter-arrival times** | $S_i \stackrel{\text{i.i.d.}}{\sim} \text{Exp}(\lambda)$ | (Thm 4.5.1) |
| **Waiting times** | $W_n \sim \text{Gamma}(n, \lambda)$; $f_{W_n}(t) = \lambda^n t^{n-1} e^{-\lambda t}/(n-1)!$ | (Thm 4.5.2) |
| **Conditional arrivals** | $f_{W_1,\ldots,W_n \mid X(t)=n} = n!\,t^{-n}$ for $0<w_1<\cdots<w_n\leq t$ | Ordered uniforms on $(0,t)$ (Thm 4.5.3) |
| **Binomial theorem** | $P[X(u)=k \mid X(t)=n] = \binom{n}{k}(u/t)^k(1-u/t)^{n-k}$ | $0<u<t$, $0\leq k\leq n$ (Thm 4.5.4, 4.6.1) |
| **Two-process conditional** | $P[X_1(t)=k \mid X_1+X_2=n] = \binom{n}{k}p_1^k p_2^{n-k}$ | $p_i = \lambda_i/(\lambda_1+\lambda_2)$ (Thm 4.5.5) |
| **M/G/∞ queue** | $M(t) \sim \text{Poisson}(\lambda pt)$; $\lambda p = \lambda\int_0^t[1-G(z)]dz$ | Steady-state mean $\to \lambda/\mu$ as $t \to \infty$ |
| **Shot noise mean** | $\mathbb{E}[I(t)] = \lambda\int_0^t h(u)\,du$ | Poisson arrivals, impulse response $h$ |
| **Shot noise variance** | $\operatorname{Var}(I(t)) = \lambda\int_0^t h^2(u)\,du$ | Long-run: depends only on area under $h$ |
| **PASTA** | $\lim_{t\to\infty} p_n(t) = \lim_{t\to\infty} a_n(t)$ | Requires: Poisson arrivals + service $\perp$ future arrivals |
| **PASTA for departures** | $d_n = a_n$ | Requires: stable system + unit-step changes |
| **Optimal dispatch** | $T^* = \sqrt{2K/(c\lambda)}$ | Minimizes $(K + c\lambda T^2/2)/T$ |
| **Periodic class limit** | General limit of $\mathbb{P}^n$ exists | Iff columns of $\mathbb{R}_1$ are identical (uniform entry into periodic class) |
