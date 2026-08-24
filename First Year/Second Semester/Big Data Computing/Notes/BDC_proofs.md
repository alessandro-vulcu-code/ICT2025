# Big Data Computing Proofs

## Table of Contents

- [[#MTBF and Word Count|MTBF and Word Count]]
  - [[#Mean Time Between Failures|Mean Time Between Failures]]
  - [[#Word Count with One Round of MapReduce|Word Count with One Round of MapReduce]]
- [[#Class Count in MapReduce|Class Count in MapReduce]]
  - [[#One-Round Class Count without Partitioning|One-Round Class Count without Partitioning]]
  - [[#Two-Round Class Count with Deterministic Partitioning|Two-Round Class Count with Deterministic Partitioning]]
  - [[#Two-Round Class Count with Random Partitioning|Two-Round Class Count with Random Partitioning]]
  - [[#High-Probability Load Bound for Random Partitioning|High-Probability Load Bound for Random Partitioning]]
- [[#FFT and k-Center|FFT and k-Center]]
  - [[#FFT 2-Approximation Theorem|FFT 2-Approximation Theorem]]
  - [[#Composable Coresets for k-Center|Composable Coresets for k-Center]]
  - [[#MR-FFT Approximation Theorem|MR-FFT Approximation Theorem]]
  - [[#Why Uniform Sampling Is Not Enough|Why Uniform Sampling Is Not Enough]]
  - [[#Diameter Approximation Lemma|Diameter Approximation Lemma]]
- [[#Diversity Maximization Coreset|Diversity Maximization Coreset]]
- [[#Streaming Algorithms|Streaming Algorithms]]
  - [[#Boyer-Moore Majority Vote|Boyer-Moore Majority Vote]]
  - [[#Reservoir Sampling|Reservoir Sampling]]
  - [[#Sticky Sampling for Approximate Frequent Items|Sticky Sampling for Approximate Frequent Items]]
  - [[#Flajolet-Martin Intuition for Distinct Counting|Flajolet-Martin Intuition for Distinct Counting]]
  - [[#Count-Min Sketch|Count-Min Sketch]]
  - [[#Count Sketch|Count Sketch]]
  - [[#Bloom Filters|Bloom Filters]]
  - [[#Locality-Sensitive Hashing Query Proof|Locality-Sensitive Hashing Query Proof]]
- [[#Foundational Definitions|Foundational Definitions]]
  - [[#MapReduce and Spark Definitions|MapReduce and Spark Definitions]]
  - [[#Metric and Clustering Definitions|Metric and Clustering Definitions]]
- [[#Additional Coreset and k-Means Results|Additional Coreset and k-Means Results]]
- [[#Additional Streaming Results|Additional Streaming Results]]
  - [[#Probabilistic Counting Guarantee|Probabilistic Counting Guarantee]]
  - [[#Full Count Sketch Guarantees|Full Count Sketch Guarantees]]
  - [[#Universal Hash Families|Universal Hash Families]]
- [[#kd-Trees and Exact Similarity Search|kd-Trees and Exact Similarity Search]]
- [[#LSH Families and Amplification|LSH Families and Amplification]]
- [[#Supplementary Proof Exercises|Supplementary Proof Exercises]]
- [[#Summary Table|Summary Table]]

## MTBF and Word Count

### Mean Time Between Failures

Consider a system with $N$ components $C_1, \dots, C_N$. At each time step, each
component may fail independently with probability

$$
p = P[C_i \text{ fails at time } t].
$$

The probability that at least one component fails at time $t$ is

$$
P[\text{some } C_i \text{ fails at time } t] = 1 - (1-p)^N.
$$

Let $X$ be the number of time units before the next failure. Since failures across
components are independent, $X$ is geometric with success probability
$1 - (1-p)^N$, hence

$$
E[X] = \frac{1}{1-(1-p)^N}.
$$

The source also contains the expression $\frac{1}{N-1}$ after this formula;
that looks like a transcription artifact unless an additional assumption was
made.

### Word Count with One Round of MapReduce

**Input:** $K$ documents

$$
D_1, \dots, D_K,
\qquad
D_i = (\text{name}, \text{list of words}).
$$

Example:

$$
D_2 = \text{avantage/apple/pear}.
$$

**Output:** pairs $(w, c(w))$, where $w$ is a word appearing in some document and
$c(w)$ is the total number of occurrences of $w$ across all documents.

**Round 1 - map phase.** For each document $D_i$, compute local word counts:

$$
D_i \mapsto
\{(w, c_i(w)) : w \text{ is a word in } D_i,\ c_i(w) =
\#\text{occurrences of } w \text{ in } D_i\}.
$$

**Round 1 - reduce phase.** For each word $w$, let $L_w$ be the list of local
counts received by the reducer:

$$
L_w = \{c_i(w) : w \text{ appears in } D_i\}.
$$

The reducer outputs

$$
(w, L_w) \mapsto \left(w, \sum_{i=1}^{K} c_i(w)\right).
$$

**Analysis.** Let $N_i$ be the number of words in $D_i$, and let

$$
N_{\max} = \max_i N_i.
$$

The map phase needs $O(N_{\max})$ local space. The reduce phase may receive one
count from each document for a single word, so it needs $O(K)$ local space.
Therefore,

$$
M_L = O(\max\{N_{\max}, K\}) = O(N_{\max} + K).
$$

Let $N$ be the total number of words in all documents. The aggregate space is
$O(N)$ because input pairs, intermediate pairs, and output pairs are all linear
in the number of processed words.

## Class Count in MapReduce

The **class count problem** is the following. We have $N$ objects
$\mathcal{O}_i$, $1 \leq i \leq N$, each labeled with a class $\chi_i$. The goal
is to count how many objects belong to each class $\chi$.

### One-Round Class Count without Partitioning

**Input pairs:**

$$
(i, (\mathcal{O}_i, \chi_i)).
$$

**Map phase.** Emit the class label as key:

$$
(i, (\mathcal{O}_i, \chi_i)) \mapsto (\chi_i, \mathcal{O}_i).
$$

**Reduce phase.** For each class $\chi$, let $L_\chi$ be the list of objects
with label $\chi$. The reducer outputs

$$
(\chi, L_\chi) \mapsto (\chi, |L_\chi|).
$$

**Analysis.** This uses one MapReduce round. If all $N$ objects have the same
class label, one reducer receives $N$ values. Therefore the local space can be
$O(N)$, which does not satisfy the usual sublinear local-space design goal.

### Two-Round Class Count with Deterministic Partitioning

Choose a number of partitions $\ell$.

**Round 1 - map phase.** Partition objects by their index:

$$
(i, (\mathcal{O}_i, \chi_i)) \mapsto (i \bmod \ell, \chi_i).
$$

**Round 1 - reduce phase.** For each partition $j$, let $L_j$ be the list of
labels assigned to that partition. The reducer counts occurrences of every label
inside $L_j$:

$$
(j, L_j) \mapsto \{(\chi, c(j,\chi)) : \chi \text{ appears in } L_j\}.
$$

**Round 2 - map phase.** Forward each partial count by class label:

$$
(\chi, c(j,\chi)) \mapsto (\chi, c(j,\chi)).
$$

**Round 2 - reduce phase.** Sum the partial counts:

$$
(\chi, L_\chi) \mapsto
\left(\chi, \sum_{c(j,\chi) \in L_\chi} c(j,\chi)\right).
$$

**Analysis.** If deterministic partitioning balances the input, each first-round
reducer receives $O(N/\ell)$ objects. The second round aggregates one partial
count per partition and class.

### Two-Round Class Count with Random Partitioning

The deterministic partition can be replaced by random partitioning.

**Round 1 - map phase.** For each object, choose a random key
$x \in \{0,\dots,\ell-1\}$ uniformly and emit

$$
(i, (\mathcal{O}_i, \chi_i)) \mapsto (x, \chi_i).
$$

Only the map phase of round 1 changes. Let $m_x$ be the number of intermediate
pairs with key $x$, and let

$$
m = \max_x m_x.
$$

The first-round reduce phase needs $O(m)$ local space. Since $N$ objects are
placed into $\ell$ partitions, some partition has at least $N/\ell$ objects, so
$m \geq N/\ell$. The goal is to show that, with high probability, random
partitioning also gives $m = O(N/\ell)$.

### High-Probability Load Bound for Random Partitioning

> [!Important] Theorem - Random Partition Load
> Fix $\ell = \sqrt{N}$. Suppose round-1 keys are assigned independently and
> uniformly to the $\ell$ partitions. Then, with high probability,
>
> $$
> m = O(\sqrt{N})
> $$
>
> and therefore
>
> $$
> M_L = O(\sqrt{N}).
> $$

**Proof.** We use two standard probability tools.

**Union bound.** For events $E_1,\dots,E_n$,

$$
P\left[\bigcup_{i=1}^{n} E_i\right] \leq \sum_{i=1}^{n} P[E_i].
$$

**Chernoff bound.** Let $X_1,\dots,X_n$ be independent Bernoulli random
variables, let $X = \sum_i X_i$, and let $\mu = E[X]$. For suitable constants,
the probability that $X$ is much larger than $\mu$ decreases exponentially in
$\mu$.

Fix a partition $x$. For each input object, define

$$
y_i =
\begin{cases}
1 & \text{if object } i \text{ is assigned to partition } x,\\
0 & \text{otherwise.}
\end{cases}
$$

Then $y_i$ is Bernoulli with

$$
P[y_i = 1] = \frac{1}{\sqrt{N}}.
$$

The load of partition $x$ is

$$
m_x = \sum_{i=1}^{N} y_i,
$$

so $m_x$ is binomial with expectation

$$
E[m_x] = N \cdot \frac{1}{\sqrt{N}} = \sqrt{N}.
$$

By Chernoff,

$$
P[m_x \geq 8\sqrt{N}] \leq 2^{-6\sqrt{N}}.
$$

For sufficiently large $N$, this is at most $1/N^6$. Define the event

$$
E_x = \{m_x \geq 8\sqrt{N}\}.
$$

By the union bound over the $\sqrt{N}$ partitions,

$$
P[m \geq 8\sqrt{N}]
= P\left[\bigcup_x E_x\right]
\leq \sqrt{N} \cdot \frac{1}{N^6}
< \frac{1}{N^5}.
$$

Therefore,

$$
P[m < 8\sqrt{N}] \geq 1 - \frac{1}{N^5}.
$$

So, with high probability, no partition receives too many objects, and
$m = O(\sqrt{N})$.

## FFT and k-Center

### FFT 2-Approximation Theorem

The **farthest-first traversal** (FFT) algorithm selects centers one at a time.
After choosing the first center, each next center is the point farthest from the
set of centers already selected.

> [!Important] Theorem - FFT for k-Center
> Let $S$ be the set of $k$ centers returned by running FFT on $P$. Then
>
> $$
> \Phi(P,S) \leq 2\Phi_{\text{center}}^{\text{opt}}(P,k).
> $$
>
> Therefore FFT is a 2-approximation algorithm for $k$-center.

**Proof.** Let

$$
S = \{c_1,c_2,\dots,c_k\}
$$

be the centers selected by FFT, and let $q$ be the point of $P$ farthest from
$S$:

$$
d(q,S) \geq d(x,S) \qquad \forall x \in P.
$$

Consider the $k+1$ points

$$
S \cup \{q\} = \{c_1,\dots,c_k,q\}.
$$

By the choice made by FFT, every pair of points in this set is at distance at
least $d(q,S)$. More explicitly, if $i < j$, then $c_j$ was chosen as a point
farthest from $\{c_1,\dots,c_{j-1}\}$, so

$$
d(c_i,c_j) \geq d(q,S).
$$

Let

$$
S^* = \{c_1^*,c_2^*,\dots,c_k^*\}
$$

be an optimal set of centers, and let

$$
\Phi_{\text{center}}^{\text{opt}}(P,k) = \Phi(P,S^*).
$$

The optimal centers induce $k$ clusters:

$$
C_t^* = \{x \in P : c_t^* \text{ is the closest optimal center to } x\},
\qquad
P = \bigcup_{t=1}^{k} C_t^*.
$$

The set $S \cup \{q\}$ has $k+1$ points but there are only $k$ optimal clusters.
By the pigeonhole principle, two of those points, call them $c_a$ and $c_b$,
belong to the same optimal cluster $C_t^*$.

By the triangle inequality,

$$
d(c_a,c_b)
\leq d(c_a,c_t^*) + d(c_b,c_t^*)
\leq 2\Phi_{\text{center}}^{\text{opt}}(P,k).
$$

Since every pair in $S \cup \{q\}$ has distance at least $d(q,S)$,

$$
d(q,S) \leq d(c_a,c_b)
\leq 2\Phi_{\text{center}}^{\text{opt}}(P,k).
$$

Finally, for every $x \in P$,

$$
d(x,S) \leq d(q,S) \leq 2\Phi_{\text{center}}^{\text{opt}}(P,k).
$$

Thus

$$
\Phi(P,S) \leq 2\Phi_{\text{center}}^{\text{opt}}(P,k).
$$

### Composable Coresets for k-Center

Let

$$
P = P_1 \cup P_2 \cup \dots \cup P_\ell.
$$

For each partition $P_i$, run FFT and compute a local coreset $T_i$. Let

$$
T = T_1 \cup T_2 \cup \dots \cup T_\ell.
$$

> [!Important] Lemma - Local FFT Representatives
> For every $x \in P_i$,
>
> $$
> d(x,T_i) \leq 2\Phi_{\text{center}}^{\text{opt}}(P_i,k).
> $$
>
> Since $\Phi_{\text{center}}^{\text{opt}}(P_i,k) \leq
> \Phi_{\text{center}}^{\text{opt}}(P,k)$, every point has a close
> representative in $T$.

**Proof.** Fix a partition $P_i$. Let $T_i$ be the $k$ centers returned by FFT
on $P_i$, and let $q_i$ be the point of $P_i$ farthest from $T_i$. Repeating the
FFT 2-approximation argument inside $P_i$ gives

$$
d(q_i,T_i) \leq 2\Phi_{\text{center}}^{\text{opt}}(P_i,k).
$$

Since $q_i$ is farthest from $T_i$, for every $x \in P_i$,

$$
d(x,T_i) \leq d(q_i,T_i)
\leq 2\Phi_{\text{center}}^{\text{opt}}(P_i,k).
$$

### MR-FFT Approximation Theorem

MR-FFT works in two rounds:

1. Partition $P$ into $\ell$ parts and run FFT on each part, producing
   $T_1,\dots,T_\ell$.
2. Let $T = \bigcup_i T_i$ and run FFT on $T$ to obtain the final center set
   $S$.

> [!Important] Theorem - MR-FFT Approximation
> Let $S$ be the set of $k$ centers returned by MR-FFT on $P$. Then
>
> $$
> \Phi(P,S) \leq 4\Phi_{\text{center}}^{\text{opt}}(P,k).
> $$
>
> The source writes a constant that appears as $G$; the triangle-inequality
> derivation gives the standard constant $4$.

**Proof.** From the previous lemma, for every $x \in P$ there exists a
representative $y \in T$ such that

$$
d(x,y) \leq 2\Phi_{\text{center}}^{\text{opt}}(P,k).
$$

The final set $S$ is obtained by running FFT on $T$. Let $\bar{q}$ be the point
of $T$ farthest from $S$. Since $T \subseteq P$, the FFT argument gives

$$
d(\bar{q},S) \leq 2\Phi_{\text{center}}^{\text{opt}}(P,k).
$$

Therefore, for every $y \in T$,

$$
d(y,S) \leq d(\bar{q},S)
\leq 2\Phi_{\text{center}}^{\text{opt}}(P,k).
$$

For any $x \in P$, choose its representative $y \in T$ and the closest center
$c \in S$ to $y$. By the triangle inequality,

$$
d(x,S)
\leq d(x,c)
\leq d(x,y) + d(y,c)
\leq 4\Phi_{\text{center}}^{\text{opt}}(P,k).
$$

Thus

$$
\Phi(P,S) \leq 4\Phi_{\text{center}}^{\text{opt}}(P,k).
$$

**Space analysis.** In round 1, each point is assigned to one partition. If the
partitioning is balanced, each reducer handles $O(N/\ell)$ points. In round 2,
the reducer handles $O(k\ell)$ coreset points. Therefore,

$$
M_L = O(\max\{N/\ell,\ k\ell\}).
$$

Choosing

$$
\ell = \sqrt{\frac{N}{k}}
$$

gives

$$
M_L = O(\sqrt{Nk}).
$$

### Why Uniform Sampling Is Not Enough

Consider $k=2$. Suppose $P$ consists of a large dense cluster plus one outlier
$q$ far away. If $T$ is a uniform random sample of size $\sqrt{N}k$, then

$$
P[q \in T] = \frac{\sqrt{N}k}{N} = \frac{k}{\sqrt{N}} \to 0.
$$

With high probability the sample does not contain the outlier. If we then select
two centers from $T$, both centers may lie in the dense cluster, while the true
optimal $2$-center solution uses one center for the outlier. This shows why a
carefully built coreset is needed.

### Diameter Approximation Lemma

Let

$$
d_{\max} = \max_{z,w \in P} d(z,w)
$$

be the true diameter. For an arbitrary point $x_i \in P$, define

$$
d_{\max}(i) = \max_{0 < j < N} d(x_i,x_j).
$$

> [!Important] Lemma - Diameter from One Point
> For every $0 < i < N$,
>
> $$
> d_{\max} \in [d_{\max}(i),\ 2d_{\max}(i)].
> $$

**Proof.** The lower bound follows directly from the definition:

$$
d_{\max} \geq d_{\max}(i).
$$

For the upper bound, let $z,w$ be points realizing the diameter. By the triangle
inequality,

$$
d_{\max} = d(z,w)
\leq d(z,x_i) + d(w,x_i)
\leq 2d_{\max}(i).
$$

Now let $T = \{c_1,\dots,c_h\}$ be a set of representatives, let $q$ be the
point of $P$ farthest from $T$, and let

$$
R = d(q,T).
$$

Let $d_T$ be the diameter of $T$. If $z,w$ realize the true diameter in $P$ and
$c_z,c_w \in T$ are their closest representatives, then

$$
d_{\max}
= d(z,w)
\leq d(z,c_z) + d(c_z,c_w) + d(c_w,w)
\leq 2R + d_T.
$$

Since $T \subseteq P$, $d_T \leq d_{\max}$. Therefore,

$$
d_T \leq d_{\max} \leq d_T + 2R.
$$

As the number of representatives grows, $R$ becomes smaller and $d_T$ becomes a
better approximation of the true diameter.

## Diversity Maximization Coreset

Consider a coreset-based algorithm for diversity maximization.

Example parameters:

$$
h = 5,
\qquad
k = 3.
$$

The algorithm:

1. Run FFT to extract $h$ centers from $P$.
2. Assign every point to its closest center, forming clusters.
3. Select up to $k$ points from each cluster.
4. Build a coreset $T$ containing the centers and the selected points.

Let $S^*$ be an optimal size-$k$ solution for diversity maximization on $P$.
For each cluster $C_\ell$, create an injective mapping

$$
\pi : S^* \cap C_\ell \to T \cap C_\ell.
$$

This is possible because

$$
|T \cap C_\ell| = k
\qquad \text{and} \qquad
|S^* \cap C_\ell| \leq |S^*| = k.
$$

Let $R$ be the clustering radius:

$$
d(x,\{c_1,\dots,c_h\}) \leq R
\qquad \forall x \in P.
$$

For every $x_i \in S^*$,

$$
d(x_i,\pi(x_i))
\leq d(x_i,c_\ell) + d(c_\ell,\pi(x_i))
\leq 2R.
$$

So every point of the optimal solution has a nearby proxy in $T$.

Consider

$$
S = \{\pi(x_i) : x_i \in S^*\} \subseteq T,
\qquad
|S| = k.
$$

For any pair $x_i,x_j \in S^*$, by the triangle inequality,

$$
d(\pi(x_i),\pi(x_j))
\geq d(x_i,x_j)
- d(x_i,\pi(x_i))
- d(x_j,\pi(x_j)).
$$

Summing over pairs gives

$$
\operatorname{div}(S)
\geq \operatorname{div}^{\text{opt}}(P,k)
- O(k^2R).
$$

If $h$ is large enough, we can make the radius term small. In the source this is
written as a condition of the form

$$
GR \leq \epsilon \Phi_{\text{value}}^{\text{opt}}(P,k).
$$

Then

$$
\operatorname{div}(S)
\geq (1-\epsilon)\operatorname{div}^{\text{opt}}(P,k),
$$

and since $S \subseteq T$,

$$
\operatorname{div}^{\text{opt}}(T,k)
\geq \operatorname{div}(S)
\geq (1-\epsilon)\operatorname{div}^{\text{opt}}(P,k).
$$

Equivalently, for a slightly adjusted $\epsilon' < \epsilon$,

$$
\operatorname{div}^{\text{opt}}(T,k)
\geq \frac{1}{1+\epsilon'}\operatorname{div}^{\text{opt}}(P,k).
$$

> [!Important] Fact - Relation Between k-Center and Diversity
>
> $$
> \Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k)
> \leq
> \frac{\operatorname{div}^{\mathrm{opt}}(P,k)}{\binom{k}{2}}.
> $$

> [!Important] Theorem - Diversity Coreset Quality
> If the proxy clustering has radius
>
> $$
> R\leq\frac18\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k),
> $$
>
> then
>
> $$
> \operatorname{div}^{\mathrm{opt}}(T,k)
> \geq\frac12\operatorname{div}^{\mathrm{opt}}(P,k).
> $$

**Proof.** Map each point $x\in S^*$ injectively to its same-cluster proxy
$\pi(x)\in T$. Since $d(x,\pi(x))\leq2R$, every pair loses at most $4R$:

$$
d(\pi(x_i),\pi(x_j))\geq d(x_i,x_j)-4R.
$$

Summing over all pairs and using the fact above,

$$
\begin{aligned}
\operatorname{div}(\pi(S^*))
&\geq\operatorname{div}^{\mathrm{opt}}(P,k)-4R\binom{k}{2}\\
&\geq\operatorname{div}^{\mathrm{opt}}(P,k)
-\frac12\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k)\binom{k}{2}\\
&\geq\frac12\operatorname{div}^{\mathrm{opt}}(P,k).
\end{aligned}
$$

Because $\pi(S^*)\subseteq T$, the optimum on $T$ is at least this value.

## Streaming Algorithms

### Boyer-Moore Majority Vote

Example stream:

$$
\Sigma = A,A,A,C,C,B,B,A,A.
$$

| Step | Item | Candidate | Count |
|---:|:---:|:---:|---:|
| 0 | - | null | 0 |
| 1 | A | A | 1 |
| 2 | A | A | 2 |
| 3 | A | A | 3 |
| 4 | C | A | 2 |
| 5 | C | A | 1 |
| 6 | B | A | 0 |
| 7 | B | B | 1 |
| 8 | A | B | 0 |
| 9 | A | A | 1 |

At the end, the candidate is $A$, which is the majority element.

> [!Important] Theorem - Boyer-Moore Majority Vote
> Given a stream $\Sigma$ with a majority element $m$, the Boyer-Moore
> algorithm returns $m$ using:
>
> - $O(1)$ working memory;
> - one pass;
> - $O(1)$ update time per element.

**Invariant.** After processing $x_1,\dots,x_t$, the processed elements can be
partitioned into:

- $\text{count}_t$ unmatched occurrences of $\text{cand}_t$;
- $(t-\text{count}_t)/2$ pairs $(e_1,e_2)$ with $e_1 \neq e_2$.

Example for $t=5$:

$$
x_1,\dots,x_5 = A,A,A,C,C.
$$

Here $\text{cand}=A$ and $\text{count}=1$. The prefix can be decomposed into one
unmatched $A$ and two canceling pairs $(A,C)$.

**Correctness proof.** Suppose, for contradiction, that the final candidate is
not the majority element $m$. By the invariant, all elements except the unmatched
final candidate occurrences are partitioned into pairs of distinct items. Each
such pair contains at most one copy of $m$.

If the final candidate is not $m$, then $m$ can appear only inside the canceling
pairs. Hence $m$ appears at most $n/2$ times, contradicting the assumption that
$m$ is a majority element. Therefore the final candidate must be $m$.

### Reservoir Sampling

> [!Important] Theorem - Reservoir Sampling
> Let $\Sigma = x_1,x_2,\dots$. For every time $t \geq m$, the set $S$
> maintained by reservoir sampling is an $m$-sample of
>
> $$
> \Sigma_t = x_1,\dots,x_t.
> $$
>
> That is, for every $i \in [1,t]$,
>
> $$
> P[x_i \in S_t] = \frac{m}{t}.
> $$

**Proof.** We prove the claim by induction on $t \geq m$.

**Base case.** For $t=m$, the reservoir contains exactly the first $m$ elements,
so each element is included with probability $1=m/m$.

**Inductive step.** Assume the claim holds at time $t-1$, so for each
$i < t$,

$$
P[x_i \in S_{t-1}] = \frac{m}{t-1}.
$$

At time $t$, the new item $x_t$ is inserted with probability $m/t$. Hence

$$
P[x_t \in S_t] = \frac{m}{t}.
$$

Now fix an old item $x_i$ with $i<t$. If $x_t$ is inserted, one of the $m$
current reservoir elements is evicted uniformly at random. Therefore an old
item that is currently in the reservoir is evicted with probability

$$
\frac{m}{t} \cdot \frac{1}{m} = \frac{1}{t}.
$$

Thus it survives with probability $1 - 1/t$, and

$$
P[x_i \in S_t]
= P[x_i \in S_{t-1}]\left(1-\frac{1}{t}\right)
= \frac{m}{t-1}\cdot\frac{t-1}{t}
= \frac{m}{t}.
$$

This completes the induction.

### Sticky Sampling for Approximate Frequent Items

The source refers to the $\epsilon$-AFI problem. Interpreting the OCR artifact
"4" as the standard frequency threshold $\phi$, the goal is:

- return all items with frequency at least $\phi n$;
- return no item with frequency below $(\phi-\epsilon)n$;
- succeed with probability at least $1-\delta$.

> [!Important] Theorem - Sticky Sampling
> Sticky sampling solves the $\epsilon$-approximate frequent items problem with
> probability at least $1-\delta$. It uses one pass, expected update time
> $O(1)$, and expected working memory
>
> $$
> O(r)=O\left(\frac{\ln(1/(\delta\phi))}{\epsilon}\right),
> \qquad
> r=\left\lceil\frac{\ln(1/(\delta\phi))}{\epsilon}\right\rceil.
> $$

**Working memory.** The working memory is proportional to the number of sampled
items stored in $S$. If an item contributes an extra stored counter with
probability $r/n$, then the expected number of stored counters is

$$
O\left(n\cdot\frac{r}{n}\right) = O(r).
$$

Thus $E[|S|]\leq r$, proving expected memory $O(r)$.

**Correctness proof.** Stored count $f_e(x)$ is always a lower bound on true frequency.
Because output requires $f_e(x)\geq(\phi-\epsilon)n$, no item below this threshold can
be returned.

Now let $a$ be frequent. If one of its first $\lceil\epsilon n\rceil$ occurrences is
sampled, all later occurrences increment its counter, giving
$f_e(a)\geq(\phi-\epsilon)n$. Therefore

$$
\Pr(a\text{ is missed})
\leq\left(1-\frac rn\right)^{\epsilon n}
\leq e^{-\epsilon r}.
$$

There are at most $1/\phi$ frequent items. Union bound gives

$$
\Pr(\text{some frequent item is missed})
\leq\frac1\phi e^{-\epsilon r}
\leq\delta.
$$

Hence every frequent item is returned with probability at least $1-\delta$, and no
deep false positive is ever returned.

### Flajolet-Martin Intuition for Distinct Counting

Example universe:

$$
U = \text{alphabet},
\qquad
|U| = 26.
$$

Representing $|U|-1 = 25$ in binary requires $5$ bits.

Example stream:

$$
\Sigma = A,D,A,A,C,B,F,F,B,A,E,C.
$$

The algorithm hashes each item and tracks the maximum number of trailing zeros
seen in the hashed values.

For a random hash value $h(x)$,

$$
P[\operatorname{tz}(h(x)) \geq 1] = \frac{1}{2},
$$

and in general,

$$
P[\operatorname{tz}(h(x)) \geq j] = \frac{1}{2^j}.
$$

If the stream has $F_0$ distinct elements, then the expected number of distinct
hashed values with at least $j$ trailing zeros is

$$
\frac{F_0}{2^j}.
$$

We expect to see such a value when

$$
\frac{F_0}{2^j} \geq 1,
$$

that is, when

$$
2^j \leq F_0.
$$

Therefore the maximum observed number of trailing zeros is an estimator for
$\log_2 F_0$, and $2^R$ estimates the number of distinct items.

### Count-Min Sketch

Example:

$$
n = 45,
\qquad
d = 3,
\qquad
w = 3.
$$

Stream:

$$
\Sigma = A,B,C,B,D,A,C,D,A,B,D,C,A,A,B.
$$

Hash values and true frequencies:

| Item | Frequency | $h_0$ | $h_1$ | $h_2$ |
|:---:|---:|---:|---:|---:|
| $A$ | 5 | 0 | 1 | 1 |
| $B$ | 4 | 1 | 2 | 1 |
| $C$ | 3 | 0 | 0 | 2 |
| $D$ | 3 | 1 | 1 | 2 |

The estimate is the minimum counter among the $d$ rows:

$$
\hat{f}_u = \min_{0 \leq j < d} C[j,h_j(u)].
$$

Examples from the source:

$$
\hat{f}_A = \min\{8,8,g\} = 8 > f_A = 5,
$$

$$
\hat{f}_C = \min\{8,3,g\} = 3 = f_C.
$$

> [!Important] Theorem - Count-Min Sketch
> Consider a $d \times w$ count-min sketch for a stream $\Sigma$ of length $n$.
> With $w = 2/\epsilon$ and $d = \log_2(1/\delta)$, for any item $u$,
>
> $$
> P[\hat{f}_u - f_u \leq \epsilon n] \geq 1-\delta.
> $$

**Proof.** Fix an item $u$ and a row $j$. The counter $C[j,h_j(u)]$ contains
$f_u$ plus contributions from other items that collide with $u$ in row $j$.
In expectation, the colliding mass is at most

$$
E[C[j,h_j(u)] - f_u] \leq \frac{n}{w}
= \frac{\epsilon n}{2}.
$$

By Markov's inequality,

$$
P[C[j,h_j(u)] - f_u > \epsilon n] < \frac{1}{2}.
$$

The estimate $\hat{f}_u$ is bad only if every row overestimates $f_u$ by more
than $\epsilon n$. Assuming independent rows,

$$
P[\hat{f}_u - f_u > \epsilon n]
< \left(\frac{1}{2}\right)^d
= \delta.
$$

Therefore,

$$
P[\hat{f}_u - f_u \leq \epsilon n] \geq 1-\delta.
$$

### Count Sketch

Example parameters:

$$
d = 3,
\qquad
w = 3.
$$

Example stream:

$$
\bar{Z} = A,B,C,B,D,A,C,D,A,B,D,C,A,A,B.
$$

Hash and sign values:

| Item | Frequency | $h_0$ | $g_0$ | $h_1$ | $g_1$ | $h_2$ | $g_2$ |
|:---:|---:|---:|---:|---:|---:|---:|---:|
| $A$ | 5 | 0 | 1 | 1 | 1 | 1 | 1 |
| $B$ | 4 | 1 | -1 | 2 | 1 | 1 | -1 |
| $C$ | 3 | 0 | -1 | 0 | -1 | 2 | 1 |
| $D$ | 3 | 1 | -1 | 1 | 1 | 2 | 1 |

For each row $j$, count sketch estimates

$$
\tilde{f}_{u,j} = g_j(u) C[j,h_j(u)].
$$

The final estimate is the median:

$$
\tilde{f}_u = \operatorname{median}\{\tilde{f}_{u,0},\dots,\tilde{f}_{u,d-1}\}.
$$

Examples:

$$
\tilde{f}_A = \operatorname{median}\{2,8,1\} = 2,
$$

$$
\tilde{f}_B = \operatorname{median}\{7,4,-1\} = 4,
$$

$$
\tilde{f}_C = \operatorname{median}\{-2,3,6\} = 3,
$$

$$
\tilde{f}_D = \operatorname{median}\{7,8,6\} = 7.
$$

> [!Important] Theorem - Unbiased Count-Sketch Row Estimate
> For a fixed item $u$ and row $j$,
>
> $$
> E[\tilde{f}_{u,j}] = f_u.
> $$

**Proof.** Fix $u \in U$ and $j \in [0,d-1]$. For each $a \in U$, $a \neq u$,
define

$$
y_a =
\begin{cases}
f_a & \text{if } h_j(a)=h_j(u) \text{ and } g_j(a)=g_j(u),\\
-f_a & \text{if } h_j(a)=h_j(u) \text{ and } g_j(a)\neq g_j(u),\\
0 & \text{if } h_j(a)\neq h_j(u).
\end{cases}
$$

The variable $y_a$ is the signed contribution of item $a$ to the estimate of
$f_u$. Thus

$$
\tilde{f}_{u,j} = f_u + \sum_{a \neq u} y_a.
$$

For $a \neq u$,

$$
P[y_a = f_a] = P[y_a = -f_a] = \frac{1}{w}\cdot\frac{1}{2}.
$$

Therefore,

$$
E[y_a]
= f_a\left(\frac{1}{w}\cdot\frac{1}{2}\right)
- f_a\left(\frac{1}{w}\cdot\frac{1}{2}\right)
= 0.
$$

By linearity of expectation,

$$
E[\tilde{f}_{u,j}]
= E\left[f_u + \sum_{a \neq u} y_a\right]
= f_u + \sum_{a \neq u} E[y_a]
= f_u.
$$

### Bloom Filters

Example:

$$
S = \{X,Y\},
\qquad
n = 12,
\qquad
k = 2.
$$

| Item | $h_0$ | $h_1$ |
|:---:|---:|---:|
| $X$ | 0 | 4 |
| $Y$ | 1 | 9 |

Checking $X$ gives a true positive because both corresponding bits are $1$.
Checking an item $T$ with

$$
h_0(T)=4,
\qquad
h_1(T)=7
$$

can return a true negative if at least one of those bits is $0$. A false
positive happens when an item not in $S$ hashes only to positions already set to
$1$.

> [!Important] Theorem - Bloom Filter False Positive Probability
> Let a Bloom filter have $n$ bits, $k$ independent hash functions, and $m$
> inserted elements. Under the usual independence approximation, the false
> positive probability is approximately
>
> $$
> \left(1-e^{-km/n}\right)^k.
> $$

**Proof.** Each insertion sets $k$ bit positions. The $km$ selected positions can
be modeled as independent uniform indices in $[0,n-1]$.

For any bit position $\ell$,

$$
P[A[\ell]=0]
= \left(1-\frac{1}{n}\right)^{km}
\approx e^{-km/n}.
$$

Let

$$
p = P[A[\ell]=0] \approx e^{-km/n}.
$$

Then a random bit is $1$ with probability $1-p$. For an element $x \notin S$,
the Bloom filter returns positive only if all $k$ queried positions are $1$:

$$
P[\text{false positive}]
= \prod_{j=0}^{k-1} P[A[h_j(x)] = 1]
\approx (1-p)^k
= \left(1-e^{-km/n}\right)^k.
$$

### Locality-Sensitive Hashing Query Proof

Consider a locality-sensitive hashing data structure for near-neighbor search
with query point $q$, radius $r$, approximation factor $c$, and dataset $P$.

**Probabilistic correctness.**

**Case 1: $B_r(q) \cap P \neq \emptyset$.** A legal output is any point
$p' \in P$ such that

$$
d(q,p') \leq cr.
$$

Choose an arbitrary point

$$
p \in B_r(q) \cap P.
$$

By the LSH property, $p$ is mapped to the same bucket as $q$ with probability at
least $p_1$. Therefore,

$$
P[\text{answer is correct}]
\geq P[p \text{ is mapped to the same bucket as } q]
\geq p_1.
$$

**Case 2: $B_r(q) \cap P = \emptyset$.** If no point lies within distance $r$,
then returning `null` is correct. Returning a point at distance at most $cr$ is
also a legal approximate answer.

**Construction and space.** The construction and space bounds follow directly
from storing each point in the bucket determined by its hash value.

**Query time.** Suppose bucket $T[h(q)]$ is implemented as a list. The scan ends
when either a point at distance at most $cr$ from $q$ is found, or the list ends.
At most $x+1$ points are checked, where $x$ is the number of far points in the
bucket:

$$
x = |\{p \in T[h(q)] : d(p,q) > cr\}|.
$$

Each far point has probability at most $p_2$ of colliding with $q$. Since there
are at most $n$ far points,

$$
E[x] \leq np_2.
$$

Thus the expected number of checked points is at most

$$
1 + np_2.
$$

## Foundational Definitions

### MapReduce and Spark Definitions

> [!Important] Definition - MapReduce Round
> One **MapReduce round** transforms key-value pairs through three phases:
>
> 1. **Map:** each input pair is processed independently and produces zero or more
>    intermediate pairs.
> 2. **Shuffle:** intermediate pairs are grouped by key.
> 3. **Reduce:** each group $(k,L_k)$ is processed and produces zero or more output pairs.
>
> One invocation of reduce on $(k,L_k)$ is called a **reducer**. Keys act both as object
> addresses and as group labels.

> [!Important] Definition - MapReduce Performance Indicators
> - $R$: number of rounds.
> - $M_L$: maximum local memory used by one map or reduce invocation.
> - $M_A$: maximum aggregate space occupied at a phase boundary.
>
> Standard goals are $R=O(1)$, $M_L=O(|input|^\epsilon)$ for some $\epsilon<1$,
> $M_A=O(|input|)$, and low work per invocation.

For deterministic partitioning into $\ell$ balanced parts, the first aggregation uses
$O(N/\ell)$ local memory and the second uses $O(\ell)$. Therefore,

$$
M_L=O\left(\frac{N}{\ell}+\ell\right),
$$

which becomes $O(\sqrt N)$ for $\ell=\sqrt N$. Random partitioning achieves the same
bound with high probability by the Chernoff-and-union-bound proof given earlier.

> [!Important] Probabilistic Tools
> For events $E_1,\ldots,E_r$, the **union bound** is
>
> $$
> \Pr\left(\bigcup_{i=1}^r E_i\right)\leq\sum_{i=1}^r\Pr(E_i).
> $$
>
> For nonnegative $X$ and $a>0$, **Markov's inequality** is
>
> $$
> \Pr(X\geq a)\leq\frac{E[X]}{a}.
> $$
>
> If $X\sim\operatorname{Binom}(n,p)$ and $\mu=np$, the course uses
>
> $$
> \Pr(X\geq\delta_1\mu)\leq2^{-\delta_1\mu}
> \quad(\delta_1\geq6),
> $$
>
> $$
> \Pr(X\leq(1-\delta_2)\mu)\leq2^{-\delta_2^2\mu/2}
> \quad(0<\delta_2<1).
> $$

> [!Important] Definition - Resilient Distributed Dataset
> An **RDD** is an immutable, partitioned collection distributed across machines. It is
> created from stable storage or other RDDs, evaluated lazily, and fault tolerant through
> lineage.

> [!Important] Definition - Spark Operations
> - A **narrow transformation** maps each input partition to at most one output partition;
>   no shuffle is needed. Example: `map`.
> - A **wide transformation** may send one input partition to many output partitions;
>   shuffle may be needed. Example: `groupByKey`.
> - A **transformation** creates a new RDD lazily.
> - An **action** returns a result and triggers materialization.
> - `cache()` is `persist(StorageLevel.MEMORY_ONLY)`.
> - `persist(StorageLevel.MEMORY_AND_DISK)` spills partitions that do not fit in RAM.
> - `reduceByKey(f)` combines values by key using associative, commutative $f$, performing
>   local aggregation before cross-partition aggregation.

### Metric and Clustering Definitions

> [!Important] Definition - Metric Space
> A metric space $(M,d)$ satisfies, for all $x,y,z\in M$:
>
> 1. $d(x,y)\geq0$.
> 2. $d(x,y)=0$ iff $x=y$.
> 3. $d(x,y)=d(y,x)$.
> 4. $d(x,z)\leq d(x,y)+d(y,z)$.

Common distances are:

$$
d_{L_r}(X,Y)=\left(\sum_i|x_i-y_i|^r\right)^{1/r},
$$

$$
d_{\mathrm{angular}}(X,Y)=
\arccos\left(\frac{X\cdot Y}{\|X\|\|Y\|}\right),
$$

$$
d_H(X,Y)=|\{i:x_i\neq y_i\}|,
\qquad
d_J(S,T)=1-\frac{|S\cap T|}{|S\cup T|}.
$$

> [!Important] Definition - Combinatorial Optimization and Approximation
> A combinatorial optimization problem specifies instances $\mathcal I$, solutions
> $\mathcal S$, feasible sets $\mathcal S_i$, and objective $\Phi$.
>
> For $c\geq1$, a $c$-approximation satisfies
>
> $$
> \Phi(A(i))\leq c\min_{s\in\mathcal S_i}\Phi(s)
> $$
>
> for minimization, and
>
> $$
> \Phi(A(i))\geq\frac1c\max_{s\in\mathcal S_i}\Phi(s)
> $$
>
> for maximization.

> [!Important] Definition - Center-Based Clustering
> A $k$-clustering is $(C_1,\ldots,C_k;S)$, where the $C_i$ partition $P$ and
> $S=\{c_1,\ldots,c_k\}$ is the center set. With
>
> $$
> d(x,S)=\min_{y\in S}d(x,y),
> $$
>
> the principal objectives are
>
> $$
> \Phi_{\mathrm{kcenter}}(P,S)=\max_{x\in P}d(x,S),
> $$
>
> $$
> \Phi_{\mathrm{kmeans}}(P,S)=\sum_{x\in P}d(x,S)^2,
> \qquad
> \Phi_{\mathrm{kmedian}}(P,S)=\sum_{x\in P}d(x,S).
> $$

> [!Important] Definition - Diameter and Diversity
> The diameter of $P$ is
>
> $$
> \Delta(P)=\max_{x,y\in P}d(x,y).
> $$
>
> For $|S|=k$, max-sum diversity is
>
> $$
> \operatorname{div}(S)=\sum_{\{x,y\}\subseteq S}d(x,y).
> $$
>
> A subset $T\subseteq P$ is a $(1+\epsilon)$-coreset for diversity when
>
> $$
> \operatorname{div}^{\mathrm{opt}}(T,k)
> \geq\frac{1}{1+\epsilon}\operatorname{div}^{\mathrm{opt}}(P,k).
> $$

## Additional Coreset and k-Means Results

> [!Important] Guarantee - k-means++
> If $S$ is returned by k-means++, then for $\alpha=\Theta(\ln k)$,
>
> $$
> E[\Phi_{\mathrm{kmeans}}(P,S)]
> \leq\alpha\Phi_{\mathrm{kmeans}}^{\mathrm{opt}}(P,k).
> $$
>
> The lecture also uses the constant-probability form
>
> $$
> \Pr\left(\Phi_{\mathrm{kmeans}}(P,S)
> \leq\alpha\Phi_{\mathrm{kmeans}}^{\mathrm{opt}}(P,k)\right)\geq\frac12.
> $$

> [!Important] Definition - Weighted k-Means
> For weights $w(x)>0$,
>
> $$
> \Phi^w_{\mathrm{kmeans}}(P,S)
> =\sum_{x\in P}w(x)d(x,S)^2.
> $$
>
> Weighted k-means++ samples $x$ with probability proportional to
> $w(x)d(x,S)^2$. Weighted Lloyd's algorithm uses centroid
>
> $$
> \frac{\sum_{x\in C}w(x)x}{\sum_{x\in C}w(x)}.
> $$

> [!Important] Definition - $\gamma$-Coreset for k-Means
> Given proxy map $\tau:P\to T$, $T$ is a $\gamma$-coreset if
>
> $$
> \sum_{p\in P}d(p,\tau(p))^2
> \leq\gamma\Phi_{\mathrm{kmeans}}^{\mathrm{opt}}(P,k).
> $$
>
> Each representative $t\in T$ receives weight
> $w(t)=|\{p\in P:\tau(p)=t\}|$.

> [!Important] Theorem - MR-kmeans Approximation
> Suppose $\mathcal A_1$ is a $\gamma$-approximation for unweighted k-means on
> each partition and $\mathcal A_2$ is an $\alpha$-approximation for weighted
> k-means on the union $T$ of local centers. Then $T$ is a $\gamma$-coreset and
>
> $$
> \Phi_{\mathrm{kmeans}}(P,S)
> =O((1+\gamma)\alpha)
> \Phi_{\mathrm{kmeans}}^{\mathrm{opt}}(P,k).
> $$
>
> Local and aggregate space are
>
> $$
> M_L=O\left(\max\left\{\frac N\ell,\ell k\right\}\right)
> =O(\sqrt{Nk}),
> \qquad M_A=O(N),
> $$
>
> for $\ell=\sqrt{N/k}$.

**Proof.** Let

$$
C=\sum_{p\in P}d(p,\tau(p))^2
\leq\gamma\operatorname{OPT}.
$$

For any center set $Z$, squared triangle inequality gives

$$
\Phi(P,Z)\leq2C+2\Phi^w(T,Z).
$$

Apply this first to optimal centers $S^*$:

$$
\Phi^{w,\mathrm{opt}}(T,k)
\leq\Phi^w(T,S^*)
\leq2C+2\operatorname{OPT}
\leq2(1+\gamma)\operatorname{OPT}.
$$

Since $\mathcal A_2$ is an $\alpha$-approximation,

$$
\begin{aligned}
\Phi(P,S)
&\leq2C+2\Phi^w(T,S)\\
&\leq2\gamma\operatorname{OPT}
+2\alpha\Phi^{w,\mathrm{opt}}(T,k)\\
&\leq\bigl(2\gamma+4\alpha(1+\gamma)\bigr)\operatorname{OPT}\\
&=O(\alpha(1+\gamma))\operatorname{OPT}.
\end{aligned}
$$

## Additional Streaming Results

> [!Important] Definition - Streaming Model
> Input is a one-way stream $\Sigma=x_1,x_2,\ldots$. At each arrival, an algorithm
> updates memory-resident state; a query asks about the prefix seen so far. Standard goals:
> one pass, sublinear memory, $O(1)$ update time, and query time independent of stream length.

> [!Important] Definition - Majority Problem
> Given $\Sigma=x_1,\ldots,x_n$, return an element occurring more than $n/2$ times when
> one exists. Boyer-Moore returns a candidate; an optional second pass verifies it.

> [!Important] Definitions - Sampling and Frequent Items
> An $m$-sample of $n$ items is a size-$m$ subset $S$ satisfying
> $\Pr(x\in S)=m/n$ for every item $x$.
>
> For threshold $\varphi$, frequent-items reporting returns every item with frequency at
> least $\varphi n$. An $\epsilon$-approximate answer must include all such items and must
> exclude every item below $(\varphi-\epsilon)n$.

> [!Important] Definitions - Sketch and Frequency Moments
> A **sketch** is a space-efficient data structure for approximate stream statistics.
> For frequencies $f_u$,
>
> $$
> F_k=\sum_{u\in U}f_u^k,
> $$
>
> where $F_0$ counts distinct items, $F_1=n$, and $F_2$ is the second moment. The Gini
> index is $1-F_2/n^2$.

### Probabilistic Counting Guarantee

> [!Important] Theorem - Flajolet-Martin Constant-Factor Guarantee
> Let
>
> $$
> R=\max_t\operatorname{tr}(h(x_t)),
> \qquad \widetilde F_0=2^R.
> $$
>
> For every $c>2$,
>
> $$
> \Pr(\widetilde F_0<F_0/c)\leq1/c,
> \qquad
> \Pr(\widetilde F_0>cF_0)\leq1/c.
> $$
>
> Hence
>
> $$
> \Pr(F_0/c\leq\widetilde F_0\leq cF_0)\geq1-2/c.
> $$
>
> Space usage is $O(\log|U|)$ bits.

**Upper-tail proof.** For one distinct item,

$$
\Pr(\operatorname{tr}(h(x))\geq j)=2^{-j}.
$$

Union bound over $F_0$ distinct items gives

$$
\Pr(R\geq j)\leq F_0 2^{-j}.
$$

Taking $j=\log_2(cF_0)$ yields

$$
\Pr(\widetilde F_0>cF_0)\leq\frac1c.
$$

The lecture states the symmetric lower-tail bound but does not supply its proof.

> [!Important] Median Trick
> Run $\ell$ independent estimators and return their median. If one estimator has
> one-sided failure probability at most $1/16$, the median fails only when at least half
> the runs fail. Chernoff makes this probability exponentially small in $\ell$; choosing
>
> $$
> \ell=\Theta(\log|U|)
> $$
>
> reduces it to at most $1/|U|$.

### Full Count Sketch Guarantees

> [!Important] Definition - Count-Min Sketch
> A count-min sketch has counters $C[d,w]$ and hashes $h_j:U\to[w]$. On item $x$,
> increment every $C[j,h_j(x)]$. Query
>
> $$
> \widetilde f_u=\min_j C[j,h_j(u)].
> $$
>
> With $w=2/\epsilon$ and $d=\log_2(1/\delta)$, the earlier proof gives
> $0\leq\widetilde f_u-f_u\leq\epsilon n$ with probability at least $1-\delta$.

> [!Important] Definition - Count Sketch
> Count sketch adds sign hashes $g_j:U\to\{-1,+1\}$. Update
>
> $$
> C[j,h_j(x)]\leftarrow C[j,h_j(x)]+g_j(x),
> $$
>
> and query
>
> $$
> \widetilde f_{u,j}=g_j(u)C[j,h_j(u)],
> \qquad
> \widetilde f_u=\operatorname{median}_j\widetilde f_{u,j}.
> $$

> [!Important] Theorem - Count Sketch Frequency Accuracy
> For $d=\log_2(1/\delta)$ and $w=O(1/\epsilon^2)$,
>
> $$
> E[\widetilde f_{u,j}]=f_u,
> $$
>
> and, with probability at least $1-\delta$,
>
> $$
> |\widetilde f_u-f_u|\leq\epsilon\sqrt{F_2}.
> $$
>
> Unbiasedness follows from signed collision terms having expectation zero, as proved in
> the earlier Count Sketch section. Source notes omit proof of the high-probability error
> statement.

> [!Important] Theorem - Count Sketch Estimator for $F_2$
> Define
>
> $$
> \widetilde F_{2,j}=\sum_{r=0}^{w-1}C[j,r]^2,
> \qquad
> \widetilde F_2=\operatorname{median}_j\widetilde F_{2,j}.
> $$
>
> Each row is unbiased:
>
> $$
> E[\widetilde F_{2,j}]=F_2.
> $$
>
> Source notes state the additional guarantee
> $|\widetilde F_2-F_2|\leq\epsilon\sqrt{F_2}$ with probability at least
> $1-\delta$, but omit its proof.

**Unbiasedness proof.** Expanding one row gives

$$
\widetilde F_{2,j}
=\sum_a f_a^2+2\sum_{a<b}
f_af_b g_j(a)g_j(b)\mathbf1[h_j(a)=h_j(b)].
$$

For $a\neq b$, pairwise-independent signs make
$E[g_j(a)g_j(b)]=0$. Every cross term therefore has expectation zero, while the
diagonal sum is $F_2$. By linearity,

$$
E[\widetilde F_{2,j}]=\sum_a f_a^2=F_2.
$$

> [!Important] Definitions - Approximate Membership and Bloom Filter
> Approximate membership must have no false negatives for inserted elements and a small
> false-positive probability for absent elements. A Bloom filter uses an $n$-bit array and
> $k$ hashes; insertion sets all $k$ addressed bits, and query returns positive iff all are
> set. Its false-positive theorem and proof appear in the earlier Bloom Filters section.

### Universal Hash Families

> [!Important] Definition - $k$-Universality
> A family $\mathcal H:U\to[m]$ is $k$-universal if, for distinct
> $x_1,\ldots,x_k$,
>
> $$
> \Pr(h(x_1)=\cdots=h(x_k))\leq\frac1{m^{k-1}}.
> $$
>
> It is strongly $k$-universal if, for all $y_1,\ldots,y_k\in[m]$,
>
> $$
> \Pr\left(\bigwedge_{i=1}^k h(x_i)=y_i\right)=\frac1{m^k}.
> $$

> [!Important] Theorem - Practical 2-Universal Family
> Let $U=[u]$, let prime $p>u$, and define
>
> $$
> h_{a,b}(x)=((ax+b)\bmod p)\bmod m,
> $$
>
> for $a\in\{1,\ldots,p-1\}$ and $b\in\{0,\ldots,p-1\}$. Choosing $(a,b)$
> uniformly gives a 2-universal family.

**Proof.** Fix distinct $x,y<p$. The map

$$
(a,b)\mapsto(ax+b\bmod p,ay+b\bmod p)
$$

is a bijection from admissible $(a,b)$ to ordered pairs of distinct residues $(r,s)$.
Indeed, from $r\neq s$ one uniquely recovers

$$
a=(r-s)(x-y)^{-1}\bmod p,
\qquad b=r-ax\bmod p.
$$

For fixed $r$, at most $\lceil p/m\rceil-1$ residues $s\neq r$ satisfy
$s\bmod m=r\bmod m$. Since

$$
\left\lceil\frac pm\right\rceil-1\leq\frac{p-1}{m},
$$

the collision probability after final reduction is at most $1/m$. This proves
2-universality.

For Mersenne prime $p=2^q-1$,

$$
x\bmod p=((x\bmod2^q)+\lfloor x/2^q\rfloor)\bmod p,
$$

so reduction uses bit masking, shifting, and addition.

## kd-Trees and Exact Similarity Search

> [!Important] Definition - $r$-Near Neighbor Search
> In metric space $(M,d)$, let
>
> $$
> B_r(q)=\{p\in M:d(p,q)\leq r\}.
> $$
>
> Given $P\subseteq M$, an $r$-NNS structure returns a point in $B_r(q)\cap P$ when
> this set is nonempty, and `null` otherwise.

> [!Important] Definition - Range Reporting
> For $P\subseteq\mathbb R^D$ and axis-aligned rectangle
>
> $$
> R=[x_{1,1},x_{1,2}]\times\cdots\times[x_{D,1},x_{D,2}],
> $$
>
> report every point in $P\cap R$.

> [!Important] Definition - kd-tree
> A kd-tree recursively partitions an enclosing rectangle. Each node represents the points
> in its region; leaves contain one point. Splits cycle through coordinates and divide the
> current point set into parts of sizes $\lfloor n/2\rfloor$ and $\lceil n/2\rceil$.

> [!Important] Theorem - Range Reporting in $\mathbb R^2$
> A kd-tree for $n$ points has $O(n\log n)$ construction time, $O(n)$ space, and
>
> $$
> O(\sqrt n+k)
> $$
>
> query time, where $k$ points are reported.

**Proof sketch.** Let $Q_1(R)$ contain visited nodes whose regions intersect but are not
contained in $R$, and let $Q_2(R)$ contain visited nodes whose regions lie inside $R$.
Search visits only $Q_1(R)\cup Q_2(R)$, apart from the root. Standard kd-tree boundary
analysis gives

$$
|Q_1(R)|=O(\sqrt n).
$$

Each node in $Q_2(R)$ contributes reported output and can be charged to one of the $k$
reported points, so $|Q_2(R)|=O(k)$. Hence

$$
T_q=O(1+|Q_1(R)|+|Q_2(R)|)=O(\sqrt n+k).
$$

> [!Important] Theorem - Range Reporting in $\mathbb R^D$
> For fixed dimension $D$, kd-trees use $O(Dn)$ space, take $O(Dn\log n)$ to build,
> and answer a range query in
>
> $$
> O(Dn^{1-1/D}+k).
> $$
>
> As $D$ grows, the exponent approaches 1, expressing the curse of dimensionality.

To reduce $r$-NNS in $\mathbb R^2$ to range reporting, query the smallest square enclosing
$B_r(q)$, then test returned candidates against the ball. Cost depends on all $k_s$ points
in that square, not only the $k_q$ points in the ball:

$$
O(\sqrt n+k_s).
$$

## LSH Families and Amplification

> [!Important] Definition - $(c,r)$-Approximate Near Neighbor Search
> If $B_r(q)\cap P\neq\emptyset$, return some $p\in P$ with $d(p,q)\leq cr$. If the
> ball is empty, return either `null` or such a point. A point farther than $cr$ is never
> legal.

> [!Important] Definition - Locality Sensitive Hashing
> A family $\mathcal H$ is $(c,r,p_1,p_2)$-locality sensitive when $p_1>p_2$ and
>
> $$
> d(p,q)\leq r\implies\Pr(h(p)=h(q))\geq p_1,
> $$
>
> $$
> d(p,q)>cr\implies\Pr(h(p)=h(q))\leq p_2.
> $$

> No condition is imposed for distances in $(r,cr]$.

> [!Important] Theorem - Basic LSH Performance
> One table built from a $(c,r,p_1,p_2)$-LSH family solves $(c,r)$-ANNS with
> success probability at least $p_1$. For $n$ points in $\mathbb R^D$:
>
> | Quantity | Bound |
> |---|---|
> | Construction | $O(Dn)$ |
> | Space | $O(Dn)$ |
> | Expected query | $O(Dnp_2)$ |
>
> Correctness and expected-scan proofs appear in
> [[#Locality-Sensitive Hashing Query Proof|Locality-Sensitive Hashing Query Proof]].

> [!Important] Theorem - Bit Sampling for Hamming Distance
> For $x\in\{0,1\}^D$, choose coordinate $i$ uniformly and set $h_i(x)=x[i]$. Then
>
> $$
> \Pr(h_i(p)=h_i(q))=1-\frac{d_H(p,q)}D.
> $$
>
> Therefore bit sampling is $(c,r,1-r/D,1-cr/D)$-locality sensitive.

**Proof.** Exactly $d_H(p,q)$ of the $D$ coordinates differ. A uniform coordinate differs
with probability $d_H(p,q)/D$, so collision probability is its complement. For a near
pair this is at least $1-r/D$; for a far pair it is below $1-cr/D$.

> [!Important] Definition - LSH $\rho$ Factor
>
> $$
> \rho=\frac{\log_2p_1}{\log_2p_2}
> =\frac{\log_2(1/p_1)}{\log_2(1/p_2)}\in(0,1).
> $$
>
> Smaller $\rho$ is better. Bit sampling has $\rho\sim1/c$.

> [!Important] Definition - Euclidean Random-Projection LSH
> Choose $a\sim N^D(0,1)$, $b$ uniformly in $[0,w]$, and define
>
> $$
> h_{a,b}(p)=\left\lceil\frac{\langle a,p\rangle+b}{w}\right\rceil.
> $$
>
> This gives Euclidean LSH with $\rho=O(1/c)$; stronger families achieve
> $\rho=O(1/c^2)$.

> [!Important] OR Construction - Independent Repetition
> Across $\ell$ independent tables, a near point fails to collide everywhere with
> probability at most $(1-p_1)^\ell$. Therefore success probability is at least
>
> $$
> 1-(1-p_1)^\ell.
> $$

> [!Important] AND Construction - Concatenation
> For $g=(h_1,\ldots,h_k)$ with independent $h_i\in\mathcal H$,
>
> $$
> p_1'=p_1^k,
> \qquad p_2'=p_2^k.
> $$
>
> Choose
>
> $$
> k=\log_{1/p_2}n.
> $$
>
> Then $p_2^k=1/n$ and, by the definition of $\rho$, $p_1^k=n^{-\rho}$. Expected
> far collisions per table are at most 1.

> [!Important] Theorem - Amplified LSH Schema
> Choose
>
> $$
> k=\log_{1/p_2}n,
> \qquad \ell=2p_1^{-k}=2n^\rho.
> $$
>
> Build $\ell$ tables, each using an independent concatenated hash. Then success
> probability is at least $1/2$, with expected bounds
>
> | Quantity | Bound |
> |---|---|
> | Construction | $O(Dn^{1+\rho}\log_{1/p_2}n)$ |
> | Space | $O(Dn+n^{1+\rho}\log_{1/p_2}n)$ |
> | Query | $O(Dn^\rho\log_{1/p_2}n)$ |

**Proof.** In one table, a fixed near point collides with probability at least
$p_1^k=n^{-\rho}$. It misses all tables with probability

$$
(1-p_1^k)^\ell
\leq e^{-\ell p_1^k}
=e^{-2}<\frac12.
$$

Thus success probability exceeds $1/2$. A far point collides in one table with
probability at most $p_2^k=1/n$, so expected far collisions in one table are at most
1 and across all tables at most $\ell=O(n^\rho)$. Computing $k$ component hashes for
each table gives expected query time $O(Dk\ell)$, yielding the displayed bound.
Construction stores each of $n$ points in $\ell$ tables and computes $k$ hashes per
placement; space stores the original points plus table keys and references.

For concatenated bit sampling, selecting $k$ independent coordinates gives

$$
p_1'=(1-r/D)^k,
\qquad p_2'=(1-cr/D)^k,
$$

and leaves $\rho$ unchanged because both logarithms are multiplied by $k$.

## Supplementary Proof Exercises

> [!Example] k-Center Coreset Bound
> Suppose $d(x,T)\leq\epsilon\operatorname{OPT}$ for all $x\in P$, where
> $\operatorname{OPT}=\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k)$, and let
> $S=\operatorname{FFT}(T,k)$. Prove a bound for $\Phi_{\mathrm{kcenter}}(P,S)$.

The FFT separation proof on $T$ can compare its $k+1$ selected/farthest points directly
with the optimal clustering of $P$, because $T\subseteq P$. Hence

$$
\max_{t\in T}d(t,S)\leq2\operatorname{OPT}.
$$

For each $x\in P$, choose $t\in T$ with $d(x,t)\leq\epsilon\operatorname{OPT}$.
Triangle inequality gives

$$
d(x,S)\leq d(x,t)+d(t,S)
\leq(2+\epsilon)\operatorname{OPT}.
$$

> [!Example] Optimal k-Center Cost on a Subset
> For $T\subseteq P$ and $k<|T|,|P|$, prove
> $\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(T,k)
> \leq2\Phi_{\mathrm{kcenter}}^{\mathrm{opt}}(P,k)$ and show tightness.

Let $S^*$ induce optimal clusters of $P$. In each cluster containing points of $T$, choose
one representative of $T$. Any other $t\in T$ in that cluster is within
$2\operatorname{OPT}$ of its representative by triangle inequality. At most $k$
representatives are needed, proving the bound. It is tight for
$P=\{-1,0,1\}$, $T=\{-1,1\}$, and $k=1$ when centers must belong to the input:
$\operatorname{OPT}(P,1)=1$ but $\operatorname{OPT}(T,1)=2$.

> [!Example] k-means++ Probability Amplification
> Run $t$ independent copies and return the solution with smallest objective. Each copy
> succeeds with probability at least $1/2$.

All copies fail with probability at most $2^{-t}$. Therefore

$$
t=\lceil\log_2N\rceil
$$

gives failure probability at most $1/N$ and success probability at least $1-1/N$.

> [!Example] Merge Two Reservoir Samples
> Let $S_1,S_2$ be independent $m$-samples from disjoint streams of equal length $n$.
> Choose a uniform size-$m$ subset $S$ of $S_1\cup S_2$.

For any original item $x$,

$$
\Pr(x\in S)
=\Pr(x\in S_i)\Pr(x\text{ selected}\mid x\in S_i)
=\frac mn\cdot\frac m{2m}
=\frac m{2n}.
$$

Thus $S$ is an $m$-sample of the concatenated length-$2n$ stream.

> [!Example] Unbiased Color-Count Estimator
> Let $S$ be an $m$-sample from $n$ red/blue items, let $R$ be the number of red items,
> and let $X_S$ count red sampled items.

For each red item $i$, let $I_i=1$ when sampled. Then

$$
X_S=\sum_{i=1}^R I_i,
\qquad E[I_i]=\frac mn.
$$

By linearity,

$$
E\left[\frac nmX_S\right]
=\frac nm\sum_{i=1}^R E[I_i]
=\frac nm\,R\frac mn
=R.
$$

## Summary Table

| Topic | Main result | Cost / Bound | Key proof idea |
|---|---|---|---|
| MTBF | $E[X] = 1/(1-(1-p)^N)$ | Geometric waiting time | Independent component failures |
| Word count | One MapReduce round computes global counts | $M_L = O(N_{\max}+K)$, $M_A=O(N)$ | Local counts, then sum by word |
| Class count | Two-round load reduction | $O(N/\ell)$ first-round load | Partition, then aggregate |
| Random partitioning | $m=O(\sqrt{N})$ w.h.p. | Failure probability $<1/N^5$ | Chernoff plus union bound |
| FFT | 2-approximation for $k$-center | $\Phi(P,S)\leq2\Phi^{\text{opt}}(P,k)$ | Pigeonhole over $k+1$ far-apart points |
| MR-FFT | Distributed $k$-center | $M_L=O(\sqrt{Nk})$ | Representatives plus triangle inequality |
| Diversity coreset | Preserves near-optimal diversity | $(1-\epsilon)$ approximation when $R$ is small | Proxy mapping inside clusters |
| MR-kmeans | Distributed weighted coreset solution | $O(\alpha(1+\gamma))$ approximation | Proxy cost plus squared triangle inequality |
| Boyer-Moore | Finds majority element if one exists | $O(1)$ memory, one pass | Cancel pairs of distinct elements |
| Reservoir sampling | Maintains uniform $m$-sample | $P[x_i \in S_t]=m/t$ | Induction on stream time |
| Sticky sampling | Approximate frequent items | $O((1/\epsilon)\ln(1/\delta))$ expected memory | Sampling plus union bound |
| Flajolet-Martin | Estimates distinct count $F_0$ | $c$-factor w.p. $1-2/c$ | Trailing-zero tail plus union bound |
| Count-min sketch | One-sided frequency estimates | Error $\leq \epsilon n$ w.p. $1-\delta$ | Markov, then min over rows |
| Count sketch | Frequency and $F_2$ estimates | Frequency error $\epsilon\sqrt{F_2}$ w.p. $1-\delta$ | Signed collisions have expectation $0$ |
| Bloom filters | False positive probability | $(1-e^{-km/n})^k$ | Probability a queried bit is set |
| Universal hashing | Practical pairwise-independent family | Collision probability $\leq1/m$ | Affine bijection modulo prime $p$ |
| kd-tree | Exact range reporting | $O(\sqrt n+k)$ in $\mathbb R^2$ | Boundary nodes plus output nodes |
| Basic LSH | Approximate near-neighbor query | Expected scan $1+np_2$ | Near collision $p_1$, far collision $p_2$ |
| Amplified LSH | Sublinear ANNS query | $O(Dn^\rho\log_{1/p_2}n)$ expected | AND reduces noise; OR restores success |
