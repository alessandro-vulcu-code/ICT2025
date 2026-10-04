# MAP REDUCE

1. Map Reduce round is a step in which a set of $K$-v pairs is transformed into another set of key-value pairs.

The Map Reduce steps are:

- **Map phase:** Input pair the map function produces $> 0$ intermediate pairs

- **Shuffle:** intermediate pairs are grouped by key $\rightarrow VK$, returning a list $Lu$ of values

- **Reduce:** $VK$ separately the reduce function is applied to $(K, Lu)$ and produces $> 0$ output pairs

---

2. In Map Reduce:

- $R$ = # rounds, generally 2 or more
- $M_L$ = local memory for each cluster, generally is live $O(1 \text{ size}^2)$ with $O \leq E < 1$
- $M_A$ = aggregate memory, it's the memory shared among the machines and generally is $O(1 \text{ size})$

The ideal Map Reduce algorithm tries to reach the target defined above. Trying to collapse all in one round causes the increase of $M_L$ generally

---

3. 10 machines with 8 GB of RAM each
128 GB of disk

$M_L$ at least 8 GB
$M_A$: for 10 clusters, $10 \cdot 128 \text{ GB} = 1280 \text{ GB}$

---

6. $N$ web does $(\nu N, D)$ each occupying $O(1)$ space.

Let $L = \sqrt{N}$

Document, mapper samples $J$ uniformly from $\{0, \dots, L-1\}$ and emits map $u(L, D) \rightarrow (J, (url, D))$

For fixed partition $j$, size

$$
X_j \sim \text{Binomial}(N, \frac{1}{L}), \quad E[X_j] = \frac{N}{L} \leq \sqrt{N}
$$

Chernoff bound gives small probability that one fixed partition greatly exceeds its mean.

Applying union bound over $L$ partitions gives, for $N \geq 16$

$$
\Pr[\max_j X_j > 6\sqrt{N}] \leq \frac{1}{N^6}
$$

=0 largest partition has $O(\sqrt{N})$ size with high prob.

If $Key \rightarrow 0$, using $o$ mod $L$ sends everything to one reducer. Ignore original $Key$ and emit fresh random partition $Key$:

$$
(0, x) \rightarrow (J, x)
$$

---

7. Class count = no receive N objects, each assigned class label $x_i$.

Input: $\{(i, (x_i, o_i)) : 0 \le i < N\}$

Objective: compute number of objects belonging to every class

$$
c(x) = \left| \{ i : x_i = x \} \right|
$$

One-round algorithm

Map

$(i, (x_i, o_i)) \rightarrow (y_i, 1)$

Reduce

For $(x, L_x)$ emits $y_i = \text{class}$

$L_x = \text{list of values}$

$|(x, L_x)|$

$R = 1$, $M_L = O(N)$, $M_A = O(N)$

Two-rounds:

Choose $L$ partitions:

Round 1

Map

$(i, (x_i, o_i)) \rightarrow (i \mod L, x_i)$

At most $\lceil N/L \rceil$ recurses

Reduce

For partition $i$, count each class locally

Round 2

Map: empty

Reduce: sum partial counts by class

$$
R = 2, M_L = O(\sqrt{N})
$$

$M_A = O(N)$

---

8. One-Round Word Count

Problem: count occurrences of each word across $k$ docs

Input: $\{(D_i, \text{name}, D_i, \text{words}) : 1 \leq i \leq k\}$
Output: $\{(w, c(w)) : w \text{ word}, c(w) = \# \text{tot occurrences}\}$

Round $i$

• Map phase: $D_i \rightarrow \{(w, c(w)): w \in D_i\}$
→qui mapper elabora un documento e conta localmente le vie
piede
reduce function

• Reduce phase: $(w_i, L_w) \rightarrow (w_i, \sum_{i \in I} c_i(w_i))$
→Reducer somma conteggi local: $\rightarrow$output pair

Analysis of Word Count

- $R = 1$
- $M_L$: $(H_p 1 \text{ word} = O(1) \text{ space})$
  - $N_i = \# \text{words in } D_i$
  - $N_{\max} = \max \{N_i : 1 \leq i \leq k\}$
- Map phase: $M_L = O(N_{\max})$
- Reduce phase: $M_L = O(k)$
  $\Rightarrow M_L = O(\max \{N_{\max}, k\}) = O(N_{\max} + k)$
- $M_A$:
  $N_A = \sum_{i=1}^{k} N_i = \text{total number of occurrences of all words}$
  aggregated over all documents

Two skew sources that causes large local space:

1. Document-size skew: largest doc requires $O(N_{\max})$
  mapper space

---

2. Word frequency shows: word occurring in all b docs sends up to b partial counts to one reducer, requiring O(b) space

---

10. Two words word count using random partitioning

Let $l = \sqrt{N}$ partitions

Round 1
Map: $(docID, D) \rightarrow (x, (w, cD(w))) \quad x \in [0, l)$
Reduce: $(x, [(w, cD(w))]) \rightarrow \{(w, c(x, w))\}$

Round 2
Map: empty
Reduce: $(w, [c(0, w), \dots, c(l-1, w)]) \rightarrow (w, \sum_x c(x, w))$

Local document counting produces at most $N$ intermediate points overall. For fixed word $w$, Round 1 produces at most one partition count per partition.

$$
|L_w| \leq l = \sqrt{N}
$$

Let $m = \max_x |L_x|$, max random partition load. Then

$$
M_L = O(N_{\max} + m + l)
$$

$$
= O(N_{\max} + \sqrt{N}) \quad M_a = O(N)
$$

---

Me. Difference between deterministic and random partitioning

Deterministic partitioning uses an hash function based on explicit data features to evenly subdivide the pairs. ex: $l$ partitions with key $i$ mod $l$, trying to reach optimal choice of $l = \sqrt{N} = O(\sqrt{N})$

Random partitioning instead assigns a uniform random key in $[0, l)$ to each intermediate pair. Always applicable.

---

# CLUSTERING, CORESETS

1. A metric space: pair $(M, d)$ with $d: M \times M \rightarrow \mathbb{R}$ such that $\forall x, y \in M$ satisfies:
   - non-negativity
   - identity
   - symmetry
   - triangle inequality

---

3. $k$-center, $k$-means, $k$-median and $c$-approximate
Let $(M, d)$ be a metric space. The $k$-center, $k$-means
and $k$-median clustering problems are optimization
problems that given a finite pointset $P \subset M$ and an
integer $K \leq |P|$, require to return the subset $S \subset P$ of
$K$ centers which minimizes the following respective objective
functions:

$$
\Phi_{ucenters}(P, S) = \max_{\pi \in P} d(x, S) \rightarrow \text{worst served point}
$$

$$
\Phi_{means}(P, S) = \sum_{\pi \in P} d(x, S)^2 \rightarrow \text{checks squared distance, emphasizes large deviations}
$$

$$
\Phi_{median}(P, S) = \sum_{\pi \in P} d(x, S) \rightarrow \text{checks total distance}
$$

For any problem $X, S$ is $c$-approximate if

$$
\Phi_x(P, S) \leq c \Phi_x^{\text{opt}}(P, K) \quad c > 1
$$

basically checking how far for algorithm's solution is far
from optimal solution

---

4. FFT, for the best first traversal is a popular 2-approx. sequential algorithm:
Input: Set $P$ of $N$ points, int $k \ge 1$
Output: Set $P$ of $N$ centers, good solver for $k$ center
Select an arbitrary point $C_i$ from $S$
for $i \le 2$ to $k$ do
    find the point $C_i \in P-S$ that makes $d(C_i, S)$
    $S \leftarrow S \cup \{C_i\}$
return $S$

It has a time complexity of $O(N \cdot k)$, but requires $k-1$ scans of $P$, so it is unsuitable for large $k$ and massive $P$

---

5. **Theorem:** $\Phi_{ucenter}(P, S) \leq 2 \cdot \Phi_{ucenter}^{opt}(P, k)$

We have $S = \{c_1, \ldots, c_n\}$ centers where $c_i$ is the $i$-th center selected by FFT.

Select a $q$ s.t. $\Phi_{ucenter}(P, S) = d(q, S)$

Consider $\{c_1, \ldots, c_k, c_{k+1}=q\}$ set of $k+1$ centers.

**CLAIM:** $d(q, S) \leq d(c_i, c_j)$ $\forall 1 \leq i < j \leq k+1$

Now let $S^* = \{c_1^*, \ldots, c_n^*\}$ be the optimal solution inducing clusters $C_1^*, \ldots, C_n^*$. By Pidgeonhole principle, among the $k+1$ points, at least two say $C_a, C_b$ - fall in the same optimal cluster $C_t^*$.

By triangle inequality:

$$
d(C_a, C_b) \leq d(C_a, C_t^*) + d(C_t^*, C_b) \leq 2 \Phi_{ucenter}^{opt}(P, k)
$$

**Therefore:**

$$
\Phi_{ucenter}(P, S) = d(q, S) \leq d(C_a, C_b) \leq 2 \Phi_{ucenter}^{opt}(P, k)
$$

---

6. When the input is too large for a sequential algorithm, the comparable careset constructor permits partitioning $P$ into $P_1, \ldots, P_n$ compiling summaries $T_i$ independently then solving $T = U; T_i$ with a cannulated loss.

$$
\begin{array}{c}
P \\
P_1 \\
T_1 \\
T_2 \\
T_b \\
J = U; T_i \\
S
\end{array}
$$

---

8. MLR-FFT is a two round MapReduce algorithm for approximating $K$-center on large dataset $P$, $|P| = N$.

Round 1: $P = P_x \cup \dots \cup P_e$ $|P_i| \approx N/l$

Run sequential FFT on each partition to obtain $T_i \in P_i$ $i \in [1, l]$

Round 2: map empty reduce: build coreset $T = \bigcup_{i=1}^l T_i$ $|T| = K/l$

then one reducer runs FFT to return set $S$ of centers

$M_L = O(\sqrt{Nu})$ $M_A = O(N)$

Quality: $\Phi_{u\text{center}}(P, S) \leq 4 \Phi_{u\text{center}}^{\text{opt}}(P, K)$

---

# 14. K-means++, Lloyd's algorithm and PAM

**Lloyd's algorithm** → Find good K-means clustering minimizing total squared distance

1. Initialize K centers
2. Assign each point to closest center
3. Replace each center by cluster centroid → automatic mean of points in cluster
4. Repeat until no change

- **Objective:** K-means
- **Centers:** any point in $R^0$, possibly outside P
- **Cost per iteration** O(NKD)
- **Fast for few iterations; distributable**
- **May coverage slowly or stop at local optimum**

**K-means++** → select first center uniformly at random

Randomized initialization, $C_k \sim \text{Uniform}(P)$. Given selected centers $S$, choose the next point with prob.

$$
\Pr(x \text{ next}) = \frac{d(x, S)^2}{\sum_{s \in S} d(y, S)^2}
$$

- repeat until $K$-centers selected

- **Objective:** mainly K-means
- **Centers:** $S \subset P$
- **Cost:** O(NKD)
- **Good for small $K$, can be processed on distib. platforms**

**PAM (Partitioning Around Medoids)**

Start with ScP, repeatedly choose best improving swap $s \in S \hookrightarrow p \in P/S$

Step when no swap improves objective

- **Obj:** K-median
- **Centers:** medoids $\rightarrow$ ScP
- **Sweep evaluation expensive $\rightarrow$ NK**
- **Good solutions, slow coverage**
- **Unsuitable for massive datasets**

**Medoid:** actual point in cluster minimizing total distance to all other cluster points

---

15. Weighted $K$-means is a variant where we use weights for every point of the dataset.

Weight $w(x)$ represents importance or multiplicity of point $x$.
Large weight means that point contributes more to objective.

A covet representing 1000 observations should not contribute the same as one representing $K$.

Input: set $P$ of $N$ points from $R^0$
Integer weight $w(x)$ $\forall x \in P$
Target number $K$ of clusters

Output: set $S$ of $K$ centers in $R^0$ minimizing

$$
\Phi^w(P, S) = \sum_{x \in P} w(x) d(x, S)^2
$$

In $K$-means, the probability changes from

$$
\pi(x) = \frac{d(x, S)^2}{\sum_{y \in P} d(y, S)^2} \rightarrow \frac{w(x) \cdot d(x, S)^2}{\sum_{y \in P} w(y) \cdot d(y, S)^2}
$$

---

16. MR-Kmeans ($A_1, A_2$): MR for $K$-means which 2 sequential algorithms $A_1$ and $A_2$ for $K$-means s.t.:

• $A_1$ solves the standard variant without weights
• $A_2$ solves the more weighted variant

Input: set $P$ of $N$ points in $IR^0$, integer $k > 1$ sequential $K$-means algo $A_1, A_2$

Output: set $S$ of $K$ centers in $IR^0$ which is good solution to the $K$-means problem on $P$

$R_1$:

• MP: partition $P$ arbitrarily in $2$ subsets of equal size $P_1, P_2$
• RP: for every $i \in [x_1, l]$ separately run $A_1$ on $P_i$ to determine a set $T_i$ of $K$-centers, and define

- $V \times eP$, proxy $\sigma(x)$ as $x$'s nearest center in $T_i$
- $V \gamma eT_i$, the weight $w(y)$ as the number of points of $P_i$ whose proxy is $y$

$R_2$:

• MP: empty
• RP: run, using a single reducer $A_2$ on $T = U_{im}^1 T_i$ to determine a set $S = \{c_1, \ldots, c_k\}$ of $K$ centers, which is then returned output

Generally we have $M_L = O(\max\{N/l, l \cdot k\}) = O(\sqrt{N \cdot k}) = O(N)$

$M_A = O(N)$

---

17. Definition of $(1 + \varepsilon)$-coreset

To evaluate the quality of a coreset, let $\varepsilon \in (a, 1)$ be an aqueeny parameter.

A subset $T \subset P$ is an $(1 + \varepsilon)$-coreset for diversity maximization problem on $P$ if:

$$
\text{div}^{\text{CPT}}(T, u) > \frac{1}{1 + \varepsilon} \text{div}^{\text{CPT}}(P, u)
$$

$= 0$ small $\varepsilon$, better solution

Also, diversity...

---

# STREAMING

1. A stream is a sequence $\Sigma = x_1, x_2, \ldots$ whose items arrive one at the time. A sequence can be bounded or unbounded.

A streaming algorithm must analyze massive or continuous data streams on the Fly using small, limited working memory without storing the data set.

**Evaluation with:**

- working memory: sublinear or polylogarithmic
- number of sequential passes: ideally one
- update time per item: ideally constant or logarithmic
- query time: independent of the stream length

**It can be**

- One pass: each item read once, required for live/unbounded streams

- Multi-pass: finite stored stream reused sequentially. Unsuitable if stream cannot be replaged

---

2. Boyer-Moore Majority vote

Given a stream $\Sigma = x_1, \ldots, x_n$, an item $a$ is a majority if its frequency exceeds n/2.

So it takes as an input the sequence $\Sigma$, then maintains two variables: candidate and integer count.

I select a candidate, say $A$. If I peek sequentially $\Sigma$ and find another $A$, count it, count -- otherwise.

If counter reaches 0, then switch candidate

[Theorem] Boyer-Moore Majority vote guarantee

If an item occurs more than n/2 times, Boyer-Moore returns that item

Proof (conclusion invariant)

After processing t items the prefix can be partitioned into count occurrences of count and $(t-1)\text{count}/2$ unequal pairs.

By induction:

• If old count is zero, new item becomes the single unpaired candidate occurrence
• If new item equals candidate, add it to unpaired candidate occurrences
• Otherwise, pair the new item with one previously unpaired candidate occurrence, count falls by one

If majority a existed, but find candidate differed, every occurrence of a would lie inside an unequal pair. Each such pair contains at most one a, so $f_a \leq n/2$, contradiction

---

4. Reservoir Sampling
with capacity $m$ on an unbounded stream $\leq$.

1. Initialization: store the first $m$ elements of the stream directly into reservoir $S$

2. Streaming update: for each item $x_{t+1}$, $t > m$, with prob. $m/t$ insert $x_{t+1}$ into $S$ and each a random existing element

We can prove it by taking an older record that has probability $\frac{m}{t-1}$ before $x_{t+1}$.

It is excited with conditional probability $\frac{1}{t}$, therefore

$$
P(x_{i} \in S_{t}) = \frac{m}{t-1} \left(1 - \frac{1}{t}\right) = \frac{m}{t}
$$

Working memory: $O(m)$ uses $S$

Update line: $O(1)$

---

5. Frequent Items and $E$-frequent Items for threshold $\phi$

For a threshold $\phi \in (0, 1)$ an item is frequent when $f_x > \phi m$.

The $E$-approximate frequent items problem requires an output $F$ satisfying:

1. every item with $f_x > \phi n$ belongs to $F$
2. no item with $f_x < (\phi - \varepsilon)n$ belongs to $F$
In the gray zone between $(\phi - \varepsilon)n$ and $\phi n$, we have tolerated frequency

$$
\phi - \varepsilon
$$

tolerated frequencies

target frequencies

---

6. Sticky sampling.

Is a probabilistic solution to the E-AFI problem using math table

$$
S = \{(x, f_c(x))\}
$$

where $f_c$ is estimated frequency

The sampling parameters are:

- Stream length $n$
- Frequency threshold $\Phi$
- Error Reference $\epsilon \in (0, \Phi)$
- Confidence parameter $\delta \in (0, 1)$

Samples at rate $r = \left\lfloor \frac{\ln(1/f_c \phi)}{\epsilon} \right\rfloor$

For each arrival $x$, if $x$ is already stored $\rightarrow$ counter[$x$] ++
else with prob. $p : \text{counter}[x] = x$, add it to $S$

As output, returns every stored $\geq \phi - \epsilon$ $n$

Working memory: $O(r) = O\left(\frac{\ln(1/f_c \phi)}{\epsilon}\right)$

Query time: $O(r)$

Update time: $O(1)$

Passes: 1 pass

---

7. Sticky sampling proof of working memory with $r$

* Working memory size: proportional to the number of entries in $S$ (assume each entry is $O(x)$). Now each $x_t$ contributes a new entry to $S$ with prob. $p_t \leq r/n$

$$
x_t = \begin{cases} 1 & \text{if } x_t \text{ contributes a new entry to } S \\ 0 & \text{otherwise} \end{cases}
$$

at the end of the stream $|S| = \sum_{t=1}^{n} x_t$

$$
\Rightarrow E[|S|] = E\left[\sum_{t=1}^{n} x_t\right] = \sum_{t=1}^{n} p_t \leq r
$$

$$
\Rightarrow WM \text{ size} = O(r)
$$

* 1 pass, $O(1)$ update time: straightforward

* Query time: $O(r)$ in expectation, immediate consequence of the fact that $E[|S|] = O(+)$

* Connectness: prove that prob is $\geq 1 - \delta$ the return at satisfies
(A) Output contains all the frequent items
(B) Output contains no item that occurs less than $(\phi - \varepsilon)$ n times.

(B) $\rightarrow$ immediate by construction
(A) $\rightarrow$ holds with probability $\geq 1 - \delta$.

$\alpha =$ arbitrary frequent item

$$
\Rightarrow \Pr(\alpha \text{ not returned in output}) \leq \Pr(\text{none of the first } \varepsilon n \text{ occurrences of } \alpha \text{ are satisfied}) = \left(1 - \frac{\kappa}{n}\right)^{\varepsilon n} \leq \left(1 - \frac{\kappa}{n}\right)^{\varepsilon n}
$$

$$
= \left(1 - \frac{\kappa}{n}\right)^{\varepsilon n} \cdot \frac{\kappa}{n} = \left((1 - \frac{1}{n})^{n/r}\right)^{\varepsilon r} \leq \left(\frac{1}{e}\right)^{\varepsilon r}
$$

Let $\alpha_1, \alpha_2, \dots, \alpha_n$ be all the frequent items we know $k \leq 1/\phi$. Now, $\Pr(3 \text{ some } \alpha_i \text{ not returned in the output}) \leq \delta$ (after oolcut.)

$$
\Rightarrow \Pr(\text{all frequent items are returned}) \geq 1 - \delta
$$

---

8. Output guarantees of sticky sampling
With probability at least $1-\delta$, return all items with frequency:

$$
f_x > \phi n \Rightarrow x \in S
$$

No false negatives for frequent items
Deterministically, 

$$
f_x < (\phi - \varepsilon)n \Rightarrow x \notin S
$$

No deep false positives
For grey zone

$$
(\phi - \varepsilon)n \leq f_x < \phi n
$$

Item may be returned or omitted.

---

10. Sketch: space efficient data structure that can be used to provide estimates of characteristic of a data-stream

Frequency moments: let $f_u$ be the frequency of an item $u$.
The $k$-th freq moment is

$$
F_u = \sum_{u \in U} f_u^u \quad \forall u > 0,
$$

Assuming $0^\circ = 0$ we have

$$
F_0 = \# \text{ distinct items in } \Sigma
$$

$$
F_1 = \# \text{ elements in sequence}
$$

$$
F_2 = \text{frequency concentration}
$$

Gini index gives infar an data impurity. Closer to 1, higher the impurity.

---

# 14. Probabilistic counting

chooses a uniform b-bit hash h: $U \rightarrow \{0, \dots, 2^{b-1}\}$ where $2^b > |U|$, let $tr(y)$ be the number of trailing zeros in binary $y$.

Maintain:

$$
R \leftarrow 0
$$

$$
V x_i \in \Sigma, \quad R \leftarrow \max\{R, tr(x_i)\}
$$

Return $\tilde{F}_0 = 2^R$

Reason: $\Pr[tr(h(x)) > j] = 2^{-j}$

$$
R = O(\log \log |U|) \text{ bits}
$$

$h$ described by $O(\log |U|) \text{ bits}$

Hence

$$
O(\log |U|) \text{ bits}
$$

---

19. Describe count-min sketch

is a space-efficient streaming data structure designed to estimate the individual frequencies $f_i$ of items in a streaming $\sum$ of length $n$ in a single pass.

Using: $dxw$ array of counters, each using $O(\log n)$ bits

High functions $h_j : U \rightarrow \{0, 1, \dots, w-1\}$

set all counters to zero

Init: $C[j, k] = 0 \quad \forall 0 \leq j < k \quad 0 \leq k < w$

For each occurrence $x_t$ in $\Sigma$, increment the mapped counter in every row

$C[j, h_j(x_t)] \leftarrow C[j, h_j(x_t)] + 1 \rightarrow$ update phase

Vog U at the end of the stream, its frequency can be estimated

$f_0 = \min_i C[j, h_j(v)] \rightarrow$ min value among its estimated mapper

---

15. Count-min sketch proof of accuracy

Consider a dxw count-min sketch for a stream $\Sigma$ of length $n$, where $d = \log_2(1/\delta)$ and $w = 2/\epsilon$, for some $\delta, \epsilon \in (0, 1)$. The sketch ensures that for any given $u \in U$ occurring in $\Sigma$

$$
\tilde{f}_0 - f_0 \leq \epsilon \cdot n
$$

with prob $> 1 - \delta$

**Proof**

Fix an arbitrary item $u \in \Sigma$.

Vow $j$ ($0 \leq j \leq d$) the error in the estimate of $f_0$ provided by row $j$ is $C[j, h_j(u)] - f_0$. Note that $C[j, h_j(u)]$ receives "in expectation" a fraction $w$ of the entire $n$ ($= \text{total num of elements in } \Sigma$).

$$
E[C[j, f_j(u)] - f_0] = \ldots = \frac{n}{w} = \frac{n - \epsilon}{2}
$$

We are interested in $\Pr(C[j, h_j(u)] - f_0 > \epsilon n)$

By Markov's inequality

$$
\Pr(C[j, h_j(u)] - f_0 > \epsilon n) = \Pr(C[j, h_j(u)] - f_0 > \frac{2\epsilon n}{2}) \leq \frac{\epsilon}{2}
$$

Then:

$$
\Pr[\tilde{f}_0 - f_0 > \epsilon n] = \Pr(V_0 \leq j < d \quad C[j, h_j(u)] - f_0 > \epsilon n) = \ldots \leq \left(\frac{1}{2}\right)^\phi
$$

Since $d = \log_2(1/\delta)$

$$
\left(\frac{1}{2}\right)^\phi = \delta
$$

Therefore, $\Pr(\tilde{f}_0 - f_0 \leq \epsilon n) > 1 - \delta$

---

17. Count-sketch is an unbiased version of Count-min
Initialize $d$ sw counters to zero.
For each row $j$, choose independent hashes:

$$
h_j : U \rightarrow \{0, \dots, w-1\} \quad \forall j
$$

$$
g_j : U \rightarrow \{-1, 1\} \quad \forall j
$$

For each $u \in U$ multiply its contribution to each row by a value $\{x, u\}$ randomly selected so to conceal all collisions.

Accuracy analysis: for any given $u \in U$ occurring in $\Sigma$

$$
\tilde{g}_u - f_u \leq \mathcal{E} \cdot w
$$

 with prob. $\geq 1-\delta$

Fix $u \in U$ and $j \in [0, d-1]$ arbitrarily. We now show that $E[\tilde{g}_u] = f_u$. Recall that $\tilde{g}_u = g_j(u) \cdot C[j, h_j(u)]$.

For every $a \in U$ a not $u$ we define a random var $Y_a$ which represents the contribution of $a$ to $f_u j$.

$$
Y_a = \begin{cases} g_a & \text{if } h_j(a) = h_j(u) \text{ AND } g_j(a) = g_j(u) \\ -g_a & \text{if } h_j(a) = h_j(u) \text{ AND } g_j(a) = -g_j(u) \\ 0 & \text{otherwise} \end{cases}
$$

It is easy to see that $f_u j = f_u + \sum_{a \in U} Y_a$.

Now observe that

$$
\begin{aligned}
\Pr(Y_a = f_u) &= \frac{1}{w} \cdot \frac{1}{2} \\
\Pr(Y_a = -f_u) &= \frac{1}{w} \cdot \frac{1}{2} \\
\Pr(Y_a = 0) &= 1 - \frac{1}{w}
\end{aligned}
$$

We have:

$$
E[\tilde{g}_u] = E[f_u] + \sum_{a \in U} Y_a = f_u + E[\sum_{a \in U} f_u] = f_u + \sum_{a \in U} E[Y_a]
$$

And $E[Y_a] = \dots = 0 \implies E[\tilde{g}_u] = f_u + \sum_{a \in U} f_u = f_u$

---

24. Bloom filter

Represents a set $S$ of $m$ elements with an $n$-bit array $A_i$ initialized to zero, and $K$ independent hashes.

$$
h_j : U \rightarrow \{0, \dots, n-1\}
$$

Insert $x$: set $A[h_j(x)] = 1 \quad \forall j$

Query $x$: if every $A[h_j(x)] = 1$ return possible present

else if $A[h_j(x)] = 0$ return possible absent

After insertions, it has no false negatives because if $x$ was inserted, then set all its portions to $1$.

A standard Bloom filter does not reset bits, therefore every inserted item passes query:

$$
x \in S \Rightarrow \text{Query}(x) \text{ present}
$$

False positives remain possible because other items may set some bits

For costs, if we assume $O(n)$-time hashes

$$
\text{Update} = O(k), \quad \text{Query} = O(k)
$$

---

# SIM SEARCH

1. Let $(M, d)$ be metric space, $P \in M$, query $q$, radius $r > 0$

(2) $r$-Near Neighbour search ($r$-NNS)

Define ball of radius $r$:

$$
B_r(q) = \{ p \in M : d(p, q) < r \}
$$

Return:

$$
\begin{cases} p \in P \cap B_r(q) & \text{if one exists} \\ \text{null} & \text{otherwise} \end{cases}
$$

(b) $(c, r)$ - Approximate NNS

For $c > 1$

• If some $p^* \in P$ satisfies $d(p^*, q) < r$, must return some $p \in P$ with $d(p, q) < r$

• Else if no point lies within $r$, return null or a point within distance $r$.

• Never return a point with distance $r > r$

---

3. Range Reporting (RR)

given $P \in R^0$ and axis-aligned rectangle

$$
R = [a_1, b_1] \times \ldots \times [a_0, b_0]
$$

return all points in $R \cap P$. RR asks for all point in a rectangle while $r$-MNS asks for one point in a metric ball.

For a balanced $k$-d-tree in $R^2$, for $n = |P|$ and $K = |P \cap R|$:

Space = $O(n)$
Query time = $O(\sqrt{n} + k)$

---

4. A Kid-tree (in $12^2$) is a balanced binary space partition tree.

Let $P$ be a set of $N$ points in $12^2$ and $R(P) \subset 12^2$ be a rectangular region containing all points in $P$.

The Kid-tree defines hierarchical decomposition of $R(P)$ into nested rectangular subregions.

- Leaves points
- Internal nodes are associated to a rectangular region denoted as region($v$)

Using a Kid-tree we can solve efficiently $R(P)$ in Space $O(n)$ and query time $O(\sqrt{N} + n)$

---

8. LSH family

Family $H$ is $(p_1, p_2, c, r)$-locality sensitive if, for random $h \in H$

$$
d(p, q) \leq r \Rightarrow \Pr_{h \sim H} [h(p) = h(q)] \geq p_1
$$

$$
d(p, q) > cr \Rightarrow \Pr_{h \sim H} [h(p) = h(q)] \leq p_2
$$

where $0 \leq p_2 < p_1 < 1$, $c > 1$. No condition for $r < d(p, q) < cr$

Basic LSH structure:

Construction:

1. Choose random $h \in H$
2. Build hash table

   $$
   T[i] = \{p \in P : h(p) = i\}, \quad i \in [0, t]
   $$

Query $q$:

1. Compute $h(q)$
2. Scan bucket $T[h(q)]$
3. Return first $p$ with

   $$
   d(p, q) \leq cr
   $$

   If none exists, return null

Query $hme$ is $O(Dnp_2) = 0$ because $\Pr(h(p) = h(q)) \leq p_2$

Space $O(Dn)$

---

# Questions from previous exams

1. Define $M_L$ and $M_A$
   $M_L =$ local space, is the max amount of main memory used by one map/reduce invocation
   $M_A =$ aggregate space, is the size of the total memory stored between the clusters

2. Weighted $k$-means and coresets
   For weights $w(x) > 0$, minimize

   $$
   \phi^w(P, S) = \sum_{x \in P} w(x) d(x, S)^2
   $$

   Using coresets:
   1. Partition $P$ into $P_1, \ldots, P_k$
   2. Compute $k$ local centers $T_i$ per partition
   3. Give each $y \in T_i$ weight, where $w(y)$ is the number of $x \in P$ such that $y$ is closest local center to $x$.
   4. Run weighted $k$-means on $T = U; T_i$

3. Bloom filter
   Represents a set $S$ of $n$-bit array $A$, initialized to zero, and $K$ independent hashes

   $$
   h_j : U \rightarrow \{0, \ldots, n-1\}
   $$

   Insert $x :$ set $A[h_j(x)] = 1$
   Query $x :$ if every $A[h_j(x)] = 1$ return possibly present
   else if $A[h_j(x)] = 0$ return possibly absent
   After insertions, it has no false negatives because if $x$ was inserted, from set all its positions to $x$.
   A standard Bloom filter does not reset bits, therefore every inserted item passes query:

   $$
   x \in S \Rightarrow \text{Query}(x) \text{ present}
   $$

---

False positives remain possible because other items may set same bits.

For costs, if we assume $O(n)$-time hashes

$$
\text{Update} = O(n), \quad \text{Query} = O(n)
$$

4. Kd-tree

A Kd-tree (in $12^2$) is a balanced binary space partition tree.

Let $P$ be a set of $N$ points in $12^2$ and $R(P) \le 12^2$ be a rectangular region containing all points in $P$.

The Kd-tree defines hierarchical decomposition of $R(P)$ into nested rectangular subregions.

- Leaves stores points
- Internal nodes are associated to a rectangular region denoted as region($n$)

Using a Kd-tree we can solve efficiently $RR$, in

$$
\text{Space} = O(n) \quad \text{and} \quad \text{query time} = O(\sqrt{N} + n)
$$

---

# Spark / Homework Description

## HW4

**Problem:** Input, set $U \subseteq \mathbb{R}^P$. Every point has
- coordinates $p = (x_1, \ldots, x_0)$
- group label $g_P \in \{A, B\}$

Algorithm must select center set $S \subseteq U$ containing

$$
K = K_A + K_B
$$

**points**

**Objective:** find the distance between $x$ and nearest selected center, $Vx$. Then, select the largest of these distances.

**Fair-FFT:** after choosing some centers, select the point furthest from its nearest center

It takes as input $U, KA, KB$, then maintains:
- 'S': centers selected so far
- 'countA', 'countB': consumed group quotas;
- 'minDist[i]': current distance from point $U[i]$ to its nearest center in 'S'

**Important optimization:** no recompiling each point's distance from every old center

It has a complexity of:
- Time: $O(NKD)$
- Space: $O(N + K)$

**MR-Fair-FFT:** Distributed, uses Spark Partitions and two rounds

**Round 1:**

RDD (Resilient Distributed Dataset) is divided into $L$ Spark partitions. Within each partition

1. mapPartitions converts its iterator into local list partitionDate
2. runs Fair-FFT
3. emits only selected local centers

---

# Round 2

1. Local coresets are merged and collected on the driver
2. Driver executes FairFFT on $T$, $K_A$, $K_B$
3. Final set $S$ contains requested group quotes.

# HW2

**Problem:** frequent items with Spark streaming

Given an unbounded stream of integers, program analyzes exactly its first $n$ valid items. Frequency of item $x$ is:

$$
f_x = \#\{ \text{occurrences of } x \text{ among first } n \text{ items} \}
$$

Frequent when $f_x > \phi_n$

**Pipeline:**

1. Socket Text Stream to connect to the website
2. Spark Streaming groups incoming data into batches
3. ForeachROD involves process_batch on each batch
4. Record passed as integers
5. toLocal Iterator(C) delivers batch records to driver one at a time
6. compilation of remaining $n$-streamLength and stops inside batch at the $n$-th valid item
7. threading event signals main thread

---

Redo questions

2. [3 points] The coreset-based MapReduce algorithm for $k$-means computes the final centers of the clusters by running a sequential algorithm $A$ on a weighted coreset $T$.

(a) How are the points in $T$ computed?

(b) For each point $q \in T$, what does its weight $w(q)$ represent?

(a) First, on coreset-based MapReduce for $k$-means, all the points are computed in the first round with an algo. A that does not consider the points weight.

Then, on Round 2, the $k$-centers are computed considering also the weight of each point.

(b) The weight $w(q)$ tells us how frequent/important is our point in the cluster.

![Figura estratta 1](images/Questions-p42_img01.jpg)
