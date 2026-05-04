# Chapter 4 — Poisson Processes

## Table of Contents

- [[#The Poisson Distribution|The Poisson Distribution]]
  - [[#Theorem 4.1.1 — Sum of Poisson Variables|Theorem 4.1.1 — Sum of Poisson Variables]]
  - [[#Theorem 4.1.2 — Poisson Composed with Binomial|Theorem 4.1.2 — Poisson Composed with Binomial]]
- [[#The Poisson Process|The Poisson Process]]
  - [[#Definition 1 — Poisson Process|Definition 1 — Poisson Process]]
  - [[#Examples|Examples]]
  - [[#Non-Homogeneous Poisson Process|Non-Homogeneous Poisson Process]]
- [[#The Law of Rare Events|The Law of Rare Events]]
- [[#Properties of Poisson Processes|Properties of Poisson Processes]]
  - [[#Theorem 4.4.1 — Superposition|Theorem 4.4.1 — Superposition]]
  - [[#Theorem 4.4.2 — Splitting (Thinning)|Theorem 4.4.2 — Splitting (Thinning)]]
- [[#Other Distributions from a Poisson Process|Other Distributions from a Poisson Process]]
  - [[#Theorem 4.5.1 — Inter-Arrival Times|Theorem 4.5.1 — Inter-Arrival Times]]
  - [[#Theorem 4.5.2 — Waiting Time Distribution|Theorem 4.5.2 — Waiting Time Distribution]]
  - [[#Ordered Uniform Points|Ordered Uniform Points]]
  - [[#Theorem 4.5.3 — Conditional Arrival Times|Theorem 4.5.3 — Conditional Arrival Times]]
  - [[#Theorem 4.5.4 — Conditional Count is Binomial|Theorem 4.5.4 — Conditional Count is Binomial]]
  - [[#Theorem 4.5.5 — Competition Theorem|Theorem 4.5.5 — Competition Theorem]]
  - [[#Corollary 4.5.6 — Competition with Sub-Interval|Corollary 4.5.6 — Competition with Sub-Interval]]
  - [[#M/G/∞ Queue|M/G/∞ Queue]]
  - [[#Shot Noise Process|Shot Noise Process]]
- [[#Binomial Theorem and Dual Version|Binomial Theorem and Dual Version]]
  - [[#Theorem 4.6.1 — Binomial Theorem (Direct Proof)|Theorem 4.6.1 — Binomial Theorem (Direct Proof)]]
  - [[#Dual Version|Dual Version]]
  - [[#Exercises|Exercises]]
- [[#P.A.S.T.A. Property|P.A.S.T.A. Property]]
  - [[#PASTA Theorem|PASTA Theorem]]
  - [[#Counter-Examples|Counter-Examples]]
  - [[#Departures See Same Distribution as Arrivals|Departures See Same Distribution as Arrivals]]
  - [[#Periodic Class — Limit Existence Condition|Periodic Class — Limit Existence Condition]]
- [[#Summary Table|Summary Table]]

---

## The Poisson Distribution

> [!Important] Definition — Poisson Distribution
> The **Poisson distribution** with parameter $\mu>0$:
> $$p_k \equiv \mathbb{P}[X=k] = \frac{e^{-\mu}\mu^k}{k!} \qquad k=0,1,2,\ldots \tag{4.1}$$
>
> Mean and variance: $\mathbb{E}[X]=\mu$, $\operatorname{Var}[X]=\mu$.

### Theorem 4.1.1 — Sum of Poisson Variables

> [!Important] Theorem 4.1.1 — Sum of Independent Poisson Variables
> **Statement:** Let $X\sim\mathrm{Poisson}(\mu)$ and $Y\sim\mathrm{Poisson}(\nu)$ be independent. Then $X+Y\sim\mathrm{Poisson}(\mu+\nu)$.
>
> **Proof:**
> By the law of total probability (events $\{X=k, Y=n-k\}$ are mutually exclusive):
> $$\mathbb{P}[X+Y=n] = \sum_{k=0}^n\mathbb{P}[X=k]\mathbb{P}[Y=n-k]$$
> Substituting (4.1) and factoring $e^{-(\mu+\nu)}$:
> $$= \sum_{k=0}^n\frac{\mu^k e^{-\mu}}{k!}\frac{\nu^{n-k}e^{-\nu}}{(n-k)!} = \frac{e^{-(\mu+\nu)}}{n!}\underbrace{\sum_{k=0}^n\binom{n}{k}\mu^k\nu^{n-k}}_{(\mu+\nu)^n}$$
> Therefore:
> $$\mathbb{P}[X+Y=n] = \frac{e^{-(\mu+\nu)}(\mu+\nu)^n}{n!} \tag{4.2}$$
> which is $\mathrm{Poisson}(\mu+\nu)$. $\square$
>
> **Intuition:** The binomial sum $\sum_k\binom{n}{k}\mu^k\nu^{n-k}=(\mu+\nu)^n$ collapses the double sum into a single Poisson. The two sources combine with additive rates.

### Theorem 4.1.2 — Poisson Composed with Binomial

> [!Important] Theorem 4.1.2 — Poisson Filtered by Binomial
> **Statement:** Let $N\sim\mathrm{Poisson}(\mu)$. Conditional on $N$, let $M\sim\mathrm{Binomial}(N,p)$. Then the unconditional distribution of $M$ is $\mathrm{Poisson}(\mu p)$.
>
> **Proof:** Referred to Exercise 1.6.1 (Chapter 1).
>
> **Intuition:** Picking $N\sim\mathrm{Poisson}(\mu)$ objects and keeping each with probability $p$ yields $\mathrm{Poisson}(\mu p)$ objects. A binomial filter reduces the effective rate without changing the distributional form.

---

## The Poisson Process

### Definition 1 — Poisson Process

> [!Important] Definition 1 — Poisson Process
> A **Poisson process** of rate $\lambda>0$ is an integer-valued stochastic process $\{X(t):t\geq 0\}$ satisfying:
>
> 1. **Independent and stationary increments:** For any $0=t_0<t_1<\cdots<t_n$, the increments $X(t_1)-X(t_0),\,X(t_2)-X(t_1),\ldots,X(t_n)-X(t_{n-1})$ are independent and each depends only on the length of the corresponding interval (not on the absolute time).
>
> 2. **Poisson-distributed increments:** For $s\geq 0$, $t>0$:
> $$\mathbb{P}[X(s+t)-X(s)=k] = \frac{(\lambda t)^k e^{-\lambda t}}{k!} \qquad k=0,1,2,\ldots$$
>
> 3. **Zero initial count:** $X(0)=0$.
>
> Consequently: $\mathbb{E}[X(t)]=\lambda t$ and $\operatorname{Var}[X(t)]=\lambda t$.
>
> **Intuition:** $\lambda$ is the constant rate of arrivals. Stationarity means the process is in its stationary state — no dependence on absolute time, only on interval length. Independent increments: what happened before has no effect on future counts.

### Examples

> [!Example] Example — Defects on Undersea Cable
> **Problem:** Defects along a cable follow a Poisson process with rate $\lambda=0.1$ per mile.
>
> *(a)* $\mathbb{P}[X(2)=0]$ = ?
>
> *(b)* $\mathbb{P}[X(3)-X(2)=0 \mid X(2)=0]$ = ?
>
> **Solution:**
>
> *(a)* $X(2)\sim\mathrm{Poisson}(0.2)$:
> $$\mathbb{P}[X(2)=0]=e^{-0.2}=0.8187$$
>
> *(b)* By **independent increments**, $X(3)-X(2)$ is independent of $X(2)$:
> $$\mathbb{P}[X(3)-X(2)=0]=\mathbb{P}[X(1)=0]=e^{-0.1}=0.9048$$
>
> **Takeaway:** Independent increments → conditioning on non-overlapping intervals is irrelevant.

> [!Example] Example — Customer Arrivals
> **Problem:** Customers arrive at rate $\lambda=4$/hour (time unit = 1 hour from 9:00 AM).
>
> Find $\mathbb{P}[X(1/2)=1,\,X(5/2)=5]$.
>
> **Solution:** Rewrite using independent increments:
> $$\mathbb{P}[X(1/2)=1,\,X(5/2)-X(1/2)=4]$$
> $$= \frac{e^{-4(1/2)}[4(1/2)]^1}{1!}\cdot\frac{e^{-4(2)}[4(2)]^4}{4!} = (2e^{-2})\left(\frac{512}{3}e^{-8}\right) = 0.0155$$
>
> **Takeaway:** Use independence + stationarity to factor joint probabilities into products of Poisson probabilities.

### Non-Homogeneous Poisson Process

A **non-homogeneous Poisson process** relaxes stationarity by allowing $\lambda=\lambda(t)$ (time-varying rate). The probability of a single event in an infinitesimal interval $h$:

$$\mathbb{P}[X(t+h)-X(t)=1] = \lambda(t)\,h + o(h)$$

The distribution of counts in $(s, s+t]$:

$$\mathbb{P}[X(t+s)-X(s)=k] = \frac{1}{k}\int_s^{t+s}(\lambda(t)t)^k e^{-\lambda(t)t}$$

*(Note: the source formula above is reproduced as-is — the factor $1/k$ may be a transcription artifact; the standard formula integrates $\lambda(u)$ over the interval.)*

---

## The Law of Rare Events

The Poisson distribution is the **discrete analog of the Normal**: just as the Normal arises as the limit of sums of many continuous r.v.s (CLT), the Poisson arises as the limit of sums of many rare discrete events.

**Fixed probability case:** $N$ independent Bernoulli trials with fixed probability $p\ll 1$, total successes $X_{N,p}\sim\mathrm{Binomial}(N,p)$. In the limit $p\to 0$, $N\to\infty$, $Np\equiv\mu$:

$$\mathbb{P}[X_{N,p}=k] \to \frac{e^{-\mu}\mu^k}{k!}$$

> [!Important] Theorem — Law of Rare Events (General)
> **Statement:** Let $\epsilon_1,\epsilon_2,\ldots$ be independent Bernoulli r.v.s with $\mathbb{P}[\epsilon_i=1]=p_i$, $S_n=\epsilon_1+\cdots+\epsilon_n$, $\mu=p_1+\cdots+p_n$. Then:
> $$\left|\mathbb{P}[S_n=k]-\frac{\mu^k e^{-\mu}}{k!}\right|\leq\sum_{i=1}^n p_i^2 \tag{4.4}$$
>
> **Corollary:** If all $p_i\equiv p$ and $Np=\mu$ is fixed, then as $N\to\infty$, $p\to 0$ and the RHS $\to 0$: $S_n$ converges in distribution to $\mathrm{Poisson}(\mu)$.
>
> **Intuition:** Even with heterogeneous $p_i$, the bound $\sum p_i^2$ vanishes when individual $p_i$ are small (hence "rare"). The Poisson is universal for counts of rare events.

**Applied to processes:** The combination of many independent processes (not necessarily Poisson) generating events at random times converges in the limit $M\to\infty$ to a single Poisson process. This makes the Poisson model universally applicable even when individual underlying processes are not Poisson.

---

## Properties of Poisson Processes

### Theorem 4.4.1 — Superposition

> [!Important] Theorem 4.4.1 — Superposition of Poisson Processes
> **Statement:** Let $X_1(t)$ and $X_2(t)$ be independent Poisson processes with rates $\lambda_1$, $\lambda_2$. Then $X(t)=X_1(t)+X_2(t)$ is a Poisson process with rate $\lambda=\lambda_1+\lambda_2$.
>
> ![[Stochastic_Processes_2020_p131_img34.jpeg]]
> *Figure 4.1 — Two independent Poisson processes combined into a single Poisson process with rate $\lambda_1+\lambda_2$.*
>
> **Proof:** Verify the three requirements of Definition 1:
>
> 1. $X(0)=X_1(0)+X_2(0)=0$. ✓
> 2. Since $X_1$, $X_2$ each have stationary and independent increments, so does $X=X_1+X_2$. ✓
> 3. $X_1(t)\sim\mathrm{Poisson}(\lambda_1 t)$ and $X_2(t)\sim\mathrm{Poisson}(\lambda_2 t)$ independently → by Theorem 4.1.1, $X(t)\sim\mathrm{Poisson}((\lambda_1+\lambda_2)t)$. ✓ $\square$

### Theorem 4.4.2 — Splitting (Thinning)

> [!Important] Theorem 4.4.2 — Splitting of a Poisson Process
> **Statement:** Let $X(t)$ be a Poisson process with rate $\lambda$. Each event is independently marked type 1 (probability $p$) or type 2 (probability $1-p$). Then the type-1 events form a Poisson process with rate $\lambda p$, the type-2 events form an independent Poisson process with rate $\lambda(1-p)$.
>
> ![[Stochastic_Processes_2020_p132_img35.jpeg]]
> *Figure 4.2 — A Poisson process split into two independent Poisson sub-processes.*
>
> **Proof:** Verify the three requirements:
>
> 1. $X_1(0)=X_2(0)=0$. ✓
> 2. $X_1$, $X_2$ inherit stationary and independent increments from $X$ (marking is independent). ✓
> 3. Joint distribution at time $t$ (noting $X_2(t)=X(t)-n$ if $X_1(t)=n$):
> $$\mathbb{P}[X_1(t)=n,\,X_2(t)=m] = \mathbb{P}[X_1(t)=n\mid X(t)=n+m]\,\mathbb{P}[X(t)=n+m]$$
> The conditional factor is $\mathrm{Binomial}(n+m,p)$:
> $$= \binom{n+m}{n}p^n(1-p)^m\cdot\frac{e^{-\lambda t}(\lambda t)^{n+m}}{(n+m)!}$$
> $$= \frac{(\lambda pt)^n e^{-\lambda pt}}{n!}\cdot\frac{(\lambda(1-p)t)^m e^{-\lambda(1-p)t}}{m!}$$
> This is the product of two independent Poisson distributions: $X_1(t)\sim\mathrm{Poisson}(\lambda pt)$ and $X_2(t)\sim\mathrm{Poisson}(\lambda(1-p)t)$, independent. ✓
>
> **Independence of increments over arbitrary intervals** — three cases (fig 4.3):
>
> - **Partial overlap** $[t_1,t_3]\cap[t_2,t_4]=[t_2,t_3]$: split into non-overlapping $[t_1,t_2]$, overlap $[t_2,t_3]$, and $[t_3,t_4]$. On the overlap, $X_1$ and $X_2$ increments are independent (proved above). On disjoint parts, increments of the same Poisson process are independent by definition. Sums of pairwise independent r.v.s are independent. ✓
> - **One contained in the other** $t_1<t_2<t_4<t_3$: split into $[t_1,t_2]$, $[t_2,t_4]$, $[t_4,t_3]$; same argument. ✓
> - **Disjoint intervals**: trivial. ✓ $\square$
>
> ![[Stochastic_Processes_2020_p133_img36.jpeg]]
> *(a) — Partial overlap $[t_2,t_3]$.*
>
> ![[Stochastic_Processes_2020_p133_img37.jpeg]]
> *(b) — One interval contained in the other.*
>
> ![[Stochastic_Processes_2020_p133_img38.jpeg]]
> *(c) — Disjoint intervals.*
>
> *Figure 4.3 — All possible overlaps of two intervals $[t_1,t_3]$ and $[t_2,t_4]$.*

---

## Other Distributions from a Poisson Process

Let $W_i$ denote the **arrival times** (times of the $i$-th event). Define the **inter-arrival times** (sojourn times):

$$S_i \equiv W_{i+1}-W_i \qquad\text{so that}\qquad W_i = \sum_{k=0}^{i-1}S_k$$

![[Stochastic_Processes_2020_p134_img39.jpeg]]
*Figure 4.4 — Typical sample path of a Poisson process: arrival times $W_i$ and sojourn times $S_i$.*

### Theorem 4.5.1 — Inter-Arrival Times

> [!Important] Theorem 4.5.1 — Inter-Arrival Times are i.i.d. Exponential
> **Statement:** The inter-arrival times $S_i$ are i.i.d. $\mathrm{Exp}(\lambda)$ random variables.
>
> **Proof:** Referred to Theorem 2.2.1 (Chapter 2, page 33).
>
> **Intuition:** Memorylessness of the Poisson process → each waiting period starts fresh → exponential sojourn times.

### Theorem 4.5.2 — Waiting Time Distribution

> [!Important] Theorem 4.5.2 — Waiting Time $W_n\sim\mathrm{Gamma}(n,\lambda)$
> **Statement:** The waiting time for the $n$-th event has the Gamma distribution:
> $$f_{W_n}(t) = \frac{\lambda^n t^{n-1}}{(n-1)!}e^{-\lambda t} \qquad n=1,2,\ldots,\quad t\geq 0$$
>
> **Proof:** $W_n=\sum_{i=0}^{n-1}S_i$ is the sum of $n$ i.i.d. $\mathrm{Exp}(\lambda)$ r.v.s, which by definition is a $\mathrm{Gamma}(n,\lambda)$ distribution. $\square$

### Ordered Uniform Points

Suppose $n$ points $U_i$ are chosen independently and uniformly in $(0,t)$. Their joint pdf is:

$$f_{U_1,\ldots,U_n}(w_1,\ldots,w_n) = t^{-n} \qquad\text{for all }(w_1,\ldots,w_n)\in(0,t)^n$$

Let $\{W_i\}$ be the **ordered** version $0\leq W_1<W_2<\cdots<W_n\leq t$. The $W_i$ are not independent (ordering constraint). For $n=2$:

$$f_{W_1,W_2}(w_1,w_2) = 2t^{-2}$$

The factor 2 counts the two permutations of $\{U_1,U_2\}$. Generalizing to $n$ points: $n!$ permutations yield:

$$f_{W_1,\ldots,W_n}(w_1,\ldots,w_n) = n!\,t^{-n} \qquad\text{for }0<w_1<\cdots<w_n\leq t$$

![[Stochastic_Processes_2020_p135_img40.jpeg]]
*Figure 4.5 — $n$ uniform points $U_i$ in $(0,t)$ and their ordered version $W_i$.*

![[Stochastic_Processes_2020_p135_img41.jpeg]]
*Figure 4.6 — Two points and their small intervals $[w_i,w_i+\Delta w_i]$. Each permutation of $\{U_1,U_2\}$ contributes equally.*

### Theorem 4.5.3 — Conditional Arrival Times

> [!Important] Theorem 4.5.3 — Given $X(t)=n$, Arrival Times are Ordered Uniform
> **Statement:** Let $W_1,W_2,\ldots$ be ordered arrival times of a Poisson process with rate $\lambda$. Conditioned on $X(t)=n$:
> $$f_{W_1,\ldots,W_n\mid X(t)=n}(w_1,\ldots,w_n) = n!\,t^{-n} \qquad 0<w_1<\cdots<w_n\leq t$$
> i.e., the $n$ arrival times are distributed as the order statistics of $n$ i.i.d. $\mathrm{Uniform}(0,t)$ r.v.s.
>
> **Proof:**
> Assume all $w_i$ are distinct (simultaneous arrivals have probability zero in a Poisson process). Choose disjoint intervals $[w_i,w_i+\Delta w_i]$. Compute the probability that exactly one arrival falls in each interval $[w_i,w_i+\Delta w_i]$ and zero arrivals fall everywhere else in $[0,t]$, given $X(t)=n$:
>
> $$\mathbb{P}[w_i\leq W_i\leq w_i+\Delta w_i,\,i=1,\ldots,n\mid X(t)=n]$$
>
> Numerator (disjoint intervals → independent Poisson increments):
> $$\prod_{i=1}^n\lambda\Delta w_i e^{-\lambda\Delta w_i}\cdot e^{-\lambda(t-\sum_i\Delta w_i)}$$
>
> Denominator (probability of $n$ events in $[0,t]$):
> $$\frac{e^{-\lambda t}(\lambda t)^n}{n!}$$
>
> The exponentials $e^{-\lambda\Delta w_1}\cdots e^{-\lambda\Delta w_n}\cdot e^{-\lambda(t-\sum\Delta w_i)}=e^{-\lambda t}$ cancel with the denominator's $e^{-\lambda t}$, and $\lambda^n$ cancels. The ratio equals:
> $$n!\,t^{-n}\,\Delta w_1\cdots\Delta w_n$$
>
> ![[Stochastic_Processes_2020_p137_img42.jpeg]]
> *Figure 4.7 — Each interval $[w_i,w_i+\Delta w_i]$ must contain exactly one arrival; disjoint intervals are independent.*
>
> Dividing by $\prod\Delta w_i$ and taking $\Delta w_i\to 0$:
> $$f_{W_1,\ldots,W_n\mid X(t)=n}(w_1,\ldots,w_n) = n!\,t^{-n} \qquad\square$$
>
> **Intuition:** Given their count, arrivals have no memory of the Poisson rate — they are just $n$ points scattered uniformly at random in $[0,t]$.

### Theorem 4.5.4 — Conditional Count is Binomial

> [!Important] Theorem 4.5.4 — $X(u)\mid X(t)=n \sim \mathrm{Binomial}(n,u/t)$
> **Statement:** For a Poisson process with rate $\lambda$, given $X(t)=n$, the number of arrivals in $(0,u)$ with $0<u<t$ satisfies:
> $$\mathbb{P}[X(u)=k\mid X(t)=n] = \binom{n}{k}\left(\frac{u}{t}\right)^k\left(1-\frac{u}{t}\right)^{n-k} \qquad 0\leq k\leq n$$
>
> ![[Stochastic_Processes_2020_p138_img43.jpeg]]
> *Figure 4.8 — Given $n$ events uniform in $(0,t)$, each falls in $(0,u)$ with probability $p=u/t$, so $X(u)\sim\mathrm{Binomial}(n,u/t)$.*
>
> **Proof:** By Theorem 4.5.3, given $X(t)=n$, each of the $n$ arrival times is i.i.d. $\mathrm{Uniform}(0,t)$. Each independently falls in $[0,u]$ with probability $u/t$. Hence $X(u)\mid X(t)=n \sim\mathrm{Binomial}(n,u/t)$. $\square$

### Theorem 4.5.5 — Competition Theorem

> [!Important] Theorem 4.5.5 — Competition Between Two Poisson Processes
> **Statement:** Let $X_1(t)$, $X_2(t)$ be independent Poisson processes with rates $\lambda_1$, $\lambda_2$. Given $X_1(t)+X_2(t)=n$:
> $$\mathbb{P}[X_1(t)=k\mid X_1(t)+X_2(t)=n] = \binom{n}{k}\left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^k\left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k} \tag{4.12}$$
>
> **Proof:** Apply the definition of conditional probability:
> $$= \frac{\mathbb{P}[X_1(t)=k]\mathbb{P}[X_2(t)=n-k]}{\mathbb{P}[X_1(t)+X_2(t)=n]}$$
> $$= \frac{e^{-\lambda_1 t}(\lambda_1 t)^k}{k!}\cdot\frac{e^{-\lambda_2 t}(\lambda_2 t)^{n-k}}{(n-k)!}\cdot\frac{n!}{e^{-(\lambda_1+\lambda_2)t}[(\lambda_1+\lambda_2)t]^n}$$
> $$= \binom{n}{k}\left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^k\left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k} \qquad\square$$
>
> **Intuition:** Each of the $n$ total arrivals independently belongs to process 1 with probability $p_1=\lambda_1/(\lambda_1+\lambda_2)$. If $\lambda_1=\lambda_2$, $p_1=1/2$.

### Corollary 4.5.6 — Competition with Sub-Interval

> [!Important] Corollary 4.5.6 — Combined Competition and Sub-Interval
> **Statement:** Let $X_1(t)$, $X_2(t)$ be independent Poisson processes in $(0,t)$ with rates $\lambda_1$, $\lambda_2$. For $0<s<t$, given $X_1(t)+X_2(t)=n$:
> $$\mathbb{P}[X_1(s)=k\mid X_1(t)+X_2(t)=n]=\frac{n!}{k!(n-k)!}\left(\frac{\lambda_1 s}{(\lambda_1+\lambda_2)t}\right)^k\left(\frac{\lambda_1(t-s)+\lambda_2 t}{(\lambda_1+\lambda_2)t}\right)^{n-k}$$
>
> **Proof:**
> $$\mathbb{P}[X_1(s)=k\mid X_1(t)+X_2(t)=n] = \frac{\mathbb{P}[X_1(s)=k,\,X_1(t)+X_2(t)=n]}{\mathbb{P}[X_1(t)+X_2(t)=n]}$$
> The event $\{X_1(t)+X_2(t)=n,\,X_1(s)=k\}$ is equivalent to $\{X_1(s)=k,\,X_1(t)-X_1(s)+X_2(t)=n-k\}$. All three r.v.s are independent (disjoint or independent processes). Factorizing and simplifying gives the stated formula. $\square$
>
> **Geometric interpretation:** The probability is proportional to the ratio of areas in a rectangle where one axis is the rate and the other is the time interval. The term $\lambda_1 s/[(\lambda_1+\lambda_2)t]$ is the ratio of the small area (process 1 in $(0,s)$) to the total area.

![[Stochastic_Processes_2020_p140_img44.jpeg]]

![[Stochastic_Processes_2020_p140_img45.jpeg]]
*Figure 4.9 — Geometric interpretation: the conditional probability is the ratio of the small rectangle (process 1 in $(0,s)$) to the total rectangle (both processes in $(0,t)$).*

---

### M/G/∞ Queue

**Setting:** Alpha particles appear according to a Poisson process of rate $\lambda$. Each particle $k$ lives for a random duration $Y_k$ with CDF $G(y)=\Pr\{Y_k\leq y\}$, independent of all others. $M(t)$ = number of particles alive at time $t$; $X(t)$ = total particles created up to $t$; $M(0)=0$.

![[Stochastic_Processes_2020_p141_img46.jpeg]]
*Figure 4.10 — Particle $k$, created at $W_k\leq t$, still exists at time $t$ iff $W_k+Y_k\geq t$.*

Particle $k$ exists at time $t$ iff $W_k+Y_k\geq t$, indicated by $\mathbf{1}\{W_k+Y_k\geq t\}$.

**Conditional distribution** given $X(t)=n$: Since $\{W_k+Y_k\geq t\}$ is symmetric in the $W_k$'s, Theorem 4.5.3 allows replacing $W_k$ with i.i.d. $U_k\sim\mathrm{Uniform}(0,t)$:

$$\Pr\{M(t)=m\mid X(t)=n\} = \Pr\left\{\sum_{k=1}^n\mathbf{1}\{U_k+Y_k\geq t\}=m\right\} = \binom{n}{m}p^m(1-p)^{n-m}$$

where $p=\Pr\{U_k+Y_k\geq t\}$:

$$p = \frac{1}{t}\int_0^t(1-G(t-u))\,du = \frac{1}{t}\int_0^t[1-G(z)]\,dz$$

**Unconditional distribution** — marginalize over $X(t)\sim\mathrm{Poisson}(\lambda t)$ (binomial $\times$ Poisson = Poisson by Theorem 4.1.2):

$$\Pr\{M(t)=m\} = \frac{e^{-\lambda pt}(\lambda pt)^m}{m!} \qquad m=0,1,\ldots \tag{4.14}$$

so $M(t)\sim\mathrm{Poisson}(\lambda pt)$ with mean:

$$\lambda pt = \lambda\int_0^t[1-G(y)]\,dy$$

**Long-run behaviour** ($t\to\infty$): The integral converges to the mean service time $1/\mu=\mathbb{E}[Y]$, so:

$$\lim_{t\to\infty}\lambda pt = \lambda\int_0^\infty[1-G(y)]\,dy = \frac{\lambda}{\mu}$$

The asymptotic mean depends only on $\mathbb{E}[Y]$, not on the shape of $G$.

---

### Shot Noise Process

**Setting:** Electrons arrive at an anode according to a Poisson process $\{X(t)\}$ with rate $\lambda$. Each electron arriving at time $W_k$ produces a current pulse with impulse response $h(x)$. The total current at time $t$:

$$I(t) = \sum_{k=1}^{X(t)}h(t-W_k)$$

![[Stochastic_Processes_2020_p144_img47.jpeg]]
*Figure 4.11 — Pulses $h(t-W_k)$ superimposed: $I(t)=\sum_{k=1}^{X(t)}h(t-W_k)$.*

By Theorem 4.5.3 (symmetry of the sum), replacing $W_k$ with $U_k\sim\mathrm{Uniform}(0,t)$:

$$\Pr\{I(t)\leq x\} = \Pr\left\{\sum_{k=1}^{X(t)}h(U_k)\leq x\right\}$$

The sum has a **random number of i.i.d. terms** (compound Poisson). Using the formulas for mean and variance of a random sum:

$$\mathbb{E}[I(t)] = \mathbb{E}[X(t)]\,\mathbb{E}[h(U_k)] = \lambda t\cdot\frac{1}{t}\int_0^t h(u)\,du = \lambda\int_0^t h(u)\,du$$

$$\operatorname{Var}(I(t)) = \lambda t\left(\operatorname{Var}(h(U_k))+\mathbb{E}[h(U_k)]^2\right) = \lambda t\,\mathbb{E}[(h(U_k))^2] = \lambda\int_0^t h^2(u)\,du$$

*(Used $\operatorname{Var}(X)=\mathbb{E}[X^2]-\mathbb{E}[X]^2$ inverted: $\mathbb{E}[X^2]=\operatorname{Var}(X)+\mathbb{E}[X]^2$.)*

**Long-run** ($t\to\infty$): both $\mathbb{E}[I]$ and $\operatorname{Var}(I)$ depend only on $\int_0^\infty h(u)\,du$ and $\int_0^\infty h^2(u)\,du$ — the pulse shape matters only through its area and squared area.

---

## Binomial Theorem and Dual Version

### Theorem 4.6.1 — Binomial Theorem (Direct Proof)

> [!Important] Theorem 4.6.1 — Binomial Theorem for Poisson Process
> **Statement:** For a Poisson process of rate $\lambda>0$, $0<u<t$, $0\leq k\leq n$:
> $$\Pr\{X(u)=k\mid X(t)=n\} = \binom{n}{k}\left(\frac{u}{t}\right)^k\left(1-\frac{u}{t}\right)^{n-k}$$
>
> **Proof (direct):**
> $$\Pr\{X(u)=k\mid X(t)=n\} = \frac{\Pr\{X(u)=k,\,X(t)-X(u)=n-k\}}{\Pr\{X(t)=n\}}$$
> The increments $X(u)$ and $X(t)-X(u)$ are independent (disjoint intervals). By stationarity, $X(t)-X(u)$ has the same distribution as $X(t-u)$. *(Caution: the replacement $X(t)-X(u)\to X(t-u)$ must be done only after factorizing — $X(t)$ and $X(t-u)$ refer to overlapping intervals and are not independent.)* Therefore:
> $$= \frac{\{e^{-\lambda u}(\lambda u)^k/k!\}\{e^{-\lambda(t-u)}[\lambda(t-u)]^{n-k}/(n-k)!\}}{e^{-\lambda t}(\lambda t)^n/n!} = \frac{n!}{k!(n-k)!}\frac{u^k(t-u)^{n-k}}{t^n} \qquad\square$$
>
> ![[Stochastic_Processes_2020_p146_img48.jpeg]]
> *Figure 4.12 — $(0,u)$ and $(u,t)$ are disjoint → independent increments. $(0,u)$ and $(0,t-u)$ overlap → not independent despite same statistics.*

### Dual Version

> [!Important] Dual Binomial Theorem
> **Statement:** For $0<t<s$ and $0\leq n\leq k$:
> $$\Pr\{X(s)=k\mid X(t)=n\} = \frac{e^{-\lambda(s-t)}[\lambda(s-t)]^{k-n}}{(k-n)!}$$
>
> **Proof:**
> $$\frac{\Pr\{X(t)=n,\,X(s)-X(t)=k-n\}}{\Pr\{X(t)=n\}} = \Pr\{X(s)-X(t)=k-n\} = \Pr\{X(s-t)=k-n\}$$
> since $X(t)$ and $X(s)-X(t)$ are independent (disjoint intervals), and stationarity applies after factorizing. $\square$

---

### Exercises

> [!Example] Exercise 4.6.1 — Written Test June 27, 2016
> **Problem:** Two independent Poisson processes $X_1(t)$, $X_2(t)$ with rates $\lambda_1=0.5$ and $\lambda_2=1$.
>
> 1. Compute $P[X_1(2)=1\mid X_1(3)=2]$ and $P[X_1(3)=2\mid X_1(2)=1]$.
> 2. Compute $P[X_1(1)=1\mid X_1(2)+X_2(2)=3]$ and $P[X_1(2)+X_2(2)=3\mid X_1(1)=1]$.
> 3. Compute $P[X_1(2)+X_2(2)=3\mid X_1(3)=0]$ and $P[X_1(2)+X_2(2)=3\mid X_1(3)=1]$.
>
> **Solutions:**
>
> **Part 1:**
>
> $X_1(2)$ given $X_1(3)=2$: Theorem 4.6.1 with $u=2$, $t=3$, $n=2$, $k=1$, $p=2/3$:
> $$P[X_1(2)=1\mid X_1(3)=2]=\binom{2}{1}\left(\frac{2}{3}\right)^1\left(\frac{1}{3}\right)^1=\frac{4}{9}\approx 0.44$$
>
> Dual: $X_1(3)$ given $X_1(2)=1$: must have $X_1(3)-X_1(2)=1$ in interval of length 1:
> $$P[X_1(3)=2\mid X_1(2)=1]=P[X_1(1)=1]=\lambda_1 e^{-\lambda_1}=0.5\,e^{-0.5}\approx 0.303$$
>
> **Part 2:**
>
> $X_1(1)$ given total $X(2)=X_1(2)+X_2(2)=3$: Theorem 4.5.5 combined with 4.5.4. Total rate $\lambda_1+\lambda_2=1.5$. Rectangle argument: $p=\lambda_1\cdot 1/[(\lambda_1+\lambda_2)\cdot 2]=0.5/(1.5\cdot 2)=1/6$. Binomial$(3,1/6)$:
> $$P[X_1(1)=1\mid X(2)=3]=\binom{3}{1}\left(\frac{1}{6}\right)^1\left(\frac{5}{6}\right)^2=\frac{25}{72}\approx 0.347$$
>
> Dual: $X(2)=3$ given $X_1(1)=1$: the remaining arrivals must come from the complement region (area = $\lambda_1\cdot 1+\lambda_2\cdot 2=2.5$):
> $$P[X(2)=3\mid X_1(1)=1]=P[X_2(2)+X_1(2)-X_1(1)=2]=\frac{(2.5)^2 e^{-2.5}}{2!}\approx 0.2565$$
>
> **Part 3:**
>
> Case $X_1(3)=0$: no arrivals from process 1 anywhere in $[0,3]$ → all 3 arrivals must come from $X_2$ in $[0,2]$:
> $$P[X_1(2)+X_2(2)=3\mid X_1(3)=0]=P[X_2(2)=3]=\frac{2^3 e^{-2}}{3!}=\frac{4}{3}e^{-2}\cdot\frac{1}{2}\approx 0.06$$
>
> *(Note: $\frac{4}{3}e^{-2}/2 = \frac{2^3}{6}e^{-2}=\frac{4}{3}e^{-2}/2$; numerical value $\approx0.0601$.)*
>
> Case $X_1(3)=1$: the single $X_1$-arrival can fall in $[0,2]$ (prob 2/3) or $[2,3]$ (prob 1/3). Use total probability over $X_1(2)\in\{0,1\}$:
> $$\sum_{i=0}^1 P[X_2(2)=3-i]\cdot P[X_1(2)=i\mid X_1(3)=1]$$
> $$= P[X_2(2)=3]\cdot\frac{1}{3}+P[X_2(2)=2]\cdot\frac{2}{3}$$
> $$= \frac{2^3 e^{-2}}{3!}\cdot\frac{1}{3}+\frac{2^2 e^{-2}}{2!}\cdot\frac{2}{3} = \frac{4}{9}e^{-2}+\frac{4}{3}e^{-2}=\frac{16}{9}e^{-2}\approx 0.24$$
>
> ![[Stochastic_Processes_2020_p150_img49.jpeg]]
> *Figure 4.13 — Geometry for part (c) of Exercise 4.6.1.*

> [!Example] Exercise 4.6.2 — Finite α-Chain
> **Problem:** A Markov chain has transition matrix:
>
> | State | 0 | 1 | 2 | 3 | 4 | 5 |
> |---|---|---|---|---|---|---|
> | 0 | $\alpha_1$ | $\alpha_2$ | $\alpha_3$ | $\alpha_4$ | $\alpha_5$ | $\alpha_6$ |
> | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
> | 2 | 0 | 1 | 0 | 0 | 0 | 0 |
> | 3 | 0 | 0 | 1 | 0 | 0 | 0 |
> | 4 | 0 | 0 | 0 | 1 | 0 | 0 |
> | 5 | 0 | 0 | 0 | 0 | 1 | 0 |
>
> with $\alpha_i\geq 0$, $\sum_{i=1}^6\alpha_i=1$. Find the limiting probability $\pi_0$.
>
> ![[Stochastic_Processes_2020_p151_img50.jpeg]]
> *Figure 4.14 — Transition diagram: from state 0, jump to state $i$ with prob $\alpha_{i+1}$; from state $i>0$, step down to $i-1$ deterministically.*
>
> **Solution:** Stationarity equations $\boldsymbol{\pi}=\boldsymbol{\pi}\mathbf{P}$:
>
> | Eq. | Stationary equation |
> |---|---|
> | $\pi_0=\pi_0\alpha_1+\pi_1$ | → $\pi_1=\pi_0(1-\alpha_1)$ |
> | $\pi_1=\pi_0\alpha_2+\pi_2$ | → $\pi_2=\pi_0(1-\alpha_1-\alpha_2)$ |
> | $\pi_2=\pi_0\alpha_3+\pi_3$ | → $\pi_3=\pi_0(1-\alpha_1-\alpha_2-\alpha_3)$ |
> | $\pi_3=\pi_0\alpha_4+\pi_4$ | → $\pi_4=\pi_0(\alpha_5+\alpha_6)$ |
> | $\pi_4=\pi_0\alpha_5+\pi_5$ | → $\pi_5=\pi_0\alpha_6$ |
>
> General pattern: $\pi_k=\pi_0\sum_{j=k+1}^6\alpha_j$ for $k=1,\ldots,5$.
>
> Normalization $\sum_{k=0}^5\pi_k=\left(\sum_{k=1}^6 k\alpha_k\right)\pi_0=1$:
> $$\pi_0 = \frac{1}{\sum_{k=1}^6 k\alpha_k} = \frac{1}{\mathbb{E}[\text{return time to }0]}$$
>
> **Interpretation:** From state 0, with probability $\alpha_k$ the chain goes to state $k-1$ and takes exactly $k$ steps to return to 0 (stepping down one per step). The mean return time is $\sum_{k=1}^6 k\alpha_k$, confirming $\pi_0=1/m_0$.

> [!Example] Exercise 4.6.3 — Infinite α-Chain
> **Problem:** Same structure as 4.6.2 but infinite: $\{\alpha_i:i=1,2,\ldots\}$ is a probability distribution. $\alpha_1>0$, $\alpha_2>0$ (aperiodic). Find the condition for a limiting distribution to exist, and what it is.
>
> **Solution:**
> Solve recursively: $\pi_n=\left(\sum_{k=n+1}^\infty\alpha_k\right)\pi_0 = \mathbb{P}[X>n]\,\pi_0$.
>
> Normalization:
> $$\sum_{n=0}^\infty\pi_n = \pi_0\sum_{n=0}^\infty\mathbb{P}[X>n] = \pi_0\,\mathbb{E}[X] = 1$$
>
> **Condition:** A limiting distribution exists iff $\mathbb{E}[X]=\sum_{n=0}^\infty\mathbb{P}[X>n]<\infty$, i.e. the $\alpha$ distribution has finite mean. Then:
> $$\pi_0 = \frac{1}{\mathbb{E}[X]}, \qquad \pi_n = \frac{\mathbb{P}[X>n]}{\mathbb{E}[X]}$$

> [!Example] Exercise 4.6.4 — Fraction of Transitions $k\to m$
> **Problem:** In a finite regular Markov chain with transition matrix $\mathbf{P}$ and limiting distribution $\boldsymbol{\pi}$, what fraction of transitions go from state $k$ to state $m$?
>
> **Solution:** In the long run, the fraction of time in state $k$ is $\pi_k$; from state $k$ the next step goes to $m$ with probability $P_{km}$:
> $$\lim_{n\to\infty}\Pr\{X_n=k,\,X_{n+1}=m\} = \pi_k P_{km}$$

> [!Example] Exercise 4.6.5 — Limits for Regular Markov Chain
> **Problem:** For a finite regular Markov chain $\{X_n\}$ with $\mathbf{P}$, $\boldsymbol{\pi}$, find:
> 1. $\lim_{n\to\infty}P[X_{n+1}=j\mid X_0=i]$
> 2. $\lim_{n\to\infty}P[X_n=k,X_{n+1}=j\mid X_0=i]$
> 3. $\lim_{n\to\infty}P[X_{n-1}=k,X_n=j\mid X_0=i]$
>
> **Solution:**
> 1. $\lim_{n\to\infty}P[X_{n+1}=j\mid X_0=i]=\pi_j$ (regular chain, independent of $i$).
> 2. Use $P[X_n=k,X_{n+1}=j\mid X_0=i]=P[X_{n+1}=j\mid X_n=k]P[X_n=k\mid X_0=i]\to P_{kj}\pi_k$.
> 3. Time-shift of (2): same limit $\pi_k P_{kj}$.

> [!Example] Exercise 4.6.6 — Backward Probability
> **Problem:** Transition matrix:
> $$\mathbf{P}=\begin{pmatrix}0.4&0.4&0.2\\0.6&0.2&0.2\\0.4&0.2&0.4\end{pmatrix}$$
> Find $\lim_{n\to\infty}P[X_{n-1}=2\mid X_n=1]$.
>
> **Solution:** Apply Bayes:
> $$P[X_{n-1}=2\mid X_n=1]=P_{21}\frac{P[X_{n-1}=2]}{P[X_n=1]}\xrightarrow{n\to\infty}P_{21}\frac{\pi_2}{\pi_1}$$
> Compute $\boldsymbol{\pi}$ from $\boldsymbol{\pi}=\boldsymbol{\pi}\mathbf{P}$, $\sum\pi_i=1$, then:
> $$\lim_{n\to\infty}P[X_{n-1}=2\mid X_n=1]=P_{21}\frac{\pi_2}{\pi_1}=0.2\cdot\frac{\pi_2}{\pi_1}=\frac{6}{35}\approx 0.1714$$

> [!Example] Exercise 4.6.7 — Man Walking in Rain (1 and 2 cars)
> **Problem:** A man commutes by car or walking. He drives only when it rains (prob $p$ each trip) and the car is where he is. States: $X_n=1$ (car available), $X_n=0$ (car not available). What fraction of days does he walk in the rain?
>
> **Solution (1 car):** Transition matrix:
> $$\mathbf{P}=\begin{pmatrix}0&1\\1-p&p\end{pmatrix}$$
> Limiting distribution: $\pi_0=\frac{1-p}{2-p}$, $\pi_1=\frac{1}{2-p}$.
>
> Probability of walking in rain per trip:
> $$\pi_0 p + \pi_1(1-p)p = \frac{(1-p)p}{2-p}+\frac{(1-p)p}{2-p} = \frac{2p(1-p)}{2-p}$$
>
> **Solution (2 cars):** States $X_n=0,1,2$ (number of cars at man's location). Transition matrix:
> $$\mathbf{P}=\begin{pmatrix}0&0&1\\0&1-p&p\\1-p&p&0\end{pmatrix}$$
> Limiting: $\pi_0=\frac{1-p}{3-p}$, $\pi_1=\pi_2=\frac{1}{3-p}$.
>
> Probability of walking in rain:
> $$\pi_0 p + \pi_2(1-p)p = \frac{2p(1-p)}{3-p}$$

---

## P.A.S.T.A. Property

> [!Important] Definition — $p_n(t)$ and $a_n(t)$
> For a queueing system with $N(t)$ users at time $t$:
> $$p_n(t) = \Pr\{N(t)=n\}$$
> $$a_n(t) = \Pr\{N(t)=n \mid \text{an arrival occurred just after time }t\}$$
>
> $p_n$ = distribution seen by **external observer**; $a_n$ = distribution seen by **arriving user**.

### PASTA Theorem

> [!Important] P.A.S.T.A. — Poisson Arrivals See Time Averages
> **Statement:** If arrivals are Poisson and service times are independent of future arrival times, then:
> $$\lim_{t\to\infty}p_n(t) = \lim_{t\to\infty}a_n(t) \qquad n=0,1,\ldots$$
>
> ![[Stochastic_Processes_2020_p158_img51.jpeg]]
> *Figure 4.16 — $N(t)$ depends on arrivals and departures up to $t$; the arrival at $t^+$ must be independent of $N(t)$.*
>
> **Proof:**
> $N(t)$ depends on arrivals and departures up to time $t$. The arrival at $t^+$ must be independent of $N(t)$, which requires:
>
> 1. **Arrival independence:** Poisson increments on disjoint intervals are independent → $N(t)$ does not affect future arrivals. ✓
> 2. **Service independence:** Departure times depend on service times, so service times must be independent of future arrivals. ✓ (Reasonable assumption.)
>
> Under these conditions the two events in $a_n(t)$ are independent:
> $$a_n(t) = \Pr\{N(t)=n\}\cdot\Pr\{\text{arrival just after }t\}$$
> Taking $t\to\infty$: $\lim p_n(t) = \lim a_n(t)$. $\square$
>
> **Interpretation:** Poisson arrivals do not "see" a biased view of the system — they see the same long-run statistics as an external observer.

### Counter-Examples

> [!Example] Counter-Example 1 — Non-Poisson Arrivals
> **Problem:** Inter-arrival times $\sim\mathrm{Uniform}[2,4]$s; service time = 1s exactly.
>
> ![[Stochastic_Processes_2020_p159_img52.jpeg]]
> *Figure 4.17 — Each arriving customer finds system empty (service finishes before next arrival).*
>
> **Analysis:** Since minimum inter-arrival time (2s) > service time (1s), every arriving customer finds the system empty: $a_0=1$, $a_i=0$ for $i>0$.
>
> External observer: system is busy for 1s and empty for $\mathrm{Uniform}[1,3]$s on average 2s. Mean cycle = 3s, so $p_1=1/3$, $p_0=2/3$.
>
> **Conclusion:** $a_0=1\neq p_0=2/3$. PASTA fails because arrivals are **not Poisson**.

> [!Example] Counter-Example 2 — Arrival-Service Dependence
> **Problem:** Arrivals are Poisson but service time of the $n$-th customer equals half the interarrival time to the $(n+1)$-th customer.
>
> **Analysis:** Service time = half next interarrival → system always empty when next customer arrives: $a_0=1$.
>
> External observer: system is busy half the time → $p_0=p_1=1/2$.
>
> **Conclusion:** $a_0=1\neq p_0=1/2$. PASTA fails because service times and future arrivals are **correlated**.

### Departures See Same Distribution as Arrivals

Define $d_n(t)=\Pr\{N(t)=n\mid\text{departure just before }t\}$. Under stability and unit-step changes in $N(t)$:

> [!Important] Theorem — $d_n=a_n$
> **Statement:** For a stable system with unit-step changes in $N(t)$:
> $$d_n = a_n \qquad n=0,1,\ldots$$
>
> **Proof:**
> Fix a level $n$. For each upward transition $n\to n+1$ (arrival finds $N=n$) there is exactly one downward transition $n+1\to n$ (departure leaves $N=n$), because the system is stable (returns to 0 infinitely often) and transitions are unit steps.
>
> ![[Stochastic_Processes_2020_p162_img53.jpeg]]
> *Figure 4.19 — For a stable system, upward and downward transitions across level $n$ balance in the long run.*
>
> In the long run:
> $$\lim_{t\to\infty}\frac{\#\{n\to n+1\text{ transitions in }[0,t]\}}{\#\{\text{all arrivals in }[0,t]\}} = \lim_{t\to\infty}\frac{\#\{n+1\to n\text{ transitions in }[0,t]\}}{\#\{\text{all departures in }[0,t]\}}$$
>
> since the difference between numerators is at most 1 (finite), while both denominators $\to\infty$ (stability). Therefore $d_n=a_n$. $\square$
>
> **Consequence for M/G/1:** The embedded Markov chain sampled at departure epochs is representative of the overall long-run distribution, justifying the M/G/1 analysis from Chapter 2.

### Periodic Class — Limit Existence Condition

Consider a reducible chain with block structure:
$$\mathbf{P} = \begin{Vmatrix}\mathbf{Q}&\mathbf{R}_1&\mathbf{R}_2\\0&\mathbf{A}&0\\0&0&\mathbf{1}\end{Vmatrix}, \qquad \mathbf{A}=\begin{Vmatrix}0&1\\1&0\end{Vmatrix}, \qquad \mathbf{A}^n=\begin{cases}\mathbf{A}&n\text{ odd}\\\mathbf{I}&n\text{ even}\end{cases}$$

$\mathbf{Q}$ = transient class, $\mathbf{A}$ = periodic class (period 2), $\mathbf{1}$ = absorbing state.

![[Stochastic_Processes_2020_p163_img54.jpeg]]
*Figure 4.20 — Chain structure: transient block $\mathbf{Q}$ connects to periodic class $\mathbf{A}$ via $\mathbf{R}_1$ and to absorbing state via $\mathbf{R}_2$.*

Computing $\mathbf{P}^n$ by induction:
$$\mathbf{P}^{n+1} = \begin{Vmatrix}\mathbf{Q}^{n+1}&\sum_{i=0}^n\mathbf{Q}^i\mathbf{R}_1\mathbf{A}^{n-i}&\left(\sum_{i=0}^n\mathbf{Q}^i\right)\mathbf{R}_2\\0&\mathbf{A}^{n+1}&0\\0&0&\mathbf{1}\end{Vmatrix}$$

The question is whether $\lim_{n\to\infty}\sum_{i=0}^n\mathbf{Q}^i\mathbf{R}_1\mathbf{A}^{n-i}$ exists. Splitting even and odd $n$:

For $n=2k$: $\xrightarrow{k\to\infty}[\mathbf{I}-\mathbf{Q}^2]^{-1}(\mathbf{R}_1+\mathbf{Q}\mathbf{R}_1\mathbf{A})$

For $n=2k+1$: $\xrightarrow{k\to\infty}[\mathbf{I}-\mathbf{Q}^2]^{-1}(\mathbf{R}_1\mathbf{A}+\mathbf{Q}\mathbf{R}_1)$

(geometric series in $\mathbf{Q}^2$ converges since $\mathbf{Q}$ is transient).

The two limits coincide iff:
$$\mathbf{R}_1+\mathbf{Q}\mathbf{R}_1\mathbf{A}=\mathbf{R}_1\mathbf{A}+\mathbf{Q}\mathbf{R}_1 \implies (\mathbf{I}-\mathbf{Q})\mathbf{R}_1=(\mathbf{I}-\mathbf{Q})\mathbf{R}_1\mathbf{A}$$

Since $(\mathbf{I}-\mathbf{Q})$ is invertible (transient $\mathbf{Q}$):

> [!Important] Condition for General Limit to Exist
> $$\mathbf{R}_1 = \mathbf{R}_1\mathbf{A}$$
> Since $\mathbf{R}_1\mathbf{A}$ is $\mathbf{R}_1$ with columns switched, this means **the two columns of $\mathbf{R}_1$ are identical** — i.e., the system enters the periodic class uniformly regardless of which state it will be in. Probabilistically: entering a periodic class from a transient state must occur with equal probability for both states of the class.

---

## Summary Table

| Concept | Definition / Formula | Conditions / Notes |
|---|---|---|
| Poisson distribution | $p_k=e^{-\mu}\mu^k/k!$ | $\mu>0$; mean = variance = $\mu$ |
| Sum of Poisson | $X+Y\sim\mathrm{Poisson}(\mu+\nu)$ | $X,Y$ independent (Thm 4.1.1) |
| Poisson+Binomial filter | $M\mid N\sim\mathrm{Bin}(N,p)\Rightarrow M\sim\mathrm{Poisson}(\mu p)$ | Thm 4.1.2 |
| Poisson process | $X(t+s)-X(s)\sim\mathrm{Poisson}(\lambda t)$; indep. stationary incr.; $X(0)=0$ | Rate $\lambda>0$ constant |
| Mean/variance | $\mathbb{E}[X(t)]=\operatorname{Var}[X(t)]=\lambda t$ | — |
| Law of Rare Events | $\|P[S_n=k]-\mathrm{Poisson}(\mu)_k\|\leq\sum p_i^2$ | Poisson = discrete CLT |
| Superposition | $X_1+X_2\sim\mathrm{Poisson}(\lambda_1+\lambda_2)$ | Independent processes (Thm 4.4.1) |
| Thinning | Each event type-1 w.p. $p$: $X_1\sim\mathrm{Poisson}(\lambda p)$, $X_2\sim\mathrm{Poisson}(\lambda(1-p))$, independent | Thm 4.4.2 |
| Inter-arrival | $S_i\sim\mathrm{Exp}(\lambda)$ i.i.d. | Thm 4.5.1 |
| Waiting time | $W_n\sim\mathrm{Gamma}(n,\lambda)$ | $W_n=\sum_{i=0}^{n-1}S_i$ (Thm 4.5.2) |
| Conditional arrival times | $f_{W_1,\ldots,W_n\mid X(t)=n}=n!\,t^{-n}$ | Ordered Uniform$(0,t)$ (Thm 4.5.3) |
| Binomial theorem | $X(u)\mid X(t)=n\sim\mathrm{Bin}(n,u/t)$ | $0<u<t$ (Thm 4.5.4, 4.6.1) |
| Competition theorem | $X_1(t)\mid X_1+X_2=n\sim\mathrm{Bin}(n,\lambda_1/(\lambda_1+\lambda_2))$ | Thm 4.5.5 |
| Dual binomial | $X(s)\mid X(t)=n\Rightarrow\mathrm{Poisson}(\lambda(s-t))$ for the excess | $0<t<s$ |
| M/G/∞ | $M(t)\sim\mathrm{Poisson}(\lambda pt)$; $p=(1/t)\int_0^t[1-G(z)]dz$ | Steady state: $\lambda/\mu$ |
| Shot noise | $\mathbb{E}[I]=\lambda\int h$; $\operatorname{Var}[I]=\lambda\int h^2$ | Compound Poisson sum |
| PASTA | $\lim p_n=\lim a_n$ if arrivals Poisson and indep. of service | Poisson Arrivals See Time Averages |
| $d_n=a_n$ | Arrivals and departures see same steady-state | Requires stability + unit-step transitions |
| Periodic limit condition | $\mathbf{R}_1=\mathbf{R}_1\mathbf{A}$ (equal columns of $\mathbf{R}_1$) | General limit exists iff uniform entry into periodic class |
