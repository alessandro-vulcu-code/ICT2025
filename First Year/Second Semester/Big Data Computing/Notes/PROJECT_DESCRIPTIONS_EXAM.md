# Big Data Computing – Detailed Description of Both Projects

## Overview

Both projects address problems where input is too large to handle with a straightforward exact method:

1. **HW1 – Fair k-Center:** select a small, representative set of centers from a massive point set while satisfying demographic quotas. It uses sequential `Fair-FFT` and two-round distributed `MR-Fair-FFT`.
2. **HW2 – Frequent Items:** find high-frequency values in a stream without storing one counter for every possible value. It compares `Sticky Sampling` with `Count-Min Sketch`.

---

## Project 1 – Fair k-Center with MR-Fair-FFT

### 1. Problem definition

Input is a set of points $U \subseteq \mathbb{R}^D$. Every point has:

- coordinates $p=(x_1,\ldots,x_D)$;
- a group label $g_p\in\{A,B\}$.

The algorithm must select a center set $S\subseteq U$ containing

$$
k=k_A+k_B
$$

points: exactly $k_A$ from group A and $k_B$ from group B.

Its objective is

$$
r(S)=\max_{x\in U}\operatorname{dist}(x,S)
=\max_{x\in U}\min_{s\in S}\lVert x-s\rVert_2.
$$

For every input point, we find its distance from its nearest selected center. The objective is the largest of these distances. Minimizing it means covering the whole dataset with the smallest possible worst-case radius.

Fairness constrains **which points may become centers**. It does not constrain point-to-center assignments: any point can be served by its nearest center, regardless of group.

### 2. Sequential Fair-FFT

FFT means **Farthest-First Traversal**. Its greedy idea: after choosing some centers, select the point currently worst served by them—the point farthest from its nearest center.

Fair-FFT adds separate group budgets.

#### Maintained state

`fairFFT(U, KA, KB)` maintains:

- `S`: centers selected so far;
- `countA`, `countB`: consumed group quotas;
- `minDists[i]`: current distance from `U[i]` to its nearest center in `S`.

`minDists` is an important optimization. The algorithm does not recompute each point's distance from every old center after every selection.

#### Step-by-step operation

1. Compute $k=k_A+k_B$.
2. Choose the first point whose group has a positive budget.
3. Initialize each cached distance:

   $$
   d_i=\operatorname{dist}(u_i,S).
   $$

4. Until $k$ centers have been chosen:
   - reject A candidates when `countA == KA`;
   - reject B candidates when `countB == KB`;
   - among eligible candidates, choose the one maximizing `minDists[i]`;
   - add it to `S` and update its group's counter;
   - update every cached distance using

     $$
     d_i\leftarrow\min(d_i,\lVert u_i-s_{new}\rVert_2).
     $$

Once one group exhausts its budget, all remaining centers must come from the other group.

#### Small example

Assume $k_A=1$ and $k_B=1$. If the first center belongs to A, A's budget is immediately exhausted. The second center must therefore belong to B. Among B points, the algorithm selects the one farthest from the first center.

#### Why this strategy is useful

Every iteration attacks the current worst-covered region among eligible candidates. Selected centers spread across the dataset rather than concentrating in one dense region.

The method is greedy: it makes the best current choice instead of exploring all possible center combinations. The fairness constraint can force a geometrically worse choice than unconstrained k-center because a far point may belong to a group whose quota is already exhausted.

#### Complexity

Let $N=|U|$, $k=k_A+k_B$, and $D$ be point dimension.

- Time: $O(NkD)$.
- Additional memory: $O(N+k)$, excluding input storage.

Each of $k$ selections scans $N$ points and computes one $D$-dimensional Euclidean distance per point. Cached minimum distances keep each iteration at $O(ND)$.

### 3. Distributed MR-Fair-FFT

The full dataset may be too large for one machine. `MRFairFFT` therefore uses Spark partitions and two rounds.

#### Round 1: local coreset construction

RDD `rddU` is divided into $L$ Spark partitions. Within each partition:

1. `mapPartitions` converts its iterator into local list `partitionData`;
2. it runs `fairFFT(partitionData, kPrimeA, kPrimeB)`;
3. it emits only selected local centers.

The program uses

$$
k'_A=2k_A,\qquad k'_B=2k_B.
$$

Thus each partition emits at most $2k_A+2k_B=2k$ points. Their union is coreset $T$, whose maximum size is $2kL$.

A **coreset** is a small summary designed to preserve important geometric structure. Farthest-first selection tends to retain remote or poorly covered regions that a random sample could miss.

Oversampling by factor two gives each partition more representatives from both groups. This can improve final accuracy, but increases communication, driver memory, and Round 2 cost.

#### Round 2: global center selection

1. Local coresets are merged and collected on the driver.
2. The driver executes

   $$
   \texttt{fairFFT}(T,k_A,k_B).
   $$

3. Final set $S$ contains requested group quotas, provided input preconditions hold and coreset contains enough eligible points.

Core idea: reduce $N$ original points to at most $2kL$ candidates, then solve final problem on this compact representation.

#### Complete Spark data flow

1. `sc.textFile(filePath, minPartitions=L)` reads CSV in distributed form.
2. `parseLine` converts each row to `(coordinate_tuple, group)`.
3. Resulting RDD is persisted with `DISK_ONLY` because later actions reuse it.
4. `mapPartitions` and `reduce` compute $N_A$, $N_B$, and $N$.
5. `MRFairFFT` constructs local coresets and final solution.
6. A final distributed pass computes true objective value over all original points:

   $$
   \max_{x\in U}\min_{s\in S}\lVert x-s\rVert_2.
   $$

Reported running time covers only `MRFairFFT`; input loading, counting, and final objective computation are excluded.

#### Distributed cost

Approximate costs:

- Round 1: $O(Nk'D)$, divided among workers;
- communication to driver: at most $O(k'L)$ points;
- Round 2: $O(k\,k'LD)$;
- final objective evaluation: $O(NkD)$, distributed.

Partition count $L$ creates a trade-off:

- larger $L$: more parallelism and smaller local partitions;
- but also more tasks, more scheduling overhead, a larger coreset, and more driver work.

Stored HW1 results illustrate this. On 13 million points, increasing $L$ from 10 to 200 greatly reduces running time through extra parallelism, while objective remains close. Very large $L$, however, eventually increases overhead and coreset size.

### 4. Important implementation details and limitations

- First center depends on input order. Reordering or repartitioning data can change selected centers.
- Coreset is collected on driver. Method is scalable only while $2kL$ remains manageable.
- Every partition is converted into a Python list. Each individual partition must fit executor memory.
- Code does not explicitly verify $k_A\leq|U_A|$ and $k_B\leq|U_B|$, although these are required problem preconditions.
- `parseLine` interprets every label other than `A` as `B`; malformed labels are not rejected.
- Previously selected points are not explicitly excluded. Normally positive distances favor new points, but duplicate coordinates or insufficient local group members can cause duplicate selections.
- Saved `AllA` experiment requests $k_B=4$ while $N_B=0$. This violates problem preconditions. Returned A-only set is not a valid fair solution for requested quotas.

### 5. Short oral-exam answer

> [!summary] Oral-exam answer
> Fair k-center minimizes maximum distance from every point to its nearest center while requiring exactly $k_A$ A centers and $k_B$ B centers. Fair-FFT repeatedly selects the eligible point farthest from current centers and blocks a group after its quota is exhausted. MR-Fair-FFT runs this procedure inside every Spark partition to build a coreset, collects at most $2kL$ candidates, and runs Fair-FFT again with final quotas. Original dataset remains distributed; only compact coreset reaches driver.

---

## Project 2 – Frequent Items with Spark Streaming

### 1. Problem definition

Program receives an unbounded stream of integers but analyzes exactly its first $n$ valid items. True frequency of item $x$ is

$$
f_x=\#\{\text{occurrences of }x\text{ among first }n\text{ items}\}.
$$

An item is truly frequent when

$$
f_x\geq\phi n,
$$

where $\phi$ is a relative threshold.

An exact dictionary may require memory proportional to number of distinct items. Project compares two approximate structures designed to use much less memory.

Code also maintains `trueFrequencies`, an exact histogram used as experimental ground truth and to print true frequencies. This dictionary is not part of memory advantage offered by approximate algorithms; a production memory-limited stream processor would normally not keep it.

### 2. Stream processing pipeline

1. `socketTextStream` connects to `algo.dei.unipd.it` on requested port.
2. Spark Streaming groups incoming data into 0.1-second micro-batches.
3. `foreachRDD` invokes `process_batch` on each batch.
4. Records are parsed as integers; malformed records are ignored.
5. `toLocalIterator()` delivers batch records to driver one at a time.
6. Code computes `remaining = n - streamLength` and stops inside batch exactly at the $n$-th valid item.
7. `threading.Event` signals main thread. Streaming context is stopped outside callback to avoid deadlock.

Both approximate algorithms process same prefix of $n$ items and update driver-side state.

### 3. Sticky Sampling

#### Parameters

Sticky Sampling uses:

- $\phi$: frequency threshold;
- $\epsilon$: accuracy tolerance, where $0<\epsilon<\phi$;
- $\delta$: failure-probability/confidence parameter.

Sampling rate is

$$
r=\frac{\ln(1/(\delta\phi))}{\epsilon}.
$$

Insertion probability is

$$
p=\min\left(\frac{r}{n},1\right).
$$

#### Update rule for each item $x$

- If $x$ is already in `stickySample`, increment its counter.
- Otherwise insert it with probability $p$, setting counter to 1.
- If random test fails, forget current occurrence. A later occurrence gives another insertion opportunity.

Once inserted, item remains in dictionary and every later occurrence is counted. Sticky counter therefore equals occurrences observed **from successful sampling onward**. It is neither true frequency nor a value rescaled by $1/p$.

#### Output rule

Returned set is

$$
F_{SS}=\{x:\widehat f^{SS}_x\geq(\phi-\epsilon)n\}.
$$

Lower threshold $(\phi-\epsilon)n$ compensates for occurrences lost before item entered sample.

#### Probabilistic intuition

A rare item has few chances to be sampled. A frequent item appears many times and receives many independent opportunities. Probability that item is never sampled after $f_x$ occurrences is

$$
(1-p)^{f_x}\leq e^{-pf_x}.
$$

Thus frequent elements enter dictionary with high probability. Smaller $\epsilon$ or smaller $\delta$ increases $r$ and $p$: accuracy or confidence improves, while dictionary becomes larger.

#### Possible errors

- **False negative:** frequent item may be sampled too late, leaving stored counter below output threshold.
- **Near-frequent result:** item with true frequency between $(\phi-\epsilon)n$ and $\phi n$ may be returned.
- Stored counter never exceeds true frequency. Therefore code cannot return an item whose true frequency is below $(\phi-\epsilon)n$.

#### Complexity

- Expected update time: $O(1)$ per item.
- Memory: $O(|\texttt{stickySample}|)$, random and indirectly controlled by $r$.
- Independent of numeric size of item domain.

### 4. Count-Min Sketch

#### Data structure

Count-Min Sketch is a $d\times w$ matrix of counters:

$$
CM[0\ldots d-1][0\ldots w-1].
$$

Each row uses an independently parameterized hash function

$$
h_j(x)=((a_jx+b_j)\bmod8191)\bmod w,
$$

where $a_j\in[1,8190]$ and $b_j\in[0,8190]$.

#### Update rule for each item $x$

For every row $j$:

1. compute $c=h_j(x)$;
2. increment `CM[j][c]`;
3. estimate frequency with minimum of all addressed counters:

   $$
   \widehat f^{CM}_x=\min_j CM[j,h_j(x)].
   $$

Item is added to `F_CM` first time

$$
\widehat f^{CM}_x\geq\phi n.
$$

Counters only increase, so once item crosses threshold it remains in `F_CM`. Checking during stream is equivalent to checking final estimate for every observed item, but avoids needing to enumerate sketch keys later.

#### Why minimum is used

Every addressed counter includes occurrences of $x$ plus occurrences of colliding items. A single row may therefore overestimate heavily. Large error in final estimate requires unfavorable collisions in every row; minimum chooses least contaminated row.

Fundamental property:

$$
\widehat f^{CM}_x\geq f_x.
$$

Count-Min never underestimates. Therefore every true frequent item reaches threshold: no false negatives, assuming exact processing of first $n$ items. Hash collisions can create false positives.

#### Roles of $d$ and $w$

- Larger $w$: fewer collisions and smaller error, but more memory.
- Larger $d$: lower probability that every row is badly contaminated, but more work per item.

In standard theoretical parametrization, $w$ controls additive error and $d$ controls failure probability. Here both are direct command-line parameters.

#### Complexity

- Update time: $O(d)$ per item.
- Matrix memory: $O(dw)$, independent of distinct-item count.
- Result-set memory: $O(|F_{CM}|)$.

### 5. Direct comparison

| Aspect | Sticky Sampling | Count-Min Sketch |
|---|---|---|
| Mechanism | Randomly starts tracking items | Shares counters through hashing |
| State | Dynamic item-to-counter dictionary | Fixed $d\times w$ matrix plus result set |
| Time per item | Expected $O(1)$ | $O(d)$ |
| Error source | Missed prefix before sampling | Hash collisions |
| False negatives | Possible with controlled probability | None at threshold $\phi n$ |
| False positives | Mainly near threshold | Possible, even for rare items after heavy collisions |
| Memory parameter | $\phi$, $\epsilon$, $\delta$ through $r$ | $d,w$ directly |
| Randomness | Sampling decisions | Hash-function parameters |

Provided example shows typical Count-Min behavior: it returns one item whose true frequency is 1 because collisions inflated its estimate. Sticky Sampling mainly returns truly frequent or near-frequent elements.

### 6. Experimental driver

`run_hw2_experiments.py` performs 18 runs:

- vary $\epsilon$ over 0.01, 0.02, 0.04 for Sticky Sampling;
- vary $w$ over 15, 30, 60 for Count-Min;
- repeat each configuration three times;
- classify returned items as frequent, almost frequent, or rare using true frequency;
- compute averages and save CSV files.

Repeated runs remain necessary even on deterministic port 8888 because sampling decisions and hash functions are random.

Expected trends:

- increasing $\epsilon$ decreases $r$ and $p$: Sticky dictionary tends to shrink, while accuracy worsens;
- increasing $w$ reduces Count-Min collisions and false positives;
- increasing $d$ improves reliability but increases processing time.

### 7. Important implementation details and limitations

- `trueFrequencies` can grow to number of distinct items. It is evaluation-only state, not streaming-memory solution.
- `toLocalIterator()` avoids collecting entire batch at once, but both algorithms are updated sequentially on driver.
- Spark Streaming has at-least-once semantics. After failure, a batch may be processed twice; code has no deduplication or checkpoint recovery.
- Initial modulo 8191 maps numbers congruent modulo 8191 identically in every row. This follows assignment specification but is a practical weakness over arbitrary 32-bit integers.
- `F_CM` is needed because sketch estimates queried keys but cannot enumerate frequent keys by itself.
- Environment variable `G26HW2_RANDOM_SEED` enables reproducible tests without changing required command-line interface.

### 8. Short oral-exam answer

> [!summary] Oral-exam answer
> Project reads first $n$ integers from Spark DStream and compares two frequent-item methods. Sticky Sampling starts tracking an unseen item with probability $p=r/n$, then counts all later occurrences; it returns counters above $(\phi-\epsilon)n$. It uses small expected memory but can miss an item sampled too late. Count-Min increments one cell in each of $d$ hash rows and estimates frequency with their minimum. It never underestimates, so it does not miss true frequent items, but collisions produce false positives. Width $w$ reduces collisions; depth $d$ improves confidence.

---

## Connection between both projects

Both projects reduce data while preserving information needed for a final decision:

- HW1 compresses a geometric dataset into a coreset;
- HW2 compresses a frequency distribution into a sample or sketch.

Main difference:

- HW1 uses distributed batch processing: local computation, summary communication, global decision;
- HW2 uses online processing: each element is seen once and updates compact state.

Key exam idea: Big Data algorithms often accept controlled approximation to reduce memory, communication, or execution time. Quality depends on parameters: $k'$ and $L$ for coreset; $\epsilon$ and $\delta$ for Sticky Sampling; $d$ and $w$ for Count-Min Sketch.
