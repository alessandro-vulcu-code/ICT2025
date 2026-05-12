# Chapter 3 — Long Run Behaviour of Markov Chains

## Table of Contents

- [[#Regular Markov Chains|Regular Markov Chains]]
  - [[#Interpretation of the Limiting Distribution|Interpretation of the Limiting Distribution]]
- [[#Non-Regular Markov Chains|Non-Regular Markov Chains]]
- [[#Classification of States|Classification of States]]
  - [[#Accessibility and Communication|Accessibility and Communication]]
  - [[#Periodicity|Periodicity]]
  - [[#Recurrence|Recurrence]]
  - [[#Fubini's Theorem and Corollary|Fubini's Theorem and Corollary]]
- [[#Basic Limit Theorem of Markov Chains|Basic Limit Theorem of Markov Chains]]
  - [[#Mean Return Time and State Classification|Mean Return Time and State Classification]]
  - [[#Theorem 3.4.2 — Stationary Distribution (Infinite State Space)|Theorem 3.4.2 — Stationary Distribution (Infinite State Space)]]
  - [[#Stationary vs Limiting Distribution|Stationary vs Limiting Distribution]]
  - [[#Random Walk Stationary Distribution|Random Walk Stationary Distribution]]
  - [[#Success Runs Recurrence Analysis|Success Runs Recurrence Analysis]]
  - [[#Example 8 — Recurrence of G/M/1 Queue|Example 8 — Recurrence of G/M/1 Queue]]
  - [[#Periodic Generalization|Periodic Generalization]]
- [[#Reducible Markov Chains|Reducible Markov Chains]]
  - [[#Another Behaviour of Infinite Markov Chains|Another Behaviour of Infinite Markov Chains]]
  - [[#Finite Markov Chains — Positive Recurrence Lemmas|Finite Markov Chains — Positive Recurrence Lemmas]]
- [[#Summary Table|Summary Table]]

---

## Regular Markov Chains

> [!Important] Definition — Regular Markov Chain
> A Markov chain is **regular** if:
> 1. It has a **finite** number of states $0, 1, \ldots, N$.
> 2. There exists an integer $k$ such that $(\mathbf{P}^k)_{ij} > 0$ for all $i,j$, i.e. all $k$-step transition probabilities are strictly positive.
>
> Consequence: given enough time, the system can reach any state from any other state. This guarantees the existence of a unique limiting probability distribution.

> [!Important] Theorem — Limiting Distribution of a Regular Markov Chain
> **Statement:** Let $\mathbf{P}$ be a regular transition probability matrix on states $0,1,\ldots,N$. Then there exists a unique limiting distribution $\boldsymbol{\pi}=(\pi_0,\pi_1,\ldots,\pi_N)^T$ such that:
>
> $$\lim_{n\to\infty} P^{(n)}_{ij} = \pi_j > 0 \quad \forall j=0,1,\ldots,N$$
>
> This limit is **independent of the initial state** $i$. The vector $\boldsymbol{\pi}$ is the unique nonnegative solution of the **stationarity equations**:
>
> $$\pi_j = \sum_{k=0}^N \pi_k P_{kj} \qquad j=0,1,\ldots,N \tag{3.1}$$
>
> subject to the normalization:
>
> $$\sum_{k=0}^N \pi_k = 1 \tag{3.2}$$
>
> **Proof:**
>
> *(Note: system (3.1) is homogeneous — if $\boldsymbol{\pi}_0$ is a solution, so is $a\boldsymbol{\pi}_0$ for any $a\neq 0$. Normalization (3.2) makes the solution unique and ensures $\boldsymbol{\pi}$ is a proper distribution.)*
>
> **Part 1 — Existence.**
>
> Since the chain is regular, the limit $\lim_{n\to\infty}P^{(n)}_{ij}=\pi_j$ exists. Normalization of $\boldsymbol{\pi}$ follows from:
> $$\sum_{j=0}^N P^{(n)}_{ij} = 1 \quad \forall n \implies \lim_{n\to\infty}\sum_{j=0}^N P^{(n)}_{ij} = 1 = \sum_{j=0}^N \pi_j$$
>
> To verify (3.1), start from the Chapman-Kolmogorov relation:
> $$P^{(n)}_{ij} = \sum_{k=0}^N P^{(n-1)}_{ik} P_{kj}$$
> Take $n\to\infty$; since $N$ is finite the limit and sum can be exchanged:
> $$\pi_j = \sum_{k=0}^N \pi_k P_{kj}$$
>
> **Part 2 — Uniqueness.**
>
> Suppose $\mathbf{x}$ is another solution: $x_j = \sum_k x_k P_{kj}$, $\sum_k x_k = 1$. In matrix form $\mathbf{x}=\mathbf{x}\mathbf{P}$. Iterating:
> $$\mathbf{x} = \mathbf{x}\mathbf{P}^{(n)} \Leftrightarrow x_l = \sum_{k=0}^N x_k P^{(n)}_{kl}$$
> Taking $n\to\infty$ and using $\sum_k x_k = 1$:
> $$x_l = \lim_{n\to\infty}\sum_{k=0}^N x_k P^{(n)}_{kl} = \underbrace{\sum_{k=0}^N x_k}_{1}\,\pi_l = \pi_l$$
> so $\boldsymbol{x}=\boldsymbol{\pi}$, proving uniqueness. $\square$
>
> **Intuition:** Regularity guarantees that no state becomes permanently unreachable. Over time the system "forgets" its initial state; the fraction of time spent in each state converges to the unique stationary vector $\boldsymbol{\pi}$.

---

### Interpretation of the Limiting Distribution

The limiting distribution $\pi_j$ has two equivalent interpretations:

1. **Long-run probability:** $\pi_j = \lim_{n\to\infty}\mathbb{P}\{X_n=j \mid X_0=i\}$ — the probability of finding the system in state $j$ after a long time, independent of initial state $i$.

2. **Long-run fraction of time:** $\pi_j$ is the fraction of time the system spends in state $j$.

**Formal derivation of interpretation 2:**

The mean fraction of visits to state $j$ over a run of length $m$ is:

$$\mathbb{E}\!\left[\frac{1}{m}\sum_{k=0}^{m-1}\mathbf{1}\{X_k=j\}\,\Big|\,X_0=i\right] = \frac{1}{m}\sum_{k=0}^{m-1}P^{(k)}_{ij}$$

Since $\lim_{n\to\infty}P^{(n)}_{ij}=\pi_j$, and a convergent sequence has the same limit as its running averages:

$$\lim_{m\to\infty}\frac{1}{m}\sum_{k=0}^{m-1}P^{(k)}_{ij} = \pi_j$$

**Application — Long-run cost:** If each visit to state $j$ incurs cost $c_j$, then the long-run mean cost per unit time is:

$$C = \sum_{j=0}^N \pi_j c_j$$

---

## Non-Regular Markov Chains

Not all Markov chains are regular. When $\mathbf{P}^n$ always contains some zero entries, the limiting distribution may:
- Not exist at all.
- Depend on the initial state (multiple limiting distributions).
- Exist and be independent of initial state, but have $\pi_j=0$ for some $j$.

![[Stochastic_Processes_2020_p70_img18.jpeg]]
*(a) — Two isolated classes, limiting distribution depends on initial state.*

![[Stochastic_Processes_2020_p70_img19.jpeg]]
*(b) — Periodic chain: no limiting distribution exists.*

![[Stochastic_Processes_2020_p70_img20.jpeg]]
*(c) — Unique limiting distribution exists but $\pi_0=0$: state 0 is never visited long-run.*

*Figure 3.1 — Examples of non-regular Markov chains.*

**Three canonical examples:**

1. $\mathbf{P} = \begin{pmatrix}1&0\\0&1\end{pmatrix} = \mathbf{I}$: $\mathbf{P}^n=\mathbf{P}$ $\forall n$. Chain stays at initial state. Limit exists but depends on $i$; some states never visited.

2. $\mathbf{P} = \begin{pmatrix}0&1\\1&0\end{pmatrix}$: $\mathbf{P}^n = \mathbf{P}$ for $n$ odd, $\mathbf{I}$ for $n$ even. $\mathbf{P}^n$ oscillates — **no limiting distribution**.

3. $\mathbf{P} = \begin{pmatrix}1/2&1/2\\0&1\end{pmatrix}$: $\mathbf{P}^n = \begin{pmatrix}(1/2)^n & 1-(1/2)^n\\0&1\end{pmatrix}$. Limit exists and is independent of $i$, but:
$$\lim_{n\to\infty}\mathbf{P}^n = \begin{pmatrix}0&1\\0&1\end{pmatrix}$$
State 0 has $\pi_0=0$ — not visited long-run.

---

## Classification of States

### Accessibility and Communication

> [!Important] Definitions — Accessibility, Communication, Irreducibility
> - State $j$ is **accessible** from $i$ if $P^{(n)}_{ij}>0$ for some $n\geq 0$.
> - States $i$ and $j$ **communicate** ($i\leftrightarrow j$) if each is accessible from the other.
> - **Communication is an equivalence relation** (reflexive, symmetric, transitive), partitioning all states into **equivalence classes**.
>
> **Proof of transitivity:** if $i\leftrightarrow j$ and $j\leftrightarrow k$, then $\exists n,m$ s.t. $P^{(n)}_{ij}>0$, $P^{(m)}_{jk}>0$. Then:
> $$P^{(n+m)}_{ik} = \sum_r P^{(n)}_{ir}P^{(m)}_{rk} \geq P^{(n)}_{ij}P^{(m)}_{jk} > 0$$
> so $i\to k$ is possible; similarly $k\to i$, proving $i\leftrightarrow k$. $\square$
>
> A chain is **irreducible** if it consists of a single communication class (all states communicate). Otherwise it is **reducible**.
>
> Different classes can be connected only by **one-way transitions**: if the system leaves class $A$ for class $B$, it cannot return to $A$.

**Example — block-diagonal reducible chain:**

$$\mathbf{P} = \begin{vmatrix}\frac{1}{2}&\frac{1}{2}&0&0&0\\\frac{1}{4}&\frac{3}{4}&0&0&0\\0&0&0&1&0\\0&0&\frac{1}{2}&0&\frac{1}{2}\\0&0&0&1&0\end{vmatrix} = \begin{vmatrix}\mathbf{P_1}&\mathbf{0}\\\mathbf{0}&\mathbf{P_2}\end{vmatrix}$$

Two isolated classes $\{0,1\}$ and $\{2,3,4\}$.

**Example — random walk with absorbing boundaries (3.4):**

$$\mathbf{P} = \begin{bmatrix}1&0&0&\cdots&0&0\\q&0&p&\cdots&0&0\\0&q&0&\cdots&0&0\\\vdots&&&&&\vdots\\0&\cdots&\cdots&\cdots&q&0&p\\0&\cdots&\cdots&\cdots&0&0&1\end{bmatrix} \tag{3.4}$$

Three classes: $A=\{0\}$, $B=\{1,\ldots,a-1\}$ (transient), $C=\{a\}$. One-way transitions $B\to A$ and $B\to C$ only.

---

### Periodicity

> [!Important] Definition — Period of a State
> The **period** $d(i)$ of state $i$ is the greatest common divisor of all integers $n\geq 1$ for which $P^{(n)}_{ii}>0$:
> $$d(i) = \gcd\{n\geq 1 : P^{(n)}_{ii}>0\}$$
> If the system never returns to $i$: $d(i)=0$ (by convention). If $P_{ii}>0$: $d(i)=1$.
>
> A state is **aperiodic** if $d(i)=1$.

**Canonical periodic example** — cyclic chain on $N$ states:

$$\mathbf{P} = \begin{pmatrix}0&1&0&\cdots&0\\0&0&1&\cdots&0\\\vdots&&&&\vdots\\1&0&0&\cdots&0\end{pmatrix}$$

Here $d(i)=N$ for every $i=0,\ldots,N-1$.

![[Stochastic_Processes_2020_p73_img21.jpeg]]
*Figure 3.2 — Block diagram for a cyclic Markov chain with $N=6$. Each state has period 6.*

**Another example (3.5):**

$$\mathbf{P} = \bordermatrix{&0&1&2&3\\0&0&1&0&0\\1&0&0&1&0\\2&0&0&0&1\\3&1&0&\frac{1}{2}&0} \tag{3.5}$$

Starting from 0, return to 0 is possible after 4, 6, 8, $\ldots$ steps → $d(0)=2$.

![[Stochastic_Processes_2020_p74_img22.jpeg]]
*Figure 3.3 — Block diagram for chain (3.5). State 0 has period 2.*

> [!Important] Theorem 3.3.1 — Period is a Class Property
> **Statement:** If $i\leftrightarrow j$ then $d(i)=d(j)$.
>
> **Proof:**
> Let $S_i=\{s>0:P^{(s)}_{ii}>0\}$ so $d(i)=\gcd(S_i)$.
>
> Since $i\leftrightarrow j$, $\exists m,n$ s.t. $P^{(m)}_{ij}>0$, $P^{(n)}_{ji}>0$. For any $s\in S_i$, the path $j\xrightarrow{n}i\xrightarrow{s}i\xrightarrow{m}j$ has positive probability:
> $$P^{(n+s+m)}_{jj} \geq P^{(n)}_{ji}P^{(s)}_{ii}P^{(m)}_{ij} > 0$$
> Similarly $P^{(n+2s+m)}_{jj}>0$. So both $n+s+m$ and $n+2s+m$ belong to $S_j$. By definition of $d(j)$:
> $$n+s+m = k_1 d(j); \quad n+2s+m = k_2 d(j)$$
> Subtracting: $s=(k_2-k_1)d(j)$, so $s$ is a multiple of $d(j)$ for every $s\in S_i$.
> This means $d(j)$ is a common divisor of $S_i$, hence $d(j)\leq d(i)$.
> Exchanging $i\leftrightarrow j$ gives $d(i)\leq d(j)$. Therefore $d(i)=d(j)$. $\square$
>
> ![[Stochastic_Processes_2020_p75_img23.jpeg]]
> *Figure 3.4 — If $d(i)=3$, all paths $i\to i$ have length divisible by 3. For any communicating $j$, $d(j)$ can be neither smaller (would create a path $i\to i$ of non-multiple-of-3 length) nor larger (two paths of lengths $n+m$ and $n+m+3$ have gcd $\leq 3$). Hence $d(j)=3$.*

---

### Recurrence

> [!Important] Definition — First Return Time and Recurrence
> The **first return time** to state $i$ is:
> $$f^{(n)}_{ii} = \mathbb{P}\{\theta_{ii}=n\} = \mathbb{P}\{X_n=i,\,X_\nu\neq i,\,\nu=1,\ldots,n-1\mid X_0=i\} \qquad n\geq 1$$
>
> The total probability of ever returning to $i$:
> $$f_{ii} = \sum_{n=0}^\infty f^{(n)}_{ii}$$
>
> - **Recurrent state:** $f_{ii}=1$ — return to $i$ is guaranteed (with probability 1).
> - **Transient state:** $f_{ii}<1$ — positive probability of never returning.

**Behaviour of transient states:** The probability of returning at least $k$ times is $(f_{ii})^k$, so the number of returns $M$ has a geometric distribution:
$$\mathbb{P}\{M\geq k\mid X_0=i\} = (f_{ii})^k, \qquad \mathbb{E}[M\mid X_0=i] = \frac{f_{ii}}{1-f_{ii}} < \infty$$

**Behaviour of recurrent states:** $f_{ii}=1$ implies the chain returns infinitely often; $M$ is an **improper random variable**:
$$\lim_{x\to\infty}\mathbb{P}[M\leq x] = 0 \neq 1$$
since $\mathbb{P}[M=\infty]=1$.

> [!Important] Definition — Improper Random Variable
> An **improper random variable** $X$ satisfies:
> $$\lim_{x\to\infty}\mathbb{P}[X>x] = P_\infty > 0$$
> interpreted as $\mathbb{P}[X=\infty]=P_\infty$. For non-negative improper r.v.: $\mathbb{E}[X]=\infty$.

![[Stochastic_Processes_2020_p76_img24.jpeg]]
*Figure 3.5 — CDF of a proper r.v. (reaches 1 in the limit) vs an improper r.v. (asymptotes below 1, reflecting positive probability of infinite value).*

> [!Important] Theorem 3.3.2 — Recurrence Criterion
> **Statement:**
> $$\text{state } i \text{ is recurrent} \iff \sum_{n=1}^\infty P^{(n)}_{ii} = \infty$$
> Equivalently, state $i$ is transient $\iff \sum_{n=1}^\infty P^{(n)}_{ii} < \infty$.
>
> **Proof:**
> Let $M = \sum_{n=1}^\infty \mathbf{1}\{X_n=i\}$ (total visits to $i$). By linearity of expectation (justified via Fubini for non-negative r.v.):
> $$\mathbb{E}[M\mid X_0=i] = \sum_{n=1}^\infty P^{(n)}_{ii}$$
> *Case 1 — transient ($f_{ii}<1$):*
> $$\sum_{n=1}^\infty P^{(n)}_{ii} = \mathbb{E}[M\mid X_0=i] = \sum_{k=1}^\infty (f_{ii})^k = \frac{f_{ii}}{1-f_{ii}} < \infty$$
> *Case 2 — recurrent ($f_{ii}=1$):*
> $$\sum_{n=1}^\infty P^{(n)}_{ii} = \sum_{k=1}^\infty (f_{ii})^k = \infty \qquad\square$$

---

### Fubini's Theorem and Corollary

> [!Important] Fubini's Theorem (exchange of sums/expectations)
> **Statement:** For a function $f(x,y)$:
> $$\sum_x\sum_y f(x,y) = \sum_y\sum_x f(x,y)$$
> is valid if any one of the double sums converges **absolutely** ($\sum\sum|f(x,y)|<\infty$).
>
> If $\sum\sum|f|=\infty$, the exchange may fail because $f=f_+-f_-$ leads to $\infty-\infty$ (indeterminate).
>
> **Key result for non-negative r.v.:** For $X_i\geq 0$:
> $$\mathbb{E}\!\left[\sum_{i=0}^\infty X_i\right] = \sum_{i=0}^\infty \mathbb{E}[X_i]$$
> always holds (both sides may be $\infty$, but they share the same value).
>
> **Proof:** If $\sum\mathbb{E}[X_i]<\infty$: Fubini directly applies. If $\sum\mathbb{E}[X_i]=\infty$: for any $M$, $\mathbb{E}[\sum_i X_i]\geq\mathbb{E}[\sum_{i=0}^M X_i]=\sum_{i=0}^M\mathbb{E}[X_i]$; since the lower bound diverges, so does the left side.
>
> *(This justifies exchanging $\mathbb{E}$ and $\sum$ in the proof of Theorem 3.3.2 — the indicator $\mathbf{1}\{X_n=i\}$ is non-negative.)*

> [!Important] Corollary — Recurrence is a Class Property
> **Statement:** If $i\leftrightarrow j$ and $i$ is recurrent, then $j$ is recurrent.
>
> **Proof:**
> Since $i\leftrightarrow j$, $\exists m,n\geq 1$ s.t. $P^{(n)}_{ij}>0$ and $P^{(m)}_{ji}>0$.
>
> For any $\nu\geq 0$, the path $j\xrightarrow{m}i\xrightarrow{\nu}i\xrightarrow{n}j$ gives:
> $$P^{(m+n+\nu)}_{jj} \geq P^{(m)}_{ji}P^{(\nu)}_{ii}P^{(n)}_{ij}$$
> Summing over $\nu$:
> $$\sum_{\nu=0}^\infty P^{(m+n+\nu)}_{jj} \geq P^{(m)}_{ji}P^{(n)}_{ij}\sum_{\nu=0}^\infty P^{(\nu)}_{ii} = \infty$$
> (since $i$ is recurrent and $P^{(m)}_{ji},P^{(n)}_{ij}>0$). Since the shifted sum $\sum P^{(m+n+\nu)}_{jj}$ diverges, a fortiori $\sum_\nu P^{(\nu)}_{jj}=\infty$, so $j$ is recurrent. $\square$

---

## Basic Limit Theorem of Markov Chains

### Mean Return Time and State Classification

For a recurrent state $i$, define the **first return time** $R_i = \min\{n\geq 1 : X_n=i\}$ with distribution $f^{(n)}_{ii}=\mathbb{P}\{R_i=n\mid X_0=i\}$.

The **mean return time** is:
$$m_i = \mathbb{E}[R_i\mid X_0=i] = \sum_{n=1}^\infty n f^{(n)}_{ii}$$

Since $i$ is recurrent, $R_i$ is finite-valued (the system returns with probability 1). However, $m_i$ may still be infinite if $f^{(n)}_{ii}$ decreases too slowly.

> [!Important] Theorem 3.4.1 — Basic Limit Theorem
> **Statement:** For a recurrent, irreducible, **aperiodic** Markov chain:
> $$\lim_{n\to\infty} P^{(n)}_{ii} = \frac{1}{\sum_{n=1}^\infty n f^{(n)}_{ii}} = \frac{1}{m_i}$$
> Moreover:
> $$\lim_{n\to\infty} P^{(n)}_{ji} = \pi_i = \frac{1}{m_i}$$
> for **all** starting states $j$.
>
> *(Proof referred to a later chapter.)*
>
> **Intuition:** If the system returns to $i$ on average every $m_i$ steps, it spends fraction $1/m_i$ of all time in $i$. The limit is independent of starting state.

Based on finiteness of $m_i$, states are classified:

| Type | $f_{ii}=\sum f^{(n)}_{ii}$ | $\lim_{k\to\infty}\mathbb{P}[M>k]$ | $\mathbb{E}[M]$ | $m_i=\sum nf^{(n)}_{ii}$ | $\pi_i=1/m_i$ |
|---|---|---|---|---|---|
| **Transient** | $<1$ | $0$ | $f_{ii}/(1-f_{ii})<\infty$ | $\infty$ | $0$ |
| **Null Recurrent** | $1$ | $1$ | $\infty$ | $\infty$ | $0$ |
| **Positive Recurrent** | $1$ | $1$ | $\infty$ | $<\infty$ | $>0$ |

*Table 3.1 — $f_{ii}$: probability of returning to $i$; $M$: number of returns; $m_i$: mean inter-return time; $\pi_i$: long-run probability.*

- **Positive recurrent** (strongly ergodic): $m_i<\infty$, $\pi_i>0$, state continues to be visited.
- **Null recurrent** (weakly ergodic): $m_i=\infty$, $\pi_i=0$, return is certain but takes infinite expected time.
- All three are class properties.

---

### Theorem 3.4.2 — Stationary Distribution (Infinite State Space)

> [!Important] Theorem 3.4.2 — Stationary Distribution for Positive Recurrent Aperiodic Class
> **Statement:** In a positive recurrent aperiodic class with states $j\in\mathbb{N}$:
> $$\lim_{n\to\infty}P^{(n)}_{jj} = \pi_j = \sum_{i=0}^\infty \pi_i P_{ij}, \qquad \sum_{i=0}^\infty \pi_i = 1$$
>
> $\boldsymbol{\pi}$ is the unique solution of the **stationarity equations**:
>
> $$\pi_i\geq 0, \quad \sum_{i=0}^\infty\pi_i=1, \quad \pi_j = \sum_{i=0}^\infty \pi_i P_{ij} \quad j\in\mathbb{N} \tag{3.7}$$
>
> **Proof (Existence):**
>
> **Step 1 — $\sum_j\pi_j\leq 1$:**
>
> Row normalization gives $\sum_{j=0}^M P^{(n)}_{ij}\leq 1$ $\forall M$. Take $n\to\infty$ (limit can enter finite sum):
> $$\sum_{j=0}^M\pi_j\leq 1 \quad\forall M \implies \sum_{j=0}^\infty\pi_j\leq 1 \tag{3.8}$$
>
> **Step 2 — $\pi_j\geq\sum_k\pi_k P^{(n)}_{kj}$:**
>
> From $P^{(m+n)}_{ij}\geq\sum_{k=0}^M P^{(m)}_{ik}P^{(n)}_{kj}$, take $m\to\infty$ (finite $M$):
> $$\pi_j\geq\sum_{k=0}^M\pi_k P^{(n)}_{kj} \quad\forall M \implies \pi_j\geq\sum_{k=0}^\infty\pi_k P^{(n)}_{kj} \tag{3.9}$$
>
> **Step 3 — (3.9) is an equality:**
>
> Suppose $\exists j$ s.t. (3.9) holds strictly. Summing over $j$:
> $$\sum_j\pi_j > \sum_j\sum_k\pi_k P^{(n)}_{kj} \geq \sum_{k=0}^M\pi_k\underbrace{\sum_j P^{(n)}_{kj}}_{1} = \sum_{k=0}^M\pi_k$$
> Sending $M\to\infty$: $\sum_j\pi_j > \sum_k\pi_k$ — contradiction. So:
> $$\pi_j = \sum_{k=0}^\infty\pi_k P^{(n)}_{kj}$$
> Setting $n=1$ gives (3.7).
>
> **Step 4 — $\sum_k\pi_k=1$:**
>
> Since $|P^{(n)}_{kj}|\leq 1$ and $\sum_k\pi_k\leq 1$, the limit can be brought inside:
> $$\pi_j = \sum_{k=0}^\infty\pi_k\lim_{n\to\infty}P^{(n)}_{kj} = \left(\sum_{k=0}^\infty\pi_k\right)\pi_j$$
> Since $\pi_j>0$ (chain is positive recurrent): $\sum_k\pi_k=1$. $\square$
>
> **Proof (Uniqueness):**
>
> Let $\mathbf{x}$ solve (3.7). By the same truncation-exchange argument:
> $$x_j\geq\sum_k x_k P^{(n)}_{kj} \quad\forall n$$
> Suppose strict for some $j$; summing gives $\sum x_j>\sum x_k$ — contradiction. So equality holds, and taking $n\to\infty$:
> $$x_j = \left(\sum_k x_k\right)\pi_j = \pi_j \qquad\square$$

---

### Stationary vs Limiting Distribution

A **stationary distribution** $\boldsymbol{\pi}$ satisfies (3.7) but may not be the limiting distribution:
- If a limiting distribution exists, it is always stationary.
- The converse fails: periodic chains may have a stationary distribution but no limiting distribution.

**Counterexample:**
$$\mathbf{P}=\begin{bmatrix}0&1\\1&0\end{bmatrix}$$
Periodic (period 2), no limiting distribution. But $\boldsymbol{\pi}=(1/2,1/2)^T$ satisfies:
$$\begin{pmatrix}\frac{1}{2}&\frac{1}{2}\end{pmatrix}\begin{bmatrix}0&1\\1&0\end{bmatrix}=\begin{pmatrix}\frac{1}{2}&\frac{1}{2}\end{pmatrix}$$

---

### Random Walk Stationary Distribution

Consider the irreducible random walk (period $d=2$, $p_i+q_i=1$):

$$\mathbf{P} = \begin{bmatrix}0&1&0&\cdots\\q_1&0&p_1&\cdots\\0&q_2&0&\cdots\\\vdots&\ddots&\ddots&\ddots\end{bmatrix}$$

The stationarity equation $\boldsymbol{x}=\boldsymbol{x}\mathbf{P}$ gives (for $i>0$):

$$x_i = p_{i-1}x_{i-1} + q_{i+1}x_{i+1} \tag{3.13}$$

with $x_0 = q_1 x_1$ (from the $i=0$ equation).

**Solution by forward substitution:**

$$x_1 = \frac{x_0}{q_1}, \quad x_2 = \frac{p_1 x_0}{q_1 q_2}, \quad x_3 = \frac{p_1 p_2 x_0}{q_1 q_2 q_3}$$

General pattern (with $p_0=1$):

$$x_i = x_0\prod_{k=0}^{i-1}\frac{p_k}{q_{k+1}} \qquad i>0 \tag{3.16}$$

Verification: $p_{i-1}x_{i-1}+q_{i+1}x_{i+1} = \frac{p_{i-1}\cdots p_1}{q_i\cdots q_1}(q_i+p_i) = x_i$ ✓

Normalization fixes $x_0$:

$$x_0 = \left(\sum_{i=0}^\infty\prod_{k=0}^{i-1}\frac{p_k}{q_{k+1}}\right)^{-1} \tag{3.17}$$

The solution exists only if the sum converges. For uniform $p_k\equiv p$, $q_k\equiv q$:
- $p<q$: sum converges → chain is **positive recurrent**.
- $p\geq q$: sum diverges → chain is **not positive recurrent** (transient).

---

### Success Runs Recurrence Analysis

Consider the success runs chain:

$$\mathbf{P} = \begin{pmatrix}p_0&1-p_0&0&0&\cdots\\p_1&0&1-p_1&0&\cdots\\p_2&0&0&1-p_2&\cdots\\\vdots&\ddots&\ddots&\ddots&\ddots\end{pmatrix} \quad (0<p_k<1)$$

![[Stochastic_Processes_2020_p88_img25.jpeg]]
*Figure 3.6 — Block diagram for the success runs chain. From any state, the chain either resets to 0 (prob $p_i$) or advances (prob $1-p_i$).*

Chain is irreducible → all states same type. Focus on state 0. Define first return time $R_0=\min\{n\geq 1:X_n=0\}$.

**Tail probabilities** (only path not returning to 0 after $k$ steps is $0\to 1\to\cdots\to k$):

$$\mathbb{P}\{R_0>k\mid X_0=0\} = \prod_{i=0}^{k-1}(1-p_i) \tag{3.18}$$

**Recurrence criterion:** State 0 is recurrent iff $f_{00}=1$, i.e. $\lim_{k\to\infty}\prod(1-p_i)=0$:

$$\text{state 0 recurrent} \iff \prod_{i=0}^\infty(1-p_i)=0 \iff \sum_{i=0}^\infty p_i = \infty \tag{3.20}$$

(by Lemma 3.4.3 below).

**Mean return time:**

$$m_0 = \sum_{k=0}^\infty\mathbb{P}\{R_0>k\} = 1 + \sum_{k=1}^\infty\prod_{i=0}^{k-1}(1-p_i)$$

**Positive recurrence** requires $m_0<\infty$, i.e. $\sum_{k=1}^\infty\prod_{i=0}^{k-1}(1-p_i)<\infty$ (stricter than (3.20)).

**Stationary distribution** (when positive recurrent):

$$\pi_0 = \frac{1}{m_0} = \frac{1}{1+\sum_{k=1}^\infty\prod_{i=0}^{k-1}(1-p_i)}, \qquad \pi_k = \pi_0\prod_{i=0}^{k-1}(1-p_i) \quad k\geq 1 \tag{3.21}$$

**Special case $p_i\equiv p$:** $\prod(1-p_i)=q^k$, so $m_0=1+\sum_{k=1}^\infty q^k = 1/p$, and $\pi_k=pq^k$.

> [!Important] Lemma 3.4.3 — Infinite Product vs Infinite Sum
> **Statement:** For $0<p_i<1$:
> $$\prod_{i=0}^\infty(1-p_i)=0 \iff \sum_{i=0}^\infty p_i=\infty$$
>
> **Proof ($\Rightarrow$):** Since $1-x < e^{-x}$ for $x>0$ (tangent inequality: $1-x$ is tangent to $e^{-x}$ at $x=0$, and $e^{-x}$ is convex):
> $$\prod_{i=0}^m(1-p_i) < \exp\!\left(-\sum_{i=0}^m p_i\right) \xrightarrow{m\to\infty} 0 \quad\text{if }\sum p_i=\infty$$
>
> **Proof ($\Leftarrow$, by contradiction):** Suppose $\sum p_i<\infty$. Use the inequality (proved by induction):
> $$\prod_{i=j}^m(1-p_i) > 1-\sum_{i=j}^m p_i \tag{3.24}$$
> *(Base case: $(1-p_j)(1-p_{j+1})=1-p_j-p_{j+1}+p_jp_{j+1}>1-p_j-p_{j+1}$. Induction: multiply both sides by $(1-p_{m+1})$.)*
>
> If $\sum p_i<\infty$, then tail sums $\to 0$, so $\exists j_0$ s.t. $\sum_{i=j}^\infty p_i<1$ $\forall j>j_0$. Then (3.24) gives:
> $$\lim_{m\to\infty}\prod_{i=j}^m(1-p_i) > 1-\sum_{i=j}^\infty p_i > 0$$
> This partial product is positive, and multiplying by the finitely many preceding non-zero factors yields $\prod_{i=0}^\infty(1-p_i)>0$ — contradicting (3.23). $\square$

---

### Example 8 — Recurrence of G/M/1 Queue

> [!Example] Example 8 — G/M/1 Queue Recurrence
> **Problem:** Determine when the G/M/1 queue (interarrivals $\sim G$, service $\sim\text{Exp}(\mu)$) is positive recurrent.
>
> **Approach:** Chain is irreducible and aperiodic. Find stationary distribution via ansatz $\pi_k=c\beta^k$.
>
> **Solution:**
>
> Stationarity equation for $k\geq 1$:
> $$\pi_k = \sum_{i=k-1}^\infty\pi_i\int_0^\infty e^{-\mu t}\frac{(\mu t)^{i+1-k}}{(i+1-k)!}\,\mathrm{d}G(t)$$
>
> Insert $\pi_k=c\beta^k$:
> $$c\beta^k = c\int_0^\infty e^{-\mu t}\beta^{k-1}\sum_{i=k-1}^\infty\frac{(\beta\mu t)^{i+1-k}}{(i+1-k)!}\,\mathrm{d}G(t) = c\int_0^\infty e^{-\mu t}\beta^{k-1}e^{\beta\mu t}\,\mathrm{d}G(t)$$
>
> (Exchanged sum and integral using Lebesgue's monotone convergence theorem.)
>
> Simplifying:
> $$\beta = \int_0^\infty e^{-\mu t(1-\beta)}\,\mathrm{d}G(t) = \mathbb{E}[e^{-\mu T(1-\beta)}] \equiv A(\beta) \tag{3.29}$$
>
> **Analysis of $A(\beta)$:**
> $$A(0) = \mathbb{E}[e^{-\mu T}]>0; \quad A(1)=1$$
> $$A'(\beta) = \int_0^\infty \mu t\,e^{-\mu t(1-\beta)}\,\mathrm{d}G(t)>0; \quad A''(\beta)>0$$
>
> $A(\beta)$ is strictly increasing and convex from $(0,A(0)>0)$ to $(1,1)$.
>
> **Case 1** — $A'(1)=\mu\mathbb{E}[T]=\mu/\lambda<1$, i.e. $\lambda>\mu$:
>
> $A(\beta)$ arrives at $(1,1)$ from above → no intersection with $y=\beta$ in $(0,1)$ → ansatz fails → chain is **transient** (arrivals exceed departures).
>
> **Case 2** — $A'(1)=\mu/\lambda>1$, i.e. $\lambda<\mu$:
>
> $A(\beta)$ arrives at $(1,1)$ from below → unique intersection $\beta^*\in(0,1)$ → valid stationary distribution $\pi_k=c(\beta^*)^k$ → chain is **positive recurrent**.
>
> **Critical case** $\lambda=\mu$: $A'(1)=1$, double root at $(1,1)$, no solution with $0<\beta<1$ → chain is **null recurrent**.
>
> ![[Stochastic_Processes_2020_p95_img26.jpeg]]
> *Figure 3.7 — Two possible behaviours of $A(\beta)$: either no intersection with $y=\beta$ in $(0,1)$ ($\lambda>\mu$, transient) or exactly one ($\lambda<\mu$, positive recurrent).*
>
> **Summary:**
> - $\lambda<\mu$: positive recurrent (stable)
> - $\lambda=\mu$: null recurrent
> - $\lambda>\mu$: transient (unstable)
>
> **Takeaway:** Stationarity equation + geometric ansatz → integral equation for $\beta$. Existence of $\beta^*\in(0,1)$ is determined by whether arrival rate is below service rate.

---

### Periodic Generalization

For irreducible, positive recurrent chains **with period** $d>1$, the limit $\lim_{n\to\infty}P^{(n)}_{ij}$ does not exist. However, along multiples of $d$:

$$\lim_{n\to\infty}P^{(nd)}_{ii} = \frac{d}{m_i}$$

**Time-averaged limiting distribution** (always well-defined):

$$\pi_i \equiv \lim_{n\to\infty}\frac{1}{n}\sum_{m=0}^{n-1}P^{(m)}_{ii} = \frac{1}{m_i} \tag{3.30}$$

**Derivation:** $P^{(n)}_{ii}=0$ for $n$ not a multiple of $d$; $P^{(nd)}_{ii}\to d/m_i$. Over one period $1\to d$: $(d-1)$ zero terms plus one term $d/m_i$ → average exactly $1/m_i$.

The $\pi_j$ so defined are the unique nonnegative solutions to:

$$\pi_j = \sum_{k=0}^\infty\pi_k P_{kj}, \qquad \sum_{j=0}^\infty\pi_j=1$$

---

## Reducible Markov Chains

**Isolated classes example:**

$$\mathbf{P} = \begin{Vmatrix}\frac{1}{2}&\frac{1}{2}&0&0\\\frac{1}{4}&\frac{3}{4}&0&0\\0&0&\frac{1}{3}&\frac{2}{3}\\0&0&\frac{2}{3}&\frac{1}{3}\end{Vmatrix} = \begin{Vmatrix}\mathbf{P}_1&\mathbf{O}\\\mathbf{O}&\mathbf{P}_2\end{Vmatrix}$$

Two isolated classes; $\mathbf{P}^n = \text{diag}(\mathbf{P}_1^n, \mathbf{P}_2^n)$.

**General rules:**
- For $i,j$ in the same positive recurrent aperiodic class: $\lim_{n\to\infty}P^{(n)}_{ij}=1/m_j\geq 0$. Eq. (3.31)
- For $j$ transient: $\lim_{n\to\infty}P^{(n)}_{ij}=0$ $\forall i$. Eq. (3.32)
- Recurrent classes are isolated: $P^{(n)}_{ij}=0$ $\forall n$ when $i\in C$, $j\notin C$.

> [!Example] Reducible Chain Example — Chain (3.33)
> **Problem:** Analyse the long-run behaviour of:
> $$\mathbf{P} = \bordermatrix{&0&1&2&3\\0&\frac{1}{2}&\frac{1}{2}&0&0\\1&\frac{1}{4}&\frac{3}{4}&0&0\\2&\frac{1}{4}&\frac{1}{4}&\frac{1}{4}&\frac{1}{4}\\3&0&0&0&1} \tag{3.33}$$
>
> **Solution:**
>
> Classes: $A=\{0,1\}$ (recurrent, aperiodic), $B=\{2\}$ (transient), $C=\{3\}$ (absorbing, recurrent).
>
> ![[Stochastic_Processes_2020_p98_img27.jpeg]]
> *Figure 3.8 — Block diagram for chain (3.33). Transitions from $B$ to $A$ and $C$ are one-way.*
>
> **Class $A$:** Stationarity equations $\pi_j=\sum_{i=0}^1\pi_i P_{ij}$:
> $$\begin{cases}\pi_0=\frac{1}{2}\pi_0+\frac{1}{4}\pi_1\\\pi_1=\frac{1}{2}\pi_0+\frac{3}{4}\pi_1\end{cases} \implies \pi_0=\frac{\pi_1}{2}; \quad \pi_0+\pi_1=1 \implies \pi_0=\frac{1}{3},\;\pi_1=\frac{2}{3}$$
>
> **Class $C$:** Trivial absorbing state → $\pi_3=1$.
>
> **Class $B$:** Transient, $\pi_{22}=0$. Absorption probability to $A$:
> $$u=(P_{20}+P_{21})\cdot 1+\frac{1}{4}u+\frac{1}{4}\cdot 0=\frac{1}{2}+\frac{1}{4}u \implies u=\frac{2}{3}=\pi_A$$
>
> Long-run probabilities starting from state 2:
> $$\pi_{20}=\pi_A\cdot\pi_0=\frac{2}{3}\cdot\frac{1}{3}=\frac{2}{9}, \quad \pi_{21}=\pi_A\cdot\pi_1=\frac{2}{3}\cdot\frac{2}{3}=\frac{4}{9}, \quad \pi_{23}=\frac{1}{3}$$
>
> **Full limiting matrix:**
>
> | Start\End | 0 | 1 | 2 | 3 |
> |---|---|---|---|---|
> | 0 | $\pi_0=1/3$ | $\pi_1=2/3$ | 0 | 0 |
> | 1 | $\pi_0=1/3$ | $\pi_1=2/3$ | 0 | 0 |
> | 2 | $2/9$ | $4/9$ | 0 | $1/3$ |
> | 3 | 0 | 0 | 0 | 1 |
>
> **Takeaway:** For a transient starting state, the long-run probabilities combine absorption probabilities into each recurrent class with the within-class stationary distributions.

> [!Example] Exercise — Binary Message Channel
> **Problem:** A binary message $\{0,1\}$ passes through $n$ stages, each flipping the bit with probability $\alpha$ ($0<\alpha<1$). $X_0$ = sent signal, $X_n$ = received signal after $n$ stages. Transition probabilities:
> $$P_{00}=P_{11}=1-\alpha, \quad P_{01}=P_{10}=\alpha$$
> Compute $\Pr\{X_5=0\mid X_0=0\}$.
>
> **Approach:** Use the two-state chain formula $\mathbf{P}^n$ from Chapter 2 with $a=b=\alpha$.
>
> **Solution:**
>
> From the two-state chain result (with $a=b=\alpha$):
> $$\mathbf{P}^n = \frac{1}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix} + \frac{(1-2\alpha)^n}{2}\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$$
> For $n=5$:
> $$P^{(5)}_{00} = \frac{1}{2}+\frac{(1-2\alpha)^5}{2} = \frac{1+(1-2\alpha)^5}{2}$$
>
> **Result:** $\Pr\{X_5=0\mid X_0=0\}=\dfrac{1+(1-2\alpha)^5}{2}$.

---

### Another Behaviour of Infinite Markov Chains

It is possible for all states of an **infinite** Markov chain to be either transient or null recurrent, so that $\lim_{n\to\infty}P^{(n)}_{ij}=0$ for all $i,j$.

A trivial example is the chain defined by the update rule:

$$\begin{cases}X_n = X_{n-1}+1\\X_0=0\end{cases}$$

so that $X_n=n$, with transition matrix:

$$\mathbf{P} = \bordermatrix{&0&1&2&3&\cdots\\0&0&1&0&0&\cdots\\1&0&0&1&0&\cdots\\2&0&0&0&1&\cdots\\3&0&0&0&0&\cdots\\\vdots&\vdots&\vdots&\vdots&\vdots&\ddots}$$

Each state is visited at most once: state $k$ is entered at step $k$ and never revisited. All states are transient; each one forms its own class.

This behaviour is only possible in chains with **infinitely many states**. A finite chain cannot have all states transient or null recurrent — it must "be somewhere" in the long run. The next two lemmas formalise this.

---

### Finite Markov Chains — Positive Recurrence Lemmas

> [!Important] Lemma 3.5.1 — Finite Chains Have at Least One Positive Recurrent State
> **Statement:** In a Markov chain with a finite number $N<\infty$ of states, there must be at least one positive recurrent state.
>
> **Proof (by contradiction):**
> Suppose no positive recurrent states exist, so $\lim_{n\to\infty}P^{(n)}_{ij}=0$ $\forall i,j$. But row normalization requires $\sum_j P^{(n)}_{ij}=1$ $\forall n$. Since $N$ is finite, exchange limit and sum:
> $$1 = \lim_{n\to\infty}\sum_{j=1}^N P^{(n)}_{ij} = \sum_{j=1}^N\lim_{n\to\infty}P^{(n)}_{ij} = 0$$
> Contradiction. $\square$
>
> *(For infinite chains, the exchange of limit and sum is illegitimate, so the argument fails — infinite transient chains are possible.)*

> [!Important] Lemma 3.5.2 — Finite Chains Have No Null Recurrent States
> **Statement:** In a Markov chain with a finite number of states, no null recurrent states exist.
>
> **Proof (by contradiction):**
> Suppose a null recurrent state exists. By the class property, it belongs to a finite null recurrent class. But treating that class as an isolated chain (it is recurrent, hence absorbing), Lemma 3.5.1 applies: that finite class must have a positive recurrent state — contradicting that all its states are null recurrent. $\square$
>
> **Corollary:** Null recurrent states exist only in infinite Markov chains.

> [!Example] Exercise — Limiting Behaviour of $\mathbf{P}_1$ and $\mathbf{P}_2$
> **Problem:** Compute $\lim_{n\to\infty}\mathbf{P}^{(n)}$ and $\lim_{n\to\infty}\mathbf{P}^{(2n+1)}$ for:
> $$\mathbf{P}_1=\begin{Vmatrix}0&1&0&0\\1&0&0&0\\\frac{1}{3}&\frac{1}{3}&\frac{1}{6}&\frac{1}{6}\\0&0&0&1\end{Vmatrix}, \qquad \mathbf{P}_2=\begin{Vmatrix}0&1&0&0\\1&0&0&0\\\frac{1}{6}&\frac{1}{3}&\frac{1}{3}&\frac{1}{6}\\0&0&0&1\end{Vmatrix}$$
>
> **Solution:**
>
> Both matrices share the upper-left $2\times 2$ block $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ which has period 2. So the subsequences for $n$ even and $n$ odd individually converge to different limits, meaning the general limit $\lim_{n\to\infty}\mathbf{P}^n$ does not exist (oscillates).
>
> The limits along even and odd subsequences do exist separately and can be computed numerically.
>
> **Takeaway:** A periodic block in the transition matrix prevents the full limit from existing; only subsequences along multiples of the period converge.

---

## Summary Table

| Concept | Definition / Formula | Notes |
|---|---|---|
| Regular chain | Finite states; $\exists k: (\mathbf{P}^k)_{ij}>0\;\forall i,j$ | Guarantees unique limiting distribution |
| Limiting distribution | $\lim_{n\to\infty}P^{(n)}_{ij}=\pi_j$ | Independent of $i$; solves $\boldsymbol{\pi}=\boldsymbol{\pi}\mathbf{P}$, $\sum\pi_j=1$ |
| Long-run fraction of time | $\pi_j=\lim_{m\to\infty}\frac{1}{m}\sum_{k=0}^{m-1}P^{(k)}_{ij}$ | Same as limiting distribution |
| Accessibility | $P^{(n)}_{ij}>0$ for some $n$ | $j$ reachable from $i$ |
| Communication | $i\leftrightarrow j$: mutual accessibility | Equivalence relation → class partition |
| Irreducible | All states communicate | Single class |
| Period $d(i)$ | $\gcd\{n\geq 1: P^{(n)}_{ii}>0\}$ | Class property (Theorem 3.3.1) |
| Aperiodic | $d(i)=1$ | Required for basic limit theorem |
| Recurrent | $f_{ii}=1$; $\sum_n P^{(n)}_{ii}=\infty$ | Class property (Corollary 3.3.2) |
| Transient | $f_{ii}<1$; $\sum_n P^{(n)}_{ii}<\infty$ | System visits $i$ finitely many times |
| Null recurrent | $f_{ii}=1$, $m_i=\infty$, $\pi_i=0$ | Certain return but infinite expected time |
| Positive recurrent | $f_{ii}=1$, $m_i<\infty$, $\pi_i=1/m_i>0$ | Stable long-run behaviour |
| Basic limit theorem | $\lim_{n\to\infty}P^{(n)}_{ji}=1/m_i$ | Requires irreducible, aperiodic, pos. recurrent |
| Stationary distribution | $\boldsymbol{\pi}=\boldsymbol{\pi}\mathbf{P}$, $\sum\pi_i=1$ | Exists for pos. recurrent; may not = limiting dist. |
| Periodic limit | $\lim_{n\to\infty}\frac{1}{n}\sum_m P^{(m)}_{ii}=1/m_i$ | Time average always $=1/m_i$ regardless of period |
| Lemma 3.5.1 | Finite chain → $\geq 1$ positive recurrent state | Contradiction if all states have $\pi_j\to 0$ |
| Lemma 3.5.2 | Finite chain → no null recurrent states | Null recurrent only in infinite chains |
| G/M/1 stability | $\lambda<\mu$: pos. recurrent; $\lambda=\mu$: null; $\lambda>\mu$: transient | Via geometric ansatz $\pi_k=c\beta^k$ |
| Lemma 3.4.3 | $\prod(1-p_i)=0\iff\sum p_i=\infty$ | Key for success-run recurrence |
