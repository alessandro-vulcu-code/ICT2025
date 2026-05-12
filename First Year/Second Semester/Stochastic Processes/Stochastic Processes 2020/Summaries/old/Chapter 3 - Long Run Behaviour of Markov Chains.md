# Chapter 3 — Long Run Behaviour of Markov Chains

The central question of this chapter is: *what happens to a Markov chain after a very long time?* Does the distribution over states converge? Does the system forget its initial condition? The answers depend critically on structural properties of the chain — regularity, irreducibility, periodicity, and recurrence.

---

## 3.1 Regular Markov Chains

**Definition.** A Markov chain is **regular** if:
1. It has a **finite** state space $\{0, 1, \ldots, N\}$.
2. There exists an integer $k \geq 1$ such that $(\mathbf{P}^k)_{ij} > 0$ for **all** pairs $i, j$. That is, every state can be reached from every other state in exactly $k$ steps.

Condition 2 means that, given enough time, any state is reachable from any starting point — the chain is "fully connected" in a strong sense.

> **Theorem 3.1.** For a regular Markov chain, there exists a unique **limiting distribution** $\boldsymbol{\pi} = (\pi_0, \pi_1, \ldots, \pi_N)$ with $\pi_j > 0$ for all $j$ and $\sum_j \pi_j = 1$, such that:
> $$\lim_{n \to \infty} P_{ij}^{(n)} = \pi_j \quad \forall\, i, j = 0, 1, \ldots, N$$

This has three striking implications:
- The long-run distribution **exists** (the limit converges).
- It is **independent of the initial state** $i$ — the chain forgets where it started.
- Every state is visited with positive probability in the long run ($\pi_j > 0$).

### Finding the Limiting Distribution

> **Theorem (Stationary equations).** The limiting distribution $\boldsymbol{\pi}$ is the **unique** non-negative solution of:
> $$\pi_j = \sum_{k=0}^{N} \pi_k P_{kj} \qquad j = 0, 1, \ldots, N \tag{3.1}$$
> subject to the normalization constraint:
> $$\sum_{k=0}^{N} \pi_k = 1 \tag{3.2}$$

In matrix form, (3.1) reads $\boldsymbol{\pi} = \boldsymbol{\pi}\mathbf{P}$: $\boldsymbol{\pi}$ is a **left eigenvector** of $\mathbf{P}$ with eigenvalue 1.

**Why do we need (3.2)?** The system (3.1) is homogeneous — if $\boldsymbol{\pi}$ is a solution, so is $a\boldsymbol{\pi}$ for any scalar $a \neq 0$. Without (3.2), the solution would not be unique. The normalization constraint selects the unique representative corresponding to a probability distribution.

**Proof (Existence and Uniqueness).**

**Existence.** Since the chain is regular, the limit $\lim_{n \to \infty} P_{ij}^{(n)} = \pi_j$ exists.

*Step 1 — Normalization.* Since each row of $\mathbf{P}^{(n)}$ sums to 1:
$$\sum_{j=0}^{N} P_{ij}^{(n)} = 1 \qquad \forall\, i, n$$

Taking $n \to \infty$ and exchanging the limit with the **finite** sum:
$$\sum_{j=0}^{N} \pi_j = \lim_{n \to \infty} \sum_{j=0}^{N} P_{ij}^{(n)} = 1 \qquad \checkmark$$

*Step 2 — Satisfies (3.1).* Start from the Chapman-Kolmogorov relation:
$$P_{ij}^{(n)} = \sum_{k=0}^{N} P_{ik}^{(n-1)} P_{kj}$$

Take $n \to \infty$ and bring the limit inside the finite sum:
$$\pi_j = \lim_{n \to \infty} P_{ij}^{(n)} = \lim_{n \to \infty} \sum_{k=0}^{N} P_{ik}^{(n-1)} P_{kj} = \sum_{k=0}^{N} \pi_k P_{kj} \qquad \checkmark$$

**Uniqueness.** Suppose $\mathbf{x}$ is another solution with $x_j = \sum_k x_k P_{kj}$ and $\sum_k x_k = 1$. In matrix form: $\mathbf{x} = \mathbf{x}\mathbf{P}$.

Multiplying by $\mathbf{P}$ repeatedly: $\mathbf{x} = \mathbf{x}\mathbf{P}^{(n)}$ for all $n$. In components:
$$x_l = \sum_{k=0}^{N} x_k P_{kl}^{(n)} \qquad \forall\, n$$

Taking $n \to \infty$ and using the finite sum:
$$x_l = \lim_{n \to \infty} \sum_{k=0}^{N} x_k P_{kl}^{(n)} = \sum_{k=0}^{N} x_k \pi_l = \underbrace{\left(\sum_{k=0}^{N} x_k\right)}_{=1} \pi_l = \pi_l \qquad \square$$

---

### 3.1.1 Interpretation of the Limiting Distribution

$\pi_j$ has two equivalent interpretations:

**Interpretation 1: Long-run probability.** After a long time, the probability of finding the chain in state $j$ is $\pi_j$, regardless of where it started:
$$\pi_j = \lim_{n \to \infty} \mathbb{P}\{X_n = j \mid X_0 = i\}$$

**Interpretation 2: Long-run fraction of time.** $\pi_j$ is the fraction of time steps the chain spends in state $j$ over an infinitely long run.

*Derivation.* The fraction of time in state $j$ over $m$ steps, starting from $i$, has expected value:
$$\mathbb{E}\!\left[\frac{1}{m}\sum_{k=0}^{m-1}\mathbf{1}\{X_k = j\} \;\Big|\; X_0 = i\right] = \frac{1}{m}\sum_{k=0}^{m-1} \mathbb{P}\{X_k = j \mid X_0 = i\} = \frac{1}{m}\sum_{k=0}^{m-1} P_{ij}^{(k)}$$

Since $P_{ij}^{(n)} \to \pi_j$, the running averages also converge (Cesàro mean):
$$\frac{1}{m}\sum_{k=0}^{m-1} P_{ij}^{(k)} \xrightarrow{m \to \infty} \pi_j$$

**Practical application.** If each visit to state $j$ incurs a cost $c_j$, the long-run average cost per unit time is:
$$C = \sum_{j=0}^{N} \pi_j c_j$$

---

## 3.2 Non-Regular Markov Chains

Not every chain is regular. A chain fails regularity if its state space is infinite, or if $\mathbf{P}^k$ always has some zero entries. In these cases, the limiting distribution may not exist, may not be unique, or may assign zero probability to some states.

**Examples:**

![[Stochastic_Processes_2020_p70_img18.jpeg]]
*(a) Two distinct limiting distributions depending on initial state.*

![[Stochastic_Processes_2020_p70_img19.jpeg]]
*(b) Periodic chain: no limiting distribution exists.*

![[Stochastic_Processes_2020_p70_img20.jpeg]]
*(c) Unique limiting distribution exists, but some states have $\pi_j = 0$.*

*Figure 3.1 — Examples of non-regular Markov chains.*

**Explicit examples:**

**1.** $\mathbf{P} = \mathbf{I}$ (identity). The chain never moves. The limiting distribution depends on the initial state; some states may never be visited. $\mathbf{P}^n = \mathbf{P}$ for all $n$.

**2.** $\mathbf{P} = \begin{pmatrix}0&1\\1&0\end{pmatrix}$. The chain alternates between states 0 and 1. Since $\mathbf{P}^n = \mathbf{P}$ for odd $n$ and $\mathbf{P}^n = \mathbf{I}$ for even $n$, the limit does not exist.

**3.** $\mathbf{P} = \begin{pmatrix}1/2&1/2\\0&1\end{pmatrix}$. Then $\mathbf{P}^n = \begin{pmatrix}(1/2)^n & 1-(1/2)^n\\0&1\end{pmatrix} \to \begin{pmatrix}0&1\\0&1\end{pmatrix}$. The limit exists and is state-independent, but $\pi_0 = 0$: state 0 is never visited in the long run.

These examples motivate a finer classification of states.

---

## 3.3 Classification of States

Non-regular behaviour arises from states that are structurally isolated. We now formalise the key concepts.

### Accessibility and Communication

**Definition.** State $j$ is **accessible** from state $i$ (written $i \to j$) if $P_{ij}^{(n)} > 0$ for some $n \geq 0$ — i.e., it is possible to reach $j$ from $i$ in finitely many steps.

**Definition.** States $i$ and $j$ **communicate** (written $i \leftrightarrow j$) if $i \to j$ and $j \to i$.

Communication is an **equivalence relation**:

1. **Reflexivity** ($i \leftrightarrow i$): $P_{ii}^{(0)} = \delta_{ii} = 1 > 0$.
2. **Symmetry** ($i \leftrightarrow j \Rightarrow j \leftrightarrow i$): follows directly from the definition.
3. **Transitivity** ($i \leftrightarrow j$ and $j \leftrightarrow k \Rightarrow i \leftrightarrow k$):

*Proof.* Since $i \leftrightarrow j$, there exist $n, m$ with $P_{ij}^{(n)} > 0$ and $P_{jk}^{(m)} > 0$. By Chapman-Kolmogorov:
$$P_{ik}^{(n+m)} = \sum_r P_{ir}^{(n)} P_{rk}^{(m)} \geq P_{ij}^{(n)} P_{jk}^{(m)} > 0$$
(the sum of non-negative terms is $\geq$ any single term). So $i \to k$. By the same argument $k \to i$, giving $i \leftrightarrow k$. $\square$

Because communication is an equivalence relation, it partitions all states into **equivalence classes** of mutually communicating states. Different classes may be linked by one-way transitions, but never by two-way ones (otherwise they would form a single class).

**Definition.** A chain is **irreducible** if it consists of a single communication class (all states communicate). Otherwise it is **reducible**.

**Example of a reducible chain:**
$$\mathbf{P} = \begin{pmatrix} \mathbf{P}_1 & \mathbf{0} \\ \mathbf{0} & \mathbf{P}_2 \end{pmatrix}$$
with two isolated classes.

**Example with one-way transitions** (random walk with absorbing barriers):
$$\mathbf{P} = \begin{pmatrix} 1 & 0 & 0 & \cdots & 0 \\ q & 0 & p & \cdots & 0 \\ 0 & q & 0 & \cdots & 0 \\ \vdots & & & \ddots & \vdots \\ 0 & \cdots & 0 & 0 & 1 \end{pmatrix} \qquad \begin{array}{l} \leftarrow \text{state } 0 \\ \leftarrow \text{state } 1 \\ \leftarrow \text{state } 2 \\ \\ \leftarrow \text{state } a \end{array} \tag{3.4}$$

Here $\{0\}$, $\{1, \ldots, a-1\}$, $\{a\}$ are three classes. Starting in the interior class can lead to either absorbing state, but not vice versa.

---

### 3.3.1 Periodicity

A state can exhibit **periodic** behaviour: the chain can only return to it at multiples of some fixed period.

**Definition.** The **period** $d(i)$ of state $i$ is:
$$d(i) = \gcd\{n \geq 1 : P_{ii}^{(n)} > 0\}$$

If $P_{ii}^{(n)} = 0$ for all $n \geq 1$ (the chain never returns to $i$), define $d(i) = 0$.

Note: if $P_{ii} > 0$ (the chain can stay at $i$), then $d(i) = 1$ since 1 divides all path lengths.

**Simple example.** A cyclic chain visiting $N$ states in order has $d(i) = N$ for every state $i$.

**Example (chain 3.5):**
$$\mathbf{P} = \bordermatrix{ & 0 & 1 & 2 & 3 \cr 0 & 0 & 1 & 0 & 0 \cr 1 & 0 & 0 & 1 & 0 \cr 2 & 0 & 0 & 0 & 1 \cr 3 & 1 & 0 & \frac{1}{2} & 0 } \tag{3.5}$$

From state 0, the chain can return after 4 steps ($0 \to 1 \to 2 \to 3 \to 0$), or after 6 steps ($0 \to 1 \to 2 \to 3 \to 2 \to 3 \to 0$), etc. All return times are even, so $d(0) = 2$.

![[Stochastic_Processes_2020_p73_img21.jpeg]]
*Figure 3.2 — Block diagram for an $N=6$ cyclic Markov chain.*

![[Stochastic_Processes_2020_p74_img22.jpeg]]
*Figure 3.3 — Block diagram for chain (3.5).*

> **Theorem 3.3.1.** Period is a class property: if $i \leftrightarrow j$, then $d(i) = d(j)$.

**Proof.** Since $i \leftrightarrow j$, there exist $m, n \geq 1$ with $P_{ij}^{(m)} > 0$ and $P_{ji}^{(n)} > 0$.

Let $S_i = \{s > 0 : P_{ii}^{(s)} > 0\}$ be the set of return-path lengths for $i$, so $d(i) = \gcd(S_i)$.

For any $s \in S_i$, the path $j \xrightarrow{n} i \xrightarrow{s} i \xrightarrow{m} j$ exists (with positive probability by Chapman-Kolmogorov), so $(n+s+m) \in S_j$. Similarly, by repeating the $i \to i$ loop twice, $(n+2s+m) \in S_j$.

Since $d(j)$ divides every element of $S_j$:
$$n + s + m = k_1 d(j), \qquad n + 2s + m = k_2 d(j)$$

Subtracting: $s = (k_2 - k_1)d(j)$, so $d(j)$ divides $s$. This holds for all $s \in S_i$, meaning $d(j)$ is a common divisor of $S_i$. Since $d(i)$ is the **greatest** common divisor, $d(i)$ is a multiple of $d(j)$.

Exchanging the roles of $i$ and $j$ gives $d(j)$ is a multiple of $d(i)$. Therefore $d(i) = d(j)$. $\square$

![[Stochastic_Processes_2020_p75_img23.jpeg]]
*Figure 3.4 — Illustration of the period class property: if $d(i) = 3$, then $n+m$ must be divisible by 3, constraining $d(j)$ to also equal 3.*

**Intuition.** If $d(i) = 3$, every return path to $i$ has length divisible by 3. If $j$ communicated with $i$ and had $d(j) = 2$, we could build a return path to $i$ of length $n + m + 2$ — not divisible by 3, contradiction. Similarly $d(j) > 3$ leads to contradiction. Hence $d(j) = 3$.

**Definition.** A state (or chain) is **aperiodic** if $d(i) = 1$ for all states $i$.

---

### 3.3.2 Recurrence

**Definition.** The **first return time** to state $i$ is the random variable:
$$\theta_{ii} = \min\{n \geq 1 : X_n = i\}$$

Its distribution is:
$$f_{ii}^{(n)} = \mathbb{P}\{\theta_{ii} = n\} = \mathbb{P}\{X_n = i,\, X_\nu \neq i\ \forall\, \nu = 1, \ldots, n-1 \mid X_0 = i\}$$

The total probability of *ever* returning to $i$ is:
$$f_{ii} = \sum_{n=1}^{\infty} f_{ii}^{(n)}$$

**Definition.**
- State $i$ is **recurrent** if $f_{ii} = 1$ (the chain returns to $i$ with certainty).
- State $i$ is **transient** if $f_{ii} < 1$ (there is a positive probability of never returning).

**Transient states: finite expected visits.** For a transient state $i$, $f_{ii} < 1$. By the Markov property, each time the chain is at $i$, the probability of returning again is $f_{ii}$. So the probability of returning at least $k$ times is $(f_{ii})^k$, and the number of returns $M$ follows a geometric distribution:
$$\mathbb{P}\{M \geq k \mid X_0 = i\} = (f_{ii})^k, \qquad \mathbb{E}[M \mid X_0 = i] = \frac{f_{ii}}{1 - f_{ii}} < \infty$$

**Recurrent states: infinite visits.** For a recurrent state, $f_{ii} = 1$. At each return, the Markov property resets the future identically, so the chain returns again with probability 1. This means the chain visits $i$ infinitely many times — the number of visits $M = \infty$ with probability 1.

![[Stochastic_Processes_2020_p76_img24.jpeg]]
*Figure 3.5 — Proper vs improper random variables. For a recurrent state, $M = \infty$ almost surely, so $\mathbb{P}[M \leq x] = 0$ for all finite $x$.*

### Improper Random Variables

The number of visits $M$ for a recurrent state does not satisfy $\lim_{x \to \infty} \mathbb{P}[M \leq x] = 1$ (the defining property of a proper random variable). Instead $\mathbb{P}[M \leq x] = 0$ for all finite $x$.

We extend the framework by allowing **improper random variables**, for which:
$$\mathbb{P}[X = \infty] = P_\infty = \lim_{x \to \infty} \mathbb{P}[X > x] > 0$$

For a recurrent state: $P_\infty = \lim_{k \to \infty} \mathbb{P}[M \geq k] = 1$.

For any non-negative improper r.v., the expectation diverges:
$$\mathbb{E}[X] = \sum_{k=0}^{+\infty} \mathbb{P}[X > k] = \infty \quad \text{(since } \lim_{k \to \infty} \mathbb{P}[X > k] > 0\text{)}$$

### Recurrence Criterion

> **Theorem.** State $i$ is recurrent if and only if $\sum_{n=1}^{\infty} P_{ii}^{(n)} = \infty$. Equivalently, state $i$ is transient if and only if $\sum_{n=1}^{\infty} P_{ii}^{(n)} < \infty$.

**Proof.** Let $M = \sum_{n=1}^{\infty} \mathbf{1}\{X_n = i\}$ count the total visits to state $i$. Its expected value is:
$$\mathbb{E}[M \mid X_0 = i] = \sum_{n=1}^{\infty} \mathbb{E}[\mathbf{1}\{X_n = i\} \mid X_0 = i] = \sum_{n=1}^{\infty} P_{ii}^{(n)}$$

(The interchange of expectation and sum is justified because $\mathbf{1}\{X_n = i\} \geq 0$; see Section 3.3.3.)

Also:
$$\mathbb{E}[M \mid X_0 = i] = \sum_{k=1}^{\infty} \mathbb{P}[M \geq k \mid X_0 = i] = \sum_{k=1}^{\infty} (f_{ii})^k = \frac{f_{ii}}{1 - f_{ii}}$$

- **Transient** ($f_{ii} < 1$): $\sum_{n=1}^{\infty} P_{ii}^{(n)} = \frac{f_{ii}}{1-f_{ii}} < \infty$ $\square$
- **Recurrent** ($f_{ii} = 1$): $\sum_{n=1}^{\infty} P_{ii}^{(n)} = \sum_{k=1}^{\infty} 1^k = \infty$ $\square$

---

### 3.3.3 Fubini's Theorem

Many arguments require exchanging the order of two infinite sums, or swapping $\mathbb{E}$ with $\sum$. The rigorous justification is:

> **Fubini's Theorem.** If either $\sum_x \sum_y |f(x,y)| < \infty$ or $\sum_y \sum_x |f(x,y)| < \infty$ (absolute convergence), then:
> $$\sum_x \sum_y f(x,y) = \sum_y \sum_x f(x,y)$$

**Why absolute convergence matters.** Decompose $f = f_+ - f_-$ (positive and negative parts). If $\sum |f|$ diverges while $\sum f$ converges, the result may be of the form $\infty - \infty$, which is indeterminate — the order of summation can change the value.

**Key result for non-negative random variables.** For $X_i \geq 0$:
$$\mathbb{E}\!\left[\sum_{i=0}^{+\infty} X_i\right] = \sum_{i=0}^{+\infty} \mathbb{E}[X_i]$$
always holds (both sides are either equal and finite, or both $= \infty$).

*Proof sketch.* Since $X_i \geq 0$, the partial sums $S_M = \sum_{i=0}^M X_i$ are monotonically non-decreasing in $M$. By Lebesgue's Monotone Convergence Theorem, $\mathbb{E}[S_M]$ can be exchanged with $\lim_{M \to \infty}$:
$$\mathbb{E}\!\left[\sum_{i=0}^{+\infty} X_i\right] = \lim_{M \to \infty} \mathbb{E}\!\left[\sum_{i=0}^M X_i\right] = \lim_{M \to \infty} \sum_{i=0}^M \mathbb{E}[X_i] = \sum_{i=0}^{+\infty} \mathbb{E}[X_i]$$

This justifies the step $\mathbb{E}[\sum_n \mathbf{1}\{X_n = i\}] = \sum_n P_{ii}^{(n)}$ used in Section 3.3.2 (since $\mathbf{1}\{X_n = i\} \geq 0$).

---

### Corollary: Recurrence is a Class Property

> **Corollary.** If $i \leftrightarrow j$ and $i$ is recurrent, then $j$ is recurrent.

**Proof.** Since $i \leftrightarrow j$, there exist $m, n \geq 1$ with $P_{ji}^{(m)} > 0$ and $P_{ij}^{(n)} > 0$. For any $\nu \geq 0$:
$$P_{jj}^{(m+\nu+n)} \geq P_{ji}^{(m)} P_{ii}^{(\nu)} P_{ij}^{(n)}$$

Summing over $\nu$:
$$\sum_{\nu=0}^{\infty} P_{jj}^{(m+\nu+n)} \geq P_{ji}^{(m)} P_{ij}^{(n)} \underbrace{\sum_{\nu=0}^{\infty} P_{ii}^{(\nu)}}_{=\,\infty \text{ (i recurrent)}} = \infty$$

Since this shifted sum diverges, $\sum_{\nu=0}^{\infty} P_{jj}^{(\nu)} = \infty$, proving $j$ is recurrent. $\square$

**Summary:** Both **periodicity** and **recurrence** are class properties — all states in the same communication class share the same period and the same recurrence type.

---

## 3.4 Basic Limit Theorem of Markov Chains

We now establish the fundamental connection between long-run behaviour and the structure of the chain.

**Setup.** For a recurrent state $i$, define the first return time:
$$R_i = \min\{n \geq 1 : X_n = i\}$$

Since $i$ is recurrent, $f_{ii} = 1$, so $R_i$ is always finite (the chain certainly returns). The **mean return time** is:
$$m_i = \mathbb{E}[R_i \mid X_0 = i] = \sum_{n=1}^{\infty} n\,f_{ii}^{(n)}$$

Importantly, $m_i$ can be infinite even though $R_i$ is always finite (if $f_{ii}^{(n)}$ decays too slowly).

### Types of Recurrent States

Based on $m_i$, recurrent states split into two subtypes:

| Type | $m_i$ | $\pi_i = 1/m_i$ | Long-run visits |
|------|--------|-----------------|----------------|
| **Positive recurrent** (strongly ergodic) | $< \infty$ | $> 0$ | Visited regularly |
| **Null recurrent** (weakly ergodic) | $= \infty$ | $= 0$ | Visited, but "rarely" |

Together with transient states, this gives the full classification:

| State type | $f_{ii}$ | $\mathbb{E}[M \mid X_0 = i]$ | $m_i$ | $\pi_i$ |
|------------|----------|-------------------------------|--------|---------|
| Transient | $< 1$ | $\frac{f_{ii}}{1-f_{ii}} < \infty$ | $\infty$ | $0$ |
| Null recurrent | $1$ | $\infty$ | $\infty$ | $0$ |
| Positive recurrent | $1$ | $\infty$ | $< \infty$ | $> 0$ |

*Table 3.1 — Classification of states: $f_{ii}$ = probability of return, $M$ = number of returns, $m_i$ = mean return time, $\pi_i$ = long-run fraction of time in $i$.*

> **Theorem 3.4.1 (Basic Limit Theorem).** Let the Markov chain be recurrent, irreducible, and aperiodic. Then:
> $$\lim_{n \to \infty} P_{ii}^{(n)} = \frac{1}{m_i} = \pi_i$$
> Moreover, for **every** starting state $j$:
> $$\lim_{n \to \infty} P_{ji}^{(n)} = \pi_i = \frac{1}{m_i}$$

This theorem makes precise the intuition: if the chain returns to $i$ once every $m_i$ steps on average, then it spends $1/m_i$ of its time there.

**Remark.** The theorem applies to any **aperiodic recurrent class** within a larger chain. Since leaving a recurrent class is impossible (any one-way transition out of a recurrent class would contradict recurrence), we can restrict the transition matrix to just that class and treat it as an irreducible chain.

---

> **Theorem 3.4.2.** In a **positive recurrent aperiodic** class with countably many states $j \in \mathbb{N}$:
> $$\pi_j = \lim_{n \to \infty} P_{ij}^{(n)} = \frac{1}{m_j} > 0$$
> and $\boldsymbol{\pi}$ is the unique solution of:
> $$\pi_j = \sum_{i=0}^{\infty} \pi_i P_{ij} \qquad \sum_{i=0}^{\infty} \pi_i = 1 \qquad \pi_i \geq 0 \tag{3.7}$$
> Any solution to (3.7) is called a **stationary probability distribution**.

**Key difference from Theorem 3.1:** here the state space may be **infinite** (countably infinite), so we cannot simply exchange limits and finite sums. The proof requires more care.

**Proof of Existence** (four steps):

**Step 1 — $\sum_j \pi_j \leq 1$.** Since $\sum_{j=0}^{+\infty} P_{ij}^{(n)} = 1$ and the partial sum is $\leq$ the full sum:
$$1 \geq \sum_{j=0}^{M} P_{ij}^{(n)} \quad \forall M, n$$
Taking $n \to \infty$ inside the *finite* sum and then $M \to \infty$:
$$\sum_{j=0}^{+\infty} \pi_j \leq 1$$

**Step 2 — $\pi_j \geq \sum_k \pi_k P_{kj}^{(n)}$.** From Chapman-Kolmogorov:
$$P_{ij}^{(m+n)} \geq \sum_{k=0}^{M} P_{ik}^{(m)} P_{kj}^{(n)}$$

Taking $m \to \infty$ inside the finite sum:
$$\pi_j \geq \sum_{k=0}^{M} \pi_k P_{kj}^{(n)} \quad \forall M, n$$
And $M \to \infty$: $\pi_j \geq \sum_{k=0}^{+\infty} \pi_k P_{kj}^{(n)}$ for all $n$.

**Step 3 — Equality in Step 2.** Suppose for contradiction that $\exists j$ such that $\pi_j > \sum_k \pi_k P_{kj}^{(n)}$ strictly. Summing over all $j$:
$$\sum_j \pi_j > \sum_j \sum_k \pi_k P_{kj}^{(n)} \geq \sum_{k=0}^{M} \pi_k \underbrace{\sum_j P_{kj}^{(n)}}_{=1} = \sum_{k=0}^{M} \pi_k \quad \forall M$$

Taking $M \to \infty$: $\sum_j \pi_j > \sum_k \pi_k$ — a contradiction. Therefore:
$$\pi_j = \sum_{k=0}^{+\infty} \pi_k P_{kj}^{(n)} \quad \forall n$$
Setting $n = 1$ gives (3.7). $\checkmark$

**Step 4 — $\sum_j \pi_j = 1$.** Use Step 3 with the fact that $|P_{kj}^{(n)}| \leq 1$ (uniform bound) and $\sum_k \pi_k \leq 1$ to bring the limit inside the sum:
$$\pi_j = \lim_{n \to \infty} \sum_k \pi_k P_{kj}^{(n)} = \left(\sum_k \pi_k\right) \lim_{n \to \infty} P_{kj}^{(n)} = \left(\sum_k \pi_k\right) \pi_j$$

Since $\pi_j > 0$ (positive recurrence), divide: $\sum_k \pi_k = 1$. $\checkmark$

**Proof of Uniqueness.** Suppose $\mathbf{x}$ satisfies (3.7). By iterating $x_j = \sum_i x_i P_{ij}$, one shows $x_j \geq \sum_k x_k P_{kj}^{(n)}$ for all $n$. By the same contradiction argument as Step 3, equality holds. Taking $n \to \infty$:
$$x_j = \sum_k x_k \pi_j = \left(\sum_k x_k\right)\pi_j = \pi_j \qquad \square$$

---

### Stationary Distribution vs. Limiting Distribution

**Important distinction:** A stationary distribution satisfying (3.7) is not always a limiting distribution.

- If a **limiting distribution** exists, it is necessarily stationary (3.7).
- The **converse is false**: a periodic chain can have a stationary distribution but no limiting distribution.

**Example:**
$$\mathbf{P} = \begin{pmatrix}0&1\\1&0\end{pmatrix}$$

This chain cycles between 0 and 1 — no limiting distribution exists. Yet $\boldsymbol{\pi} = (1/2, 1/2)$ satisfies (3.7):
$$\begin{pmatrix}\frac{1}{2} & \frac{1}{2}\end{pmatrix} \begin{pmatrix}0&1\\1&0\end{pmatrix} = \begin{pmatrix}\frac{1}{2} & \frac{1}{2}\end{pmatrix} \checkmark$$

**Conclusion:** Solving (3.7) for an **aperiodic** chain both proves positive recurrence (existence of solution) and gives the limiting distribution. For periodic chains, (3.7) may be solvable, but the solution is a time-average — not a pointwise limit.

---

### Random Walk Example — Finding the Stationary Distribution

Consider the irreducible random walk with period $d = 2$:
$$\mathbf{P} = \begin{pmatrix} 0 & 1 & 0 & \cdots \\ q_1 & 0 & p_1 & \cdots \\ 0 & q_2 & 0 & \cdots \\ \vdots & & & \ddots \end{pmatrix}, \qquad p_i, q_i > 0$$

Although periodic ($d = 2$), a stationary distribution still exists if we can solve:
$$x_i = p_{i-1} x_{i-1} + q_{i+1} x_{i+1} \qquad i > 0 \tag{3.13}$$
with $x_0 = q_1 x_1$ and $\sum_i x_i = 1$.

**Solving by forward substitution:**
$$x_1 = \frac{x_0}{q_1}, \quad x_2 = \frac{p_1 x_0}{q_1 q_2}, \quad x_3 = \frac{p_1 p_2 x_0}{q_1 q_2 q_3}$$

The general pattern is:
$$x_i = x_0 \prod_{k=0}^{i-1} \frac{p_k}{q_{k+1}} \qquad i \geq 1 \quad (p_0 \equiv 1) \tag{3.16}$$

**Verification:** Substituting into (3.13):
$$p_{i-1}x_{i-1} + q_{i+1}x_{i+1} = \frac{p_{i-1}\cdots p_1 x_0}{q_i \cdots q_1}\,(q_i + p_i) = x_i \checkmark$$

**Normalization** fixes $x_0$:
$$x_0 = \left(\sum_{i=0}^{+\infty} \prod_{k=0}^{i-1} \frac{p_k}{q_{k+1}}\right)^{-1} \tag{3.17}$$

The stationary solution exists only if this sum converges. For the homogeneous case $p_k \equiv p$, $q_k \equiv q$:
- $p < q$: sum converges $\Rightarrow$ chain is **positive recurrent**.
- $p \geq q$: sum diverges $\Rightarrow$ chain is **not positive recurrent** (null recurrent or transient).

---

### Lemma 3.4.3 — Infinite Product vs. Infinite Sum

> **Lemma.** For $0 < p_i < 1$:
> $$\prod_{i=0}^{\infty}(1-p_i) = 0 \iff \sum_{i=0}^{\infty} p_i = \infty$$

**Proof ($\Rightarrow$):** Using $1-x < e^{-x}$ for $x \in (0,1)$ (since $e^{-x}$ is convex and lies above its tangent at $x=0$):
$$\prod_{i=0}^{m}(1-p_i) < \exp\!\left(-\sum_{i=0}^{m} p_i\right) \xrightarrow{m \to \infty} 0 \quad \text{if } \sum p_i = \infty$$

**Proof ($\Leftarrow$):** Suppose $\prod_{i=0}^\infty(1-p_i) = 0$. We show $\sum p_i = \infty$ by contradiction.

Assume $\sum p_i < \infty$. Then the tail sum vanishes: $\exists j_0$ such that $0 < \sum_{i=j}^\infty p_i < 1$ for all $j > j_0$.

Using the inductive inequality (proved by induction on $m$):
$$\prod_{i=j}^{m}(1-p_i) > 1 - \sum_{i=j}^{m} p_i \tag{3.24}$$

(*Base case*: $(1-p_j)(1-p_{j+1}) = 1 - p_j - p_{j+1} + p_jp_{j+1} > 1 - p_j - p_{j+1}$ since $p_jp_{j+1} > 0$.)

Then $\lim_{m \to \infty} \prod_{i=j}^m (1-p_i) > 1 - \sum_{i=j}^\infty p_i > 0$.

Since this tail product is positive, and differs from the full product $\prod_{i=0}^\infty(1-p_i)$ by only finitely many nonzero factors, the full product must also be positive — contradicting hypothesis. $\square$

---

### Success Run Chain — Recurrence Analysis

Consider the success run chain:
$$\mathbf{P} = \begin{pmatrix} p_0 & 1-p_0 & 0 & 0 & \cdots \\ p_1 & 0 & 1-p_1 & 0 & \cdots \\ p_2 & 0 & 0 & 1-p_2 & \cdots \\ \vdots & & & & \ddots \end{pmatrix} \qquad 0 < p_k < 1 \tag{3.6}$$

![[Stochastic_Processes_2020_p88_img25.jpeg]]
*Figure 3.6 — Block diagram for the success run chain.*

The chain is irreducible (all states are in the same class). Focus on state 0.

**Tail probabilities.** Starting from 0, the only path *not* returning to 0 in the first $k$ steps is $0 \to 1 \to 2 \to \cdots \to k$. Therefore:
$$\mathbb{P}\{R_0 > k \mid X_0 = 0\} = \prod_{i=0}^{k-1}(1-p_i)$$

**Recurrence condition.** State 0 is recurrent iff the chain returns to 0 with certainty:
$$f_{00} = \lim_{k \to \infty} \left(1 - \prod_{i=0}^{k-1}(1-p_i)\right) = 1 \iff \prod_{i=0}^{\infty}(1-p_i) = 0$$

By Lemma 3.4.3: **State 0 is recurrent if and only if $\sum_{i=0}^{\infty} p_i = \infty$**.

**Positive recurrence condition.** Using the tail-sum formula for expectation:
$$m_0 = \mathbb{E}[R_0 \mid X_0 = 0] = \sum_{k=0}^{\infty} \mathbb{P}\{R_0 > k \mid X_0 = 0\} = 1 + \sum_{k=1}^{\infty} \prod_{i=0}^{k-1}(1-p_i)$$

State 0 is positive recurrent iff $m_0 < \infty$, i.e. iff $\sum_{k=1}^{\infty} \prod_{i=0}^{k-1}(1-p_i) < \infty$ — a stronger requirement than recurrence alone.

**Stationary distribution.** When positive recurrent, $\pi_0 = 1/m_0$. The remaining stationary probabilities follow from the stationarity equations:
$$\pi_1 = (1-p_0)\pi_0, \quad \pi_2 = (1-p_1)\pi_1, \quad \ldots$$

In general:
$$\pi_k = \pi_0 \prod_{i=0}^{k-1}(1-p_i) \qquad k \geq 1$$

**Special case $p_i \equiv p$.** Then $\prod_{i=0}^{k-1}(1-p_i) = q^k$ where $q = 1-p$, giving $m_0 = 1/(1-q) \cdot \frac{1}{p} = 1/p$ and $\pi_k = pq^k$ — a geometric distribution on $\mathbb{N}_0$.

---

### Example 8 — Recurrence of the G/M/1 Queue

Recall from Chapter 2 that the G/M/1 queue (general inter-arrivals, exponential service) sampled at arrival times has transition probabilities:
$$P_{i,i+1-j} = \int_0^{\infty} e^{-\mu t} \frac{(\mu t)^j}{j!}\,\mathrm{d}G(t) \qquad j = 0, 1, \ldots, i$$
$$P_{i0} = \int_0^{\infty} \sum_{k=i+1}^{\infty} e^{-\mu t} \frac{(\mu t)^k}{k!}\,\mathrm{d}G(t) \qquad i \geq 0$$

The chain is irreducible and aperiodic. To determine positive recurrence, we search for a stationary distribution.

**Ansatz $\pi_k = c\beta^k$.** Substituting into the stationarity equation $\pi_k = \sum_i \pi_i P_{ik}$ and exchanging the sum and integral (justified by Monotone Convergence, since all terms are non-negative):

$$c\beta^k = c \int_0^{\infty} e^{-\mu t} \beta^{k-1} \sum_{j=0}^{\infty} \frac{(\beta\mu t)^j}{j!}\,\mathrm{d}G(t) = c \int_0^{\infty} e^{-\mu t} \beta^{k-1} e^{\beta\mu t}\,\mathrm{d}G(t)$$

Simplifying (the factor $\beta^{k-1}$ cancels $\beta^k/\beta$ on the left):
$$\beta = \int_0^{\infty} e^{-\mu t(1-\beta)}\,\mathrm{d}G(t) = \mathbb{E}[e^{-\mu T(1-\beta)}] \equiv A(\beta) \tag{3.29}$$

This is a **fixed-point equation** for $\beta$. For the ansatz to yield a valid probability distribution, we need $0 < \beta < 1$.

**Analysis of $A(\beta)$.** Since $T > 0$:
- $A(0) = \mathbb{E}[e^{-\mu T}] > 0$
- $A(1) = \mathbb{E}[1] = 1$
- $A'(\beta) = \mu\,\mathbb{E}[T e^{-\mu T(1-\beta)}] > 0$ (strictly increasing)
- $A''(\beta) = \mu^2\,\mathbb{E}[T^2 e^{-\mu T(1-\beta)}] > 0$ (strictly convex)

$A(\beta)$ is a strictly increasing, strictly convex function going from $(0, A(0) > 0)$ to $(1, 1)$.

The question is whether $A(\beta)$ crosses the line $y = \beta$ at some $\beta^* \in (0,1)$:

![[Stochastic_Processes_2020_p95_img26.jpeg]]
*Figure 3.7 — The two possible behaviours of $A(\beta)$: either it reaches $(1,1)$ "from below" (intersection at $\beta^* \in (0,1)$, positive recurrence) or "from above" (no intersection, chain is transient).*

**Case 1: $A'(1) < 1$.** $A$ approaches $(1,1)$ from above: no intersection in $(0,1)$. Since $A'(1) = \mu \mathbb{E}[T] = \mu/\lambda$, this means $\lambda > \mu$. The ansatz fails; no stationary distribution. The chain is **transient** (arrivals outpace service, queue grows to infinity).

**Case 2: $A'(1) > 1$.** $A$ approaches $(1,1)$ from below: unique intersection $\beta^* \in (0,1)$. This means $\lambda < \mu$. The ansatz gives a valid stationary distribution $\pi_k = c(\beta^*)^k$, proving **positive recurrence**.

**Case 3: $A'(1) = 1$ ($\lambda = \mu$).** Tangent at $(1,1)$: no intersection in $(0,1)$. The chain is **null recurrent**.

**Summary for G/M/1:**
$$\begin{cases} \lambda < \mu & \text{positive recurrent (stable)} \\ \lambda = \mu & \text{null recurrent} \\ \lambda > \mu & \text{transient (unstable)} \end{cases}$$

The stationary distribution is geometric: $\pi_k = (1-\beta^*) (\beta^*)^k$, where $\beta^*$ is the unique solution of (3.29) in $(0,1)$.

---

## 3.4.1 Periodic Generalization

For a periodic irreducible chain with period $d$, the pointwise limit $\lim_{n \to \infty} P_{ij}^{(n)}$ does not exist. However, inspecting the chain only at multiples of $d$:
$$\lim_{n \to \infty} P_{ii}^{(nd)} = \frac{d}{m_i}$$

More usefully, the **time-average** (Cesàro mean) always exists:
$$\pi_i \equiv \lim_{n \to \infty} \frac{1}{n}\sum_{m=0}^{n-1} P_{ii}^{(m)} = \frac{1}{m_i} \tag{3.30}$$

**Intuition.** During one period $\{1, \ldots, d\}$: for $d-1$ of those steps $P_{ii}^{(m)} = 0$ (by periodicity), and for the one step that is a multiple of $d$, $P_{ii}^{(nd)} \to d/m_i$. The average over $d$ steps is therefore $(d-1) \cdot 0 + 1 \cdot (d/m_i)$ divided by $d$, giving $1/m_i$.

The $\pi_i$ defined by (3.30) still satisfy the stationarity equations:
$$\pi_j = \sum_{k=0}^{\infty} \pi_k P_{kj}, \qquad \sum_{j=0}^{\infty} \pi_j = 1$$

So the stationary distribution exists and is unique even for periodic chains, but it represents a *time-average* rather than a *pointwise limit*.

---

## 3.5 Reducible Markov Chains

While irreducible chains are most common, reducible chains arise when the state space decomposes into multiple classes.

**Block-diagonal example:**
$$\mathbf{P} = \begin{pmatrix}\mathbf{P}_1 & \mathbf{0} \\ \mathbf{0} & \mathbf{P}_2\end{pmatrix}, \quad \mathbf{P}^n = \begin{pmatrix}\mathbf{P}_1^n & \mathbf{0} \\ \mathbf{0} & \mathbf{P}_2^n\end{pmatrix}$$

The two classes evolve completely independently; each can be analysed separately using the results above.

**General rules for reducible chains:**
- For $i$ and $j$ in the same **aperiodic positive recurrent** class: $\lim_{n \to \infty} P_{ij}^{(n)} = 1/m_j > 0$ (Theorem 3.4.1).
- For $j$ **transient**: $\lim_{n \to \infty} P_{ij}^{(n)} = 0$ for all $i$ — the chain eventually leaves and never returns. $(3.32)$
- Starting from a **transient state** $i$, reaching a **recurrent state** $j$: requires computing the absorption probability into $j$'s class.

**Worked example.** Consider:
$$\mathbf{P} = \bordermatrix{ & 0 & 1 & 2 & 3 \cr 0 & 1/2 & 1/2 & 0 & 0 \cr 1 & 1/4 & 3/4 & 0 & 0 \cr 2 & 1/4 & 1/4 & 1/4 & 1/4 \cr 3 & 0 & 0 & 0 & 1} \tag{3.33}$$

Three classes: $A = \{0, 1\}$ (recurrent), $B = \{2\}$ (transient), $C = \{3\}$ (absorbing, recurrent).

**Class $A$ — positive recurrent.** Solving the stationarity equations:
$$\pi_0 = \frac{1}{2}\pi_0 + \frac{1}{4}\pi_1, \quad \pi_1 = \frac{1}{2}\pi_0 + \frac{3}{4}\pi_1, \quad \pi_0 + \pi_1 = 1$$
$$\Rightarrow \pi_0 = \frac{1}{3}, \quad \pi_1 = \frac{2}{3}$$

**Class $C$ — absorbing.** Trivially $\pi_3 = 1$.

**Class $B = \{2\}$ — transient.** $\lim_{n \to \infty} P_{22}^{(n)} = 0$.

**Absorption probabilities from state 2.** Using first-step analysis, let $u$ = probability of absorption in $A$ starting from 2:
$$u = (P_{20} + P_{21}) \cdot 1 + P_{22} \cdot u + P_{23} \cdot 0 = \frac{1}{2} + \frac{1}{4}u \implies u = \frac{2}{3}$$

So from state 2: probability $2/3$ of ending in $A$, probability $1/3$ of ending in $C$.

**Long-run probabilities from initial state 2.** To find $\lim_{n\to\infty} P_{2j}^{(n)}$: first move to the absorbing class (with the computed probabilities), then within that class reach the stationary distribution:
$$\lim_{n \to \infty} P_{20}^{(n)} = \mathbb{P}(\text{absorbed in }A) \cdot \pi_0 = \frac{2}{3} \cdot \frac{1}{3} = \frac{2}{9}$$
$$\lim_{n \to \infty} P_{21}^{(n)} = \mathbb{P}(\text{absorbed in }A) \cdot \pi_1 = \frac{2}{3} \cdot \frac{2}{3} = \frac{4}{9}$$
$$\lim_{n \to \infty} P_{22}^{(n)} = 0 \quad \text{(transient)}$$
$$\lim_{n \to \infty} P_{23}^{(n)} = \mathbb{P}(\text{absorbed in }C) = \frac{1}{3}$$

**Complete limiting matrix:**
$$\lim_{n \to \infty} \mathbf{P}^n = \bordermatrix{ & 0 & 1 & 2 & 3 \cr 0 & 1/3 & 2/3 & 0 & 0 \cr 1 & 1/3 & 2/3 & 0 & 0 \cr 2 & 2/9 & 4/9 & 0 & 1/3 \cr 3 & 0 & 0 & 0 & 1}$$

**Key principle for reducible chains:** the long-run behaviour from a transient state is a mixture of the limiting distributions of the recurrent classes, weighted by the absorption probabilities into each class.
