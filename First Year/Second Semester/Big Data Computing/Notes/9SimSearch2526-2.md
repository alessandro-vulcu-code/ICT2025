# Similarity Search (Part 2)

## Table of Contents

- [[#High-Dimensional Similarity Search|High-Dimensional Similarity Search]]
  - [[#Approximation Effects|Approximation Effects]]
  - [[#Approximate Near Neighbor Search|Approximate Near Neighbor Search]]
  - [[#ANNS Examples|ANNS Examples]]
- [[#Locality Sensitive Hashing|Locality Sensitive Hashing]]
  - [[#Core Idea|Core Idea]]
  - [[#LSH Definition|LSH Definition]]
  - [[#Basic LSH Data Structure|Basic LSH Data Structure]]
  - [[#Boolean-Vector Example|Boolean-Vector Example]]
  - [[#Basic LSH Performance|Basic LSH Performance]]
- [[#LSH Families|LSH Families]]
  - [[#Hamming Distance Bit Sampling|Hamming Distance: Bit Sampling]]
  - [[#The Rho Factor|The Rho Factor]]
  - [[#Euclidean Distance Random Projection|Euclidean Distance: Random Projection]]
- [[#Improving Collision Probabilities|Improving Collision Probabilities]]
  - [[#Repetition OR Construction|Repetition: OR Construction]]
  - [[#Concatenation AND Construction|Concatenation: AND Construction]]
  - [[#Combined LSH Schema|Combined LSH Schema]]
  - [[#Combined-Schema Performance|Combined-Schema Performance]]
- [[#Concatenated Bit Sampling|Concatenated Bit Sampling]]
- [[#Exercises|Exercises]]
- [[#Final Summary|Final Summary]]
- [[#References|References]]

This lecture continues Part 1, which introduced exact similarity search, kd-trees, and the
curse of dimensionality. Part 2 studies **Approximate Near Neighbor Search** and
**Locality Sensitive Hashing** for high-dimensional data.

## High-Dimensional Similarity Search

### Approximation Effects

Approximation tackles the curse of dimensionality by relaxing exact $r$-NNS answers. For a
query point $q$ and radius $r$, two errors are possible:

- **False positive:** the returned point $p$ has $d(p,q)>r$. This is acceptable only when
  $d(p,q)$ is not much larger than $r$.
- **False negative:** no $r$-near neighbor is returned even though one exists. This should be
  avoided.

The approximation model therefore permits controlled false positives but preserves a
probabilistic guarantee against false negatives.

### Approximate Near Neighbor Search

> [!Important] Definition - $(c,r)$-Approximate Near Neighbor Search
> **Statement:** Given a set $P$ of $n$ points from metric space $(M,d)$, construct a data
> structure that, for query point $q\in M$, threshold $r>0$, and constant $c\geq1$, behaves as
> follows:
>
> - If $B_r(q)\cap P\neq\emptyset$, return a point $p\in P$ satisfying $d(p,q)\leq cr$.
> - If $B_r(q)\cap P=\emptyset$, return either `null` or a point $p\in P$ satisfying
>   $d(p,q)\leq cr$, if one exists.
>
> In the second case, `null` is always valid, even if a point within distance $cr$ exists.
>
> **Guarantee:** The structure never returns a point farther than $cr$ from $q$.
>
> **Intuition:** Radius $r$ identifies genuinely near points; $cr$ is the largest acceptable
> distance for an approximate answer.

### ANNS Examples

> [!Example] Near Points Exist
> Points $A$, $B$, $C$, and $D$ are legal outputs. At least one point lies inside radius $r$,
> and all four candidates lie inside radius $cr$.

![[ToSummarize/9SimSearch2526-2_images/page-006-near-points.png]]
*Figure 1 - $(c,r)$-ANNS instance with near points; all marked points inside radius $cr$ are legal outputs.*

> [!Example] No Near Point Exists
> No point lies inside radius $r$. Points $A$ and $B$ lie inside radius $cr$, so legal outputs
> are $A$, $B$, or `null`.

![[ToSummarize/9SimSearch2526-2_images/page-007-no-near-points.png]]
*Figure 2 - Instance with no point in $B_r(q)$ but two points within distance $cr$.*

> [!Example] Only Far Points Exist
> Every point lies outside radius $cr$. The only legal answer is `null`.

![[ToSummarize/9SimSearch2526-2_images/page-008-only-far-points.png]]
*Figure 3 - Instance containing only points too far from $q$ to be returned.*

## Locality Sensitive Hashing

### Core Idea

*Locality Sensitive Hashing* (LSH), introduced in the late 1990s, is widely used for
high-dimensional near-neighbor search in recommender systems, duplicate or plagiarism
detection, and search engines.

Its main ideas are:

- Randomly select a hash function $h$ from a suitable family $\mathcal{H}$ to partition the
  space into regions.
- Make near points likely to map to the same region.
- Make far points likely to map to different regions.
- Search for neighbors of query $q$ only in the region identified by $h(q)$.

Standard hashing tries to minimize collisions between arbitrary elements. LSH instead makes
collision probability positively related to similarity.

### LSH Definition

Consider a metric space $(M,d)$ and a hash family

$$
\mathcal{H}=\{h:M\rightarrow S\},
$$

where $S$ is a domain such as integer range $[0,t]$. For $p,q\in M$,

$$
\Pr_{h\in\mathcal{H}}[h(p)=h(q)]
$$

denotes the probability that a uniformly random $h\in\mathcal{H}$ maps $p$ and $q$ to the
same value.

> [!Important] Definition - $(c,r,p_1,p_2)$-Locality Sensitive Hashing
> Given $c>1$, $r>0$, and $p_1,p_2\in[0,1]$ with $p_1>p_2$, family $\mathcal{H}$ is
> **$(c,r,p_1,p_2)$-locality sensitive** if, for all $p,q\in M$:
>
> - if $d(p,q)\leq r$, then
>   $\Pr_{h\in\mathcal{H}}[h(p)=h(q)]\geq p_1$;
> - if $d(p,q)>cr$, then
>   $\Pr_{h\in\mathcal{H}}[h(p)=h(q)]\leq p_2$.
>
> **Unspecified region:** No collision guarantee is imposed when $d(p,q)\in(r,cr]$.
>
> **Intuition:** $p_1$ lower-bounds collisions of near pairs, while $p_2$ upper-bounds
> collisions of far pairs.

Collision probability is usually a monotonically decreasing function of distance.

![[ToSummarize/9SimSearch2526-2_images/page-011-collision-probability.png]]
*Figure 4 - Example collision probability decreasing with normalized Hamming distance.*

### Basic LSH Data Structure

A $(c,r,p_1,p_2)$-LSH family directly yields a basic $(c,r)$-ANNS data structure.

> [!Important] Algorithm - Basic LSH for $(c,r)$-ANNS
> **Construction:**
>
> 1. Select $h$ uniformly at random from $\mathcal{H}$.
> 2. Create hash table $T$ whose buckets are implemented as lists.
> 3. Insert every $p\in P$ into bucket
>
>    $$
>    T[h(p)].
>    $$
>
> Thus,
>
> $$
> T[j]=\{p\in P:h(p)=j\}.
> $$
>
> **Query:** Given $q$, scan $T[h(q)]$. Return the first point $p$ satisfying
> $d(p,q)\leq cr$; return `null` if no such point exists.
>
> ```text
> BuildBasicLSH(P, H):
>     choose h uniformly at random from H
>     initialize empty hash table T
>     for each p in P:
>         append p to T[h(p)]
>     return (h, T)
>
> QueryBasicLSH(q, h, T, c, r):
>     for each p in T[h(q)]:
>         if d(p, q) <= c*r:
>             return p
>     return null
> ```

### Boolean-Vector Example

Let

$$
M=\{\text{Boolean vectors of length }9\}
$$

with Hamming distance. Input $P\subset M$ contains $n=8$ vectors.

![[ToSummarize/9SimSearch2526-2_images/page-013-boolean-vectors.png]]
*Figure 5 - Eight Boolean vectors in input set $P$.*

For $0\leq i<j<8$, let $h_{i,j}:M\rightarrow[0,3]$ map vector $x$ to the integer represented
by bits $x[i]x[j]$. Define

$$
\mathcal{H}=\{h_{i,j}:0\leq i<j<8\}.
$$

The source uses vectors of length $9$ but index condition $j<8$ (note: possible transcription
artifact; zero-based indexing over all nine positions would normally allow $j<9$).

Suppose $h_{1,2}$ is selected. Query $q$ hashes to bucket $3$. The annotation distinguishes
outputs legal for every $c\geq1$ from additional outputs legal only when $c\geq2$.

![[ToSummarize/9SimSearch2526-2_images/page-014-hash-table-example.png]]
*Figure 6 - Hash-table construction and query for the Boolean-vector example.*

For a query $q$, bucket $T[h(q)]$ behaves as follows:

- A near point $p$ with $d(p,q)\leq r$ appears in the bucket with probability at least $p_1$.
- A far point $p'$ with $d(p',q)>cr$ appears in the bucket with probability at most $p_2$.

In the worst case, $P$ contains one near point and $n-1$ far points. At most $np_2$ far
points collide with $q$ in expectation.

### Basic LSH Performance

Assume metric space $(M,d)$ has dimensionality $D$, each point requires $O(D)$ words, and hash
values and distances can be computed in $O(D)$ time.

> [!Important] Theorem - Performance of Basic LSH
> Let $P$ contain $n$ points in a $D$-dimensional metric space, and let $\mathcal{H}$ be a
> $(c,r,p_1,p_2)$-locality-sensitive family. Basic LSH answers a query successfully with
> probability at least $p_1$ and has:
>
> | Quantity | Bound |
> |---|---|
> | Construction time | $O(Dn)$ |
> | Space | $O(Dn)$ |
> | Expected query time | $O(Dnp_2)$ |

#### Proof of Probabilistic Correctness

**Case 1:** $B_r(q)\cap P\neq\emptyset$.

Any returned point $p'$ with $d(p',q)\leq cr$ is legal. Choose an arbitrary
$p\in B_r(q)\cap P$. Since $\mathcal{H}$ is locality sensitive,

$$
\begin{aligned}
\Pr_h[\text{answer is correct}]
&\geq \Pr_h[\text{answer}\neq\texttt{null}]\\
&\geq \Pr_h[h(p)=h(q)]\\
&\geq p_1.
\end{aligned}
$$

![[ToSummarize/9SimSearch2526-2_images/page-017-performance-proof-1.png]]
*Figure 7 - First part of the handwritten proof: correctness when an $r$-near point exists.*

**Case 2:** $B_r(q)\cap P=\emptyset$.

Every possible answer is correct: either `null`, or a point $p$ with $d(p,q)\leq cr$.
Construction time and space follow directly from hashing and storing all $n$ points.

The query scans $T[h(q)]$ until it finds a point within distance $cr$ or reaches the end of
the list.

![[ToSummarize/9SimSearch2526-2_images/page-018-performance-proof-2.png]]
*Figure 8 - Second part of the handwritten proof: the empty-ball case and cost setup.*

#### Proof of Expected Query Time

Let $x$ be the number of far points $p\in P$ satisfying

$$
d(p,q)>cr
\qquad\text{and}\qquad
h(p)=h(q).
$$

Query time is $O(Dx)$. For each far point, collision probability is at most $p_2$, so

$$
\mathbb{E}[x]\leq np_2.
$$

Therefore,

$$
\mathbb{E}[\text{query time}]=O(Dnp_2).
$$

![[ToSummarize/9SimSearch2526-2_images/page-019-performance-proof-3.png]]
*Figure 9 - Final part of the handwritten expected-query-time proof.*

## LSH Families

### Hamming Distance Bit Sampling

Let

$$
M=\{\text{Boolean vectors of length }D\}.
$$

For $0\leq i<D$, define $h_i:M\rightarrow\{0,1\}$ by $h_i(x)=x[i]$, and let

$$
\mathcal{H}_H=\{h_i:0\leq i<D\}.
$$

For points $p,q$, a uniformly random coordinate agrees with probability

$$
\Pr_{h\in\mathcal{H}_H}[h(p)=h(q)]
=1-\frac{d_H(p,q)}{D},
$$

where $d_H$ is Hamming distance.

> [!Important] Proposition - Bit Sampling Is Locality Sensitive
> If $d_H(p,q)\leq r$, then
>
> $$
> \Pr_{h\in\mathcal{H}_H}[h(p)=h(q)]
> =1-\frac{d_H(p,q)}{D}
> \geq1-\frac{r}{D}
> \stackrel{\mathrm{def}}{=}p_1.
> $$
>
> If $d_H(p,q)>cr$, then
>
> $$
> \Pr_{h\in\mathcal{H}_H}[h(p)=h(q)]
> =1-\frac{d_H(p,q)}{D}
> <1-\frac{cr}{D}
> \stackrel{\mathrm{def}}{=}p_2.
> $$
>
> Therefore, $\mathcal{H}_H$ is
> $(c,r,1-r/D,1-cr/D)$-locality sensitive.

### The Rho Factor

A locality-sensitive family is effective when $p_1\gg p_2$. Its quality is measured by

$$
\rho
=\frac{\log_2p_1}{\log_2p_2}
=\frac{\log_2(1/p_1)}{\log_2(1/p_2)}.
$$

Because $1\geq p_1>p_2>0$, it follows that $\rho\in(0,1)$. As $p_1/p_2$ increases,
$\rho$ decreases, so a smaller $\rho$ is better.

For bit sampling,

$$
\rho
=\frac{\log_2(1-r/D)}{\log_2(1-cr/D)}
\sim\frac{r/D}{cr/D}
=\frac{1}{c}.
$$

> [!Important] Design Goal - Minimize $\rho$
> Factor $\rho$ controls final LSH exponents in space and query time. Better separation between
> near-pair and far-pair collision probabilities produces smaller $\rho$ and faster search.

### Euclidean Distance Random Projection

Let $M=\mathbb{R}^D$. For fixed $w>0$, vector $a\in\mathbb{R}^D$, and offset
$b\in[0,w]$, define $h_{a,b}:M\rightarrow\mathbb{Z}$ by

$$
h_{a,b}(p)
=\left\lfloor\frac{\langle a,p\rangle+b}{w}\right\rfloor,
$$

where $\langle\cdot,\cdot\rangle$ is the inner product. Define

$$
\mathcal{H}_E(w)
=\{h_{a,b}:a\in\mathbb{R}^D,\ b\in[0,w]\}.
$$

If $a$ is sampled from $\mathcal{N}^D(0,1)$ and $b$ uniformly from $[0,w]$, then
$\mathcal{H}_E(w)$ is $(c,r,p_1,p_2)$-locality sensitive with

$$
\rho=O(1/c).
$$

#### Practical Bucket Implementation

Functions in $\mathcal{H}_E(w)$ map points to arbitrary integers. In practice, after selecting
$h_{a,b}$, a secondary hash function maps nonempty primary buckets to a small index range. For
query $q$, the implementation retrieves the candidates sharing the secondary index of
$h_{a,b}(q)$ and searches the relevant primary bucket for a near neighbor.

Better Euclidean LSH families achieve

$$
\rho\in O(1/c^2).
$$

![[ToSummarize/9SimSearch2526-2_images/page-027-euclidean-observations-1.png]]
*Figure 10 - First handwritten implementation observation for Euclidean LSH.*

![[ToSummarize/9SimSearch2526-2_images/page-028-euclidean-observations-2.png]]
*Figure 11 - Continuation and stronger Euclidean $\rho$ bound.*

#### Random-Projection Example

The following sequence shows the geometric meaning of $h_{a,b}$:

1. Choose projection direction $a$.
2. Project each point orthogonally onto the line in direction $a$.
3. Divide the line into intervals of width $w$.
4. Hash query $q$ according to the interval containing its projection.

![[ToSummarize/9SimSearch2526-2_images/page-029-random-projection-1.png]]
*Figure 12 - Input points and random direction $a$ before projection.*

![[ToSummarize/9SimSearch2526-2_images/page-030-random-projection-2.png]]
*Figure 13 - Orthogonal projections of points onto direction $a$.*

![[ToSummarize/9SimSearch2526-2_images/page-031-random-projection-3.png]]
*Figure 14 - Projected line partitioned into intervals of width $w$.*

![[ToSummarize/9SimSearch2526-2_images/page-032-random-projection-4.png]]
*Figure 15 - Query point $q$ added to the random-projection example.*

## Improving Collision Probabilities

Ideal LSH has $p_1$ close to $1$ and $p_2$ close to $0$. When one family does not provide
this separation, two amplification techniques can be combined:

| Technique | Construction | Main effect | Cost |
|---|---|---|---|
| **Repetition / OR** | Use $\ell$ independent tables | Increases near-point success probability | More buckets checked |
| **Concatenation / AND** | Combine $k$ independent hashes per table | Decreases far-point collision probability | More hashes computed per table |

### Repetition OR Construction

Repeat search $\ell>1$ times using $\ell$ hash tables built from independent functions selected
uniformly from $\mathcal{H}$.

Let $p$ satisfy $d(p,q)\leq r$.

- In one table, probability that $p$ and $q$ occupy different buckets is at most $1-p_1$.
- By independence, probability that they differ in all $\ell$ tables is at most
  $(1-p_1)^\ell$.
- Hence, probability that they collide in at least one table is at least

$$
1-(1-p_1)^\ell.
$$

For $\ell>1$,

$$
(1-p_1)^\ell<1-p_1,
$$

and therefore

$$
1-(1-p_1)^\ell>p_1.
$$

![[ToSummarize/9SimSearch2526-2_images/page-035-repetition-proof-1.png]]
*Figure 16 - First part of the handwritten OR-construction analysis.*

![[ToSummarize/9SimSearch2526-2_images/page-036-repetition-proof-2.png]]
*Figure 17 - Completion of the handwritten repetition inequality.*

### Concatenation AND Construction

Form family $\mathcal{G}$ by concatenating $k\geq1$ independent functions selected uniformly
from $\mathcal{H}$:

$$
\mathcal{G}
=\left\{g\in\mathcal{H}^k:
g(p)=(h_1(p),\ldots,h_k(p)),\ h_i\in\mathcal{H}\right\}.
$$

For random $g\in\mathcal{G}$ and distinct $p,q$:

- if $d(p,q)\leq r$, then $\Pr[g(p)=g(q)]\geq p_1^k$;
- if $d(p,q)>cr$, then $\Pr[g(p)=g(q)]\leq p_2^k$.

Choose

$$
k=\log_{1/p_2}n
=\frac{\log_2n}{\log_2(1/p_2)}.
$$

Then:

- for near pairs, collision probability is at least

  $$
  p_1^k=\frac{1}{n^\rho};
  $$

- for far pairs, collision probability is at most

  $$
  p_2^k=\frac{1}{n}.
  $$

Thus, expected number of far-point collisions with a query in one concatenated table is at most
$1$.

The identity $p_1^k=n^{-\rho}$ follows from

$$
\begin{aligned}
k
&=\frac{\log_2n}{\log_2(1/p_2)}\\
&=\frac{\log_2n}{\log_2(1/p_1)}
  \frac{\log_2(1/p_1)}{\log_2(1/p_2)}\\
&=\rho\log_{1/p_1}n.
\end{aligned}
$$

Equivalently,

$$
p_1^{-k}=n^\rho.
$$

![[ToSummarize/9SimSearch2526-2_images/page-040-concatenation-derivation.png]]
*Figure 18 - Handwritten derivation connecting $k$, $p_1$, and $\rho$.*

### Combined LSH Schema

Combine $k$-way concatenation with $\ell$ independent repetitions.

> [!Important] Algorithm - Amplified LSH for $(c,r)$-ANNS
> **Construction:**
>
> 1. Construct $\ell$ independent functions $g_1,\ldots,g_\ell$.
> 2. Each $g_i$ concatenates $k$ functions sampled independently from $\mathcal{H}$.
> 3. For each $g_i$, build hash table $T_i$ for all points in $P$.
> 4. Bucket $T_i[j]$ contains all $p\in P$ satisfying $g_i(p)=j$.
>
> **Query:** Scan
>
> $$
> T_1[g_1(q)],\ldots,T_\ell[g_\ell(q)]
> $$
>
> until finding a point $p$ with $d(p,q)\leq cr$. Return it, or return `null` if no such
> point is found.
>
> ```text
> BuildAmplifiedLSH(P, H, k, ell):
>     for i = 1 to ell:
>         choose h_i,1, ..., h_i,k independently from H
>         define g_i(p) = (h_i,1(p), ..., h_i,k(p))
>         initialize table T_i
>         for each p in P:
>             append p to T_i[g_i(p)]
>     return {(g_i, T_i)} for i = 1, ..., ell
>
> QueryAmplifiedLSH(q, tables, c, r):
>     for i = 1 to ell:
>         for each p in T_i[g_i(q)]:
>             if d(p, q) <= c*r:
>                 return p
>     return null
> ```

The lecture animation incrementally adds tables $T_1,T_2,T_3,\ldots,T_i,\ldots,T_\ell$. The
final accumulated diagram is shown below.

![[ToSummarize/9SimSearch2526-2_images/page-048-lsh-schema.png]]
*Figure 19 - Combined LSH schema with $\ell$ tables and $k$ concatenated hashes per table.*

### Combined-Schema Performance

> [!Important] Theorem - Amplified LSH Performance
> Let $P$ contain $n$ points in metric space $(M,d)$, and let $\mathcal{H}$ be a
> $(c,r,p_1,p_2)$-locality-sensitive family. Set
>
> $$
> k=\log_{1/p_2}n
> \qquad\text{and}\qquad
> \ell=2p_1^{-k}=2n^\rho,
> $$
>
> where
>
> $$
> \rho=\frac{\log_2p_1}{\log_2p_2}.
> $$
>
> A query succeeds with probability at least $1/2$. Performance is:
>
> | Quantity | Bound |
> |---|---|
> | Construction time | $O\!\left(Dn^{1+\rho}\log_{1/p_2}n\right)$ |
> | Space | $O\!\left(Dn+n^{1+\rho}\log_{1/p_2}n\right)$ |
> | Expected query time | $O\!\left(Dn^\rho\log_{1/p_2}n\right)$ |
>
> **Reasoning:** Concatenation makes expected far collisions per table at most $1$.
> Repetition uses $\ell=2n^\rho$ independent tables to restore constant success probability.
> Parameter $k=\log_{1/p_2}n$ contributes the logarithmic factor to hash evaluation and
> storage.

## Concatenated Bit Sampling

Concatenating $k$ bit-sampling hashes selects $k$ random coordinates. It yields:

- if $d_H(p,q)\leq r$,

  $$
  \Pr[h(p)=h(q)]\geq(1-r/D)^k;
  $$

- if $d_H(p,q)\geq cr$,

  $$
  \Pr[h(p)=h(q)]\leq(1-cr/D)^k.
  $$

Concatenation does not change $\rho$.

Bit sampling is a projection onto a random subset of dimensions:

```text
x       00101001010        y       10101100010
h(x)    011                h(y)    011
```

Increasing $k$ makes collision probability decrease more rapidly with relative Hamming
distance.

![[ToSummarize/9SimSearch2526-2_images/page-055-bit-sampling-chart.png]]
*Figure 20 - Bit-sampling collision probability for $k=1$ and $k=3$, with thresholds $r$ and $cr$.*

## Exercises

> [!Example] Exercise 1 - Similar Documents
> **Problem:** Let $P$ be a collection of $n$ documents. Let $W$ contain $D$ relevant words,
> and suppose similarity depends on how many words from $W$ two documents share, ignoring
> relative frequencies.
>
> 1. Describe a document representation and a data structure for $P$ based on a suitable
>    locality-sensitive family, using only one hash function.
> 2. Find $c$ and $r$ such that $(c,r)$-ANNS is solved correctly with probability at least
>    $1/2$ and expected query time $O(n)$. The trivial exact method costs $O(Dn)$ per query.
>
> **Source status:** The lecture states this exercise but does not provide a worked solution.

> [!Example] Exercise 2 - Searching for a Far Vector
> **Problem:** Let $P$ contain $n$ Boolean vectors of dimension $D$, stored in hash table $T$
> using a random bit-sampling hash $h$ from
> $\mathcal{H}=\{h_i:0\leq i<D\}$. Let $\operatorname{not}(h(x))$ denote negation of binary
> value $h(x)$.
>
> 1. Given $p$ and $q$, determine
>    $\Pr_{h\in\mathcal{H}}[h(p)=\operatorname{not}(h(q))]$ as a function of $d_H(p,q)$.
> 2. Given query $q$, find an $r$-far point $p\in P$, meaning $d_H(p,q)\geq r$. Explain how to
>    search efficiently in $T$ and state the probabilistic guarantees.
>
> **Source status:** The lecture states this exercise but does not provide a worked solution.

## Final Summary

| Technique / Concept | Definition or guarantee | Cost / role |
|---|---|---|
| $(c,r)$-ANNS | If an $r$-near point exists, return one within distance $cr$ | Controlled false positives; avoid false negatives probabilistically |
| $(c,r,p_1,p_2)$-LSH | Near collision probability $\geq p_1$; far probability $\leq p_2$ | Converts similarity into hash collisions |
| Basic LSH | One random hash table | Success $\geq p_1$; expected query $O(Dnp_2)$ |
| Hamming bit sampling | $h_i(x)=x[i]$ | Collision $1-d_H(p,q)/D$ |
| Bit-sampling parameters | $p_1=1-r/D$, $p_2=1-cr/D$ | $\rho\sim1/c$ |
| $\rho$ factor | $\log(1/p_1)/\log(1/p_2)$ | Smaller $\rho$ gives better exponents |
| Euclidean random projection | $\left\lfloor(\langle a,p\rangle+b)/w\right\rfloor$ | Random projected buckets; $\rho=O(1/c)$ |
| Improved Euclidean LSH | Better locality-sensitive families | $\rho=O(1/c^2)$ |
| Repetition / OR | $\ell$ independent tables | Near collision $\geq1-(1-p_1)^\ell$ |
| Concatenation / AND | $k$ hashes per table | Near $\geq p_1^k$; far $\leq p_2^k$ |
| Parameter $k$ | $\log_{1/p_2}n$ | Makes far collision probability at most $1/n$ |
| Parameter $\ell$ | $2p_1^{-k}=2n^\rho$ | Restores success probability to at least $1/2$ |
| Amplified LSH query | Scan $\ell$ concatenated-hash buckets | Expected $O(Dn^\rho\log_{1/p_2}n)$ |
| Amplified LSH space | Store $\ell$ tables | $O(Dn+n^{1+\rho}\log_{1/p_2}n)$ |

## References

- **[LRU14]** J. Leskovec, A. Rajaraman, and J. Ullman. *Mining Massive Datasets*.
  Cambridge University Press, 2014. Section 3.6.
- **[BCKO08]** Mark de Berg, Otfried Cheong, Marc van Kreveld, and Mark Overmars.
  *Computational Geometry: Algorithms and Applications*, 3rd ed. Springer-Verlag, 2008.
  Section 5.2.
- **[AI08]** Alexandr Andoni and Piotr Indyk. "Near-optimal hashing algorithms for approximate
  nearest neighbor in high dimensions." *Communications of the ACM* 51(1), 2008.
