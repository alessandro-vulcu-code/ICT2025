> 1) Prove that a Markov chain with a finite number of states cannot have any null recurrent state.

A state can be:

- recurrent: if, starting from it, you go back with probability $1$;
- positive recurrent: if the average return time is finite;
- null recurrent: if you go back with probability $1$, but the average return time is infinite.

Assume there are no positive recurrent states.

$$
N = |E| < +\infty
$$

number of states.

$$
\sum_{j=1}^{N} P_{ij}^{(n)} = 1
$$

$$
\forall i \in E, \quad n > 0
$$

$$
1 = \lim_{n \to +\infty} \sum_{j=1}^{N} P_{ij}^{(n)}
= \sum_{j=1}^{N} \lim_{n \to +\infty} P_{ij}^{(n)} = 0
$$

since $|E|$ is finite and probabilities are positive only for positive recurrent states.

$\Rightarrow$ contradiction.

Then, suppose there is one null recurrent state, which will then belong to a finite null recurrent class.

Since a recurrent class is a Markov chain by itself, this is not possible.

---

> 2) Prove that for a renewal process $E[S_{N(t)+1}] = E[X](M(t) + 1)$.

Let $A(t) = E[S_{N(t)+1}] \leftarrow$ first epoch of the first renewal strictly after $t$.

Let $X_1 = x$.

**Idea:** calculate the mean value of the next renewal time after $t$.

If $x > t$, there is no renewal before $t$, so $S_{N(t)+1} = x$.

If $x \leq t$, the process renews at time $x$ and restarts independently.

Must wait for the first renewal after residual time $t - x$:

$$
E[S_{N(t)+1} \mid X_1 = x]
=
\begin{cases}
x, & x > t, \\
x + A(t - x), & x \leq t.
\end{cases}
$$

Integrating for $F$ we obtain:

$$
A(t) = \mu + \int_0^t A(t - x) \, dF(x)
$$

This is a renewal equation with constant forcing term $\mu$.

Standard solution of:

$$
Z(t) = a(t) + \int_0^t Z(t - x) \, dF(x)
$$

Here $a(t) = \mu$, so

$$
A(t) = \mu + \mu \int_0^t dH(x) = \mu(1 + M(t)).
$$

---

> 3) Prove that for a Markov chain the $n$-step transition probabilities, $P_{ij}^{(n)}$, satisfy the relationship

$$
P_{ij}^{(n)} = \sum_{m} P_{im}^{(k)} P_{mj}^{(n-k)}, \quad k = 0, 1, \ldots, n.
$$

Starting from state $i$, decompose the event $\{X_n = j\}$ according to the intermediate state at time $k$.

$$
P_{ij}^{(n)} = P(X_n = j \mid X_0 = i) = \ldots
$$

$$
\ldots =
\sum_m P(X_k = m \mid X_0 = i)
P(X_n = j \mid X_k = m, X_0 = i)
$$

By the Markov property, conditioned on $X_k = m$, the future after time $k$ is independent of the past.

The probability of moving from $m$ to $j$ in $n-k$ steps is $P_{mj}^{(n-k)}$.

Hence:

$$
P_{ij}^{(n)} = \sum_m P_{im}^{(k)} P_{mj}^{(n-k)}.
$$

---

> 4) State and prove the elementary renewal theorem.

If $\mu = E[X_1] \in (0, \infty)$, then

$$
\lim_{t \to \infty} \frac{M(t)}{t} = \frac{1}{\mu}.
$$

Proof: we know that $A(t) = E[S_{N(t)+1}]$.

Lower bound:

Since $S_{N(t)+1} > t$,

$$
t < \mu(M(t) + 1)
$$

so

$$
\frac{M(t)}{t} > \frac{1}{\mu} - \frac{1}{t}.
$$

Therefore:

$$
\lim_{t \to \infty} \frac{M(t)}{t} \geq \frac{1}{\mu}.
$$

Upper bound: $a > 0$, define truncated interarrival times:

$$
Y_n = \min(X_n, a), \quad \mu_a = E[Y_1].
$$

Let $N_a(t)$ be the renewal count and $M_a(t)$ the renewal function for the truncated process.

Since $Y_n \leq X_n$, then $N(t) \leq N_a(t)$ and $M(t) \leq M_a(t)$.

Also, $Y_n \leq a$, so:

$$
S_{N_a(t)+1}^{a} \leq t + a.
$$

Thus:

$$
\mu_a(M_a(t) + 1) = E[S_{N_a(t)+1}^{a}] \leq t + a.
$$

Therefore:

$$
\frac{M(t)}{t} \leq \frac{M_a(t)}{t}
\leq \frac{t + a}{\mu_a t} - \frac{1}{t}.
$$

Taking limits:

$$
\lim_{t \to \infty} \frac{M(t)}{t} \leq \frac{1}{\mu_a}.
$$

As $a \to \infty$, $\mu_a \to \mu$, so:

$$
\lim_{t \to \infty} \frac{M(t)}{t} \leq \frac{1}{\mu}.
$$

Combine limits:

$$
\lim_{t \to \infty} \frac{M(t)}{t} = \frac{1}{\mu}.
$$

---

> 5) Prove that in a Markov chain the period is a class property.

If states $i$ and $j$ communicate, then they have the same period.

$$
i \leftrightarrow j \Rightarrow d(i) = d(j).
$$

**Proof:**

$$
S_i = \{s \geq 1 : P_{ii}^{(s)} > 0\}
$$

is the set of possible return times to $i$.

$$
d(i) = \gcd S_i.
$$

Since $i \leftrightarrow j$, $\exists m,n \geq 1$ such that:

$$
P_{ij}^{(m)} > 0, \quad P_{ji}^{(n)} > 0.
$$

Take any $s \in S_i$. Then $P_{ii}^{(s)} > 0$.

By joining paths $j \to i \to i \to j$:

$$
P_{jj}^{(n+s+m)} \geq P_{ji}^{(n)} P_{ii}^{(s)} P_{ij}^{(m)} > 0.
$$

Thus $n+s+m, n+2s+m \in S_j$, so:

$$
d(j) \mid n+s+m, \quad d(j) \mid (n+2s+m).
$$

Subtract:

$$
d(j) \mid s.
$$

Since $\forall s \in S_i$, $d(j) \mid s$, then $d(j) \mid d(i)$.

By symmetry, $d(i) \mid d(j)$.

Hence, $d(i) = d(j)$.

---

> 6) Prove that for a Poisson process $X(t)$ the statistics of $X(s)$ conditioned on $X(t)$, $s < t$, is binomial, and provide the expression of $P[X(s) = k \mid X(t) = n]$.

If $X(t)$ is a Poisson process with rate $\lambda$, $0 < s < t$, $0 \leq k \leq n$, then

$$
P(X(s) = k \mid X(t) = n)
= \binom{n}{k} \left(\frac{s}{t}\right)^k
\left(1 - \frac{s}{t}\right)^{n-k}.
$$

Proof: independent increments:

$$
X(t) = X(s) + (X(t) - X(s))
$$

with $X(s) \sim \operatorname{Pois}(\lambda s)$ and $X(t) - X(s) \sim \operatorname{Pois}(\lambda(t-s))$, independent. Therefore:

$$
P(X(s) = k \mid X(t) = n)
= \frac{P(X(s) = k, X(t) - X(s) = n-k)}{P(X(t) = n)}
$$

$$
=
\frac{
e^{-\lambda s}\frac{(\lambda s)^k}{k!}
e^{-\lambda(t-s)}\frac{(\lambda(t-s))^{n-k}}{(n-k)!}
}{
e^{-\lambda t}\frac{(\lambda t)^n}{n!}
}
$$

$$
= \binom{n}{k} \left(\frac{s}{t}\right)^k
\left(1 - \frac{s}{t}\right)^{n-k}.
$$

---

> 7) Prove that if states $i$ and $j$ of a Markov chain communicate and $i$ is recurrent, then $j$ is also recurrent.

**Theorem:** If $i$ and $j$ communicate, and $i$ is recurrent, then also $j$ is recurrent.

**Proof:** $i \leftrightarrow j \Rightarrow \exists m,n > 1$ such that:

$$
P_{ji}^{(m)} > 0, \quad P_{ij}^{(n)} > 0.
$$

For $v > 0$:

$$
P_{jj}^{(m+v+n)} \geq P_{ji}^{(m)} P_{ii}^{(v)} P_{ij}^{(n)}.
$$

Summing over $v$:

$$
\sum_{v > 0} P_{jj}^{(m+v+n)}
\geq
P_{ji}^{(m)} P_{ij}^{(n)} \sum_{v > 0} P_{ii}^{(v)}.
$$

Since $i$ is recurrent:

$$
\sum_{v > 0} P_{ii}^{(v)} = \infty
$$

by the recurrence criterion.

Hence:

$$
\sum_{\ell > 0} P_{jj}^{(\ell)} = \infty,
$$

so $j$ is recurrent.

---

> 8) For a Poisson process of rate $\lambda$, prove that the interarrival times are iid exponential with mean $1/\lambda$.

Let $S_n$ be the time between the $(n-1)$st and $n$th event.

1. $P[S_0 > t] = P[\text{no arrivals in } [0,t)] = e^{-\lambda t}$.

   $\Rightarrow S_0 \sim \exp(\lambda)$ with mean $\frac{1}{\lambda}$.

2. $P[S_1 > t \mid S_0 = s] = P[\text{no arrivals in } (s,s+t) \mid S_0 = s]$.

   $\Rightarrow e^{-\lambda t}$, so $S_1 \sim \exp(\lambda)$ with mean $\frac{1}{\lambda}$.

3. $P[S_n > t \mid S_i = s_i, i = 0, \dots, n-1]$.

   $$
   \Rightarrow
   P[\text{no arrivals in } (s_0 + \dots + s_{n-1}, s_0 + \dots + s_{n-1}+t)
   \mid S_i = s_i, i = 0, \dots, n-1]
   $$

   $\Rightarrow e^{-\lambda t}$, so $S_n \sim \exp(\lambda)$ with mean $\frac{1}{\lambda}$.

The interarrival times are iid by independent and stationary increments.

---

> 9) Consider a random walk over the non-negative integers with the following transition probabilities: $P_{01} = 1$, $P_{i,i+1} = p$, $P_{i,i-1} = q$, $i > 0$, with $p + q = 1$. Study its behavior, and in particular characterize its recurrence or transience and derive the steady-state distribution.

$$
P =
\begin{array}{c|ccccc}
 & 0 & 1 & 2 & 3 & \cdots \\
\hline
0 & 0 & 1 & 0 & 0 & \cdots \\
1 & q & 0 & p & 0 & \cdots \\
2 & 0 & q & 0 & p & \cdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots
\end{array}
$$

Derive the steady-state distribution. We need to solve:

$$
x_i = \sum_{j=0}^{\infty} x_j P_{ji} = p x_{i-1} + q x_{i+1}
$$

where

$$
\sum_{k=0}^{\infty} x_k = 1.
$$

Firstly:

$$
x_0 = qx_1 \quad \Rightarrow \quad x_1 = \frac{x_0}{q}.
$$

$$
x_1 = x_0 + qx_2
\quad \Rightarrow \quad
x_2 = \frac{x_1 - x_0}{q}
= \frac{\frac{x_0}{q} - x_0}{q}
= \frac{p x_0}{q^2}.
$$

Generally, for $i \geq 1$:

$$
x_i = \frac{1}{p}\left(\frac{p}{q}\right)^i x_0.
$$

Using the normalization condition:

$$
1 = x_0 + \sum_{k=1}^{\infty} x_k
= x_0 + \frac{x_0}{p}\sum_{k=1}^{\infty}\left(\frac{p}{q}\right)^k.
$$

If $p < q$, the series converges and:

$$
x_0 = \frac{q-p}{2q},
$$

and for $i \geq 1$:

$$
x_i = \frac{1}{p}\left(\frac{p}{q}\right)^i \frac{q-p}{2q}.
$$

From this we can conclude that:

- If $p < q$, the chain is positive recurrent and admits the steady-state distribution above.
- If $p = q$, the chain is null recurrent and no steady-state distribution exists.
- If $p > q$, the chain is transient and no steady-state distribution exists.

---

> 11) For a Poisson process $X(t)$ of rate $\lambda$, state and derive the expression of $P[X(u) = k \mid X(t) = n]$ for the two cases (i) $0 < u < t$, $0 \leq k \leq n$ and (ii) $0 < t < u$, $0 \leq n \leq k$.

**Binomial theorem**

1. $0 < u < t$, $0 \leq k \leq n$

$$
P[X(u) = k \mid X(t) = n]
= \frac{P[X(u) = k, X(t) = n]}{P[X(t) = n]}
$$

$$
= \frac{P[X(u) = k, X(t) - X(u) = n - k]}{P[X(t) = n]}
$$

$$
= \binom{n}{k}\left(\frac{u}{t}\right)^k
\left(1 - \frac{u}{t}\right)^{n-k}.
$$

2. $0 < t < u$, $0 \leq n \leq k$

$$
P[X(u) = k \mid X(t) = n]
= \frac{P[X(u) = k, X(t) = n]}{P[X(t) = n]}
$$

$$
= \frac{P[X(t) = n, X(u) - X(t) = k - n]}{P[X(t) = n]}.
$$

By independent increments:

$$
= \frac{P[X(t) = n]P[X(u) - X(t) = k - n]}{P[X(t) = n]}
$$

and by stationary increments:

$$
= P[X(u - t) = k - n].
$$

Therefore:

$$
P[X(u) = k \mid X(t) = n]
= e^{-\lambda(u - t)} \frac{(\lambda(u - t))^{k - n}}{(k - n)!}.
$$

---

> 12) For a renewal process, state precisely (also providing a formal proof) what is the value of

$$
\lim_{t \to \infty} \frac{N(t)}{t} = \frac{1}{\mu}
$$

with probability $1$.

Proof:

$$
S_{N(t)} \leq t \leq S_{N(t)+1}.
$$

Divide by $N(t)$:

$$
\frac{S_{N(t)}}{N(t)} \leq \frac{t}{N(t)} \leq \frac{S_{N(t)+1}}{N(t)}.
$$

Since $N(t) \to \infty$ as $t \to \infty$, by the law of large numbers:

$$
\lim_{t \to \infty} \frac{S_{N(t)}}{N(t)}
= \lim_{n \to \infty} \frac{S_n}{n}
= \mu
$$

with probability $1$.

Also:

$$
\lim_{t \to \infty} \frac{S_{N(t)+1}}{N(t)}
=
\lim_{t \to \infty}
\frac{S_{N(t)+1}}{N(t)+1}
\cdot
\frac{N(t)+1}{N(t)}
= \mu \cdot 1
$$

with probability $1$.

Thus:

$$
\mu \leq \lim_{t \to \infty} \frac{t}{N(t)} \leq \mu
$$

with probability $1$, hence

$$
\lim_{t \to \infty} \frac{N(t)}{t} = \frac{1}{\mu}
$$

with probability $1$.
