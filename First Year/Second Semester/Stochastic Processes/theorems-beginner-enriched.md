---
type: exercise
tags: [exercise, exam-prep, markov-chains, poisson-process, renewal-process]
sources: [exams-theorems]
related:
  - "[[theorems/finite-state-positive-recurrence]]"
  - "[[theorems/chapman-kolmogorov]]"
  - "[[theorems/elementary-renewal-theorem]]"
  - "[[theorems/period-class-property]]"
  - "[[theorems/binomial-conditional-distribution]]"
  - "[[theorems/poisson-interarrival-exponential]]"
  - "[[theorems/recurrence-criterion]]"
---

# Theorems - Beginner Enriched Version

General notation used repeatedly:

- $E$ is the state space of a Markov chain.
- $P_{ij}^{(n)}$ is the probability of being in state $j$ after $n$ steps when the chain starts from state $i$.
- $X(t)$ is a Poisson counting process: it counts how many arrivals happened up to time $t$.
- In renewal-process questions, $X_1,X_2,\ldots$ are interarrival times, $S_n=X_1+\cdots+X_n$ is the time of the $n$-th renewal, $N(t)$ is the number of renewals up to time $t$, and $M(t)=E[N(t)]$.
- $\mu=E[X]$ or $\mu=E[X_1]$ is the mean interarrival time.

---

> 1) Prove that a Markov chain with a finite number of states cannot have any null recurrent state.

A state can be:

- recurrent: if, starting from it, you go back with probability $1$;
- positive recurrent: if the average return time is finite;
- null recurrent: if you go back with probability $1$, but the average return time is infinite.

Here "go back" means "return to the same state at some future time".

More formally, if the chain starts from state $i$, define the first positive return time

$$
T_i^+ = \inf\{n \geq 1 : X_n = i\}.
$$

Then:

- $i$ is recurrent if $P_i(T_i^+ < \infty)=1$;
- $i$ is positive recurrent if $E_i[T_i^+]<\infty$;
- $i$ is null recurrent if $P_i(T_i^+ < \infty)=1$ but $E_i[T_i^+]=\infty$.

Assume there are no positive recurrent states.

$$
N = |E| < +\infty
$$

where $N$ is the number of states. The notation $|E|$ means "the size of $E$".

For every starting state $i$, after $n$ steps the chain must be somewhere in $E$. Therefore the probabilities of being in all possible states must add up to $1$:

$$
\sum_{j=1}^{N} P_{ij}^{(n)} = 1
$$

$$
\forall i \in E, \quad n > 0.
$$

Now use a standard Markov-chain fact:

- if a state is transient, then the probability of being there at very large times goes to $0$;
- if a state is null recurrent, then the probability of being there at very large times also goes to $0$;
- positive recurrent states are the only states that can carry non-zero long-run probability mass.

Under the assumption "there are no positive recurrent states", this gives

$$
\lim_{n \to +\infty} P_{ij}^{(n)} = 0
$$

for every pair of states $i,j$.

Because $|E|$ is finite, the limit can pass through the finite sum:

$$
1 = \lim_{n \to +\infty} \sum_{j=1}^{N} P_{ij}^{(n)}
= \sum_{j=1}^{N} \lim_{n \to +\infty} P_{ij}^{(n)} = 0.
$$

This says $1=0$, which is impossible. So the assumption was false: a finite Markov chain must contain at least one positive recurrent state.

Now suppose there is one null recurrent state. A recurrent state belongs to a recurrent class, meaning a set of states that communicate with each other and cannot be left once entered.

Since the original state space is finite, this recurrent class is also finite. Once the chain is inside this class, the class behaves like a finite Markov chain by itself. By the argument above, this finite class must contain a positive recurrent state.

But recurrence type is a class property: inside one communicating recurrent class, states cannot be partly positive recurrent and partly null recurrent. So the supposed null recurrent state would be in a finite class that must be positive recurrent, contradiction.

Therefore a finite Markov chain cannot have any null recurrent state.

---

> 2) Prove that for a renewal process $E[S_{N(t)+1}] = E[X](M(t) + 1)$.

Before the proof, decode the notation:

- $X_1,X_2,\ldots$ are the times between renewals.
- $E[X]=\mu$ is the average time between two renewals.
- $S_n=X_1+\cdots+X_n$ is the time of the $n$-th renewal.
- $N(t)$ is the number of renewals that have happened by time $t$.
- $S_{N(t)+1}$ is the first renewal epoch strictly after $t$.
- $M(t)=E[N(t)]$ is the expected number of renewals by time $t$.

Let

$$
A(t) = E[S_{N(t)+1}]
$$

where $A(t)$ is the expected time of the first renewal strictly after $t$.

Let $X_1 = x$.

This means we condition on the first interarrival time being equal to $x$.

**Idea:** calculate the mean value of the next renewal time after $t$ by splitting into two cases.

If $x > t$, the first renewal happens after $t$. So the first renewal after $t$ is exactly the first renewal:

$$
S_{N(t)+1} = x.
$$

If $x \leq t$, the first renewal happens at time $x$. After a renewal, the process starts again independently, with the same probabilistic behavior as at time $0$. This restart property is the main idea of renewal theory.

After time $x$, there is still residual time $t-x$ to cover. The expected time, measured from the restart point, of the first renewal after that residual time is $A(t-x)$. Since the restart point itself occurs at time $x$, the absolute time is

$$
x + A(t-x).
$$

Therefore

$$
E[S_{N(t)+1} \mid X_1 = x]
=
\begin{cases}
x, & x > t, \\
x + A(t - x), & x \leq t.
\end{cases}
$$

Now integrate over all possible values of $x$. Let $F$ be the distribution function of $X_1$. Writing $dF(x)$ means "average with respect to the distribution of $X_1$":

$$
A(t)
= \int_{(0,t]} [x + A(t-x)]\,dF(x)
+ \int_{(t,\infty)} x\,dF(x).
$$

Combine the two terms containing $x$:

$$
\int_{(0,t]} x\,dF(x) + \int_{(t,\infty)} x\,dF(x)
= \int_{(0,\infty)} x\,dF(x)
= \mu.
$$

So

$$
A(t) = \mu + \int_0^t A(t - x) \, dF(x).
$$

This is a renewal equation with constant forcing term $\mu$.

Standard solution of:

$$
Z(t) = a(t) + \int_0^t Z(t - x) \, dF(x)
$$

is

$$
Z(t)=a(t)+\int_0^t a(t-x)\,dH(x),
$$

where $H$ is the renewal measure. In this course notation, for the renewal function,

$$
H(t)=M(t).
$$

Here $a(t) = \mu$, a constant. Therefore

$$
A(t) = \mu + \mu \int_0^t dH(x).
$$

Since $\int_0^t dH(x)=M(t)$,

$$
A(t) = \mu(1 + M(t)).
$$

Finally, because $A(t)=E[S_{N(t)+1}]$ and $\mu=E[X]$,

$$
E[S_{N(t)+1}] = E[X](M(t)+1).
$$

---

> 3) Prove that for a Markov chain the $n$-step transition probabilities, $P_{ij}^{(n)}$, satisfy the relationship

$$
P_{ij}^{(n)} = \sum_{m} P_{im}^{(k)} P_{mj}^{(n-k)}, \quad k = 0, 1, \ldots, n.
$$

This is the Chapman-Kolmogorov equation.

Meaning of the symbols:

- $P_{ij}^{(n)}$ means: start from $i$, be in $j$ after $n$ steps.
- $k$ is an intermediate time between $0$ and $n$.
- $m$ is the intermediate state visited at time $k$.
- $P_{im}^{(k)}$ means: go from $i$ to $m$ in $k$ steps.
- $P_{mj}^{(n-k)}$ means: go from $m$ to $j$ in the remaining $n-k$ steps.

Starting from state $i$, decompose the event $\{X_n = j\}$ according to the intermediate state at time $k$.

The chain must be in exactly one state $m$ at time $k$. So we split the probability into all possible cases:

$$
P_{ij}^{(n)} = P(X_n = j \mid X_0 = i)
$$

$$
=
\sum_m P(X_k = m, X_n = j \mid X_0 = i).
$$

Use the multiplication rule for conditional probability:

$$
P(X_k = m, X_n = j \mid X_0 = i)
$$

$$
=
P(X_k = m \mid X_0 = i)
P(X_n = j \mid X_k = m, X_0 = i).
$$

Therefore

$$
P_{ij}^{(n)}
=
\sum_m P(X_k = m \mid X_0 = i)
P(X_n = j \mid X_k = m, X_0 = i).
$$

By the Markov property, conditioned on $X_k = m$, the future after time $k$ is independent of the past.

So knowing $X_0=i$ gives no extra information once we already know $X_k=m$:

$$
P(X_n = j \mid X_k = m, X_0 = i)
=
P(X_n = j \mid X_k = m).
$$

Because the chain is homogeneous, the probability of moving from $m$ to $j$ in $n-k$ steps is

$$
P_{mj}^{(n-k)}.
$$

Also,

$$
P(X_k=m\mid X_0=i)=P_{im}^{(k)}.
$$

Hence:

$$
P_{ij}^{(n)} = \sum_m P_{im}^{(k)} P_{mj}^{(n-k)}.
$$

For $k=0$, this says "start from $i$ immediately". For $k=n$, this says "the intermediate time is already the final time". Both edge cases work if $P^{(0)}$ is the identity matrix.

---

> 4) State and prove the elementary renewal theorem.

If $\mu = E[X_1] \in (0, \infty)$, then

$$
\lim_{t \to \infty} \frac{M(t)}{t} = \frac{1}{\mu}.
$$

Interpretation:

- $M(t)$ is the expected number of renewals by time $t$.
- $\frac{M(t)}{t}$ is the expected renewal rate per unit time.
- $\mu$ is the average time between renewals.
- So $\frac{1}{\mu}$ is the intuitive long-run number of renewals per unit time.

Proof: we know that

$$
A(t) = E[S_{N(t)+1}]
$$

and from item 2:

$$
A(t)=\mu(M(t)+1).
$$

Lower bound:

Since $S_{N(t)+1}$ is the first renewal time strictly after $t$,

$$
S_{N(t)+1} > t.
$$

Taking expectations:

$$
E[S_{N(t)+1}] > t.
$$

Using $E[S_{N(t)+1}]=\mu(M(t)+1)$:

$$
t < \mu(M(t) + 1).
$$

Divide by $\mu t$:

$$
\frac{1}{\mu} < \frac{M(t)+1}{t}.
$$

So

$$
\frac{M(t)}{t} > \frac{1}{\mu} - \frac{1}{t}.
$$

When $t$ becomes very large, $\frac{1}{t}$ goes to $0$. Therefore:

$$
\lim_{t \to \infty} \frac{M(t)}{t} \geq \frac{1}{\mu}.
$$

Strictly speaking, this line proves the lower bound for the possible limit, or more formally:

$$
\liminf_{t \to \infty} \frac{M(t)}{t} \geq \frac{1}{\mu}.
$$

Upper bound: $a > 0$, define truncated interarrival times:

$$
Y_n = \min(X_n, a), \quad \mu_a = E[Y_1].
$$

Meaning:

- $Y_n$ is equal to $X_n$ if $X_n\leq a$;
- $Y_n$ is cut down to $a$ if $X_n>a$;
- therefore $Y_n \leq X_n$ always;
- $\mu_a$ is the average truncated interarrival time.

Let $N_a(t)$ be the renewal count and $M_a(t)$ the renewal function for the truncated process.

Since $Y_n \leq X_n$, the truncated process has shorter or equal interarrival times. Shorter waiting times mean renewals happen earlier, so by time $t$ the truncated process has at least as many renewals:

$$
N(t) \leq N_a(t)
$$

and after taking expectations:

$$
M(t) \leq M_a(t).
$$

Also, $Y_n \leq a$, so after time $t$, the next truncated renewal cannot be more than $a$ time units away:

$$
S_{N_a(t)+1}^{a} \leq t + a.
$$

The superscript $a$ reminds us that this renewal epoch belongs to the truncated process.

Apply item 2 to the truncated process:

$$
\mu_a(M_a(t) + 1) = E[S_{N_a(t)+1}^{a}].
$$

Using $S_{N_a(t)+1}^{a} \leq t+a$:

$$
\mu_a(M_a(t) + 1) = E[S_{N_a(t)+1}^{a}] \leq t + a.
$$

Therefore:

$$
M_a(t)+1 \leq \frac{t+a}{\mu_a}.
$$

Subtract $1$:

$$
M_a(t) \leq \frac{t+a}{\mu_a}-1.
$$

Since $M(t)\leq M_a(t)$:

$$
\frac{M(t)}{t} \leq \frac{M_a(t)}{t}
\leq \frac{t + a}{\mu_a t} - \frac{1}{t}.
$$

Taking large $t$ with fixed $a$:

$$
\lim_{t \to \infty} \frac{M(t)}{t} \leq \frac{1}{\mu_a}.
$$

More formally:

$$
\limsup_{t \to \infty} \frac{M(t)}{t} \leq \frac{1}{\mu_a}.
$$

As $a \to \infty$, the truncation disappears. Since $Y_n=\min(X_n,a)$ increases to $X_n$,

$$
\mu_a = E[Y_1] \to E[X_1]=\mu.
$$

Thus

$$
\frac{1}{\mu_a} \to \frac{1}{\mu}.
$$

So:

$$
\lim_{t \to \infty} \frac{M(t)}{t} \leq \frac{1}{\mu}.
$$

Combine the lower and upper bounds:

$$
\lim_{t \to \infty} \frac{M(t)}{t} = \frac{1}{\mu}.
$$

---

> 5) Prove that in a Markov chain the period is a class property.

If states $i$ and $j$ communicate, then they have the same period.

$$
i \leftrightarrow j \Rightarrow d(i) = d(j).
$$

Meaning:

- $i \leftrightarrow j$ means $i$ can reach $j$ and $j$ can reach $i$ in some positive number of steps.
- $d(i)$ is the period of state $i$.
- Period means the greatest common divisor of all possible return times to that state.

**Proof:**

$$
S_i = \{s \geq 1 : P_{ii}^{(s)} > 0\}
$$

is the set of possible return times to $i$.

For example, if it is possible to return to $i$ after $2,4,6,\ldots$ steps only, then

$$
S_i=\{2,4,6,\ldots\}
$$

and

$$
d(i)=2.
$$

In general:

$$
d(i) = \gcd S_i.
$$

Since $i \leftrightarrow j$, $\exists m,n \geq 1$ such that:

$$
P_{ij}^{(m)} > 0, \quad P_{ji}^{(n)} > 0.
$$

This means:

- there is a possible path from $i$ to $j$ in $m$ steps;
- there is a possible path from $j$ to $i$ in $n$ steps.

Take any $s \in S_i$. Then

$$
P_{ii}^{(s)} > 0.
$$

This means there is a possible return path from $i$ back to $i$ in $s$ steps.

Now build a return path from $j$ back to $j$:

1. go from $j$ to $i$ in $n$ steps;
2. go from $i$ back to $i$ in $s$ steps;
3. go from $i$ to $j$ in $m$ steps.

By joining paths $j \to i \to i \to j$:

$$
P_{jj}^{(n+s+m)} \geq P_{ji}^{(n)} P_{ii}^{(s)} P_{ij}^{(m)} > 0.
$$

So $n+s+m$ is a possible return time to $j$.

If we repeat the $i \to i$ loop twice, we also get

$$
P_{jj}^{(n+2s+m)} > 0.
$$

Thus

$$
n+s+m, n+2s+m \in S_j.
$$

Since $d(j)$ is the greatest common divisor of all numbers in $S_j$, it divides every element of $S_j$:

$$
d(j) \mid n+s+m, \quad d(j) \mid (n+2s+m).
$$

Subtract the first number from the second:

$$
(n+2s+m)-(n+s+m)=s.
$$

Therefore:

$$
d(j) \mid s.
$$

This works for every $s \in S_i$. So $d(j)$ divides every possible return time to $i$. Hence it divides their greatest common divisor:

$$
d(j) \mid d(i).
$$

By symmetry, repeat the same argument with $i$ and $j$ exchanged:

$$
d(i) \mid d(j).
$$

If two positive integers divide each other, they are equal.

Hence,

$$
d(i) = d(j).
$$

So period is a class property.

---

> 6) Prove that for a Poisson process $X(t)$ the statistics of $X(s)$ conditioned on $X(t)$, $s < t$, is binomial, and provide the expression of $P[X(s) = k \mid X(t) = n]$.

If $X(t)$ is a Poisson process with rate $\lambda$, $0 < s < t$, $0 \leq k \leq n$, then

$$
P(X(s) = k \mid X(t) = n)
= \binom{n}{k} \left(\frac{s}{t}\right)^k
\left(1 - \frac{s}{t}\right)^{n-k}.
$$

Meaning:

- $X(s)$ is the number of arrivals up to time $s$.
- $X(t)$ is the number of arrivals up to the later time $t$.
- We are told that exactly $n$ arrivals happened by time $t$.
- We ask for the probability that exactly $k$ of those $n$ arrivals already happened by time $s$.

The answer is binomial because, conditional on the total number $n$ in $[0,t]$, each arrival is equally likely to fall in the subinterval $[0,s]$. The fraction of the interval is $s/t$.

Proof: independent increments:

$$
X(t) = X(s) + (X(t) - X(s)).
$$

Here:

- $X(s)$ counts arrivals in $[0,s]$;
- $X(t)-X(s)$ counts arrivals in $(s,t]$;
- these two intervals are disjoint, so the two counts are independent.

Also:

$$
X(s) \sim \operatorname{Pois}(\lambda s)
$$

and

$$
X(t) - X(s) \sim \operatorname{Pois}(\lambda(t-s)).
$$

Therefore:

$$
P(X(s) = k \mid X(t) = n)
= \frac{P(X(s) = k, X(t) - X(s) = n-k)}{P(X(t) = n)}.
$$

The numerator is a product because the increments are independent:

$$
P(X(s)=k, X(t)-X(s)=n-k)
$$

$$
=
P(X(s)=k)P(X(t)-X(s)=n-k).
$$

Use the Poisson probability formula:

$$
P(Y=r)=e^{-\theta}\frac{\theta^r}{r!}
\quad \text{if } Y\sim\operatorname{Pois}(\theta).
$$

So:

$$
P(X(s) = k \mid X(t) = n)
=
\frac{
e^{-\lambda s}\frac{(\lambda s)^k}{k!}
e^{-\lambda(t-s)}\frac{(\lambda(t-s))^{n-k}}{(n-k)!}
}{
e^{-\lambda t}\frac{(\lambda t)^n}{n!}
}.
$$

Now simplify:

- $e^{-\lambda s}e^{-\lambda(t-s)}=e^{-\lambda t}$, so exponential factors cancel;
- $\lambda^k\lambda^{n-k}=\lambda^n$, so powers of $\lambda$ cancel;
- the factorial part gives $\frac{n!}{k!(n-k)!}=\binom{n}{k}$;
- the powers of $s$ and $t-s$ divided by $t^n$ give $\left(\frac{s}{t}\right)^k\left(\frac{t-s}{t}\right)^{n-k}$.

Therefore:

$$
P(X(s) = k \mid X(t) = n)
= \binom{n}{k} \left(\frac{s}{t}\right)^k
\left(1 - \frac{s}{t}\right)^{n-k}.
$$

---

> 7) Prove that if states $i$ and $j$ of a Markov chain communicate and $i$ is recurrent, then $j$ is also recurrent.

**Theorem:** If $i$ and $j$ communicate, and $i$ is recurrent, then also $j$ is recurrent.

Meaning:

- $i \leftrightarrow j$ means $i$ can reach $j$ and $j$ can reach $i$.
- $i$ recurrent means that if the chain starts at $i$, it returns to $i$ with probability $1$.
- We want to prove that $j$ also has return probability $1$.

We use the recurrence criterion:

$$
i \text{ is recurrent}
\quad \Longleftrightarrow \quad
\sum_{v>0} P_{ii}^{(v)}=\infty.
$$

So instead of directly proving return probability $1$, we prove that the same infinite-sum criterion holds for $j$.

**Proof:** $i \leftrightarrow j \Rightarrow \exists m,n > 0$ such that:

$$
P_{ji}^{(m)} > 0, \quad P_{ij}^{(n)} > 0.
$$

This means:

- from $j$ it is possible to reach $i$ in $m$ steps;
- from $i$ it is possible to reach $j$ in $n$ steps.

For $v > 0$:

$$
P_{jj}^{(m+v+n)} \geq P_{ji}^{(m)} P_{ii}^{(v)} P_{ij}^{(n)}.
$$

Why this inequality is true:

- one possible way to return from $j$ to $j$ is:
  $$
  j \to i \to i \to j;
  $$
- go from $j$ to $i$ in $m$ steps;
- stay in the sense of returning from $i$ to $i$ in $v$ steps;
- go from $i$ to $j$ in $n$ steps.

The probability of this specific path structure is

$$
P_{ji}^{(m)} P_{ii}^{(v)} P_{ij}^{(n)}.
$$

There may be other ways to return from $j$ to $j$ in $m+v+n$ steps, so the total probability $P_{jj}^{(m+v+n)}$ is at least this product.

Summing over $v$:

$$
\sum_{v > 0} P_{jj}^{(m+v+n)}
\geq
P_{ji}^{(m)} P_{ij}^{(n)} \sum_{v > 0} P_{ii}^{(v)}.
$$

The terms $P_{ji}^{(m)}$ and $P_{ij}^{(n)}$ do not depend on $v$, so they can be pulled outside the sum.

Since $i$ is recurrent:

$$
\sum_{v > 0} P_{ii}^{(v)} = \infty
$$

by the recurrence criterion.

Also,

$$
P_{ji}^{(m)} P_{ij}^{(n)} > 0.
$$

A positive constant times infinity is still infinity, so:

$$
\sum_{v > 0} P_{jj}^{(m+v+n)} = \infty.
$$

The sum above is only part of the full sum

$$
\sum_{\ell > 0} P_{jj}^{(\ell)}.
$$

Therefore the full sum is also infinite:

$$
\sum_{\ell > 0} P_{jj}^{(\ell)} = \infty.
$$

By the recurrence criterion, $j$ is recurrent.

---

> 8) For a Poisson process of rate $\lambda$, prove that the interarrival times are iid exponential with mean $1/\lambda$.

In this item, keep the source notation:

$$
S_n
$$

means the time between the $(n-1)$st and $n$th event. This is local notation for this proof. In renewal questions, $S_n$ often means the epoch of the $n$-th renewal, but here it means interarrival time.

Let $S_n$ be the time between the $(n-1)$st and $n$th event.

We need to prove two things:

- each $S_n$ has exponential distribution with rate $\lambda$;
- the variables $S_0,S_1,S_2,\ldots$ are independent and identically distributed.

1. First interarrival time:

$$
P[S_0 > t] = P[\text{no arrivals in } [0,t)].
$$

For a Poisson process with rate $\lambda$,

$$
X(t)\sim\operatorname{Pois}(\lambda t).
$$

So

$$
P[\text{no arrivals in } [0,t)] = P[X(t)=0].
$$

Using the Poisson formula:

$$
P[X(t)=0]=e^{-\lambda t}\frac{(\lambda t)^0}{0!}=e^{-\lambda t}.
$$

Therefore:

$$
P[S_0 > t] = e^{-\lambda t}.
$$

This is exactly the survival function of an exponential random variable with rate $\lambda$.

So

$$
S_0 \sim \exp(\lambda)
$$

with mean

$$
\frac{1}{\lambda}.
$$

2. Second interarrival time:

$$
P[S_1 > t \mid S_0 = s]
= P[\text{no arrivals in } (s,s+t) \mid S_0 = s].
$$

If $S_0=s$, the first arrival happened at time $s$. The next waiting time is bigger than $t$ exactly when no arrivals happen in the interval $(s,s+t)$.

Poisson processes have stationary increments, so the number of arrivals in an interval depends only on the interval length, not on its location. The interval $(s,s+t)$ has length $t$.

They also have independent increments, so the future interval after time $s$ is independent of what happened before.

Therefore:

$$
P[S_1 > t \mid S_0 = s] = e^{-\lambda t}.
$$

So

$$
S_1 \sim \exp(\lambda)
$$

with mean

$$
\frac{1}{\lambda}.
$$

3. General interarrival time:

$$
P[S_n > t \mid S_i = s_i, i = 0, \dots, n-1].
$$

The condition

$$
S_i=s_i,\quad i=0,\dots,n-1
$$

means we know all previous waiting times. Therefore we know the time of the previous arrival:

$$
s_0+s_1+\cdots+s_{n-1}.
$$

The event $S_n>t$ means no arrivals occur in the next interval of length $t$:

$$
P[\text{no arrivals in } (s_0 + \dots + s_{n-1}, s_0 + \dots + s_{n-1}+t)
\mid S_i = s_i, i = 0, \dots, n-1].
$$

By independent and stationary increments, this probability depends only on the length $t$ and not on the past:

$$
e^{-\lambda t}.
$$

Thus

$$
S_n \sim \exp(\lambda)
$$

with mean

$$
\frac{1}{\lambda}.
$$

Since every $S_n$ has the same distribution and each future waiting time is independent of previous waiting times, the interarrival times are iid exponential with mean $1/\lambda$.

---

> 9) Consider a random walk over the non-negative integers with the following transition probabilities: $P_{01} = 1$, $P_{i,i+1} = p$, $P_{i,i-1} = q$, $i > 0$, with $p + q = 1$. Study its behavior, and in particular characterize its recurrence or transience and derive the steady-state distribution.

The state space is

$$
\{0,1,2,3,\ldots\}.
$$

The transition rules are:

- from $0$, the chain must go to $1$;
- from any $i>0$, the chain goes one step right to $i+1$ with probability $p$;
- from any $i>0$, the chain goes one step left to $i-1$ with probability $q$;
- $p+q=1$.

So $p$ is the probability of moving away from $0$, and $q$ is the probability of moving toward $0$.

The transition matrix is:

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

Meaning:

- $x_i$ is the steady-state probability of state $i$.
- The equation $x_i = \sum_j x_jP_{ji}$ says: long-run probability of being in $i$ equals total incoming probability flow into $i$.
- The normalization condition says all state probabilities must add up to $1$.

For state $0$, the only way to enter $0$ is from state $1$ with probability $q$:

$$
x_0 = qx_1.
$$

So:

$$
x_1 = \frac{x_0}{q}.
$$

For state $1$, the chain can enter from state $0$ with probability $1$, or from state $2$ with probability $q$:

$$
x_1 = x_0 + qx_2.
$$

Solve for $x_2$:

$$
x_2 = \frac{x_1 - x_0}{q}.
$$

Substitute $x_1=\frac{x_0}{q}$:

$$
x_2
= \frac{\frac{x_0}{q} - x_0}{q}
= \frac{x_0(1-q)}{q^2}.
$$

Since $p+q=1$, we have $1-q=p$. Therefore:

$$
x_2 = \frac{p x_0}{q^2}.
$$

Generally, for $i \geq 1$:

$$
x_i = \frac{1}{p}\left(\frac{p}{q}\right)^i x_0.
$$

Check the formula:

- for $i=1$:
  $$
  x_1=\frac{1}{p}\frac{p}{q}x_0=\frac{x_0}{q};
  $$
- for $i=2$:
  $$
  x_2=\frac{1}{p}\frac{p^2}{q^2}x_0=\frac{p x_0}{q^2}.
  $$

Now use the normalization condition:

$$
1 = x_0 + \sum_{k=1}^{\infty} x_k.
$$

Substitute the formula for $x_k$:

$$
1 = x_0 + \frac{x_0}{p}\sum_{k=1}^{\infty}\left(\frac{p}{q}\right)^k.
$$

This is a geometric series with ratio $\frac{p}{q}$.

It converges only if

$$
\frac{p}{q}<1,
$$

which means

$$
p<q.
$$

If $p < q$, the series converges and:

$$
\sum_{k=1}^{\infty}\left(\frac{p}{q}\right)^k
=
\frac{\frac{p}{q}}{1-\frac{p}{q}}
=
\frac{p}{q-p}.
$$

Therefore:

$$
1
= x_0 + \frac{x_0}{p}\frac{p}{q-p}
= x_0 + \frac{x_0}{q-p}
= x_0\left(1+\frac{1}{q-p}\right).
$$

So:

$$
x_0
=
\frac{1}{1+\frac{1}{q-p}}
=
\frac{q-p}{1+q-p}.
$$

Since $p+q=1$,

$$
1+q-p = p+q+q-p = 2q.
$$

Hence:

$$
x_0 = \frac{q-p}{2q}.
$$

and for $i \geq 1$:

$$
x_i = \frac{1}{p}\left(\frac{p}{q}\right)^i \frac{q-p}{2q}.
$$

From this we can conclude that:

- If $p < q$, the chain is positive recurrent and admits the steady-state distribution above.
- If $p = q$, the chain is null recurrent and no steady-state distribution exists.
- If $p > q$, the chain is transient and no steady-state distribution exists.

Why these cases make sense:

- $p<q$: movement toward $0$ is more likely than movement away from $0$, so the chain keeps coming back often enough to have a long-run distribution.
- $p=q$: there is no drift. The chain still returns to states with probability $1$, but return times have infinite mean, so it is null recurrent.
- $p>q$: movement away from $0$ is more likely, so there is positive probability of drifting to infinity and never returning; the chain is transient.

One extra exam-relevant note: the chain has period $2$, because every move changes parity. From an even state you go to an odd state, and from an odd state you go to an even state. So returns can only happen in even numbers of steps.

---

> 11) For a Poisson process $X(t)$ of rate $\lambda$, state and derive the expression of $P[X(u) = k \mid X(t) = n]$ for the two cases (i) $0 < u < t$, $0 \leq k \leq n$ and (ii) $0 < t < u$, $0 \leq n \leq k$.

**Binomial theorem**

We compare two observation times, $t$ and $u$.

There are two different cases:

- $u<t$: we ask about an earlier time $u$ given the later count at time $t$;
- $t<u$: we ask about a later time $u$ given the earlier count at time $t$.

1. $0 < u < t$, $0 \leq k \leq n$

Here $u$ is before $t$. If $X(t)=n$, then by time $t$ there are exactly $n$ arrivals. We ask how many of those already occurred by time $u$.

$$
P[X(u) = k \mid X(t) = n]
= \frac{P[X(u) = k, X(t) = n]}{P[X(t) = n]}.
$$

The event $\{X(u)=k, X(t)=n\}$ is the same as:

- $k$ arrivals in $[0,u]$;
- $n-k$ arrivals in $(u,t]$.

So:

$$
P[X(u) = k \mid X(t) = n]
= \frac{P[X(u) = k, X(t) - X(u) = n - k]}{P[X(t) = n]}.
$$

Using the same calculation as item 6:

$$
= \binom{n}{k}\left(\frac{u}{t}\right)^k
\left(1 - \frac{u}{t}\right)^{n-k}.
$$

So:

$$
P[X(u) = k \mid X(t) = n]
= \binom{n}{k}\left(\frac{u}{t}\right)^k
\left(1 - \frac{u}{t}\right)^{n-k}.
$$

2. $0 < t < u$, $0 \leq n \leq k$

Here $t$ is before $u$. We already know:

$$
X(t)=n.
$$

To have $X(u)=k$, the process must have exactly $k-n$ new arrivals during the interval $(t,u]$.

Start from conditional probability:

$$
P[X(u) = k \mid X(t) = n]
= \frac{P[X(u) = k, X(t) = n]}{P[X(t) = n]}.
$$

Rewrite the joint event:

$$
\{X(u)=k, X(t)=n\}
=
\{X(t)=n, X(u)-X(t)=k-n\}.
$$

Thus:

$$
P[X(u) = k \mid X(t) = n]
= \frac{P[X(t) = n, X(u) - X(t) = k - n]}{P[X(t) = n]}.
$$

By independent increments:

$$
P[X(t) = n, X(u) - X(t) = k - n]
=
P[X(t)=n]P[X(u)-X(t)=k-n].
$$

Therefore:

$$
= \frac{P[X(t)=n]P[X(u)-X(t)=k-n]}{P[X(t)=n]}.
$$

Cancel $P[X(t)=n]$:

$$
=P[X(u)-X(t)=k-n].
$$

By stationary increments, the distribution of $X(u)-X(t)$ depends only on the length $u-t$:

$$
X(u)-X(t)\sim\operatorname{Pois}(\lambda(u-t)).
$$

Equivalently:

$$
X(u)-X(t) \stackrel{d}{=} X(u-t).
$$

Therefore:

$$
P[X(u) = k \mid X(t) = n]
= P[X(u - t) = k - n].
$$

Using the Poisson formula:

$$
P[X(u) = k \mid X(t) = n]
= e^{-\lambda(u - t)} \frac{(\lambda(u - t))^{k - n}}{(k - n)!}.
$$

If $k<n$, the probability is $0$, because a Poisson process count cannot decrease over time.

---

> 12) For a renewal process, state precisely (also providing a formal proof) what is the value of

$$
\lim_{t \to \infty} \frac{N(t)}{t} = \frac{1}{\mu}
$$

with probability $1$.

This is a stronger statement than the elementary renewal theorem:

- item 4 says the expected rate satisfies $M(t)/t \to 1/\mu$;
- item 12 says the actual random rate satisfies $N(t)/t \to 1/\mu$ with probability $1$.

"With probability $1$" means "almost surely": exceptions may exist mathematically, but they have probability $0$.

Proof:

$$
S_{N(t)} \leq t \leq S_{N(t)+1}.
$$

Meaning:

- $S_{N(t)}$ is the last renewal time not exceeding $t$;
- $S_{N(t)+1}$ is the first renewal time after $t$;
- therefore $t$ lies between them.

Divide by $N(t)$:

$$
\frac{S_{N(t)}}{N(t)} \leq \frac{t}{N(t)} \leq \frac{S_{N(t)+1}}{N(t)}.
$$

For small $t$, it is possible that $N(t)=0$, so division by $N(t)$ is not allowed. This does not matter for the limit, because as $t\to\infty$, the renewal count $N(t)$ goes to infinity with probability $1$.

Since $N(t) \to \infty$ as $t \to \infty$, by the law of large numbers:

$$
\lim_{t \to \infty} \frac{S_{N(t)}}{N(t)}
= \lim_{n \to \infty} \frac{S_n}{n}
= \mu
$$

with probability $1$.

Why this is true:

$$
S_n=X_1+\cdots+X_n.
$$

So

$$
\frac{S_n}{n}
=
\frac{X_1+\cdots+X_n}{n}.
$$

This is the sample average of the i.i.d. interarrival times. By the strong law of large numbers, it converges to their mean $\mu$.

Also:

$$
\lim_{t \to \infty} \frac{S_{N(t)+1}}{N(t)}
=
\lim_{t \to \infty}
\frac{S_{N(t)+1}}{N(t)+1}
\cdot
\frac{N(t)+1}{N(t)}.
$$

The first factor converges to $\mu$ by the same law of large numbers:

$$
\frac{S_{N(t)+1}}{N(t)+1}\to\mu.
$$

The second factor is

$$
\frac{N(t)+1}{N(t)}=1+\frac{1}{N(t)}.
$$

Since $N(t)\to\infty$,

$$
1+\frac{1}{N(t)}\to1.
$$

Therefore:

$$
\lim_{t \to \infty} \frac{S_{N(t)+1}}{N(t)}
= \mu \cdot 1
$$

with probability $1$.

Thus:

$$
\mu \leq \lim_{t \to \infty} \frac{t}{N(t)} \leq \mu
$$

with probability $1$, hence

$$
\lim_{t \to \infty} \frac{t}{N(t)} = \mu
$$

with probability $1$.

Taking reciprocals gives

$$
\lim_{t \to \infty} \frac{N(t)}{t} = \frac{1}{\mu}
$$

with probability $1$.

---
