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
> O\left(\frac{1}{\epsilon}\ln\frac{1}{\delta}\right).
> $$

**Working memory.** The working memory is proportional to the number of sampled
items stored in $S$. If an item contributes an extra stored counter with
probability $r/n$, then the expected number of stored counters is

$$
O\left(n\cdot\frac{r}{n}\right) = O(r).
$$

With

$$
r = \Theta\left(\frac{1}{\epsilon}\ln\frac{1}{\delta}\right),
$$

the expected memory bound follows.

**Correctness idea.** For a truly frequent item $a$, the probability that none
of its occurrences is sampled is bounded by

$$
\left(1-\frac{r}{n}\right)^{f_a}
\leq e^{-rf_a/n}.
$$

Choosing $r$ large enough makes this probability small. A union bound over all
frequent items gives probability at most $\delta$ that some frequent item is
missed. False positives are avoided by returning only items whose estimated
count is at least $(\phi-\epsilon)n$.

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
| Boyer-Moore | Finds majority element if one exists | $O(1)$ memory, one pass | Cancel pairs of distinct elements |
| Reservoir sampling | Maintains uniform $m$-sample | $P[x_i \in S_t]=m/t$ | Induction on stream time |
| Sticky sampling | Approximate frequent items | $O((1/\epsilon)\ln(1/\delta))$ expected memory | Sampling plus union bound |
| Flajolet-Martin | Estimates distinct count $F_0$ | $2^R$ from max trailing zeros | $P[\operatorname{tz}\geq j]=2^{-j}$ |
| Count-min sketch | One-sided frequency estimates | Error $\leq \epsilon n$ w.p. $1-\delta$ | Markov, then min over rows |
| Count sketch | Unbiased signed estimates | Median reduces error probability | Symmetric signed collisions have expectation $0$ |
| Bloom filters | False positive probability | $(1-e^{-km/n})^k$ | Probability a queried bit is set |
| LSH | Approximate near-neighbor query | Expected scan $1+np_2$ | Near collision prob. $p_1$, far collision prob. $p_2$ |
