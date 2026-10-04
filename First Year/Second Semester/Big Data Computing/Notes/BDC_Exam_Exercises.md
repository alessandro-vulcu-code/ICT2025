# BDC Exam Exercises

## MapReduce

1. A cluster has 10 machines, each with 8 GB of RAM and 128 GB of disk. Round inputs and
   outputs reside in HDFS across these disks. Ignoring replication and system overhead,
   determine the largest feasible $M_L$ and $M_A$. How do these limits change when HDFS
   uses replication factor $b$? State the general resource conditions for running an
   algorithm with given $M_L$ and $M_A$.
   ([Example WT 1, Part 1.1](../Slides/Exercises/Exams/ExampleWT-1.pdf);
   [Example WT 4, Part 1.1](../Slides/Exercises/Exams/ExampleWT-4.pdf))

2. A MapReduce algorithm receives $N$ web documents represented by $(\mathrm{url},D)$,
   each occupying $O(1)$ space. Describe a map phase that creates $\lceil\sqrt N\rceil$
   small partitions. Determine the expected size of a fixed partition and state a
   high-probability bound on the largest partition. How would you partition $N$ records
   whose original keys are all zero?
   ([19/07/2023, Question 1](../Slides/Exercises/Exams/Questions/19-07-2023/Questions.jpg);
   [14/07/2025, Question 1](../Slides/Exercises/Exams/Questions/14-07-2025.txt))

3. Given integer records $(i,x_i)$ with $0\leq i<N$, compute their arithmetic mean in
   two MapReduce rounds using $M_L=O(\sqrt N)$ and $M_A=O(N)$. Modify the algorithm to
   use $M_L=O(N^{1/4})$, and determine the round count. Generalize to local budget
   $O(M)$ for $2\leq M<\sqrt N$. Why can averaging local averages be incorrect?
   ([EX-MR 1](../Slides/Exercises/EX-MR2526.pdf))

4. Given $(i,x_i)$ with $0\leq i<N$, design a simple two-round algorithm for the exact
   number of distinct values. Identify its worst-case local-space bottlenecks. Then
   design an $O(1)$-round algorithm with $M_L=O(\sqrt N)$ and $M_A=O(N)$, including
   the final aggregation of the number of distinct values.
   ([EX-MR 2](../Slides/Exercises/EX-MR2526.pdf))

5. Design an $O(1)$-round algorithm for $W=AV$, where $A$ is a dense $m\times n$
   matrix, $V$ is an $n$-vector, and $m\leq\sqrt n$. Specify the input representation
   and obtain $M_L=o(n)$ and $M_A=O(mn)$. Account for replication and mapper output.
   How would you modify the algorithm for larger $m$?
   ([EX-MR 4](../Slides/Exercises/EX-MR2526.pdf))

6. A dataset contains records $(i,(s_i,t_i))$, where $i\in[0,N-1]$ is distinct,
   $s_i$ is a sensor, and $t_i$ is a temperature. For constant $K>0$, design a two-round
   algorithm that returns all records of sensors with at most $K$ records and exactly
   $K$ arbitrarily chosen records for every other sensor. Prove correctness and obtain
   $M_L=o(N)$ and $M_A=O(N)$ without assumptions on sensor frequencies. How do the
   bounds change for $K=\lceil\log_2N\rceil$?
   ([EX-MR 5](../Slides/Exercises/EX-MR2526.pdf);
   [Example WT 3, Part 2.1](../Slides/Exercises/Exams/ExampleWT-3.pdf))

7. A dataset has $N$ slot-machine outcomes $(i,(s_i,o_i))$ with distinct sequential IDs.
   Outcome $o$ is frequent for machine $s$ if $(s,o)$ occurs at least $N/50$ times;
   a machine is biased if it has a frequent outcome. Design a three-round algorithm
   returning exactly one $(s,\mathrm{null})$ for each biased machine, with
   $M_L=o(N)$ and $M_A=O(N)$. Prove the bound on the final reducer input.
   ([Example WT 1, Part 2.1](../Slides/Exercises/Exams/ExampleWT-1.pdf);
   [21/06/2022, EX-1 A](../Slides/Exercises/Exams/sol210622.pdf))

8. An online store has $N$ purchase records $(i,(c_i,p_i))$ with distinct sequential
   IDs. A customer is compulsive if some customer-product pair occurs at least $N/50$
   times. Design a three-round algorithm returning each compulsive customer once,
   using $M_L=o(N)$ and $M_A=O(N)$.
   ([21/06/2022, EX-1 B](../Slides/Exercises/Exams/sol210622.pdf))

9. A $t\times t$ grid receives $N$ connections $(k,(i,j))$, where $k\in[0,N-1]$ is
   distinct and $t=O(\sqrt N)$. Design a three-round algorithm returning $(i,t_i)$
   exactly for rows with more than $t/2$ occupied cells, where $t_i$ counts distinct
   occupied cells in row $i$. Repeated connections to a cell are unrestricted. Prove
   correctness and obtain $M_L=o(N)$ and $M_A=O(N)$.
   ([Example WT 5, Part 2.1](../Slides/Exercises/Exams/ExampleWT-5.pdf);
   [18/06/2025, Exercise 1](../Slides/Exercises/Exams/18-06-25.pdf))

10. Let $P$ contain $N$ points represented by $(i,x_i)$ with distinct sequential IDs,
    and let $Q=\{q_1,\ldots,q_k\}$ be global query points with $k\leq\sqrt N$.
    Design a two-round algorithm returning, for each $q\in Q$, a nearest point
    $q^P\in P$. Obtain $M_L=o(N)$ and $M_A=O(N)$, including the size of local
    summaries and copies of $Q$. How do the costs and choice of partition count change
    for $\sqrt N<k=o(N)$?
    ([08/09/2023, Part 2.1](<../Slides/Exercises/Exams/08-09-2023/Part 2.jpg>))

11. A mapper emits $L$ records per input point, each containing a vector of $k$ numbers.
    What contributions does this make to local and aggregate space in the course model?
    Explain why counting keys without counting payload sizes can invalidate an analysis.

12. In a two-round aggregation, each of $L$ balanced partitions emits at most $k$
    representatives. Compare gathering all representatives in one reducer with grouping
    them into $k$ separate reducers. Derive the corresponding local-space bounds and
    explain why their optimal partition counts can differ.

13. For the older frequent-itemset problem, let $I=I_1\cup I_2$ with disjoint parts.
    An itemset is fair if half its items belong to each part. Let $F_{2k}$ contain the
    frequent fair itemsets of size $2k$ at a fixed support threshold. Two members are
    compatible when they share exactly $k-1$ items from each part. For $k\geq2$, define
    $C_{2k+2}=\{X\cup Y:X,Y\in F_{2k},\ X,Y\text{ compatible}\}$.
    Prove that $F_{2k+2}\subseteq C_{2k+2}$.
    ([13/07/2022, Exercise 2; older syllabus](../Slides/Exercises/Exams/sol130722.pdf))

## Coreset

1. Given points $(\mathrm{ID}_x,x)$ with distinct IDs and a global set $S$ of $k$ centers,
   assign each point to its nearest center in one MapReduce round using $M_L=O(k)$.
   Specify tie breaking and analyze aggregate space, including the assumptions needed
   when copies of $S$ are counted.
   ([EX-CTCL 2](../Slides/Exercises/EX-CTCL2526.pdf))

2. Run FFT on $P=\{0,2,3,9,10,17\}\subset\mathbb R$ with $k=3$, starting at $0$
   and breaking ties toward the smaller coordinate. Give the selection sequence,
   nearest-center distances after each iteration, final clusters, and final radius.

3. Define the diameter $\Delta(P)$ of a metric point set. For an arbitrary $x\in P$,
   derive and prove the approximation ratio of
   $\Delta_x=\max_{y\in P}d(x,y)$. Compute $\Delta_x$ in two MapReduce rounds
   with $M_L=O(\sqrt N)$ and $M_A=O(N)$ when $x$ is globally available.
   ([EX-CTCL 8](../Slides/Exercises/EX-CTCL2526.pdf))

4. Let $P=\{x_0,\ldots,x_{N-1}\}$ and let $S[1],\ldots,S[k]$ be global centers
   outside $P$, with $k=O(\sqrt N)$. Every point has a unique nearest center.
   Design a two-round algorithm selecting one input point from each nonempty induced
   cluster, using $M_L=o(N)$ and $M_A=O(N)$. For the resulting set $T$, derive a
   diameter guarantee in terms of $R=\max_{x\in P}d(x,S)$ and explain the effect
   of centers not belonging to $T$.
   ([EX-CTCL 6](../Slides/Exercises/EX-CTCL2526.pdf);
   [29/06/2023, Exercise 1](../Slides/Exercises/Exams/Questions/29-06-2023/Questions.txt))

5. Design an exact diameter algorithm for points $(i,x_i)$ with $0\leq i<N$, using
   $O(1)$ MapReduce rounds, $M_L=O(\sqrt N)$, and $M_A=O(N^2)$. Account for
   replication, pairwise distance computation, and the final global maximum.
   ([EX-CTCL 7](../Slides/Exercises/EX-CTCL2526.pdf))

6. Divide $[0,1]^2$ into $c^2$ cells of side $1/c$. For nonempty $P\subseteq[0,1]^2$,
   let $T$ contain one point from each occupied cell. Quantify the additive error when
   approximating $\Delta(P)$ by $\Delta(T)$. Under what additional condition does
   this imply a useful multiplicative guarantee?
   ([EX-CTCL 10](../Slides/Exercises/EX-CTCL2526.pdf))

7. Let $P\subseteq[0,1]$ and $k>1$. Suppose each interval
   $[(i-1)/k,i/k]$, $1\leq i\leq k$, contains an input point. Prove
   $\Phi^{\mathrm{opt}}_{\mathrm{kcenter}}(P,k)\leq1/k$, with centers chosen
   from $P$. State how shared interval endpoints and the requirement for $k$ distinct
   centers should be handled.
   ([Example WT 2, Part 2.1](../Slides/Exercises/Exams/ExampleWT-2.pdf))

8. Points are given as $(\mathrm{ID}(q),(q,c(q)))$, where IDs are distinct in $[0,N-1]$
   and $c(q)$ is the center of $q$'s cluster. Design a two-round algorithm finding the
   farthest point of each nonempty cluster, using $M_L=o(N)$ and $M_A=O(N)$.
   Prove the reducer-size bounds without assuming balanced clusters.
   ([EX-CTCL 11](../Slides/Exercises/EX-CTCL2526.pdf))

9. Each of $N$ points is represented by $(\mathrm{ID}_x,(x,i_x,\gamma_x))$, with
   distinct sequential IDs, a nonempty cluster index $i_x$, and color
   $\gamma_x\in\{0,1\}$. In two rounds, output $(i,b_i)$ for every cluster,
   where $b_i$ is its common color or $-1$ if it is mixed. Obtain $M_L=o(N)$ and
   $M_A=O(N)$ and prove that the local summaries can be merged correctly.
   ([EX-CTCL 12](../Slides/Exercises/EX-CTCL2526.pdf))

10. Let a constant number $k\geq2$ of clusters have global centers $c_1,\ldots,c_k$.
    Each weighted point is represented by $(x,(i_x,w_x))$. Design a two-round algorithm
    returning, for every nonempty cluster $C_i$, the index $j\ne i$ minimizing
    $\sum_{x\in C_i}w_xd(x,c_j)^2$. Specify a partitioning method applicable to these
    keys and analyze local and aggregate space, targeting $o(N)$ and $O(N)$.
    ([EX-CTCL 13](../Slides/Exercises/EX-CTCL2526.pdf))

11. Let $k$ be constant, with global centers $c_1,\ldots,c_k$, and let points be
    represented by $(\mathrm{ID}_x,(x,i_x))$ with distinct sequential IDs. For every
    nonempty cluster $C_i$, find the center maximizing
    $|C_i|^{-1}\sum_{x\in C_i}d(x,c)$ in two rounds. Prove correctness and obtain
    $M_L=o(N)$ and $M_A=O(N)$.
    ([Example WT 4, Part 2.1](../Slides/Exercises/Exams/ExampleWT-4.pdf))

12. For the older fair $k$-means problem minimizing the maximum of the two groups'
    average squared distances, write the objective $\Phi(A,B,C)$. Suppose $n-1$
    group-A observations lie at $0$ and one group-B observation lies at $1$. With one
    unrestricted real-valued center, determine an optimal standard $k$-means center
    and an optimal fair center, including their limits as $n\to\infty$. How does
    this fairness definition differ from the current quota-constrained $k$-center?
    ([Example WT 5, Part 1.4](../Slides/Exercises/Exams/ExampleWT-5.pdf))

13. A recalled question calls the preceding two-group example “fair $k$-center.”
    If interpreted literally, what is an optimal unrestricted standard one-center
    solution? If centers must be input observations and satisfy a specified group
    quota, what changes? Which objective and feasibility information must be stated
    before comparing a standard and a fair optimum?
    ([18/06/2025, recalled Question 4](../Slides/Exercises/Exams/Questions/18-06-2025.txt))

14. Let an optimal $k$-center-with-$z$-outliers solution induce non-outlier clusters
    $C_1,\ldots,C_k$ and radius $\Phi^{\mathrm{opt}}$. For any set $X\subseteq P$
    of $k+z+1$ points, show that two non-outliers of $X$ belong to the same cluster.
    Deduce a bound on $d_{\min}(X)$ in terms of $\Phi^{\mathrm{opt}}$ and use it
    to justify an initial radius lower bound $r_{\min}=d_{\min}(X)/2$.
    ([13/07/2022, Exercise 1](../Slides/Exercises/Exams/sol130722.pdf))

15. For HW1, trace `fairFFT` on the ordered labeled points
    $[((0),A),((1),B),((0),B)]$ with $k_A=1$ and $k_B=2$, treating the two
    differently labeled observations at coordinate zero as distinct input records.
    Use the code's strict `>` comparison and iteration order. Does the returned
    list necessarily contain $k$ distinct input records? Which invariant would
    prevent selecting an already selected record, including zero-distance ties?
    ([HW1: fairFFT](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW1/G26HW1.py>))

## Streaming

1. Describe Boyer-Moore majority voting and trace it on $A,B,A,C,A,D,A,A$ and on
   $A,A,A,C,C,C,B,B,B$. What does its counter represent? When is a second pass needed?

2. A stream contains $n$ distinct integers from $[1,n+1]$. Find the missing integer
   in one pass using $O(1)$ words and $O(1)$ update and query time. State the required
   counter bit width and explain which assumptions are essential.
   ([EX-STR 2](../Slides/Exercises/EX-STR2526.pdf))

3. For Reservoir Sampling, let $S_t$ be the reservoir after item $x_t$, with $t>m$.
   Given that $x_t$ was inserted, determine $\Pr(x_i\in S_t\mid x_t\in S_t)$ for
   $i<t$. Derive the corresponding probability conditioned on $x_t$ not being inserted.
   ([Example WT 1, Part 1.3](../Slides/Exercises/Exams/ExampleWT-1.pdf))

4. A frequent item $a$ occurs at least $\varphi n$ times in a stream of length $n$.
   Show that a reservoir of size $m\geq1/\varphi$ contains at least one occurrence
   of $a$ in expectation. Does this ensure that every such sample contains $a$?
   ([EX-STR 3](../Slides/Exercises/EX-STR2526.pdf))

5. Let $S_1$ and $S_2$ be independent size-$m$ samples from disjoint streams of equal
   length $n$. Using only these samples, construct a size-$m$ sample of their
   concatenation whose individual occurrence-inclusion probabilities are $m/(2n)$,
   and prove this property. Does equal marginal inclusion also imply that all
   size-$m$ subsets of the concatenation are equally likely?
   ([EX-STR 4](../Slides/Exercises/EX-STR2526.pdf), with a distributional extension)

6. A stream of $n$ red or blue items contains $R$ red occurrences. If a size-$m$
   reservoir contains $X_S$ red occurrences, prove that $(n/m)X_S$ is an unbiased
   estimator of $R$. State where linearity of expectation is used.
   ([EX-STR 5](../Slides/Exercises/EX-STR2526.pdf))

7. Run Boyer-Moore and Sticky Sampling with $\varphi=1/2$ in parallel. Return the
   Boyer-Moore candidate exactly when it belongs to the Sticky Sampling output;
   otherwise return `null`. Analyze both the case of a strict majority and the
   case of no strict majority. Can this procedure always certify a majority?
   ([EX-STR 6](../Slides/Exercises/EX-STR2526.pdf))

8. Define a sketch and the frequency moments $F_0$, $F_1$, and $F_2$ of an
   insertion-only stream. Express its Gini impurity through frequency moments and
   compute these quantities when all items are equal and when $m$ distinct items
   have equal frequency. Must every sketch be linear in the frequency vector?

9. An even-length stream of $n>10$ items contains $n/2-5$ copies of $a$, $n/2-5$
   copies of $b$, and 10 occurrences of other items. In a $d\times2$ Count-Min
   Sketch, derive a tight upper bound $R$ on the relative error for $a$ in a row
   where $a$ and $b$ do not collide. With uniform pairwise-independent row hashes
   and independent rows, derive lower bounds on the probability of error at most
   $R$ for one row and for the final estimate. Distinguish lower bounds from exact
   probabilities where other-item collisions matter.
   ([EX-STR 10](../Slides/Exercises/EX-STR2526.pdf))

10. A Count Sketch has $d=2\log_2N$ independent rows, assuming this is an integer.
    A row estimate for a fixed item $u$ is bad when
    $|\widetilde f_{u,j}-f_u|>\varepsilon f_u$, and each row is bad with probability
    $1/12$. Use a Chernoff bound to show that at least $d/2$ bad rows occur with
    probability at most $1/N$. Deduce the corresponding guarantee for the median,
    specifying the convention for even $d$.
    ([08/09/2023, Part 2.2](<../Slides/Exercises/Exams/08-09-2023/Part 2.jpg>))

11. Sensor measurements arrive as $(k_i,w_i)$ with integer weights, and
    $f_u=\sum_{i:k_i=u}w_i$. Design a space-efficient unbiased estimator of
    $H_2=\sum_u f_u^2$. Specify the updates, the query, and a proof of unbiasedness.
    Does the argument still apply to negative measurements?
    ([EX-STR 9](../Slides/Exercises/EX-STR2526.pdf);
    [Example WT 1, Part 2.2](../Slides/Exercises/Exams/ExampleWT-1.pdf))

12. Transactions $(p_i,\gamma_i)$ record purchases when $\gamma_i=1$ and returns
    when $\gamma_i=0$. Design a $d\times w$ counter structure giving an unbiased
    estimate of a product's net sales. Specify the estimator whose expectation you
    prove. How accurate is it if every transaction refers to the same product $p$?
    How does this differ from assuming several products have equal net frequencies?
    ([Example WT 2, Part 2.2](../Slides/Exercises/Exams/ExampleWT-2.pdf);
    [29/06/2023, recalled Exercise 2](../Slides/Exercises/Exams/Questions/29-06-2023/Questions.txt))

13. A stream contains colored items $(u_i,\gamma_i)$ with red or blue labels.
    Using one $d\times w$ counter array, give an unbiased estimator for
    $f'_u=f_{u,\mathrm{red}}/2+f_{u,\mathrm{blue}}/3$. State the update and query.
    If no other item collides with $u$ in one row, does that row give the exact
    weighted frequency? Prove your answer.
    ([Example WT 4, Part 2.2](../Slides/Exercises/Exams/ExampleWT-4.pdf))

14. Two $n$-bit Bloom filters represent $S_1$ and $S_2$ using identical hash functions.
    Combine them into a filter for $S_1\cup S_2$ without false negatives. Derive the
    probability that a fixed output bit is zero, accounting for possible overlap
    between the sets.
    ([Example WT 3, Part 2.2](../Slides/Exercises/Exams/ExampleWT-3.pdf);
    [21/06/2022, EX-2](../Slides/Exercises/Exams/sol210622.pdf))

15. A Bloom filter for $m$ items has an even-length $n$-bit array $A$ and $k$ independent
    hashes uniform on $[0,n-1]$. Transform it in $O(n)$ time into an $n/2$-bit filter.
    Specify its hashes and query rule, prove the absence of false negatives, and
    calculate the probability that a fixed new bit is zero.
    ([EX-STR 11](../Slides/Exercises/EX-STR2526.pdf))

16. For HW2 with $n=10^6$, $\varphi=0.07$, $\delta=0.05$, and
    $\varepsilon\in\{0.01,0.02,0.04\}$, compute the Sticky Sampling insertion
    probability and output threshold for each configuration. Explain why the
    dictionary size differs from $|F_{SS}|$, and why neither stored Sticky
    counters nor Count-Min estimates are the true frequencies printed by the program.
    ([HW2 code](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/G26HW2.py>);
    [experiment runner](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/run_hw2_experiments.py>))

17. In HW2, which structures and guarantees depend on each of $n$, $\varphi$,
    $\varepsilon$, $\delta$, $d$, and $w$? Does changing $\varepsilon$ automatically
    change the Count-Min width? For $d=5$ and $w\in\{15,30,60\}$, translate the
    course's Count-Min bound into an additive-error/confidence statement under
    valid hash-domain assumptions, and explain its limits for the actual 32-bit input.
    ([HW2 code](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/G26HW2.py>))

18. The HW2 experiment runner classifies returned items as frequent, almost frequent,
    or rare. State the thresholds and compute them for $n=10^6$, $\varphi=0.07$,
    and classification parameter $\varepsilon=0.04$. Explain which returned
    categories Sticky Sampling can exclude deterministically and which Count-Min
    can exclude only probabilistically under appropriate assumptions. Why must
    candidate-set size and number of sketch counters be reported separately?
    ([experiment runner](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/run_hw2_experiments.py>))

## Simsearch

1. Define a kd-tree, its internal nodes, leaves, associated regions, and alternating
   splitting rule in two dimensions. If a node at even depth has region
   $[0,12]\times[0,8]$ and split $x=5$, define its children's regions. Repeat for
   an odd-depth node split at $y=3$, specifying boundary conventions.
   ([14/07/2025, Question 4](../Slides/Exercises/Exams/Questions/14-07-2025.txt);
   [July 2026 recalled questions](<../Slides/Exercises/Audio/WhatsApp Image 2026-07-17 at 17.54.55.jpeg>))

2. Construct a balanced kd-tree for
   $P=\{(1,5),(2,2),(3,7),(4,4),(5,1),(6,8),(7,3),(8,6)\}$, using vertical
   splits at even depths and midpoint splits between the two middle coordinates.
   Trace the query rectangle $[2.5,7.5]\times[2.5,7.5]$, identifying pruned,
   fully contained, and partially intersecting regions.

3. Every node of a kd-tree stores an arbitrary point from its subtree. Adapt
   `SearchKdTree` to return one point of $P\cap R$, or `null`, in $O(\sqrt n)$
   time. Prove correctness and explain why the output-size term disappears.
   ([EX-SIMSEARCH 1](../Slides/Exercises/EX-SIMSEARCH2526.pdf))

4. A collection contains $n$ documents and a vocabulary of $D$ relevant words;
   word frequencies are ignored. Propose a Boolean representation and a
   single-table bit-sampling structure for finding a similar document. Find
   parameters $r,c$ giving success probability at least $1/2$ and expected query
   time $O(n)$ instead of $O(Dn)$. State the distance represented by your encoding.
   ([EX-SIMSEARCH 2](../Slides/Exercises/EX-SIMSEARCH2526.pdf))

5. Boolean vectors are stored in one table using a random bit-sampling hash $h$.
   Derive $\Pr[h(p)=\operatorname{not}(h(q))]$ from $d_H(p,q)$. Design a query
   for an $r$-far point satisfying $d_H(p,q)\geq r$, and prove its probabilistic
   guarantee, including the case when no such point exists.
   ([EX-SIMSEARCH 3](../Slides/Exercises/EX-SIMSEARCH2526.pdf);
   [Example WT 5, Part 2.2](../Slides/Exercises/Exams/ExampleWT-5.pdf);
   [18/06/2025, Exercise 2](../Slides/Exercises/Exams/18-06-25.pdf))

6. For a family with $p_1=1/2$, $p_2=1/4$, and $n=2^{20}$, determine $\rho$,
   the smallest integer $K$ with $p_2^K\leq1/n$, and an integer number of tables
   sufficient for success at least $0.99$ for a fixed query with a near point.
   Bound the expected number of far collisions across those tables.

## Spark

1. Given the following program, identify which calls can trigger distributed work,
   what each timing interval includes, and what data may be reused. How would
   removing `cache()` change the two actions?

   ```python
   start = time.time()
   values = sc.textFile(path).map(int).filter(lambda x: x > 0).cache()
   planned = time.time()
   n = values.count()
   counted = time.time()
   total = values.reduce(lambda a, b: a + b)
   finished = time.time()
   ```

2. Write an RDD Word Count pipeline using per-document counts, `groupByKey`, and
   `mapValues`. Rewrite it with `reduceByKey`. Give the record type after each
   transformation and discuss behavior when one word occurs in every document.

3. Write the two-round Word Count pipeline based on explicit random keys. Explain
   `groupBy` versus `groupByKey`, describe the local aggregation function, and
   bound how many partial counts of one word reach the final aggregation.
   ([[3.WordCountSpark#Technique 1 — Random Keys (groupBy)]])

4. Write the Word Count variant that aggregates within existing RDD partitions
   using `mapPartitions`. Compare its shuffles, temporary state, and load
   assumptions with the explicit-random-key variant. How can document expansion
   cause previously balanced partitions to become unbalanced?
   ([[3.WordCountSpark#Technique 2 — Spark Partitions (mapPartitions)]])

5. Design an experiment comparing alternative Word Count or clustering pipelines.
   Explain how to control input partitions, materialization, cache reuse, repeated
   actions, and initialization costs so that the reported times measure comparable
   work. Which memory bottlenecks can remain even when the input RDD is distributed?

6. Trace HW1's actions and timing boundaries: group counting, `MRFairFFT`, and
   final radius evaluation. Which action first materializes persisted input?
   Does the reported `Running time of MRFairFFT` include loading, local coreset
   extraction, coreset collection, final sequential selection, and original-data
   radius evaluation? Justify each inclusion or exclusion from the code.
   ([HW1 main program](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW1/G26HW1.py>))

7. HW2 uses a 0.1-second batch interval, `local[*]`, `foreachRDD`, and a
   `threading.Event`. Explain the purpose of each and why stopping is requested
   in the callback but performed outside it. If a batch starts with 97 valid
   items already processed and target $n=100$, trace a batch containing four
   valid integers and malformed records. Which updates and counters change?
   ([HW2: process_batch and main](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/G26HW2.py>))
