# Chapter 3 - Long Run Behaviour of Markov Chains

## Table of Contents

- [[#3.1 Regular Markov Chains|3.1 Regular Markov Chains]]
  - [[#3.1.1 Interpretation of the Limiting Distribution|3.1.1 Interpretation of the Limiting Distribution]]
- [[#3.2 Non regular Markov chains|3.2 Non regular Markov chains]]
- [[#3.3 Classification of States|3.3 Classification of States]]
  - [[#3.3.1 Periodicity|3.3.1 Periodicity]]
  - [[#3.3.2 Recurrence|3.3.2 Recurrence]]
  - [[#Improper random variables|Improper random variables]]
  - [[#3.3.3 Fubini's Theorem|3.3.3 Fubini's Theorem]]
  - [[#Corollary - Recurrence Is a Class Property|Corollary - Recurrence Is a Class Property]]
- [[#3.4 Basic Limit Theorem of Markov Chains|3.4 Basic Limit Theorem of Markov Chains]]
  - [[#Example 8 - Recurrence of G/M/1 Queue|Example 8 - Recurrence of G/M/1 Queue]]
  - [[#3.4.1 Periodic generalization|3.4.1 Periodic generalization]]
- [[#3.5 Reducible Markov chains|3.5 Reducible Markov chains]]
  - [[#3.5.1 Another behaviour of infinite Markov chains|3.5.1 Another behaviour of infinite Markov chains]]
- [[#3.6 Absorption probabilities|3.6 Absorption probabilities]]
  - [[#Solution|Solution]]
- [[#3.7 Transient states|3.7 Transient states]]
  - [[#Lemma 3.7.1.|Lemma 3.7.1]]
  - [[#Lemma 3.7.2.|Lemma 3.7.2]]
  - [[#Lemma 3.7.3.|Lemma 3.7.3]]
  - [[#Example 11 - Random Walk with Variable Parameters|Example 11 - Random Walk with Variable Parameters]]
- [[#Summary Table|Summary Table]]

---

## 3.1 Regular Markov Chains

A Markov Chain is said to be regular if:

1. It has a finite number of states $0,1,\ldots,N$.
2. There is an integer $k\in\mathbb{Z}$ so that $(\mathbf{P}^{k})_{ij}>0\;\forall i,j$, i.e. all $k$-step transition probabilities are non-zero.

From these two conditions it follows that, given enough time, the system can (in principle) evolve from any state $i$ to any other state $j$. We will see (later on) that this guarantees the existence of a unique limiting probability distribution $\pi=(\pi_{0},\pi_{1},\ldots,\pi_{N})$, where $\pi_{j}>0\;\forall j=0,\ldots,N$ and $\sum_{j}\pi_{j}=1$, such that:

$$
\lim_{n\to\infty}P^{(n)}_{ij}=\pi_{j}>0\quad\forall j=0,1,\ldots,N
$$

This means that:

- There is a definite asymptotic behaviour - i.e. the limit $\lim_{n\to\infty}P^{(n)}_{ij}$ exists.
- This limit is independent of the initial state $i$, and so the system completely “forgets” where it came from.
- All states will keep being visited, because $\pi_{j}>0$, i.e. $\pi_{j}\neq 0$.

> [!Important] Theorem - Limiting Distribution of a Regular Markov Chain
> **Statement:** Let $\mathbf{P}$ be a regular transition probability matrix on the states $0,1,\ldots,N$. Then the limiting distribution $\boldsymbol{\pi}=(\pi_{0},\pi_{1},\ldots,\pi_{N})^{T}$ is the unique, nonnegative solution of the stationarity equations together with normalization.
>
> $$
> \pi_{j}=\sum_{k=0}^{N}\pi_{k}P_{kj}\qquad j=0,1,\ldots,n
> $$
>
> $$
> \sum_{k=0}^{N}\pi_{k}=1
> $$
>
> **Proof:** The full proof is transcribed immediately below, preserving the existence and uniqueness arguments.
>
> **Intuition:** Regularity eventually mixes every initial state into every other state, so the chain forgets where it started and converges to a single long-run distribution.

Let P be a regular transition probability matrix on the states $0,1,\ldots,N$. Then the limiting distribution $\boldsymbol{\pi}=(\pi_{0},\pi_{1},\ldots,\pi_{N})^{T}$ is the unique, nonnegative solution of the equations:

$$
\pi_{j}=\sum_{k=0}^{N}\pi_{k}P_{kj}\qquad j=0,1,\ldots,n
$$


with $\pi_{k}\geq 0$ and the normalization constraint:

$$
\sum_{k=0}^{N}\pi_{k}=1
$$

Proof. First note that the system in (3.1) is homogeneous, meaning that if $\pi_{0}$ is a solution then also $a\pi_{0}$, with $a\in\mathbb{R}\setminus\{0\}$ is a solution - and so it admits an infinite number of solutions. So, to have only a unique $\pi$ we need the constraint of (3.2), which also serves to guarantee that $\pi$ correctly represents a probability distribution.

1. Existence. As the Markov chain is regular, it admits a limiting distribution $\lim_{n\to\infty}P^{(n)}_{ij}=\pi_{j}$, for which $\sum_{k=0}^{N}\pi_{k}=1$. In fact:

$$
\sum_{j=0}^{N}P^{(n)}_{ij}=1\qquad\forall i\in\{0,\ldots,N\},n\geq 1
$$

Taking the limit of both sides:

$$
\lim_{n\to\infty}\sum_{j=0}^{N}P^{(n)}_{ij}=1=\sum_{j=0}^{N}\pi_{j}
$$

And so the $\pi_{j}$ are correctly normalized.

All that’s left is to show that they verify (3.1). To do so, we start from:

$$
\mathbf{P}^{(n)}=\mathbf{P}^{(n-1)}\times\mathbf{P}\Leftrightarrow P^{(n)}_{ij}=\sum_{k=0}^{N}P^{(n-1)}_{ik}P_{kj}\quad j=0,\ldots,N
$$

And take the limit $n\to\infty$:

$$
\lim_{n\to\infty}P^{(n)}_{ij} =\lim_{n\to\infty}\sum_{k=0}^{N}P^{n-1}_{ik}P_{kj}
\Rightarrow\pi_{j} =\sum_{k=0}^{N}\lim_{n\to\infty}P^{n-1}_{ik}P_{kj}=\sum_{k=0}^{N}\pi_{k}P_{kj}
$$

which is exactly (3.1). Exchanging the limit and the sum can be done because $N$ is finite, and so we do not have problems of convergence.
2. Uniqueness. Suppose that $\boldsymbol{x}$ is a solution of (3.1), i.e. that:

$$
x_{j}=\sum_{k=0}^{N}x_{k}P_{kj}\quad j=0,\ldots,N\qquad\sum_{k=0}^{N}x_{k}=1
$$

We want to show that $x_{j}=\pi_{j}$, and so there is only one limiting probability. In matrix notation:

$$
\boldsymbol{x}=\boldsymbol{x}\mathbf{P}
$$


Multiplying to the right by $\mathbf{P}$:

$$
\boldsymbol{x}\mathbf{P}=\boldsymbol{x}\mathbf{P}^{(2)}
$$

In terms of entries, this equates to:

$$
x_{l}\underset{(3.11)}{=}\sum_{j=0}^{N}x_{j}P_{jl}=\sum_{j=0}^{N}\sum_{k=0}^{N}x_{k}P_{kj}P_{jl}=\sum_{k=0}^{N}x_{k}P_{kl}^{(2)}
$$

where we *exchanged* the order of the two sums (as they are over a finite number of elements) to highlight the 2-step transition matrix.

Note that $\boldsymbol{x}=\boldsymbol{x}\mathbf{P}=\boldsymbol{x}\mathbf{P}^{(2)}$. Reiterating $n$ times:

$$
\boldsymbol{x}=\boldsymbol{x}\mathbf{P}^{(n)}\Leftrightarrow x_{l}=\sum_{k=0}^{N}x_{k}P_{kl}^{(n)}\quad l=0,\ldots,N
$$

As this holds for all values of $n$, it holds also in the limit $n\to\infty$:

$$
x_{l}=\lim_{n\to\infty}\sum_{k=0}^{N}x_{k}P_{kl}^{(n)}=\underbrace{\sum_{k=0}^{N}x_{k}}_{1}\pi_{l}=\pi_{l}\qquad l=0,\ldots,N
$$

which proves uniqueness.

### 3.1.1 Interpretation of the Limiting Distribution

Given a regular transition matrix $\mathbf{P}$ for a Markov process on $N+1$ states $0,\ldots,N$, we can find the limiting distribution by solving (3.1):

$$
\pi_{i}=\sum_{k=0}^{N}\pi_{k}P_{ki}\quad i=0,\ldots,N\qquad\sum_{i=0}^{N}\pi_{i}=1
$$

This means that the probability of finding the system in state $j$ *after a long time* does not depend on the initial state $i$, and it is given by $\pi_{j}$:

$$
\pi_{j}=\lim_{n\to\infty}P_{ij}^{(n)}=\lim_{n\to\infty}\mathbb{P}\{X_{n}=j|X_{0}=i\}
$$

Equivalently, each $\pi_{j}$ represents the *fraction of time* spent by the system in state $j$. In particular, this is useful to compute the long run average of *functional* of the states. For example, if each visit to state $j$ is associated with a *cost* $c_{j}$, then the long run mean cost $C$ (per unit time) associated with the Markov chain is:

$$
C=\sum_{j=0}^{N}\pi_{j}c_{j}
$$

This second interpretation comes from the fact that if a sequence $\{a_{n}\}_{n\in\mathbf{\mathbb{N}}}$ converges to a limit $a$, then also the *running averages* over the first $m$ elements


converge to $a$:

$$
\lim_{k\to\infty}a_{k}=a\Rightarrow\lim_{m\to\infty}\frac{1}{m}\sum_{k=0}^{m-1}a_{k}=a
$$

(but the converse is not true in general).

With respect to our problem, we note that the *fraction of time* spent by the system in state $j$ over a $m$-long run can be written as:

$$
\frac{1}{m}\sum_{k=0}^{m-1}\mathbf{1}\{X_{k}=j\}
$$

The *mean* fraction of visits of state $j$ (over a $m$-long run) is then:

$$
\mathbb{E}\left[\frac{1}{m}\sum_{k=0}^{m-1}\mathbf{1}\{X_{k}=j\}|X_{0}=i\right] =\frac{1}{m}\sum_{k=0}^{m-1}\mathbb{E}[\mathbf{1}\{X_{k}=j\}|X_{0}=i]=
=\frac{1}{m}\sum_{k=0}^{m-1}\mathbb{P}\{X_{k}=j|X_{0}=i\}=
=\frac{1}{m}\sum_{k=0}^{m-1}P_{ij}^{(k)}
$$

Taking the limit $n\to\infty$, we know that:

$$
\lim_{n\to\infty}P_{ij}^{(n)}=\pi_{j}\Rightarrow\lim_{n\to\infty}\frac{1}{m}\sum_{k=0}^{m-1}P_{ij}^{(k)}=\pi_{j}
$$

And so:

$$
\lim_{n\to\infty}\mathbb{E}\left[\frac{1}{m}\sum_{k=0}^{m-1}\mathbf{1}\{X_{k}=j\}|X_{0}=i\right]=\lim_{m\to\infty}\frac{1}{m}\sum_{k=0}^{m-1}P_{ij}^{(k)}=\pi_{j}
$$


## 3.2 Non regular Markov chains

Not all Markov chains are regular, that is there are Markov chains such that their $n$-step probability matrix $\mathbf{P}^{n}$ always contains some $0$ entries. In these cases, the previously derived results about the limiting distribution may not hold, and in particular:

- The limiting distribution $\lim_{n\to\infty}P_{ij}^{(n)}$ may not exist at all
- There could be several limiting distributions, each depending on the initial state
- The system may stop visiting certain states in the long-run, i.e. $\lim_{n\to\infty}P_{ij}=\pi_{j}$ holds, but not $\pi_{j}\neq 0$ $\forall j$.

We can show explicit examples for all these cases (fig. 3.1):

Examples of non-regular MC


![[Stochastic_Processes_2020_p70_img18.jpeg]]
*(a) - There are two limiting distributions, depending on the initial state*

![[Stochastic_Processes_2020_p70_img19.jpeg]]
*(b) - The chain is periodic: no limiting distribution exist.*

![[Stochastic_Processes_2020_p70_img20.jpeg]]
*(c) - A unique limiting distribution (independent of initial state) exists, but certain states (0 in this case) are never visited in the long run.*
*Figure 3.1 - Examples of non-regular Markov chains.*

1.  $\left[ \begin{array}{ll}1 & 0\\ 0 & 1 \end{array} \right] = \mathbb{1}\qquad \mathbf{P}^n = \mathbf{P}\quad \forall n$

In this case the Markov chain just remains fixed in the initial state. Clearly the limiting distribution exists, but it is not independent of the initial state (or else all the rows in the limit would have been equal). Moreover, depending on the case, some states are not visited anymore in the long run: if the chain starts at 0, it will never visit 1, meaning that  $\pi_1 = 0$ .

2.  $\left[ \begin{array}{ll}0 & 1\\ 1 & 0 \end{array} \right]\qquad \mathbf{P}^n = \left\{ \begin{array}{ll}\mathbf{P} & n\text{odd}\\ \mathbb{1} & n\text{even} \end{array} \right.$

In this case the limiting distribution does not even exist, since  $\mathbf{P}^n$  keeps oscillating.

3.  $\left[ \begin{array}{cc}\frac{1}{2} & \frac{1}{2}\\ 0 & 1 \end{array} \right]\qquad \mathbf{P}^n = \left[ \begin{array}{cc}(\frac{1}{2})^n & 1 - (\frac{1}{2})^n\\ 0 & 1 \end{array} \right]$

Here the limit exists, it is independent of initial state, but not all limiting probabilities are strictly positive:

$$
\lim  _ {n \to \infty} \mathbf {P} ^ {n} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 1 \end{array} \right]
$$

## 3.3 Classification of States

All non-regular Markov chains, by definition, arise from the presence of states that are isolated from each other, i.e. there is no possible chain of transitions - however long - linking them.

So, it is useful to formalize the concepts of accessibility and communication between states.

A state  $j$  is said to be accessible from state  $i$  if  $P_{ij}^{(n)} > 0$  for some integers  $n \geqslant 0$ , thus meaning that it is possible to reach state  $j$ , starting from  $i$ , in a certain number of steps.

If states  $i$  and  $j$  are accessible to each other, then they are said to communicate, and we denote this with  $i \leftrightarrow j$ . Two non-communicating states are such that either  $P_{ij}^{(n)} = 0$  or  $P_{ji}^{(n)} = 0$  (or both) for all  $n \geqslant 0$ .

Accessibility

Communication


Communication between states is an equivalence relation, i.e. it satisfies the following three key properties:

1. Reflexivity $(i \leftrightarrow i)$. Clearly $i$ can access itself, without even moving:

$$
P_{ij}^{(0)} = \delta_{ij} = \begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases}
$$

2. Symmetry $(i \leftrightarrow j$ then $j \leftrightarrow i)$, which follows directly from the definition of communication
3. Transitivity $(i \leftrightarrow j, j \leftrightarrow k$ then $i \leftrightarrow k)$

In order to prove 3, let $i \leftrightarrow j$ and $j \leftrightarrow k$. By hypothesis, this means that there exist integers $n$ and $m$ such that $P_{ij}^{(n)} > 0$ and $P_{jk}^{(m)} > 0$. Consequently, since each $P_{ji}^{(t)}$ is non-negative, we conclude:

$$
P_{ik}^{(n + m)} = \sum_{r = 0}^{\infty} P_{ir}^{(n)} P_{rk}^{(m)} \geqslant P_{ij}^{(n)} P_{jk}^{(m)} > 0
$$

where in (a) we used the fact that a sum of non-negative terms is always greater or equal each of its addends. This proves that the transition $i \to k$ is possible, i.e. it has a non-zero probability. By a similar argument one can prove that also the reverse transition $(k \to i)$ is possible, i.e. there exists an integer $\nu$ s.t. $P_{ki}^{(\nu)} > 0$, thus proving $i \leftrightarrow k$.

Because of these properties, we can now partition the totality of states into equivalence classes, each formed by inter-communicating states.

Note that different classes are not isolated: it may be possible to start in one class $A$ and move to some other class $B$ with non-zero probability. However, in this case the reverse transition $(B \to A)$ is impossible: otherwise the two classes would together form a single class. In other words, different classes can be connected only by one-way transitions.

If chain is made up of one single class, then it is said to be irreducible, otherwise it is said to be reducible. In other words, in an irreducible class, all states communicate with each other. For example, the following transition probability matrix describes a Markov chain with two different non-interacting classes:

Irreducibility

$$
\mathbf{P} = \begin{vmatrix}
\frac{1}{2} & \frac{1}{2} & 0 & 0 & 0 \\
\frac{1}{4} & \frac{3}{4} & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & \frac{1}{2} & 0 & \frac{1}{2} \\
0 & 0 & 0 & 1 & 0
\end{vmatrix} = \begin{vmatrix}
\mathbf{P_1} & 0 \\
0 & \mathbf{P_2}
\end{vmatrix}
$$


Another example is given by the following random-walk model:

$$
\mathbf {P} = \left[ \begin{array}{c c c c c c c c} 1 & 0 & 0 & 0 & \dots & 0 & 0 & 0 \\ q & 0 & p & 0 & \dots & 0 & 0 & 0 \\ 0 & q & 0 & p & \dots & 0 & 0 & 0 \\ \vdots & & & & & \vdots & \vdots & \vdots \\ 0 & \dots & \dots & \dots & \dots & q & 0 & p \\ 0 & \dots & \dots & \dots & \dots & 0 & 0 & 1 \end{array} \right] \begin{array}{l} 0 \\ 1 \\ 2 \\ \vdots \\ a - 1 \\ a \end{array} \tag {3.4}
$$

Here $p, q > 0$ are respectively the probabilities of forward/backward motion. Note that states 0 and $a$ are absorbing, and so we have three classes: $A = \{0\}$, $B = \{1,2,\ldots,a - 1\}$ and $C = \{a\}$. Starting anywhere in class $B$ can lead to $A$ or $C$, but the reverse transition cannot happen.

### 3.3.1 Periodicity

A Markov chain exhibits a periodic behaviour when it cyclically visits some states. More precisely, we focus on a single state $i$ and say that it is periodic with a certain period $d(i)$ if the system may visit it only every $n$ steps. In other words, if the system starts at $i$, then it may return to $i$ after $n$, $2n$, $3n$ or any multiple of $n$ steps - but never during an "in-between" step such as $n - 1$.

So, we formally define the period $d(i)$ of state $i$ as the greatest common divisor (g.c.d.) of all integers $n \geqslant 1$ for which $P_{ii}^{(n)} > 0$.

In the case that the system never returns to $i$, i.e. $P_{ii} = 0 \quad \forall n \geqslant 1$, we conventionally define $d(i) = 0$.

Note that if $P_{ii} > 0$, then $d(i) = 1$, since the system can remain in this state any length of time.

The most obvious example of periodicity is given by a chain cycling through $N$ states:

$$
\mathcal {M} _ {n \times n} \ni \mathbf {P} = \left( \begin{array}{c c c c c c} 0 & 1 & 0 & 0 & \dots & 0 \\ 0 & 0 & 1 & 0 & \dots & 0 \\ \vdots & & & & & \vdots \\ 0 & \dots & & \dots & \dots & 1 \\ 1 & 0 & 0 & \dots & \dots & 0 \end{array} \right)
$$

Here $d(i) = N$ for every $i = 0, \dots, N - 1$, as can be seen from the block diagram in fig. 3.2.

Periodicity


Another example is given by:

$$
\mathbf {P} = \begin{array}{c c c c c} & 0 & 1 & 2 & 3 \\ 0 & 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 1 & 0 \\ 2 & 0 & 0 & 0 & 1 \\ 3 & 1 & 0 & \frac {1}{2} & 0 \end{array} \tag {3.5}
$$

with the block diagram represented in fig. 3.3. Starting from 0, the system can return to 0 after 4, 6, 8, etc. steps (depending on how many iterations it spends between states 2 and 3), meaning that  $d(0) = 2$ .

Similarly, in the case of a random walk (3.4) every transient state 1, 2, ...,  $N - 1$  has period 2. In fact, starting from  $i$ , the system can return to it after an even number of steps: half spent "getting away" from  $i$ , and the other half "returning towards"  $i$ . In other words,  $P_{ii}^{n} = 0$  for every  $n$  odd.

> [!Important] Theorem 3.3.1 - Period Is a Class Property
> **Statement:** Period is a class property:
>
> $$
> i \leftrightarrow j \quad \Longrightarrow \quad d (i) = d (j)
> $$
>
> **Proof:** The full proof is transcribed immediately below.
>
> **Intuition:** If two states communicate, paths can be spliced through each other. This forces the possible return times of one state to share the same greatest common divisor as the other.

Theorem 3.3.1. Period is a class property:

$$
i \leftrightarrow j \quad \Longrightarrow \quad d (i) = d (j)
$$

In other words, all states that communicate with each other, i.e. are contained in the same class, share the same period.

Proof. The basic idea is shown in fig. 3.4. Essentially, we want to show that  $d(j) \leq s$ , where  $s$  is the length of any path  $i \to i$ . This implies that  $d(j) \leq d(i)$ . Then, exchanging the roles of  $i$  and  $j$ , we reach the equality  $d(i) = d(j)$ .

Let  $S_{i}$  be the set containing the lengths of all possible paths starting from  $i$  and returning to  $i$ :  $S_{i} = \{s > 0 : P_{ii}^{(s)} > 0\}$ . Then the period of  $i$  is  $d(i) = gcd(S_{i})$ .

By hypothesis,  $i \leftrightarrow j$ , and so there are two integers  $m, n$  such that  $P_{ij}^{(m)} > 0$ ,  $P_{ji}^{(n)} > 0$ .

So, it is possible to have a path from  $j \to i$  in  $n$  steps, then from  $i \to i$  in  $s \in S_i$  steps and finally going from  $i \to j$  in  $m$  steps:

$$
P _ {j j} ^ {(n + s + m)} = \sum_ {h, k} P _ {j h} ^ {(n)} P _ {h k} ^ {(s)} P _ {k j} ^ {(m)} \geqslant P _ {j i} ^ {(n)} P _ {i i} ^ {(s)} P _ {i j} ^ {(m)} > 0
$$

![[Stochastic_Processes_2020_p73_img21.jpeg]]
*Figure 3.2 - Block diagram for a  $N = 6$  cyclic Markov chain*


![[Stochastic_Processes_2020_p74_img22.jpeg]]
*Figure 3.3 - Block diagram for (3.5)*

Since all terms in the sum are non-negative, it is certainly greater or equal to a particular addend, which is chosen to be strictly greater than 0.

Similarly, the path that repeats the  $i \to i$  cycle two times is possible:

$$
P _ {i i} ^ {(2 s)} \geqslant \left(P _ {i i} ^ {(s)}\right) ^ {2} > 0 \quad \Rightarrow \quad P _ {j j} ^ {(n + 2 s + m)} > 0
$$

So we have found two possible path lengths that start from  $j$  and return to  $j$ , i.e.  $\forall s \in S_i$  both  $(n + s + m)$  and  $(n + 2s + m) \in S_j$ . By definition of  $d(j)$ , all elements of  $S_j$  are integer multiples of  $d(j)$ :

$$
n + s + m = k _ {1} d (j); \quad n + 2 s + m = k _ {2} d (j) \qquad k _ {1}, k _ {2} \in \mathbb {N}
$$

Subtracting member to member we get:

$$
s = (k _ {2} - k _ {1}) d (j)
$$

And so also  $s$  is a integer multiple of  $d(j)$ . This holds  $\forall s \in S_i$ , meaning that  $d(j)$  is a common divisor of all elements of  $S_i$ . As  $d(i)$  is the greatest common divisor of  $S_i$ , then  $d(i)$  must be a multiple of  $d(j)$ .

Finally, note that we can switch the roles of  $i$  and  $j$  and repeat all these arguments, concluding that also  $d(j)$  must be a multiple of  $d(i)$ . Clearly this can happen only if:

$$
d (i) = d (j)
$$

□

### 3.3.2 Recurrence

The smallest path-length  $s$  needed for starting in a state  $i$  and returning to  $i$  is the first return time  $\theta_{ii}$ . Its distribution is given by:

Recurrence

$$
f _ {i i} ^ {(n)} = \mathbb {P} \{\theta_ {i i} = n \} = \mathbb {P} \{X _ {n} = i, X _ {\nu} \neq i, \nu = 1, 2 \dots , n - 1 | X _ {0} = i \} \quad \forall n \geqslant 1
$$


![[Stochastic_Processes_2020_p75_img23.jpeg]]
*Figure 3.4 - Suppose that  $d(i) = 3$ . Then all paths that start from  $i$  and return to  $i$  must have a length that is a multiple of 3 - in particular  $n + m$  must be divisible by 3. Now focus on  $j$ , and note that  $d(j)$  cannot be  $< 3$ . In fact, if  $d(j)$  were, for example, 2, then it would exist a 2-step path  $j \rightarrow j$ . But then we could construct a path  $i \rightarrow i$  of  $n + m + 2$  steps ( $i \rightarrow j$  in  $n$  steps,  $j \rightarrow j$  in 2 steps and  $j \rightarrow i$  in  $m$  steps), which is not a multiple of 3. Similarly,  $d(j)$  cannot be  $> 3$ : because we can construct two paths  $j \rightarrow j$  with length  $n + m$  and  $n + m + 3$ , and their g.c.d. is  $\leq 3$ . So  $d(j) = d(i) = 3$*

So  $f_{ii}^{(n)}$  is the probability that, starting from the  $i$ -th state, the first return to  $i$  occurs exactly at the  $n$ -th transition.

Clearly this is just a special case of first passage time, and in particular we can compute  $f_{ii}^{(n)}$  recursively according to 2.26, keeping in mind that  $i = j$ .

Consider a process starting from state  $i$ . The probability  $f_{ii}$  that it will return to state  $i$  (after any amount of time) is given by the sum of the single probabilities of first arrival times for different  $n$  steps, since they are disjoint events (we can arrive for the first time only once):

$$
f _ {i i} = \sum_ {n = 0} ^ {\infty} f _ {i i} ^ {(n)} = \lim _ {N \to \infty} \sum_ {n = 0} ^ {N} f _ {i i} ^ {(n)}
$$

When  $f_{ii} = 1$ , a state is said to be recurrent, because we are guaranteed that sooner or later we will come back to it. If a state is not recurrent, then it is said to be transient.

Considering a transient state  $i$ , then  $f_{ii} < 1$  for definition. Supposing we come back once, because of Markov property we forget about past events, and so the probability of coming back again is  $f_{ii} < 1$  one more time. This means that the probability of returning at least twice is  $(f_{ii})^2 < 1$ . By iterating this argument, we obtain that the probability to come back to  $i$ -th state at least  $k$  times is:  $(f_{ii})^k$ ,  $k = 1, 2 \ldots$ .

Let  $M$  be the random variable that counts how many times the chain returns to state  $i$ . Its distribution is geometric:

$$
\mathbb {P} \{M \geqslant k | X _ {0} = i \} = (f _ {i i}) ^ {k} \quad \text {for} \mathrm {k} = 1, 2 \dots
$$

The expectation of  $M$  is then:

$$
\mathbb {E} [ M | X _ {0} = i ] = \sum_ {k = 1} ^ {\infty} \mathbb {P} \{M \geq k | X _ {0} = i \} = \sum_ {k = 1} ^ {\infty} (f _ {i i}) ^ {k} = \frac {f _ {i i}}{1 - f _ {i i}}
$$

Transient states


![[Stochastic_Processes_2020_p76_img24.jpeg]]
*Figure 3.5 - Cumulative probabilities for proper and non proper random variables. Notice as, for the non proper random variable, while  $X \to \infty$ ,  $P(X)$  asymptotically tends to a value different than 1.*

For a recurrent state  $i$ , however, we are certain that the chain will return to it. By the Markovian property, at each return the chain "forgets" about its past - and so the probability of returning will be always 1, meaning that given infinite time the system will visit  $i$  an infinite number of times. This kind of behaviour cannot be captured by random variables in their current definition. In fact, one of the basic properties of proper or finite-values random variables, is that:

$$
\lim  _ {x \rightarrow \infty} \mathbb {P} [ X \leqslant x ] = \lim  _ {x \rightarrow \infty} F (x) = 1
$$

However, in the case of  $M$  for a recurrent state  $i$ , we have  $\mathbb{P}[M \leq x] = 0$  for all finite  $x$ , because the chain will surely return to  $i$  an infinite amount of times! So:

$$
\lim  _ {x \rightarrow \infty} \mathbb {P} [ M \leq x ] = 0 \neq 1
$$

and thus  $M$  is not a proper random variable. So, to study these kind of variables, we need a generalized definition, leading to the so-called improper random variables.

### Improper random variables

We now introduce the improper random variables, for which we admit:

$$
\lim  _ {x \rightarrow \infty} \mathbb {P} [ X > x ] = P _ {\infty} > 0
$$

We interpret  $P_{\infty}$  as the probability that  $X$  will take an infinite value, thus denoting it (formally) with:

$$
\mathbb {P} [ X = \infty ] = P _ {\infty}
$$

In other words, proper random variables cannot ever assume infinite values, as their probability of assuming greater and greater values must vanish. On the other hand, improper random variables may have a finite probability of assuming an infinite value.

Recurrent states



Let $n$ be the number of visits to a recurrent state $i$. Then $\mathbb{P}[n\geqslant k]=1\ \forall k$ because of the definition of recurrent state, and also the probability of visiting $i$ any number of times is also $1$. Taking the limit of the tail probability as $k\to\infty$:

$$
P_{\infty}=\lim_{k\to\infty}\mathbb{P}[n>k]=\mathbb{P}[n=\infty]=1.
$$

This means that, in the limit, $n$ can’t take any possible finite value.

For non-negative improper r.v.s, we have in the continuous case:

$$
\mathbb{E}[X]=\int_{0}^{+\infty}x\,\mathrm{d}F(x)=\int_{0}^{+\infty}\mathbb{P}[X>x]\,\mathrm{d}x=\infty
$$

So the expectation of an improper r.v. diverges, since $\lim_{x\to\infty}\mathbb{P}[X>x]>0$.

The same holds for discrete non-negative improper r.v.s

$$
\mathbb{E}[X]=\int_{0}^{+\infty}x\,\mathrm{d}F(x)=\sum_{k=0}^{+\infty}\mathbb{P}[X>k]=\infty
$$


$$
\text{state }i\text{ is recurrent}\ \ \Longleftrightarrow\ \sum_{n=1}^{\infty}P_{ii}^{(n)}=\infty
$$

Equivalently, state $i$ is transient if and only if $\sum_{n=1}^{\infty}P_{ii}^{(n)}<\infty$.

Note that this is just a restatement of the second Borel-Cantelli lemma, since all paths $i\to i$ of different length $n$ form independent events.


Let $M$ be the number of visits to $i$-th state:

$$
M=\sum_{n=1}^{+\infty}\mathbf{1}\{X_{n}=i\}
$$

Its expectation is given by:

$$
\mathbb{E}[M|X_{0}=i] =\mathbb{E}\left[\sum_{n=1}^{+\infty}\mathbf{1}\{X_{n}=i\}|X_{0}=i\right]=
\underset{(a)}{=}\sum_{n=1}^{+\infty}\mathbb{E}\left[\mathbf{1}\{X_{n}=i\}|X_{0}=i\right]=\sum_{n=1}^{+\infty}P_{ii}^{(n)}
$$

In other words, the sum of the *return* probabilities $P_{ii}^{(n)}$ is exactly the average number of returns to state $i$.

However, step (a) needs justification. In fact, we know we are allowed to bring the expectation inside the sum (because of linearity), but this is always true only when we are summing a finite number of terms - which is not the case


here. When dealing with infinite sums, we are implicitly considering limits - one for the expectation, and one for the sum. In general, their order may actually matter, and so we cannot exchange them without providing some kind of justification. For now, we will assume that (a) is legitimate, delaying its proof to argument 3.3.3.

All that’s left is to examine two cases:

1. If $i$ is a transient state, then $f_{ii}<1$, so:

$$
\sum_{n=1}^{+\infty}P_{ii}^{(n)}=\mathbb{E}[M|X_{0}=i]=\sum_{k=1}^{+\infty}P[M\geqslant k|X_{0}=i]=\sum_{k=1}^{+\infty}(f_{ii})^{k}=\frac{f_{ii}}{1-f_{ii}}<\infty
$$
2. If $i$ is a recurrent state, then $f_{ii}=1$, leading to:

$$
\sum_{n=1}^{+\infty}P_{ii}^{(n)}=\mathbb{E}[M|X_{0}=i]=\sum_{k=1}^{+\infty}P[M\geqslant k|X_{0}=i]=\sum_{k=1}^{+\infty}(f_{ii})^{k}=\infty
$$

Summarizing, for a transient state the expectation of $M$ is finite, while for a recurring state it is infinite - which concludes the proof. ∎

### 3.3.3 Fubini's Theorem

In many cases we use the linearity property of the operators $\sum$, $\int$, $\mathbb{E}$ to swap their position. This happens for example when, for $x$ and $y$ belonging to some sets $D_{x}$ and $D_{y}$ we write:

$$
\sum_{x\in D_{x}}\sum_{y\in D_{y}}f(x,y)=\sum_{y\in D_{y}}\sum_{x\in D_{x}}f(x,y)
$$

or when we exchange a sum with an expected value: $\mathbb{E}\sum=\sum\mathbb{E}$.
The mathematical tool allowing us to do so is the Fubini’s Theorem, that states that if any one of the sums $\sum_{x}\sum_{y}f(x,y)$ or $\sum_{y}\sum_{x}f(x,y)$ converges absolutely, meaning that the sum with $|f(x,y)|$ is finite, then the exchange is valid.
In order to have a better understanding of this result, consider the following. We can rewrite any function $f(x,y)$ as the difference of its positive and negative parts $f_{\pm}(x,y)$:

$$
f(x,y)=f_{+}(x,y)-f_{-}(x,y)
$$

where:

$$
f_{+}(x,y)=\max(f(x,y),0)\qquad f_{-}(x,y)=-\min(f(x,y),0)
$$

Basically, $f_{\pm}(x,y)$ are the modulus of the positive and negative values that $f$ can take.


Then the double sum $\sum_{x}\sum_{y}f(x,y)$ can be rewritten as:

$$
\sum_{x}\sum_{y}f(x,y)=\sum_{x}\sum_{y}f_{+}(x,y)-\sum_{x}\sum_{y}f_{-}(x,y)
$$

Similarly, the double sum of $|f(x,y)|$ is given by:

$$
\sum_{x}\sum_{y}|f(x,y)|=\sum_{x}\sum_{y}f_{+}(x,y)+\sum_{x}\sum_{y}f_{-}(x,y)
$$

As stated by Fubini’s theorem, if $\sum_{x}\sum_{y}|f(x,y)|<\infty$, then both $\sum_{x}\sum_{y}f_{+}<\infty$ and $\sum_{x}\sum_{y}f_{-}<\infty$ as well, and their difference $f_{+}-f_{-}$ is well defined, too. On the other hand it may happen that $\sum_{x}\sum_{y}|f|$ is infinite while $\sum_{x}\sum_{y}f$ is finite, because $f(x,y)\leqslant|f(x,y)|$. In this case $\sum_{x}\sum_{y}|f|$ may be made up by two possible diverging components. Then, it may occur that $\sum_{x}\sum_{y}f=\sum_{x}\sum_{y}f_{+}-\sum_{x}\sum_{y}f_{-}=\infty-\infty=\text{\sf?}$ which is an indeterminate form.

Example Let $X_{i}$ be a non-negative random variable. We want now to establish whether it is legitimate for us to exchange $\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]=\sum_{i=0}^{+\infty}\mathbb{E}\left[X_{i}\right]$.

- If $\sum_{i=0}^{+\infty}\mathbb{E}[X_{i}]<\infty$ and recalling that in the non-negative case absolute convergence and simple convergence refer to the same concept, from Fubini’s theorem we know that $\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]<\infty$ too. This means that both $\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]$ and $\sum_{i=0}^{+\infty}\mathbb{E}\left[X_{i}\right]$ exist, and share the same value. In conclusion the exchange is valid.
- If $\sum_{i=0}^{+\infty}\mathbb{E}[X_{i}]=\infty$, then the other expression is infinite as well:

$$
\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]\geqslant\mathbb{E}\left[\sum_{i=0}^{M}X_{i}\right]=\sum_{i=0}^{M}\mathbb{E}[X_{i}]\quad\forall M
$$

We could lowerbound the sum since $X_{i}$ is a non-negative random variable and the sum is monotonically increasing in $i$, note that this argument is valid for any value $M$ that we may choose. But since even the lowerbounded sum diverges itself:

$$
\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]\geqslant\lim_{M\to\infty}\sum_{i=0}^{M}\mathbb{E}\left[X_{i}\right]=\infty
$$

And therefore $\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]=\infty$ as well, thus making the exchange not possible.

In conclusion, in a certain sense, for non-negative random variables $X_{i}$, it always holds that they share the same value:

$$
\sum_{i=0}^{+\infty}\mathbb{E}[X_{i}]=\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]
$$

No matter either that value is finite, or infinite.


Note that when we made the truncation of the sum we applied *Lebesgue’s convergence theorem*: for $X_{i}\geqslant 0$, $\sum_{i=0}^{M}X_{i}$ is monotonic in M. Therefore the exchange of the limits, i.e. $\lim_{M\to\infty}\sum_{i=0}^{M}$ and $\mathbb{E}$, is guaranteed in Lebesgues’s monotonic convergence theorem.

Recalling what we did while proving 3.3.2, the exchange was indeed valid since we were dealing with a non-negative random variable i.e. the indicator function, which can take values either 0 or 1. Because of the arguments we have just seen, the exchange was therefore valid.

We will now introduce a corollary of the just mentioned theorem 3.3.2, which states that also *recurrence* is a *class property*:

### Corollary - Recurrence Is a Class Property

If $i\leftrightarrow j$ and if i is recurrent, then j is recurrent.


Since $i$ and $j$ are communicating, for sure there exists two integers $m,n\geqslant 1$ s.t.

$$
P_{ij}^{(n)}>0\qquad\text{and}\qquad P_{ji}^{(m)}>0
$$

Now let $\nu\geqslant 0$ and consider, as we did for proving 3.3.1, the probability of returning in j in $(m+n+\nu)$ number of steps: $P_{jj}^{(m+n+\nu)}=\sum_{h,k}^{\infty}P_{jh}^{(m)}P_{hk}^{(\nu)}P_{kj}^{(n)}\geqslant P_{ji}^{(m)}P_{ii}^{(\nu)}P_{ij}^{(n)}$ and, on summing:

$$
\sum_{\nu=0}^{\infty}P_{jj}^{(m+n+\nu)}\geqslant\sum_{\nu=0}^{\infty}P_{ji}^{(m)}P_{ii}^{(\nu)}P_{ij}^{(n)}=P_{ji}^{(m)}P_{ij}^{(n)}\sum_{\nu=0}^{\infty}P_{ii}^{(\nu)}
$$

But we are assuming that $i$ is recurrent, then the sum $\sum_{\nu=0}^{\infty}P_{ii}^{(\nu)}$ diverges. In addition, since $P_{ij}^{(n)},P_{ji}^{(m)}>0$ the whole product in the r.h.s. diverges as well, making $\sum_{\nu=0}^{\infty}P_{jj}^{(m+n+\nu)}$ diverge itself, too, because it is bigger. We also notice that the first term $\sum_{\nu=0}^{\infty}P_{jj}^{(m+n+\nu)}$ starts at step $(m+n)$ and moreover we know it is infinite. Therefore the $\sum_{\nu=0}^{\infty}P_{jj}^{(\nu)}$ diverges being it even bigger, because this time we considered $\nu=0$ as the starting point. ∎

We have just proved that recurrence, as well as periodicity, is a class property: it means that all states in a class are either recurrent or nonrecurrent.

## 3.4 Basic Limit Theorem of Markov Chains

We are finally able to formalize and *prove* the intuitive fact that the *long-run* probability of returning to a state $i$ is the *reciprocal* of the average return time $m_{i}$: that is, if the system is at $i$ every $m_{i}$ steps, then it spends $1/m_{i}$ of the total time in $i$, and so if we inspect the state at a random step (of a *infinitely long* experiment) we will find the system at $i$ with probability $1/m_{i}$. Moreover,


we will also find the appropriate conditions that are necessary for this result to hold.

Consider a recurrent state $i$. As we have seen before, the first return time $R_{i}$ can be defined as:

$$
R_{i}=\min\{n\geq i;X_{n}=i\}
$$

and is distributed according to:

$$
f_{ii}^{(n)}=\mathbb{P}\{R_{i}=n|X_{0}=i\}=\mathbb{P}\{X_{n}=i,X_{\nu}\neq i\,\forall\nu=1,\ldots,n-1|X_{0}=i\}
$$

Since the state $i$ is recurrent, $f_{ii}=\sum_{n=1}^{\infty}f_{ii}^{(n)}=1$, and so $R_{i}$ is a finite-valued random variable. In other words, $R_{i}$ can never be infinite, since the system will return to $i$ *for sure*. More precisely, the probability of $R_{i}$ being arbitrarily high *vanishes*.

The mean duration between visits to state $i$ is the expectation of $R_{i}$:

$$
m_{i}=\mathbb{E}[R_{i}|X_{0}=i]=\sum_{n=1}^{\infty}nf_{ii}^{(n)}
$$

In other words, the system *on average* returns to $i$ once every $m_{i}$ units of time.

Note that the fact that $R_{i}$ is a finite-valued random variable does not prevent $m_{i}$ from being infinite. This in fact happens if $\mathbb{P}[R_{i}=n]$ decreases *sufficiently slowly* as $n\to\infty$.


> [!Important] Theorem 3.4.1 - Basic Limit Theorem of Markov Chains
> **Statement:** For a recurrent, irreducible, aperiodic Markov chain, the long-run probability of being in state $i$ is the reciprocal of the mean return time $m_i$.
>
> $$
> \lim_{n\to\infty}P_{ii}^{(n)}=\frac{1}{\sum_{n=1}^{\infty}nf_{ii}^{(n)}}=\frac{1}{m_{i}}
> $$
>
> $$
> \lim_{n\to\infty}P_{ji}^{(n)}=\pi_{i}=\frac{1}{m_i}
> $$
>
> **Proof:** The source refers the proof to a later chapter; the statement and consequences are preserved below.
>
> **Intuition:** If returns to $i$ occur every $m_i$ steps on average, then the long-run fraction of time spent in $i$ is $1/m_i$.

Consider a recurrent, irreducible, aperiodic Markov chain. Let $P_{ii}^{(n)}$ be the probability of entering state $i$ at the $n$-th transition, with $n\in\mathbb{N}$, given that the initial state is $i$ ($X_{0}=i$). Let $f_{ii}^{(n)}$ be the probability of first returning to state $i$ at the $n$-th transition. Then:

$$
\lim_{n\to\infty}P_{ii}^{(n)}=\frac{1}{\sum_{n=1}^{\infty}nf_{ii}^{(n)}}=\frac{1}{m_{i}}
$$
**Also:**

$$
\lim_{n\to\infty}P_{ji}^{(n)}=\pi_{i}=\lim_{n\to\infty}P_{ii}^{(n)}=\frac{1}{m_{i}}
$$

for all states $j$.

The proof is referred to a later chapter.

Note that theorem 3.4.1 can be applied also to aperiodic recurrent classes in a Markov Chain. In fact, we noted that different classes can only be linked by *one-way* transitions - meaning that after leaving a class $C$, the system cannot return in it. So a *recurrent class* must necessarily be isolate, i.e. such that


$P_{ij}^{(n)} = 0$  for all  $i \in C$ ,  $j \notin C$ , and for all  $n$ . So we can consider the submatrix  $\| \mathbf{P}_{ij}\|$ , with  $i, j \in C$ , as the transition probability matrix of a separate irreducible Markov Chain, for which the basic limit theorem directly applies.

Depending on the finiteness of  $m_{i}$ , we distinguish two cases:

- If the average return time  $m_i$  is finite, then  $\lim_{n \to \infty} P_{ii}^{(n)} > 0$ , and the same applies to all states  $j \leftrightarrow i$ . This means that  $\pi_j > 0$  for every  $j$ , and so all states in the aperiodic recurrent class continue to be visited in the long run. Classes with this property are said to be positive recurrent, or strongly ergodic.
- If  $m_i = \infty$ , then  $\pi_j = 0$  for every  $j$ , then the class is said to be null recurrent, or weakly ergodic. In a sense, this is the critical line separating transient states from recurrent ones, where the system will return to  $i$  surely, but it needs infinite time to do so.

Since these are all class properties, there cannot be positive recurrent and null recurrent states in the same class. So, a state can be either transient, positive recurrent or null recurrent, with all the properties summarized in table 3.1.

|  Type of State | fii=∑n=1∞f(ni)ii | limk→∞P[M>k|X0=i] | E[M|X0=i] | mi=∑n=1∞nf(ni)ii | πi=1/mi  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  Transient | <1 | 0 | fii/1-fii<∞ | ∞ | 0  |
|  Null Recurrent | 1 | 1 | ∞ | ∞ | 0  |
|  Positive Recurrent | 1 | 1 | ∞ | <∞ | >0  |

*Table 3.1 - Summary of the main properties for the different categories of states.  $f_{ii}$  is the probability of returning to  $i$ ,  $M$  is the number of returns to  $i$ ,  $m_i$  the average time between returns and  $\pi_i$  the probability of the system being in  $i$  in the long run.*

A positive recurrent aperiodic class behaves, when taken by itself, the same as a regular Markov chain, and so the same result about the limiting distribution still holds:


> [!Important] Theorem 3.4.2 - Stationary Distribution for a Positive Recurrent Aperiodic Class
> **Statement:** In a positive recurrent aperiodic class, the limiting probabilities are the unique nonnegative solution of the stationarity equations.
>
> $$
> \pi_ {i} \geq 0, \sum_ {i = 0} ^ {\infty} \pi_ {i} = 1 \quad \pi_ {j} = \sum_ {i = 0} ^ {\infty} \pi_ {i} P _ {i j} \quad j \in \mathbb {N} \tag {3.7}
> $$
>
> **Proof:** The full existence and uniqueness proof is transcribed immediately below.
>
> **Intuition:** Positive recurrence gives positive long-run mass, while aperiodicity removes oscillations, so the stationary solution is also the limiting distribution.

In a positive recurrent aperiodic class with states  $j \in \mathbb{N}$ , we have:

$$
\lim  _ {n \rightarrow \infty} P _ {j j} ^ {(n)} = \pi_ {j} = \sum_ {i = 0} ^ {\infty} \pi_ {i} P _ {i j} \quad \sum_ {i = 0} ^ {\infty} \pi_ {i} = 1
$$

and  $\pi$  is uniquely determined by the set of equations:

$$
\pi_ {i} \geq 0, \sum_ {i = 0} ^ {\infty} \pi_ {i} = 1 \quad \pi_ {j} = \sum_ {i = 0} ^ {\infty} \pi_ {i} P _ {i j} \quad j \in \mathbb {N} \tag {3.7}
$$

In general, any set  $(\pi_i)_{i=0}^{\infty}$  satisfying (3.7) is called a stationary probability distribution.


Note, however, that theorem 3.4.2 is actually more general than the result we got for regular Markov chain, as here we are not assuming a *finite* number of states. In fact, we cannot employ the same proof - because there we needed to exchange the order of two sums, which needs justification in the infinite case. Of course, we could use Fubini’s theorem to generalize the previous arguments, but in this case is actually more instructive to restart from first principles.


As before, we need to prove two things: that the limiting probabilities $\pi_{j}$ are indeed the solution of (3.7), and that this solution is unique.

Existence:

1. We start from the normalization condition for rows in the $n$-step transition matrix:

$$
1=\sum_{j=0}^{+\infty}P_{ij}^{(n)}\qquad\forall n
$$

Since all the addends are non-negative, the total sum cannot be lower than any *truncated* sum:

$$
1=\sum_{j=0}^{+\infty}P_{ij}^{(n)}\geq\sum_{j=0}^{M}P_{ij}^{(n)}\qquad\forall n,M
$$

We then take the limit $n\to\infty$, and bring it inside the sum, since it is over a *finite* number of elements:

$$
1\geq\lim_{n\to\infty}\sum_{j=0}^{M}P_{ij}^{(n)}=\sum_{j=0}^{M}\lim_{n\to\infty}P_{ij}^{(n)}=\sum_{j=0}^{M}\pi_{j}\qquad\forall M
$$

Finally we take also the $M\to\infty$ limit, leading to:

$$
\lim_{M\to\infty}\sum_{j=0}^{M}\pi_{j}=\sum_{j=0}^{+\infty}\pi_{j}\leq 1
$$

So we have found that the sum of $\pi_{j}$ converges. Clearly, we would like to prove that it is *exactly* $1$.
2. Again we start from a known relationship:

$$
P_{ij}^{(m+n)}=\sum_{k=0}^{+\infty}P_{ik}^{(m)}P_{kj}^{(n)}\qquad\forall m,n
$$

Again we can truncate the sum to write an inequality:

$$
P_{ij}^{(m+n)}\geq\sum_{k=0}^{M}P_{ik}^{(m)}P_{kj}^{(n)}\qquad\forall m,n,M
$$


Taking the limit $m\to\infty$ and taking it into the finite sum:

$$
\pi_{j}=\lim_{m\to\infty}P_{ij}^{(m+n)}\geq\lim_{m\to\infty}\sum_{k=0}^{M}P_{ik}^{(m)}P_{kj}^{(n)} =\sum_{k=0}^{M}\lim_{m\to\infty}P_{ik}^{(m)}P_{kj}^{(n)}=
=\sum_{k=0}^{M}\pi_{k}P_{kj}^{(n)}\quad\forall M,n
$$

Finally, we take also $M\to\infty$, leading to:

$$
\pi_{j}\geq\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}\qquad\forall n
$$
3. We want to show that (3.9) hold as an equality, and we do this by contradiction. Suppose that there exist an index $j$ for which (3.9) holds *strictly*:

$$
\exists j\colon\pi_{j}>\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}
$$

Summing over $j$, the inequality remains strict:

$$
\sum_{j=0}^{+\infty}\pi_{j}>\sum_{j=0}^{+\infty}\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}
$$

Let’s evaluate this last sum. Again, we first *truncate* the inner sum to the first $M$ elements, so that we can exchange the two sums and obtain an inequality that remains valid also in the limit $M\to\infty$:

$$
\sum_{j=0}^{+\infty}\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}\geq\sum_{j=0k=0}^{+\infty}\sum_{k=0}^{M}\pi_{k}P_{kj}^{(n)}=\sum_{k=0}^{M}\pi_{k}\sum_{j=0}^{+\infty}P_{kj}^{(n)}=\sum_{k=0}^{M}\pi_{k}\quad\forall M
$$

And in particular:

$$
\sum_{j=0}^{+\infty}\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}\geq\lim_{M\to\infty}\sum_{k=0}^{M}\pi_{k}=\sum_{k=0}^{+\infty}\pi_{k}
$$

Substituting in (3.10) we get:

$$
\sum_{j=0}^{+\infty}\pi_{j}>\sum_{j=0}^{+\infty}\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}\geq\sum_{k=0}^{+\infty}\pi_{k}
$$

which is absurd, as no quantity can be strictly greater than itself. So, by contradiction it must be:

$$
\pi_{j}=\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}\quad\forall n
$$


Setting $n=1$ we obtain part of the thesis we wish to prove.
4. All that’s left is to deal with the normalization property, i.e. show that (3.8) holds as an equality.

First, note that $|P_{kj}^{(n)}|\leq 1$ $\forall n$ (they are uniformly bounded). This, along with the convergence of $\sum_{k=0}^{+\infty}\pi_{k}\leq 1$ (3.8) allows to bring the limit inside the sum in the following:

$$
\pi_{j}=\lim_{n\to\infty}\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}=\sum_{k=0}^{+\infty}\pi_{k}\lim_{n\to\infty}P_{kj}^{(n)}=\left(\sum_{k=0}^{+\infty}\pi_{k}\right)\pi_{j}
$$

Since $\pi_{j}>0$ (because the chain is positive recurrent by hypothesis), we can divide both sides by $\pi_{j}$, leading to:

$$
\sum_{k=0}^{+\infty}\pi_{k}=1
$$

This finally proves the existence of the solution of (3.7).

Uniqueness.
Let $\boldsymbol{x}$ be a solution, i.e. such that:

$$
x_{j}=\sum_{i=0}^{+\infty}x_{i}P_{ij};\qquad\sum_{i=0}^{+\infty}x_{i}=1
$$

We then proceed as we did for regular MC$s$, rewriting the $x_{i}$ in the rhs of (3.11) by using (3.11) itself. Then we apply again the trick of truncating the inner sum to exchange the sums:

$$
x_{j} =\sum_{i=0}^{+\infty}\left(\sum_{k=0}^{+\infty}\pi_{k}P_{ki}\right)P_{ij}\geq\sum_{i=0}^{+\infty}\left(\sum_{k=0}^{M}x_{k}P_{ki}\right)P_{ij}=
=\sum_{k=0}^{M}x_{k}\sum_{i=0}^{+\infty}P_{ki}P_{ij}=\sum_{k=0}^{M}x_{k}P_{kj}^{(2)}\quad\forall M
$$

And this holds also in the limit $M\to\infty$. Therefore:

$$
x_{j}\geq\sum_{k=0}^{+\infty}x_{k}P_{kj}^{(2)}
$$

And by iterating this argument:

$$
x_{j}\geq\sum_{k=0}^{+\infty}x_{k}P_{kj}^{(n)}\qquad\forall n
$$

To prove that this is indeed an equality, we proceed as in point 3 of the previous proof, and assume that there is an index $j$ for which (3.12) is strict. By a similar


reasoning, this leads to a contradiction:

$$
\sum_{j=0}^{+\infty}x_{j}>\sum_{k=0}^{+\infty}x_{k}
$$

Therefore (3.12) must hold as an equality:

$$
x_{j}=\sum_{k=0}^{+\infty}x_{k}P_{kj}^{(n)}\qquad\forall n
$$

Finally, letting $n\to\infty$ and using the same argument as in point 4 to bring the limit inside the sum:

$$
x_{j}=\lim_{n\to\infty}\sum_{k=0}^{+\infty}x_{k}P_{kj}^{(n)}=\sum_{k=0}^{+\infty}x_{k}\lim_{n\to\infty}P_{kj}^{(n)}=\left(\sum_{k=0}^{+\infty}x_{k}\right)\pi_{j}
$$

and since $\sum_{k=0}^{+\infty}x_{k}=1$ we have $x_{j}=\pi_{j}$, thus concluding the proof. ∎

Solving (3.7) suffices to say that an aperiodic Markov chain is positive recurrent. Conversely, proving that (3.7) does not admit solutions, means that the aperiodic Markov chain is not positive recurrent.

For a general Markov chain, however, a stationary distribution is not necessarily the same as the limiting distribution. In fact, if a limiting distribution exists, then it is stationary (i.e. it is the solution of (3.7)), but the converse is not true: sometimes (3.7) can be solved, but the Markov chain is periodic and so that solution is clearly not the limiting distribution (that does not exist).

The simplest example of this kind of behaviour is given by:

$$
\mathbf{P}=\begin{bmatrix}0&1\\
1&0\end{bmatrix}
$$

This is a non-regular Markov chain that always cycles between states $0$ and $1$, thus presenting no limiting distribution. However it admits a stationary distribution, which is $\boldsymbol{\pi}=(1/2,1/2)^{T}$. In fact:

$$
\left(\begin{array}[]{cc}\frac{1}{2}&\frac{1}{2}\end{array}\right)\times\begin{bmatrix}0&1\\
1&0\end{bmatrix}=\left(\begin{array}[]{cc}\frac{1}{2}&\frac{1}{2}\end{array}\right)
$$


Consider the following random walk:

$$
\mathbf{P}=\begin{bmatrix}0&1&0&\cdots&\cdots\\
q_{1}&0&p_{1}&\cdots&\cdots\\
0&q_{2}&0&p_{2}&\cdots\\
\vdots&\ddots&\ddots&\ddots&\ddots\end{bmatrix}
$$


$q_{i},p_{i}>0$, then the chain is irreducible, with $d(i)=2$ (to return to the same state $i$, we need an equal number of steps in one direction, and in the opposite one, thus all $P^{(n)}_{ii}$ with $n$ odd are $0$). So it is not aperiodic, meaning that theorem 3.4.2 cannot be applied. However, there is a stationary distribution, i.e. we can solve:

$$
\mbox{\boldmath }=\mbox{\boldmath }\mbox{\boldmath }\Leftrightarrow x_{i}=\sum_{j=0}^{+\infty}x_{j}P_{ji}=p_{i-1}x_{i-1}+q_{i+1}x_{i+1}\qquad i>0 (3.13)
$$

under the normalization:

$$
\sum_{i=0}^{+\infty}x_{i}=1
$$

and with $p_{0}=1$, and $x_{0}=q_{1}x_{1}$.

Recall that we previously solved a similar equation while doing first-step analysis:

$$
\mbox{\boldmath }=\mbox{\boldmath }\mbox{\boldmath } (3.14)
$$

However we cannot directly apply the same method, as in (3.14) $\mathbf{P}$ multiplies the vector from the left and not from the right as in (3.13).

However, the idea is similar. We start by solving the first equation:

$$
x_{0}=q_{1}x_{1}\Rightarrow x_{1}=\frac{x_{0}}{q_{1}}
$$

And substitute in the second one:

$$
x_{1}=x_{0}+q_{2}x_{2}\Rightarrow x_{2}=\frac{x_{1}-x_{0}}{q_{2}}=\frac{\left(1-q_{1}\right)\ x_{1}}{q_{2}}=\frac{p_{1}x_{0}}{q_{1}q_{2}}
$$

where we used the row-normalization of $\mathbf{P}$, for which $p_{i}+q_{i}=1$.
Repeating one more time:

$$
x_{2}=p_{1}x_{1}+q_{3}x_{3}\Rightarrow x_{3}=\frac{x_{2}-p_{1}x_{1}}{q_{3}}\underset{(3.15)}{=}\frac{p_{1}x_{1}(1-q_{2})}{q_{2}q_{3}}=\frac{p_{1}p_{2}x_{0}}{q_{1}q_{2}q_{3}}
$$

From that we can guess the form of the general solution:

$$
x_{i}=x_{0}\frac{p_{i-1}p_{i-2}\cdots p_{1}}{q_{i}q_{i-1}\cdots q_{1}}\underset{p_{0}=1}{=}x_{0}\prod_{k=0}^{i-1}\frac{p_{k}}{q_{k+1}}\qquad i>0
$$

and substitute it back in (3.13) to check if it is right:

$$
p_{i-1}x_{i-1}+q_{i+1}x_{i+1} =p_{i-1}\frac{p_{i-2}\cdots p_{1}}{q_{i-1}\cdots q_{1}}+q_{i+1}\frac{p_{i}\cdots p_{1}}{q_{i+1}\cdots q_{1}}=
=\frac{p_{i-1}\cdots p_{1}}{q_{i}\cdots q_{1}}\underbrace{(q_{i}+p_{i})}_{1}=x_{i}
$$


All that's left is to fix the value of  $x_0$  by imposing the normalization:

$$
\sum_ {i = 0} ^ {+ \infty} x _ {i} = x _ {0} \sum_ {i = 0} ^ {+ \infty} \prod_ {k = 0} ^ {i - 1} \frac {p _ {k}}{q _ {k + 1}} = 1 \Rightarrow x _ {0} = \left(\sum_ {i = 0} ^ {+ \infty} \prod_ {k = 0} ^ {i - 1} \frac {p _ {k}}{q _ {k + 1}}\right) ^ {- 1} \tag {3.17}
$$

(with the convention that a product with no elements is equal to 1, the neutral element of the product:  $\prod_{k=0}^{0}(\dots) = 1$ ).

The stationary solution (3.16) exists only if the infinite sum in (3.17) converges to a non-zero finite value. If it were diverging, then  $x_0 = 0$ , and so all  $x_i = 0 \forall i$ , meaning that the normalization constraint is not respecting.

Suppose that  $p_k \equiv p$  and  $q_k \equiv q$ , i.e. the probabilities of moving in one or the other direction are independent of the system's state. In this case we can directly inspect the convergence of the sum in (3.17):

- If  $p < q$ , the sum converges, and the chain is positive recurrent. Intuitively, in this case the system "tends to return over its steps", thus visiting the same states over and over.
- If  $p \geq q$ , the sum diverges and no solution exists, meaning that the chain is not positive recurrent. Intuitively, in this case the system tends to "escape" towards infinity, always visiting new transient states.

![[Stochastic_Processes_2020_p88_img25.jpeg]]
*Figure 3.6 - Block diagram for the success run Markov Chain*


Consider now the following Markov chain, describing the success runs of a sequence of binomial trials:

$$
\mathbf {P} = \left| \left| \begin{array}{c c c c c} p _ {0} & 1 - p _ {0} & 0 & 0 & \dots \\ p _ {1} & 0 & 1 - p _ {1} & 0 & \dots \\ p _ {1} & 0 & 0 & 1 - p _ {2} & \dots \\ \vdots & \ddots & \ddots & \ddots & \ddots \end{array} \right| \right| \quad (0 <   p _ {k} <   1)
$$

with the block diagram shown in figure 3.6. Clearly the chain is irreducible, and so all states are of the same type, meaning that to study their recurrence we can focus on only one of them, for example the 0-th.


So, let’s define the first return time $R_{0}$ to state 0:

$$
R_{0}=\min\{n\geq 1;X_{n}=0\}
$$

By just observing the diagram in fig. 3.6 we can compute the statistics of $R_{0}$:

$$
\mathbb{P}\{R_{0}>1|X_{0}=0\}=(1-p_{0})
\mathbb{P}\{R_{0}>2|X_{0}=0\}=(1-p_{0})(1-p_{1})
\mathbb{P}\{R_{0}>3|X_{0}=0\}=(1-p_{0})(1-p_{1})(1-p_{2})
$$

In fact the probability $\mathbb{P}\{R_{0}>i|X_{0}=0\}$ of returning to 0 for the first time after $i$ steps is equivalent to the probability of not returning to 0 for $i$ consecutive steps, which is necessarily the probability of travelling through states $1,\ldots,i$, as this is the only possible path that does not return to 0. So:

$$
\mathbb{P}\{R_{0}>k|X_{0}=0\}=(1-p_{0})(1-p_{1})\cdots(1-p_{k-1})=\prod_{i=0}^{k-1}(1-p_{i})
$$

Then note that:

$$
f_{00}^{(n)}=\mathbb{P}\{R_{0}=n|X_{0}=0\}\Rightarrow\mathbb{P}\{R_{0}>k|X_{0}=0\}=1-\sum_{n=1}^{k}f_{00}^{(n)}
$$

and rearranging:

$$
\sum_{n=1}^{k}f_{00}^{(n)}=1-\mathbb{P}\{R_{0}>k|X_{0}=0\}=1-\prod_{i=0}^{k-1}(1-p_{i})
$$

By definition, state 0 is recurrent if the sum in (3.19) is 1 for $k\to\infty$, i.e. if:

$$
\lim_{k\to\infty}\prod_{i=0}^{k-1}(1-p_{i})=\prod_{i=0}^{\infty}(1-p_{i})=0
$$

(3.20) is equivalent to:

$$
\sum_{i=0}^{\infty}p_{i}=\infty
$$

by the application of lemma 3.4.3.

State 0 is positive recurrent when the average return time $m_{0}=\mathbb{E}[R_{0}|X_{0}=0]$ is finite:

$$
m_{0}=\sum_{k=0}^{\infty}\mathbb{P}\{R_{0}>k|X_{0}=0\}=
\underset{(3.18)}{=}1+\sum_{k=1}^{\infty}\prod_{i=0}^{k-1}(1-p_{i})
$$


And $m<\infty$ only if:

$$
\sum_{k=1}^{\infty}\prod_{i=0}^{k-1}(1-p_{i})<\infty
$$

which is a *stronger* requirement than (3.19), as expected. In this case, we can compute the stationary probability $\pi_{0}$ as the reciprocal of $m_{0}$:

$$
\pi_{0}=\frac{1}{m_{0}}=\frac{1}{1+\sum_{k=1}^{\infty}\prod_{i=0}^{k-1}(1-p_{i})}
$$

And then derive all the other stationary probabilities from the equations for the stationary distribution:

$$
(1-p_{0})\pi_{0} =\pi_{1}
(1-p_{1})\pi_{1} =\pi_{2}
(1-p_{2})\pi_{2} =\pi_{3}
\vdots
$$

leading to:

$$
\pi_{1} =(1-p_{0})\pi_{0}
\pi_{2} =(1-p_{1})\pi_{1}=(1-p_{1})(1-p_{0})\pi_{0}
\pi_{3} =(1-p_{2})\pi_{2}=(1-p_{2})(1-p_{1})(1-p_{0})\pi_{0}
$$

And in general:

$$
\pi_{k}=\pi_{0}\prod_{i=0}^{k-1}(1-p_{i})\qquad k\geq 1
$$

In the special case where all the $p_{i}$ are equal to a constant $p=1-q$, then:

$$
\prod_{i=0}^{k-1}(1-p_{i})=q^{k}\Rightarrow m_{0}=1+\sum_{k=1}^{\infty}q^{k}=\frac{1}{p}
$$

and $\pi_{k}=pq^{k}$ for $k\in\mathbb{N}$.


If $0<p_{i}<1$, $i\in\mathbb{N}$, then:

$$
u_{m}=\prod_{i=0}^{m}(1-p_{i})\xrightarrow[m\to\infty]{}0\Leftrightarrow\sum_{i=0}^{\infty}p_{i}=\infty
$$


Suppose that:

$$
\sum_{i=0}^{\infty}p_{i}=\infty
$$


Then:

$$
1-p_{i}<1-p_{i}+\frac{p_{i}^{2}}{2!}-\frac{p_{i}^{3}}{3!}+\cdots=e^{-p_{i}}\qquad i\in\mathbb{N}
$$

In fact $y=1-x$ is the tangent of $y=e^{-x}$ at $x=0$, and because $e^{-x}$ is convex, it is always higher than its tangents.
Since (3.22) holds for any $i$, it holds also for the product:

$$
\prod_{i=0}^{m}(1-p_{i})<\exp\left(-\sum_{i=0}^{m}p_{i}\right)\xrightarrow[n\to\infty]{(3.21)}0
$$

And so we have proved:

$$
\sum_{i=0}^{\infty}p_{i}=\infty\Rightarrow\prod_{i=0}^{\infty}(1-p_{i})=0
$$

To prove the converse, we assume:

$$
\lim_{m\to\infty}\prod_{i=0}^{m}(1-p_{i})=0
$$

Then we make use of the following inequality:

$$
\prod_{i=j}^{m}(1-p_{i})>(1-p_{j}-p_{j+1}-\cdots-p_{m})=1-\sum_{i=j}^{m}p_{i}\qquad m\geq j+1
$$

which can be proved by induction. It holds for $m=j+1$:

$$
(1-p_{j})(1-p_{j+1})=1-p_{j}-p_{j+1}+p_{j}p_{j+1}>1-p_{j}-p_{j+1}
$$

because all the $p_{k}$ are non-zero, and so $p_{j}p_{j+1}>0$.
So, assuming it holds for $m$, we can prove that it holds for $m+1$:

$$
\prod_{i=j}^{m+1}(1-p_{i}) =(1-p_{m+1})\prod_{i=j}^{m}(1-p_{i})\underset{(3.24)}{\geq}(1-p_{m+1})\left(1-\sum_{i=j}^{m}p_{i}\right)=
=1-\sum_{i=j}^{m}p_{i}-p_{m+1}+\underbrace{p_{m+1}\sum_{i=j}^{m}p_{i}}_{>0}>1-\sum_{i=j}^{m+1}p_{i}
$$

and so it is true for every $m$.
Then we proceed by contradiction. Suppose that the sum (3.21) actually converges:

$$
\sum_{i=0}^{\infty}p_{i}<\infty
$$


This means that the tail sum must vanish:

$$
\lim_{j\to\infty}\sum_{i=j}^{\infty}p_{i}=0
$$

So it must become arbitrarily small, and in particular it must be *definitely* between $0$ and $1$:

$$
\exists j_{0}>1\text{ s.t. }0<\sum_{i=j}^{\infty}p_{i}<1\quad\forall j>j_{0}
$$

But in that case, applying (3.24) leads to:

$$
\lim_{m\to\infty}\prod_{i=j}^{m}(1-p_{i})>\lim_{m\to\infty}\Bigg{(}1-\underbrace{\sum_{i=j}^{m}p_{i}}_{<1}\Bigg{)}>0
$$

Now note that the lhs of (3.27) differs from (3.23) by only a finite number of non-zero factors (because the $p_{i}\neq 1$). So:

$$
\lim_{m\to\infty}\prod_{i=j}^{m}(1-p_{i})>0\Rightarrow\lim_{m\to\infty}\prod_{i=0}^{\infty}(1-p_{i})>0
$$

But this contradicts our hypothesis (3.23), meaning that (3.25) cannot be true, and so:

$$
\prod_{i=0}^{\infty}(1-p_{i})=0\Rightarrow\sum_{i=0}^{\infty}p_{i}=\infty
$$

which concludes the proof.

∎

### Example 8 - Recurrence of G/M/1 Queue

> [!Example] Example 8 - Recurrence of G/M/1 Queue
> **Problem:** Determine when the G/M/1 queue is positive recurrent from its transition probabilities.
>
> **Approach:** Solve the stationarity equation with the ansatz $\pi_k=c\beta^k$ and analyze the fixed point $\beta=A(\beta)$.
>
> **Solution:** The complete worked solution is transcribed below.
>
> **Takeaway:** For the G/M/1 queue, stability corresponds to arrivals being slower than service: $\lambda<\mu$.

Let’s now examine when the G/M/1 queue is positive recurrent. We already computed the transition probabilities in (2.4) at page 36:

$$
P_{i,i+1-j} =\int_{0}^{\infty}e^{-\mu t}\frac{(\mu t)^{j}}{j!}\,\mathrm{d}G(t)\qquad j=0,1,\ldots,i
P_{i0} =\int_{0}^{\infty}\sum_{k=i+1}^{\infty}e^{-\mu t}\frac{(\mu t)^{k}}{k!}\,\mathrm{d}G(t)\qquad i\geq 0
$$

The chain is irreducible, meaning that all states are in the same class, and also aperiodic. So, to prove positive recurrence, we just need to solve the stationarity equation:

$$
\pi_{k}=\sum_{i}\pi_{i}P_{ik}\quad k\geq 0\qquad\sum_{k}\pi_{k}=1
$$


which in this case becomes:

$$
\pi_{k}=\sum_{i=k-1}^{\infty}\pi_{i}\int_{0}^{\infty}e^{-\mu t}\frac{(\mu t)^{i+1-k}}{(i+1-k)!}\,\mathrm{d}G(t)\quad k\geq 1\qquad\sum_{k=0}^{\infty}\pi_{k}=1
$$

We ignore the case $k=0$, which is more complicated, as we will be able to compute $\pi_{0}$ by imposing normalization.

To solve (3.28) we use the ansatz $\pi_{k}=c\beta^{k}$, leading to:

$$
c\beta^{k}=c\sum_{i=k-1}^{\infty}\beta^{i}\int_{0}^{\infty}e^{-\mu t}\frac{(\mu t)^{i+1-k}}{(i+1-k)!}\,\mathrm{d}G(t)=
$$

We exchange the integral and the sum (which is allowed because we are dealing with all non-negative terms, meaning that the partial sums are monotone functions, and we can apply Lebesgue’s monotone convergence theorem). We also split $\beta^{i}$ in two factors, bringing one inside the inner sum, constructing an exponential:

$$
=c\int_{0}^{\infty}e^{-\mu t}\beta^{k-1}\sum_{i=k-1}^{\infty}\frac{(\beta\mu t)^{i+1-k}}{(i+1-k)!}\;\mathrm{d}G(t)=
=c\int_{0}^{\infty}e^{-\mu t}\beta^{k-1}\ e^{\beta\mu t}\ \mathrm{d}G(t)
$$

Rearranging:

$$
\beta=\int_{0}^{\infty}e^{-\mu t(1-\beta)}\,\mathrm{d}G(t)
$$

Note that this result does not depend on $k$ - so if we find a solution for $\beta$ such that $\pi_{k}=c\beta^{k}$ is normalizable we would have the entire stationary distribution, proving positive recurrence.

Clearly it must be $0<\beta<1$, otherwise $\sum_{k}\pi_{k}=\sum_{k}c\beta^{k}$ would either be $0$ or diverge.

We rewrite (3.29) as follows:

$$
\beta=\int_{0}^{+\infty}e^{-\mu t(1-\beta)}\,\mathrm{d}G(t)=\mathbb{E}[e^{-\mu T(1-\beta)}]=A(\beta)
$$

and study the intersections of the curves $y=\beta$ and $y=A(\beta)$.

First we examine the two extrema:

$$
A(0)=\int_{0}^{+\infty}e^{-\mu t}\,\mathrm{d}G(t)>0
A(1)=\int_{0}^{+\infty}\mathrm{d}G(t)=1
$$

Then the first two derivatives:

$$
A^{\prime}(\beta)=\int_{0}^{+\infty}\mu te^{-\mu t(1-\beta)}\,\mathrm{d}G(t)>0\qquad\forall\beta
A^{\prime\prime}(\beta)=\int_{0}^{+\infty}(\mu t)^{2}e^{-\mu t(1-\beta)}\,\mathrm{d}G(t)>0\qquad\forall\beta
$$


Summarizing, $A(\beta)$ is strictly increasing and convex, and goes from $(0,A(0))$ with $A(0)>0$ to $(1,1)$.

So, with respect to $y=\beta$, there are only two possible behaviours, as illustrated in fig. 3.7:

1. $A(\beta)$ reaches $(1,1)$ “from above”, i.e. $A^{\prime}(1)<1$, meaning that:

$$
A^{\prime}(1)=\mu{\rm I\kern-1.79993ptE}[T]=\frac{\mu}{\lambda}<1\Leftrightarrow\lambda>\mu
$$

where $\lambda=1/{\rm I\kern-1.79993ptE}[T]$ is the arrival rate in the queue.

In this case there are no intersections with $y=\beta$ except the trivial one at $(1,1)$, which is not acceptable (because we need $0<\beta<1$). Thus (3.29) has no solutions.

Note that this does not prove that the chain is not positive recurrent, but only that the ansatz we started from is not valid. However, from other considerations, we know that the Markov chain is transient for $\lambda>\mu$ - because more people arrive than depart, and so the system’s state in the long run will “escape towards infinity”.
2. $A(\beta)$ reaches $(1,1)$ from below, i.e. $A^{\prime}(1)>1$. This happens if:

$$
A^{\prime}(1)=\mu{\rm I\kern-1.79993ptE}[T]=\frac{\mu}{\lambda}>1\Leftrightarrow\lambda<\mu
$$

In this case there is a non-trivial intersection with $y=\beta$, which is denoted as $\beta^{*}\in(0,1)$. This is a valid solution for (3.29), thus proving both that our ansatz was valid, and that the chain is positive recurrent.

This case corresponds to an arrival rate $\lambda$ that is less than that one of departures, and so intuitively we expect the system to be stable, returning over and over to the same “low” states.

In summary: we started with the stationarity equation (3.28), introduced an ansatz leading to the integral equation (3.29), for which we have found a solution in the case $\lambda<\mu$.

As the chain is irreducible and aperiodic, if a stationary solution exists then it is unique, and corresponds to the limiting distribution. So, the solution we have found by guessing its form is rigorous, and it’s the only correct solution in its domain.

However, outside that domain, we can only say that the ansatz was not useful, and we need to employ other methods to actually draw any conclusion about the chain’s recurrence.

Finally, we spend some words on the critical case $\lambda=\mu$, with $A^{\prime}(1)=1$. Here there is a double intersection with $y=\beta$ at $(1,1)$, and so (3.29) has no solution, and we cannot draw any conclusion with our method.

However, it can be shown that in this case the chain is null recurrent. So:

- $\lambda<\mu$: chain is positive recurrent (or stable)


- $\lambda = \mu$: chain is null recurrent
- $\lambda > \mu$: chain is transient (or unstable)

![[Stochastic_Processes_2020_p95_img26.jpeg]]
*Figure 3.7 - There are only two possible behaviours for $A(\beta)$, resulting in either 0 or exactly 1 intersections with $y = \beta$.*

### 3.4.1 Periodic generalization

We proved the existence of a limiting distribution for irreducible, positive recurrent, aperiodic Markov chains. In the periodic case, clearly the limiting distribution cannot exist:

$$
\breve{\Delta} \lim_{n \to \infty} P_{ij}^{(n)}
$$

However, we can inspect $P_{ij}^{(n)}$ only for $n$ that are multiples of the period $d$ of the chain. In this case, it can be shown that:

$$
\lim_{n \to \infty} P_{ii}^{(nd)} = \frac{d}{m_i}
$$

We can always consider the mean time that the system spends in state $i$, and define a "limiting distribution" as follows:

$$
\lim_{n \to \infty} \frac{1}{n} \sum_{m = 0}^{n - 1} P_{ii}^{(m)} \equiv \pi_i = \frac{1}{m_i} \tag{3.30}
$$

In fact now the sum is over all states, also the ones that are non-multiples of $d$. However, by periodicity we know that $P_{ii}^{n} = 0$ if $n$ is not a multiple of $d$, while $P_{ii}^{(nd)} \xrightarrow[n \to \infty]{} d / m_i$. So, during a single period from $1 \to d$, we find null values for $d - 1$ terms because we can not be in the $i$-th state before the period ends, and $d / m_i$ for the last one, leading to an average of exactly $1 / m_i$.

Again, the $\pi_j$ so defined can be found as the unique nonnegative solution to


the stationarity equations:

$$
\pi_ {j} = \sum_ {k = 0} \pi_ {k} P _ {k j} \qquad \sum_ {j = 0} ^ {\infty} \pi_ {j} = 1
$$

## 3.5 Reducible Markov chains

While most Markov chains encountered in stochastic modelling are irreducible, sometimes it can happen to deal with a reducible case.

One such example is the following:

$$
\mathbf {P} = \left\| \begin{array}{c c c c} \frac {1}{2} & \frac {1}{2} & 0 & 0 \\ \frac {1}{4} & \frac {3}{4} & 0 & 0 \\ 0 & 0 & \frac {1}{3} & \frac {2}{3} \\ 0 & 0 & \frac {2}{3} & \frac {1}{3} \end{array} \right\| = \left\| \begin{array}{c c} \mathbf {P} _ {1} & \mathbf {O} \\ \mathbf {O} & \mathbf {P} _ {2} \end{array} \right\| \qquad \mathbf {P} _ {1} = \left\| \begin{array}{c c} \frac {1}{2} & \frac {1}{2} \\ \frac {1}{4} & \frac {3}{4} \end{array} \right\|; \mathbf {P} _ {2} = \left\| \begin{array}{c c} \frac {1}{3} & \frac {2}{3} \\ \frac {2}{3} & \frac {1}{3} \end{array} \right\|
$$

This chain contains two isolate classes, which can be modelled as two separate chains with transition matrices  $\mathbf{P}_1$  and  $\mathbf{P}_2$ . Their evolution can be completely separated, and in fact:

$$
\mathbf {P} ^ {n} = \left\| \begin{array}{c c} \mathbf {P} _ {1} ^ {n} & \mathbf {O} \\ \mathbf {O} & \mathbf {P} _ {2} ^ {n} \end{array} \right\|
$$

In general, however, one-way transitions between different classes can happen.

We can apply the basic limit theorem to any aperiodic recurrent class in a reducible Markov chain. As we previously noted, a recurrent class must be isolate from the others, meaning that if  $i$  is in that class and  $j$  in another, then  $P_{ij}^{(n)} = 0 \forall n$ . On the other hand, for states in the same class we have, in the long run:

$$
\lim  _ {n \rightarrow \infty} P _ {i j} ^ {(n)} = \frac {1}{m _ {j}} \geq 0 \tag {3.31}
$$

If a class is transient, then the system will stay in it for a finite time, and then leave it and never return. So, for any transient state  $j$  we have:

$$
\lim  _ {n \rightarrow \infty} P _ {i j} ^ {(n)} = 0 \quad \forall i \tag {3.32}
$$

Summarizing, (3.31) covers transitions between recurrent states, and (3.32) the ones to a transient state.

The only remaining case to examine is that of a starting transient state  $i$ , and final recurrent state  $j$ .


Let's see what happens with an example:

$$
\mathbf {P} = \left. \begin{array}{c c c c c} 0 & 0 & 1 & 2 & 3 \\ 0 & \frac {1}{2} & \frac {1}{2} & 0 & 0 \\ 1 & \frac {1}{4} & \frac {3}{4} & 0 & 0 \\ 2 & \frac {1}{4} & \frac {1}{4} & \frac {1}{4} & \frac {1}{4} \\ 3 & 0 & 0 & 0 & 1 \end{array} \right| \tag {3.33}
$$

There are three classes:  $A = \{0,1\}$ ,  $B = \{2\}$  and  $C = \{3\}$ .

Looking at the block diagram in fig. 3.8, we can see that:

- If the system starts in  $A$ , it will remain there forever. Note that  $A$  is aperiodic, because of the non-zero probabilities of same-state transitions  $0 \to 0$  and  $1 \to 1$ .

We can then search for the stationary distribution:

$$
\pi_ {j} = \sum_ {i = 0} ^ {1} \pi_ {i} P _ {i j} \quad j = 0, 1 \qquad \pi_ {0} + \pi_ {1} = 1
$$

leading to the following system of equations:

$$
\left\{ \begin{array}{l} \pi_ {0} = \pi_ {0} \cdot \frac {1}{2} + \pi_ {1} \cdot \frac {1}{4} \\ \pi_ {1} = \pi_ {0} \cdot \frac {1}{2} + \pi_ {1} \cdot \frac {3}{4} \end{array} \right.
$$

We need to solve only one of them, and then impose the normalization:

$$
\pi_ {0} = \frac {\pi_ {1}}{2} \wedge \pi_ {0} + \pi_ {1} = 1 \Rightarrow \pi_ {0} = \frac {1}{3} \quad \pi_ {1} = \frac {2}{3}
$$

And so  $A$  is positive recurrent.

-  $C$  is formed by a single absorbing state, and so here the chain's behaviour is trivial: the class is aperiodic, positive recurrent, with limiting probability merely given by  $\pi_3 = 1$ .
- Class  $B$  is transient: its only state cannot ever be reached from different states, and it is not absorbing. Transitions  $B \to C$  and  $B \to A$  are possible, but one-way.

In the long run, clearly  $\pi_{22} \equiv \lim_{n \to \infty} P_{22}^{(n)} = 0$ , because 2 is transient. To get the other probabilities we can apply first-step analysis to classes. Explicitly, let  $u \equiv \pi_A$  denote the probability of absorption in class  $A$  if the system starts at 2. Then  $1 - u \equiv \pi_C$  is the probability of absorption in  $C$ . So:

$$
u = (P _ {2 0} + P _ {2 1}) \cdot 1 + \frac {1}{4} \cdot u + \frac {1}{4} \cdot 0 = \frac {1}{2} + \frac {1}{4} u \Rightarrow u = \frac {2}{3}
$$

In this case we could have just noted that, if starting at 2, the probability of going to  $C$  is half that of going to  $A$ . Imposing normalization this leads


directly to  $\pi_{23} = 1 / 3$ , and  $\pi_A = \pi_{20} + \pi_{21} = 2 / 3$ .

When the system is in  $A$ , the probabilities of being in 0 or 1 (in the limit), are the ones found before, i.e.  $\pi_0$  and  $\pi_1$ .

So, to get from 2 to 0, we first need to move from  $B$  to class  $A$ , and then to be in the correct state in the limit:

$$
\pi_ {2 0} = \lim _ {n \to \infty} \mathbb {P} (X _ {n} = 0 | X _ {n} \in A) \mathbb {P} (X _ {n} \in A | X _ {0} = 2) = \pi_ {0} \cdot \pi_ {A} = \frac {2}{3} \cdot \frac {1}{3} = \frac {2}{9}
$$

Similarly, for  $2\to 1$

$$
\pi_ {2 1} = \pi_ {A} \cdot \pi_ {1} = \frac {2}{3} \cdot \frac {2}{3} = \frac {4}{9}
$$

Summarizing, the limiting distribution for the whole chain is given by:

|  limn→∞Pn= | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |  π0 | π1 | 0 | 0 | 1 | 2 | 3 |   |
|   |  π0 | π1 | 0 | 0 | 1 | 2 | 3 |   |
|   |  π20 | π21 | 0 | π23 | 2 | 3 | 0 | 1  |
|   |  0 | 0 | 0 | 1 | 3 | 0 | 0 | 1  |

![[Stochastic_Processes_2020_p98_img27.jpeg]]
*Figure 3.8 - Block diagram for the Markov chain in (3.33).*


Consider the problem of sending a binary message 0,1 through a signal channel consisting of several stages, where transmission through each stage is subject to a fixed probability of error  $\alpha$ . Let  $X_0$  be the signal that is sent and let  $X_n$  be the signal that is received at the  $n$ -th stage. Suppose that  $X_n$  is a Markov chain with transition probabilities:

$$
P _ {0 0} = P _ {1 1} = 1 - \alpha \quad P _ {0 1} = P _ {1 0} = \alpha , \quad (0 <   \alpha <   1)
$$

Determine  $Pr\{X_5 = 0 | X_0 = 0\}$  that is the probability of correct transmission through five stages.

Solution.

### 3.5.1 Another behaviour of infinite Markov chains

It is possible for all states of a infinite Markov chain to be either transient or null recurrent, such that the transition probability linking any two of them $i$, $j$ vanishes in the limit: $\lim_{n\to \infty}P_{ij}^{(n)} = 0$ [1, p. 220].

A trivial example is given by the Markov chain with the update rule:

$$
\left\{ \begin{array}{l} X _ {n} = X _ {n - 1} + 1 \\ X _ {0} = 0 \end{array} \right.
$$


Infinite chain of non-recurring states

meaning that $X_{n} = X_{0} + n$, and the transition matrix is:

$$
\mathbf {P} = \left[ \begin{array}{c c c c c} 0 & 1 & 2 & 3 & \dots \\ 0 & 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 1 & 0 \\ 2 & 0 & 0 & 0 & 1 \\ 3 & 0 & 0 & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \vdots \end{array} \right]
$$

In this case each state can be visited at most one time. More precisely the $n$-th state will be visited at time step $n$ and then abandoned forever. As a consequence, all states of the chain are transient, and each one of them forms a class by itself.

Clearly, such kind of behaviour can be realized only in Markov chains with infinitely many possible states - meaning that a MC with a finite number $N$ of states, must have no null recurrent states, and not all of its states can be transient. Informally: the chain must always be "somewhere", and given infinite time and only a finite number of states, then it is forced to return to some states it visited before. Let's prove this in two steps [2, day 10/04]:

1. First we will prove the presence of at least a positive recurrent state
2. Then we will prove the absence of null recurrent states

Lemma 3.5.1. In a Markov chain with a finite number of states, there must be at least one positive recurrent state.

Proof. We proceed by contradiction. Consider a chain with a finite number $M < \infty$ of states, and suppose that there are no positive recurrent states, meaning that:

$$
\lim  _ {n \rightarrow \infty} P _ {i j} ^ {(n)} = 0 \tag {3.34}
$$

By normalization, we know that summing over the $i$-th of the $n$-step transition matrix leads to 1:

$$
\sum_ {j = 1} ^ {N} P _ {i j} ^ {(n)} = 1 \qquad \forall n
$$

1. Finite states $\Rightarrow$ at least one is positive recurrent


This must hold also in the limit:

$$
\lim _ {n \to \infty} \sum_ {j = 1} ^ {N} P _ {i j} ^ {(n)} \stackrel {!} {=} 1
$$

However, as  $N$  is finite, we can exchange the order of sum and limit, leading to:

$$
1 \stackrel {!} {=} \lim  _ {n \rightarrow \infty} \sum_ {j = 1} ^ {N} P _ {i j} ^ {(n)} = \sum_ {j = 1} ^ {N} \lim  _ {n \rightarrow \infty} P _ {i j} ^ {(n)} = 0 \tag {3.35}
$$

which is clearly a contradiction. Therefore we conclude that our initial assumption was wrong, so there must be at least one positive recurrent state in the chain. In other words, in the long run, a finite chain must "find itself somewhere".

Conversely, any chain in which all states are transient must be infinite. In this case the exchange of the sum with the limit in (3.35) would not be legitimate, thus not leading to a contradiction.

Lemma 3.5.2. In a Markov chain with a finite number of states there cannot be any null recurrent states.

Proof. We proceed again by contradiction. Suppose there is one null recurrent state. Recalling that it is a class property, we then know that it must belong to a finite null recurrent class (as there are is only a finite number of states available). On the other hand a null recurrent class can be considered a Markov chain by itself: once we arrive into it, we are not supposed to leave. But from the previous result this is not possible: a finite class cannot be made by only null recurrent states, as it must have at least one positive recurrent state - thus contradicting our hypothesis.  $\square$

A corollary of these two lemmas is is that null recurrent states are only allowed in infinite chains.


We want to study the limiting behaviours i.e. computing using any kind of software (Python, R, MATLAB...) the two limits:  $\lim_{n\to \infty}\mathbf{P}^{(n)}$  and  $\lim_{n\to \infty}\mathbf{P}^{(2n + 1)}$  for the following two matrices:

$$
\mathbf {P} _ {1} = \left\| \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ \frac {1}{3} & \frac {1}{3} & \frac {1}{6} & \frac {1}{6} \\ 0 & 0 & 0 & 1 \end{array} \right\| \qquad \mathbf {P} _ {2} = \left\| \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ \frac {1}{6} & \frac {1}{3} & \frac {1}{3} & \frac {1}{6} \\ 0 & 0 & 0 & 1 \end{array} \right\|
$$

and then comment the results.

Solution. For both matrices can be easily identified the upper-left block  $\left( \begin{array}{ll}0 & 1\\ 1 & 0 \end{array} \right)$  that has period 2, then the two subsequences for  $n$  even and  $n$

2. Finite states  $\Rightarrow$  no null recurrent

Null recurrent states are possible only in infinite MCs


odd will individually converge, but each one for a different value. Therefore the general limits will not exist since they oscillate.

In particular for  $\mathbf{P_2}$  we expect that the general limit for the terms in the third row do not exist, because of the oscillating nature of the upper-left block. The third row refers to the probability that, given we started in the transient state 2, we end up in the periodic absorbing class  $\{0,1\}$ . Numerically we can see that both the two subsequences  $\lim_{n\to \infty}\mathbb{P}^{2n}$  and  $\lim_{n\to \infty}\mathbb{P}^{2n + 1}$  converge, but to different values:

$$
(\mathbf {P} _ {2}) ^ {1 0 0 0} = (\mathbf {P} _ {2}) ^ {1 0 0 2} = \left\| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ \frac {7}{1 6} & \frac {5}{1 6} & 0 & \frac {1}{4} \\ 0 & 0 & 0 & 1 \end{array} \right\| \qquad (\mathbf {P} _ {2}) ^ {1 0 0 1} = \left\| \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ \frac {5}{1 6} & \frac {7}{1 6} & 0 & \frac {1}{4} \\ 0 & 0 & 0 & 1 \end{array} \right\|
$$

This can be summarised by saying that the two limits individually exist and converge to different values, whereas the general limit does not since it keeps oscillating. Note that the probability of being in the absorbing class on the right side, is the proportion of going outside the transient state (2/3) and finally enter the state absorbing class (1/6).

On the other hand when we do the same with the first matrix  $\mathbf{P}_1$ :

$$
(\mathbf {P} _ {1}) ^ {1 0 0 0} = (\mathbf {P} _ {1}) ^ {1 0 0 2} = \left\| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ \frac {4}{1 0} & \frac {4}{1 0} & 0 & \frac {2}{1 0} \\ 0 & 0 & 0 & 1 \end{array} \right\| \qquad (\mathbf {P} _ {1}) ^ {1 0 0 1} = \left\| \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ \frac {4}{1 0} & \frac {4}{1 0} & 0 & \frac {2}{1 0} \\ 0 & 0 & 0 & 1 \end{array} \right\|
$$

Everything is very similar to the example above. The probability of going out of the state 2 is now  $5/6$ . Starting from there we can be absorbed either into the class  $\{0,1\}$  with probability  $2/3$ , or end up in the absorbing class on the right side with probability  $1/6$ . Once we are absorbed by the  $\{0,1\}$  class, however, we can find ourselves with equal probability either in 0 or in 1 state. This is valid for any value of  $n$  when taking the limit, that is both for odd and even values, whereas before they were different.

Finally we can conclude that, for this special case, despite the presence of the periodic upper-left class, the two subsequences converge to an unique value, thus making the limit  $\lim_{t\to \infty}P_{2j}^{(n)}$  exist.


![[Stochastic_Processes_2020_p102_img28.jpeg]]
*Figure 3.9 - Markov chain for example n. 10*


In order to generalize the previous example, let us consider the following chain:

$$
\mathbf {P} = \left\| \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ a & b & c & 1 - a - b - c \\ 0 & 0 & 0 & 0 \end{array} \right\|
$$

Here we can tell easily that 2 is a transient state. It may lead either to the periodic  $\{0,1\}$  class or to an other recurrent class that we can consider, for our purposes, as a single absorbing state. This chain has a transition matrix of the  $\mathbf{P}_1$  kind written above.

Compute  $\mathrm{P}[X_{2n} = 0|X_0 = 2]$  and  $\mathrm{P}[X_{2n + 1} = 0|X_0 = 2]$  and find under which conditions on the transition rates  $a, b, c$  it holds that:

$$
\lim _ {n \to \infty} P [ X _ {2 n} = 0 | X _ {0} = 2 ] = \lim _ {n \to \infty} P [ X _ {2 n + 1} = 0 | X _ {0} = 2 ]
$$

Comment the result on the conditions just found in a probabilistic fashion. Solution. Will be provided next lecture. See (13).

## 3.6 Absorption probabilities

We have seen through an example (3.33, pag. 97) that the  $n$ -step transition probability  $\mathbb{P}^{(n)}(A \to B)$  to go from a transient state  $A$  to a recurrent state  $B$ , in the long run ( $n \to \infty$ ), is the product between two values: the probability of being absorbed in the recurrent class of  $B$ , and the limiting probability of  $B$  within that class. Let's now formalize this statement [3, p. 91].

Let  $i \in T$  be a transient state, and  $k \in C$  a recurrent one (with this property extending to the respective classes). Suppose we start at  $X_0 = i$ . The probability of entering  $C$  for the first time at step  $n$  by reaching state


$k\in C$ is given by:

$$
\pi^{(n)}_{ik}(C)=\mathbb{P}[X_{n}=k,\;X_{m}\notin C,\;m=1,2,...,n-1|X_{0}=i]
$$

Summing over all possible states $k\in C$ we get the probability of entering $C$ from state $i$ at time step $n$ for the first time:

$$
\pi^{(n)}_{i}(C)=\sum_{k\in C}\pi^{(n)}_{ik}(C)
$$

The events of entering $C$ for the first time at different timesteps are clearly disjoint. Summing over all possible $n$, we get the “generic” probability of entering class $C$ at any time from state $i$:

$$
\pi_{i}(C)=\sum_{n=1}^{+\infty}\pi^{(n)}_{i}(C)
$$

Having established this notation, we can state the following theorem *[3, p. 91]*:


> [!Important] Theorem 3.6.1 - Limiting Probability from a Transient State to a Recurrent Class
> **Statement:** Let $j\in C$ and $i\in T$, where $C$ is an aperiodic recurrent class and $T$ is a transient one. Then:
>
> $$
> \lim_{n\to\infty}P^{(n)}_{ij}=\pi_{i}(C)\lim_{n\to\infty}P^{(n)}_{jj}=\pi_{i}(C)\cdot\pi_{j}
> $$
>
> **Proof:** The complete argument is derived immediately below from the first entrance decomposition and the Basic Limit Theorem.
>
> **Intuition:** To be in $j$ in the long run after starting from a transient state, the chain must first be absorbed into $C$, and then it must mix inside $C$ according to the limiting probability of $j$.

Let $j\in C$ and $i\in T$, where $C$ is an aperiodic recurrent class and $T$ is a transient one. Then it holds that:

$$
\lim_{n\to\infty}P^{(n)}_{ij}=\pi_{i}(C)\lim_{n\to\infty}P^{(n)}_{jj}=\pi_{i}(C)\cdot\pi_{j}
$$

(Note that the limit depends on both $i$ and $j$).

Proof. Decompose the event $\{X_n=j\}$ according to the first time $r$ at which the chain enters the recurrent class $C$, and according to the first state $k\in C$ reached at that entrance time. Since $j\in C$, being at $j$ at time $n$ means that the chain must have entered $C$ at some time $r\leq n$. Therefore:

$$
P^{(n)}_{ij}=\sum_{r=1}^{n}\sum_{k\in C}\pi^{(r)}_{ik}(C)P^{(n-r)}_{kj}.
$$

For fixed $r$ and $k\in C$, the class $C$ is aperiodic and recurrent, so the Basic Limit Theorem gives:

$$
\lim_{n\to\infty}P^{(n-r)}_{kj}=\pi_j.
$$

The terms $\pi^{(r)}_{ik}(C)P^{(n-r)}_{kj}$ are non-negative and bounded by $\pi^{(r)}_{ik}(C)$, and the total mass of the dominating series is:

$$
\sum_{r=1}^{+\infty}\sum_{k\in C}\pi^{(r)}_{ik}(C)=\sum_{r=1}^{+\infty}\pi^{(r)}_i(C)=\pi_i(C).
$$

Thus the limit may be exchanged with the sum, yielding:

$$
\lim_{n\to\infty}P^{(n)}_{ij}
=\sum_{r=1}^{+\infty}\sum_{k\in C}\pi^{(r)}_{ik}(C)\pi_j
=\pi_j\sum_{r=1}^{+\infty}\pi^{(r)}_i(C)
=\pi_i(C)\pi_j.
$$

This proves:

$$
\lim_{n\to\infty}P^{(n)}_{ij}=\pi_i(C)\lim_{n\to\infty}P^{(n)}_{jj}=\pi_i(C)\pi_j.
$$


$$
\lim_{n\to\infty}\sum_{m=0}^{n-1}P^{(m)}_{ij}
$$

Limiting transition probability transient $\to$ recurrent

Limiting transition matrix (3.38).


Let us take a look on an exercise assigned on the 05-09-2007 written exam, that is very similar to the ones that we should expect to find in tests.

Consider a Markov chain with the following transition matrix:

$$
\mathbf {P} = \left| \begin{array}{c c c c c} 0 & 1 & 2 & 3 & 4 \\ 0 & 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 & 0 \\ 2 & 0 & 0 & 0.4 & 0.6 \\ 3 & 0.5 & 0 & 0 & 0.2 \\ 4 & 0 & 0 & 0.6 & 0.4 \end{array} \right| \tag {3.38}
$$

1. Classify the states and identify the classes
2. Compute the probabilities of absorption in all recurrent classes starting from each transient state
3. Compute  $\lim_{n\to \infty}\mathbf{P}^n$  and  $\lim_{n\to \infty}\frac{1}{n}\sum_{k = 1}^{n}\mathbf{P}^k$
4. Compute the average recurrence times for all states

### Solution

1. As can be seen from the block diagram (fig. 3.10) there are three distinct classes:  $\mathbf{A} = \{0,1\}$ ,  $\mathbf{B} = \{3\}$ ,  $\mathbf{C} = \{2,4\}$ .

If the system starts in state 2 or 4, it never visits other states, so  $C$  is a positive recurrent class. Moreover it is aperiodic because the system may stay in the same state with non-zero probability.

The same occurs if we start in either 0 or 1, thus  $A$  is a positive recurrent class. However, in this case it is periodic, because the system deterministically goes back and forth from state 0 to state 1 with period  $d = 2$ .

Finally, class  $B$  consists only of the transient state 3, since no connections from other states lead back to it, but it leads to other states with non-zero probability.

2. Noting that there is only one transient state and two different absorbing classes, it is enough to compute just one of the two absorption probabilities - the other one will be its complementary to 1.

Starting in 3, we leave the state with probability  $0.3 + 0.5 = 0.8$ . Supposing that this happens, the system will go to  $C$  with a probability of  $\pi_3(\{2,4\}) \equiv \pi_3(C) = 0.3 / 0.8 = 3 / 8$ , given by the ratio of the total probability of transitions to  $C$  (0.3, only  $3 \to 4$  counts) and the total probability of leaving  $B$  in the first place (0.8). Similarly, the system goes to  $A$  with  $\pi_3(\{0,1\}) \equiv \pi_3(A) = 0.5 / 0.8 = 5 / 8$  - and both results sum to 1 as expected.


3. We start with the limit of the  $n$ -step transition matrix:

|  limn→∞P^n = | 0 | 1 | 2 | 3 | 4  |
| --- | --- | --- | --- | --- | --- |
|   |  0 | ? | ? | ? | ?  |
|   |  1 | ? | ? | ? | ?  |
|   |  2 | ? | ? | ? | ?  |
|   |  3 | ? | ? | ? | ?  |
|   |  4 | ? | ? | ? | ?  |

Since  $A$  is a periodic class, no limit exists for transition probabilities between elements of  $A$ , i.e.  $\{0,1\}$  - we denote this with a “ $\times$ ”. Clearly there is no way to exit  $A$ , and so the probabilities from  $\{0,1\}$  to any other state are 0:

|  limn→∞P^n = | 0 | 1 | 2 | 3 | 4  |
| --- | --- | --- | --- | --- | --- |
|   |  0 | × | × | 0 | 0  |
|   |  1 | × | × | 0 | 0  |
|   |  2 | ? | ? | ? | ?  |
|   |  3 | ? | ? | ? | ?  |
|   |  4 | ? | ? | ? | ?  |

Similarly, if the system starts in  $C = \{2,4\}$  it will remain there, as it is a recurrent class. As transition probabilities  $2 \leftrightarrow 4$  are symmetric, we expect the limiting/stationary probability to be the same for both states, i.e.  $\pi_2 = \pi_4 = 1/2$ :

|  limn→∞P^n = | 0 | 1 | 2 | 3 | 4  |
| --- | --- | --- | --- | --- | --- |
|   |  0 | × | × | 0 | 0  |
|   |  1 | × | × | 0 | 0  |
|   |  2 | 0 | 0 | 1/2 | 0  |
|   |  3 | ? | ? | ? | ?  |
|   |  4 | 0 | 0 | 1/2 | 0  |

Finally, as 3 is transient,  $\pi_{33} = 0$ . We have seen (theorem 3.6.1) that the limiting probabilities are the product between the probability of going to a class, and the limiting distribution within that class, so:

$$
\pi_{30} = \pi_3(A)\pi_0 \pi_{32} = \pi_3(C)\pi_2
\pi_{31} = \pi_3(A)\pi_1 \pi_{34} = \pi_3(C)\pi_4
$$

However,  $\pi_0$  and  $\pi_1$  do not exist (as  $A$  is periodic) and thus neither do  $\pi_{30}$  and  $\pi_{31}$ . On the other hand, we obtain:

$$
\pi_{32} = \pi_{34} = \frac{3}{8}\cdot \frac{1}{2} = \frac{3}{16}
$$


leading to:

![[Stochastic_Processes_2020_p106_img29.jpeg]]
*Figure 3.10a - Partial limiting transition matrix $\lim_{n\to\infty}\mathbf{P}^n$ for the chain in (3.38), where periodic entries in class $A$ do not have ordinary limits.*

Note that, as certain entries are missing, not all rows sum to 1.

All that's left is to compute:

$$
\lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 0} ^ {n} \mathbf {P} ^ {k}
$$

We know that anywhere  $\lim_{n\to \infty}\mathbf{P}^n$  exists,  $\lim_{n\to \infty}\frac{1}{n}\sum_{k = 1}^{n}\mathbf{P}^k$  will exist and will be equal. Whereas, for periodic cases where the limiting probabilities didn't exist before, they now do exist - and are given by the average fraction of time spent in those states. So:

$$
\pi_ {0} = \pi_ {1} = \frac {1}{d} = \frac {1}{2}
$$

And from (thm. 3.6.1):

$$
\pi_ {3 0} = \pi_ {3 1} = \pi_ {3} (A) \cdot \frac {1}{2} = \frac {5}{8} \cdot \frac {1}{2} = \frac {5}{1 6}
$$

leading to:

![[Stochastic_Processes_2020_p106_img30.jpeg]]
*Figure 3.10b - Cesaro limiting transition matrix $\lim_{n\to\infty}\frac{1}{n}\sum_{k=1}^{n}\mathbf{P}^k$ for the same chain, where periodic components are averaged over a full period.*

As a fast check, we note as all rows sum to 1, so our computations should be correct.

4. Let  $m_i$  be the average recurrence time of state  $m_i$ , and denote with  $\pmb{m}$  the  $d = 5$  vector containing all the  $m_i$ .

For an aperiodic recurrent class (such as  $C$ ) we know that, from the Basic Limit Theorem (3.6, pag. 81)  $m_i$  is the reciprocal of the limiting probability  $\pi_i$ :

$$
m _ {2} = m _ {4} = \left(\frac {1}{2}\right) ^ {- 1} = 2
$$


For the periodic recurrent class  $A$  we use the generalization (3.30, pag. 95):

$$
m _ {i} = \left(\lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 1} ^ {n} P _ {i i} ^ {(n)}\right) ^ {- 1} \Rightarrow m _ {0} = m _ {1} = \left(\frac {1}{2}\right) ^ {- 1} = 2
$$

For transient state 3, the same computation would lead  $m_3 = 1 / 0 = \infty$ . We can justify this result proceeding with first-step analysis. From state 3 only two types transitions are possible:  $3 \rightarrow 3$  with  $p = 0.2$  (leading to a recurrence time of 1) and  $3 \rightarrow 0 \lor 4$  with  $p = 0.8$  (leading to an infinite recurrence time, as then 3 is never visited again). So the average return time will be bigger than any number with a finite probability  $p = 0.8$ . This makes the average recurrence time for a transient state an improper random variable, thus necessarily implying that its average value must be infinite, and so  $m_3 = \infty$ .

In summary:

$$
\boldsymbol {m} = \left( \begin{array}{c} 2 \\ 2 \\ 2 \\ \infty \\ 2 \end{array} \right)
$$

Note that return times must be at least 1: they can not be zero even for transient states, since any transition requires at least one step. We denote the fact of "never returning" by saying that the (average) return time is infinite.

Let us summarize all possible cases in one table:

|  Start: i | End: j | limn→∞Pij(n)  |
| --- | --- | --- |
|  Any | Transient | 0  |
|  Recurrent ∈ C | Recurrent∉C | 0  |
|  Recurrent ∈ C | Recurrent ∈ C | πj=1/mj  |
|  Transient | Recurrent ∈ C | πi(C)πj=πi(C)/mj  |

Limiting transition probabilities between all types of states

*Table 3.2 - Summary of limiting transition probabilities  $i \rightarrow j$  between all possible types of states.  $\pi_i(C)$  denotes the probability of entering class  $C$  from state  $i$ , given by (3.36), and  $C$  is a aperiodic recurrent class.*

Table 3.2 can be extended to the case of  $C$  being a periodic recurrent class by just substituting  $\lim_{n\to \infty}P_{ij}^{(n)}$  with:

$$
\lim  _ {n \to \infty} \frac {1}{n} \sum_ {k = 1} ^ {n} P _ {i j} ^ {(k)}
$$


## 3.7 Transient states

In this section we will derive a criterion (i.e. a necessary and sufficient condition) for transiency for irreducible Markov chains, as sometimes using the recurrence definition (thm. 3.3.2) may not be convenient *[4, p. 78–82]*.

Let $S$ be a fixed set of states (arbitrarily chosen) of some irreducible Markov chain $\{X_{n}\}$. We denote with $Y_{i}(n)$ the probability that a system starting at state $i\in S$ will not leave $S$ for $n$ steps:

$$
Y_{i}(n)\equiv\mathbb{P}\{X_{j}\in S\quad\forall j=1,2,...,n|X_{0}=i\},\ i\in S
$$

In other words, $Y_{i}(n)$ is the probability of a system “surviving” $n$ steps in set $S$. For $n=1$ this amounts to the sum of transition probabilities to states inside $S$:

$$
Y_{i}(1)=\sum_{j\in S}P_{ij}
$$

And for $n>1$ we proceed by first-step analysis:

$$
Y_{i}(n)=\sum_{j\in S}P_{ij}Y_{j}(n-1)
$$

We now proceed to show several properties of $Y_{i}(n)$ *[2, day 10/04]*.

### Lemma 3.7.1.

> [!Important] Lemma 3.7.1 - Monotonicity of Survival Probabilities
> **Statement:** $Y_{i}(n)$ is a non-increasing function of $n$ for every $i\in S$.
>
> **Proof:** The induction proof is transcribed immediately below.
>
> **Intuition:** Surviving inside $S$ for more steps is a stricter event than surviving for fewer steps, so its probability cannot increase with time.

$Y_{i}(n)$ is a non-increasing function of $n$ $\forall i\in S$.


We proceed by induction. First we prove that it holds for $n=2$:

$$
Y_{i}(2)=\sum_{j\in S}P_{ij}Y_{j}(1)\underset{Y_{j}(1)\leq 1}{\leq}\sum_{j\in S}P_{ij}=Y_{i}(1)
$$

as $Y_{j}(1)$ is a probability.

Now, suppose the hypothesis holds up to $n$:

$$
Y_{i}(n)\leq Y_{i}(n-1)\leq\cdots\leq Y_{i}(1)
$$

Given that, we want to prove that it holds up to $n+1$ too:

$$
Y_{i}(n+1)\leq Y_{i}(n)
$$

Using (3.39) we get:

$$
Y_{i}(n+1)\underset{(3.39)}{\equiv}\sum_{j\in S}P_{ij}Y_{j}(n)\underset{(3.40)}{\leq}\sum_{j\in S}P_{ij}Y_{j}(n-1)=Y_{i}(n)\leq\cdots\leq Y_{i}(1)
$$

which concludes the proof. ∎

We have just found that $Y_{i}$ is a monotone (non-increasing) sequence, which is also bounded in the interval $[0,1]$ since it is a probability. Thus, it is convergent, i.e. $\lim_{n\to\infty}Y_{i}^{(n)}\equiv Y_{i}$ exists. Then, taking the limit of both sides of (3.39) leads to:

“Survival” probabilities are converging


$$
\lim_{n\to\infty}Y_{i}(n)=\lim_{n\to\infty}\sum_{j\in S}P_{ij}Y_{j}(n-1)\underset{(a)}{=}\sum_{j\in S}P_{ij}\lim_{n\to\infty}Y_{j}(n-1)
\Rightarrow Y_{i}=\sum_{j\in S}P_{ij}Y_{j}
$$

where exchanging the sum with the limit in (a) is allowed by the Lebesgue monotonic convergence theorem.

In summary, $Y_{i}$ can be interpreted as the probability that a Markov chain starting from state $i$, never leaves the set $S$, and it must satisfy (3.41).

We can then proceed backwards and try to solve (3.41) to determine $Y_{i}$. However, this requires some caution - as (3.41) is a set of homogeneous equations, allowing an infinite number of proportional solutions. Explicitly, if $\boldsymbol{Z}=(Z_{1},\ldots,Z_{N})^{T}$ solves (3.41), then $\boldsymbol{Z}^{\prime}=\alpha\boldsymbol{Z}\ \forall\alpha\in\mathbb{R}$ is a solution too.

As we are interested in finding $Y_{i}$, which are probabilities, we focus on the solutions $\boldsymbol{Z}$ which are bounded by 1:

$$
Z_{i}=\sum_{j\in S}P_{ij}Z_{j},\qquad|Z_{i}|\leq 1,\qquad i\in S
$$

It can be proved that if $Z_{i}$ is a solution of (3.42) and $Y_{i}$ is a solution of (3.41), we can say that $Y_{i}$ is the biggest solution of that set. More formally:

### Lemma 3.7.2.

> [!Important] Lemma 3.7.2 - Maximal Bounded Solution
> **Statement:** If $Z_i$ is any bounded solution of (3.42), with $|Z_i|\leq 1$, then $|Z_i|\leq Y_i$.
>
> $$
> |Z_{i}|\leq Y_{i}=\lim_{n\to\infty}Y_{i}(n)
> $$
>
> **Proof:** The induction proof is transcribed immediately below.
>
> **Intuition:** The actual survival probability dominates every bounded harmonic candidate for survival.

Let $Z_{i}$ be any bounded solution of the system (3.42), with $|Z_{i}|\leq 1$. Then:

$$
|Z_{i}|\leq Y_{i}=\lim_{n\to\infty}Y_{i}(n)
$$

In other words, $Y_{i}$ is the largest between all possible bounded solutions of (3.42):

$$
Y_{i}=\underset{\boldsymbol{Z}\text{ solution of }\eqref{2.42}}{\max}Z_{i}
$$


Again we proceed by induction. At the beginning we have that:

$$
|Z_{i}|=\left|\sum_{j\in S}P_{ij}Z_{j}\right|\underset{(a)}{\leq}\sum_{j\in S}P_{ij}|Z_{j}|\underset{|Z_{i}|\leq 1}{\leq}\sum_{j\in S}P_{ij}=Y_{i}(1)
$$

where in (a) we used the triangular inequality and the fact that probabilities are non-negative: $|P_{ij}|=P_{ij}$.

Now suppose that $|Z_{i}|\leq Y_{i}(n)$ for some $n$. Then, we prove that it holds also for $n+1$:

$$
|Z_{i}|\leq\sum_{j\in S}P_{ij}|Z_{j}|\leq\sum_{j\in S}P_{ij}Y_{j}(n)=Y_{i}(n+1)
$$

Thus:

$$
|Z_{i}|\leq Y_{i}(n)\leq Y_{i}(n+1)\qquad\forall n
$$


As it holds for all $n$, it is valid also in the limit:

$$
|Z_{i}|\leq\lim_{n\to\infty}Y_{i}(n)\equiv Y_{i}
$$

which concludes our proof. ∎

We can now make a step forward and make some considerations about the system (3.42). Since it is homogeneous, there are two obvious solutions: $Z_{i}=0$ $\forall i$ and $Z_{i}=\infty$ $\forall i$. But if we can find a solution $|Z_{i}|$ that is both bounded and nonzero, then since $Y_{i}$ is the maximal solution it must be non zero, too:

$$
0<|Z_{i}|\leq Y_{i}\Rightarrow Y_{i}>0
$$

Conversely, if the only bounded solution $Z_{i}$ that the system (3.42) has is the zero one, then $Y_{i}=0$ must be zero, because of (3.43).

Before proceeding, we need two more results. The first one is a recurrence criterion for irreducible Markov chain:

### Lemma 3.7.3.

> [!Important] Lemma 3.7.3 - Recurrence Criterion Through State 0
> **Statement:** An irreducible Markov chain with state space $\mathbb{N}$ is recurrent if and only if every state reaches state $0$ with probability one.
>
> $$
> f_{i0}=\sum_{n=1}^{\infty}f_{i0}^{(n)}=1\qquad\forall i\neq 0
> $$
>
> **Proof:** The necessity and sufficiency proof is transcribed immediately below.
>
> **Intuition:** In an irreducible chain, recurrence of one reference state is equivalent to eventual return communication from every other state.

An irreducible Markov chain with state space $\mathbb{N}$ is recurrent if and only if:

$$
f_{i0}=\sum_{n=1}^{\infty}f_{i0}^{(n)}=1\qquad\forall i\neq 0
$$

$f_{i0}^{(n)}$ is the probability of a system starting at state $i$ and reaching state $0$ for the first time at the $n$-th step. Then, summing over all possible $n$ leads to the probability of visiting $0$ at any time from state $i$. Thus, $f_{i0}=1$ means that the system will certainly visit state $0$ in the future.


We proceed in two steps:

1. Necessity ($\Leftarrow$). Assuming that $f_{i0}=1$ $\forall i\neq 0$, then the probability of returning to the state $0$ given the fact we started from $i$ is given by first step analysis:

$$
f_{00}=P_{00}+\sum_{i\neq 0}P_{0i}f_{i0}
$$

Since all $f_{i0}=1$ $\forall i\neq 0$, this becomes:

$$
f_{00}=P_{00}+\sum_{i\neq 0}P_{0i}=\sum_{i}P_{0i}=1
$$

by normalization. Thus the probability of starting at $0$ and returning to $0$ is unity, meaning that state $0$ is recurrent (and so all other states, because the chain is irreducible).
2. Sufficiency ($\Rightarrow$). Formally, proving $A\Rightarrow B$ is equivalent to proving $\neg B\Rightarrow\neg A$. Hence, we want to prove that if (3.44) is false, then the MC is non-recurrent.


So, suppose that $f_{i0}$ is not 1 for all $i\neq 0$, meaning that there exists some $i\neq 0$ such that $f_{i0}<1$. This means that, if the system starts at $i$, then it is not certain that it will ever visit 0. The idea is then to note that there is a non-zero probability of going from 0 to $i$, and then never returning back, meaning that $f_{00}<1$, and so 0 (and all the other states) are non-recurrent.

In fact, as the MC is irreducible, all states communicate, and so there is a way to go from 0 to $i$ given a sufficient number $m$ of steps: $\exists m$ s.t. $P^{(m)}_{0i}>0$. Let $n$ be the minimum number of steps required to travel from 0 to $i$, i.e.:

$$
n=\min_{m>0}\left\{P^{(m)}_{0i}>0\right\}
$$

Consider one of these “optimal paths” $A=(a_{1},\ldots,a_{n})$, with $a_{1}=0$ and $a_{n}=i$. $A$ cannot reach 0 in any intermediate step: $a_{j}\neq 0$ $\forall j\neq n$. If it were so, then it would clearly exist a path connecting $0\rightarrow i$ in $j<n$ steps, but $n$ is already the minimum number of steps for such a path.

Then, an event where the system never returns to 0 is one where it first goes from $0\rightarrow i$ in $n$ steps, and then never goes back to 0. The probability of such an event is the product of the probability $P^{(n)}_{0i}$ of getting to $i$ in $n$ steps, and $(1-f_{i0})$ - and it is nonzero. Clearly, there could be many other events where the chain never returns to 0 - so the full probability of not returning, i.e. $1-f_{00}$, must be greater than that product:

$$
1-f_{00}\geq P^{(n)}_{0i}(1-f_{i0})>0\Rightarrow f_{00}<1
$$

Thus 0 is non-recurrent, and so are all other states.

∎

We are now ready to prove the transience criterion we are interested in:


An irreducible Markov chain with state space $\mathbb{N}=\{0,1,2,\ldots\}$ has all transient states if and only if the system of equations:

$$
Z_{i}=\sum_{j=1}^{\infty}P_{ij}Z_{j}\qquad i=1,2,\ldots
$$

has a nonzero bounded solution.

Note that the just stated system and (3.42) are the same, they only differ by the sum that starts from $j=1$ and by the equation for $i=0$, that is not included in the statement of the theorem.


Let $S$ be the set of all states $1,2,\ldots$ (all except 0). Then $Y_{i}$, i.e. the probability of not leaving $S$, is just the probability that starting from $i$ we never reach state 0, i.e. $1-f_{i0}$:

$$
Y_{i}=1-f_{i0}
$$


![[Stochastic_Processes_2020_p112_img31.jpeg]]
*Figure 3.11 - Markov chain for exercise 3.7.1*

Now, since we have supposed there exists a nonzero bounded solution, using the result provided by lemma 3.7.2, we know that  $Y_{i}$  must be at least greater or equal than that particular solution, and so  $Y_{i} > 0$  for some  $i$ , meaning that  $1 - f_{i0} > 0 \Rightarrow f_{i0} < 1$ , which implies that state 0 is transient through lemma 3.7.3.

Conversely, if the only bounded solution of the system (3.45) is given by  $Y_{i} = 0 \forall i$ , then  $Y_{i} = 1 - f_{i0} = 0 \Rightarrow f_{i0} = 1 \forall i$ , meaning (lemma 3.7.3) that the chain is recurrent, thus concluding our proof.


An urn contains five red and three green balls. The balls are chosen at random, one by one, from the urn. If a red ball is chosen it is removed. Any green ball that is chosen is returned to the urn. This selection process continues until all of the red balls have been removed from the urn. What is the mean duration of the game?

Let  $X_{n}$  is the Markov process that refers to the number of red balls we have at time step  $n$ . Its transition matrix is:

![[Stochastic_Processes_2020_p112_img32.jpeg]]
*Figure 3.11b - Transition matrix for the urn process, where the state is the number of red balls remaining before absorption at 0.*

Clearly by "duration of the game" we are asked to compute  $\nu_{5}$ : the mean absorption time starting from state 5, since the game ends when there are no more red balls. We then write the system of equations using first step analysis, in order to try to compute it recursively. The first term will be:

$$
\nu_ {5} = 1 + \frac {3}{8} \nu_ {5} + \frac {5}{8} \nu_ {4} \Longrightarrow \nu_ {5} = \frac {8}{5} + \nu_ {4} \tag {3.46}
$$

and, in general:

$$
\nu_ {i} = 1 + a _ {i} \nu_ {i} + (1 - a _ {i}) \nu_ {i - 1}
$$


where we can see from 3.46 that for  $i = 5$  we have  $a_5 = \frac{3}{8}$ . While, taking a look at the transition matrix we have that for  $i = 4$ $a_4 = \frac{4}{7}$ , for  $i = 3$ $a_3 = \frac{1}{2}$  and so on, until  $i = 0$  where  $a_0 = 1$ . As before, we write the last equation recursively:

$$
(1 - a _ {i}) \nu_ {i} = 1 + (1 - a _ {i}) \nu_ {i - 1} \Longrightarrow v _ {i} = \frac {1}{1 - a _ {i}} + \nu_ {i - 1}
$$

It can be thus solved recursively by substituting each  $a_i$ , and by noticing that  $\frac{1}{1 - a_i}$  returns the inverse of the probability of changing the state to a lower one. Finally we conclude:

$$
\nu_ {5} = \frac {8}{5} + \frac {7}{4} + 2 + \frac {5}{2} + 4 = 1 1. 8 5
$$

Note that the time spent in each state distributes geometrically, and so its average is the inverse of the outgoing probability. Therefore, the average absorption time is nothing more than the sum of the average time spent in each of the states.


You have five fair coins. You toss them all so that they randomly fall heads or tails. Those that fall tails in the first toss you pick up and toss again. You toss again those that show tails after the second toss, and so on, until all show heads. Let  $X$  be the number of coins involved in the last toss.

Find  $\operatorname{Pr}\{X = 1\}$ , that is the probability of having only one coin while tossing for the last time.

Let us start by discussing about our Markov chain. First we note that, since  $X$  is the number of coins that is not heads, the state can not increase but only decrease or remain equal.

In order to compute the probability that we have exactly 1 coin in the last toss, we make 1 an absorbing state. Note that 0 state is an absorbing state as well, since we do not have any more coins to toss. Therefore, being absorbed in 0 means we have never visited in state 1 and so the last toss was involving more than one coin. On the other hand, if we get absorbed in the state 1, our last toss will involve exactly one coin that is the event asked by the problem. Transition matrix for this process is:

|  P = | 0 | 1 | 2 | 3 | 4 | 5  |
| --- | --- | --- | --- | --- | --- | --- |
|   |  1 | 0 | 0 | 0 | 0 | 0  |
|   |  0 | 1 | 0 | 0 | 0 | 0  |
|   |  1/4 | 1/2 | 1/4 | 0 | 0 | 0  |
|   |  1/8 | 3/8 | 3/8 | 1/8 | 0 | 0  |
|   |  1/16 | 4/16 | 6/16 | 4/16 | 1/16 | 0  |
|   |  1/32 | 5/32 | 10/32 | 10/32 | 5/32 | 1/32  |

In order to answer the question of the problem we want, given we started in state 5 i.e. with 5 coins to flip, to compute the probability of getting absorbed


in state 1. This can be obtained again using first step analysis and application of absorption probabilities for the specific state 1, thus solving the following system:

$$
\left\{ \begin{array}{l} u _ {0} = 1 \cdot 0 \\ u _ {1} = 0 u _ {0} + 1 \\ u _ {2} = \frac {1}{4} u _ {0} + \frac {1}{2} u _ {1} + \frac {1}{4} u _ {2} \\ u _ {3} = \frac {1}{8} u _ {0} + \frac {3}{8} u _ {1} + \frac {3}{8} u _ {2} + \frac {1}{8} u _ {3} \\ u _ {4} = \frac {1}{1 6} u _ {0} + \frac {4}{1 6} u _ {1} + \frac {6}{1 6} u _ {2} + \frac {4}{1 6} u _ {3} + \frac {1}{1 6} u _ {4} \\ u _ {5} = \frac {1}{3 2} u _ {0} + \frac {5}{3 2} u _ {1} + \frac {1 0}{3 2} u _ {2} + \frac {1 0}{3 2} u _ {3} + \frac {5}{3 2} u _ {4} + \frac {1}{3 2} u _ {5} \end{array} \right.
$$

and the result we are looking for is:  $u_{5} = 0.7235$ .


A Markov chain  $X_0, X_1, X_2, \ldots$  has the transition probability matrix:

$$
\mathbf {P} = \left. \begin{array}{l l l l} & 0 & 1 & 2 \\ 0 & 0. 3 & 0. 2 & 0. 5 \\ 1 & 0. 5 & 0. 1 & 0. 4 \\ 2 & 0 & 0 & 1 \end{array} \right\|
$$

and is known to start in state  $X_0 = 0$ . Eventually, the process will end up in state 2. What is the probability that when the process moves into state 2, it does from state 1?

Hint: Let  $T = \min \{n \geqslant 0; X_n = 2\}$  and let  $z_i = Pr\{X_{T-1} = 1 | X_0 = i\}$  for  $i = 0, 1$ . We note that  $X_{T-1}$  is the state just prior to absorption.

Establish and solve the first step equations:

$$
z _ {0} = \quad 0. 3 z _ {0} + 0. 2 z _ {1}
z _ {1} = 0. 4 + 0. 5 z _ {0} + 0. 1 z _ {1}
$$

In first equation there is a blank space: it refers to the event where, starting from state 0, we suddenly get absorbed. Therefore the particular event requested by the problem, that is being absorbed in state 2 coming from state 1, does not occur. So it is the probability times 0, that returns 0.

While in the second equation, that refers to state 1, we can be absorbed by state 2 with probability 0.4. But, since it is the event that we want to occur, it is the probability times 1. What is requested by the problem is therefore to compute  $z_0$ .

Another way to solve this problem is the following one. Let us consider the following transition matrix:


where we split the state 2 into two different states: one refers to state 2 but only in the case that we come from state 1, which is denoted by win. It is indeed the event we want! On the other hand the second one refers to the event where we are absorbed by state 2, but coming from state 0, and it is denoted by lose. In the end we want to compute the probability that we end up in the win state, given the fact we started in 0 state. Again we are in the same situation of the exercise 3.7.2. Since there are two absorbing states, we shall continue by using first step analysis, solving the following system of equations:

$$
\begin{cases}
u_{\text{lose}} = 0 \\
u_{\text{win}} = 0u_{\text{lose}} + 1 \\
u_{1} = 0u_{\text{lose}} + 0.4u_{\text{win}} + 0.1u_{1} + 0.5u_{0} \\
u_{0} = 0.5u_{\text{lose}} + 0u_{\text{win}} + 0.2u_{1} + 0.3u_{0}
\end{cases}
$$
thus finally finding that:

$$
z_{0}=u_{0,win}=\frac{8}{53}
$$

### Example 11 - Random Walk with Variable Parameters

> [!Example] Example 11 - Random Walk with Variable Parameters
> **Problem:** Apply the transience criterion to a random walk on $0,1,2,\ldots$ with reflecting boundary at $0$ and variable transition probabilities $p_i,q_i$.
>
> **Approach:** Solve the bounded harmonic system by studying consecutive differences $Z_{i+1}-Z_i$.
>
> **Solution:** The complete worked solution is transcribed below.
>
> **Takeaway:** The random walk classification depends on convergence of products of local odds ratios $q_j/p_j$ and $p_j/q_j$.

Let’s see an application of the transience criterion seen in (3.45, pag. 111). Consider a random walk with states $0,1,2...$ for which:

$$
P_{i,i+1}=p_{i}\quad P_{i,i-1}=q_{i}=1-p_{i}\qquad i=0,1,2...
$$

with reflecting boundary condition $p_{0}=1$. In this case, (3.45) becomes:

$$
Z_{1}=p_{1}Z_{2}, i=1
Z_{i}=p_{i}Z_{i+1}+q_{i}Z_{i-1} i>1
$$

and can be solved recursively.
The idea is to evaluate the difference between consecutive $Z_{i}$. In the first case we have:

$$
Z_{2}-Z_{1}=Z_{2}-p_{1}Z_{2}=\underbrace{Z_{2}}_{Z_{1}/p_{1}}\underbrace{(1-p_{1})}_{(3.48)}\frac{(1-p_{1})}{q_{1}}=\frac{q_{1}}{p_{1}}Z_{1}
$$


For general $i$ we start from (2) instead:

$$
Z_i \underbrace{(p_i + q_i)}_{1} = p_i Z_{i+1} + q_i Z_{i-1}
$$

and rearranging:

$$
q_i (Z_i - Z_{i-1}) = p_i (Z_{i+1} - Z_i) \Rightarrow Z_{i+1} - Z_i = \frac{q_i}{p_i} (Z_i - Z_{i-1}), \quad i > 1
$$

The factor $(Z_i - Z_{i-1})$ in turn can be rewritten in terms of the previous difference:

$$
Z_i - Z_{i-1} = \frac{q_{i-1}}{p_{i-1}} (Z_{i-1} - Z_{i-2})
$$

and so on, until we reach $Z_2 - Z_1$ given by (3.50) leading to a recurrence relation.

Therefore the $Z_{i+1} - Z_i$ can be written as:

$$
Z_{i+1} - Z_i = \left[ \prod_{j=2}^{i} \frac{q_j}{p_j} \right] (Z_2 - Z_1) \underset{(3.50)}{=} Z_1 \prod_{j=1}^{i} \frac{q_j}{p_j} \quad i \geq 1
$$

If we sum over $i$:

$$
\begin{aligned}
\sum_{i=0}^{n} (Z_{i+1} - Z_i) &= (Z_{n+1} - Z_n) + (Z_n - Z_{n-1}) + \dots + (Z_1 - Z_0) \\
&= Z_{n+1} - Z_0 \\
&= Z_1 \sum_{i=0}^{n} \underbrace{\left( \prod_{j=1}^{i} \frac{q_j}{p_j} \right)}_{\rho_i} = Z_1 \sum_{i=0}^{n} \rho_i \tag{3.51}
\end{aligned}
$$

with the convention that $\prod_{i=1}^{0} \equiv 1$, and $\rho_0 \equiv 1$. If this solution is bounded, then by applying theorem 3.7.1 we have proven that all states are transient. The solution (3.51) is bounded only if and only if the sum over $\rho_i$ converges to a finite value:

$$
\lim_{n \to \infty} Z_n < \infty \Leftrightarrow \sum_{i=0}^{\infty} \rho_i < \infty
$$

This, along with the results found in the example 6 in page 86, provides a complete classification of the states in the random walk MC:

1. Positive recurrent if and only if:

$$
\sum_{j=0}^{\infty} \frac{p_0 \cdots p_j}{q_0 \cdots q_{j+1}} < \infty
$$

2. Transient if and only if:

$$
\sum_{j=1}^{\infty} \frac{q_1 \cdots q_j}{p_1 \cdots p_j} < \infty
$$


Note that this condition is essentially the inverse of positive recurrence one, and moreover they are mutually exclusive. In other words one can show that if the condition 1) holds, then the sum in 2) must diverge, and viceversa. It’s thus impossible for both sum to converge, but actually they both can diverge as the case 3) below.
3. Null recurrent if and only if:

$$
\sum_{j=0}^{\infty}\frac{p_{0}\cdots p_{j}}{q_{0}\cdots q_{j+1}}=\infty\vee\sum_{j=1}^{\infty}\frac{q_{1}\cdots q_{j}}{p_{1}\cdots q_{j}}=\infty
$$

this case may happen for example when, for $j\to\infty$, $q_{j}$ and $p_{j}$ either go to zero too slowly or don’t even go zero. This means that both sums may diverge, thus the Markov chain being null recurrent.


We want to proceed classifying the Markov chain M/G/1 system, that we have previously discussed in sec. 2.3. Its transition matrix is the following, recalling that we sample at departure times:

$$
\mathbf{P}=\begin{bmatrix}a_{0}&a_{1}&a_{2}&a_{3}&a_{4}&\cdots\\
a_{0}&a_{1}&a_{2}&a_{3}&a_{4}&\cdots\\
0&a_{0}&a_{1}&a_{2}&a_{3}&\cdots\\
0&0&a_{0}&a_{1}&a_{2}&\cdots\\
0&0&0&a_{0}&a_{1}&\cdots\\
\vdots&\vdots&\vdots&\vdots&\vdots&\ddots\end{bmatrix}
$$

Where each $a_{i}$ is drawn from the distribution of arrivals during the service period. Let $\rho$ be the average of this distribution, i.e. the average number of arrivals during a service time:

$\rho=\sum_{n=0}^{\infty}na_{n}$ (3.53)

This chain has 3 possible classifications according to the value of $\rho$:

1. Positive recurrent if $\rho<1$
2. Null recurrent if $\rho=1$
3. Transient if $\rho>1$

Part 1. Let’s prove that, starting with positive recurrence.

This can be done by solving the stationarity equations:

$\pi_{i}=\sum_{j}P_{ji}\pi_{j}\quad i\geq 0$ (3.54)


f we can find the a set of solutions $\pi_{i}$, then we know that they will be also the limiting distribution and conclude that the chain is *positive recurrent*. Otherwise, if there is no solution, it cannot be positive recurrent.

Equation (3.54) can be rewritten in matrix form as:

$\boldsymbol{\pi}=\boldsymbol{\pi}\mathbf{P}$

meaning that the $i$-th element of $\boldsymbol{\pi}$ is the *scalar product* between the $i$-th column of $\mathbf{P}$ and $\boldsymbol{\pi}$ itself. Given the form of $\mathbf{P}$ in (3.52), this means that $\pi_{0}$ multiplies $a_{i}$, $\pi_{1}$ multiplies $a_{i}$, $\pi_{2}$ multiplies $a_{i-1}$, $\pi_{3}$ multiplies $a_{i-2}$, and so on until we reach the last element in the column different from zero, that is $a_{0}$:

$\pi_{i}=\pi_{0}a_{i}+\sum_{j=1}^{i+1}\pi_{j}a_{i-j+1}\qquad i\geq 0$ (3.55)

The idea to solve this equations is to rewrite them in terms of *probability generating functions* *[2, day 17/04]*. Recall that, for a (discrete) probability mass function with non-negative integer values such as $\{\pi_{j}\}_{j\in\mathbf{\mathcal{N}}}$, the probability generating function is defined by the power expansion:

$\pi(s)\equiv\sum_{j=0}^{+\infty}\pi_{j}s^{j}$ (3.56)

Similarly, the same can be done for $\{a_{i}\}_{i\in\mathbf{\mathcal{N}}}$:

$A(s)\equiv\sum_{i=0}^{+\infty}a_{i}s^{i}$ (3.57)

To rewrite (3.55) in terms of (3.56) and (3.57) we just need to multiply the left and right sides by $s^{i}$, and then sum over $i\in\mathbf{\mathcal{N}}$. We do this one step at a time, starting with the left side:

$\pi_{i}\to\sum_{i=0}^{+\infty}\pi_{i}s^{i}\underset{\eqref{eq:def1}}{=}\pi(s)$ (3.58)

And the first term of the right side:

$\pi_{0}a_{i}\to\sum_{i=0}^{+\infty}\pi_{0}a_{i}s^{i}=\pi_{0}\sum_{i=0}^{+\infty}a_{i}s^{i}\underset{\eqref{eq:def2}}{=}\pi_{0}A(s)$ (3.59)

The remaining term is a *shifted convolution* of $\{\pi_{j}\}$ and $\{a_{i}\}$. First, let’s deal with the *shift* $+1$ in the index of $a_{i}$:

$a_{i+1}\to\sum_{i=0}^{+\infty}a_{i+1}s^{i}\underset{\eqref{eq:def3}}{=}\sum_{i=1}^{+\infty}a_{i}s^{i-1}\underset{\eqref{eq:def4}}{=}\frac{1}{s}\sum_{i=0}^{+\infty}a_{i}s^{i}a_{0}s^{0}\underset{\eqref{eq:def5}}{=}\frac{A(s)-a_{0}}{s}$ (3.60)

where in (a) we shifted the index of summation, and in (b) we added and subtracted the 0-th term, so that we may use (3.57) in the last step.


On the other hand, the transform of a convolution is just the product of the transformed terms:

$$
(\pi * a) _ {i} = \sum_ {j = 0} ^ {i} \pi_ {j} a _ {i - j} \rightarrow \sum_ {i = 0} ^ {+ \infty} \sum_ {j = 0} ^ {i} \pi_ {j} a _ {i - j} s ^ {i} = _ {(a)} \sum_ {i = 0} ^ {+ \infty} a _ {i} s ^ {i} \sum_ {j = 0} ^ {+ \infty} \pi_ {j} s ^ {j} = A (s) \pi (s) \tag {3.61}
$$

This can be thought in analogy with the convolution theorem for Fourier transforms (which are just a particular type of power series transform). Explicitly, the equivalence (a) can be shown as just a matter of rearranging addends. Consider the sum:

$$
A (s) \pi (s) = \sum_ {i = 0} ^ {+ \infty} a _ {i} s ^ {i} \sum_ {j = 0} ^ {+ \infty} \pi_ {j} s ^ {j} = \sum_ {j = 0} ^ {+ \infty} \pi_ {j} \left(\sum_ {i = 0} ^ {+ \infty} a _ {i} s ^ {i + j}\right) \tag {3.62}
$$

Graphically, we can write each term with index  $j$  and  $i$  as the entry  $(j,i)$  of a  $\infty \times \infty$  matrix:

$$
\begin{array}{c c c c} \pi_ {0} a _ {0} & \pi_ {0} a _ {1} s & \pi_ {0} a _ {2} s ^ {2} & \dots \\ \pi_ {1} a _ {0} s & \pi_ {1} a _ {1} s ^ {2} & \pi_ {1} a _ {2} s ^ {3} & \dots \\ \pi_ {2} a _ {0} s ^ {2} & \pi_ {2} a _ {1} s ^ {3} & \pi_ {3} a _ {2} s ^ {4} & \dots \\ \vdots & \vdots & \vdots & \ddots \end{array} \tag {3.63}
$$

Assuming (3.62) converges, the result will not change if we vary the order of summation. As (3.62) is currently written, we are first summing over all the  $i$ -th row elements, multiplying the result by  $\pi_i$ , then repeating for each row and summing again. Alternatively, we could first sum over elements with the same power of  $s$ , i.e. the ones on the (highlighted) diagonals of (3.63):

$$
\begin{array}{l} A (s) \pi (s) = \pi_ {0} a _ {0} s ^ {0} + (\pi_ {0} a _ {1} + \pi_ {1} a _ {0}) s ^ {1} + (\pi_ {0} a _ {2} + \pi_ {1} a _ {1} + \pi_ {2} a _ {0}) s ^ {2} + \dots = \\ = \pi_ {0} a _ {0 - 0} s ^ {0} + (\pi_ {0} a _ {1 - 0} + \pi_ {1} a _ {1 - 1}) s ^ {1} + (\pi_ {0} a _ {2 - 0} + \pi_ {1} a _ {2 - 1} + \pi_ {2} a _ {2 - 2}) s ^ {2} + \dots = \\ = \sum_ {i = 0} ^ {+ \infty} s ^ {i} \left(\sum_ {j = 0} ^ {i} \pi_ {j} a _ {i - j}\right) = \sum_ {i = 0} ^ {+ \infty} \sum_ {j = 0} ^ {i} \pi_ {j} a _ {i - j} s ^ {i} \\ \end{array}
$$

This is called the Cauchy product of two infinite sequences. Note that the argument works only in the infinite case, as there the size of diagonals grows indefinitely. In the finite case, the diagonals grow in size until the main diagonal is reached, and then shrink, meaning that the equivalence (3.61) needs to be corrected.

We can then put together (3.60) and (3.61), obtaining the transform for a shifted convolution. First, denote for simplicity:

$$
\sum_ {j = 0} ^ {i} \pi_ {j} a _ {i - j} \equiv \mathcal {A} _ {i}
$$


Then the transform of $\mathcal{A}_{i+1}$ is:

$$
\sum_{j=0}^{i+1} \pi_j a_{i-j+1} \equiv \mathcal{A}_{i+1} \rightarrow \sum_{i=0}^{+\infty} \mathcal{A}_{i+1} = \frac{\sum_{i=0}^{+\infty} \mathcal{A}_i s^i - \mathcal{A}_0}{s} = \frac{\sum_{i=0}^{+\infty} \sum_{j=0}^{i} \pi_j a_{i-j} - \pi_0 a_0}{s} = \frac{A(s) \pi(s) - \pi_0 a_0}{s} \tag{3.64}
$$

This is close to the transform of the rightmost term in (3.55), with the only difference that the sum in (3.64) starts at 0 and not at 1 as in (3.55). This can be solved by just removing the 0-th "excess" term:

$$
\sum_{i=0}^{+\infty} \sum_{j=1}^{i+1} \pi_j a_{i-j+1} = \underbrace{\sum_{i=0}^{+\infty} \sum_{j=0}^{i+1} \pi_j a_{i-j+1}}_{(3.64)} - \underbrace{\sum_{i=0}^{+\infty} \pi_0 a_{i+1}}_{\pi_0 \cdot (3.60)} = \frac{A(s) \pi(s) - \pi_0 a_0}{s} - \pi_0 \frac{A(s) - a_0}{s} = \frac{A(s) \pi(s) - \pi_0 A(s)}{s} \tag{3.65}
$$

And so (3.65) is finally the transform of the rightmost term in (3.55).

Putting (3.58), (3.59) and (3.65) together, we get the full transform of (3.55):

$$
\pi(s) = \pi_0 A(s) + \frac{A(s) \pi(s) - \pi_0 A(s)}{s} \tag{3.66}
$$

Supposing the distribution of arrivals is known, $A(s)$ is known. By rearranging we can then find $\pi(s)$:

$$
\pi(s) = \pi_0 \frac{(s-1) A(s)}{s - A(s)} \tag{3.67}
$$

$\pi_0$ is a constant factor that can be determined by normalization, noting that:

$$
\pi(s = 1) = \left. \sum_{i=0}^{+\infty} \pi_i s^i \right|_{s=1} = \sum_{i=0}^{+\infty} \pi_i \stackrel{!}{=} 1
$$

And the same clearly holds for $A(s)$. Then:

$$
\lim_{s \to 1^-} \pi(s) = \lim_{s \to 1^-} \pi_0 \frac{(s-1) A(s)}{s - A(s)} = \pi_0 \left( \lim_{s \to 1^-} \frac{s-1}{s - A(s)} \right) \underbrace{\left( \lim_{s \to 1^-} A(s) \right)}_{1} = \pi_0 \lim_{s \to 1^-} \left( 1 - \frac{1 - A(s)}{1 - s} \right)^{-1} = \pi_0 \left[ 1 - A'(1) \right]^{-1} = \frac{\pi_0}{1 - \rho} \stackrel{!}{=} 1
$$

Where in (a) we used the moment generating property of $A(s)$:

$$
\left. \frac{\mathrm{d}}{\mathrm{d}s} A(s) \right|_{s=1} = \left. \frac{\mathrm{d}}{\mathrm{d}s} \sum_{i=0}^{+\infty} a_i s^i \right|_{s=1} = \left. \sum_{i=1}^{+\infty} i a_i s^{i-1} \right|_{s=1} = \sum_{i=0}^{+\infty} i a_i = \mathbb{E}[\{a_i\}] \equiv \tag{3.53}
$$


If $\rho < 1$, then $\pi_0 = 1 - \rho$ is an acceptable solution, and can be inserted in (3.67) to find $\pi(s)$, which can then be anti-transformed (either analytically or numerically) to find $\{\pi_j\}$. Clearly, the result will depend on the specific choice of $\{a_i\}$, and so we cannot go further without making more assumptions.

In summary, we distinguish between three cases according to the value of $\rho$:

- $\rho < 1$: our solution is acceptable
- $\rho = 1$: we do not find a nonzero solution because all $\pi_0 = 0$
- $\rho > 1$: it would be meaningless since $\pi_0 < 0$

So, we have just shown that the only case where we can find a solution for the stationary equation is when $\rho < 1$, thus making the chain positive recurrent. If the condition on $\rho < 1$ does not hold, a similar procedure can show that the chain can not be positive recurrent.

**Part 2.** Now let us continue by considering the question of transience.

We want then to seek a bounded solution to the equations (3.45), that considering the specific transition matrix $\mathbf{P}$ (3.52) take the form:

$$
Z_1 = \sum_{j=1}^{\infty} a_j Z_j \tag{3.68}
Z_i = \sum_{j=0}^{\infty} a_j Z_{i+j-1} \quad i > 1 \tag{3.69}
$$

Note that we are ignoring the 0-th row of the matrix because the sum in the system (3.45) starts from 1. So in the first equation (3.68) we consider $Z_1$, that is the product between the first row of the matrix $\mathbf{P}$ and the vector $\mathbf{Z}$, and the form of (3.69) follows by using almost the same argument.

To find a solution, we consider the ansatz $Z_i = 1 - s^i$. The first equation (3.68) becomes:

$$
\begin{aligned}
i = 1: & 1 - s = \sum_{j=1}^{+\infty} a_j (1 - s^j) = \Big( \underbrace{\sum_{j=0}^{+\infty} a_j}_{1} - a_0 \Big) - \Big( \underbrace{\sum_{j=0}^{+\infty} a_j s^j}_{A(s)} - a_0 \Big) = \\
& = 1 - g_0 \cdot A(s) + g_0 = 1 - A(s) \Rightarrow s = A(s)
\end{aligned}
$$

And similarly for (3.69) we have:

$$
i > 1: \qquad 1 - s^i = \sum_{j=0}^{+\infty} a_j (1 - s^{i+j-1}) = 1 - s^{i-1} A(s) \Rightarrow s = A(s)
$$

Both equations take an unique form:

$$
s = A(s) \tag{3.70}
$$

which we have already studied before in the example (8) at page 92.


We want our solution $Z_{i}=1-s^{i}$ not to be zero, so we need to find a value of $s<1$ that solves (3.70), thus proving that the chain is transient. So we need to study (3.70) and find the intersection between the two curves shown in fig. 3.12.

In the graph we exploit the fact that we have already met $A(s)=\mathbb{E}[s^{x}]$ in the example mentioned above - and in particular we know that $A(s)$ in the interval $s\in[0,1]$ has a value strictly greater than zero, it is *increasing* and *convex*, and lastly $A(1)=1$. A intersection is then present if and only if $A^{\prime}(1)=\rho>1$ holds, meaning that $A(s)$ reaches $1$ “from below”.

This proves that, for $\rho>1$, (3.70) can be solved, and thus the MC is transient due to theorem 3.7.1. However, this is just a sufficient condition, as we are merely consider *one possible way* to solve (3.69) - i.e. one in the form of $Z_{i}=1-s^{i}$ - which we have not proven to be the only possible one. So, if $\rho\leq 1$, the fact that (3.70) has no bounded solution just tells us that the ansatz we made is not valid, with no consequences for the characterization of the MC.

Part 3. In summary, we have demonstrated that if $\rho<1$ then the chain is *positive recurrent*, while if $\rho>1$ the chain is *transient*. Now we want to study the last case, where $\rho=1$.

For $\rho=1$ our chain can either be transient or null recurrent. In order to find which, we will now introduce a new criterion for *recurrence*.


Recurrence criterion. Consider the following set of inequalities:

$Z_{i}\geq\sum_{j=0}^{+\infty}P_{ij}Z_{j}\quad i\geq 1$ (3.71)

If we are able to find a solution $Z_{i}$ for (3.71) that diverges $Z_{i}\overset{i\to\infty}{\to}\infty$ then the Markov chain is recurrent (either positive or null).


Omitted. ∎

In our case, (3.71) becomes:

$Z_{i}\geq\sum_{j=0}^{+\infty}P_{ij}Z_{j}=a_{0}Z_{i-1}+a_{1}Z_{i}+a_{2}Z_{i+1}+...=\sum_{j=0}^{+\infty}a_{j}Z_{i+j-1}\quad i\geq 1$

Let us try an obviously divergent solution $Z_{i}=i$:

$i\geq\sum_{j=0}^{+\infty}a_{j}(i+j-1)=i\underbrace{\sum_{j=0}^{+\infty}a_{j}}_{1}+\underbrace{\sum_{j=0}^{+\infty}ja_{j}}_{\rho}-1=i+\rho-1$

The inequality is thus satisfied for all $i\geq 1$ when $\rho\leq 1$, thus concluding that the Markov chain is recurrent thanks to the just introduced criterion.

Now recalling that the MC is:

- Positive recurrent $\Leftrightarrow\rho<1$


![[Stochastic_Processes_2020_p123_img33.jpeg]]
*Figure 3.12 - We need to find the solution of equation 3.70 by drawing the two curves. It is indeed a plot we have already seen before.*

- Transient if  $\rho > 1$

We have that for  $\rho = 1$  the Markov chain can not be positive recurrent, but still is recurrent because of the result we have just found, and so it must be null recurrent.


We want now to provide the solution to the example (10) at page 102 assigned last lecture. We recall its transition matrix:

$$
\mathbf {P} = \left| \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ a & b & c & 1 - a - b - c \\ 0 & 0 & 0 & 0 \end{array} \right|
$$

Solution. We were asked to find under which conditions on  $a, b, c$  it holds that:

$$
\lim _ {n \to \infty} P [ X _ {2 n} = 0 | X _ {0} = 2 ] = \lim _ {n \to \infty} P [ X _ {2 n + 1} = 0 | X _ {0} = 2 ]
$$

First we set the condition on  $c$ , that must be  $c < 1$ , otherwise the problem would not make sense any more since we are stuck in state 2, and moreover later we would face some mathematical issues.

We start by noting that, given we start in state 2, the only ways we have to end up in state 0 at an even time-step are the following ones. We can either remain in 2 with probability  $c$  for an odd number of time steps and then make the transition to 0 with probability  $a$ , or alternatively stay in 2 for an even number of time steps, make the transition to 1 with probability  $b$ , and finally jump to state 0. These are the only ways we have to end up in state 0 in an even number of time steps, and we have already taken into account that, once we are in the  $\{0,1\}$ , we keep on oscillating between the


two states. Explicitly:

$P[X_{2n}=0|X_{0}=2]=\sum_{i=0}^{n-1}c^{2i+1}a+\sum_{i=0}^{n-1}c^{2i}b=(ac+b)\sum_{i=0}^{n-1}c^{2i}=(ac+b)\frac{1-c^{2n}}{1-c^{2}}$

Where in the last passage we recognized that the sum is a geometric truncated. Note moreover that, in the sums, the time we spent in state 2 before the transition distributes geometrically as we expected.

The second expression indeed requests us to be in state 0 in an odd time. There are essentially two ways in which this can occur, similar to the previous ones. We can spend either an *even* number of steps in 2 and then make the transition to state 1, or alternatively remain in 2 for an *odd* time and then do the transition to 0. In the latter however, note as we sum up to $n$ and not $n-1$ as in the previous cases: this is nevertheless irrelevant since the following step will be to consider the limit. Making it explicitly:

$P[X_{2n+1}=0|X_{0}=2]=\sum_{i=0}^{n-1}c^{2i+1}b+\sum_{i=0}^{n}c^{2i}a=bc\frac{1-c^{2n}}{1-c^{2}}+a\frac{1-c^{2n+2}}{1-c^{2}}$

Computing the limit as $n\to\infty$ for both cases we obtain:

$\lim_{n\to\infty}P_{20}^{(2n)}=\frac{ac+b}{1-c^{2}}\quad\lim_{n\to\infty}P_{20}^{(2n+1)}=\frac{bc+a}{1-c^{2}}$

The two limits are the same, thus making the general limit $\lim_{n\to\infty}P_{20}^{(n)}$ exist, only when the two numerators are equal, so:

$ac+b=bc+a\to b(1-c)=a(1-c)\iff a=b$

This is a reasonable solution: if $a$ and $b$ were different, thus privileging a state against the other, then we would introduce a bias in our statistic wrt to the time the entrance to either state 1 or 0. It would reflect into the fact that the evolution may not be balanced, thus making the relative terms of the matrix oscillate for ever (as in the example (9) just before the one we are considering). In this case, there is nothing we can do to make the two limits of the subsequences converge. But on the other hand, having the same probability of entering either state 0 or state 1, is like considering the average over a period: since the transitions rates are now *uniform*, it will make the two limits converge and finally the general one will exist.
We have just shown that even if we are dealing with classes that show a period, in the case where we start in there, we know we will keep oscillating for ever. Moreover the behaviour of these classes will generally affect also the transition probabilities, in the long run, of entering them starting from a transient states. Nevertheless in some special cases, that are for example when we have a uniform probability to enter either one of the states in the periodic class, the subsequences may converge and the limit may exist.


Now let us consider a slightly more complex Markov chain with the following transition matrix:

$$
\mathbf {P} = \left\| \begin{array}{c c c} \mathbf {Q} & \mathbb {R} _ {1} & \mathbb {R} _ {2} \\ 0 & \mathbb {A} & 0 \\ 0 & 0 & 1 \end{array} \right\|
$$

Where $\mathbf{Q}$ is the transient class, $\mathbb{A}$ is the matrix $\left( \begin{array}{ll}0 & 1\\ 1 & 0 \end{array} \right)$ that has period 2, while $\mathbb{R}_1$ and $\mathbb{R}_2$ are the absorbing classes. We can see as the center block is the periodic block we have seen before.

Try to find the powers of the matrix, in particular even and odd powers and see what the expressions will become for each block. The interesting part is to see under which conditions the $\mathbb{R}_1$ block will not be oscillating any more.

Solution. See (4.7.1) at page 164.

---

## Summary Table

| Concept | Definition / Formula | Conditions / Notes |
|---|---|---|
| **Regular Markov chain** | Finite chain with some $k$ such that $(\mathbf{P}^k)_{ij}>0$ for all $i,j$ | Has a unique limiting distribution independent of the initial state |
| **Limiting distribution** | $\lim_{n\to\infty}P_{ij}^{(n)}=\pi_j$ | For regular chains and positive recurrent aperiodic classes |
| **Stationary distribution** | $\pi_j=\sum_i\pi_iP_{ij}$, $\sum_i\pi_i=1$ | A limiting distribution is stationary; a stationary distribution may exist even when ordinary limits do not |
| **Accessibility** | $j$ is accessible from $i$ if $P_{ij}^{(n)}>0$ for some $n\geq 0$ | Formalizes reachability between states |
| **Communication** | $i\leftrightarrow j$ if $i$ and $j$ are mutually accessible | Equivalence relation; partitions states into classes |
| **Irreducible chain** | All states communicate with each other | The entire state space is one class |
| **Period** | $d(i)=\gcd\{n\geq 1:P_{ii}^{(n)}>0\}$ | Period is a class property |
| **Aperiodic state/class** | $d(i)=1$ | Needed for ordinary limiting probabilities in recurrent classes |
| **First return probability** | $f_{ii}^{(n)}=\mathbb{P}\{\theta_{ii}=n\}$ | Distribution of the first return time to state $i$ |
| **Recurrent state** | $f_{ii}=\sum_{n=1}^{\infty}f_{ii}^{(n)}=1$ | The chain returns to $i$ with probability one |
| **Transient state** | $f_{ii}<1$ | Expected number of returns is $f_{ii}/(1-f_{ii})<\infty$ |
| **Recurrence criterion** | $i$ recurrent iff $\sum_{n=1}^{\infty}P_{ii}^{(n)}=\infty$ | Transient iff the same sum is finite |
| **Mean return time** | $m_i=\sum_{n=1}^{\infty}n f_{ii}^{(n)}$ | May be finite or infinite even for recurrent states |
| **Positive recurrent state** | $m_i<\infty$ | Long-run probability $\pi_i=1/m_i>0$ |
| **Null recurrent state** | $f_{ii}=1$ and $m_i=\infty$ | Returns occur with probability one, but mean return time is infinite |
| **Basic Limit Theorem** | $\lim_{n\to\infty}P_{ji}^{(n)}=\pi_i=1/m_i$ | Recurrent, irreducible, aperiodic chains/classes |
| **Periodic generalization** | $\lim_{n\to\infty}\frac{1}{n}\sum_{m=0}^{n-1}P_{ii}^{(m)}=\pi_i=1/m_i$ | Cesaro averages handle periodic oscillation |
| **Absorption probability** | $\pi_i(C)=\sum_{n=1}^{\infty}\pi_i^{(n)}(C)$ | Probability that transient state $i$ eventually enters recurrent class $C$ |
| **Transient to recurrent limit** | $\lim_{n\to\infty}P_{ij}^{(n)}=\pi_i(C)\pi_j$ | $i$ transient, $j\in C$, and $C$ aperiodic recurrent |
| **Finite-state chain fact** | At least one positive recurrent state; no null recurrent states | Null recurrence requires an infinite state space |
| **Survival probability** | $Y_i(n)=\mathbb{P}\{X_j\in S,\ j=1,\ldots,n\mid X_0=i\}$ | Used for transience criteria through bounded solutions |
| **Transience criterion** | $Z_i=\sum_{j=1}^{\infty}P_{ij}Z_j$ has a nonzero bounded solution | For irreducible chains on $\mathbb{N}$ |
| **Random walk classification** | Products of $p_j/q_j$ and $q_j/p_j$ determine recurrence type | Positive recurrent, transient, or null recurrent depending on convergence |
| **M/G/1 classification** | Positive recurrent if $\rho<1$, null recurrent if $\rho=1$, transient if $\rho>1$ | $\rho=\sum_{n=0}^{\infty}na_n$ is the mean number of arrivals during service |
