# Similarity Search (Part 2)

## Table of Contents

- [[#High-Dimensional Similarity Search|High-Dimensional Similarity Search]]
  - [[#From Exact r-NNS to Approximation|From Exact r-NNS to Approximation]]
  - [[#c-r-Approximate Near Neighbor Search|c-r-Approximate Near Neighbor Search]]
- [[#Locality Sensitive Hashing|Locality Sensitive Hashing]]
  - [[#Definition of LSH|Definition of LSH]]
  - [[#Solving c-r-ANNS with LSH|Solving c-r-ANNS with LSH]]
  - [[#Basic LSH Data Structure and Performance|Basic LSH Data Structure and Performance]]
- [[#LSH Families for Common Distances|LSH Families for Common Distances]]
  - [[#Bit Sampling for Hamming Distance|Bit Sampling for Hamming Distance]]
  - [[#Random Projection for Euclidean Distance|Random Projection for Euclidean Distance]]
- [[#Improving the Data Structure|Improving the Data Structure]]
  - [[#OR Construction Repetition|OR Construction Repetition]]
  - [[#AND Construction Concatenation|AND Construction Concatenation]]
  - [[#General LSH Schema for c-r-ANNS|General LSH Schema for c-r-ANNS]]
- [[#Concatenating Bit Sampling|Concatenating Bit Sampling]]
- [[#Exercises|Exercises]]
- [[#Summary|Summary]]
- [[#References|References]]
- [[#Final Summary Table|Final Summary Table]]

![[Pics/SimSearch2/SimSearch2-01.png]]
*Figure 1 - Title slide for Similarity Search, Part 2.*

![[Pics/SimSearch2/SimSearch2-02.png]]
*Figure 2 - Lecture outline: exact similarity search from Part 1, then approximate near neighbor search and Locality Sensitive Hashing.*

## High-Dimensional Similarity Search

![[Pics/SimSearch2/SimSearch2-03.png]]
*Figure 3 - Section divider introducing similarity search in high dimensions.*

### From Exact $r$-NNS to Approximation

![[Pics/SimSearch2/SimSearch2-04.png]]
*Figure 4 - Motivation for approximation in high-dimensional $r$-NNS.*

The **curse of dimensionality** can be tackled by resorting to approximate
approaches.

For an $r$-NNS query with query point $q$ and radius $r$, approximation can
affect the output in two ways:

| Approximation effect | Meaning | Acceptable? |
|---|---|---|
| False positive | The returned point $p$ has distance $> r$ from $q$ | Acceptable only if $d(p,q)$ is not too much larger than $r$ |
| False negative | No $r$-near neighbor is returned while one exists | Should be avoided |

The main objective is therefore to allow controlled false positives while avoiding
false negatives with good probability.

### $(c, r)$-Approximate Near Neighbor Search

![[Pics/SimSearch2/SimSearch2-05.png]]
*Figure 5 - Definition of the $(c,r)$-Approximate Near Neighbor Search problem.*

> [!Important] Definition - $(c,r)$-Approximate Near Neighbor Search ($(c,r)$-ANNS)
> **Statement:** Given a set $P$ of $n$ points from the metric space $(M,d)$,
> construct a data structure that, given a query point $q \in M$ and a distance
> threshold $r > 0$, provides the following answer for a certain constant
> $c \geq 1$:
>
> - If there are points in $B_r(q) \cap P$, it returns a point $p \in P$ with
>   $d(p,q) \leq cr$.
> - If there are no points in $B_r(q) \cap P$, it may return either null or a
>   point $p \in P$ with $d(p,q) \leq cr$, if one exists.
>
> **Remark:** In the second case, a null answer is always acceptable, even if a
> point $p \in P$ with $d(p,q) \leq cr$ exists.
>
> **Observation:** In all cases, the data structure never returns a point far
> away from the query point $q$, i.e. at distance $> cr$.
>
> **Intuition:** The algorithm is allowed to return a point in the relaxed ball
> of radius $cr$, but if a true $r$-near neighbor exists it should not return
> null.

![[Pics/SimSearch2/SimSearch2-06.png]]
*Figure 6 - $(c,r)$-ANNS example with near points. Legal outputs are any of the four points $A,B,C,D$.*

> [!Example] $(c,r)$-ANNS Example - Near Points Exist
> **Setting:** Some points lie inside $B_r(q)$ and some lie in the larger ball
> of radius $cr$.
>
> **Legal outputs:** Any of the four points $A, B, C, D$.
>
> **Takeaway:** When near points exist, any returned point within distance
> $\leq cr$ is acceptable.

![[Pics/SimSearch2/SimSearch2-07.png]]
*Figure 7 - $(c,r)$-ANNS example with no near points. Legal outputs are $A$, $B$, or null.*

> [!Example] $(c,r)$-ANNS Example - No Near Points
> **Setting:** There are no points inside $B_r(q)$, but there are points inside
> the relaxed radius $cr$.
>
> **Legal outputs:** $A$, $B$, or null.
>
> **Takeaway:** If $B_r(q) \cap P = \emptyset$, returning null is legal, and so
> is returning a point within distance $\leq cr$ if such a point exists.

![[Pics/SimSearch2/SimSearch2-08.png]]
*Figure 8 - $(c,r)$-ANNS example with only far points. The only legal output is null.*

> [!Example] $(c,r)$-ANNS Example - Only Far Points
> **Setting:** All points are farther than $cr$ from $q$.
>
> **Legal output:** null.
>
> **Takeaway:** The data structure must not return points farther than $cr$.

## Locality Sensitive Hashing

![[Pics/SimSearch2/SimSearch2-09.png]]
*Figure 9 - Main idea of using Locality Sensitive Hashing for approximate near neighbor search.*

The lecture presents a solution to $(c,r)$-ANN based on **Locality Sensitive
Hashing (LSH)**. LSH is a technique introduced in the late 90s and widely used
for high-dimensional near-neighbor search in applications such as recommender
systems, duplicate/plagiarism detection, and search engines.

Main ideas:

- The entire space is partitioned into regions through a hash function $h$
  randomly extracted from a suitable family $\mathcal{H}$.
- The partitioning ensures two properties:
  1. Two near points are likely to be mapped by $h$ to the same region.
  2. Two far points are likely to be mapped by $h$ to different regions.
- The neighbors of the query point $q$ are searched for in the region identified
  by $h(q)$.

> [!Important] Observation - LSH vs Standard Hashing
> Standard hashing aims at minimizing collision probability for any pair of
> elements. LSH instead makes collision probability positively related to the
> similarity between elements.
>
> **Intuition:** Similar objects should collide often; far objects should collide
> rarely.

### Definition of LSH

![[Pics/SimSearch2/SimSearch2-10.png]]
*Figure 10 - Formal definition of a $(c,r,p_1,p_2)$-locality sensitive hash family.*

Consider a metric space $(M,d)$ and a family of hash functions:

$$
\mathcal{H} = \{h : M \to S\},
$$

where $S$ is a given domain, for example indices in some range $[0,t]$.
For any two points $p,q \in M$, denote by

$$
\Pr_{h \in \mathcal{H}}[h(p) = h(q)]
$$

the probability that a hash function $h$ extracted uniformly at random from
$\mathcal{H}$ maps $p$ and $q$ to the same value.

> [!Important] Definition - $(c,r,p_1,p_2)$-Locality Sensitive Hashing
> **Statement:** Given parameters $c > 1$, $r > 0$, and
> $p_1,p_2 \in [0,1]$, with $p_1 > p_2$, a family $\mathcal{H}$ is
> **$(c,r,p_1,p_2)$-locality sensitive** if, for any $p,q \in M$:
>
> - If $d(p,q) \leq r$, then
>
>   $$
>   \Pr_{h \in \mathcal{H}}[h(p)=h(q)] \geq p_1.
>   $$
>
> - If $d(p,q) > cr$, then
>
>   $$
>   \Pr_{h \in \mathcal{H}}[h(p)=h(q)] \leq p_2.
>   $$
>
> **Intuition:** Near points collide with probability at least $p_1$, while far
> points collide with probability at most $p_2$.

![[Pics/SimSearch2/SimSearch2-11.png]]
*Figure 11 - Comments on LSH collision probabilities and a typical decreasing collision curve.*

Important comments:

- The collision probability for points with distance in $(r,cr]$ is not specified.
- Usually, the collision probability between two points $p,q$ can be expressed
  as a monotonically decreasing function of $d(p,q)$.
- Example: for a pair of points with Hamming distance $d$ normalized in $[0,1]$,
  one can define an LSH whose collision probability decreases as $d$ increases.

### Solving $(c,r)$-ANNS with LSH

![[Pics/SimSearch2/SimSearch2-12.png]]
*Figure 12 - Basic LSH data structure for solving $(c,r)$-ANNS, with handwritten note that buckets $T[j]$ are implemented as lists.*

A $(c,r,p_1,p_2)$-LSH family $\mathcal{H}$ can be used for solving $(c,r)$-ANNS
on the input set $P$ as follows.

> [!Important] Algorithm - Basic LSH Data Structure
> **Construction:**
>
> 1. Randomly select $h$ from $\mathcal{H}$.
> 2. Insert all points of $P$ into a hash table $T$ using function $h$.
> 3. Let $T[j]$ be the potentially empty bucket containing all points in $P$
>    with hash value $j$:
>
>    $$
>    T[j] = \{p \in P : h(p) = j\}.
>    $$
>
> **Query:**
>
> 1. For a query $q$, scan $T[h(q)]$ until a point $p$ with
>    $d(p,q) \leq cr$ is found.
> 2. Return that point.
> 3. If there is no such point, return null.
>
> **Implementation note from handwriting:** The $T[j]$ buckets are implemented
> as lists.

### Example with Boolean Vectors

![[Pics/SimSearch2/SimSearch2-13.png]]
*Figure 13 - LSH example over Boolean vectors of length 9 using two sampled bits.*

The example uses:

- Metric space: $M = \{\text{Boolean vectors of length }9\}$.
- Distance function: Hamming distance.
- $P \subset M$ is a set of $n = 8$ vectors of length 9.

For $0 \leq i < j < 8$, let

$$
h_{i,j}: M \to [0,3]
$$

be the hash function mapping each vector $x \in M$ to the integer whose binary
configuration is $x[i]x[j]$. Define:

$$
\mathcal{H} = \{h_{i,j} : 0 \leq i < j < 8\}.
$$

![[Pics/SimSearch2/SimSearch2-14.png]]
*Figure 14 - Construction example with $h_{1,2}$ selected, plus handwritten notes about legal outputs for different $c$ values.*

> [!Example] LSH Example - Hashing Boolean Vectors
> **Construction:** Suppose that $h_{1,2} \in \mathcal{H}$ is selected.
> The points of $P$ are grouped by their values under $h_{1,2}$.
>
> **Query:** The query vector $q$ is mapped to one bucket.
>
> **Handwritten annotations:**
>
> - $P$ labels the input point set.
> - Some outputs are legal only for $c \geq 2$.
> - Other outputs are legal for any $c > 1$.
>
> **Takeaway:** The value of $c$ determines how large the acceptable output ball
> is; increasing $c$ makes more returned points legal.

### Basic LSH Data Structure and Performance

![[Pics/SimSearch2/SimSearch2-15.png]]
*Figure 15 - Expected contents of the bucket $T[h(q)]$ for the query point $q$.*

For a query point $q$, the bucket $T[h(q)]$ is expected to contain:

- A near point $p$, i.e. $d(p,q) \leq r$, with probability at least $p_1$.
  However, that point might also end up in a different bucket.
- A far point $p'$, i.e. $d(p',q) > cr$, only with probability at most $p_2$.

Worst-case scenario:

- $P$ contains one near point $p \in P$ with $d(q,p) \leq r$.
- $P$ contains $n-1$ far points $p'$ with $d(p',q) > cr$.

In expectation, at most $np_2$ far points collide with $q$.

![[Pics/SimSearch2/SimSearch2-16.png]]
*Figure 16 - Performance theorem for the basic LSH data structure.*

Assume that $(M,d)$ is a space of dimensionality $D$, for example
$M = \mathbb{R}^D$, and that:

- Each point of $M$ requires $O(D)$ words to be stored.
- Hash values and distances can be computed in $O(D)$ time.

> [!Important] Theorem - Basic LSH Performance for $(c,r)$-ANNS
> **Statement:** Let $P$ be a set of $n$ points in a $D$-dimensional metric
> space $(M,d)$, and let $\mathcal{H}$ be a $(c,r,p_1,p_2)$-locality sensitive
> family of hash functions. Using $\mathcal{H}$ and the basic approach to
> $(c,r)$-ANNS, a query $q$ is answered successfully with probability
> $\geq p_1$. Moreover:
>
> | Quantity | Bound |
> |---|---|
> | Construction time | $O(Dn)$ |
> | Space | $O(Dn)$ |
> | Query time | $O(Dnp_2)$ in expectation |

![[Pics/SimSearch2/SimSearch2-17.png]]
*Figure 17 - Handwritten proof of probabilistic correctness for the basic LSH data structure.*

> [!Important] Proof - Basic LSH Probabilistic Correctness
> **Case 1:** $B_r(q) \cap P \neq \emptyset$.
>
> In this case, any $p' \in P$ with $d(p',q) \leq cr$ is a legal output.
> Consider an arbitrary point
>
> $$
> p \in B_r(q) \cap P
> $$
>
> which must exist, and let $h \in \mathcal{H}$ be the extracted hash function.
> Then:
>
> $$
> \Pr(\text{answer is correct})
> =
> \Pr(\text{answer} \neq \text{null})
> \geq
> \Pr(h(p)=h(q))
> \geq
> p_1.
> $$
>
> **Reasoning:** If the near point $p$ collides with $q$, then $p$ is in the
> scanned bucket $T[h(q)]$, and a legal output can be found.

![[Pics/SimSearch2/SimSearch2-18.png]]
*Figure 18 - Continuation of the handwritten proof: correctness, construction time, space, and query-time setup.*

Since $\mathcal{H}$ is $(c,r,p_1,p_2)$-locality sensitive, the inequality above
holds.

**Case 2:** $B_r(q) \cap P = \emptyset$.

In this case, any answer is correct: either a point $p$ with $d(p,q) \leq cr$,
or null.

Construction time and space are straightforward. For query time, the scan of the
list $T[h(q)]$ stops as soon as a point $p$ with $d(p,q) \leq cr$ is found, or
when the end of the list is reached.

![[Pics/SimSearch2/SimSearch2-19.png]]
*Figure 19 - Handwritten expected query-time proof for the basic LSH data structure.*

Let $x$ be the number of points $p \in P$ such that:

$$
d(p,q) > cr
\quad \text{and} \quad
h(p) = h(q).
$$

The query time is:

$$
O(D \cdot x).
$$

The random variable $x$ satisfies:

$$
\mathbb{E}[x] \leq np_2,
$$

because, for each $p \in P$ with $d(p,q) > cr$, the LSH property gives:

$$
\Pr(h(p)=h(q)) \leq p_2.
$$

There are at most $n$ such points, hence the expected query time is:

$$
O(D \cdot n \cdot p_2).
$$

![[Pics/SimSearch2/SimSearch2-20.png]]
*Figure 20 - Blank slide preserved from the source.*

![[Pics/SimSearch2/SimSearch2-21.png]]
*Figure 21 - Blank slide preserved from the source.*

## LSH Families for Common Distances

![[Pics/SimSearch2/SimSearch2-22.png]]
*Figure 22 - Section divider for LSH families for Hamming and Euclidean distances.*

### Bit Sampling for Hamming Distance

![[Pics/SimSearch2/SimSearch2-23.png]]
*Figure 23 - Bit-sampling LSH for Hamming distance, with handwritten note explaining the probability $d_H(p,q)/D$.*

Let the metric space be:

$$
M = \{\text{Boolean vectors of length }D\}.
$$

For $0 \leq i < D$, define the hash function:

$$
h_i : M \to \{0,1\}
$$

that maps each vector $x \in M$ to its $i$-th bit $x[i]$. The hash family is:

$$
\mathcal{H}_H = \{h_i : 0 \leq i < D\}.
$$

Given two points $p,q$, the probability of collision is:

$$
\Pr_{h \in \mathcal{H}_H}[h(p)=h(q)]
= 1 - \frac{d_H(p,q)}{D},
$$

where $d_H()$ denotes Hamming distance.

The handwritten note explains that $\frac{d_H(p,q)}{D}$ is the probability that
the extracted hash function $h_i$ samples an index $i$ where $p[i] \neq q[i]$.

![[Pics/SimSearch2/SimSearch2-24.png]]
*Figure 24 - Proof that bit sampling is $(c,r,1-r/D,1-cr/D)$-locality sensitive, with handwritten labels for $p_1$ and $p_2$.*

For any two points $p,q$:

- If $d_H(p,q) \leq r$, then:

$$
\Pr_{h \in \mathcal{H}_H}[h(p)=h(q)]
=
1 - \frac{d_H(p,q)}{D}
\geq
1 - \frac{r}{D}
\stackrel{def}{=}
p_1.
$$

- If $d_H(p,q) > cr$, then:

$$
\Pr_{h \in \mathcal{H}_H}[h(p)=h(q)]
=
1 - \frac{d_H(p,q)}{D}
<
1 - \frac{cr}{D}
\stackrel{def}{=}
p_2.
$$

Therefore:

$$
\mathcal{H}_H
\text{ is }
(c,r,1-r/D,1-cr/D)\text{-locality sensitive}.
$$

The handwritten labels identify $p_1 = 1-r/D$ and $p_2 = 1-cr/D$.

#### The $\rho$ Factor

![[Pics/SimSearch2/SimSearch2-25.png]]
*Figure 25 - Definition of the $\rho$ factor and its value for bit sampling.*

A $(c,r,p_1,p_2)$-locality sensitive family $\mathcal{H}$ is effective when:

$$
p_1 >> p_2.
$$

A parameter used to measure the quality of such a family is the **$\rho$ factor**:

$$
\rho =
\frac{\log_2 p_1}{\log_2 p_2}
=
\frac{\log_2(1/p_1)}{\log_2(1/p_2)}.
$$

Since $1 \geq p_1 > p_2 > 0$, we have $\rho \in (0,1)$. The value decreases as
$p_1/p_2$ grows; therefore, smaller $\rho$ is better.

For bit sampling:

$$
\rho =
\frac{\log_2 p_1}{\log_2 p_2}
=
\frac{\log_2(1-r/D)}{\log_2(1-cr/D)}
\sim
\frac{r/D}{cr/D}
=
\frac{1}{c}.
$$

### Random Projection for Euclidean Distance

![[Pics/SimSearch2/SimSearch2-26.png]]
*Figure 26 - Random projection LSH for Euclidean distance.*

The metric space is:

$$
M = \mathbb{R}^D.
$$

For a fixed value $w > 0$ and parameters $a \in \mathbb{R}^D$ and
$b \in [0,w]$, define the hash function:

$$
h_{a,b}(p) : M \to \mathbb{Z}
$$

as:

$$
h_{a,b}(p)
=
\left\lceil
\frac{\langle a,p \rangle + b}{w}
\right\rceil,
$$

where $\langle \cdot,\cdot \rangle$ denotes the inner product.

Define:

$$
\mathcal{H}_E(w)
=
\{h_{a,b}(p) : a \in \mathbb{R}^D \text{ and } b \in [0,w]\}.
$$

It can be shown that $\mathcal{H}_E(w)$ is $(c,r,p_1,p_2)$-locality sensitive
with:

$$
\rho = O(1/c),
$$

assuming $a$ is selected with normal distribution $N^D(0,1)$ and $b$ with
uniform distribution.

![[Pics/SimSearch2/SimSearch2-27.png]]
*Figure 27 - Handwritten observations about practical implementation of random projection buckets.*

> [!Important] Observation - Implementing Random Projection Buckets
> The hash functions of $\mathcal{H}_E(w)$ map points
> $p \in \mathbb{R}^D$ into arbitrary integers.
>
> For practical purposes, once a function $h_{a,b}$ is extracted from
> $\mathcal{H}_E(w)$, a further hash function $h$ is used to map the non-empty
> buckets created by $h_{a,b}$ to indices in a small range.
>
> For a query $q$, the bucket $T[h_{a,b}(q)]$ is first retrieved among those
> mapped by $h$ to the same index, and then this bucket is searched for a near
> neighbor of $q$.

![[Pics/SimSearch2/SimSearch2-28.png]]
*Figure 28 - Continuation of handwritten observations on random projection.*

For Euclidean spaces, better families of locality-sensitive hash functions exist
with:

$$
\rho \in O(1/c^2).
$$

#### Random Projection Example

![[Pics/SimSearch2/SimSearch2-29.png]]
*Figure 29 - Random projection example: points and projection direction $a$.*

![[Pics/SimSearch2/SimSearch2-30.png]]
*Figure 30 - Random projection example: points projected onto the line in direction $a$.*

![[Pics/SimSearch2/SimSearch2-31.png]]
*Figure 31 - Random projection example: bucket width $w$ shown in the projected line.*

![[Pics/SimSearch2/SimSearch2-32.png]]
*Figure 32 - Random projection example: query point $q$ and its projected bucket.*

The figures illustrate how points are projected onto the line defined by $a$,
then grouped into intervals of width $w$. A query point $q$ searches the bucket
corresponding to its projected value.

## Improving the Data Structure

![[Pics/SimSearch2/SimSearch2-33.png]]
*Figure 33 - Motivation for improving LSH collision probabilities.*

Ideally, LSH should have $p_1$ close to 1 and $p_2$ close to 0. However, a
family $\mathcal{H}$ may not provide this type of guarantees.

The lecture outlines two improvements:

| Goal | Technique |
|---|---|
| Increase collision probability of near points | Repetition / OR construction |
| Decrease collision probability of far points | Concatenation / AND construction |

Combined together, these improvements yield better LSH.

### OR Construction: Repetition

![[Pics/SimSearch2/SimSearch2-34.png]]
*Figure 34 - Improvement 1: increase collision probability of near points by using $\ell$ hash tables.*

> [!Important] Improvement 1 - Repetition / OR Construction
> **Idea:** Repeat the search $\ell > 1$ times using $\ell$ distinct hash tables
> based on independent hash functions chosen uniformly at random from a
> $(c,r,p_1,p_2)$-locality sensitive family $\mathcal{H}$.
>
> **Effect:** The probability that a near point $p$ with $d(p,q) \leq r$
> collides with the query point $q$ in at least one hash table increases with
> $\ell$.
>
> **Cost:** Checking $\ell$ buckets, one for each hash table, becomes
> computationally expensive.

![[Pics/SimSearch2/SimSearch2-35.png]]
*Figure 35 - Handwritten derivation for the success probability under repetition.*

Let $p$ be such that:

$$
d(p,q) \leq r.
$$

For one particular hash table, the probability that $p$ and $q$ are in different
buckets is at most:

$$
1-p_1.
$$

For all $\ell$ hash tables, the probability that $p$ and $q$ are in different
buckets is at most:

$$
(1-p_1)^\ell,
$$

by independence of the hash functions.

Therefore, the probability that, given the query $q$, the point $p$ is found in
the same bucket as $q$ in at least one hash table is:

![[Pics/SimSearch2/SimSearch2-36.png]]
*Figure 36 - Handwritten conclusion that repetition increases the near-point collision probability.*

$$
\geq 1 - (1-p_1)^\ell.
$$

For $\ell > 1$:

$$
(1-p_1)^\ell < 1-p_1.
$$

Hence:

$$
1 - (1-p_1)^\ell
>
1 - (1-p_1)
=
p_1.
$$

Thus repetition improves the success probability for near points.

![[Pics/SimSearch2/SimSearch2-37.png]]
*Figure 37 - Blank slide preserved from the source.*

### AND Construction: Concatenation

![[Pics/SimSearch2/SimSearch2-38.png]]
*Figure 38 - Improvement 2: decrease collision probability of far points by concatenating $k$ hash functions.*

> [!Important] Improvement 2 - Concatenation / AND Construction
> **Idea:** Use a family $\mathcal{G}$ of hash functions obtained by
> concatenating $k \geq 1$ independent hash functions chosen uniformly at random
> from a $(c,r,p_1,p_2)$-locality sensitive family $\mathcal{H}$.
>
> Namely:
>
> $$
> \mathcal{G}
> =
> \{g \in \mathcal{H}^k\}
> =
> \{g(p) = (h_1(p), \ldots, h_k(p)), \text{ with } h_i \in \mathcal{H}\}.
> $$
>
> For a random $g \in \mathcal{G}$ and any two points $p,q$ with $p \neq q$:
>
> - If $d(p,q) \leq r$, then
>
>   $$
>   \Pr[g(p)=g(q)] \geq p_1^k.
>   $$
>
> - If $d(p,q) > cr$, then
>
>   $$
>   \Pr[g(p)=g(q)] \leq p_2^k.
>   $$
>
> **Intuition:** Concatenation requires all $k$ component hashes to match, so far
> points become much less likely to collide.

![[Pics/SimSearch2/SimSearch2-39.png]]
*Figure 39 - Choosing $k = \log_{1/p_2} n$ so that far-point collision probability becomes at most $1/n$.*

Suppose that we set:

$$
k
=
\log_{1/p_2} n
=
\frac{\log_2 n}{\log_2(1/p_2)}.
$$

Then, for a random $g \in \mathcal{G}$ and any two points $p,q$ with
$p \neq q$:

- If $d(p,q) \leq r$, then:

$$
\Pr[g(p)=g(q)] \geq p_1^k = 1/n^\rho.
$$

- If $d(p,q) > cr$, then:

$$
\Pr[g(p)=g(q)] \leq p_2^k = 1/n.
$$

With this choice of $k$, the expected number of collisions of a query point $q$
with far points in the same bucket is at most 1.

![[Pics/SimSearch2/SimSearch2-40.png]]
*Figure 40 - Handwritten derivation of $p_1^k = n^{-\rho}$.*

The handwritten derivation expands $k$ as follows:

$$
k
=
\frac{\log_2 n}{\log_2(1/p_2)}.
$$

Using the $\rho$ factor:

$$
k
=
\frac{\log_2 n}{\log_2(1/p_1)}
\cdot
\frac{\log_2(1/p_1)}{\log_2(1/p_2)}
=
(\log_{1/p_1} n)\cdot \rho.
$$

Therefore:

$$
p_1^k = n^{-\rho}.
$$

![[Pics/SimSearch2/SimSearch2-41.png]]
*Figure 41 - Blank slide preserved from the source.*

### General LSH Schema for $(c,r)$-ANNS

![[Pics/SimSearch2/SimSearch2-42.png]]
*Figure 42 - General LSH schema combining repetition and concatenation.*

The two improvements are merged into a general schema. Let $\mathcal{H}$ be a
$(c,r,p_1,p_2)$-locality sensitive family of hash functions, and let $k$ and
$\ell$ be values to be set later.

> [!Important] Algorithm - General LSH Schema for $(c,r)$-ANNS
> **Construction:**
>
> 1. Construct $\ell$ hash functions $g_1,\ldots,g_\ell$.
> 2. Each $g_i$ consists of the concatenation of $k$ hash functions randomly and
>    independently selected from $\mathcal{H}$.
> 3. For each $g_i$, construct a hash table $T_i$ of points in $P$ using $g_i$.
> 4. Let $T_i[j]$ be the potentially empty bucket containing all points in $P$
>    with hash value $j$ when using $g_i$.
>
> **Query:**
>
> 1. Scan the buckets:
>
>    $$
>    T_1[g_1(q)], \ldots, T_\ell[g_\ell(q)].
>    $$
>
> 2. Stop when a $cr$-near point $p$ is found and return it.
> 3. If no such point is found, return null.

#### Schema Example

![[Pics/SimSearch2/SimSearch2-43.png]]
*Figure 43 - General LSH schema example: point set $P$.*

![[Pics/SimSearch2/SimSearch2-44.png]]
*Figure 44 - General LSH schema example: first hash table $T_1$ using $g_1 = h_{1,1} \circ \cdots \circ h_{1,k}$.*

$$
g_1 = h_{1,1} \circ \cdots \circ h_{1,k}.
$$

![[Pics/SimSearch2/SimSearch2-45.png]]
*Figure 45 - General LSH schema example: adding $T_2$ using $g_2 = h_{2,1} \circ \cdots \circ h_{2,k}$.*

$$
g_2 = h_{2,1} \circ \cdots \circ h_{2,k}.
$$

![[Pics/SimSearch2/SimSearch2-46.png]]
*Figure 46 - General LSH schema example: adding $T_3$ using $g_3 = h_{3,1} \circ \cdots \circ h_{3,k}$.*

$$
g_3 = h_{3,1} \circ \cdots \circ h_{3,k}.
$$

![[Pics/SimSearch2/SimSearch2-47.png]]
*Figure 47 - General LSH schema example: generic table $T_i$ using $g_i = h_{i,1} \circ \cdots \circ h_{i,k}$.*

$$
g_i = h_{i,1} \circ \cdots \circ h_{i,k}.
$$

![[Pics/SimSearch2/SimSearch2-48.png]]
*Figure 48 - General LSH schema example: final table $T_\ell$ using $g_\ell = h_{\ell,1} \circ \cdots \circ h_{\ell,k}$.*

$$
g_\ell = h_{\ell,1} \circ \cdots \circ h_{\ell,k}.
$$

![[Pics/SimSearch2/SimSearch2-49.png]]
*Figure 49 - Performance theorem for the combined LSH schema.*

> [!Important] Theorem - General LSH Performance for $(c,r)$-ANNS
> **Statement:** Let $P$ be a set of $n$ points in a metric space $(M,d)$, and
> let $\mathcal{H}$ be a $(c,r,p_1,p_2)$-locality sensitive family of hash
> functions. Fix:
>
> $$
> k = \log_{1/p_2} n
> \quad \text{and} \quad
> \ell = 2p_1^{-k} = 2n^\rho,
> $$
>
> where:
>
> $$
> \rho = \frac{\log_2 p_1}{\log_2 p_2}.
> $$
>
> Using the above approach to $(c,r)$-ANNS, a query is answered successfully with
> probability $\geq 1/2$.
>
> The performance is:
>
> | Quantity | Bound |
> |---|---|
> | Construction time | $O(Dn^{1+\rho}\log_{1/p_2} n)$ |
> | Space | $O(Dn + n^{1+\rho}\log_{1/p_2} n)$ |
> | Query time | $O(Dn^\rho \log_{1/p_2} n)$ in expectation |
>
> **Intuition:** Concatenation reduces far-point collisions, while repetition
> recovers enough probability of finding near points.

![[Pics/SimSearch2/SimSearch2-50.png]]
*Figure 50 - Blank slide preserved from the source.*

![[Pics/SimSearch2/SimSearch2-51.png]]
*Figure 51 - Blank slide preserved from the source.*

![[Pics/SimSearch2/SimSearch2-52.png]]
*Figure 52 - Blank slide preserved from the source.*

![[Pics/SimSearch2/SimSearch2-53.png]]
*Figure 53 - Blank slide preserved from the source.*

## Concatenating Bit Sampling

![[Pics/SimSearch2/SimSearch2-54.png]]
*Figure 54 - Concatenating bit sampling for Hamming distance and projecting to a random subset of dimensions.*

Concatenating $k$ bit-sampling LSH functions consists in randomly selecting
$k$ indexes. It yields the following collision probabilities:

- If $d_H(p,q) \leq r$, then:

$$
\Pr_{h \in \mathcal{H}_H}[h(p)=h(q)]
\geq
(1-r/D)^k.
$$

- If $d_H(p,q) \geq cr$, then:

$$
\Pr_{h \in \mathcal{H}_H}[h(p)=h(q)]
\leq
(1-cr/D)^k.
$$

The concatenation does not change the $\rho$ value.

**Bitsampling:** project to a random subset of dimensions:

$$
x = 00101001010
\qquad
y = 10101100010
$$

$$
h(x) = 011
\qquad
h(y) = 011.
$$

![[Pics/SimSearch2/SimSearch2-55.png]]
*Figure 55 - Collision probability plot for concatenating bit sampling, comparing $k=1$ and $k=3$.*

The plot shows that increasing $k$ makes collision probability decrease faster
as relative Hamming distance grows. This is exactly the purpose of AND
construction: far points collide much less often.

## Exercises

![[Pics/SimSearch2/SimSearch2-56.png]]
*Figure 56 - Exercise on document similarity using locality-sensitive hashing.*

> [!Example] Exercise - Document Similarity with LSH
> **Problem:** Let $P$ be a collection of $n$ documents that you want to store
> into a suitable data structure so to retrieve, given a query document $q$, a
> similar document in $P$. Let $W$ be a set of $D$ relevant words and suppose
> that the similarity between two documents depends on the number of words of
> $W$ in common, ignoring their relative frequencies.
>
> 1. Describe a representation of the documents and a data structure for $P$
>    based on a suitable locality-sensitive family of hash functions. Use only
>    one hash function for the data structure.
> 2. Based on the above point, find values of $c$ and $r$ such that the
>    $(c,r)$-ANNS problem for $P$ can be solved correctly with probability at
>    least $1/2$ and expected query time $O(n)$. Observe that the trivial exact
>    approach requires $O(Dn)$ query time.
>
> **Source status:** The slide states the exercise but does not provide a worked
> solution.

![[Pics/SimSearch2/SimSearch2-57.png]]
*Figure 57 - Exercise on finding far Boolean vectors using bit-sampling LSH.*

> [!Example] Exercise - Far Vectors with Bit Sampling
> **Problem:** Let $P$ be a set of $n$ $D$-dimensional Boolean vectors. Suppose
> that $P$ is stored into a hash table $T$ built using a hash function $h$
> randomly drawn from the bit-sampling LSH family
> $\mathcal{H} = \{h_i : 0 \leq i < D\}$. For $h \in \mathcal{H}$, let
> $\text{not}(h(x))$ denote the negation of the binary value $h(x)$.
>
> 1. Given two vectors $p$ and $q$, determine the probability
>
>    $$
>    \Pr_{h \in \mathcal{H}}[h(p) = \text{not}(h(q))]
>    $$
>
>    as a function of the Hamming distance $d_H(p,q)$.
>
> 2. Given a query vector $q$, we want to find an $r$-far vector $p \in P$, i.e.
>    such that $d_H(p,q) \geq r$. Based on the above analysis, how would you
>    efficiently search such a $p$ in the table $T$? What probabilistic
>    guarantees does your method provide?
>
> **Source status:** The slide states the exercise but does not provide a worked
> solution.

## Summary

![[Pics/SimSearch2/SimSearch2-58.png]]
*Figure 58 - Lecture summary.*

The lecture covered:

- Similarity search: $r$-NNS and RR problems.
- $k$-d tree for similarity search in low dimensions.
- Curse of dimensionality for similarity search.
- $(c,r)$-ANNS problem.
- LSH approach to the $(c,r)$-ANNS problem:
  - definition of $(c,r,p_1,p_2)$-locality sensitive hash functions;
  - solving $(c,r)$-ANNS through $(c,r,p_1,p_2)$-locality sensitive hash functions;
  - $(c,r,p_1,p_2)$-locality sensitive hash functions for Hamming and Euclidean
    distances, using bit sampling and random projection;
  - improving collision probabilities with repetition and concatenation, and
    their combination.

## References

![[Pics/SimSearch2/SimSearch2-59.png]]
*Figure 59 - References for similarity search, kd-trees, and LSH.*

- **LRU14** J. Leskovec, A. Rajaraman and J. Ullman. *Mining Massive Datasets*.
  Cambridge University Press, 2014. Section 3.6.
- **BCKO08** Mark de Berg, Otfried Cheong, Marc van Kreveld, and Mark Overmars.
  *Computational Geometry: Algorithms and Applications* (3rd ed. ed.).
  Springer-Verlag, 2008. Section 5.2.
- **AI08** Alexandr Andoni and Piotr Indyk. 2008. Near-optimal hashing algorithms
  for approximate nearest neighbor in high dimensions. *Communications of the
  ACM* 51, 1, 2008.

## Final Summary Table

| Algorithm / Technique | Model | Cost / Bound | Typical use |
|---|---|---|---|
| $(c,r)$-ANNS | Metric space $(M,d)$ | Returns point within $cr$ if an $r$-near point exists; may return null when none exists | Approximate high-dimensional near neighbor search |
| Basic LSH | One hash table using $h \in \mathcal{H}$ | Construction $O(Dn)$, space $O(Dn)$, expected query $O(Dnp_2)$, success probability $\geq p_1$ | Simple approximate near neighbor data structure |
| $(c,r,p_1,p_2)$-LSH | Hash family over metric space | Near points collide with probability $\geq p_1$; far points collide with probability $\leq p_2$ | Core primitive for $(c,r)$-ANNS |
| Bit sampling | Hamming space over Boolean vectors of length $D$ | $\Pr[h(p)=h(q)] = 1 - d_H(p,q)/D$ | LSH for Hamming distance |
| Bit sampling sensitivity | Hamming distance | $(c,r,1-r/D,1-cr/D)$-locality sensitive | Establishes $p_1$ and $p_2$ for Hamming LSH |
| $\rho$ factor | Any LSH family | $\rho = \log_2 p_1 / \log_2 p_2 = \log_2(1/p_1)/\log_2(1/p_2)$ | Measures quality of LSH; smaller is better |
| Bit sampling $\rho$ | Hamming distance | $\rho \sim 1/c$ | Quality bound for simple Hamming LSH |
| Random projection | Euclidean space $\mathbb{R}^D$ | $h_{a,b}(p)=\left\lceil(\langle a,p\rangle+b)/w\right\rceil$ | LSH for Euclidean distance |
| Random projection quality | Euclidean distance | $\rho = O(1/c)$; better families can reach $\rho \in O(1/c^2)$ | Approximate near neighbor in Euclidean spaces |
| Repetition / OR construction | $\ell$ independent hash tables | Near-point success becomes at least $1-(1-p_1)^\ell$ | Increase probability of finding near points |
| Concatenation / AND construction | $k$ independent hashes combined as $g(p)=(h_1(p),\ldots,h_k(p))$ | Near collision $\geq p_1^k$, far collision $\leq p_2^k$ | Decrease collision probability of far points |
| Choice $k=\log_{1/p_2}n$ | AND construction | Far collision probability $\leq 1/n$; near collision probability $\geq 1/n^\rho$ | Keep expected far collisions small |
| General LSH schema | $\ell=2p_1^{-k}=2n^\rho$ hash tables, each using concatenation length $k$ | Success probability $\geq 1/2$; query $O(Dn^\rho\log_{1/p_2}n)$ in expectation | Practical theoretical LSH data structure for $(c,r)$-ANNS |
| Concatenating bit sampling | Hamming distance | Collision probabilities $(1-r/D)^k$ and $(1-cr/D)^k$ | Stronger Hamming LSH via AND construction |
