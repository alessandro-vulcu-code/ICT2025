# Chapter 4 — Poisson Processes

Poisson processes occupy a special role in stochastic modelling: they describe the accumulation of rare, independent events over time, arise as universal limits of many different processes (Law of Rare Events), and admit remarkably clean closed-form results. This chapter develops their theory from the ground up.

---

## 4.1 The Poisson Distribution

**Definition.** The **Poisson distribution** with parameter $\mu > 0$ has probability mass function:
$$p_k \equiv \mathbb{P}[X = k] = \frac{e^{-\mu}\mu^k}{k!}, \qquad k = 0, 1, 2, \ldots \tag{4.1}$$

Its mean and variance are both equal to $\mu$:
$$\mathbb{E}[X] = \mu, \qquad \mathrm{Var}[X] = \mu$$

The coincidence of mean and variance is a distinctive signature of the Poisson distribution and is often used in practice to test whether data follows it.

---

> **Theorem 4.1.1 (Sum of Poisson variables is Poisson).** Let $X \sim \mathrm{Poisson}(\mu)$ and $Y \sim \mathrm{Poisson}(\nu)$ be independent. Then $X + Y \sim \mathrm{Poisson}(\mu + \nu)$.

**Proof.** We compute $\mathbb{P}[X + Y = n]$ directly. The event $\{X + Y = n\}$ decomposes into mutually exclusive events $\{X = k, Y = n-k\}$ for $k = 0, 1, \ldots, n$. By the law of total probability and independence:

$$\mathbb{P}[X + Y = n] = \sum_{k=0}^{n} \mathbb{P}[X=k]\,\mathbb{P}[Y=n-k] = \sum_{k=0}^{n} \frac{\mu^k e^{-\mu}}{k!}\,\frac{\nu^{n-k}e^{-\nu}}{(n-k)!}$$

Factoring $e^{-(\mu+\nu)}$ and multiplying/dividing by $n!$ to expose the binomial theorem:

$$= \frac{e^{-(\mu+\nu)}}{n!} \underbrace{\sum_{k=0}^{n} \binom{n}{k} \mu^k \nu^{n-k}}_{(\mu+\nu)^n} = \frac{e^{-(\mu+\nu)}(\mu+\nu)^n}{n!} \tag{4.2}$$

which is $\mathrm{Poisson}(\mu + \nu)$. $\square$

**Corollary.** By induction, the sum of $m$ independent Poisson random variables with parameters $\mu_1, \ldots, \mu_m$ is $\mathrm{Poisson}(\mu_1 + \cdots + \mu_m)$.

---

> **Theorem 4.1.2 (Binomial thinning of a Poisson).** Let $N \sim \mathrm{Poisson}(\mu)$ and, conditional on $N$, let $M \sim \mathrm{Binomial}(N, p)$. Then the marginal distribution of $M$ is $\mathrm{Poisson}(\mu p)$.

**Intuition.** Take $N$ Poisson-distributed objects and keep each independently with probability $p$. The number retained, $M$, is again Poisson — with the effective rate reduced by the factor $p$. The binomial thinning acts as a "filter" that scales the rate without changing the distributional form.

*(Proof: this is Exercise 1.6.1. The argument uses the law of total probability to sum over all values of $N$, applying the binomial pmf and the Poisson pmf for $N$, and recognising the resulting series as a Poisson pmf.)*

---

## 4.2 The Poisson Process

A **Poisson process** formalises the intuition of counting rare, memoryless events accumulating over time.

> **Definition 1 (Poisson process).** A Poisson process of rate $\lambda > 0$ is an integer-valued stochastic process $\{X(t) : t \geq 0\}$ satisfying:
>
> 1. **Initial condition:** $X(0) = 0$.
> 2. **Independent and stationary increments:** For any $0 = t_0 < t_1 < \cdots < t_n$, the increments $X(t_1)-X(t_0),\, X(t_2)-X(t_1),\, \ldots,\, X(t_n)-X(t_{n-1})$ are mutually independent random variables, and the distribution of $X(t_{i+1})-X(t_i)$ depends only on the interval length $t_{i+1}-t_i$.
> 3. **Poisson increments:** For any $s \geq 0$ and $t > 0$:
> $$\mathbb{P}[X(s+t) - X(s) = k] = \frac{(\lambda t)^k e^{-\lambda t}}{k!}, \qquad k = 0, 1, 2, \ldots$$

**Unpacking the axioms:**
- **Independent increments:** the number of events in any interval is independent of events in any disjoint interval. The future does not depend on the past.
- **Stationary increments:** the process is in its "steady state" — the event rate $\lambda$ is constant over time, and the count distribution depends only on interval length, not position.
- **Poisson increments:** each count follows a Poisson distribution with mean $\lambda t$ (rate times duration).

Immediate consequences:
$$\mathbb{E}[X(t)] = \lambda t, \qquad \mathrm{Var}[X(t)] = \lambda t$$

---

**Example 1 — Undersea cable defects.** Defects occur at rate $\lambda = 0.1$ per mile.

- $\mathbb{P}[\text{no defects in first 2 miles}] = \mathbb{P}[X(2)=0] = e^{-0.2} \approx 0.819$
- By independent increments, the conditional probability of no defects in miles 2–3, *given* no defects in miles 0–2, equals the unconditional probability:
  $\mathbb{P}[X(3)-X(2)=0] = e^{-0.1} \approx 0.905$

**Example 2 — Customer arrivals.** Customers arrive at rate $\lambda = 4$/hour. The store opens at 9:00 AM (set as $t=0$).

$$\mathbb{P}[X({\textstyle\frac{1}{2}})=1,\, X({\textstyle\frac{5}{2}})=5] = \mathbb{P}[X({\textstyle\frac{1}{2}})=1]\cdot\mathbb{P}[X({\textstyle\frac{5}{2}})-X({\textstyle\frac{1}{2}})=4]$$

Using independent increments to factorise, then computing each Poisson probability:
$$= \frac{e^{-2} \cdot 2^1}{1!} \cdot \frac{e^{-8}\cdot 8^4}{4!} = 2e^{-2}\cdot\frac{512}{3}e^{-8} \approx 0.0155$$

**Non-homogeneous Poisson process.** Relaxing stationarity, let the rate be a function of time $\lambda(t)$. In an infinitesimal interval $[t, t+h]$:
$$\mathbb{P}[X(t+h)-X(t) = 1] = \lambda(t)h + o(h), \qquad \mathbb{P}[X(t+h)-X(t) \geq 2] = o(h)$$

The expected number of events in $(s, s+t]$ becomes $\int_s^{s+t} \lambda(\tau)\,\mathrm{d}\tau$ rather than $\lambda t$.

---

## 4.3 The Law of Rare Events

The Poisson distribution is the discrete analogue of the Gaussian distribution. Just as the Central Limit Theorem guarantees that the sum of many i.i.d. continuous random variables converges to a Gaussian, the **Law of Rare Events** guarantees that the count of many independent, individually-unlikely events converges to a Poisson distribution.

**Simple form.** Consider $N$ independent Bernoulli trials, each succeeding with probability $p \ll 1$, with the total expected successes $\mu = Np$ held fixed. As $N \to \infty$ and $p \to 0$:
$$\mathbb{P}[X_{N,p} = k] = \binom{N}{k}p^k(1-p)^{N-k} \xrightarrow{N\to\infty} \frac{e^{-\mu}\mu^k}{k!}$$

**General form.** The result holds even when the success probabilities vary across trials:

> **Theorem 4.3.1 (Law of Rare Events).** Let $\varepsilon_1, \varepsilon_2, \ldots, \varepsilon_n$ be independent Bernoulli random variables with $\mathbb{P}[\varepsilon_i = 1] = p_i$. Let $S_n = \varepsilon_1 + \cdots + \varepsilon_n$ and $\mu = p_1 + \cdots + p_n$. Then the distribution of $S_n$ differs from $\mathrm{Poisson}(\mu)$ by at most:
> $$\left|\mathbb{P}[S_n = k] - \frac{\mu^k e^{-\mu}}{k!}\right| \leq \sum_{i=1}^{n} p_i^2 \tag{4.4}$$

The bound (4.4) vanishes when all $p_i$ are small — the Poisson approximation becomes exact. If $p_i \equiv p$ and $Np = \mu$, then $\sum p_i^2 = Np^2 = \mu p = \mu^2/N \to 0$.

**Extension to stochastic processes.** The Law of Rare Events extends to processes: the superposition of many independent, low-rate processes (not necessarily Poisson themselves) converges to a Poisson process as the number of contributing processes grows. This justifies using a single Poisson model to describe aggregate arrivals from many heterogeneous sources — even if none of the individual sources is Poisson.

---

## 4.4 Properties of Poisson Processes

The two main operations — **superposition** (merging processes) and **thinning** (splitting) — preserve the Poisson property.

### Superposition

> **Theorem 4.4.1 (Superposition).** Let $X_1(t)$ and $X_2(t)$ be independent Poisson processes with rates $\lambda_1$ and $\lambda_2$. Then $X(t) = X_1(t) + X_2(t)$ is a Poisson process with rate $\lambda_1 + \lambda_2$.

![[Stochastic_Processes_2020_p131_img34.jpeg]]
*Figure 4.1 — Two merged Poisson processes form a single Poisson process with combined rate $\lambda_1 + \lambda_2$.*

**Proof.** We verify all three axioms of Definition 1:
1. $X(0) = X_1(0) + X_2(0) = 0 + 0 = 0$. $\checkmark$
2. Since $X_1$ and $X_2$ each have independent stationary increments, their sum $X$ inherits both properties. $\checkmark$
3. $X_1(t) \sim \mathrm{Poisson}(\lambda_1 t)$ and $X_2(t) \sim \mathrm{Poisson}(\lambda_2 t)$ are independent, so by Theorem 4.1.1: $X(t) \sim \mathrm{Poisson}((\lambda_1 + \lambda_2)t)$. $\checkmark$ $\square$

---

### Thinning (Splitting)

> **Theorem 4.4.2 (Thinning).** Let $X(t)$ be a Poisson process with rate $\lambda$. Independently classify each event as type 1 (with probability $p$) or type 2 (with probability $1-p$). Let $X_1(t)$ and $X_2(t)$ count type-1 and type-2 events. Then $X_1(t)$ and $X_2(t)$ are **independent** Poisson processes with rates $\lambda p$ and $\lambda(1-p)$.

![[Stochastic_Processes_2020_p132_img35.jpeg]]
*Figure 4.2 — Each event in a Poisson process is independently classified; the two sub-streams are themselves independent Poisson processes.*

**Proof.** Axioms 1 and 2 are inherited from $X$ (since independent thinning preserves stationarity and independence of increments). For axiom 3, compute the **joint distribution** of $X_1(t)$ and $X_2(t)$:

$$\mathbb{P}[X_1(t)=n,\, X_2(t)=m] = \mathbb{P}[X_1(t)=n \mid X(t)=n+m]\,\mathbb{P}[X(t)=n+m]$$

Given $X(t) = n+m$ total events, the number of type-1 events is $\mathrm{Binomial}(n+m, p)$:

$$= \binom{n+m}{n}p^n(1-p)^m \cdot \frac{e^{-\lambda t}(\lambda t)^{n+m}}{(n+m)!}$$

Expanding and regrouping:

$$= \frac{(\lambda pt)^n e^{-\lambda pt}}{n!} \cdot \frac{(\lambda(1-p)t)^m e^{-\lambda(1-p)t}}{m!}$$

This factorises as the product of two independent Poisson pmfs with rates $\lambda pt$ and $\lambda(1-p)t$. $\checkmark$

**Independence of increments on overlapping intervals.** To complete the proof that $X_1$ and $X_2$ are independent processes (not just independent at any fixed time $t$), we show that increments $X_1(t_3)-X_1(t_1)$ and $X_2(t_4)-X_2(t_2)$ are independent for all choices of intervals $[t_1,t_3]$ and $[t_2,t_4]$.

There are three cases:

![[Stochastic_Processes_2020_p133_img36.jpeg]]
*(a) — Partially overlapping: $[t_1,t_3]$ and $[t_2,t_4]$ share $[t_2,t_3]$.*

![[Stochastic_Processes_2020_p133_img37.jpeg]]
*(b) — One interval fully inside the other.*

![[Stochastic_Processes_2020_p133_img38.jpeg]]
*(c) — Disjoint intervals.*

*Figure 4.3 — All possible overlaps of two intervals.*

**Case (a): Partial overlap $t_1 < t_2 < t_3 < t_4$.** Decompose:
$$X_1(t_3) - X_1(t_1) = \underbrace{[X_1(t_3)-X_1(t_2)]}_{\text{overlap}} + \underbrace{[X_1(t_2)-X_1(t_1)]}_{\text{non-overlap}}$$
$$X_2(t_4) - X_2(t_2) = \underbrace{[X_2(t_3)-X_2(t_2)]}_{\text{overlap}} + \underbrace{[X_2(t_4)-X_2(t_3)]}_{\text{non-overlap}}$$

On the overlap $[t_2,t_3]$: $X_1$ and $X_2$ increments are independent (shown above). On non-overlapping intervals, Poisson increments are always independent. Sums of pairwise-independent terms are independent. $\checkmark$

**Cases (b) and (c)** follow by similar decomposition. $\square$

---

## 4.5 Distributions Associated with a Poisson Process

A Poisson process carries a rich family of associated distributions, depending on which aspect we focus on.

**Definitions:**
- **Arrival times (waiting times)** $W_n$: the time at which the $n$-th event occurs.
- **Inter-arrival times (sojourn times)** $S_i = W_{i+1} - W_i$: time between consecutive events.

![[Stochastic_Processes_2020_p134_img39.jpeg]]
*Figure 4.4 — A sample path of a Poisson process showing waiting times $W_i$ (absolute) and sojourn times $S_n$ (between events).*

Clearly $W_n = \sum_{k=0}^{n-1} S_k$.

---

> **Theorem 4.5.1 (Inter-arrival times are exponential).** The sojourn times $S_i$ are i.i.d. $\mathrm{Exp}(\lambda)$.

**Proof.** See the proof of Theorem 2.2.1 (Chapter 2). For completeness: $\mathbb{P}[S_0 > t] = \mathbb{P}[0 \text{ events in } [0,t]] = e^{-\lambda t}$, so $S_0 \sim \mathrm{Exp}(\lambda)$. By independent and stationary increments, the same calculation applies to each $S_n$ conditioned on any history, yielding independence. $\square$

---

> **Theorem 4.5.2 (Waiting times are Gamma-distributed).** The time $W_n$ of the $n$-th event has the Gamma distribution:
> $$f_{W_n}(t) = \frac{\lambda^n t^{n-1}}{(n-1)!}\,e^{-\lambda t}, \qquad t \geq 0, \quad n = 1, 2, \ldots$$

**Proof.** Since $W_n = S_0 + S_1 + \cdots + S_{n-1}$ is the sum of $n$ i.i.d. $\mathrm{Exp}(\lambda)$ random variables, and the Gamma distribution with parameters $(n, \lambda)$ is by definition the distribution of such a sum (Section 1.5.4), the result follows immediately. $\square$

---

### Uniform Conditional Distribution of Arrival Times

Given that exactly $n$ events occurred in $(0, t]$, where are they located?

**Setup.** Draw $n$ points $U_1, \ldots, U_n$ independently and uniformly on $(0, t)$. Their joint pdf is:
$$f_{U_1,\ldots,U_n}(u_1,\ldots,u_n) = t^{-n}, \qquad (u_1,\ldots,u_n) \in (0,t)^n$$

Now let $W_1 < W_2 < \cdots < W_n$ be the same points in ascending order. The ordered statistics are not independent (the ordering constraint couples them). Their joint pdf is:
$$f_{W_1,\ldots,W_n}(w_1,\ldots,w_n) = n!\,t^{-n}, \qquad 0 < w_1 < w_2 < \cdots < w_n \leq t \tag{4.8}$$

The factor $n!$ accounts for the $n!$ permutations of $\{U_i\}$ that all produce the same ordered sequence $\{W_i\}$.

![[Stochastic_Processes_2020_p135_img40.jpeg]]
*Figure 4.5 — $n$ uniform points $U_i$ on $(0,t)$, and their ordered version $W_i$.*

![[Stochastic_Processes_2020_p135_img41.jpeg]]
*Figure 4.6 — For $n=2$: either $U_1$ or $U_2$ can fall in $[w_1, w_1+\Delta w_1]$; both permutations contribute.*

**Derivation for $n=2$.** The probability that $W_1 \in [w_1, w_1+\Delta w_1]$ and $W_2 \in [w_2, w_2+\Delta w_2]$ equals the probability that $U_1$ or $U_2$ occupies the first interval and the other occupies the second (both permutations are possible and mutually exclusive):

$$f_{W_1,W_2}(w_1,w_2)\,\Delta w_1\,\Delta w_2 = 2 \cdot \frac{\Delta w_1}{t}\cdot\frac{\Delta w_2}{t}$$

Dividing by $\Delta w_1\,\Delta w_2$ and taking the limit: $f_{W_1,W_2}(w_1,w_2) = 2t^{-2} = 2!\,t^{-2}$. Generalising to $n$ points gives (4.8). $\square$

---

> **Theorem 4.5.3 (Conditional uniform distribution of arrival times).** Given $X(t) = n$, the joint pdf of the $n$ arrival times $W_1 < W_2 < \cdots < W_n$ is:
> $$f_{W_1,\ldots,W_n|X(t)=n}(w_1,\ldots,w_n) = n!\,t^{-n}, \qquad 0 < w_1 < \cdots < w_n \leq t \tag{4.9}$$
> Equivalently: given their count, the arrival times are distributed as $n$ independent uniform random variables on $(0,t)$, sorted in order.

**Proof.** Choose disjoint intervals $[w_i, w_i + \Delta w_i]$ (possible since all $w_i$ are distinct; simultaneous events are negligible in a Poisson process). Compute the probability that the $i$-th arrival falls in $[w_i, w_i+\Delta w_i]$ and no arrivals occur elsewhere:

$$\mathbb{P}[\text{one arrival in each } [w_i,w_i+\Delta w_i],\, \text{zero elsewhere} \mid X(t)=n]$$

![[Stochastic_Processes_2020_p137_img42.jpeg]]
*Figure 4.7 — One arrival in each $[w_i, w_i+\Delta w_i]$, zero elsewhere. Increments over disjoint intervals are independent.*

By independence of Poisson increments over disjoint intervals, the numerator factors:

$$\text{Numerator} = \prod_{i=1}^n (\lambda\,\Delta w_i\,e^{-\lambda\Delta w_i})\cdot e^{-\lambda(t - \sum_i \Delta w_i)}$$

$$= \lambda^n e^{-\lambda t}\prod_{i=1}^n \Delta w_i$$

Dividing by $\mathbb{P}[X(t)=n] = e^{-\lambda t}(\lambda t)^n/n!$:

$$f_{W_1,\ldots,W_n|X(t)=n}\,\Delta w_1\cdots\Delta w_n = \frac{\lambda^n e^{-\lambda t}\prod_i\Delta w_i}{e^{-\lambda t}(\lambda t)^n/n!} = n!\,t^{-n}\prod_i\Delta w_i$$

Dividing by $\prod_i\Delta w_i$ and taking the limit gives (4.9). $\square$

---

> **Theorem 4.5.4 (Binomial theorem — past interval).** Let $X(t)$ be a Poisson process and fix $0 < u < t$. Given $X(t) = n$, the number of arrivals in $(0, u)$ follows:
> $$\mathbb{P}[X(u) = k \mid X(t) = n] = \binom{n}{k}\left(\frac{u}{t}\right)^k\left(1-\frac{u}{t}\right)^{n-k}, \qquad k = 0, 1, \ldots, n$$

**Proof.** By Theorem 4.5.3, given $X(t)=n$, each of the $n$ arrival times is uniformly distributed in $(0,t)$ and independent. Each falls in $(0,u)$ with probability $u/t$. The number falling in $(0,u)$ is therefore $\mathrm{Binomial}(n, u/t)$. $\square$

![[Stochastic_Processes_2020_p138_img43.jpeg]]
*Figure 4.8 — Each of $n$ uniform arrival times falls in $(0,u)$ with probability $u/t$, giving a binomial count.*

**Direct proof (without Theorem 4.5.3).** Using conditional probability and independence of increments on disjoint intervals $[0,u]$ and $(u,t]$:

$$\mathbb{P}[X(u)=k \mid X(t)=n] = \frac{\mathbb{P}[X(u)=k,\, X(t)-X(u)=n-k]}{\mathbb{P}[X(t)=n]}$$

$$= \frac{e^{-\lambda u}(\lambda u)^k/k! \cdot e^{-\lambda(t-u)}[\lambda(t-u)]^{n-k}/(n-k)!}{e^{-\lambda t}(\lambda t)^n/n!} = \binom{n}{k}\frac{u^k(t-u)^{n-k}}{t^n} \qquad \square$$

---

> **Theorem 4.5.5 (Joint distribution for two processes).** Let $X_1(t), X_2(t)$ be independent Poisson processes with rates $\lambda_1, \lambda_2$. Given $X_1(t)+X_2(t)=n$:
> $$\mathbb{P}[X_1(t)=k \mid X_1(t)+X_2(t)=n] = \binom{n}{k}\left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^k\left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k} \tag{4.12}$$

**Intuition.** Each of the $n$ combined events independently belongs to process 1 with probability $p_1 = \lambda_1/(\lambda_1+\lambda_2)$ — the fraction of the total rate contributed by process 1. So $X_1(t) \mid X_1(t)+X_2(t)=n$ is $\mathrm{Binomial}(n, p_1)$.

**Proof.** Apply the definition of conditional probability:

$$\mathbb{P}[X_1(t)=k \mid X_1(t)+X_2(t)=n] = \frac{\mathbb{P}[X_1(t)=k,\, X_2(t)=n-k]}{\mathbb{P}[X_1(t)+X_2(t)=n]}$$

$$= \frac{e^{-\lambda_1 t}(\lambda_1 t)^k/k! \cdot e^{-\lambda_2 t}(\lambda_2 t)^{n-k}/(n-k)!}{e^{-(\lambda_1+\lambda_2)t}[(\lambda_1+\lambda_2)t]^n/n!} = \binom{n}{k}\left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^k\left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k} \qquad \square$$

---

> **Theorem 4.5.6 (Combined theorem — two processes, sub-interval).** Let $X_1(t), X_2(t)$ be independent Poisson processes with rates $\lambda_1, \lambda_2$. Fix $0 < s < t$. Given $X_1(t)+X_2(t)=n$:
> $$\mathbb{P}[X_1(s)=k \mid X_1(t)+X_2(t)=n] = \binom{n}{k}\left(\frac{\lambda_1 s}{(\lambda_1+\lambda_2)t}\right)^k\left(\frac{\lambda_1(t-s)+\lambda_2 t}{(\lambda_1+\lambda_2)t}\right)^{n-k}$$

![[Stochastic_Processes_2020_p140_img44.jpeg]]
![[Stochastic_Processes_2020_p140_img45.jpeg]]
*Figure 4.9 — Geometric interpretation: the parameter $\left(\frac{\lambda_1 s}{(\lambda_1+\lambda_2)t}\right)^k$ is the ratio of the small rectangle's area (the event of interest) to the large rectangle's area (the conditioning event).*

**Proof.** Apply the definition of conditional probability:

$$\mathbb{P}[X_1(s)=k \mid X_1(t)+X_2(t)=n] = \frac{\mathbb{P}[X_1(s)=k,\, X_1(t)+X_2(t)=n]}{\mathbb{P}[X_1(t)+X_2(t)=n]}$$

If $X_1(s)=k$ and $X_1(t)+X_2(t)=n$, then the remaining $n-k$ events come from $X_1(t)-X_1(s)$ (process 1 after time $s$) plus $X_2(t)$ (all of process 2). These are independent of $X_1(s)$ (disjoint intervals for process 1, fully independent for process 2), so:

$$\mathbb{P}[X_1(s)=k,\, X_1(t)-X_1(s)+X_2(t)=n-k]$$

All pieces are independent Poisson increments:
- $X_1(s) \sim \mathrm{Poisson}(\lambda_1 s)$
- $X_1(t)-X_1(s) \sim \mathrm{Poisson}(\lambda_1(t-s))$
- $X_2(t) \sim \mathrm{Poisson}(\lambda_2 t)$

The denominator is $\mathrm{Poisson}((\lambda_1+\lambda_2)t)$. Computing the ratio and simplifying yields the binomial formula above. $\square$

---

### 4.5.1 M/G/$\infty$ Queue — Radioactive Decay Example

Consider alpha particles appearing according to a Poisson process of rate $\lambda$. Each particle $k$ arrives at time $W_k$ and exists for a random duration $Y_k$, with $\{Y_k\}$ i.i.d. with distribution $G$. Let $M(t)$ = number of particles existing at time $t$.

![[Stochastic_Processes_2020_p141_img46.jpeg]]
*Figure 4.10 — Particle $k$ (created at $W_k \leq t$) still exists at time $t$ iff $W_k + Y_k \geq t$.*

**Goal:** find the distribution of $M(t)$.

**Step 1 — Condition on $X(t) = n$.** Particle $k$ still exists at $t$ iff $W_k + Y_k \geq t$. The count $M(t)$ is the sum of indicator variables:
$$M(t) = \sum_{k=1}^{n} \mathbf{1}\{W_k + Y_k \geq t\}$$

**Step 2 — Replace $W_k$ with $U_k$.** The expression $\mathbf{1}\{W_k + Y_k \geq t\}$ is symmetric in $k$ (does not depend on the ordering of arrival times). By Theorem 4.5.3, we can replace the ordered $W_k$ with i.i.d. uniforms $U_k \sim \mathrm{Uniform}(0,t)$:

$$\mathbb{P}[M(t)=m \mid X(t)=n] = \mathbb{P}\!\left[\sum_{k=1}^n \mathbf{1}\{U_k + Y_k \geq t\} = m\right]$$

**Step 3 — Identify as Binomial.** Each indicator $\mathbf{1}\{U_k + Y_k \geq t\}$ is i.i.d. Bernoulli with success probability:

$$p = \mathbb{P}[U_k + Y_k \geq t] = \frac{1}{t}\int_0^t \mathbb{P}[Y_k \geq t - u]\,\mathrm{d}u = \frac{1}{t}\int_0^t [1-G(t-u)]\,\mathrm{d}u = \frac{1}{t}\int_0^t [1-G(z)]\,\mathrm{d}z$$

The sum of $n$ i.i.d. Bernoulli$(p)$ indicators is $\mathrm{Binomial}(n, p)$:
$$\mathbb{P}[M(t)=m \mid X(t)=n] = \binom{n}{m}p^m(1-p)^{n-m}$$

**Step 4 — Remove the conditioning.** Marginalise over $X(t) \sim \mathrm{Poisson}(\lambda t)$. Since a Binomial$(N, p)$ where $N \sim \mathrm{Poisson}(\lambda t)$ yields $\mathrm{Poisson}(\lambda t \cdot p)$ (Theorem 4.1.2):

$$\mathbb{P}[M(t)=m] = \sum_{n=m}^{\infty}\binom{n}{m}p^m(1-p)^{n-m}\frac{(\lambda t)^n e^{-\lambda t}}{n!} = \frac{e^{-\lambda p t}(\lambda p t)^m}{m!}$$

So $M(t) \sim \mathrm{Poisson}(\lambda p t)$ with mean:

$$\lambda pt = \lambda\int_0^t [1-G(z)]\,\mathrm{d}z$$

**Long-run behaviour.** As $t \to \infty$:
$$\lambda pt \to \lambda\int_0^{\infty}[1-G(z)]\,\mathrm{d}z = \frac{\lambda}{\mu}$$

where $\mu = \mathbb{E}[Y_k]$ is the mean lifetime (using $\mathbb{E}[Y] = \int_0^\infty \mathbb{P}[Y > z]\,\mathrm{d}z = \int_0^\infty [1-G(z)]\,\mathrm{d}z$). The stationary mean number of particles is $\lambda/\mu$ — consistent with Little's Law.

---

### 4.5.2 Shot Noise Process

**Model.** Electrons arrive at an anode according to a Poisson process $\{X(t)\}$ of rate $\lambda$. Each electron $k$ (arriving at $W_k$) produces a current pulse with impulse response $h(\cdot)$. The total current at time $t$ is:
$$I(t) = \sum_{k=1}^{X(t)} h(t - W_k)$$

![[Stochastic_Processes_2020_p144_img47.jpeg]]
*Figure 4.11 — Total current = superposition of shifted pulse responses, one per electron arrival.*

**Computing $\mathbb{P}[I(t) \leq x]$.** Condition on $X(t) = n$, apply Theorem 4.5.3 to replace ordered $W_k$ with i.i.d. uniforms $U_k$ (valid since $h(t-W_k)$ is symmetric in $k$), then collect back into a random sum:

$$\mathbb{P}[I(t) \leq x] = \mathbb{P}\!\left[\sum_{k=1}^{X(t)} h(U_k) \leq x\right]$$

where $U_k \overset{\text{i.i.d.}}{\sim} \mathrm{Uniform}(0,t)$ and $X(t) \sim \mathrm{Poisson}(\lambda t)$ are independent.

**Mean.** Using the formula $\mathbb{E}[\text{random sum}] = \mathbb{E}[N]\cdot\mathbb{E}[\text{term}]$:

$$\mathbb{E}[I(t)] = \mathbb{E}[X(t)]\cdot\mathbb{E}[h(U_k)] = \lambda t \cdot \frac{1}{t}\int_0^t h(u)\,\mathrm{d}u = \lambda\int_0^t h(u)\,\mathrm{d}u$$

**Variance.** Using $\mathrm{Var}[\text{random sum}] = \mathbb{E}[N]\cdot\mathrm{Var}[\text{term}] + \mathrm{Var}[N]\cdot(\mathbb{E}[\text{term}])^2$ and the fact that $\mathbb{E}[N] = \mathrm{Var}[N] = \lambda t$ (Poisson):

$$\mathrm{Var}[I(t)] = \lambda t\,\mathrm{Var}[h(U_k)] + \lambda t\,(\mathbb{E}[h(U_k)])^2 = \lambda t\,\mathbb{E}[(h(U_k))^2] = \lambda\int_0^t h^2(u)\,\mathrm{d}u$$

**Long-run behaviour.** As $t \to \infty$ (integrating beyond the pulse duration), only the total area under each pulse matters: $\mathbb{E}[I] \to \lambda\int_0^\infty h(u)\,\mathrm{d}u$ and similarly for the variance. Different pulse shapes with the same area produce the same long-run mean current.

---

## 4.6 Binomial Theorem — Direct Proof and Dual Version

### Direct Proof

> **Theorem 4.6.1 (Binomial theorem).** For a Poisson process of rate $\lambda$, $0 < u < t$, $0 \leq k \leq n$:
> $$\mathbb{P}[X(u)=k \mid X(t)=n] = \binom{n}{k}\left(\frac{u}{t}\right)^k\left(1-\frac{u}{t}\right)^{n-k}$$

This is the same as Theorem 4.5.4, but the direct proof below is important for exam purposes.

**Proof.** By definition of conditional probability, using the event $X(t) = n \Leftrightarrow X(u) = k \text{ and } X(t)-X(u) = n-k$:

$$\mathbb{P}[X(u)=k \mid X(t)=n] = \frac{\mathbb{P}[X(u)=k,\, X(t)-X(u)=n-k]}{\mathbb{P}[X(t)=n]}$$

![[Stochastic_Processes_2020_p146_img48.jpeg]]
*Figure 4.12 — Intervals $(0,u)$ and $(u,t)$ are disjoint (increments independent), but $(0,u)$ and $(0,t-u)$ overlap — stationarity allows us to substitute $X(t)-X(u)$ with $X(t-u)$ only after factorising.*

**Critical subtlety:** $X(t)-X(u)$ and $X(u)$ refer to disjoint intervals, so they are **independent**. After factorising, we use stationarity to identify $X(t)-X(u) \overset{d}{=} X(t-u)$. We must factorise *before* applying stationarity — $X(u)$ and $X(t-u)$ overlap and are not independent.

$$= \frac{\mathbb{P}[X(u)=k]\cdot\mathbb{P}[X(t)-X(u)=n-k]}{\mathbb{P}[X(t)=n]} = \frac{e^{-\lambda u}(\lambda u)^k/k!\cdot e^{-\lambda(t-u)}[\lambda(t-u)]^{n-k}/(n-k)!}{e^{-\lambda t}(\lambda t)^n/n!}$$

$$= \binom{n}{k}\frac{u^k(t-u)^{n-k}}{t^n} \qquad \square$$

---

### Dual Version (Future Interval)

Now condition on the *past* and ask about the *future*: $\mathbb{P}[X(s)=k \mid X(t)=n]$ where $0 < t < s$ and $k \geq n$.

This asks: given $n$ arrivals by time $t$, what is the probability of $k$ arrivals by the later time $s$?

$$\mathbb{P}[X(s)=k \mid X(t)=n] = \frac{\mathbb{P}[X(t)=n,\, X(s)-X(t)=k-n]}{\mathbb{P}[X(t)=n]}$$

Since $(0,t)$ and $(t,s)$ are disjoint, $X(t)$ and $X(s)-X(t)$ are independent. Cancelling $\mathbb{P}[X(t)=n]$:

$$= \mathbb{P}[X(s)-X(t)=k-n] \overset{\text{stationary}}{=} \mathbb{P}[X(s-t)=k-n] = \frac{e^{-\lambda(s-t)}[\lambda(s-t)]^{k-n}}{(k-n)!}$$

**Interpretation:** Given $n$ arrivals by time $t$, the additional arrivals in $(t,s]$ are independent of the history and follow $\mathrm{Poisson}(\lambda(s-t))$ — a direct consequence of the memoryless (Markov) property of the Poisson process.

---

## Exercises

### Exercise 4.6.1 (Exam — June 27, 2016)

Two independent Poisson processes: $X_1(t)$ with $\lambda_1 = 0.5$/unit time, $X_2(t)$ with $\lambda_2 = 1$/unit time.

**Part 1: $P[X_1(2)=1 \mid X_1(3)=2]$ and $P[X_1(3)=2 \mid X_1(2)=1]$**

*Forward (large given small)*: By Theorem 4.6.1, given 2 arrivals in $(0,3)$, the number in the smaller interval $(0,2)$ is $\mathrm{Binomial}(2, 2/3)$:
$$P[X_1(2)=1 \mid X_1(3)=2] = \binom{2}{1}\left(\frac{2}{3}\right)^1\left(\frac{1}{3}\right)^1 = \frac{4}{9} \approx 0.44$$

*Backward (small given large)*: By the dual version, given 1 arrival in $(0,2)$, arrivals in $(2,3)$ are independent $\mathrm{Poisson}(\lambda_1 \cdot 1) = \mathrm{Poisson}(0.5)$:
$$P[X_1(3)=2 \mid X_1(2)=1] = P[X_1(3)-X_1(2)=1] = P[X_1(1)=1] = 0.5\,e^{-0.5} \approx 0.303$$

**Part 2: $P[X_1(1)=1 \mid X_1(2)+X_2(2)=3]$ and $P[X_1(2)+X_2(2)=3 \mid X_1(1)=1]$**

*Forward*: By Theorem 4.5.6 (geometric interpretation: ratio of area $\lambda_1 \cdot 1 = 0.5$ to total area $(\lambda_1+\lambda_2)\cdot 2 = 3$, so $p = 0.5/3 = 1/6$):
$$P[X_1(1)=1 \mid X_1(2)+X_2(2)=3] = \binom{3}{1}\left(\frac{1}{6}\right)^1\left(\frac{5}{6}\right)^2 = \frac{25}{72} \approx 0.347$$

*Backward*: Given $X_1(1)=1$, the remaining arrivals $\{X_2(2) + (X_1(2)-X_1(1))\}$ come from a Poisson with parameter $\lambda_2 \cdot 2 + \lambda_1 \cdot 1 = 2 + 0.5 = 2.5$:
$$P[X_1(2)+X_2(2)=3 \mid X_1(1)=1] = P[X_2(2)+X_1(2)-X_1(1)=2] = \frac{(2.5)^2 e^{-2.5}}{2!} \approx 0.257$$

**Part 3: $P[X_1(2)+X_2(2)=3 \mid X_1(3)=0]$ and $P[X_1(2)+X_2(2)=3 \mid X_1(3)=1]$**

*Condition $X_1(3)=0$*: Process 1 has no arrivals in $(0,3)$ — in particular none in $(0,2)$. All 3 arrivals must come from $X_2(2) \sim \mathrm{Poisson}(2)$:
$$P[X_1(2)+X_2(2)=3 \mid X_1(3)=0] = P[X_2(2)=3] = \frac{2^3 e^{-2}}{6} = \frac{4}{9}e^{-2} \approx 0.060$$

*Condition $X_1(3)=1$*: The single $X_1$ arrival can be in $(0,2)$ or $(2,3)$. Condition on $X_1(2) \in \{0,1\}$ (the only possible values), using the binomial theorem ($p=2/3$):

![[Stochastic_Processes_2020_p150_img49.jpeg]]
*Figure 4.13 — Graph for point (c) of Exercise 4.6.1.*

$$P[X_1(2)+X_2(2)=3 \mid X_1(3)=1] = \sum_{i=0}^{1} P[X_2(2)=3-i]\cdot P[X_1(2)=i \mid X_1(3)=1]$$

$$= P[X_2(2)=3]\cdot\frac{1}{3} + P[X_2(2)=2]\cdot\frac{2}{3}$$

$$= \frac{2^3 e^{-2}}{6}\cdot\frac{1}{3} + \frac{2^2 e^{-2}}{2}\cdot\frac{2}{3} = \frac{4}{9}e^{-2} + \frac{4}{3}e^{-2} = \frac{16}{9}e^{-2} \approx 0.24$$

---

### Exercise 4.6.2 — Cyclic Markov Chain

A Markov chain on states $\{0,1,2,3,4,5\}$ has transition matrix:

| | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | $\alpha_1$ | $\alpha_2$ | $\alpha_3$ | $\alpha_4$ | $\alpha_5$ | $\alpha_6$ |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 0 | 1 | 0 | 0 | 0 | 0 |
| 3 | 0 | 0 | 1 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 | 1 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 1 | 0 |

with $\alpha_i \geq 0$ and $\sum_{i=1}^6 \alpha_i = 1$.

![[Stochastic_Processes_2020_p151_img50.jpeg]]
*Figure 4.14 — Transition diagram for Exercise 4.6.2. The chain cycles: state $k$ always moves to $k-1$, and state 0 jumps to state $j$ with probability $\alpha_{j+1}$.*

**Find the limiting probability $\pi_0$.**

The chain is irreducible (all states communicate through state 0). The period of state 0 is $d(0) = 1$ if $\alpha_1 > 0$ (the chain can return in 1 step), or we must analyse further.

Using the Basic Limit Theorem: $\pi_0 = 1/m_0$ where $m_0$ is the mean return time to state 0.

Starting from state 0, the chain must visit exactly $j$ states before returning ($j = 0$ if it returns to 0 directly, i.e. with probability $\alpha_1$; $j=1$ if it goes $0 \to 1 \to 0$ in 2 steps with probability $\alpha_2$; etc.). The return time is $T = j + 1$ with probability $\alpha_{j+1}$.

$$m_0 = \mathbb{E}[T] = \sum_{j=0}^{5}(j+1)\alpha_{j+1} = 1\cdot\alpha_1 + 2\cdot\alpha_2 + 3\cdot\alpha_3 + 4\cdot\alpha_4 + 5\cdot\alpha_5 + 6\cdot\alpha_6$$

Therefore:
$$\boxed{\pi_0 = \frac{1}{m_0} = \frac{1}{\sum_{j=1}^{6} j\,\alpha_j}}$$

The stationary probabilities of the other states can be found similarly: state $k$ is only reachable from state $k+1$ (for $k < 5$) or directly from state 0 (for state $j$ with probability $\alpha_{j+1}$), and the stationary equations give $\pi_k = \pi_0 \sum_{j=k}^5 \alpha_{j+1}$ for $k \geq 1$.
