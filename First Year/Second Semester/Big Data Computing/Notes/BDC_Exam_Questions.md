# BDC Theory Questions, Theorems and Proofs

## MapReduce

1. Define a MapReduce round and describe the input and output of its map, shuffle, and
   reduce phases. How are intermediate records grouped, and how can several rounds be composed?

2. Define the number of rounds $R$, local space $M_L$, and aggregate space $M_A$ in the
   course model. Which input, output, intermediate records, and auxiliary data must be counted?
   What design goals should a scalable algorithm satisfy? Why is executing an arbitrary
   sequential algorithm in one reducer generally inadequate?
   ([Example WT 3, Part 1.1](../Slides/Exercises/Exams/ExampleWT-3.pdf))

3. State the cluster resource requirements for executing a MapReduce algorithm with
   local space $M_L$ and aggregate space $M_A$. Explain how worker RAM, distributed
   storage, replication, and system overhead affect feasibility.
   ([Example WT 1, Part 1.1](../Slides/Exercises/Exams/ExampleWT-1.pdf);
   [Example WT 4, Part 1.1](../Slides/Exercises/Exams/ExampleWT-4.pdf))

4. State and prove the cluster mean-time-between-failures result under independent
   exponential machine lifetimes. Explain its assumptions and implications for
   fault tolerance, replication, and recovery.

5. Given $N$ records with distinct keys $i\in\{0,\ldots,N-1\}$, describe a deterministic
   partition into $L$ groups and prove a bound on the largest group. Does the same bound
   hold for arbitrary distinct integer keys? Give a counterexample or a proof.

6. Prove that independently assigning $N$ records uniformly to $\sqrt N$ groups gives
   maximum load $O(\sqrt N)$ with probability at least $1-1/N^5$, assuming $N$ is a
   sufficiently large perfect square. State the indicator variables, the Chernoff bound,
   and the union bound used. Why is a bound on expected load alone insufficient?

7. Describe and analyze the one-round and two-round algorithms for Class Count on records
   $(i,(\gamma_i,o_i))$. For the two-round algorithm, analyze $R$, $M_L$, and $M_A$ as
   functions of $N$ and $L$, choose $L$, and explain why a class containing all records
   does not violate the claimed space bound.

8. Describe and analyze one-round Word Count when documents are input records. Let $N$
   be the total number of word occurrences, $b$ the number of documents, and $N_{\max}$ the largest
   document size. Analyze $M_L$ and $M_A$, accounting for local counting within documents.
   Which two different sources of skew can cause large local space?

9. Describe and analyze two-round Word Count using random partitioning. Specify what is
   partitioned, bound the number of partial counts for one word, and analyze local and
   aggregate space, including the maximum document size and probabilistic assumptions.
   ([EX-MR 3](../Slides/Exercises/EX-MR2526.pdf))

10. State the union bound, Markov's inequality, Chebyshev's inequality, and the
    upper- and lower-tail Chernoff bounds used in the notes, including their
    hypotheses. Prove the union bound and Markov's inequality, and derive Chebyshev's
    inequality from Markov's. Which bounds require independence, and which can be
    applied to dependent random variables?
    ([[BDC_proofs#MapReduce and Spark Definitions]]; [[BigDataComputing_Exam_MasterGuide]])

## Coreset

1. Define a metric space and state its four distance requirements. Define the Minkowski
   distance for exponent $r\geq1$ and its $L_1$, $L_2$, and $L_\infty$ cases. Prove
   that $L_1$ satisfies the metric axioms. Does squared Euclidean distance satisfy them?
   ([EX-CTCL 1](../Slides/Exercises/EX-CTCL2526.pdf))

2. Define a feasible solution, objective function, and $c$-approximation for minimization
   and maximization problems. Why must the direction of the approximation inequality
   depend on whether the objective is minimized or maximized?

3. Define the objectives of $k$-center, $k$-means, and $k$-median and a $c$-approximate
   solution for each. For a fixed center set $S$, describe an optimal induced clustering.
   Explain the distinction between centers constrained to the input and unrestricted
   centers, and compare sensitivity to outliers.
   ([08/09/2023, Part 1.2](<../Slides/Exercises/Exams/Questions/Part 1.jpg>))

4. Describe Farthest-First Traversal (FFT) and show how to implement it in $O(Nk)$ time
   when a distance computation costs $O(1)$. What state must be maintained, and what
   changes when points have dimension $D$ and distances cost $O(D)$?
   ([EX-CTCL 3](../Slides/Exercises/EX-CTCL2526.pdf))

5. Let $S=\{c_1,\ldots,c_k\}$ be selected by FFT and let $q$ be farthest from $S$.
   Prove that every two distinct points of $S\cup\{q\}$ are at distance at least
   $d(q,S)$. Use this property to prove FFT's approximation guarantee. How would the
   proof shorten if the separation property were supplied without proof?
   ([Example WT 3, Part 1.3](../Slides/Exercises/Exams/ExampleWT-3.pdf))

6. Describe the composable coreset technique for a problem whose input is too large for
   a sequential algorithm. What properties must the local summaries and their union
   satisfy? Under what size and quality conditions is the technique effective?
   ([19/07/2023, Question 3](../Slides/Exercises/Exams/Questions/19-07-2023/Questions.jpg))

7. Describe both rounds of MR-FFT with $L$ balanced partitions. Derive the coreset size,
   local space, and aggregate space; optimize $L$ and state when local space is $o(N)$.
   Compare one advantage and one disadvantage with sequential FFT.
   ([Example WT 4, Part 1.2](../Slides/Exercises/Exams/ExampleWT-4.pdf);
   [14/07/2025, Question 2](../Slides/Exercises/Exams/Questions/14-07-2025.txt))

8. Prove the coverage guarantee of the coreset formed by the first round of MR-FFT,
   expressing its radius relative to the optimum on the original dataset. Then prove
   the approximation guarantee of the complete algorithm. Explain why the proof must
   compare against the original optimal clusters.

9. Construct a family of instances showing why a small uniform random sample can be a
   poor coreset for $k$-center. Quantify the probability of missing an isolated cluster
   and explain why its effect differs from missing a point in a dense cluster.

10. Let $T\subseteq P$, $|T|>k$, and suppose every $x\in P$ satisfies
    $d(x,T)\leq\varepsilon\Phi^{\mathrm{opt}}_{\mathrm{kcenter}}(P,k)$,
    where $0<\varepsilon<1$. If $S=\operatorname{FFT}(T,k)$, prove an upper bound
    on $\Phi_{\mathrm{kcenter}}(P,S)$ in terms of $\varepsilon$ and the optimum on $P$.
    ([EX-CTCL 4](../Slides/Exercises/EX-CTCL2526.pdf))

11. Let $T\subseteq P$ and $k<|T|$, with centers required to belong to the dataset
    being clustered. Prove
    $\Phi^{\mathrm{opt}}_{\mathrm{kcenter}}(T,k)\leq
    2\Phi^{\mathrm{opt}}_{\mathrm{kcenter}}(P,k)$ and show tightness.
    Why is the stronger inequality without factor $2$ not automatic?
    ([EX-CTCL 5](../Slides/Exercises/EX-CTCL2526.pdf))

12. Define the diameter $\Delta(P)$ of a metric point set. State and prove the
    approximation guarantee obtained by selecting an arbitrary $x\in P$ and using
    $\Delta_x=\max_{y\in P}d(x,y)$. Which metric property is essential?
    ([EX-CTCL 8](../Slides/Exercises/EX-CTCL2526.pdf))

13. Let $T\subseteq P$ satisfy $d(x,T)\leq R$ for every $x\in P$. Derive and prove
    lower and upper bounds on $\Delta(P)$ in terms of $\Delta(T)$ and $R$.
    What condition on $R$ and $\Delta(T)$ guarantees a $(1+\varepsilon)$ approximation?
    ([Example WT 5, Part 1.2](../Slides/Exercises/Exams/ExampleWT-5.pdf);
    [18/06/2025, recalled Question 2](../Slides/Exercises/Exams/Questions/18-06-2025.txt))

14. Describe Lloyd's algorithm, $k$-means++ initialization, and PAM. Compare their
    objectives, allowed center locations, computational costs, and suitability for
    massive datasets. What guarantee is stated for $k$-means++, and what does it imply
    about a single run?

15. Define weighted $k$-means. Give the selection probabilities for the first and later
    centers in weighted $k$-means++, and the centroid update in weighted Lloyd's method.
    How should zero total weight or zero total sampling score be handled?
    ([Example WT 2, Part 1.2](../Slides/Exercises/Exams/ExampleWT-2.pdf);
    [July 2026 recalled questions](<../Slides/Exercises/Audio/WhatsApp Image 2026-07-17 at 17.54.55.jpeg>))

16. State and prove the probability-amplification result for independent runs of
    $k$-means++, when the solution with minimum objective value is returned. Express
    the failure bound as a function of the number of runs. Explain how Markov's
    inequality converts an expected approximation guarantee into a constant-probability
    guarantee, including any change to the approximation factor.
    ([EX-CTCL 9](../Slides/Exercises/EX-CTCL2526.pdf))

17. Describe the construction of the weighted coreset in MR-$k$-means. How are its
    representatives selected, what does each weight count, and why can the weights
    not generally be discarded? Specify both rounds and analyze space as a function
    of $N$, $k$, and the partition count $L$.
    ([Example WT 1, Part 1.2](../Slides/Exercises/Exams/ExampleWT-1.pdf))

18. Define the proxy-error $\gamma$-coreset used for $k$-means in the notes. State
    and prove the resulting approximation guarantee when the final weighted
    algorithm is an $\alpha$-approximation. First justify the coreset's proxy-error
    bound from local $\gamma$-approximate solutions; then derive both directions
    of the cost comparison between original points and weighted proxies. State the
    admissible center domains needed for comparisons with global optimal centers.
    Explain how using more local representatives changes the accuracy-space tradeoff.
    ([[BDC_proofs#Additional Coreset and k-Means Results]])

19. Define max-sum diversity using unordered pairs and a $(1+\varepsilon)$-coreset
    for this maximization problem. What guarantee follows from a $c$-approximation
    on such a coreset? Explain why one representative per geometric cluster may be
    insufficient for preserving a size-$k$ diverse solution.

20. Describe the diversity coreset built from $h$ FFT centers and up to $k$ points
    from each induced cluster. Prove that an optimal size-$k$ solution has distinct
    proxies in the coreset. Derive the additive loss in diversity in terms of radius
    $R$ and $k$, and identify a condition giving a $2$-coreset. How does changing $h$
    affect cost and quality? State the relation between optimal $k$-center radius
    and optimal average pairwise diversity used in this proof. Taking that relation
    as given, extend the argument to a $(1+\varepsilon)$-coreset and derive a
    sufficient radius condition, distinguishing multiplicative approximation from
    a retained fraction of the optimum.

21. For the current Fair $k$-Center homework, define the objective and exact group
    quotas. Describe sequential Fair-FFT and both rounds of MR-Fair-FFT, including
    local oversampling. What feasibility checks are needed globally and inside each
    partition? Can the unconstrained FFT approximation proof be applied unchanged?
    ([[PROJECT_DESCRIPTIONS_EXAM]];
    [29/06/2023, recalled Question 1, adapted to current homework](../Slides/Exercises/Exams/Questions/29-06-2023/Questions.txt))

22. For the older fair $k$-means problem minimizing the maximum of the demographic
    groups' average squared distances, define the objective and admissible centers.
    Explain how this notion of fairness differs from the current quota-constrained
    fair $k$-center homework.
    ([Example WT 5, Part 1.4](../Slides/Exercises/Exams/ExampleWT-5.pdf))

23. For the older $k$-center-with-$z$-outliers problem, define its objective and describe
    what the second round of a coreset-based algorithm does. If each of $L$ partitions
    emits at most $k+z+1$ weighted representatives, how does increasing $L$ affect the
    number of points processed by that round?
    ([Example WT 3, Part 1.2, with coreset size specified](../Slides/Exercises/Exams/ExampleWT-3.pdf))

24. For the older silhouette homework question, define the silhouette of a point and
    the average silhouette of a clustering. Explain how within-cluster and
    between-cluster distances affect the score, and state how singleton clusters
    and degenerate zero-distance cases should be handled.
    ([29/06/2023, recalled Question 2](../Slides/Exercises/Exams/Questions/29-06-2023/Questions.txt))

25. In HW1, explain the invariant maintained by `minDists`, how group budgets
    restrict the next candidate, and how the first center is selected when one
    quota is zero. Derive time and auxiliary-space bounds in terms of $N$, $D$,
    and $k=k_A+k_B$. Which part of FFT's separation argument can fail when
    candidates are restricted by group budgets?
    ([HW1: fairFFT](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW1/G26HW1.py>))

26. HW1 uses local quotas $k'_A=2k_A$ and $k'_B=2k_B$. Does global feasibility
    imply feasibility in every partition? Discuss empty partitions, a partition
    lacking one group, and a partition with fewer eligible records than its local
    quota. Which checks does the submitted code perform, and what policy would
    preserve distinct local representatives without rejecting a globally feasible
    input unnecessarily?
    ([HW1 specification](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/instruction.md>);
    [HW1 code](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW1/G26HW1.py>))

27. Let $L_{\mathrm{actual}}$ be the number of HW1 input partitions, $B$ the
    largest partition size, and $h=k'_A+k'_B$. Derive bounds on the number of
    records collected into $T$, executor working memory, and driver memory.
    Include dimension $D$ and distinguish record counts from memory words.
    Under balanced partitions, how should $L_{\mathrm{actual}}$ depend on $N$
    and $h$ to balance local input size against collected coreset size?
    ([HW1: MRFairFFT](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW1/G26HW1.py>))

28. In HW1, compare evaluating the final radius on the collected coreset with
    evaluating it on the original distributed dataset. Which does the program
    print? Explain why a small coreset radius alone does not certify a small
    original-data radius. How would you interpret changing radius and runtime
    when the partition count or oversampling factor increases?
    ([HW1 code](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW1/G26HW1.py>))

29. Define Hamming, Jaccard, and angular distance as used in the clustering notes.
    State appropriate domains, the convention for two empty sets in Jaccard
    distance, and the effect of positive rescaling on angular distance. On which
    representation does angular distance satisfy identity of indiscernibles?
    ([[4.Coreset2526-1]]; [[TheoremsDefinitionsProofs#Definitions - Common Distances]])

## Streaming

1. Define the streaming model, update and query operations, and its main performance
   metrics. Explain why working memory in words and working memory in bits can give
   different bounds. Compare one-pass and multiple-pass algorithms.
   ([Example WT 4, Part 1.4(a)](../Slides/Exercises/Exams/ExampleWT-4.pdf))

2. Describe Boyer-Moore majority voting, including initialization, update rules,
   and output. What does its counter represent? When is a second pass needed,
   and what can be concluded after only the first pass?

3. Prove the Boyer-Moore invariant: after $t$ items, the prefix can be partitioned
   into `count` copies of `cand` and unequal-item pairs. Use it to prove correctness
   when a strict majority exists, and explain what remains true when none exists.
   ([EX-STR 1](../Slides/Exercises/EX-STR2526.pdf))

4. Describe Reservoir Sampling with capacity $m$ on an unbounded stream. Prove that
   each occurrence among the first $t\geq m$ positions is retained with probability
   $m/t$. Why must repeated values be treated as distinct stream occurrences?

5. Define Frequent Items and $\varepsilon$-Approximate Frequent Items for threshold
   $\varphi$. Specify required, forbidden, and optional outputs. Prove an upper
   bound on the number of truly frequent items.

6. Describe Sticky Sampling for known stream length $n$, with parameters
   $0<\varepsilon<\varphi<1$ and $0<\delta<1$. Give its sampling parameter,
   insertion probability, update rule, and output threshold. What must happen when
   the nominal insertion probability exceeds $1$?

7. State and prove a bound on the expected working memory of Sticky Sampling with
   $r=\lceil\ln(1/(\delta\varphi))/\varepsilon\rceil$. Is this a deterministic
   bound? State its update and query costs under expected constant-time dictionary
   operations.
   ([Example WT 2, Part 1.3](../Slides/Exercises/Exams/ExampleWT-2.pdf);
   [29/06/2023, recalled Question 3](../Slides/Exercises/Exams/Questions/29-06-2023/Questions.txt))

8. State the output guarantees of Sticky Sampling, distinguishing deterministic
   exclusions from probabilistic inclusions. Prove the probability bound for missing
   one truly frequent item, and then the simultaneous guarantee for all frequent
   items. Explain how the gray zone affects valid answers.
   ([Example WT 5, Part 1.3](../Slides/Exercises/Exams/ExampleWT-5.pdf);
   [18/06/2025, recalled Question 3](../Slides/Exercises/Exams/Questions/18-06-2025.txt))

9. Explain the extension of Sticky Sampling to unknown stream length at the level
   described in the notes. How do batch sizes and sampling probabilities evolve,
   and why must the retained state be recalibrated?

10. Define a sketch and the frequency moments $F_0$, $F_1$, and $F_2$ of an
    insertion-only stream. Express Gini impurity through frequency moments and
    explain what it measures. Must every sketch be linear in the frequency vector?

11. Describe Probabilistic Counting for distinct elements: hash assumptions, trailing
    zero statistic, state update, and final estimate. Explain why duplicate arrivals
    do not act like new distinct values, and account for state and hash-description
    space in bits.
    ([Example WT 3, Part 1.4](../Slides/Exercises/Exams/ExampleWT-3.pdf);
    [08/09/2023, Part 1.3](<../Slides/Exercises/Exams/Questions/Part 1.jpg>))

12. For the estimate $\widetilde F_0=2^R$ from Probabilistic Counting, derive an
    upper-tail bound using indicator variables and Markov's inequality. Explain
    how the proof of the lower tail depends on independence between hashes of
    distinct items. State the constant-factor theorem, including both tail
    probabilities and space cost. Prove a lower-tail bound under fully independent
    uniform hashes, handling integer thresholds, and distinguish it from what
    follows using only pairwise independence.

13. Run an odd number $\ell$ of independent Probabilistic Counting instances and
    return their median $\widehat F_0$. Prove that an appropriate
    $\ell=\Theta(\log|U|)$ gives both
    $\Pr(\widehat F_0<F_0/16)\leq1/|U|$ and
    $\Pr(\widehat F_0>16F_0)\leq1/|U|$. State the per-instance tail bounds
    and the independence assumptions used in the amplification.
    ([EX-STR 7](../Slides/Exercises/EX-STR2526.pdf))

14. Describe Count-Min Sketch initialization, update, and frequency query. Prove
    its one-sided error property for insertion-only streams. Derive the width,
    depth, space, and time needed for additive error at most $\varepsilon n$
    with probability at least $1-\delta$ for a fixed item.

15. Prove the Count-Min error guarantee by writing a row's collision noise explicitly,
    bounding its expectation, applying Markov's inequality, and using independent
    rows. How must the failure parameter change to guarantee all of $q$ fixed
    frequency queries simultaneously?

16. Two relations have join-key frequencies $a_u$ and $b_u$. Express their equijoin
    size in terms of these frequencies. Describe an estimator using compatible
    Count-Min Sketches, explain why it overestimates for nonnegative frequencies,
    and state why identical row hashes are required.

17. Describe Count Sketch, including bucket hashes, sign hashes, updates, row
    estimators, and final frequency query. Prove that a row estimator is unbiased.
    Why are signs needed, and why is taking a minimum inappropriate here?

18. Derive a variance bound for a Count Sketch row frequency estimate and use it to
    obtain an additive-error guarantee in terms of $\varepsilon\sqrt{F_2}$.
    Explain how width and independent repetitions affect error and confidence.
    Distinguish unbiasedness of individual rows from accuracy of the median.

19. For one Count Sketch row, define
    $\widetilde F_{2,j}=\sum_{b=0}^{w-1}C[j,b]^2$. Prove that this is an unbiased
    estimator of $F_2$. What independence is needed for the expectation calculation,
    and what stronger sign independence is used for the usual variance bound?
    Derive that variance bound, then use Chebyshev's inequality and independent
    rows to prove relative error at most $\varepsilon F_2$ with probability
    at least $1-\delta$. Choose width and depth and state the update and
    second-moment query costs. Why must this error scale be distinguished from
    the $\varepsilon\sqrt{F_2}$ scale for an individual frequency query?
    ([EX-STR 8](../Slides/Exercises/EX-STR2526.pdf))

20. Compare Count-Min and Count Sketch for nonnegative and signed updates, error
    direction, error scale, memory, and query cost. Explain how sketches from disjoint
    stream segments can be merged and identify the necessary compatibility conditions.

21. Define approximate membership. Describe how a Bloom filter is initialized and
    queried, and prove that it has no false negatives after insertions. Give its
    update and query cost, and explain why clearing a queried item's bits is not
    generally a valid deletion operation.
    ([14/07/2025, Question 3](../Slides/Exercises/Exams/Questions/14-07-2025.txt);
    [July 2026 recalled questions](<../Slides/Exercises/Audio/WhatsApp Image 2026-07-17 at 17.54.55.jpeg>))

22. A Bloom filter has $b$ bits, $m$ distinct inserted items, and $k$ independent
    uniform hash functions. Derive the probability that a fixed bit remains zero
    and the usual approximation for the false-positive rate. Identify the
    approximations involved, determine an approximately optimal $k$, and relate
    bits per item to a target false-positive rate.

23. Explain fingerprinting for approximate membership and compare its memory and
    false-positive behavior with Bloom filters. Why must hash-description space
    be considered when comparing theoretical and practical implementations?

24. Define $k$-universality and strong $k$-universality using the conventions of the
    notes. Explain their difference and identify where pairwise independence,
    independent repetitions, and four-wise independent signs enter the streaming
    analyses studied in this course.

25. For $U=\{0,\ldots,u-1\}$ and prime $p>u$, describe the family
    $h_{a,b}(x)=((ax+b)\bmod p)\bmod w$, its parameter ranges, representation cost,
    and collision guarantee. Prove its $2$-universality by analyzing the ordered
    pair of residues before reduction modulo $w$, and then counting colliding
    residues. Does this also establish strong $2$-universality after reduction?
    Explain and justify how a Mersenne prime $p=2^q-1$ supports fast modular
    reduction using binary operations.
    ([[7.Streaming2526-2#Practical Hash Families]])

26. The homework uses $h_j(x)=((a_jx+b_j)\bmod8191)\bmod w$. What happens to
    distinct keys congruent modulo 8191? Can increasing sketch depth separate them?
    State the domain assumption needed before applying the theoretical hash guarantee.
    ([[PROJECT_DESCRIPTIONS_EXAM]])

27. In the current Frequent Items homework, compare the sets returned by Sticky
    Sampling and Count-Min, their thresholds, and their possible errors. Can Count-Min
    alone enumerate all item identities? Account separately for sketch counters,
    candidate sets, and the exact-frequency dictionary used for evaluation.
    ([[PROJECT_DESCRIPTIONS_EXAM]])

28. In HW2, explain the distinction between the Sticky Sampling dictionary and
    its filtered output set $F_{SS}$. Why are stored Sticky counters and Count-Min
    estimates different from the true frequencies printed by the program?
    ([HW2 code](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/G26HW2.py>);
    [experiment runner](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/run_hw2_experiments.py>))

29. In `process_item`, the Count-Min threshold for adding an item to $F_{CM}$ is
    checked only when that item arrives. Prove that every truly frequent item is
    nevertheless included after the first $n$ updates. Is this output necessarily
    identical to querying every observed item's sketch estimate at the end?
    Construct a collision-based counterexample or prove equality. Explain the
    role of collision updates after an item's last occurrence.
    ([HW2: process_item](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/G26HW2.py>))

30. In HW2, which structures and guarantees depend on each of $n$, $\varphi$,
    $\varepsilon$, $\delta$, $d$, and $w$? Does changing $\varepsilon$ automatically
    change the Count-Min width? Explain how the theoretical error and confidence
    parameters relate to the code's explicit width and depth, and state the limits
    imposed by the hash family on the actual 32-bit input domain.
    ([HW2 code](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/G26HW2.py>))

31. Define frequent, almost frequent, and rare items using the thresholds in the
    HW2 experiment runner. Which categories can Sticky Sampling exclude
    deterministically, and which can Count-Min exclude only probabilistically under
    appropriate assumptions? Why must candidate-set size and sketch-counter count
    be reported separately?
    ([experiment runner](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/run_hw2_experiments.py>))

32. HW2 repeats experiments on a deterministic source stream. Why can results still
    vary across runs? Explain how changing the random seed, sampling parameter,
    width, or depth affects the experiment, and what repeated runs can and cannot
    establish about a high-probability theorem. How would you ensure both algorithms
    are compared against the same exact stream prefix?
    ([HW2 specification](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/HW2_Description.md>);
    [experiment runner](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/run_hw2_experiments.py>))

## Simsearch

1. Define $r$-Near Neighbor Search and $(c,r)$-Approximate Near Neighbor Search.
   Specify valid outputs when an $r$-near point exists, when points exist only at
   distances in $(r,cr]$, and when all points are farther than $cr$.
   ([Example WT 1, Part 1.4](../Slides/Exercises/Exams/ExampleWT-1.pdf);
   [29/06/2023, recalled Question 4](../Slides/Exercises/Exams/Questions/29-06-2023/Questions.txt))

2. Distinguish $r$-NNS, nearest-neighbor search, $k$-nearest-neighbor search,
   $r$-near-neighbor reporting, and similarity join. For each, specify the input
   query and the required output. Give the space and query cost of brute-force
   $r$-NNS for $n$ points of dimension $D$.

3. Define Range Reporting for axis-aligned rectangles and explain how it differs
   from $r$-NNS. State the space and query bounds of a balanced kd-tree in
   $\mathbb R^2$, including the dependence on the number of reported points.
   ([Example WT 2, Part 1.4](../Slides/Exercises/Exams/ExampleWT-2.pdf);
   [19/07/2023, Question 4](../Slides/Exercises/Exams/Questions/19-07-2023/Questions.jpg))

4. Define a kd-tree, its internal nodes, leaves, associated regions, and alternating
   splitting rule in two dimensions. Describe how each child's region follows from
   the parent region and splitting hyperplane, including boundary conventions.
   ([14/07/2025, Question 4](../Slides/Exercises/Exams/Questions/14-07-2025.txt);
   [July 2026 recalled questions](<../Slides/Exercises/Audio/WhatsApp Image 2026-07-17 at 17.54.55.jpeg>))

5. Describe `SearchKdTree` and prove correctness. Derive construction time and
   storage, then prove the $O(\sqrt n+t)$ query bound in two dimensions by
   distinguishing boundary-intersecting regions from reported subtrees. Derive
   the recurrence for regions crossed by a fixed axis-aligned boundary line
   over two consecutive tree levels, and justify the output-sensitive term.

6. Explain how an enclosing-square Range Reporting query can answer Euclidean
   $r$-NNS in two dimensions. Derive the cost in terms of the square's output
   size and construct an example where many square candidates lie outside the ball.
   Does the reduction guarantee $O(\sqrt n)$ query time?

7. Generalize kd-trees to $D$ dimensions. State their construction, storage, and
   Range Reporting costs under the course's representation convention. Explain
   how the exponent in the query bound illustrates the curse of dimensionality.

8. Define a $(p_1,p_2,c,r)$-locality-sensitive family, specifying the inequalities
   on all parameters and both collision conditions. How does this objective
   differ from that of universal hashing for ordinary hash tables?
   ([08/09/2023, Part 1.4(a)](<../Slides/Exercises/Exams/Questions/Part 1.jpg>))

9. Describe preprocessing and querying for a single-table LSH structure. Explain
   why candidate distances must be checked and prove its success guarantee.
   What can be returned if no input point is within distance $r$?
   ([08/09/2023, Part 1.4(b)](<../Slides/Exercises/Exams/Questions/Part 1.jpg>))

10. For a single LSH table, derive expected query time when hash evaluations and
    distance computations cost $O(D)$. Account for the initial hash evaluation,
    rejected far points, and early stopping at the first acceptable point. Under
    what condition can the resulting bound be abbreviated to $O(Dnp_2)$?
    ([Example WT 4, Part 1.3](../Slides/Exercises/Exams/ExampleWT-4.pdf))

11. Define bit-sampling LSH for $D$-dimensional Boolean vectors. Derive its collision
    probability in terms of Hamming distance and identify valid $p_1,p_2$ for
    thresholds $r$ and $cr$, with $0<r<cr<D$.

12. Describe random-projection LSH for Euclidean distance, including the random
    projection, bucket width, and random shift. Explain why nearby points are
    more likely to collide. How can a secondary hash table represent the
    potentially unbounded integer bucket indices?

13. Define the LSH exponent $\rho$ and explain its significance for query time
    and preprocessing. Prove that $0<\rho<1$ when $0<p_2<p_1<1$. Compare two
    families with different $\rho$ values under otherwise comparable costs.

14. Derive the near-point success probability under the OR construction with $L$
    independent tables. Determine $L$ sufficient for failure probability at most
    $\delta$. Explain the effect on storage and the number of candidate scans.

15. Derive collision bounds for the AND construction using $K$ independent hashes
    per table. Choose an integer $K$ making the far-point collision probability
    at most $1/n$, and relate the near-point probability to $\rho$, accounting
    for rounding.

16. Combine AND and OR amplification to obtain constant-probability approximate
    near-neighbor search. Derive suitable $K,L$, preprocessing, space, and expected
    query costs. State whether point coordinates are shared across tables or copied,
    and include the cost of computing composite hashes.

17. Show how concatenated bit sampling changes collision probability as a function
    of Hamming distance. Does it change $\rho$? Explain the difference between
    choosing coordinates independently with replacement and choosing distinct
    coordinates without replacement.

## Spark

1. Describe the roles of the driver, `SparkContext`, executors, and cluster manager.
   Distinguish a worker machine, an executor, a task, and an RDD partition. How do
   execution and resource placement differ between local and cluster deployment?

2. Define an RDD and explain partitioning, immutability, coarse-grained transformations,
   and lineage. How can Spark reconstruct a lost partition? What role does external
   stable storage play?

3. Explain lazy evaluation and how it can distort timing measurements. If a timed
   block only defines transformations, what has it measured? Describe how to time
   the actual computation and how cached input changes what the measurement includes.
   ([Example WT 5, Part 1.1](../Slides/Exercises/Exams/ExampleWT-5.pdf);
   [08/09/2023, Part 1.1(a)](<../Slides/Exercises/Exams/Questions/Part 1.jpg>);
   [18/06/2025, recalled Question 1](../Slides/Exercises/Exams/Questions/18-06-2025.txt))

4. Distinguish transformations and actions, giving examples of each. Explain narrow
   and wide dependencies and their relationship to shuffles. Classify `map`,
   `flatMap`, `filter`, `mapValues`, `groupByKey`, and `repartition`, stating any
   partitioner-related qualifications needed.

5. Explain `cache()` and persistence with `MEMORY_ONLY` and `MEMORY_AND_DISK` for
   the RDD setting used in the course. When is cached data first materialized,
   and what happens if partitions do not fit in memory? Why can repeated actions
   recompute an uncached lineage?

6. Explain how an RDD pipeline implements the map, grouping, and reduce work of a
   logical MapReduce round. Why need not logical MapReduce rounds correspond
   one-to-one to Spark stages or actions?
   ([08/09/2023, Part 1.1(b)](<../Slides/Exercises/Exams/Questions/Part 1.jpg>))

7. Describe `mapPartitions` in Python and `mapPartitionsToPair` in Java, including
   their input and output interfaces. Compare them with element-wise `map` and
   `flatMap`. Why is local aggregation possible without grouping by an explicit
   random key?
   ([Example WT 2, Part 1.1](../Slides/Exercises/Exams/ExampleWT-2.pdf))

8. Compare `groupByKey().mapValues(...)` and `reduceByKey(...)` for summing values
   by key. State the algebraic properties required of the reduction function and
   explain the communication benefit of local combining. Is subtraction a valid
   reduction? Is concatenating strings suitable for an order-independent result?

9. Explain `map`, `flatMap`, and `mapValues`, and their corresponding pair-producing
   Java methods. Show how a named function and a lambda can be passed as arguments.
   How does the number of output records differ between `map` and `flatMap`?

10. Describe the record types and aggregation steps in the course's one-round
    Word Count pipeline. Compare the roles of per-document counting,
    `groupByKey` followed by `mapValues`, and `reduceByKey`. Explain behavior when one
    word occurs in every document.

11. Explain the two-round Word Count method based on explicit random keys.
    Distinguish `groupBy` from `groupByKey`, describe local aggregation, and justify
    the bound on partial counts for one word before the final aggregation.
    ([[3.WordCountSpark#Technique 1 — Random Keys (groupBy)]])

12. Explain how the Word Count variant based on `mapPartitions` aggregates within
    existing partitions. Compare its shuffles, temporary state, and balance
    assumptions with the explicit-random-key variant. Why can document expansion
    make previously balanced partitions unbalanced?
    ([[3.WordCountSpark#Technique 2 — Spark Partitions (mapPartitions)]])

13. Explain what `repartition(L)` does and why it costs communication. Does preserving
    partition count preserve balance after a large `flatMap` or selective filter?
    Which quantities matter when choosing the number of partitions for Word Count
    versus an MR-FFT coreset?

14. Explain broadcast variables for a small global center set and how they support
    point-to-center assignment. Contrast them with collecting the entire point set
    into driver memory. Which data must fit locally in each approach?

15. Compare RDDs, DataFrames, and Datasets at the level covered in the notes. What
    structure or typing does each expose, and why are RDDs sufficient for the
    MapReduce algorithms implemented in this course?

16. Describe how an external stream is accessed and represented in the micro-batch
    Spark Streaming model used in the homeworks. Explain DStreams, batch RDDs,
    `socketTextStream`, and `foreachRDD`. How can a sequential item-at-a-time
    algorithm maintain its state across batches?
    ([19/07/2023, Question 2](../Slides/Exercises/Exams/Questions/19-07-2023/Questions.jpg);
    [Example WT 4, Part 1.4(b)](../Slides/Exercises/Exams/ExampleWT-4.pdf))

17. In the current streaming homework, explain how to process exactly the first $n$
    valid items when the final batch contains more items than needed. What memory
    and scalability issues arise from `collect()` or `toLocalIterator()` on the
    driver, and which parts of the computation remain distributed?
    ([[PROJECT_DESCRIPTIONS_EXAM]])

18. Describe the Spark data flow of MR-Fair-FFT: partition-local center extraction,
    collecting the coreset, final center selection, and distributed radius
    evaluation. Which objects reside on the driver and executors, and how does
    local oversampling affect their sizes?
    ([[PROJECT_DESCRIPTIONS_EXAM]])

19. HW1 reads data with `textFile(filePath, minPartitions=L)` and persists parsed
    points using `DISK_ONLY`. Does this call alone establish exactly $L$ balanced
    partitions? Explain how to inspect the actual partition count and sizes,
    and why this distinction matters for the theoretical MR-Fair-FFT space bound.
    ([HW1 input loading](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW1/G26HW1.py>))

20. Explain the timing policy used in HW1 and the role of the group-counting action
    in materializing persisted input. Which phases belong to the reported MRFairFFT
    runtime, and why is original-data radius evaluation measured separately?
    ([HW1 main program](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW1/G26HW1.py>))

21. In HW2, explain the roles of the micro-batch interval, `local[*]`, `foreachRDD`,
    and `threading.Event`. Why is stopping requested inside the callback but performed
    outside it? Explain how the batch callback enforces the valid-item prefix limit.
    ([HW2: process_batch and main](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/G26HW2.py>))

22. Suppose a processed batch is replayed after a failure while HW2's driver-side
    dictionaries and counters retain its previous updates. Are `process_item`
    and `process_batch` idempotent? Explain the effects on exact frequencies,
    sketches, and the stopping threshold. What additional state or processing
    protocol would be needed to justify exactly-once updates under this scenario?
    ([HW2 callbacks](</home/alessandrovulcu/Documenti/Università/Big-Data-Computing/HW2/G26HW2.py>))
