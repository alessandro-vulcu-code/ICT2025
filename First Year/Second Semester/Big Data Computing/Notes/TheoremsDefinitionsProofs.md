# Theorems, Definitions, and Proofs - Big Data Computing

This file aggregates definitions, theorem statements, lemmas, guarantees, and proof
ideas from the course notes in `Notes/`.

Scope:
- Included sources: numbered lecture notes and `BDC_proofs.md`.
- Excluded source: `ExamStyleQuestions.md`, because it contains generated questions.
- Duplicate proofs from `BDC_proofs.md` are consolidated with the corresponding lecture topic.
- Obsidian image embeds are preserved when they support a definition, construction, or proof.

## 1. MapReduce

Sources: `Notes/1.MapReduce2526.md`, `Notes/BDC_proofs.md`.

### Mean Time Between Failures

Consider a system with $N$ independent components $C_1,\ldots,C_N$. At each time step,
component $C_i$ fails with probability $p$.

The probability that at least one component fails at time $t$ is:

$$
\Pr(\exists C_i \text{ that fails at time } t) = 1-(1-p)^N.
$$

Let $X$ be the number of time units before the next failure. Then $X$ is geometric with
success probability $1-(1-p)^N$, hence:

$$
E[X] = \frac{1}{1-(1-p)^N}.
$$

As $N$ grows, $1-(1-p)^N$ tends to 1, so $E[X]$ tends to 1. For large systems,
failures become frequent, so fault tolerance is required.

### Definition - MapReduce Round

![[Pics/MapReduce/Mapreduce--005.jpg]]

A MapReduce computation is a sequence of rounds. One round transforms a set of
key-value pairs into another set of key-value pairs through:

1. Map phase: for each input pair separately, the map function outputs zero or more
   intermediate pairs.
2. Shuffle: intermediate pairs are grouped by key.
3. Reduce phase: for each key $k$, the reduce function is applied to $(k,L_k)$ and
   outputs zero or more pairs.

One invocation of the reduce function on $(k,L_k)$ is called a reducer.

Keys have two roles:
- addresses for objects;
- labels for groups processed in reduce phases.

### Definition - MapReduce Performance Indicators

For a MapReduce algorithm:

- $R$: number of rounds.
- $M_L$: maximum local memory used by one map or reduce invocation.
- $M_A$: maximum aggregate disk space occupied at the beginning or end of a phase.

Design goals:

1. $R=O(1)$.
2. $M_L=O(|input|^\epsilon)$ for $\epsilon<1$.
3. $M_A=O(|input|)$.
4. Low complexity per map/reduce invocation.

### Deterministic Partitioning Bound

Partition $N$ input pairs into $\ell$ reducers using key $i \bmod \ell$.
If the partition is balanced, each first-round reducer receives $O(N/\ell)$ pairs.
A second aggregation over $\ell$ partial results may require $O(\ell)$ local space.
Thus:

$$
M_L = O\left(\frac{N}{\ell}+\ell\right).
$$

Choosing $\ell=\sqrt{N}$ gives:

$$
M_L=O(\sqrt{N}).
$$

### Theorem - Balanced Random Partitioning

Let $N$ pairs be assigned independently and uniformly to $\ell=\sqrt{N}$ partitions.
Let $m$ be the maximum partition size. Then with probability at least $1-1/N^5$:

$$
m=O(\sqrt{N}).
$$

Therefore random partitioning gives:

$$
M_L=O(\sqrt{N})
$$

with high probability.

![[Pics/MapReduce/Mapreduce--013.jpg]]

#### Proof

Fix one partition $x$. For each pair $i$, define:

$$
Y_i =
\begin{cases}
1 & \text{if pair } i \text{ is assigned to partition } x,\\
0 & \text{otherwise.}
\end{cases}
$$

Then $Y_i$ is Bernoulli with:

$$
\Pr(Y_i=1)=\frac{1}{\sqrt{N}}.
$$

The load of partition $x$ is:

$$
m_x=\sum_{i=0}^{N-1}Y_i.
$$

Thus:

$$
m_x \sim \mathrm{Binom}\left(N,\frac{1}{\sqrt{N}}\right),
\qquad E[m_x]=\sqrt{N}.
$$

By Chernoff, for a sufficiently large constant, for example 6:

$$
\Pr(m_x\geq 6\sqrt{N}) \leq 2^{-6\sqrt{N}}.
$$

For $N\geq 16$, $\sqrt{N}\geq \log_2 N$, so:

$$
2^{-6\sqrt{N}} \leq 2^{-6\log_2 N} = \frac{1}{N^6}.
$$

Let $E_x$ be the event that partition $x$ has load at least $6\sqrt{N}$.
There are $\sqrt{N}$ partitions. By union bound:

$$
\Pr(m\geq 6\sqrt{N})
= \Pr\left(\bigcup_x E_x\right)
\leq \sqrt{N}\cdot \frac{1}{N^6}
\leq \frac{1}{N^5}.
$$

Hence:

$$
\Pr(m<6\sqrt{N}) \geq 1-\frac{1}{N^5}.
$$

### Probabilistic Tools

Union bound:

$$
\Pr\left(\bigcup_{i=1}^r E_i\right)\leq \sum_{i=1}^r \Pr(E_i).
$$

Markov's inequality, for nonnegative $X$ and $a>0$:

$$
\Pr(X\geq a)\leq \frac{E[X]}{a}.
$$

Chernoff bound for $X=\sum_i X_i\sim \mathrm{Binom}(n,p)$ and $\mu=np$:

$$
\Pr(X\geq \delta_1\mu)\leq 2^{-\delta_1\mu}
\qquad \text{for } \delta_1\geq 6,
$$

$$
\Pr(X\leq (1-\delta_2)\mu)\leq 2^{-\delta_2^2\mu/2}
\qquad \text{for } \delta_2\in(0,1).
$$

## 2. Spark and Word Count in Spark

Sources: `Notes/2.Spark2526.md`, `Notes/3.WordCountSpark.md`.

### Definition - Resilient Distributed Dataset

![[Pics/Spark/Spark-002.jpg|500]]

An RDD is the fundamental Spark abstraction: a collection of elements of the same
type, partitioned and distributed across machines.

Main properties:

- Created from stable storage or from other RDDs through transformations.
- Immutable.
- Lazy: materialized only when an action is performed.
- Fault tolerant through lineage, the sequence of transformations used to create it.

### Definition - Narrow and Wide Transformations

![[Pics/Spark/Spark-003.png]]

Narrow transformation: each input partition contributes to at most one output
partition. No shuffle is needed. Example: `map`.

Wide transformation: one input partition may contribute to many output partitions.
Shuffle may be needed. Example: `groupByKey`.

### Definition - Action and Lazy Evaluation

A transformation creates a new RDD but does not immediately compute it. An action
returns a value to the application and triggers materialization.

Lazy evaluation affects time measurements: measuring only transformations can miss
most of the actual computation, because computation starts when an action is executed.

### Definition - Persistence

`cache()` is equivalent to `persist(StorageLevel.MEMORY_ONLY)`: partitions are stored
in RAM after first materialization; partitions that do not fit are recomputed.

`persist(StorageLevel.MEMORY_AND_DISK)` stores partitions in RAM when possible and on
disk otherwise.

### Definition - `reduceByKey`

For each key, `reduceByKey(f)` combines all values through a binary function `f`.
The function must be commutative and associative because Spark is free to aggregate in
a tree-like order.

`reduceByKey` first aggregates inside partitions and then across partitions, so it can
behave like a two-round aggregation.

### Local-Space Bound - One-Round Word Count

For $K$ documents, let $N_i$ be the number of words in document $D_i$ and:

$$
N_{\max}=\max_i N_i.
$$

In the map phase, local counts inside one document require $O(N_{\max})$ space.
In the reduce phase, one word may appear in all $K$ documents, so one reducer may
receive $O(K)$ local counts.

Therefore:

$$
M_L=O(N_{\max}+K).
$$

The aggregate space is:

$$
M_A=O(N),
$$

where $N$ is the total number of words.

### Definition and Analysis - Class Count

Class Count input:

$$
(i,(\mathcal{O}_i,\chi_i)),
$$

where $\mathcal{O}_i$ is an object and $\chi_i$ is its class label.

Goal: output, for each class $\chi$, the number of objects with that label.

One-round naive algorithm:

$$
(i,(\mathcal{O}_i,\chi_i)) \mapsto (\chi_i,\mathcal{O}_i).
$$

Reducer:

$$
(\chi,L_\chi)\mapsto(\chi,|L_\chi|).
$$

If all $N$ objects have the same class, one reducer receives $N$ values, so:

$$
M_L=O(N).
$$

Two-round deterministic partitioning with $\ell$ partitions:

Round 1:

$$
(i,(\mathcal{O}_i,\chi_i)) \mapsto (i\bmod \ell,\chi_i).
$$

Each first-round reducer counts labels inside one partition:

$$
(j,L_j)\mapsto \{(\chi,c(j,\chi)):\chi \text{ appears in } L_j\}.
$$

Round 2 sums partial counts:

$$
(\chi,L_\chi)\mapsto
\left(\chi,\sum_{c(j,\chi)\in L_\chi}c(j,\chi)\right).
$$

With balanced partitions:

$$
M_L=O\left(\max\left\{\frac{N}{\ell},\ell\right\}\right).
$$

Choosing $\ell=\sqrt{N}$ gives:

$$
M_L=O(\sqrt{N}),
\qquad M_A=O(N).
$$

## 3. Clustering and Coresets - Part 1

Sources: `Notes/4.Coreset2526-1.md`, `Notes/BDC_proofs.md`.

### Definition - Metric Space

A metric space is an ordered pair $(M,d)$ where $M$ is a set and:

$$
d:M\times M\to \mathbb{R}
$$

satisfies, for all $x,y,z\in M$:

1. $d(x,y)\geq 0$.
2. $d(x,y)=0 \iff x=y$.
3. $d(x,y)=d(y,x)$.
4. $d(x,z)\leq d(x,y)+d(y,z)$.

Triangle inequality:

![[Pics/Coreset1/Pasted image 20260428111303.png]]

$$
d(x,y)-d(y,z)\leq d(x,z)\leq d(x,y)+d(y,z).
$$

If $d(y,z)$ is small, then $y$ and $z$ are almost interchangeable with respect to
their distance from $x$. This is a key coreset intuition.

### Definitions - Common Distances

Minkowski distance of order $r>0$:

$$
d_{L_r}(X,Y)=\left(\sum_i |x_i-y_i|^r\right)^{1/r}.
$$

Special cases:

- $r=1$: Manhattan distance.
- $r=2$: Euclidean distance.
- $r=\infty$: Chebyshev distance.

Angular distance:

$$
d_{\mathrm{angular}}(X,Y)
= \arccos\left(\frac{X\cdot Y}{\|X\|\|Y\|}\right).
$$

Hamming distance for binary vectors:

$$
d_{\mathrm{Hamming}}(X,Y)=|\{i:x_i\neq y_i\}|.
$$

Jaccard distance for sets:

$$
d_{\mathrm{Jaccard}}(S,T)=1-\frac{|S\cap T|}{|S\cup T|}.
$$

### Definition - Combinatorial Optimization Problem

A combinatorial optimization problem is defined by:

- $\mathcal{I}$: set of instances.
- $\mathcal{S}$: set of solutions.
- $\mathcal{S}_i\subseteq \mathcal{S}$: feasible solutions for instance $i$.
- $\Phi:\mathcal{S}\to \mathbb{R}$: objective function.

Goal: find a feasible solution minimizing or maximizing $\Phi$.

### Definition - $c$-Approximation

For $c\geq 1$, algorithm $A$ is a $c$-approximation if it returns a feasible
solution $A(i)$ such that:

For minimization:

$$
\Phi(A(i)) \leq c\cdot \min\{\Phi(s):s\in \mathcal{S}_i\}.
$$

For maximization:

$$
\Phi(A(i)) \geq \frac{1}{c}\cdot \max\{\Phi(s):s\in \mathcal{S}_i\}.
$$

### Definition - $k$-Clustering

A $k$-clustering of $P$ is:

$$
\mathcal{C}=(C_1,\ldots,C_k;S),
$$

where $P=C_1\cup\cdots\cup C_k$ is a partition into disjoint clusters and
$S=\{c_1,\ldots,c_k\}$ is the set of centers.

### Definitions - Center-Based Objectives

For $x\in P$ and $S\subseteq P$:

$$
d(x,S)=\min_{y\in S}d(x,y).
$$

$k$-center:

$$
\Phi_{\mathrm{kcenter}}(P,S)=\max_{x\in P} d(x,S).
$$

$k$-means:

$$
\Phi_{\mathrm{kmeans}}(P,S)=\sum_{x\in P}(d(x,S))^2.
$$

$k$-median:

$$
\Phi_{\mathrm{kmedian}}(P,S)=\sum_{x\in P}d(x,S).
$$

Given $S$, the best partition assigns each point to its closest center.

### Theorem - FFT is a 2-Approximation for $k$-Center

Farthest-First Traversal (FFT) chooses an arbitrary first center and then repeatedly
chooses the point farthest from the current set of centers.

![[Pics/Coreset1/Coreset1-015.jpg]]

Let $S$ be the $k$ centers returned by FFT. Then:

$$
\Phi_{\mathrm{kcenter}}(P,S)
\leq 2\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k).
$$

#### Proof

Let:

$$
S=\{c_1,\ldots,c_k\}
$$

be the centers chosen by FFT, and let $q$ be the point farthest from $S$:

$$
\Phi_{\mathrm{kcenter}}(P,S)=d(q,S).
$$

Consider the $k+1$ points:

$$
\{c_1,\ldots,c_k,q\}.
$$

Claim: every pair among these points has distance at least $d(q,S)$.

If $i<j$, then $c_j$ was chosen as a farthest point from
$\{c_1,\ldots,c_{j-1}\}$, so:

$$
d(c_i,c_j)\geq d(q,S).
$$

Let $S^*=\{c_1^*,\ldots,c_k^*\}$ be an optimal center set, inducing optimal
clusters $C_1^*,\ldots,C_k^*$. Since there are $k+1$ points and $k$ optimal
clusters, by pigeonhole principle two of the points, call them $c_a,c_b$, belong
to the same optimal cluster $C_t^*$.

By triangle inequality:

$$
d(c_a,c_b)
\leq d(c_a,c_t^*)+d(c_b,c_t^*)
\leq 2\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k).
$$

Since every pair in $\{c_1,\ldots,c_k,q\}$ is at distance at least $d(q,S)$:

$$
d(q,S)\leq d(c_a,c_b)
\leq 2\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k).
$$

Thus:

$$
\Phi_{\mathrm{kcenter}}(P,S)
\leq 2\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k).
$$

### Theorem - Space Complexity of MR-FFT

MR-FFT:

1. Partition $P$ into $\ell$ parts $P_1,\ldots,P_\ell$.
2. Run FFT on each $P_i$ to get $T_i$ of size $k$.
3. Let $T=\bigcup_i T_i$.
4. Run FFT on $T$ to get final center set $S$.

![[Pics/Coreset1/Pasted image 20260428112904.png]]

The algorithm can be implemented with:

$$
M_L=O(\sqrt{Nk}), \qquad M_A=O(N).
$$

#### Proof

Round 1 reducer memory is:

$$
O(N/\ell).
$$

Round 2 reducer memory is:

$$
O(\ell k).
$$

Therefore:

$$
M_L=O\left(\max\left\{\frac{N}{\ell},\ell k\right\}\right).
$$

Choose:

$$
\ell=\sqrt{\frac{N}{k}}.
$$

Then:

$$
\frac{N}{\ell}=\ell k=\sqrt{Nk},
$$

so:

$$
M_L=O(\sqrt{Nk}).
$$

Aggregate space is linear because each round stores $O(N)$ total data.

### Lemma - Coreset Quality for MR-FFT

Let $T=\bigcup_{i=1}^{\ell}T_i$ be the coreset built by MR-FFT. For every
$x\in P$:

$$
d(x,T)\leq 2\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k).
$$

#### Proof

Let $x\in P_r$. Let $T_r$ be the $k$ centers obtained by running FFT on $P_r$.
Let $q_r$ be the point of $P_r$ farthest from $T_r$.

Applying the FFT 2-approximation argument to the $k+1$ points
$T_r\cup \{q_r\}$, but comparing them with the optimal clustering of all of $P$,
gives:

$$
d(q_r,T_r)
\leq 2\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k).
$$

Since $q_r$ is the farthest point of $P_r$ from $T_r$:

$$
d(x,T_r)\leq d(q_r,T_r).
$$

Because $T_r\subseteq T$:

$$
d(x,T)\leq d(x,T_r)
\leq 2\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k).
$$

### Theorem - MR-FFT is a 4-Approximation

Let $S$ be the centers returned by MR-FFT. Then:

$$
\Phi_{\mathrm{kcenter}}(P,S)
\leq 4\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k).
$$

![[Pics/Coreset1/Pasted image 20260428112951.png]]

#### Proof

From the coreset quality lemma, for every $x\in P$ there is $y\in T$ such that:

$$
d(x,y)\leq 2\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k).
$$

Since $S=\mathrm{FFT}(T,k)$, the same FFT argument gives, for every $y\in T$:

$$
d(y,S)\leq 2\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k).
$$

For any $x\in P$, choose such a representative $y\in T$ and a closest center
$c\in S$ to $y$. By triangle inequality:

$$
d(x,S)\leq d(x,c)
\leq d(x,y)+d(y,c)
\leq 4\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k).
$$

Thus:

$$
\Phi_{\mathrm{kcenter}}(P,S)
\leq 4\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k).
$$

### Counterexample - Uniform Sampling is Not a $k$-Center Coreset

![[Pics/Coreset1/Pasted image 20260428113024.png]]

Let $k=2$. Suppose $P$ contains a large dense cluster $P_1$ and a small far cluster
$P_2$ of constant size $m=O(1)$.

If $T$ is a uniform random sample of size $\sqrt{Nk}$, then:

$$
\Pr[T \text{ contains a point of } P_2]
\leq \sqrt{Nk}\cdot \frac{m}{N}
\to 0.
$$

With high probability $T$ misses $P_2$. Then any clustering based on $T$ can have
radius comparable to the distance between $P_1$ and $P_2$, while the optimal
2-center solution covers both clusters. The approximation ratio can be arbitrarily
bad.

## 4. Coresets - Part 2

Sources: `Notes/5.Coreset2526-2.md`, `Notes/BDC_proofs.md`.

### Definition - Diameter

![[Pics/Coreset2/Coreset2-000.jpg]]

The diameter of a pointset $P$ in metric space $(M,d)$ is:

$$
\Delta(P)=\max_{x,y\in P} d(x,y).
$$

### Lemma - 2-Approximation of Diameter from One Point

For any arbitrary $x\in P$, define:

$$
\Delta_x=\max_{y\in P} d(x,y).
$$

Then:

$$
\Delta(P)\in [\Delta_x,2\Delta_x].
$$

![[Pics/Coreset2/Pasted image 20260428114521.png]]

#### Proof

Lower bound:

$$
\Delta(P)\geq \Delta_x
$$

because $\Delta(P)$ maximizes over all pairs, while $\Delta_x$ maximizes only over
pairs involving $x$.

Upper bound: let $z,w$ realize the diameter. By triangle inequality:

$$
\Delta(P)=d(z,w)\leq d(z,x)+d(x,w)\leq 2\Delta_x.
$$

### Theorem - Coreset-Based Diameter Bound

Let $T$ be a set of representatives and let:

$$
R=\max_{x\in P}d(x,T).
$$

Let $\Delta(T)$ be the diameter of $T$. Then:

$$
\Delta(T)\leq \Delta(P)\leq \Delta(T)+2R.
$$

![[Pics/Coreset2/Pasted image 20260428130825.png]]

#### Proof

Since $T\subseteq P$:

$$
\Delta(T)\leq \Delta(P).
$$

Let $z,w\in P$ realize $\Delta(P)$, and let $c_z,c_w\in T$ be closest
representatives of $z,w$. Then:

$$
d(z,c_z)\leq R,\qquad d(w,c_w)\leq R.
$$

By triangle inequality:

$$
\Delta(P)=d(z,w)
\leq d(z,c_z)+d(c_z,c_w)+d(c_w,w)
\leq R+\Delta(T)+R.
$$

Thus:

$$
\Delta(P)\leq \Delta(T)+2R.
$$

If $R\leq \epsilon\Delta(T)$, then:

$$
\Delta(P)\leq (1+2\epsilon)\Delta(T).
$$

### Definition - Diversity Maximization

Given $P$ in metric space $(M,d)$ and integer $k<|P|$, find $S\subset P$ with
$|S|=k$ maximizing:

$$
\mathrm{div}(S)=\sum_{x,y\in S}d(x,y).
$$

This is also called max-sum diversity or remote clique.

### Definition - $(1+\epsilon)$-Coreset for Diversity

Let $\epsilon\in(0,1)$. A subset $T\subset P$ is a $(1+\epsilon)$-coreset if:

$$
\mathrm{div}^{\mathrm{opt}}(T,k)
\geq \frac{1}{1+\epsilon}
\mathrm{div}^{\mathrm{opt}}(P,k).
$$

If $T$ is a $(1+\epsilon)$-coreset and $S$ is a $c$-approximation on $T$, then:

$$
\mathrm{div}(S)
\geq \frac{1}{c(1+\epsilon)}
\mathrm{div}^{\mathrm{opt}}(P,k).
$$

### Fact - Relation Between $k$-Center and Diversity

$$
\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k)
\leq
\frac{\mathrm{div}^{\mathrm{opt}}(P,k)}{\binom{k}{2}}.
$$

### Proxy Lemma - Diversity Coreset

Build a coreset by:

1. Extracting $h>k$ centers $W$ by FFT.
2. Assigning $P$ to clusters $C_1,\ldots,C_h$ induced by $W$.
3. Selecting $\min\{k,|C_i|\}$ points from each cluster.

Let $R$ be the radius of the clustering induced by $W$.

For every $x\in S^*$, where $S^*$ is an optimal diversity solution, there exists a
distinct proxy $\tau(x)\in T$ in the same cluster such that:

$$
d(x,\tau(x))\leq 2R.
$$

![[Pics/Coreset2/Pasted image 20260428114730.png]]

#### Proof

In each cluster $C_i$, at most $k$ points of $S^*$ can appear because $|S^*|=k$.
The construction selects at least $\min\{k,|C_i|\}$ points from $C_i$, so each
point of $S^*\cap C_i$ can be assigned to a distinct proxy in $T\cap C_i$.

If $c_i$ is the cluster center, then:

$$
d(x,c_i)\leq R,
\qquad d(\tau(x),c_i)\leq R.
$$

By triangle inequality:

$$
d(x,\tau(x))\leq d(x,c_i)+d(c_i,\tau(x))\leq 2R.
$$

For $x_i,x_j\in S^*$:

$$
d(\tau(x_i),\tau(x_j))
\geq d(x_i,x_j)-d(x_i,\tau(x_i))-d(x_j,\tau(x_j)).
$$

Summing over all pairs shows that diversity is preserved up to a loss depending on
$R$. If $R$ is small enough, $T$ is a good diversity coreset.

### Theorem - Diversity Coreset Quality

If the clustering radius $R$ of the coreset construction satisfies:

$$
R \leq \frac{1}{8}\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k),
$$

then:

$$
\mathrm{div}^{\mathrm{opt}}(T,k)
\geq \frac{1}{2}\mathrm{div}^{\mathrm{opt}}(P,k).
$$

Thus $T$ is a 2-coreset for diversity maximization.

#### Proof Idea

Let $S^*$ be optimal for $P$. Map every $x\in S^*$ to a distinct proxy
$\tau(x)\in T$ in the same cluster. The proxy lemma gives:

$$
d(x,\tau(x))\leq 2R.
$$

For every pair $x_i,x_j\in S^*$:

$$
d(\tau(x_i),\tau(x_j))
\geq
d(x_i,x_j)-4R.
$$

Summing over all $\binom{k}{2}$ pairs:

$$
\mathrm{div}(\tau(S^*))
\geq
\mathrm{div}^{\mathrm{opt}}(P,k)
-4R\binom{k}{2}.
$$

Using:

$$
\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k)
\leq
\frac{\mathrm{div}^{\mathrm{opt}}(P,k)}{\binom{k}{2}},
$$

and the assumption on $R$, the additive loss is at most one half of
$\mathrm{div}^{\mathrm{opt}}(P,k)$. Since $\tau(S^*)\subseteq T$:

$$
\mathrm{div}^{\mathrm{opt}}(T,k)
\geq \mathrm{div}(\tau(S^*))
\geq \frac{1}{2}\mathrm{div}^{\mathrm{opt}}(P,k).
$$

### Guarantee - k-means++

k-means++ is randomized. If $S$ is the returned center set, then:

$$
E[\Phi_{\mathrm{kmeans}}(P,S)]
\leq \alpha \Phi_{\mathrm{kmeans}}^{\mathrm{opt}}(P,k),
\qquad \alpha=\Theta(\ln k).
$$

### Definition - Weighted $k$-Means

Input: pointset $P\subset \mathbb{R}^D$, weights $w(x)>0$, target $k$.

Objective:

$$
\Phi^w_{\mathrm{kmeans}}(P,S)
= \sum_{x\in P} w(x)(d(x,S))^2.
$$

Weighted k-means++ sampling probability:

$$
\pi(x)=
\frac{w(x)(d(x,S))^2}
{\sum_{y\in P-S}w(y)(d(y,S))^2}.
$$

Weighted Lloyd centroid for cluster $C=\{x_1,\ldots,x_t\}$:

$$
\frac{\sum_{i=1}^t w(x_i)x_i}{\sum_{i=1}^t w(x_i)}.
$$

### Definition - $\gamma$-Coreset for $k$-Means

Given $P$, coreset $T\subseteq P$, and proxy function $\tau:P\to T$, $T$ is a
$\gamma$-coreset for $k$-means if:

$$
\sum_{p\in P}(d(p,\tau(p)))^2
\leq
\gamma \Phi_{\mathrm{kmeans}}^{\mathrm{opt}}(P,k).
$$

### Theorem - Approximation Ratio of MR-kmeans

Suppose:

- $\mathcal{A}_1$ is a $\gamma$-approximation for unweighted $k$-means.
- $\mathcal{A}_2$ is an $\alpha$-approximation for weighted $k$-means.

Then:

1. The coreset $T$ computed in Round 1 is a $\gamma$-coreset.
2. The final solution $S$ satisfies:

$$
\Phi_{\mathrm{kmeans}}(P,S)
=O((1+\gamma)\alpha)
\Phi_{\mathrm{kmeans}}^{\mathrm{opt}}(P,k).
$$

The $(1+\gamma)$ factor is coreset loss; the $\alpha$ factor is the loss from
solving weighted $k$-means approximately on $T$.

### Space Bound - MR-kmeans

MR-kmeans has the same local-space structure as MR-FFT:

$$
M_L=O\left(\max\left\{\frac{N}{\ell},\ell k\right\}\right).
$$

Choosing:

$$
\ell=\sqrt{\frac{N}{k}}
$$

gives:

$$
M_L=O(\sqrt{Nk}),
\qquad M_A=O(N).
$$

## 5. Streaming - Part 1

Sources: `Notes/6. Streaming2526-1.md`, `Notes/BDC_proofs.md`.

### Definition - Streaming Model

![[Pics/Streaming/streaming-000.jpg]]

Input is a continuous one-way stream:

$$
\Sigma=x_1,x_2,\ldots,x_n,\ldots
$$

Upon receiving $x_n$:

- Update task: update memory-resident data structures.
- Query task: compute the answer for the prefix seen so far.

Main KPIs:

1. Working memory $s \ll |\Sigma|$.
2. Number of passes $p=1$.
3. Update time $T_u=O(1)$.
4. Query time independent of $n$.

### Definition - Majority Problem

Given stream $\Sigma=x_1,\ldots,x_n$, return an element occurring more than
$n/2$ times, if such an element exists.

### Theorem - Boyer-Moore Correctness

Boyer-Moore returns the true majority element if one exists. It uses:

- $O(1)$ memory;
- one pass, plus one optional verification pass;
- $O(1)$ update and query time.

#### Invariant

After processing $x_1,\ldots,x_t$, the processed prefix can be partitioned into:

- $\mathrm{count}_t$ unmatched occurrences of $\mathrm{cand}_t$;
- $(t-\mathrm{count}_t)/2$ pairs $(e_1,e_2)$ with $e_1\neq e_2$.

#### Proof

Let $m$ be the true majority. Suppose for contradiction that the final candidate is
not $m$.

By the invariant, all elements except unmatched final candidate occurrences are
partitioned into pairs of distinct elements. Each such pair contains at most one
copy of $m$.

If the final candidate is not $m$, then all occurrences of $m$ must lie inside the
canceling pairs. Therefore $m$ occurs at most $n/2$ times, contradicting the
assumption that $m$ is a majority element.

Thus the final candidate must be $m$.

### Definition - $m$-Sample

Given a set $X$ of $n$ elements and $1\leq m<n$, an $m$-sample is a random subset
$S\subset X$ with $|S|=m$ such that:

$$
\forall x\in X,\qquad \Pr(x\in S)=\frac{m}{n}.
$$

### Theorem - Reservoir Sampling Correctness

Reservoir Sampling maintains an $m$-sample of the stream prefix $\Sigma_t$ for every
$t\geq m$.

![[Pics/Streaming/streaming-001.jpg]]

For every $i\in[1,t]$:

$$
\Pr(x_i\in S_t)=\frac{m}{t}.
$$

#### Proof

Induction on $t\geq m$.

Base case $t=m$: all first $m$ elements are in $S$, so:

$$
\Pr(x_i\in S_m)=1=\frac{m}{m}.
$$

Inductive step: assume for $t-1$:

$$
\Pr(x_i\in S_{t-1})=\frac{m}{t-1}.
$$

New item $x_t$ is inserted with probability $m/t$, so:

$$
\Pr(x_t\in S_t)=\frac{m}{t}.
$$

For an old item $x_i$, if $x_t$ is inserted, one uniformly random reservoir item is
evicted. Thus an old item currently in the reservoir is evicted with probability:

$$
\frac{m}{t}\cdot \frac{1}{m}=\frac{1}{t}.
$$

It survives with probability $1-1/t$. Hence:

$$
\Pr(x_i\in S_t)
=\frac{m}{t-1}\left(1-\frac{1}{t}\right)
=\frac{m}{t}.
$$

### Definition - Frequent Items

Given stream $\Sigma$ over universe $U$ and threshold $\varphi\in(0,1)$, return all
items occurring at least $\varphi n$ times.

The number of frequent items is at most $1/\varphi$.

### Definition - $\epsilon$-Approximate Frequent Items

![[Pics/Streaming/streaming-002.png]]

Given threshold $\varphi$ and accuracy $\epsilon\in(0,\varphi)$, return a set that:

- includes all items with frequency at least $\varphi n$;
- contains no item with frequency below $(\varphi-\epsilon)n$.

Items with frequency in $[(\varphi-\epsilon)n,\varphi n)$ are allowed false positives.

### Theorem - Sticky Sampling

Sticky Sampling solves $\epsilon$-AFI with probability at least $1-\delta$ and uses:

$$
O(r)
=O\left(\frac{\ln(1/(\delta\varphi))}{\epsilon}\right)
$$

expected memory, where:

$$
r=\left\lceil \frac{\ln(1/(\delta\varphi))}{\epsilon}\right\rceil.
$$

It uses one pass, $O(1)$ expected update time, and $O(r)$ expected query time.

#### Proof

Memory: each item creates a new entry with probability at most $r/n$. Let $X_t=1$
if item $x_t$ creates a new entry. Then:

$$
|S|=\sum_{t=1}^n X_t,
$$

and:

$$
E[|S|]=\sum_{t=1}^n E[X_t]\leq n\cdot \frac{r}{n}=r.
$$

No deep false positives: an item is returned only if its stored estimate satisfies:

$$
f_e(x)\geq(\varphi-\epsilon)n.
$$

Since $f_e(x)$ is a lower bound on true frequency, no item with true frequency below
$(\varphi-\epsilon)n$ can be returned.

No false negatives with probability at least $1-\delta$: let $a$ be frequent, so
$f_a\geq \varphi n$. If one of the first $\lceil \epsilon n\rceil$ occurrences of
$a$ is sampled, then all later occurrences increment its counter and:

$$
f_e(a)\geq (\varphi-\epsilon)n.
$$

Thus:

$$
\Pr(a \text{ not returned})
\leq \left(1-\frac{r}{n}\right)^{\epsilon n}
\leq e^{-\epsilon r}.
$$

There are at most $1/\varphi$ frequent items. By union bound:

$$
\Pr(\exists \text{ frequent item missed})
\leq \frac{1}{\varphi}e^{-\epsilon r}
\leq \delta.
$$

Therefore all frequent items are returned with probability at least $1-\delta$.

## 6. Streaming - Part 2

Sources: `Notes/7.Streaming2526-2.md`, `Notes/BDC_proofs.md`.

### Definition - Sketch

A sketch is a space-efficient data structure that provides estimates of statistical
characteristics of a stream, typically with probabilistic guarantees.

### Definition - Frequency Moments

For each $u\in U$, define:

$$
f_u=|\{j:x_j=u,\ 1\leq j\leq n\}|.
$$

The $k$-th frequency moment is:

$$
F_k=\sum_{u\in U} f_u^k,
$$

with $0^0=0$.

Special cases:

- $F_0$: number of distinct elements.
- $F_1$: stream length.
- $F_2$: second moment.

Gini index:

$$
1-\frac{F_2}{|\Sigma|^2}.
$$

### Theorem - Probabilistic Counting Guarantee for $F_0$

The Flajolet-Martin probabilistic counting algorithm maintains:

$$
R=\max_t \operatorname{tr}(h(x_t)),
$$

where $\operatorname{tr}$ is number of trailing zeros. It returns:

$$
\tilde{F}_0=2^R.
$$

For any $c>2$:

$$
\Pr(\tilde{F}_0 < F_0/c)\leq 1/c,
\qquad
\Pr(\tilde{F}_0 > cF_0)\leq 1/c.
$$

Therefore:

$$
\Pr(F_0/c\leq \tilde{F}_0\leq cF_0)\geq 1-\frac{2}{c}.
$$

The algorithm uses $O(\log |U|)$ bits.

#### Upper-Tail Proof

For a fixed distinct item:

$$
\Pr(\operatorname{tr}(h(x))\geq j)=\frac{1}{2^j}.
$$

By union bound over the $F_0$ distinct elements:

$$
\Pr(R\geq j)\leq F_0\cdot \frac{1}{2^j}.
$$

Set $j=\log_2(cF_0)$. Then:

$$
\Pr(\tilde{F}_0>cF_0)
=\Pr(2^R>cF_0)
\leq
F_0\cdot \frac{1}{2^{\log_2(cF_0)}}
=\frac{1}{c}.
$$

### Median Trick

Run $\ell$ independent instances and return the median estimate. If one instance has
failure probability at most $1/16$ on one side, then the median is bad only if at
least half of the $\ell$ instances are bad. A Chernoff bound makes this probability
exponentially small in $\ell$. Choosing:

$$
\ell=\Theta(\log |U|)
$$

makes the failure probability at most $1/|U|$.

### Definition - Count-Min Sketch

A count-min sketch uses:

- a $d\times w$ array $C$ of counters;
- hash functions $h_0,\ldots,h_{d-1}:U\to \{0,\ldots,w-1\}$.

Update for stream item $x_t$:

$$
C[j,h_j(x_t)] \leftarrow C[j,h_j(x_t)]+1
\qquad \forall j.
$$

Query for item $u$:

$$
\tilde{f}_u=\min_{0\leq j<d} C[j,h_j(u)].
$$

### Theorem - Count-Min Frequency Accuracy

With:

$$
w=\frac{2}{\epsilon},\qquad d=\log_2(1/\delta),
$$

for any item $u$:

$$
\tilde{f}_u-f_u\leq \epsilon n
$$

with probability at least $1-\delta$.

#### Proof

Fix $u$ and one row $j$. The error is:

$$
C[j,h_j(u)]-f_u.
$$

Expected colliding mass:

$$
E[C[j,h_j(u)]-f_u]
=\sum_{a\neq u} f_a\Pr(h_j(a)=h_j(u))
\leq \frac{n}{w}
=\frac{\epsilon n}{2}.
$$

By Markov:

$$
\Pr(C[j,h_j(u)]-f_u>\epsilon n)\leq \frac{1}{2}.
$$

The final estimator is bad only if every row has error above $\epsilon n$.
By row independence:

$$
\Pr(\tilde{f}_u-f_u>\epsilon n)
\leq \left(\frac{1}{2}\right)^d
=\delta.
$$

### Definition - Count Sketch

Count sketch uses:

- a $d\times w$ counter array $C$;
- hash functions $h_j:U\to \{0,\ldots,w-1\}$;
- sign functions $g_j:U\to \{-1,+1\}$.

Update:

$$
C[j,h_j(x_t)] \leftarrow C[j,h_j(x_t)] + g_j(x_t).
$$

Row estimate:

$$
\tilde{f}_{u,j}=g_j(u)C[j,h_j(u)].
$$

Final estimate:

$$
\tilde{f}_u=\operatorname{median}_j \tilde{f}_{u,j}.
$$

### Theorem - Count Sketch Frequency Accuracy

For:

$$
d=\log_2(1/\delta),
\qquad w=O(1/\epsilon^2),
$$

count sketch satisfies:

$$
E[\tilde{f}_{u,j}]=f_u
$$

for every row $j$, and with probability at least $1-\delta$:

$$
|\tilde{f}_u-f_u|\leq \epsilon\sqrt{F_2}.
$$

#### Proof of Unbiasedness

Fix $u$ and row $j$. For every $a\neq u$, define:

$$
Y_a=
\begin{cases}
f_a & \text{if } h_j(a)=h_j(u) \text{ and } g_j(a)=g_j(u),\\
-f_a & \text{if } h_j(a)=h_j(u) \text{ and } g_j(a)=-g_j(u),\\
0 & \text{otherwise.}
\end{cases}
$$

Then:

$$
\tilde{f}_{u,j}=f_u+\sum_{a\neq u}Y_a.
$$

For each $a\neq u$:

$$
\Pr(Y_a=f_a)=\frac{1}{w}\cdot\frac{1}{2},
\qquad
\Pr(Y_a=-f_a)=\frac{1}{w}\cdot\frac{1}{2}.
$$

Thus:

$$
E[Y_a]=0.
$$

By linearity of expectation:

$$
E[\tilde{f}_{u,j}]
=f_u+\sum_{a\neq u}E[Y_a]
=f_u.
$$

### Theorem - Count Sketch Accuracy for $F_2$

For each row:

$$
\tilde{F}_{2,j}=\sum_{k=0}^{w-1} C[j,k]^2.
$$

Final estimate:

$$
\tilde{F}_2=\operatorname{median}_j \tilde{F}_{2,j}.
$$

Each row estimator is unbiased:

$$
E[\tilde{F}_{2,j}]=F_2.
$$

With probability at least $1-\delta$:

$$
|\tilde{F}_2-F_2|\leq \epsilon\sqrt{F_2}.
$$

#### Proof Hint for Unbiasedness

For $a\neq b$, define signed interaction variables:

$$
Y_{ab}=
\begin{cases}
f_af_b & \text{if } h_j(a)=h_j(b) \text{ and } g_j(a)=g_j(b),\\
-f_af_b & \text{if } h_j(a)=h_j(b) \text{ and } g_j(a)=-g_j(b),\\
0 & \text{otherwise.}
\end{cases}
$$

Then:

$$
\tilde{F}_{2,j}
=\sum_a f_a^2+\sum_{a\neq b}2Y_{ab}.
$$

Since $E[Y_{ab}]=0$, linearity of expectation gives:

$$
E[\tilde{F}_{2,j}]=F_2.
$$

### Definition - Approximate Membership Problem

Given a stream from universe $U$ and a set $S$ of $m$ elements, store $S$ compactly
so queries satisfy:

- no false negatives for $x\in S$;
- small false-positive probability for $x\notin S$.

### Definition - Bloom Filter

A Bloom filter uses:

- an array $A$ of $n$ bits, initialized to 0;
- $k$ hash functions $h_0,\ldots,h_{k-1}:U\to \{0,\ldots,n-1\}$.

Initialization:

$$
A[h_j(e)]\leftarrow 1
\qquad \forall e\in S,\ 0\leq j<k.
$$

Query: claim $x\in S$ iff:

$$
A[h_0(x)]=A[h_1(x)]=\cdots=A[h_{k-1}(x)]=1.
$$

There are no false negatives because every inserted item sets all queried positions
to 1.

### Theorem - Bloom Filter False Positive Rate

For $x\notin S$, under independence assumptions:

$$
\Pr(\text{false positive})\simeq (1-e^{-km/n})^k.
$$

#### Proof

After inserting $m$ items, $km$ positions are sampled uniformly. For a fixed cell
$\ell$:

$$
\Pr(A[\ell]=0)=\left(1-\frac{1}{n}\right)^{km}.
$$

For large $n$:

$$
\left(1-\frac{1}{n}\right)^{km}
=
\left[\left(1-\frac{1}{n}\right)^n\right]^{km/n}
\approx e^{-km/n}.
$$

Thus a queried bit is 1 with probability:

$$
1-e^{-km/n}.
$$

A false positive requires all $k$ queried bits to be 1:

$$
\Pr(\text{false positive})
\approx (1-e^{-km/n})^k.
$$

The false-positive rate is minimized, for fixed $n,m$, by:

$$
k=(\ln 2)\frac{n}{m}.
$$

### Definition - $k$-Universality

A family $\mathcal{H}$ of hash functions from $U$ to $[m]$ is $k$-universal if,
for any $k$ distinct elements $x_1,\ldots,x_k$:

$$
\Pr(h(x_1)=h(x_2)=\cdots=h(x_k))
\leq \frac{1}{m^{k-1}},
$$

where $h$ is chosen uniformly from $\mathcal{H}$.

It is strongly $k$-universal if, for any distinct $x_1,\ldots,x_k$ and any
$y_1,\ldots,y_k\in[m]$:

$$
\Pr((h(x_1)=y_1)\wedge\cdots\wedge(h(x_k)=y_k))
=\frac{1}{m^k}.
$$

### Theorem - Practical 2-Universal Hash Family

Let $U=[u]$, range $[m]$, and let $p>u$ be prime. For:

$$
1\leq a\leq p-1,
\qquad 0\leq b\leq p-1,
$$

define:

$$
h_{a,b}(x)=((ax+b)\bmod p)\bmod m.
$$

The family:

$$
\mathcal{H}_p=\{h_{a,b}:1\leq a\leq p-1,\ 0\leq b\leq p-1\}
$$

is 2-universal.

If $p=2^q-1$ is a Mersenne prime, then:

$$
x\bmod p
=((x\bmod 2^q)+\lfloor x/2^q\rfloor)\bmod p,
$$

so modulo can be implemented with fast bit shifts and additions.

## 7. Similarity Search - Part 1

Source: `Notes/8.SimSearch2526-1.md`.

### Definition - $r$-Near Neighbor Search

For metric space $(M,d)$, query point $q$, and radius $r>0$:

$$
B_r(q)=\{p\in M:d(p,q)\leq r\}.
$$

Given $P\subset M$, construct a data structure that, for query $q$, returns:

- a point $p\in B_r(q)\cap P$ if one exists;
- `null` if $B_r(q)\cap P=\emptyset$.

![[Pics/SimSearch1/SimSearch1-08.png]]

### Definition - Range Reporting

Given $P\subset \mathbb{R}^D$, construct a data structure that, for an axis-aligned
rectangle:

$$
R=[x_{1,1}:x_{1,2}]\times \cdots \times [x_{D,1}:x_{D,2}],
$$

returns all points of $P$ contained in $R$.

![[Pics/SimSearch1/SimSearch1-15.png]]

Range Reporting returns all points in a rectangle. $r$-NNS returns one point in a
metric ball, if one exists.

### Definition - kd-tree

![[Pics/SimSearch1/SimSearch1-18.png]]

For $P\subset \mathbb{R}^2$, a kd-tree is a binary tree defining a hierarchical
decomposition of a rectangle $R(P)$ containing all points.

- Root region is $R(P)$.
- Each internal node $v$ has a rectangular region and represents
  $P_v=P\cap \operatorname{region}(v)$.
- Each leaf contains exactly one point.
- Splits alternate vertical and horizontal lines by depth.

The split line divides $P_v$ into two sets of sizes:

$$
\left\lfloor \frac{|P_v|}{2}\right\rfloor,
\qquad
\left\lceil \frac{|P_v|}{2}\right\rceil.
$$

### Theorem - Range Reporting with kd-trees in $\mathbb{R}^2$

For $P\subset \mathbb{R}^2$ with $|P|=n$, Range Reporting can be solved with:

| Quantity | Bound |
|---|---|
| Construction time | $O(n\log n)$ |
| Space | $O(n)$ |
| Query time | $O(\sqrt{n}+k)$ |

where $k$ is the number of reported points.

![[Pics/SimSearch1/SimSearch1-31.png]]

#### Proof Sketch

Query time is proportional to the number of visited nodes.

Define:

$$
Q_1(R)=
\{v\in T:\operatorname{region}(v)\cap R\neq \emptyset
\text{ and }
\operatorname{region}(v)\not\subset R\},
$$

$$
Q_2(R)=
\{v\in T:\operatorname{region}(v)\cap R\neq \emptyset
\text{ and }
\operatorname{region}(v)\subseteq R\}.
$$

Search visits only nodes in $Q_1(R)\cup Q_2(R)$, except possibly the root.

Known bounds:

$$
|Q_1(R)|=O(\sqrt{n}),
\qquad
|Q_2(R)|=O(k).
$$

Therefore:

$$
T_q=O(1+|Q_1(R)|+|Q_2(R)|)=O(\sqrt{n}+k).
$$

![[Pics/SimSearch1/SimSearch1-32.png]]
![[Pics/SimSearch1/SimSearch1-33.png]]

### Theorem - Range Reporting with kd-trees in $\mathbb{R}^D$

For $P\subset \mathbb{R}^D$:

| Quantity | Bound |
|---|---|
| Construction time | $O(Dn\log n)$ |
| Space | $O(Dn)$ |
| Query time | $O(Dn^{1-1/D}+k)$ |

As $D$ grows, $1-1/D$ approaches 1, so the query cost approaches linear scanning.

### kd-tree Reduction for $r$-NNS

![[Pics/SimSearch1/SimSearch1-36.png]]

To answer an $r$-NNS query in $\mathbb{R}^2$:

1. Let $R_q$ be the smallest square enclosing $B_r(q)$.
2. Run Range Reporting on $R_q$.
3. Return a point in $S\cap B_r(q)$ if one exists; otherwise return `null`.

The query time depends on:

$$
k_s=|S|,
$$

not only on:

$$
k_q=|S\cap B_r(q)|.
$$

## 8. Similarity Search - Part 2

Sources: `Notes/9SimSearch2526-2.md`, `Notes/BDC_proofs.md`.

### Definition - $(c,r)$-Approximate Near Neighbor Search

Given $P\subset M$, construct a data structure that, for query $q$, satisfies:

- If $B_r(q)\cap P\neq\emptyset$, return some $p\in P$ with $d(p,q)\leq cr$.
- If $B_r(q)\cap P=\emptyset$, return either `null` or a point $p$ with
  $d(p,q)\leq cr$.

The structure must never return a point at distance greater than $cr$.

![[Pics/SimSearch2/SimSearch2-05.png]]

### Definition - Locality Sensitive Hashing

Let $\mathcal{H}$ be a family of hash functions $h:M\to S$.
For $c>1$, $r>0$, and $p_1>p_2$, $\mathcal{H}$ is
$(c,r,p_1,p_2)$-locality sensitive if:

If $d(p,q)\leq r$:

$$
\Pr_{h\in\mathcal{H}}[h(p)=h(q)]\geq p_1.
$$

If $d(p,q)>cr$:

$$
\Pr_{h\in\mathcal{H}}[h(p)=h(q)]\leq p_2.
$$

The probability for distances in $(r,cr]$ is not specified.

![[Pics/SimSearch2/SimSearch2-10.png]]

### Theorem - Basic LSH Performance for $(c,r)$-ANNS

Using one hash table built from a $(c,r,p_1,p_2)$-LSH family:

| Quantity | Bound |
|---|---|
| Construction time | $O(Dn)$ |
| Space | $O(Dn)$ |
| Query time | $O(Dnp_2)$ in expectation |
| Success probability | at least $p_1$ |

![[Pics/SimSearch2/SimSearch2-16.png]]

#### Proof - Correctness

If $B_r(q)\cap P\neq\emptyset$, choose:

$$
p\in B_r(q)\cap P.
$$

If $h(p)=h(q)$, then $p$ is in the scanned bucket and is a legal output because
$d(p,q)\leq r\leq cr$.

By the LSH property:

$$
\Pr(h(p)=h(q))\geq p_1.
$$

Therefore the query succeeds with probability at least $p_1$.

If $B_r(q)\cap P=\emptyset$, returning `null` is legal, and returning a point within
distance $cr$ is also legal.

![[Pics/SimSearch2/SimSearch2-17.png]]
![[Pics/SimSearch2/SimSearch2-18.png]]

#### Proof - Expected Query Time

Let:

$$
x=|\{p\in P:d(p,q)>cr \text{ and } h(p)=h(q)\}|.
$$

For every far point $p$:

$$
\Pr(h(p)=h(q))\leq p_2.
$$

There are at most $n$ far points, so:

$$
E[x]\leq np_2.
$$

Each checked distance costs $O(D)$, so expected query time is:

$$
O(Dnp_2).
$$

![[Pics/SimSearch2/SimSearch2-19.png]]

### Theorem - Bit Sampling for Hamming Distance

For $M=\{0,1\}^D$, define:

$$
h_i(x)=x[i],
\qquad 0\leq i<D.
$$

Let:

$$
\mathcal{H}_H=\{h_i:0\leq i<D\}.
$$

For two vectors $p,q$:

$$
\Pr_{h\in\mathcal{H}_H}[h(p)=h(q)]
=1-\frac{d_H(p,q)}{D}.
$$

Thus $\mathcal{H}_H$ is:

$$
(c,r,1-r/D,1-cr/D)\text{-locality sensitive}.
$$

![[Pics/SimSearch2/SimSearch2-23.png]]
![[Pics/SimSearch2/SimSearch2-24.png]]

#### Proof

The sampled bit differs with probability:

$$
\frac{d_H(p,q)}{D}.
$$

So collision probability is:

$$
1-\frac{d_H(p,q)}{D}.
$$

If $d_H(p,q)\leq r$:

$$
1-\frac{d_H(p,q)}{D}\geq 1-\frac{r}{D}=p_1.
$$

If $d_H(p,q)>cr$:

$$
1-\frac{d_H(p,q)}{D}<1-\frac{cr}{D}=p_2.
$$

### Definition - $\rho$ Factor

For an LSH family:

$$
\rho=\frac{\log_2 p_1}{\log_2 p_2}
=\frac{\log_2(1/p_1)}{\log_2(1/p_2)}.
$$

Since $1\geq p_1>p_2>0$:

$$
\rho\in(0,1).
$$

Smaller $\rho$ is better.

For bit sampling:

$$
\rho
=\frac{\log_2(1-r/D)}{\log_2(1-cr/D)}
\sim \frac{1}{c}.
$$

![[Pics/SimSearch2/SimSearch2-25.png]]

### Definition - Random Projection LSH for Euclidean Distance

For $M=\mathbb{R}^D$, choose $w>0$, $a\in \mathbb{R}^D$, and $b\in[0,w]$.
Define:

$$
h_{a,b}(p)=
\left\lceil \frac{\langle a,p\rangle+b}{w}\right\rceil.
$$

If $a$ is selected from $N^D(0,1)$ and $b$ uniformly from $[0,w]$, the family is
LSH for Euclidean distance with:

$$
\rho=O(1/c).
$$

Better Euclidean LSH families achieve:

$$
\rho=O(1/c^2).
$$

![[Pics/SimSearch2/SimSearch2-26.png]]

### OR Construction - Repetition

Use $\ell$ independent hash tables from the same LSH family.

For a near point $p$ with $d(p,q)\leq r$, the probability that $p$ fails to collide
with $q$ in one table is at most $1-p_1$.

The probability it fails in all $\ell$ tables is at most:

$$
(1-p_1)^\ell.
$$

Therefore, the probability it collides in at least one table is at least:

$$
1-(1-p_1)^\ell.
$$

![[Pics/SimSearch2/SimSearch2-34.png]]
![[Pics/SimSearch2/SimSearch2-35.png]]
![[Pics/SimSearch2/SimSearch2-36.png]]

### AND Construction - Concatenation

Let $\mathcal{G}$ be obtained by concatenating $k$ independent functions from
$\mathcal{H}$:

$$
g(p)=(h_1(p),\ldots,h_k(p)).
$$

If $d(p,q)\leq r$:

$$
\Pr(g(p)=g(q))\geq p_1^k.
$$

If $d(p,q)>cr$:

$$
\Pr(g(p)=g(q))\leq p_2^k.
$$

Choose:

$$
k=\log_{1/p_2}n
=\frac{\log_2 n}{\log_2(1/p_2)}.
$$

Then:

$$
p_2^k=\frac{1}{n}.
$$

Using:

$$
\rho=\frac{\log_2(1/p_1)}{\log_2(1/p_2)},
$$

we get:

$$
p_1^k=n^{-\rho}.
$$

Thus the expected number of far-point collisions is at most 1, while a near point
collides with probability at least $n^{-\rho}$.

![[Pics/SimSearch2/SimSearch2-38.png]]
![[Pics/SimSearch2/SimSearch2-39.png]]
![[Pics/SimSearch2/SimSearch2-40.png]]

### Theorem - General LSH Schema

Use:

$$
k=\log_{1/p_2}n,
\qquad
\ell=2p_1^{-k}=2n^\rho.
$$

Build $\ell$ hash tables. Each table uses one concatenated hash function:

$$
g_i=(h_{i,1},\ldots,h_{i,k}).
$$

Query scans:

$$
T_1[g_1(q)],\ldots,T_\ell[g_\ell(q)]
$$

and stops when it finds a point within distance $cr$.

The success probability is at least $1/2$.

Performance:

| Quantity | Bound |
|---|---|
| Construction time | $O(Dn^{1+\rho}\log_{1/p_2}n)$ |
| Space | $O(Dn+n^{1+\rho}\log_{1/p_2}n)$ |
| Query time | $O(Dn^\rho\log_{1/p_2}n)$ in expectation |

![[Pics/SimSearch2/SimSearch2-42.png]]
![[Pics/SimSearch2/SimSearch2-49.png]]

### Concatenated Bit Sampling

Concatenating $k$ bit-sampling hashes means selecting $k$ random coordinates.

If $d_H(p,q)\leq r$:

$$
\Pr[h(p)=h(q)]\geq (1-r/D)^k.
$$

If $d_H(p,q)\geq cr$:

$$
\Pr[h(p)=h(q)]\leq (1-cr/D)^k.
$$

Concatenation does not change the $\rho$ value.

![[Pics/SimSearch2/SimSearch2-54.png]]
![[Pics/SimSearch2/SimSearch2-55.png]]
