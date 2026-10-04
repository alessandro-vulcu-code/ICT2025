# Domande di teoria dagli esami

## Written exam: example 1

1. **[3 points]** Consider the execution of a MapReduce algorithm on a cluster with 10
   machines, each equipped with a RAM of 8 GB and a disk of 128 GB. Before and after
   the Map and Reduce Phases of each round, data are stored into a HDFS built on the
   union of the disks. Let $M_L$ and $M_A$ be the algorithm’s local and aggregate space.
   What are the maximum values (in GB) for $M_L$ and $M_A$ which ensure a successful
   execution of the algorithm?

2. **[3 points]** The coreset-based MapReduce algorithm for k-means computes the final
   centers of the clusters by running a sequential algorithm $\mathcal{A}$ on a weighted
   coreset $T$.

   (a) How are the points in $T$ computed?

   (b) For each point $q\in T$, what does its weight $w(q)$ represent?

3. **[4 points]** Consider the execution of Reservoir Sampling on an unbounded stream
   $\Sigma=x_1,x_2,\ldots$. For $t>m$, let $S_t$ be the set of $m$ elements maintained
   by the algorithm after processing $x_t$, and suppose that $x_t$ has been added to
   $S_t$. For an element $x_i$ with $i<t$, determine probability that $x_i\in S_t$, given
   that $x_t\in S_t$.

4. **[3 points]** Let $P$ be a set of points from a metric space $(M,d)$. Define the
   $(c,r)$-Approximate Near Neighbor Search problem and explain how it differs from the
   exact $r$-Near Neighbor Search problem.

## Written exam: example 2

1. **[3 points]** Spark API provides a method `mapPartitionsToPair`, in Java, or
   `mapPartitions`, in Python, to transform an RDD (it was used in the WordCount example,
   and in the homeworks). Briefly describe what the method does. You do not need to write
   code.

2. **[3 points]** Consider the adaptation of algorithm k-means++ to solve the weighted
   variant of k-means clustering for a pointset $P$, where each $x\in P$ has weight
   $w(x)\geq0$. Let $S$ be the current set of selected centers at some point during the
   algorithm. What is the probability that a given point $y\in P-S$ is selected as a next
   center?

3. **[3 points]** Consider the $\epsilon$-Approximate Frequent Items ($\epsilon$-AFI)
   problem for a stream $\Sigma=x_1,x_2,\ldots x_n$, with frequency threshold $\varphi$,
   and accuracy parameter $\epsilon\in(0,\varphi)$. For a desired confidence $\delta$,
   the Sticky Sampling algorithm ($n$ known) uses sampling rate
   $r=\ln(1/(\delta\phi))/\epsilon$. State and prove a bound on the expected working
   memory required by the algorithm.

4. **[4 points]** Referring to similarity search

   (a) Define the Range Reporting (RR) problem, and say how it differs from the Near
   Neighbor Search (NNS) problem.

   (b) Suppose that a kd-tree is used to store a set $P$ of points in $\mathbb{R}^2$.
   State the bounds on its space requirements and its query time for the RR problem.

## Written exam: example 3

1. **[3 points]** Answer the following questions:

   (a) What are the design goals that a *good* MapReduce algorithm should target,
   relatively to: number of rounds $R$, local space $M_L$, and aggregate space $M_A$?

   (b) Any sequential algorithm can be straightforwardly transformed into a 1-round
   MapReduce algorithm which uses one reducer: explain why this does not yield a *good*
   MapReduce algorithm.

2. **[3 points]** Refer to Round 2 of the algorithm for k-center with $z$ outliers
   implemented in Homework 3: briefly describe what the round does, and how the number
   of points it processes is affected by increasing the parameter $L$ (number of
   partitions).

3. **[4 points]** Let $S=\{c_1,c_2,\ldots,c_k\}$ be the solution computed by
   Farthest-First Traversal on a pointset $P$, and let $\Phi_{\mathrm{kcenter}}(P,S)$ be
   its objective function value. Define $q$ as the point of $P$ farthest from the centers.
   Using, without proof, the fact that $d(q,S)$ is less than or equal to the distance
   between any two points in $\{c_1,c_2,\ldots,c_k,q\}$, show that
   $\Phi_{\mathrm{kcenter}}(P,S)\leq2\Phi^{\mathrm{opt}}_{\mathrm{kcenter}}(P,k)$.

4. **[3 points]** Consider the computation of the distinct elements of a stream
   $\Sigma=x_1,x_2,\ldots x_n$. Explain how the Probabilistic Counting algorithm
   processes an element $x_j$ and how it derives the final estimate.

## Written exam: example 4

1. **[3 points]** Consider a MapReduce algorithm $A$ that uses local space $M_L$ and
   aggregate space $M_A$. In order to run $A$ successfully on a cluster, what
   characteristics must the cluster have?

2. **[3 points]** Consider the execution of MR-Farthest-First Traversal to compute a
   solution to k-center for a set $P$ of $N$ points. Briefly describe Round 1 and Round 2,
   and analyze their local space requirements as a function of the number $\ell$ of
   partitions.

3. **[4 points]** Consider a set $P$ of $n$ points from $\mathbb{R}^D$ stored in a hash
   table $T$ based on a hash function $h$ randomly selected from a $(p_1,p_2,c,r)$-locality
   sensitive family $\mathcal{H}$.

   (a) Explain how the hash table $T$ can be used for answering a $(c,r)$-Approximate
   Near Neighbor Search query.

   (b) Show that the query requires $O(Dnp_2)$ time in expectation.

4. **[3 points]** Answer the following questions regarding the streaming framework.

   (a) What are the performance metrics used to evaluate a streaming algorithm?

   (b) As seen in Homework 3, the Spark Stream provides the items in batches. Briefly
   explain how each batch is represented and how a standard streaming algorithm (which
   processes one item at the time) can be implemented using Spark Stream.

## Written exam: example 5

1. **[3 points]** With reference to the Resilient Distributed Dataset (RDD) of Spark,
   define the notion of *lazy evaluation* and explain how it may negatively affect the
   quality of time measurements.

2. **[3 points]** Consider a set $P$ of $N$ points from a metric space, and a subset
   $T\subseteq P$ of $k$ centers such that for every $x\in P$, $d(x,T)\leq R$. Let
   $\Delta$ and $\Delta_T$ denote the diameters of $P$ and $T$, respectively. State and
   prove an upper to $\Delta$ as a function of $\Delta_T$ and $R$.

3. **[3 points]** Suppose that Sticky Sampling is used to determine frequent items in a
   stream $\Sigma$ of $n$ items, with frequency threshold $\varphi$ and parameters
   $\epsilon$ and $\delta$. Let $S$ be the set of items returned by the algorithm. What
   are the probabilistic guarantees regarding $S$?

4. **[4 points]** (QUESTION RELATED TO THE HOMEWORS) Consider a set of points
   $U\subset\mathbb{R}^d$, split into two demographic groups $A$ and $B$, that is,
   $U=A\cup B$. Given a number of clusters $k$, fair k-means clustering aims at finding
   a set $C$ of centroids which minimize the fair objective function $\Phi(A,B,C)$.

   (a) Define $\Phi(A,B,C)$.

   (b) Suppose that 1 centroid must be chosen for the set of $n$ points in $\mathbb{R}$
   depicted in the image below. If $n\to+\infty$, what is a good centroid for the
   standard k-means objective and what is a good centroid for the above fair objective?

## Written exam: 08/09/23 - Part 1

1. **[3 points]** With reference to the RDD (*Resilient Distributed Dataset*) in Spark.

   (a) What is the *lazy evaluation* and how does it influence time measurements?

   (b) Briefly describe how an RDD is used in the implementation of a MapReduce round.

2. **[3 points]** Consider the center-based clustering problems k-center, k-means,
   k-median.

   - Define the objective function of each problem.
   - Define the notion of $c$-approximate solution $S$ for the 3 problems.
   - Describe the best clustering of $P$ induced by a given solution $S$, with respect
     to the objective functions of the 3 problems.

3. **[3 points]** Consider a stream $\Sigma=x_1,x_2,\ldots x_n$ with items from an
   universe $U$. Describe an algorithm that provides an estimate of the 0-th moment
   $F_0$ (i.e., number of distinct elements) in $O(\log|U|)$ bits.

4. **[4 points]** Consider a metric space $(M,d)$ with a family $\mathcal{H}$ of hash
   functions from $M$ to some range $[0,t]$.

   (a) For $0\leq p_2<p_1<1$, $c>1$ and $r>0$, when is family $\mathcal{H}$ called
   $(p_1,p_2,c,r)$-Locality Sensitive?

   (b) Assume $\mathcal{H}$ to be $(p_1,p_2,c,r)$-Locality Sensitive. Briefly describe
   the data structure based on $\mathcal{H}$ for the $(c,r)$-ANNS problem on an input
   $P$, and the query procedure for a point $q$.

## Written exam: 19/07/2023

1. **[4 points]** A MapReduce algorithm receives in input $N$ web documents, each
   represented by a pair $(url,D)$, where $D$ is the document and $url$ is its address.
   Assume that each pair occupies $O(1)$ space. Describe a map phase that splits the
   input into $\sqrt{N}$ small partitions, and state the theoretical guarantees for your
   partitioning.

2. **[3 points]** Briefly explain how a data stream, generated by some external source,
   can be processed in Spark Streaming, as seen in Homework 3.

3. **[3 points]** Suppose that we want to solve a problem $\Pi$ on instances $P$ which
   are too large to be processed by standard sequential algorithms. Briefly describe
   the composable coreset technique which can be used in this case, and state under what
   circumstances it is effective.

4. **[3 points]** Referring to similarity search

   (a) Define the Range Reporting (RR) problem, and say how it differs from the Near
   Neighbor Search (NNS) problem.

   (b) Suppose that a kd-tree is used to store a set $P$ of points in $\mathbb{R}^2$.
   State the bounds on its space requirements and its query time for the RR problem.

## Written exam: 29/06/2023

1. briefly explain the MR approx with node color from First homework.

2. average silhouette for C and how It captures Intra-cluster and Inter-cluster.

3. sticky sampling for epsilon-afi problem and why its Memory Is O(r).

4. def (c,r)-ANNS and the difference with NNS

## Theory questions: 14/07/2025

1. Tell how you can partition N (0, x) pairs into √N partitions and show the expected
   size of resulting partitions.

2. Tell how a coreset can be computed using MR-Farthest first traversal and state without
   proof how well it represents points in P. Tell one advantage and one disadvantage with
   respect to standard FFT.

3. Tell how a Bloom filter is initialized and how a query is made. Show that it never
   returns false negatives.

4. Define kd-tree and tell which problem can be solved efficiently using it.

## Theory questions: 18/06/2025

1. Explain lazy loading and how it affects quality of time measurements.

2. Let D and D_S be the diameters of P and S subset of P respectively. Give an upper
   bound to D as function of D_S knowing that d(x, S) < R, where x is a point of P.

3. Give the probabilistic guarantees for sticky sampling.

4. Write the objective function of fair k-centers. Then suppose we are in one dimensional
   space and there are n-1 points of class A overlapping at coordinate 0 and 1 point of
   class B at coordinate 1. Tell where we should place an optimal center with respect to
   the standard k-center objective function, and then with respect to the fair objective
   func.
