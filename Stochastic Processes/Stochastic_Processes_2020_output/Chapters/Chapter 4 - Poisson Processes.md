CHAPTER 4

Poisson Processes

Poisson processes play a distinct role in modeling many natural phenomena, at least in a first approximation. Moreover, they are mathematically simple, allowing to derive important analytical results and gain some relevant fundamental understanding.

In the following chapter, we will focus on defining and studying the properties of Poisson Processes.

# 4.1 The Poisson Distribution

The Poisson distribution with parameter  $\mu > 0$  is given by:

$$
p _ {k} \equiv \mathbb {P} [ X = k ] = \frac {e ^ {- \mu} \mu^ {k}}{k !} \quad \text {for} k = 0, 1, 2, \dots \tag {4.1}
$$

Recall (equation (1.15), pag. 18) that its mean and variance are:

$$
\mathbb {E} [ X ] = \mu \quad \operatorname {Var} [ X ] = \mu
$$

One first important property [1, ch. 5] is that the sum of two random variables with Poisson distributions follows a Poisson distribution too:

Theorem 4.1.1. Let  $X$  and  $Y$  be independent random variables having Poisson distributions with parameters  $\mu$  and  $\nu$ , respectively. Then the sum  $X + Y$  has a Poisson distribution with parameter  $\mu + \nu$ .

Proof. We proceed by direct computation of the distribution of  $X + Y$ , by searching an expression for  $\mathbb{P}[X + Y = n]$ . Each event  $\{X + Y = n\}$  is made up by the sequence of mutually exclusive events where  $X = k$  for some  $k = 0, \ldots, n$  and consequently  $Y = n - k$ . Thus, due to the law of total probability:

$$
\mathbb {P} [ X + Y = n ] = \sum_ {k = 0} ^ {n} \mathbb {P} [ X = k, Y = n - k ]
$$


Poisson distribution

Sum of Poisson variables is Poisson


Since $X$ and $Y$ are independent, the joint probabilities factorize:

$=\sum_{k=0}^{n}\mathbb{P}[X=k]\mathbb{P}[Y=n-k]=$
$\mathop{\equiv}_{(4.1)}\sum_{k=0}^{n}\frac{\mu^{k}e^{-\mu}}{k!}\frac{\nu^{n-k}e^{-\nu}}{(n-k)!}=$

Then we pull out a factor $e^{-\mu-\nu}$ that does not depend on $k$, and multiply and divide by $n!$ to highlight a *binomial sum*:

$=\frac{e^{-(\mu+\nu)}}{n!}\underbrace{\sum_{k=0}^{n}\frac{n!}{k!(n-k)!}\mu^{k}\nu^{n-k}}_{(\mu+\nu)^{k}}$

So:

$\mathbb{P}[X+Y=n]=\frac{e^{-(\mu+\nu)}(\mu+\nu)^{n}}{n!}\qquad n=0,1,\ldots$ (4.2)

which is exactly the Poisson Distribution (4.1) with parameter $\mu+\nu$. ∎

Another relevant fact is that *composing* a Poisson distribution with a Binomial one results in another Poisson distribution. More precisely:


Let $N$ be a Poisson random variable with parameter $\mu$, and conditional on $N$, let $M$ have a binomial distribution with parameters $N$ and $p$. Then the unconditional distribution of $M$ is Poisson with parameter $\mu p$.

In other words, if we pick $N$ objects, with $N$ following a Poisson distribution, and then *keep* each one of them with a given probability $p$, the number $M$ of remaining objects at the end will follow a Poisson distribution with parameter $\mu p\leq\mu$. In a sense, the second *binomial process* acts just as a “filter”, reducing the *effective rate* of the whole process without modifying the form of its distribution.


See ex. 1.6.1 at page 24. ∎

### 4.2 The Poisson Process

We now make a recap of what we have already seen in (2.2) at page 32.

A Poisson process describes, intuitively, how the *count* $X$ of *rare* events changes over time $t$. More formally:

###### Definition 1 (Poisson process).

A *Poisson process* of intensity, or rate, $\lambda>0$ is an integer-valued stochastic process $\{X(t):t\geq 0\}$ for which:

1. For any sequence of instants $t_{0}=0<t_{1}<t_{2}<...<t_{n}$ the process *increments*

$X(t_{1})-X(t_{0}),X(t_{2})-X(t_{1}),...,X(t_{n})-X(t_{n-1})$


are independent and stationary random variables.

Intuitively, each increment $X(t_{i+1})-X(t_{i})$ represents the number of *events* occurred in the time interval $(t_{i},t_{i+1}]$. So, in other words, this requirement tells us that the number of events occurring inside a certain time interval is *independent* of how many events occur in every other *disjoint* time interval. Moreover, *stationarity* means that $X(t_{i+1})-X(t_{i})$ depends *only* on the *size* of the time interval $t_{i+1}-t_{i}$: given more time *more* events will be observed, but the *rate* of occurrence is always fixed, and does not depend on the *absolute value* of $t$. In other words, we are describing a process in its *stationary* state, when its behavior does not change anymore.
2. For $s\geq 0$ and $t>0$, the random variables $X(s+t)-X(s)$ has a Poisson distribution with rate $\lambda t$:

$\mathbb{P}[X(s+t)-X(s)=k]=\frac{(\lambda t)^{k}e^{-\lambda t}}{k!}\qquad for\ k=0,1,2...$

Note that, in accordance with the previous requirement, the distribution of $X(s+t)-X(s)$ depends *only* on the duration $t$ of the inspected interval, since $\lambda$ is assumed to be *constant*.
3. $X(0)=0$. In other words, no event can occur *right at the start* at the process, when the counter is “reset”.

Note that if $X(t)$ is a Poisson process of rate $\lambda>0$, then its mean and variance are given by:

$\mathbb{E}[X(t)]=\lambda t\qquad\text{Var}[X(t)]=\lambda t$


Defects occur along an undersea cable according to a Poisson process of rate $\lambda=0.1$ per mile.

- What is the probability that no defects appear in the first two miles of the cable?

$X(2)$ has a Poisson distribution with parameter $\lambda t=0.1\cdot 2=0.2$, and so:

$\mathbb{P}[X(2)=0]=e^{-0.2}=0.8187$
- Given that there are no defects in the first two miles of cable, what is the conditional probability of no defects between mile two and three?

Here we use the independence of $X(3)-X(2)$ and $X(2)-X(0)=X(2)$. So it follows that the conditional probability is the same as the unconditional probability:

$\mathbb{P}[X(3)-X(2)=0]=\mathbb{P}[X(1)=0]=e^{-0.1}=0.9048$


Customers arrive in a certain store according to a Poisson process of rate $\lambda = 4$ per hour.

- Given that the store opens at 9.00 AM, what is the probability that exactly one customer has arrived by 9.30 and a total of five have arrived by 11.30 AM?

First we set as our unity time the hour, starting from 9.00 AM. We are asked to determine $\mathbb{P}[X(1/2) = 1, X(5/2) = 5]$. Using the independence of $X(5/2) - X(1/2)$ and $X(1/2)$, we reformulate the request as:

$$
\begin{array}{l}
\mathbb{P}[X(1/2) = 1, X(5/2) = 5] = \mathbb{P}[X(1/2) = 1, X(5/2) - X(1/2) = 4] = \\
= \left(\frac{e^{-4(1/2)} \left[4(\frac{1}{2})\right]^1}{1!}\right) \left(\frac{e^{-4(2)} [4(2)]^4}{4!}\right) = (2e^{-2}) \left(\frac{512}{3}e^{-8}\right) = 0.0155
\end{array}
$$

**Non-homogeneous processes.** A possible generalization of the Poisson process definition is to *relax* the stationarity hypothesis, by letting the rate $\lambda$ be a function of time: $\lambda(t)$.

This means that the average rate of number of counts per unit of time is not constant anymore, but changes with respect to time. In fact, the probability of a single event occurring in an infinitesimal interval $h$ of time is proportional to $\lambda$:

$$
\mathbb{P}[X(t + h) - X(t) = 1] = \frac{(\lambda h) e^{-\lambda h}}{1!} = (\lambda h)(1 - \lambda h + O(h^2))) = \lambda h + o(h)
$$

The probability of $k$ events happening in a time interval $(s, s + t]$ would then be given by:

$$
\mathbb{P}[X(t + s) - X(s) = k] = \frac{1}{k} \int_{s}^{t + s} (\lambda(t)t)^k e^{-\lambda(t)t}
$$

## 4.3 The Law of Rare Events

The incredible range of applicability of the Poisson distribution is explained by the fact that it is the “discrete analog” of the normal distribution.

For the latter, we know from the Central Limit Theorem that, under pretty mild assumptions, the sum of many continuous random variables will follow a Gaussian distribution — and this is why the Gaussian is so relevant in statistics.

A similar thing happens for the discrete random variables, with the final distribution being the Poisson distribution. This is the so-called *Law of Rare Events*. In essence, suppose that a certain event can occur in many circumstances, but has a low probability of happening in any specific circumstance. We say that this event is “rare”, and the *Law of Rare Events* states that the

Poisson as a “discrete” analog of the normal distribution


total number of these rare events that do happen follows (approximately) a Poisson distribution.

The simplest example of rare events is given by considering an experiment with a low and fixed probability $p\ll 1$ of success, which is repeated a high number $N$ of times. In this case, the total number of successes $X_{N,p}$ after $N$ trials follows a binomial distribution:

$\mathbb{P}[X_{N,p}=k]=\frac{N!}{k!(N-k)!}p^{k}(1-p)^{N-k}\qquad\text{for }k=0,\ldots,n$

In the limit of rare events $p\to 0$ and infinite trials $N\to+\infty$, with a fixed success rate $Np\equiv\mu>0$, it is known from probability theory that $X_{N,p}$ will follow the Poisson distribution:

$\mathbb{P}[X_{\mu}=k]=\frac{e^{-\mu}\mu^{k}}{k!}\qquad\text{for }k=0,1,2,\ldots$

The Law of Rare Events, however, is much more general than that. In particular, even if the probability of success $p$ changes at each trial $i$, in the limit $N\to\infty$ $X_{N,\boldsymbol{p}}$ will still follow a Poisson distribution, this time with rate $\sum_{i=1}^{N}p_{i}$. More formally, this is a consequence of the following theorem:


Let $\boldsymbol{\epsilon}_{1}$, $\boldsymbol{\epsilon}_{2}...$ be independent Bernoulli random variables, where:

$\mathbb{P}[\boldsymbol{\epsilon}_{i}=1]=p_{i}\quad\text{and}\quad\mathbb{P}[\boldsymbol{\epsilon}_{i}=0]=1-p_{i}$

and let $S_{n}=\boldsymbol{\epsilon}_{1}+\cdots+\boldsymbol{\epsilon}_{n}$. The distribution of $S_{n}$ is given by:

$$
\mathbb{P}[S_{n}=k]=\!\!\sum_{\begin{subarray}{c}x_{i}=\pm 1\\
x_{1}+\cdots+x_{n}=k\end{subarray}}\prod_{i=1}^{n}p_{i}^{x_{i}}(1-p_{i})^{1-x_{i}}
$$

which differs from a Poisson distribution with rate $\mu=p_{1}+\cdots+p_{n}$ by at most:

$$
\left|\mathbb{P}[S_{n}=k]-\frac{\mu^{k}e^{-\mu}}{k!}\right|\leq\sum_{i=1}^{n}p_{i}^{2}
$$

In particular, if all $p_{i}\equiv p$ and $Np=\mu$ is kept fixed, in the limit $N\to+\infty$, $p=\mu/N\to 0$, and so does the RHS of 4.4.

An analog of the Law of Rare Events holds for stochastic processes, stating that the total counts of events generated by many independent processes can be approximately described by a single Poisson process.

In other words, consider a high number $M$ of processes (not necessarily Poisson processes) generating events at random times. Each of them can be described by a separate time axis with a certain number of points (representing events) on it. If we combine all axes, and consider only the total number of events $X(t)$ occurred before a given time $t$, without considering their different origin, then, in the limit $M\to\infty$, $X(t)$ would be described by a Poisson process.

Law of Rare Events, fixed probability case

Law of Rare Events: general case

Law of Rare Events applied to Poisson processes


As the sum of many discrete random variables will approximately follow a Poisson distribution, so does the combination of many stochastic processes.

This is really useful in reality, because often the events we are interested in can be produced in different ways by different natural phenomena, each following a different law, destroying any hope of a complete description. However, thanks to the Law of Rare Events, we can still describe the counts of these events with a unique Poisson process — even if no one of the underlying stochastic processes is Poisson.

# 4.4 Properties of Poisson Processes

Poisson processes share many of the important properties of the Poisson distribution.

For example, in analogy with theorem 4.1.1, combining two Poisson processes leads to another Poisson process. More formally [2, day 21/04]:

Theorem 4.4.1. Let  $X_{1}(t)$  and  $X_{2}(t)$  be two independent Poisson Processes with rates  $\lambda_{1}, \lambda_{2}$ . Then, the variable that counts both of them  $X(t) = X_{1}(t) + X_{2}(t)$  is a Poisson process itself with rate  $\lambda = \lambda_{1} + \lambda_{2}$ .

Sum of Poisson processes

![[Stochastic_Processes_2020_p131_img34.jpeg]]
Figure (4.1) - Graphical representation of two combined Poisson processes, where their sum is a Poisson process itself with its parameter that is the sum of the two parameters

Proof. To prove that  $X(t)$  is a Poisson process, we just need to verify that it satisfies the three requirements in definition 1.

1. At the starting time  $t = 0$ , the number of events counted for both processes will be zero ( $X_{1}(0) = X_{2}(0) = 0$ ), and so their sum:  $X(0) = 0$
2. Since  $X_{1}$  and  $X_{2}$  have stationary and independent increments separately, so does  $X$  that is their sum. This can be shown explicitly by writing the distribution of  $X$ .
3. Given the fact that the random variables  $X_{1}(t)$  and  $X_{2}(t)$  are Poisson distributed with parameter  $\lambda_1 t$  and  $\lambda_2 t$  and are independent of each other, their sum  $X(t) = X_{1}(t) + X_{2}(t)$  is therefore a Poisson distribution with parameter  $(\lambda_1 t + \lambda_2 t)$  as a consequence of theorem 4.1.1.

□

Similarly, filtering a Poisson process by selecting each generated event with a fixed probability  $p$ , results again in a Poisson process in the end, in analogy of what happens in theorem 4.1.2. More formally:

Theorem 4.4.2. Let  $X(t)$  be a Poisson Process with rate  $\lambda$  and let each event be independently marked as either type 1 with probability  $p$ , or type 2 with probability  $1 - p$ . Then, the events of the type 1 and 2 follow two independent Poisson Processes with rates  $\lambda p$  and  $\lambda (1 - p)$ .

![[Stochastic_Processes_2020_p132_img35.jpeg]]
Figure (4.2) - Graphical representation of two split Poisson processes with the conditions stated in theorem 4.4.2

Proof. As before, we start by verifying the 3 requirements of definition 1:

1. When we start counting since there are no events at all, so  $X_{1}(0) = X_{2}(0) = 0$
2. Since  $X$  has stationary and independent increments and the marking of events occurs independently, then  $X_{1}$  and  $X_{2}$  inherit from  $X$  the stationarity and independence of their respective increments.
3. The joint distribution of the number of arrivals in the two sub-processes before a fixed time  $t$  is:

$$
\mathbb {P} [ X _ {1} (t) = n, X _ {2} (t) = m ] = \mathbb {P} [ X _ {1} (t) = n | X (t) = n + m ] \mathbb {P} [ X (t) = n + m ] =
$$

since if  $X(t) = n + m$  and  $X_{1}(t) = n$ , then  $X_{2}(t) = m$ . Note that  $\mathbb{P}[X_1(t) = n|X(t) = n + m]$  is the probability of accepting exactly  $n$  events from  $n + m$  trials, where the success probability of each trial is  $p$ , which is given by a Binomial distribution, leading to:

$$
\begin{array}{l} = \left( \begin{array}{c} n + m \\ n \end{array} \right) p ^ {n} (1 - p) ^ {m} \frac {e ^ {- \lambda t} (\lambda t) ^ {n + m}}{(n + m) !} = \\ = \frac {(n + m) !}{n ! m !} p ^ {n} (1 - p) ^ {m} e ^ {- \lambda p t} e ^ {- \lambda (1 - p) t} \frac {(\lambda t) ^ {n + m}}{(n + m) !} = \\ = \frac {(\lambda p t) ^ {n} e ^ {- \lambda p t}}{n !} \frac {(\lambda t (1 - p)) ^ {m} e ^ {- \lambda (1 - p) t}}{m !} \\ \end{array}
$$

which is exactly the product of two Poisson distributions, with rates  $\lambda tp$  and  $\lambda t(1 - p)$  respectively.

From the last point we know that  $X_{1}(t)$  and  $X_{2}(t)$  are independent random variables when they are evaluated at the same instant  $t$ . However, to prove that  $X_{1}$  and  $X_{2}$  are independent Poisson processes, we need to show that the increments  $X_{1}(t_{3}) - X_{1}(t_{1})$  and  $X_{2}(t_{4}) - X_{2}(t_{2})$  are independent for every possible choice of the intervals  $[t_1,t_3]$  and  $[t_2,t_4]$ .


- Let's start from the case  $t_1 < t_2 < t_3 < t_4$ , where there is a partial overlap in  $[t_2, t_3]$  (fig. 5.10a). We can split it into two non-overlapping parts  $[t_1, t_2]$  and  $[t_3, t_4]$ , and the overlap  $[t_2, t_3]$ , by rewriting:

$$
X_{1}(t_{3}) - X_{1}(t_{1}) = [X_1(t_3) - X_1(t_2)] + [X_1(t_2) - X_1(t_1)]
X_{2}(t_{4}) - X_{2}(t_{2}) = [X_{2}(t_{4}) - X_{2}(t_{3})] + [X_{2}(t_{3}) - X_{2}(t_{2})]
$$

Since  $X_{1}(t)$  and  $X_{2}(t)$  are independent when evaluated at the same time, the increments on the overlap  $X_{1}(t_{3}) - X_{1}(t_{2})$  and  $X_{2}(t_{3}) - X_{2}(t_{2})$  are independent. In all other cases we are dealing with Poisson increments on disjoint time intervals, which are guaranteed to be independent. Finally, sums of pairwise independent random variables are independent, and so  $X_{1}(t_{3}) - X_{1}(t_{1})$  and  $X_{2}(t_{4}) - X_{2}(t_{2})$  are independent of each other.

- The same reasoning can be applied to all the other overlaps. If  $t_1 < t_2 < t_4 < t_3$ , i.e. if one interval  $[t_2, t_4]$  is inside the other  $[t_1, t_3]$  (fig. 5.10b), we can again split the intervals in three regions: two non-overlapping  $([t_1, t_2]$  and  $[t_4, t_3])$ , and one overlapping  $([t_2, t_4])$ . We then proceed as before.
- The final case (fig. 4.3c) is trivial, since there is no overlap.

![[Stochastic_Processes_2020_p133_img36.jpeg]]
(a) - The two time intervals may be overlapping in some part of them.

![[Stochastic_Processes_2020_p133_img37.jpeg]]
(b) - Another case is when a time interval fully contains the other one.

![[Stochastic_Processes_2020_p133_img38.jpeg]]
(c) - The last case is where the two time intervals are disjoint.
Figure (4.3) - All the possible overlaps of two intervals  $[t_1, t_3]$  and  $[t_2, t_4]$ .

# 4.5 Other distributions

A Poisson process is much more than a collection of Poisson distributed increments  $X(t_{n}) - X(t_{n - 1})$ . Depending on which aspect of the process we focus on, different distributions emerge [1, sec. 5.3].

As a start, let's consider the arrival times (or waiting times)  $W_{i}$  at which a new event occurs, and the count  $X$  goes up by 1 (fig. 4.4). We define the interarrival times (or sojourn times)  $S_{i}$  as the difference between two consecutive arrival times:

$$
S _ {i} \equiv W _ {i + 1} - W _ {i}
$$


Clearly:

$$
W _ {i} = \sum_ {k = 0} ^ {i - 1} S _ {k}
$$

![[Stochastic_Processes_2020_p134_img39.jpeg]]
Figure (4.4) – A typical sample path of a Poisson process showing the waiting times $W_{i}$ and the sojourn times $S_{n}$.

Let's find the statistics of these quantities. For the inter-arrival times, we already know the answer:

Theorem 4.5.1. Inter-arrival times $S_{i}$ are i.i.d. exponential random variables with rate $\lambda$ [1, thm 5.5].

Inter-arrival $W_{i} \sim$ Exponential

Proof. See the proof theorem (2.2.1) at page 33.

For the waiting times, we have instead:

Theorem 4.5.2. The waiting time $W_{n}$, i.e. the time needed for the $n$-th event to occur, has the gamma distribution whose probability density function is [1, thm 5.4]:

Waiting times $W_{i} \sim$ Gamma

$$
f _ {W _ {n}} (t) = \frac {\lambda^ {n} t ^ {n - 1}}{(n - 1) !} e ^ {- \lambda t} \qquad n = 1, 2, \ldots \quad t \geq 0
$$

Proof. Recall the fact that we defined the Gamma distribution in (1.5.4 at pag. 20) with parameters $n, \lambda$, as the distribution of the sum of $n$ i.i.d. exponential random variables with parameter $\lambda$. So, since:

$$
W _ {n} = \sum_ {i = 0} ^ {n - 1} S _ {i}
$$

where $S_{i}$, $i = 0, \dots, n - 1$ are all exponential random variables with rate $\lambda$, it follows that the sum $W_{n}$ is a Gamma distribution.

If we fix the number $n$ of events occurring in the time interval $(0, t)$, then the joint probability of the arrival times $\{W_i\}_{i=1,\dots,n}$ is that of an ordered sequence of uniformly chosen points, which can be derived from the uniform distribution as follows.

Suppose we choose independently $n$ points $U_{i}$ uniformly in the interval $(0, t)$ (fig. 4.5). The joint distribution of $\{U_{i}\}_{i=1,\dots,n}$ is given by the product of $n$


![[Stochastic_Processes_2020_p135_img40.jpeg]]
Figure (4.5) - Let us draw some points  $(U_i$ 's) on the interval  $(0, t)$  that distribute uniformly. Then consider also their ordered version  $W_i$ 's. The goal is to compute their statistics.

uniform pdfs.

The situation drastically changes when we consider the order of the points. Let's call  $\{W_i\}$  the sequence of ordered  $U_i$ , with  $0 \leq W_1 < W_2 < \dots < W_n \leq t$ . Note that the  $W_i$  are not independent of each other, since they must satisfy the ordering. This makes much more difficult to compute their joint probability.

So, let us start with the simplest case where we have only two points, and then proceed to generalize. Since we are working with continuous variables, we consider the probability of  $W_{1}$  and  $W_{2}$  respectively being inside two small intervals  $[w_{1}, w_{1} + \Delta w_{1}]$  and  $[w_{2}, w_{2} + \Delta w_{2}]$  (fig. 4.6).

![[Stochastic_Processes_2020_p135_img41.jpeg]]
Figure (4.6) - Now let us consider only to points and their corresponding intervals  $[w_i, w_i + \Delta w_i]$ . Note that in either one of the two ordered intervals may be contained either  $U_1$  or  $U_2$ , and there are two possible combinations when assigning them.

In the limit of  $\Delta w_{1},\Delta w_{2}\to 0$  , the probability density  $f_{W_1,W_2}(w_1,w_2)$  is constant inside these intervals, and so:

$$
f _ {W _ {1}, W _ {2}} \left(w _ {1}, w _ {2}\right) \Delta w _ {1} \Delta w _ {2} = \mathbb {P} \left[ w _ {1} \leq W _ {1} \leq w _ {1} + \Delta w _ {1}, w _ {2} \leq W _ {2} \leq w _ {2} + \Delta w _ {2} \right] \tag {4.5}
$$

The latter is equal to the probability of  $U_{1}$  (or  $U_{2}$ ) being in  $[w_{1}, w_{1} + \Delta w_{1}]$  and the other in  $[w_{2}, w_{2} + \Delta w_{2}]$ . This is because every permutation of the same  $\{U_{i}\}$ , once ordered, will result in the same collection of  $\{W_{i}\}$ , and so we must count all of them:

$$
\begin{array}{l} = \mathbb {P} [ w _ {1} \leq U _ {1} \leq w _ {1} + \Delta w _ {1}, w _ {2} \leq U _ {2} \leq w _ {2} + \Delta w _ {2} ] + \\ \mathbb {P} \left[ w _ {1} \leq U _ {2} \leq w _ {1} + \Delta w _ {1}, w _ {2} \leq U _ {1} \leq w _ {2} + \Delta w _ {2} \right] = \\ \end{array}
$$

Note that we may sum the probabilities of all different permutations since they are mutually exclusive.

Since  $U_{1}$  and  $U_{2}$  are both uniform and independent, we have:

$$
\mathbb {P} [ w _ {1} \leq U _ {1} \leq w _ {1} + \Delta w _ {1}, w _ {2} \leq U _ {2} \leq w _ {2} + \Delta w _ {2} ] = \frac {\Delta w _ {1}}{t} \frac {\Delta w _ {2}}{t}
$$


and the same holds for every other permutation, leading to:

$$
f_{W_{1},W_{2}}(w_{1},w_{2})\Delta w_{1}\Delta w=2\left(\frac{\Delta w_{1}}{t}\right)\left(\frac{\Delta w_{2}}{t}\right)=2t^{-2}\Delta w_{1}\Delta w_{2}
$$

Now, by dividing both (4.5) and (4.6) for $\Delta w_{1}\Delta w_{2}$ and passing to the limit we obtain that:

$$
f_{W_{1},W_{2}}(w_{1},w_{2})=2t^{-2}
$$

The 2 comes from the fact that there are only two possible ways in which we can dispose $U_{1}$ and $U_{2}$ in the two intervals.
By repeating the same reasoning, (4.7) can be generalized to the case of 3 points: $U_{1}$, $U_{2}$, $U_{3}$. This time, there are $2\cdot 3$ possible ways in which we can arrange the 3 elements, and the exponent of $t$ will be $-3$.
Generalizing this argument up to $n$ elements, the number of permutations of $n$ elements $U_{1},U_{2}...U_{n}$ is $n!$, whereas the joint pdf will be proportional to $t^{-n}$. So, the joint probability density function for $W_{1},W_{2},\ldots,W_{n}$ is given by:

$$
f_{W_{1},W_{2}...W_{n}}(w_{1},w_{2},...,w_{n})=n!t^{-n}\qquad\mbox{for }0<w_{1}<w_{2}<...<w_{n}\leq t
$$

Note that the pdf’s domain is not the entire $(0,t)^{n}$, since the $w_{i}$ must be in ascending order.
On the other hand, the joint pdf for $n$ uniform points in $(0,t)$ is given by:

$$
f_{U_{1},U_{2},...,U_{n}}(w_{1},w_{2},...,w_{n})=t^{-n}
$$

with the domain spanning the entire $(0,t)^{n}$, since the $U_{i}$ need not be ordered.

We are finally able to formally state and prove the link between Poisson processes and the ordered uniform distribution:


Let $W_{1},W_{2},\ldots$ be the ordered occurrence times in a Poisson process of rate $\lambda>0$. Let us condition on $X(t)\equiv N(t)=n$, that is the fact that in interval $(0,t)$ we observe exactly $n$ events. Given their number, the arrival times of $n$ events $\{W_{1},W_{2},\ldots,W_{n}\}$ have the joint probability density function *[1, thm 5.7]*:

$$
f_{W_{1},...,W_{n}|X(t)=n}(w_{1},\ldots,w_{n})=n!t^{-n}\qquad\mbox{for }0<w_{1}<\cdots<w_{n}\leq t
$$

Note that this theorem holds only if we are told how many events ($N(t)=n$) we have observed in interval $(0,t)$. In other words the theorem states that, given their number, the arrival times of $n$ events have the joint probability that is equal to the distribution obtained by ordering $n$ independent and uniform random variables.


Let’s first assume that all $w_{i}$’s are distinct. This can be done because, in a Poisson process, the probability of two events occurring at the same time is negligibly small, and so can be neglected. This is a consequence of the fact that the probability of one arrival in a given interval goes to zero linearly w.r.t. the size of the interval (see section (2.2)). Thus, as the interval’s length goes


to zero, the only relevant events will be either one arrival or no arrivals at all. Informally, in a Poisson process "simultaneous events are impossible".

If all  $w_{i}$  are distinct, we can choose intervals  $[w_{i}, w_{i} + \Delta w_{i}]$  such that they are all disjoint, since  $\Delta w_{i}$  can be as small as needed. We can then consider the probability that, given exactly  $n$  arrivals, there  $i$ -th arrival  $W_{i}$  lies inside the  $i$ -th interval  $[w_{i}, w_{i} + \Delta w_{i}]$ :

$$
\mathbb {P} [ w _ {i} \leq W _ {i} \leq w _ {i} + \Delta w _ {i}, i = 1, \dots , n | X (t) = n ] = \tag {4.11}
$$

which, in the limit of  $\Delta w_{i}\to 0$ , is linear in the joint probability density  $f_{W_1,\ldots ,W_n|X(t) = n}(w_1,\ldots ,w_n)$ :

$$
= f _ {W _ {1}, \dots , W _ {n} | X (t) = n} (w _ {1}, \dots , w _ {n}) \Delta w _ {1} \dots \Delta w _ {n} + o (\Delta w _ {1}, \dots , \Delta w _ {n})
$$

If we can compute (4.11), dividing by the  $n$ -dim volume and taking the limit leads to an expression for the density.

![[Stochastic_Processes_2020_p137_img42.jpeg]]
Figure (4.7) - We note as the expression (4.11) requires as there must be no arrivals outside each interval  $[w_i, w_i + \Delta w_i]$ . Each increment, since belongs to a disjoint interval, is independent of the others.

So, let's proceed by computing the probability (4.11). This is the probability that we have exactly one arrival for each interval  $[w_i, w_i + \Delta w_i]$ , while having zero arrivals outside them (fig. 4.7), given that  $n$  events have occurred. Since Poisson increments over disjoint intervals are independent, we have:

$$
\begin{array}{l} = \mathbb {P} [ \text {o n e a r r i v a l i n} [ w _ {i}, w _ {i} + \Delta w _ {i} ], i = 1, \dots , n \text {a n d} \\ \text {z e r o a r r i v a l s e v e r y w h e r e e l s e i n} [ 0, t ] \mid X (t) = n ] = \\ = \frac {\lambda \Delta w _ {1} e ^ {- \lambda \Delta w _ {1}} \lambda \Delta w _ {2} e ^ {- \lambda \Delta w _ {2}} \dots \lambda \Delta w _ {n} e ^ {- \lambda \Delta w _ {n}} e ^ {- \lambda (t - \sum_ {i = 1} ^ {n} \Delta w _ {i})}}{e ^ {- \lambda t} (\lambda t) ^ {n} / n !} = \\ \end{array}
$$

Where we recognize the first factors as the probability of exactly one event in each interval  $\Delta w_{i}$ , and the last one as having no events at all in the remaining  $(t - \sum_{i=1}^{n} \Delta w_{i})$ . In order to condition the probability on an event, we had to divide the denominator by the probability of the event to occur. But since  $X(t) = n$  is a Poisson process, this is simply  $e^{-\lambda t} (\lambda t)^{n} / n!$ , that is the probability of having  $n$  events in a time interval of length  $t$ .

Note now that at the numerator the terms  $e^{\lambda \Delta w_1} \ldots e^{\lambda \Delta w_n} = e^{\lambda \sum_{i=1}^{n} \Delta w_i}$  cancel out, and so do  $e^{-\lambda t}$  and  $\lambda$ . At the end we obtain:

$$
f _ {W _ {1}, \dots , W _ {n} | X (t) = n} (w _ {1}, \dots , w _ {n}) \Delta w _ {1} \dots \Delta w _ {n} + o (\Delta w _ {1}, \dots , \Delta w _ {n}) = n! t ^ {- n} \Delta w _ {1} \dots \Delta w _ {n}
$$

Dividing both terms by  $\Delta w_{1}\cdot \cdot \cdot \cdot \Delta w_{n}$  and taking the limit  $\Delta w_{i}\to 0\quad i =$


$1,\ldots ,n$  completes the proof:

$$
f _ {W _ {1}, \dots , W _ {n} | X (t) = n} (w _ {1}, \dots , w _ {n}) = n! t ^ {- n}
$$

We can summarize this result by saying that, if we know how many arrivals we have in a Poisson process in an interval  $(0,t)$ , the joint distribution, conditioned on the number  $n$  of arrivals, is the same that would be obtained by considering  $n$  ordered uniform random variables each distributed in the same interval.

Suppose now that  $n$  events have happened in  $(0, t)$ . Then, the probability of  $k \leq n$  events happening in  $(0, u)$ , with  $u \leq t$ , is given by a Binomial distribution:

Theorem 4.5.4. Let  $X(t)$  be a Poisson process with rate  $\lambda$ . Given the fact we know that in the interval  $(0, t)$  we have  $n$  arrivals, that is  $X(t) = n$ , we want to find the probability that the number of arrivals in a subset  $0 < u < t$  is  $0 \leq k \leq n$ . Then, in formulas [1, thm 5.6]:


![[Stochastic_Processes_2020_p138_img43.jpeg]]
Figure (4.8) - Since we know that  $(0,t)$  contains  $n$  events, the arrival times  $X_{n}$  are uniform in  $X_{n}$ , and so each of them will fall into  $(0,u)$  with a probability  $p = u / t$ . So, the probability of  $k$  events being in  $(0,u)$  is that of obtaining  $k$  successes (each with probability  $p$ ) after  $n$  trials, which is given by a Binomial distribution.

Proof. In order to prove it we use the results provided by the previous theorem: since given  $X(t) = n$  the  $n$  arrival times are i.i.d. uniformly distributed in the interval  $(0, t)$ , the probability that each falls in the interval  $[0, u]$  is  $u / t$  and therefore  $X(u)$  is binomial with parameters  $(n, u / t)$  thus concluding the proof. This is moreover shown in figure 4.8

A similar result holds for the combination of two Poisson processes:

Theorem 4.5.5. Let  $X_{1}(t), X_{2}(t)$  be two concurrent independent Poisson processes with rates  $\lambda_{1}, \lambda_{2}$ . Given the total number of arrivals in interval  $(0, t)$  i.e.  $X_{1}(t) + X_{2}(t) = n$ , the probability of having  $k$  arrivals in the first process is:

$$
\mathbb {P} \left[ X _ {1} (t) = k \mid X _ {1} (t) + X _ {2} (t) = n \right] = \binom {n} {k} \left(\frac {\lambda_ {1}}{\lambda_ {1} + \lambda_ {2}}\right) ^ {k} \left(\frac {\lambda_ {2}}{\lambda_ {1} + \lambda_ {2}}\right) ^ {n - k} \tag {4.12}
$$


As expected, this probability is given by a binomial distribution.

In fact, the probability $p_{1}$ of a generic event belonging to 1 is the ratio between the rate $\lambda_{1}$ of 1, and the total rate $\lambda_{1}+\lambda_{2}$ of both processes. If $\lambda_{1}=\lambda_{2}$, $p_{1}=1/2$ as expected, since in this case we are combining two equal Poisson processes. If, for instance, $\lambda_{1}=2\lambda_{2}$, then $p_{1}=2/3$, while $p_{2}=1/3=1-p_{1}$ is the probability of an event belonging to 2.


We proceed by direct computation of the LHS of (4.12) by applying the definition of conditional probability, leading to:

$$
\frac{\mathbb{P}[X_{1}(t)=k,\ X_{1}(t)+X_{2}(t)=n]}{\mathbb{P}[X_{1}(t)+X_{2}(t)=n]}=
$$

If $X_{1}(t)+X_{2}(t)=n$ and $X_{1}(t)=k$, then $X_{2}(t)=n-k$. Then, since $X_{1}$ and $X_{2}$ are independent processes, we can factorize the joint probability:

$$
=\frac{\mathbb{P}[X_{1}(t)=k\ ,\ X_{2}(t)=n-k]}{\mathbb{P}[X_{1}(t)+X_{2}(t)=n]}=
=\frac{e^{-\lambda_{1}t}(\lambda_{1}t)^{k}}{k!}\frac{e^{-\lambda_{2}t}(\lambda_{2}t)^{n-k}}{(n-k)!}\frac{n!}{e^{-(\lambda_{1}t+\lambda_{2}t)}(\lambda_{1}t+\lambda_{2}t)^{n}}=
=\binom{n}{k}\left(\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}\right)^{k}\left(\frac{\lambda_{2}}{\lambda_{1}+\lambda_{2}}\right)^{n-k}
$$

which completes the proof. ∎

Finally, we can compose theorems 4.5.4 and 4.5.5 as follows:


Let $X_{1}(t)$ and $X_{2}(t)$ be two independent Poisson processes with rates $\lambda_{1}$, $\lambda_{2}$ in the interval $(0,t)$. Let $s$ be a subset of $t$ s.t. $0<s<t$. Given we know the total number $n$ of arrivals in the interval $(0,t)$ i.e. $X_{1}(t)+X_{2}(t)=n$, the probability of $0\leq k\leq n$ events occurring for process $1$ in the subset $(0,s)$ is given by:

$$
\mathbb{P}[X_{1}(s)=k|X_{1}(t)+X_{2}(t)=n]=\frac{n!}{k!(n-k)!}\left(\frac{\lambda_{1}s}{(\lambda_{1}+\lambda_{2})t}\right)^{k}\left(\frac{\lambda_{1}(t-s)+\lambda_{2}t}{(\lambda_{1}+\lambda_{2})t}\right)^{n-k}
$$


We proceed again by direct computation. By applying the definition of conditional probability we have:

$$
\mathbb{P}[X_{1}(s)=k|X_{1}(t)+X_{2}(t)=n]=\frac{\mathbb{P}[X_{1}(s)=k,\ X_{1}(t)+X_{2}(t)=n]}{\mathbb{P}[X_{1}(t)+X_{2}(t)=n]}=
$$

If $n$ events have occurred in $X_{1}+X_{2}$ during $(0,t)$, $k$ of which belonging to 1 in the interval $(0,s)$, then $n-k$ events must have occurred in $X_{2}$ during $(0,t)$ or in $X_{1}$ during $(s,t)$, i.e. $X_{1}(t)-X_{1}(s)+X_{2}(t)=n-k$. Now all of these random variables are independent, and so the joint probability factorizes:

$$
=\frac{\mathbb{P}[X_{1}(s)=k,\ X_{1}(t)-X_{1}(s)+X_{2}(t)=n-k]}{\mathbb{P}[X_{1}(t)+X_{2}(t)=n]}=
$$


![[Stochastic_Processes_2020_p140_img44.jpeg]]

![[Stochastic_Processes_2020_p140_img45.jpeg]]
Figure (4.9) - The situation can be described by using this graph: we are dealing with a large interval  $(0, t)$  which contains  $(0, s)$ , that is the base of rectangle. There are moreover two processes  $\lambda_1$  and  $\lambda_2$  that rule the number of arrivals, and either them individually or their sum can be drawn onto the vertical axis. The product between the two sides of the rectangle returns the parameters defining the Poisson process we are interested in.

This result has a geometric interpretation (fig. 4.9). In particular, the term  $\left(\frac{\lambda_1s}{(\lambda_1 + \lambda_2)t}\right)^k$  is the ratio between the small area in the figure, representing the event we are looking for, and the larger area, i.e. the conditional event.

# 4.5.1  $\mathbf{M} / \mathbf{G} / \infty$  queue

We want now to use the theorems we have just proved by analyzing the following example, dealing with a radioactive mass material.

A similar one would be a service station where each user arrives according to a Poisson process at time  $W_{k}$ . A customer will remain in the station for a certain amount of time  $Y_{k}$  and then will depart. The difference between these examples and the ones we saw in the previous lectures ( $M / G / XX$ ), is that in this case there is no waiting times for service: once a customer enters the system he will not wait his turn and will be immediately served, no matter how many clients are already being served. We can then state that the number of services is therefore infinite, and describe our problem as a  $\mathbf{M} / \mathbf{G} / \infty$  queue. In this formalism  $M(t)$  is the Poisson distribution that describes our arrivals, whereas  $G(t)$  denotes the generic distribution of waiting times, while  $\infty$  tells that we can serve an infinite number of customers at the same time.


![[Stochastic_Processes_2020_p141_img46.jpeg]]
Figure (4.10) – The figure depicts example (15). Particle created at time $W_{k} \leqslant t$ still exists at time $t$ if $W_{k} + Y_{k} \geqslant t$


Viewing a fixed mass of a certain radioactive material, suppose that *alpha* particles appear in time according to a Poisson process of intensity $\lambda$. Each particle exists for a random duration and is then annihilated. Suppose that the successive lifetimes $Y_{1}, Y_{2}, \ldots$ of distinct particles are independent random variables having the common distribution function $G(y) = Pr\{Y_{k} \leqslant y\}$. Let $X(t)$ be the total number of particles created up to time $t$, and let $M(t)$ count the number of alpha particles existing at time $t$. Obviously it must hold that $M(t) \leqslant X(t)$, since the number of existing particles cannot exceed the number of particles created. The problem is depicted in figure 4.10.

We want now to find the number of particles present at time $t$: so we want to compute $M(t)$ given that at the beginning the timer was zero, i.e. $M(0) = 0$. We moreover condition on the number $n$ of particles emitted up to time $t$, that is $X(t) = n$, where $W_{1},\ldots ,W_{n}\leqslant t$ are the times when particles were created. Then, for each particle emitted, we have that the particle $k$ still exists if and only if $W_{k} + Y_{k}\geqslant t$: the sum of its arrival and service times must be greater than the actual time $t$. Let us introduce the indicator function such that indicates whether a particle still exists at time $t$:

$$
\mathbb {1} \{W _ {k} + Y _ {k} \geqslant t \} = \left\{ \begin{array}{l l} 1 & \quad \text{if } W _ {k} + Y _ {k} \geqslant t \\ 0 & \quad \text{if } W _ {k} + Y _ {k} < t \end{array} \right.
$$

Summing on all indicator functions corresponding to all particles, we then obtain the probability that the number of existing particles is equal to $m$, conditioned on the total number of particles created up to time $t$ that is $n$.

$$
Pr\{M(t) = m \mid X(t) = n\} = Pr\left\{\sum_{k=1}^{n} \mathbb{1}\{W_k + Y_k \geqslant t\} = m \mid X(t) = n\right\} = \tag{4.13}
$$

We can notice that on the rhs we have something in function of $W_{k}$ given the total number of arrivals $n$. It should remind us that given the condition on $n$, the theorem we proved last lecture states that the joint statistics of


the $W_{1},...,W_{n}$ is the same statistics we would have by dealing with ordered version of i.i.d. random variables in $(0,t)$. Moreover we can see that the expression $\{W_{k}+Y_{k}\geqslant t\}$ does not depend on the order of $W_{k}$. For example, in the case we had the following quantity $\sum_{k=1}^{n}kW_{k}$, we would notice that actually it depends on the arrival times: the later it is, the more it weights in the sum. So in this case the order would be important.
But since $\{W_{k}+Y_{k}\geqslant t\}$ is completely symmetric i.e. it is invariant on the permutation of $W$’s and we have the condition $X(t)=n$, the theorem (4.11) allows us to replace the $W_{i}$’s with the same number of i.i.d. uniform random variables $U_{i}$’s in the interval $(0,t]$, not facing any issue. We thus obtain:

$$
Pr\Big{\{}\sum_{k=1}^{n}\mathbb{1}\{W_{k}+Y_{k}\geqslant t\}=m|X(t)=n\Big{\}}=Pr\Big{\{}\sum_{k=1}^{n}\mathbb{1}\{U_{k}+Y_{k}\geqslant t\}=m\Big{\}}=
$$

Note that the rhs becomes now independent of the total number of arrivals $X(t)=n$, since we are already considering it by taking the sum. Moreover both $U_{k}$ and $Y_{k}$ are i.i.d., so each of indicator function is a binary random variable independent of all others. The sum of these $n$ indicator function is thus binomial with parameters $n$ and $p$ that is computed as:

$$
p=Pr\{U_{k}+Y_{k}\geqslant t\}=\frac{1}{t}\int_{0}^{t}Pr\{Y_{k}\geqslant t-u\}du=
$$

Where we brought $U_{k}$ to the rhs and then condition it to $U_{k}$, thus obtaining $u$. In order to remove the latter condition, we can average over the distribution of $U_{k}$’s that is uniform in the interval $(0,t)$, so we need to divide it by the length of the interval. Moreover we notice that $Pr\{Y_{k}\geqslant t-u\}$ is the complementary distribution of $G(y=t-u)$:

$$
=\frac{1}{t}\int_{0}^{t}(1-G(t-u))du=\frac{1}{t}\int_{0}^{t}[1-G(z)]dz
$$

Where in the last step we just introduced a new variable $z=t-u$.
Now that we have obtained the probability of the binomial distribution we can rewrite (4.13) as:

$$
Pr\{M(t)=m|X(t)=n\}=\frac{n!}{m!(n-m)!}p^{m}(1-p)^{n-m}
$$

Where $p$ is the one we have just computed. In order to remove the condition $X(t)=n$ we marginalize over the distribution of $X$ that we know is Poisson. Given that we have a binomial distribution of parameters $(n,p)$ and $n$ is Poisson distributed itself, if we want to find the unconditional distribution of $M(t)$ we obtain a new Poisson, where the new $\lambda$ is then scaled according to $p$ of the binomial. Mathematically:

$$
Pr\{M(t)=m\}=\sum_{n=m}^{\infty}Pr\{M(t)=m|X(t)=n\}Pr\{X(t)=n\}=
=\sum_{n=m}^{\infty}\frac{n!}{m!(n-m)!}p^{m}(1-p)^{n-m}\frac{(\lambda t)^{n}e^{-\lambda t}}{n!}=e^{-\lambda t}\frac{(\lambda pt)^{m}}{m!}\sum_{n=m}^{\infty}\frac{(1-p)^{n-m}(\lambda t)^{n-m}}{(n-m)!}
$$

Where the infinite sum is an exponential series and reduces according to:

$$
\sum_{n=m}^{\infty}\frac{(1-p)^{n-m}(\lambda t)^{n-m}}{(n-m)!}=\sum_{j=0}^{\infty}\frac{[\lambda t(1-p)]^{j}}{j!}=e^{\lambda t(1-p)}
$$

Thus obtaining the unconditional distribution that is nothing more than the $X(t)$ distribution, where we are rescaling $\lambda$ using the probability $p$ as we have already told before:

$$
Pr\{M(t)=m\}=\frac{e^{-\lambda pt}(\lambda pt)^{m}}{m!}\qquad for\ m=0,1,...
$$

But recalling how we introduced $p$, we have that at any time the number of particles existing at time $t$ has a Poisson distribution whose mean is:

$$
\lambda pt=\lambda\int_{0}^{t}[1-G(y)]dy
$$

Note that the parameter is time varying, but it is worth to see what is the behaviour of the system for long times, since it might be settled into some stationary values. As $t\to\infty$ (4.14) becomes the expected service time, since the integrand is $[1-G(y)]$, that is the tail of the distribution $G(y)$. For a generic $t$, the value of the integral depends on the details of the specific distribution $G(y)$, whereas in the long run it depends only on the mean $\mu$. This implies that in the long run two distributions will converge, despite they are different, if both have the same mean. Note also that in the case where the lifetime of a particle has a maximum finite value $t_{MAX}$, as long as we are integrating in a region ($t^{\prime}>t_{MAX}$) exceeding this upper bound value, the tail distribution $[1-G(y)]\to 0$ since $G(y)=1$. This implies that the asymptotic behaviour for the two different distributions, observed for $t\to\infty$, can be found also for $t$ exceeding the maximum lifetime of a particle, if it is finite.
Finally, we conclude by saying that in inference terminology $\int_{0}^{\infty}[1-G(y)]dy$ is the inverse of the average service rate $\mu$. In other words:

$$
\lambda pt=\lambda\int_{0}^{\infty}[1-G(y)]dy=\lambda/\mu
$$

#### 4.5.2 Shot Noise process

A Shot Noise process models electrical effects that are produced by the random arrival of electrons to an anode. In order to discuss it, let us make the following hypotheses:

- Let assume electrons arrive to an anode according to a Poisson process


$$
\{X(t);t\geqslant 0\} \lambda
$$

- An arriving  $e^{-}$  produces a current whose intensity per unit of time after arrival is given by the impulse response function  $h(x)$ .

![[Stochastic_Processes_2020_p144_img47.jpeg]]
Figure (4.11) - The figure shows different pulses generated by the arrival of electrons at different times. The current produced will be the sum of the different pulses  $I(t) = \sum_{k=1}^{X(t)} h(t - W_k)$ .

The intensity of the current  $I(t)$  will be then the superposition of the impulse response functions, that are generated by electrons arrived up to time  $t$ :

$$
I (t) = \sum_ {k = 1} ^ {X (t)} h (t - W _ {k})
$$

Note that the argument of the pulse functions are shifted according to the time of arrival of each  $e^{-}$ , i.e. by  $W_{k}$  for the  $k$ -th electron. We want now to study the statistics of this current intensity  $I(t)$ , that is compute the probability for the current to be less than a value  $x$ . In formulas:

$$
P r \{I (t) \leqslant x \} = P r \Big \{\sum_ {k = 1} ^ {X (t)} h (t - W _ {k}) \leqslant x \Big \} =
$$

We can indeed condition on the total number  $n$  of arrivals up to time  $t$ , and consequently remove the same condition by marginalizing over the probabilities of  $X(t) = n$  for  $n = 0,1,2\dots$ :

$$
= \sum_ {n = 0} ^ {\infty} P r \Big \{\sum_ {k = 1} ^ {X (t)} h (t - W _ {k}) \leqslant x | X (t) = n \Big \} P r \{X (t) = n \} =
$$

Since we are conditioning on the number of terms, the random sum becomes a fixed sum:

$$
= \sum_ {n = 0} ^ {\infty} P r \Big \{\sum_ {k = 1} ^ {n} h (t - W _ {k}) \leqslant x | X (t) = n \Big \} P r \{X (t) = n \} =
$$

Now we can invoke the theorem (4.11): we are dealing with something that depends on the joint statistics of  $W_{k}$ 's given their number  $n$ . In addition,


$W_{k}$’s have the same distribution of the ordered version of $n$ i.i.d. uniform random variables in the same interval, so $\sum_{k=1}^{n}h(t-W_{k})\leqslant x$ is invariant w.r.t. permutations of the $W$’s: all response functions are in fact equal for all arrivals and the order in which we sum them is not important, thus being symmetric. These are the reasons for which we can replace $W_{k}$’s with their corresponding $U_{k}$’s, obtaining:

$$
=\sum_{n=0}^{\infty}Pr\Big{\{}\sum_{k=1}^{n}h(t-U_{k})\leqslant x\Big{\}}Pr\{X(t)=n\}=
$$

Where we can drop the condition on the number of total arrivals $n$, being the $\sum_{k}$ independent of it:

$$
=\sum_{n=0}^{\infty}Pr\Big{\{}\sum_{k=1}^{n}h(U_{k})\leqslant x\Big{\}}Pr\{X(t)=n\}=
$$

that are equivalent since $U_{k}$ and $t-U_{k}$ share the same distribution. Recalling that at the beginning we introduced some factors in order to average over the all possible $n$, we want now to make a step back and rewrite the finite sum as a *random* sum. And finally:

$$
Pr\{I(t)\leqslant x\}=P\Big{\{}\sum_{k=1}^{\infty}h(U_{k})\leqslant x\Big{\}}
$$

We know actually how to find the statistics of a random sum whose all terms are i.i.d.: being the $U_{k}$’s i.i.d., so the $h(U_{k})$’s will be. In addition, $U_{k}$’s are also independent of their number $X(t)$.

We have already seen this kind of sum in example (1), so we can compute the complete statistics by using either the generating or characteristic functions. An other way to do this is introducing the two first moments. We recall the expected value of a random sum is the product of the expected value of the number of terms (Poisson distributed), times the common expected value for each term (uniformly distributed). In formulas:

$$
\mathbb{E}[I(t)]=\mathbb{E}[X(t)]\mathbb{E}[h(U_{k})]=\lambda t\frac{1}{t}\int_{0}^{t}h(u)du=\lambda\int_{0}^{t}h(u)du
$$

As for the variance, we recall that the variance is the sum of the product of expectation of the number terms times the variance of the terms, plus the variance of number of terms times the square of average of terms. In formulas:

$$
Var(I(t))=\lambda t\ Var(h(U_{k}))+\lambda t\mathbb{E}[h(U_{k})]^{2}=\lambda t\Big{(}Var(h(U_{k}))+\mathbb{E}[(h(U_{k}))]^{2}\Big{)}=
=\lambda t\mathbb{E}[(h(U_{k}))^{2}]=\lambda t\frac{1}{t}\int_{0}^{t}h^{2}(u)du=\lambda\int_{0}^{t}h^{2}(u)du
$$


Where we used the definition of  $Var(X)$  by reverting it and obtaining  $\mathbb{E}[X^2] = Var(X) + \mathbb{E}[X]^2$ .

Note as we let  $t \to \infty$ , thus integrating for times longer than the duration of the pulse, then the integral will be the area of under each pulse in the image 4.11. So, in the limit for large  $t$ , the mean  $\mathbb{E}[I(t)]$  and  $Var(I(t))$  will be no longer dependent on the shape of the pulse, since only the area  $\int_0^t h(u)du$  will be important to us. This implies that even for different shaped pulses, as long as they share the same value of the area subtended by the function  $h(t)$ , they will on the average produce the same current.

# 4.6 Binomial theorem

We recall a theorem that we have already seen before at page 138:

Theorem 4.6.1. Let  $[X(t)]$  be a Poisson process of rate  $\lambda >0$ . Then for  $0 < u < t$  and  $0\leqslant k\leqslant n$ ,

$$
P r \{X (u) = k | X (t) = n \} = \frac {n !}{k ! (n - k) !} \left(\frac {u}{t}\right) ^ {k} \left(1 - \frac {u}{t}\right) ^ {n - k}
$$

We have already proved this theorem by using (4.5.3), but there is also an other way that is often requested during written tests and it is worth to see and understand better. We will now see how to prove this theorem directly.

Proof. Straightforward computations give:

$$
P r \{X (u) = k | X (t) = n \} =
= \frac {P r \{X (u) = k \text{ and } X (t) = n \}}{P r \{X (t) = n \}} = \frac {P r \{X (u) = k \text{ and } X (t) - X (u) = n - k \}}{P r \{X (t) = n \}}
$$

Where we simply used the definition of conditional event. The situation is described by the figure:

![[Stochastic_Processes_2020_p146_img48.jpeg]]
Figure (4.12) - Note as the two intervals  $(0, u)$  and  $(u, t)$  are disjoint, so increments are independent of each other. Whereas  $(0, u)$  and  $(0, t - u)$  overlap, thus not being independent despite they share the same statistics.

The numerator of the fraction above expresses the joint probability of having  $k$  events in the shorter interval  $(0, u)$  and  $n$  overall in interval  $(0, t)$ . This second


event can be written as having $n-k$ arrivals in the shorter interval $(u,t)$. Note that the two intervals $(0,u)$ and $(u,t)$ are disjoint, and so the two corresponding events are independent random variables: this is the first property we use in this passage. Secondly, we must say that the increment in the interval $(u,t)$ is the same as the increment in interval $(0,t-u)$: it is based on the Poisson property that the increments are stationary and so depend only on the length of the interval. For the last property we could have replaced $X(t)-X(u)$ with $X(t-u)$ making no errors since they both share the same statistics, but ONLY AFTER an intermediate step where we have factorized the two probabilities: the two increments $X(u)$ and $X(t-u)$ refer to the two superimposing intervals $(0,u)$ and $(0,t-u)$, thus not being independent of each other.

This allows us to write it as the product of the two individual probabilities, and we know that all of them are Poisson:

$$
=\frac{\{e^{-\lambda u}(\lambda u)^{k}/k!\}\{e^{-\lambda(t-u)}[\lambda(t-u)]^{n-k}/(n-k)!\}}{e^{-\lambda t}(\lambda t)^{n}/n!}=
$$

And simplifying:

$$
=\frac{n!}{k!(n-k)!}\frac{u^{k}(t-u)^{n-k}}{t^{n}}
$$

That is an other way to write the expression pointed out in the theorem, so concluding our proof. $\Box$

Let us consider the dual situation of the theorem we have just introduced:


(dual version)

$$
Pr\{X(s)=k|X(t)=n\}\qquad 0\leqslant n\leqslant k,\quad 0<t<s
$$

Here we want to compute the probability of having $k$ arrivals in the largest interval $(0,s)$, conditioned on the fact that we have already had $n$ arrivals in the interval $(0,t)$. Obviously this is equivalent to have $k-n$ arrivals in the interval $(t,s)$ as it is shown in the picture, thus having two probabilities referring to two different disjoint intervals. By using the definition of conditioned probability:

$$
\frac{Pr\{X(s)=k\ ,\ X(t)=n\}}{Pr\{X(t)=n\}}=
\frac{Pr\{X(t)=n\ ,\ X(s)-X(t)=k-n\}}{Pr\{X(t)=n\}}=
$$
But since the two joint probabilities refer to two disjoint intervals, they are independent of each other, so factorizable.

$$
=\frac{Pr\{X(t)=n\ \}Pr\{\ X(s)-X(t)=k-n\}}{Pr\{X(t)=n\}}=Pr\{X(s-t)=k-n\}=
$$


Where in the last passage we used the fact that the two increments are stationary, so $X(s)-X(t)$ and $X(s-t)$ actually have the same statistics. Recall that this must be done ONLY AFTER we have factorized the two terms as shown above. In fact, $X(t)$ and $X(s)-X(t)$ are independent since they refer to disjoint intervals, whereas $X(t)$ and $X(t-s)$ refer to overlapping intervals thus not being independent even if they share the same statistics: skipping the intermediate passage would be wrong. We finally recognize the last probability as a Poisson process:

$$
Pr\{X(s-t)=k-n\}=\frac{e^{-\lambda(s-t)}(\lambda(s-t))^{k-n}}{(k-n)!}
$$

###### Exercise 4.6.1 (Written test - June 27, 2016)

Consider two independent Poisson processes $X_{1}(t)$ and $X_{2}(t)$, where $X_{i}(t)$ is the number of arrivals for process $i$ during $[0,t]$. The average number of arrivals per unit time of the two processes is $\lambda_{1}=0.5$ and $\lambda_{2}=1$ respectively.

1. Compute $P[X_{1}(2)=1|X_{1}(3)=2]$ and $P[X_{1}(3)=2|X_{1}(2)=1]$
2. Compute $P[X_{1}(1)=1|X_{1}(2)+X_{2}(2)=3]$ and $P[X_{1}(2)+X_{2}(2)=3|X_{1}(1)=1]$
3. Compute $P[X_{1}(2)+X_{2}(2)=3|X_{1}(3)=0]$ and $P[X_{1}(2)+X_{2}(2)=3|X_{1}(3)=1]$

Solution.

1) The first probability we need to compute refers to the same process, but different intervals. We know, from the previous theorem (4.6.1) that, given the number of arrivals in the large interval, the probability of having a certain number of events in the smaller one is binomially distributed with parameters $(n=2,p=2/3)$, where $p$ is given by the ratio of the length of the two intervals. So the computations return:

$$
P[X_{1}(2)=1|X_{1}(3)=2]={2\choose 1}\left({2\over 3}\right)^{1}\left({1\over 3}\right)^{2-1}={4\over 9}\simeq 0.44
$$

Now we do the opposite: we want to know, given the number of arrivals in the small interval that is $X_{1}(2)=1$, what is the probability of having a certain number of events $X_{1}(3)=2$ in the large one. In other words, we want to compute the probability that $X_{1}(3)-X_{1}(2)=3-2=1$. In formulas:

$$
P[X_{1}(3)=2|X_{1}(2)=1] =P[X_{1}(3)-X_{1}(2)=1]=
=P[X_{1}(1)=1]=0.5e^{-0.5}\simeq 0.3
$$

2) The second question involves $X_{1}$ given the condition of the sum of $X_{1}+X_{2}$. This should reminds us of the theorem (4.5.5), where recalling the picture


(4.9) we can associate the bigger rectangle with the event that gives us the condition where the two processes are combined in the large interval $(0,t)$: its area will indeed be the parameter $(\lambda_{1}+\lambda_{2})t$ of the corresponding Poisson event. Whereas the small rectangle is associated to the probability we are request to compute. We will have then a binomial with parameters $(n,p)$, where $n$ is the total number of arrivals, and $p$ is the ratio between the two areas. Let us compute the probability:

$$
P[X_{1}(1)=1|X(2)=3]=\binom{3}{1}\binom{1}{6}^{1}\binom{5}{6}^{3-1}=\frac{25}{72}\simeq 0.347
$$

where we introduced as a new variable $X(t)=X_{1}(t)+X_{2}(t)$.

Now we want to switch the roles: given that the area of the small rectangle, we want to find the probability that the large one will have a certain area. This is, obviously, equivalent to constraint the value of the difference between the large and the small surfaces. What happens in the difference is itself a Poisson variable with parameter that is the area of the region, i.e. the sum of the two rectangles ($[\lambda_{1},\lambda_{1}+\lambda_{2}]\times[0,2]\cup[0,\lambda_{1}]\times[1,2]$) that is $2.5$. In formulas:

$$
P[X(2)=3|X_{1}(1)=1]=P[X_{2}(2)+X_{1}(2)-X_{1}(1)=2]=\frac{(2.5)^{2}e^{-2.5}}{2}\simeq 0.2565
$$

#### 3

[Discussed in lecture on April, 28th] We shall notice that we are in a different situation from the previous points. In the first point we had that the conditional event completely contained the event of which we were asked to compute the probability, making it to be a binomial process. Whereas in the second point the situation was the dual one: the event whose we needed to compute the probability was indeed containing the conditional event, making the "remaining" area follow a Poisson process.

Now the situation is slightly different since neither contains the other. The first event we need to compute the probability is the sum in the interval $(0,2)$, while the conditional event refers to a single process in the interval $(0,3)$. In this case clearly the two different intervals are partially overlapping, so we can not use the previously results.

Note that the conditional event requests us to not have $any$ arrivals corresponding to the process with rate $\lambda_{1}$ in the whole interval $(0,3)$. The probability of having a total number $k$ of arrivals will be indeed given totally by the process $X_{2}$ in the interval $(0,2)$. Arrivals in that interval will be Poisson with parameter $\lambda_{2}$. And so the probability requested will be:

$$
P[X_{1}(2)+X_{2}(2)=3|X_{1}(3)=0]=P[X_{2}(2)=3]=\frac{2^{3}e^{-2}}{3!}=\frac{4}{9}e^{-2}\simeq 0.06
$$

As for the second point, we know that the conditional event points out that in the rectangle where before there was not any arrival, now we have one arrival. This implies that we must have the remaining arrivals all given by process $X_{2}$.

But one should notice one more thing: the single arrival of the conditional event related to $X_{1}$ could be either occur in two disjoint intervals that are $(0,2)$ and $(2,3)$. In the first case, $X_{2}$ would give us the remaining $2$ arrivals,


while in the second one  $X_{2}$  should give us all 3 of them. In brief, according to where the single arrival in  $X_{1}$  comes, we need to wait the complementary arrivals for the other process  $X_{2}$  that will complete the probability of the event we are looking for. These complementary probabilities will then need to be linearly combined using as weights the probabilities that the two events in the condition can occur. We can indeed use the law of total probability and so condition over to an event referring to  $X_{1}(2)$ , and then take the average. Being  $X_{1}(3) = 1$ ,  $X_{1}(2) = \{1,0\}$  can assume only two values. So writing in formulas what we have just stated:

$$
P \left[ X _ {1} (2) + X _ {2} (2) = 3 \mid X _ {1} (3) = 1 \right] =
\sum_ {i = 0} ^ {1} P [ X _ {1} (2) + X _ {2} (2) = 3 \lfloor \underline {{X}} _ {1} (3) = \overline {{1}}, X _ {1} (2) = i ] P [ X _ {1} (2) = i | X _ {1} (3) = 1 ] =
$$

Where we can neglect the  $X_{1}(3) = 1$  because it is not necessary any more once we have introduced the condition on  $X_{1}(2)$ . We obtain something that we can compute:

$$
= \sum_ {i = 0} ^ {1} P [ X _ {1} (2) + X _ {2} (2) = 3 | X _ {1} (2) = i ] P [ X _ {1} (2) = i | X _ {1} (3) = 1 ] =
$$

The first term is indeed the probability for  $X_{2}(2) = 3 - i$  where  $i = 0,1$ , whereas the second is clearly binomial. Solving the sum for the different  $i$ 's:

$$
= \overbrace {P [ X _ {2} (2) = 3 ] \cdot \frac {1}{3}} ^ {i = 0} + \overbrace {P [ X _ {2} (2) = 2 ] \cdot \frac {2}{3}} ^ {i = 1}
$$

Note as every term is multiplied by the ratio of the lengths of the intervals, that is the probability for a random variable in  $[0,3]$  to fall either in  $[0,2]$  or in  $[1,3]$ .

$$
= \frac {2 ^ {3} e ^ {- 2}}{3 !} \cdot \frac {1}{3} + \frac {2 ^ {2} e ^ {- 2}}{2 !} \cdot \frac {2}{3} = \frac {4}{9} e ^ {- 2} + \frac {4}{3} e ^ {- 2} = \frac {1 6}{9} e ^ {- 2} \simeq 0. 2 4
$$

![[Stochastic_Processes_2020_p150_img49.jpeg]]
Figure (4.13) - Graph for the point  $c$ ) of the exercise 4.6.1



A Markov chain has the transition probability:

|   | 0 | 1 | 2 | 3 | 4 | 5  |
| --- | --- | --- | --- | --- | --- | --- |
|  0 | α1 | α2 | α3 | α4 | α5 | α6  |
|  1 | 1 | 0 | 0 | 0 | 0 | 0  |
|  2 | 0 | 1 | 0 | 0 | 0 | 0  |
|  3 | 0 | 0 | 1 | 0 | 0 | 0  |
|  4 | 0 | 0 | 0 | 1 | 0 | 0  |
|  5 | 0 | 0 | 0 | 0 | 1 | 0  |

where  $\alpha_{i}\geqslant 0$ ,  $i = 1,\ldots ,6$  and  $\sum_{i = 1}^{6}\alpha_{i} = 1$ .

- Determine the limiting probability of being in state 0.

![[Stochastic_Processes_2020_p151_img50.jpeg]]
Figure (4.14) - Transition matrix of exercise 4.6.2

Solution. For a process as depicted in figure 4.14 we can write the following stationary equations, where we have obtained the row vector  $\vec{\pi}$  by multiplying itself for each column of the matrix  $\mathbf{P}$ :

|  π0= π0α1+π1  |
| --- |
|  π1= π0α2+π2  |
|  π2= π0α3+π3  |
|  π3= π0α4+π4  |
|  π4= π0α5+π5  |
|  π5= π0α6  |

We can then start rewriting the system starting from the last row, and then replace recursively the  $\pi_i$  with the  $\pi_{i + 1}$  computed in the row below, thus obtaining the following system:

|  π0=(α1+α2+α3+α4+α5+α6)π0  |
| --- |
|  π1=(α2+α3+α4+α5+α6)π0  |
|  π2=(α3+α4+α5+α6)π0  |
|  π3=(α4+α5+α6)π0  |
|  π4=(α5+α6)π0  |
|  π5=α6π0  |


Where we know that  $\sum_{i=1}^{6} \alpha_i = 1$ , so for each  $i$ -th row of the system we note that the limiting probability becomes  $1 - \alpha_i$ , that is the probability of being at least in the  $i$ -th state. We can now proceed to solve the system and find the stationary solutions, that are all determined except for the common factor  $\pi_0$  which will be computed by applying the normalization condition  $\sum_{i=0}^{5} \pi_i = \left( \sum_{k=1}^{6} k \alpha_k \right) \pi_0 = 1$ , that is the mean of the distribution of the  $\alpha$ 's. Now we want to understand what the distribution does: as shown in the image 4.14 starting from the state 0, it selects a generic  $i$ -th state and then deterministically goes back to zero one step per time, so taking  $i + 1$  steps to go back to the starting point. For example, if from 0 we go to state 4 with probability  $\alpha_5$ , then it will take 5 time steps to come back to 0. If we go to state 2 with probability  $\alpha_3$ , then we will be back in 3 time steps, and so on. Generalizing: given we start from 0, with probability  $\alpha_k$  my return time in 0 will be  $k$ .

Note as the formula  $\left(\sum_{k=1}^{6} k\alpha_{k}\right)\pi_{0} = 1$  is the average return time to 0, that corresponds to the inverse of the probability of being in that state in the long run, as we would expect from theory. Finally we conclude that:

$$
\pi_ {0} = \frac {1}{\sum_ {i = 1} ^ {6} k a _ {k}} = \frac {1}{\text {mean of} \alpha \text {distribution}}
$$


A similar exercise to the previous one is the following: let  $\{\alpha_{i}:i = 1,2,\ldots \}$  be a probability distribution, and consider the Markov chain whose transition probability matrix is:

|   | 0 | 1 | 2 | 3 | 4 | 5 | ...  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  0 | α1 | α2 | α3 | α4 | α5 | α6 | ...  |
|  1 | 1 | 0 | 0 | 0 | 0 | 0 | ...  |
|  2 | 0 | 1 | 0 | 0 | 0 | 0 | ...  |
|  3 | 0 | 0 | 1 | 0 | 0 | 0 | ...  |
|  4 | 0 | 0 | 0 | 1 | 0 | 0 | ...  |
|  5 | 0 | 0 | 0 | 0 | 1 | 0 | ...  |
|  : | : | : | : | : | : | : | ..  |

Note that the difference with the previous one is that we are now dealing with an infinite Markov chain.

- What condition on the probability distribution  $\{\alpha_{i} : i = 1,2,\ldots\}$  is necessary and sufficient in order that a limiting distribution exist, and what is this limiting distribution? Assume  $\alpha_{1} > 0$  and  $\alpha_{2} > 0$  so that the chain is aperiodic.

Solution. The solution is similar to the previous problem. Recall that the row vector  $\vec{\pi}$  is obtained by multiplying itself for each column of the matrix  $\mathbf{P}$ .

The first component becomes  $\pi_0 = \alpha_1\pi_0 + \pi_1$ . Thus solving for  $\pi_1 = (1 -$


$\alpha_{1})\pi_{0}$.
The second equation will become: $\pi_{1}=\alpha_{2}\pi_{0}+\pi_{2}$ and replacing with the value we have just found for $\pi_{1}$ we can write: $\pi_{2}=(1-\alpha_{1}-\alpha_{2})\pi_{0}$. Iteratively we find that for a generic $\pi_{n}$ the limiting distribution will be:

$$
\pi_{n}=\left(\sum_{k=n+1}^{\infty}\alpha_{k}\right)\pi_{0}
$$

Here we recall that $\sum_{n=0}^{\infty}\pi_{n}=1$, and by imposing this condition by summing over all $\pi$’s and finally solving the equation for $\pi_{0}$ we obtain:

$$
\pi_{0}=\left(\sum_{n=0}^{\infty}\sum_{k=n+1}^{\infty}\alpha_{k}\right)^{-1}=\left(\sum_{n=0}^{\infty}P[X>n]\right)^{-1}
$$

Obviously the double sum $\sum_{n=0}^{\infty}\sum_{k=n+1}^{\infty}\alpha_{k}$ must converge to a finite value, otherwise the $\alpha_{k}$’s distribution would not exist and we could have not solved for $\pi_{0}$. In that case the $\vec{\pi}$ would be made of all $0$’s thus not being an acceptable solution for the system, that is why the double sum must converge. We recall moreover the meaning of $\alpha_{k}$, that is the probability $P[x=k]$. When we sum $\sum_{k=n+1}^{\infty}$ we are then considering the probability $P[x>n]$. On the other hand, the sum $\sum_{n=0}^{\infty}P[x>n]$ is the average of the distribution, so once again we find that $\pi_{0}$ is the inverse of the average distribution of the return times in $0$. This is indeed valid only because when we pick a value $n$ for the distribution $\alpha_{n}$, then the first return time to the starting point will be exactly of $n$ time steps.

###### Exercise 4.6.4 (Chap IV - Prob. 1.4):

A finite state regular Markov chain has transition probability matrix $\mathbf{P}=|P_{ij}|$ and limiting distribution $\pi=|\pi_{i}|$. In the long run, what fraction of the transitions are from a prescribed state $k$ to a prescribed state $m$?

Solution. First we should recall that transition probabilities are conditional probabilities, indeed we want to compute the probability to come to a certain state $m$ given we started in an other one $k$. For any transition, it must hold that first we must find ourselves in state $k$, and then from state $k$ we must go to state $m$. The problem thus asks us to compute:

$$
\pi_{k}P_{km}=\lim_{n\rightarrow\infty}P[X_{n}=k\ ,\ X_{n+1}=m]
$$

We could even have added the condition on the initial state, but since the chain is regular we know from theory that it is not important where we start, so we can neglect it.


Determine the following limits in terms of the transition probability matrix $\mathbf{P} = |P_{ij}|$ and limiting distribution $\pi = |\pi_i|$ of a finite state regular Markov chain $\{X_{n}\}$:

1. $\lim_{n\to \infty}P[X_{n + 1} = j|X_0 = i]$
2. $\lim_{n\to \infty}P[X_n = k, X_{n + 1} = j|X_0 = i]$
3. $\lim_{n\to \infty}P[X_{n - 1} = k, X_n = j|X_0 = i]$

Solution. 1) Here the precise step, being it either $n$ or $n + 1$ or $n - 1$, is not so important because we are considering the limit as $\lim_{n\to \infty}$. Moreover, since the chain is regular, this limit will be independent of the starting condition, so we basically need to compute:

$$
\lim _ {n \to \infty} P [ X _ {n + 1} = j | X _ {0} = i ] = \pi_ {j}
$$

2) Here we neglect as well the initial condition since the chain is regular. There is in addition a joint probability referring to two consecutive states: we are requested to be in state $k$ in the long run, that happens with probability $\pi_{k}$, and starting from there going to state $j$ according to the transition probability $P_{kj}$. So we need to compute:

$$
\lim _ {n \to \infty} P [ X _ {n + 1} = j | X _ {n} = k, X _ {0} = i ] P [ X _ {n} = k | X _ {0} = i ]
$$

Where we first used the definition of conditional probability, and noting that we can drop the initial condition $X_0 = i$ in the first factor since it is older than $X_n = k$. We have already found $\lim_{n\to \infty}P[X_n = k|X_0 = i] = \lim_{n\to \infty}P[X_{n + 1} = k|X_0 = i] = \pi_k$. Finally, knowing that the first term is the one step transition probability we can write:

$$
\lim _ {n \to \infty} P [ X _ {n} = k, X _ {n + 1} = j | X _ {0} = i ] = \pi_ {k} P _ {k j}
$$

3) The third one, in the limit as $n \to \infty$ is the time shifted version of the probability we had to find in the point 2), namely:

$$
\lim _ {n \to \infty} P [ X _ {n} = k, X _ {n + 1} = j | X _ {0} = i ] = \lim _ {n \to \infty} P [ X _ {n - 1} = k, X _ {n} = j | X _ {0} = i ] = \pi_ {k} P _ {k j}
$$


A Markov chain has the transition probability matrix:

$$
\mathbf{P}=\begin{array}[]{c c c c}0&1&2\\
0&\left|\begin{array}[]{c c c}0.4&0.4&0.2\\
1&0.6&0.2&0.2\\
2&0.4&0.2&0.4\end{array}\right|\\
\end{array}
$$

After a long period of time, you observe the chain and see that it is in state 1. What is the conditional probability that the previous state was state 2? That is, find:

$$
\lim_{n\to\infty}P[X_{n-1}=2|X_{n}=1]
$$

Solution. Note that this problem is slightly different from the ones we have already solved: we are now looking at the chain backward. We write the definition of conditional probability:

$$
P[X_{n-1}=2|X_{n}=1]=\frac{P[X_{n-1}=2\ ,\ X_{n}=1]}{P[X_{n}=1]}=
\frac{P[X_{n}=1|X_{n-1}=2]P[X_{n-1}=2]}{P[X_{n}=1]}=P_{21}\frac{P[X_{n-1}=2]}{P[X_{n}=1]}=
$$

Where we wrote the joint probability in the numerator as a conditional one. We recognized that the first term is the one step transition probability, namely $P_{21}$. Note that in the limit, as $n\to\infty$, both the numerator and denominator converge respectively to $\pi_{2}$ and $\pi_{1}$ since the Markov chain is regular and it does not depend on the initial state.

$$
=\lim_{n\to\infty}P_{21}\frac{\pi_{2}}{\pi_{1}}=\frac{6}{35}\simeq 0.1714
$$

Where $P_{21}=0.2$ and $\pi_{1}$ and $\pi_{2}$ must be computed by solving the stationary equations.


An individual either drives his car or walks in going from his home to his office in the morning, and from his office to his home in the afternoon. He uses the following strategy: if it is raining in the morning, then he drives the car, provided it is at home to be taken. Similarly, if it is raining in the afternoon and his car is at the office, them he drives the car home. He walks on any morning or afternoon that it is not raining or the car is not where he is. Assume that, independent of the past, it rains during successive mornings and afternoon with constant probability $p$. In the long run, on what fraction of *days* does our man walk in the rain? What if he owns two cars?


Solution. First let us consider the time in "trips" unit, and not as we would normally do in days: every day there will be two trips. Let us define the following states:

- $X_{n}=1$ if the car is available, i.e. at the same place of our man
- $X_{n}=0$ otherwise

Let us now think about the transition matrix of the problem. For the first row we reason as it follows: if the guy does not have the car, so we are in state $X_{n}=0$, in the next trip he will not be able to do anything but walk. Note that when he walks, he will walk to the place where the car actually is, so necessarily $X_{n+1}=1$.

On the other hand, if he has the car, so being in $X_{n}=1$, at the place where he is and he walks back he will have to leave the car, so the at the next trip he will not have the car, thus being $X_{n+1}=0$. But we know that he drives only when it is raining, so $P_{10}=1-p$, namely the probability that it does not rain. Whereas, if it rains with probability $p$, he will drive thus having the car available for the following trip, thus remaining in $X_{n+1}=1$. The transition probability matrix takes the form:

It is indeed a Markov chain: whether the car will be next step depends on where it is now, and on whether it rains with probability $p$. These two present notions will let us to fully characterize the next step, without any knowledge about previous states required.

Now we want to find the long run probability $\pi_{0}$ and $\pi_{1}$ to characterize the behaviour of the chain for long times. Recall now that they are proportional to the incoming probability, so $1-p$ and $1$, and normalized by the sum of the twos. Namely:

$$
\pi_{0}=\frac{1-p}{2-p}\qquad\pi_{1}=\frac{1}{2-p}
$$

We want now to find the probability for a given day that the guy walks in the rain. In order to do that, let us condition on what happens in the morning, whether he has the car or not:

$$
\pi_{0}p+\pi_{1}(1-p)p=\frac{2p(1-p)}{2-p}
$$


Where the first term corresponds to the event that he does not have the car, which happens with probability $\pi_{0}$ in the long run, and then he walks to the office where his car was left the previous day. In this trip he may get wet, according to the fact that is raining or not with probability $p$. While, for the second term, if he does have the car in the morning which occurs with probability $\pi_{1}$, he will not get wet if it is already raining: he would drive to the office and then have the car for the rest of the day. Whereas, if in the morning it is not raining with probability $1-p$, he will walk to the office leaving the car at home. In the case that in the afternoon rains with probability $p$, he will not have the car and thus get wet walking.

In the case where the man has two cars things are slightly different. We define as $X_{n}$ the number of the car where our man is, so if we are in state $X_{n}=0$ then our man will have no cars at his disposal, while for $X_{n}=2$ he will have both of them. The transition probability matrix will be:

$$
\mathbf{P}=\begin{array}[]{c c c c}&0&&1&2\\
0&&0&0&1\\
1&&0&1-p&p\\
2&&1-p&p&0\end{array}
$$

Where, as before, the last row describes the situation where the guy starts and has no cars $X_{n}=0$: he will surely go in the next step where there are both of them, so $X_{n+1}=2$ with probability $1$. Then, on the following trip i.e. starting with one car $X_{n}=1$, it will not be allowed for him to go state $0$: if it will be raining then he will drive thus having two cars $X_{n+1}=2$ with probability $p$, if not he will leave the car where it is and remain in state $X_{n+1}=1$ with probability $1-p$. The last case is where he starts having two cars $X_{n}=2$, in the case in rains with probability $p$ he will be able to drive only one car thus having one car for the following trip $X_{n+1}=1$. Otherwise, cars will remain as they actually are, and our man will have no cars at his disposal $X_{n+1}=0$ with probability $1-p$. Obviously, the third possibility is impossible, he can either leave both cars to the place he leaves, or drive either one of them.

Applying a similar reasoning as before we can find the stationary probability for the three different states, that are respectively:

$$
\pi_{0}=\frac{1-p}{3-p}\qquad\pi_{1}=\frac{1}{3-p}\qquad\pi_{2}=\frac{1}{3-p}
$$

The possibility that, in the long run, the guy gets wet will be then:

$$
\pi_{0}p+\pi_{2}(1-p)p=\frac{2p(1-p)}{3-p}
$$

# 4.7 P.A.S.T.A. property

When studying the MC for  $M / G / 1$  there was an issue relating to the continuous time process counting the number of users at time  $t$  present in the system, that was not Markovian. This was due to the fact that service times were not memoryless for the  $M / G / 1$  queue, as well as the interarrival times were not for the  $G / M / 1$  one. In order to tackle this issue we needed either to explicitly include the number of the users in the service, or to sample the evolution of the processes at some specific times when this information was deterministically given. Now an other issue arises: how can we be sure that times sampled according to some specific rules, no matter they were upon arrivals or departures, are representative of the long run behaviour of our process? We want then to know whether we are introducing some sort of bias while sampling istances according to a distribution, and if and how this might affect the statistics of our process in the long run. We will face this problem in the case of Poisson processes.

Let us define the two probabilities  $p_n(t)$  and  $a_n(t)$ :

$$
p _ {n} (t) = P \{N (t) = n \}
a_{n}(t) = P\{N(t) = n \mid \text{an arrival occurred just after time } t\}
$$

where the first one denotes the probability that up to time  $t$ , the number of users in the system  $N(t) = n$  is exactly equal to  $n$ . Note that this would be the distribution seen by an external observer that wants to know the probability for the system to be in a given state at time  $t$ . Whereas the second one is exactly the same one, but conditioned on the event that one arrival has occurred just after the time  $t$ . It is indeed the distribution, given the state, of the probability seen by an arriving user. We want then to know whether these two probabilities are the same one, by checking if our discretized time sampling may have introduced some bias. We will now see that under some assumptions they will indeed be the same one.

If the arrivals are Poisson, then the two probabilities will be the same one under very general conditions regardless of the distribution of the service times. Note that the only requirement needed is that the future arrivals must be independent of the current number of users in the system.

![[Stochastic_Processes_2020_p158_img51.jpeg]]
Figure (4.16) - The number of users in the system  $N(t)$  depends both on the number of departures and arrivals up to time  $t$ , moreover we condition this on the fact that we have an arrival immediately after time  $t$ .

$N(t)$  depends both on arrivals and departures up to time  $t$ . We are requested that the arrival occurring at time  $t^+$  is independent of  $\mathbf{N}(\mathbf{t})$ , and consequently of both arrivals and departure times.

The first requirement, namely the independence of arrival times, is guaranteed


by the fact that arrivals are Poisson. Hence increments are independent for disjoint time intervals.

On the other hand, departure times are the sum of arrival and service times, and so they do depend on them. Consequently, service times need to be independent of future arrivals. Note that this is quite reasonable: in a system the distribution of serving times should not be dependent on the distribution of future arrivals. Having noted so, we can now prove that the two statistics are the same one.

Recall that we introduced the requirement that arrivals must be independent of the number of users in the system at any time  $t$ , so the two events stated in the definition of  $a_{n}(t)$  are independent and their probability can be rewritten accordingly as their product:

$$
a _ {n} (t) = P \{N (t) = n \} P \{\text {a n a r r i v a l o c c u r r e d j u s t a f t e r t i m e} t \}
$$

Then, in the limit:

$$
\lim _ {t \to \infty} p _ {n} (t) = \lim _ {t \to \infty} a _ {n} (t)
$$

We can conclude that in a system where arrivals are Poisson, the distribution of states of the process seen by an external observer is the same one experienced by a user entering the system in the long run. This means that the sampling induced by arriving users according to Poisson process, will not bias the statistics.

We refer to this property by using the following acronym: P.A.S.T.A. that stands for Poisson Arrivals See Time Averages. Time averages are the statistics seen by an external observer, and in the long run we know that Poisson arrivals will see the same statistics, thus concluding there is no bias.

This result however is not obvious, in order to show it, we will deal with the following examples where we drop either one of the previous hypotheses.

## Non Poisson arrivals

Let us consider an arrival process that is not Poisson, but still interarrival times are independent of each other and uniformly distributed in the interval [2, 4] seconds. In addition let us set the condition that the service time must be exactly of 1 second.

![[Stochastic_Processes_2020_p159_img52.jpeg]]
Figure (4.17) – Typical evolution of the process: interarrival times are uniformly distributed according to  $U[2,4]s$ , while service time is fixed to 1s.

Note that the lower bound for the interarrival times interval is 2s, whereas the service time is less and it is 1s. Each user that arrives will thus find the system


empty, because the previous customer will have already been served before the following one comes. The statistics seen by an arriving customer will be then:

$$
a_{0}=P[N(t)=0\mid\text{arrival has just occurred }]=1
a_{i}=0\qquad i>0
$$

At any time $t$, given that a customer has just arrived, the latter will find the system in state $0$, i.e. the state with no users. Note that as this statistics is valid for any $t$, it will hold consequently for $t\to\infty$, because the system can not be found in any other state but $0$.
On the other hand, an external observer will see the system occupied for exactly $1s$ and empty for a period of time that distributes uniformly according to $U[1,3]$.
On average, he will see the system empty for $2$s. In the long run we expect a single user being served for $1$s every $3$s on average, thus leading to:

$$
p_{0}=\lim_{t\to\infty}P[N(t)=0]=2/3
p_{1}=\lim_{t\to\infty}P[N(t)=1]=1/3
p_{i}=0\qquad i>1
$$

Clearly, the two statistics seen by an arriving and an external users are different:

$$
a_{0}\neq p_{0}\qquad a_{1}\neq p_{1}
$$

as we expected from the P.A.S.T.A. property, not being the arrivals Poisson.

#### 3.3.1 Arrival - Service times not independent

An other example is where arrivals are Poisson, but service times of past users and future arrivals times are indeed correlated. Let us suppose now that the transmission time of the $n^{th}$ packet is equal to one half of the interarrival time between packets $n$ and $n+1$. Our process is the following:

Figure (4.18) – Arrival and service times are here correlated: service time will be indeed half of the next interarrival time.

Note that we have the guarantee that the system will be empty when a new user comes into the system: interarrival times between two consecutive customers are in fact twice as long as the service times of the user that has last arrived. The statistics seen by an arriving user will be:

$$
a_{0}=1
p_{0}=p_{1}=1/2
$$

In the long run the system will be empty half of the time, while it will be occupied by a single user the other half: we can see clearly that the two quantities are not independent of each other. In the limit:

$$
p_{0}=p_{1}=1/2
$$

It is clear that the two statistics are different: this is because, despite the fact that we have Poisson arrivals, the independence between the service time for users that have already arrived and the future interarrival times does not hold.

Using last two examples we have just showed that both conditions are necessary in order to make Poisson arrivals see time averages.

#### M/G/1 queue example

We have said before that for the $M/G/1$ queue it was requested to sample at specific times, that were the departure times and not the arrival times. We used the latter ones when we started our argument, so there is a link missing in order to close the loop. It is still to be proved that it does not matter whether we sample either at departures, or at arrival times. Differently we would not know if our analysis for the $M/G/1$ queue is representative of what an observer would see from outside the system. Let us introduce a third distribution $d_{n}(t)$, conditioned to the event that there has just been at departure. We will have the following set of probabilities:

$$
a_{n}(t)=P[N(t)=n\mid\text{an arrival occurred just before time }t]
d_{n}(t)=P[N(t)=n\mid\text{a departure occurred just before time }t]
p_{n}(t)=P[N(t)=n]
$$

$d_{n}(t)$ will be then the statistics left behind by a departing user. The corresponding steady state will be denoted as $d_{n}=\lim_{t\rightarrow\infty}d_{n}(t)$.

We want now to prove that the distribution seen by a departing user is the same one seen by an arriving user. Formally:

$$
d_{n}=a_{n}\qquad n=0,1,...
$$

We want now to close the loop and show that the two steady distributions are the same one, thus $d_{n}$ being equal to the “time average” distribution seen by a Poisson arriving user. In this way we will be able to show that $d_{n}$ denotes the actual distribution at any given time in the long run for $M/G/1$ queue, so being unbiased.


In order to prove this we need a couple of assumptions. The first one is that the system is stable, in other words it must be able to reach all $n$ possible steady states with probability larger than zero: the chain must be positive recurrent. The second one is that $\mathbf{N(t)}$, that describes the number of users in the system at time $t$, must change by unit steps like it happens in


Random Walk processes. This is reasonable: we are allowed to have a single arrival thanks to the Poisson process property where multiple arrivals can not occur. On the other hand, assuming that we have only one server, only one person will leave after each service, so decrementing  $N(t)$  by a unit. These are actually not strong assumptions for our system: a relatively simple one may satisfy them.

![[Stochastic_Processes_2020_p162_img53.jpeg]]
Figure (4.19) - For a stable system we know that we will find it empty with probability 1 an infinite number of times. We can prove it by fixing a value  $n$  a see how many transition upward or downward we encounter with respect to this level.

The first consequence we face once we have assumed that the system is stable, is that in the long run it will be empty an infinite number of times with probability 1. Having fixed a value of  $n$ , for each upward transition there must the relative downward transition, or else the system would not be stable: we know that we will come back to 0 for sure in the future.

Moreover, when we reach a larger value than  $n$  obviously we had to pass through  $n$  itself: no jumps are allowed because the second condition stated above.

In summary, any time the queue empties we will count both a upward and a downward transitions.

Clearly when transition  $n \to n + 1$  occurs, i.e. an user arrives, the latter will find the system in the  $n$ -th state. It is true also the converse: any time a downward transition occurs, i.e.  $n + 1$ -th customer leaves the system, we will find ourselves in state  $n$ .

Let us now compute the total number of transitions  $\mathbf{n} \to \mathbf{n} + \mathbf{1}$  in the generic interval  $[0, t]$ . This is equivalent to compute the number of arrivals in  $[0, t]$  which find the system in state  $n$ . Let us normalize it to the number of the total upward transitions from a generic state  $k$ :

$$
\frac {\# \text {o f} n \rightarrow n + 1 \text {t r a n s i t i o n s i n} [ 0 , t ]}{\# \text {o f} k \rightarrow k + 1 \text {t r a n s i t i o n s i n} [ 0 , t ] \forall k}
$$

We note that the denominator is the total number of arrivals in the  $[0, t]$  interval. The ratio is then the fraction of arrivals in interval  $[0, t]$  that find our system in state  $n$ .

Following the same procedure for the departures:

$$
\frac {\# \text {o f} n + 1 \rightarrow n \text {t r a n s i t i o n s i n} [ 0 , t ]}{\# \text {o f} k + 1 \rightarrow k \text {t r a n s i t i o n s i n} [ 0 , t ] \forall k}
$$

where this is indeed the fraction of departures that leave behind the system in state  $n$ .

Recalling that for each upward transition there must be a downward one, there-


fore the difference between the two numerators must return at most 1, depending on the instant when we sample our system. Sampling, for example, when the system is in a state  $j > n$ , then their difference will return one. In the other case, sampling at  $j' < n$ , will return 0 because either we haven't made any upward transition over the  $n$ -th state, or we have already made its relative downward one.

The fact that the system is stable ensures that, in the limit as  $t \to \infty$ , all the terms in both fractions go to infinity. On the other hand, the difference between the number of upward and downward transitions, that is at most 1, must vanish being it a finite number.

Finally both fractions will converge to an unique value. It holds that:

$$
\lim_{t\to \infty}\frac{\# \mathrm{of} n\to n + 1\mathrm{transitions~in~}[0,t]}{\# \mathrm{of} k\to k + 1\mathrm{transitions~in~}[0,t]\forall k} = \lim_{t\to \infty}\frac{\# \mathrm{of} n + 1\to n\mathrm{transitions~in~}[0,t]}{\# \mathrm{of} k + 1\to k\mathrm{transitions~in~}[0,t]\forall k}
$$

In the limit, the probability that an arriving user finds the system in state  $n$  will be the same for a departing user to leave the state in state  $n$ .

This basically proves the equality:

$$
d _ {n} = a _ {n} \qquad n = 0, 1, \dots .
$$

Consequently our previous analysis made for  $M / G / 1$  queue was consistent and legitimate: even when we considered the embedded Markov Chain subsampling at specific instants, we obtained a result that was representative of the whole behaviour of the chain.

![[Stochastic_Processes_2020_p163_img54.jpeg]]
Figure (4.20) - Sketch depicting the situation of problem 14. We have a transient block, that can lead either to an absorbing block or to a periodic class.


Now we want to discuss the solution for the periodic class exercise (14) at page 125. Recalling its transition matrix:

$$
\mathbb {P} = \left\| \begin{array}{c c c} \mathbb {Q} & \mathbb {R} _ {1} & \mathbb {R} _ {2} \\ 0 & \mathbb {A} & 0 \\ 0 & 0 & 1 \end{array} \right\| \qquad \text {w h e r e}   \mathbb {A} = \left\| \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right\| \qquad \text {a n d}   \mathbb {A} ^ {n} = \left\{ \begin{array}{c c c} \left\| \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right\| & n o d d \\ 1 & 0 \\ 0 & 1 \end{array} \right\} n e v e n
$$


As we can see our chain has a recurrent periodic class  $\mathbb{A}$  of period 2, a transient class  $\mathbb{Q}$  that is connected to the first one thanks to the block  $\mathbb{R}_1$ , and to the last absorbing class thanks to  $\mathbb{R}_2$ . Note that the block  $\mathbb{A}$  will never have a limit because it will oscillate deterministically between the its two states for ever.

Now we want to study the behaviour of  $\mathbb{P}^n$  as  $n$  increases, in particular focusing on the behaviour of the block  $\mathbb{R}_1$ , that may have a limit under certain assumptions. Recall that we know already, from (13) at page 123, that the two subsequences for  $\mathbb{P}^{2n}$  and  $\mathbb{P}^{2n + 1}$  present different limits, but now we wonder whether they might converge to the same one according to some conditions, and therefore making the general limit to exist. We can then easily compute  $\mathbb{P}^2$  and  $\mathbb{P}^3$ :

$$
\mathbb {P} ^ {2} = \left[ \begin{array}{c c c} \mathbb {Q} ^ {2} & \mathbb {Q R} _ {1} + \mathbb {R} _ {1} \mathbb {A} & \mathbb {Q R} _ {2} + \mathbb {R} _ {2} \\ 0 & \mathbb {A} ^ {2} & 0 \\ 0 & 0 & \mathbb {1} \end{array} \right]
\mathbb {P} ^ {3} = \left[ \begin{array}{c c c} \mathbb {Q} ^ {3} & \mathbb {Q} ^ {2} \mathbb {R} _ {1} + \mathbb {Q} \mathbb {R} _ {1} \mathbb {A} + \mathbb {R} _ {1} \mathbb {A} ^ {2} & \mathbb {Q} ^ {2} \mathbb {R} _ {2} + \mathbb {Q} \mathbb {R} _ {2} + \mathbb {R} _ {2} \\ 0 & \mathbb {A} ^ {3} & 0 \\ 0 & 0 & \mathbb {1} \end{array} \right]
$$

We then recognize a pattern, that can be proven by induction as well, while computing  $\mathbb{P}^{n + 1}$ :

$$
\begin{array}{l} \mathbb {P} ^ {n + 1} = \left[ \begin{array}{c c c} \mathbb {Q} ^ {n + 1} & \mathbb {Q} ^ {n} \mathbb {R} _ {1} + \mathbb {Q} ^ {n - 1} \mathbb {R} _ {1} \mathbb {A} + \ldots + \mathbb {Q} \mathbb {R} _ {1} \mathbb {A} ^ {n - 1} + \mathbb {R} _ {1} \mathbb {A} ^ {n} & \left(\sum_ {i = 0} ^ {n} \mathbb {Q} ^ {i}\right) \mathbb {R} _ {2} \\ 0 & \mathbb {A} ^ {n + 1} & 0 \\ 0 & 0 & \mathbb {1} \end{array} \right] = \\ = \left[ \begin{array}{c c c} \mathbb {Q} ^ {n + 1} & \sum_ {i = 0} ^ {n} \mathbb {Q} ^ {i} \mathbb {R} _ {1} \mathbb {A} ^ {n - i} & \left(\sum_ {i = 0} ^ {n} \mathbb {Q} ^ {i}\right) \mathbb {R} _ {2} \\ 0 & \mathbb {A} ^ {n + 1} & 0 \\ 0 & 0 & \mathbb {1} \end{array} \right] = \mathbb {P} ^ {n + 1} \\ \end{array}
$$

and we want to know whether  $\lim_{n\to \infty}\sum_{i = 0}^{n}\mathbf{Q}^i\mathbb{R}_1\mathbb{A}^{n - i}$  this limit exists. For even  $n$  we can replace  $n = 2k$  and:

$$
\sum_ {i = 0} ^ {2 k} \mathbb {Q} ^ {i} \mathbb {R} _ {1} \mathbb {A} ^ {2 k - i} = \sum_ {j = 0} ^ {k} \mathbb {Q} ^ {2 j} \mathbb {R} _ {1} + \sum_ {j = 0} ^ {k - 1} \mathbb {Q} ^ {2 j + 1} \mathbb {R} _ {1} \mathbb {A} =
$$

where we split the initial sum into two terms: the first contains the even indices and the last one the odd indices. Note that if  $i$  is even then also  $2k - 2j$  will be also even, so  $\mathbb{A}^{2k - 2j} = \mathbb{1}$  and thus is absent in the first term. Whereas for the second one we remember that  $\mathbb{A}^{2k + 1 - 2j} = \mathbb{A}$ . We can rewrite the two sums


by using the associative property thus obtaining:

$$
=\left(\sum_{j=0}^{k}\mathbb{Q}^{2j}\right)\mathbb{R}_{1}+\left(\sum_{j=0}^{k-1}\mathbb{Q}^{2j}\right)\mathbb{Q}\mathbb{R}_{1}\mathbb{A}\xrightarrow{k\to\infty}\left[\mathbb{1}-\mathbb{Q}^{2}\right]^{-1}(\mathbb{R}_{1}+\mathbb{Q}\mathbb{R}_{1}\mathbb{A})
$$

Where in the last step we used the fact that the two sums are both geometric and, for large $k$, they converge to the same value that is $[\mathbb{1}-\mathbb{Q}^{2}]^{-1}$. Recall that we are dealing with matrices, so the term $[\mathbb{1}-\mathbb{Q}^{2}]$ is a matrix itself, of which we need to take the inverse.

Whereas for odd $n=2k+1$. Using the same argument and splitting the sum into two sums with even and odd indices, and recalling how $\mathbb{A}^{n}$ behaves for different $n$ we obtain:

$$
\sum_{i=0}^{2k+1}\mathbb{Q}^{i}\mathbb{R}_{1}\mathbb{A}^{2k+1-i}=\sum_{j=0}^{k}\mathbb{Q}^{2j}\mathbb{R}_{1}\mathbb{A}+\sum_{j=0}^{k}\mathbb{Q}^{2j+1}\mathbb{R}_{1}=
$$

That can be rewritten by collecting the common factors as:

$$
\left(\sum_{j=0}^{k}\mathbb{Q}^{2j}\right)(\mathbb{R}_{1}\mathbb{A}+\mathbb{Q}\mathbb{R}_{1})\xrightarrow{k\to\infty}\left[\mathbb{1}-\mathbb{Q}^{2}\right]^{-1}(\mathbb{R}_{1}\mathbb{A}+\mathbb{Q}\mathbb{R}_{1})
$$

where as before we recognized the geometric sum.

The limits of the two different subsequences are the same if it holds that:

$$
[\mathbb{1}-\mathbb{Q}^{2}]^{-1}(\mathbb{R}_{1}+\mathbb{Q}\mathbb{R}_{1}\mathbb{A})=[\mathbb{1}-\mathbb{Q}^{2}]^{-1}(\mathbb{R}_{1}\mathbb{A}+\mathbb{Q}\mathbb{R}_{1})
$$

Where we should have checked that $\mathbb{Q}$ is invertible. But recalling that it is a stochastic process matrix, then we now that it must be invertible and so $\mathbb{Q}$, $\mathbb{Q}^{2}$ and $[\mathbb{1}-\mathbb{Q}]$ are. Rearranging the terms:

$$
\mathbb{R}_{1}+\mathbb{Q}\mathbb{R}_{1}\mathbb{A}=\mathbb{R}_{1}\mathbb{A}+\mathbb{Q}\mathbb{R}_{1}\Rightarrow(\mathbb{1}-\mathbb{Q})\mathbb{R}_{1}=(\mathbb{1}-\mathbb{Q})\mathbb{R}_{1}\mathbb{A}
$$

That returns us the condition for them to be equal that is:

$$
\mathbb{R}_{1}=\mathbb{R}_{1}\mathbb{A}
$$

Note that the term $\mathbb{R}_{1}\mathbb{A}$ is nothing more but $\mathbb{R}_{1}$ where we switched the columns. So the limit for the two subsequences coincide, thus making the general limit exist, only if the columns of $\mathbb{R}_{1}$ are identical. In a statistical point of view, it gives us the condition for the general limit to exist that when we enter a periodic class from a transient state, we do it uniformly. It is indeed a generalization of what we saw some time ago.


Shocks occur to a system according to a Poisson process of rate  $\lambda$ . Suppose that the system survives each shock with probability  $\alpha$ , independently of other shocks, so that its probability of surviving  $k$  shocks is  $\alpha^k$ . What is the probability of surviving at time  $t$ ?

Solution. This exercise can be solved in two ways. The first one, that is the more linear, we want to find:

$$
P[\text{survive at time } t] = \sum_{k=0}^{\infty} P[\text{survive at time } t \mid k \text{ shocks occurred}] P[k \text{ shocks occurred}] =
$$

Where we used the law of total probability. We know in addiction that the probability for  $k$  shocks to occur is Poisson distributed with parameter  $\lambda$ , and for the system to survive  $k$  shocks is  $\alpha^k$ . So we obtain:

$$
= \sum_ {k = 0} ^ {\infty} \alpha^ {k} \frac {e ^ {- \lambda t} (\lambda t) ^ {k}}{k !} = e ^ {- \lambda t} \sum_ {k = 0} ^ {\infty} \frac {(\alpha \lambda t) ^ {k}}{k !} = e ^ {- \lambda t} e ^ {\lambda \alpha t} = e ^ {- \lambda (1 - \alpha) t}
$$

Where we simply took out of the sum the term independent of  $k$  and finally we applied the sum definition of the exponential function. For the second path to solve this exercise, we should have noticed that the last result could be interpreted as the probability of having 0 events, for a process with parameter  $\lambda (1 - \alpha)$ .

![[Stochastic_Processes_2020_p166_img55.jpeg]]
Figure (4.21) - In the problem (4.7.2), once a shock as occurred the system can either survive with probability  $\alpha$ , or not survive with probability  $1 - \alpha$ .

The probability, once a shock occurred, for the system to be alive is then  $\alpha$ , whereas with probability  $1 - \alpha$  it would be fatal. So we have already seen as a split Poisson process is a Poisson process itself with the rate rescaled, in this case by a factor  $\lambda(1 - \alpha)$ , where the  $\lambda$  belongs to the original process. We are requested to compute then the probability for no shock of the "fatal" kind to occur up to time  $t$ , that is a Poisson with parameter  $\lambda(1 - \alpha)$  and  $k = 0$ : it is indeed equal to the one we have found above.


Customers arrive at a facility at random according to a Poisson process of rate  $\lambda$ . There is a waiting time cost of  $c$  per customer per unit time. The customer gather at the facility and are processed or dispatched in groups at fixed times  $T, 2T, 3T, \ldots$ . Any time we dispatch some customers, there is a dispatch cost of  $K$ . The process is depicted in the following graph.

1. What is the total dispatch cost during the first cycle from time 0 to time  $T$ ?
2. What is the mean total customer waiting cost during the first cycle?
3. What is the mean total customer waiting + dispatch cost per unit time during the first cycle?
4. What value of  $T$  minimizes this mean cost per unit time?

![[Stochastic_Processes_2020_p167_img56.jpeg]]
Figure (4.22) - The number of customers in a dispatching system as a function of time for problem (4.7.3)

# Solution.

$a$  ) The answer is simply  $K$  that is the total dispatch cost occurred in the first cycle.
$b$  ) Note that for each customer arrived the system will face a cost  $c$  that is multiplied by the interval of time elapsed until the next dispatch time. It is easy to see that the total customer waiting time is the total area subtended by the curves in the graph above. We can compute the total waiting cost as:

$$
c \int_ {0} ^ {T} X (t) d t
$$

but we know that  $X(t)$  is a random variable. So if we want the mean customer waiting time, we need its expectation value for the first cycle:

average waiting cost  $= c\mathbb{E}[\int_0^T X(t)dt] = c\int_0^T\mathbb{E}[X(t)dt] = c\int_0^T\lambda tdt = \frac{c\lambda T^2}{2}$

where we used the fact that the interval  $[0, T]$  is constant and so we are allowed to bring the expectation value inside the integral. Then, recalling that  $X(t)$  is Poisson we know that its expectation value is  $\lambda t$  and then easily compute the


integral.

c)Whereas, if we want to compute the average total cost per unit time, we need to include the the dispatch cost as well:

$$
\text{average total cost per unit time}=\frac{K+c\lambda T^{2}/2}{T}
$$

d) Last point requests us to optimize the quantity we have just found for the point c) by varying the dispatch time $T$. Note that there is a trade-off: the more we increase $T$, the more the time increases and consequently it waiting cost $c$. Viceversa, decreasing $T$, we dispatch more often thus facing the dispatch cost $K$ more often, whereas the waiting cost $c$ decreases being the waiting times shorter. We can find the optimal value for $T$ by simply deriving wrt T the average total cost per unit time:

$$
\frac{d}{dT}\frac{k+c\lambda T^{2}/2}{T}=-\frac{k}{T^{2}}+\frac{c\lambda}{2}\stackrel{{\scriptstyle!}}{{=}}0
$$

The optimal solution $T*$ that minimizes the cost is then;

$$
T^{*}=\sqrt{\frac{2k}{c\lambda}}
$$


Suppose that a book of 600 pages contains a total of 240 typographical errors uniformly distributed over the pages. Develop a Poisson approximation for the probability that three particular successive pages are error-free.

Solution. When we make the assumption that errors are uniformly distributed, then it implies that each error can be found in a page with probability 1/600. The number of errors on a unique given page we know it follows a binomial distribution, where $p=1/600$ is rather small and conversely $n=240$ is quite high. The given distribution can be approximated by a Poisson with rate $np$, and in formula:

$$
\text{Binom}\left(n=240,p=\frac{1}{600}\right)\simeq\text{Poisson}(np=0.4)
$$

That is the distribution of number of errors on a given page. Making the assumption that each error is independent of the others, and more specifically on the others on different pages, we should notice that we are computing the probability of having 0 errors on three different and disjoint intervals. It does not matter the order of the pages, so we can neglect the request of the problem that they need to be successive, as long as they are distinct pages. The probability requested will be Poisson distributed itself, with rate that is $3\cdot np$: three times the one we stated before for a single page. Formally:


$$
P[3\text{ pages are error-free}]\simeq e^{-1.2}
$$

There is no difference indeed when considering any three pages, or consecutive three pages of the book: the total size of the interval (i.e. number of pages) is the relevant quantity for the Poisson process and not not their position as long as they are disjoint.


Suppose that $N$ points are uniformly distributed over the surface o fa circular disk of radius $r$. Determine the probability distribution for the number of points within a distance of 1 of the origin as $N\to\infty$, $r\to\infty$ in such a way that the ratio $N/(\pi r^{2})=\lambda$ is still constant.

Solution. The extension of Poisson processes to bidimensional systems is quite natural: once we know that the points that fall inside a certain surface are Poisson distributed, we know for sure that their number will depend exclusively on the measure of the area, and will be independent of both the position and the shape because of the stationary increments property. In addition, when we consider two disjoint areas, their increments will be independent of each other. These are the postulates for bidimensional Poisson processes.

![[Stochastic_Processes_2020_p169_img57.jpeg]]
Figure (4.23) – Bidimensional Poisson processes will be independent of both the position and the shape of the two areas, as long as they are disjoint. The number of events counted will be indeed function only of the measure.

We want now to count how many points fall in the small circle of radius 1, given that they are uniformly distributed in the larger circle of radius $r$. Each of these points has the probability of being inside the inner circle of radius $R=1$, that is the ratio between the two areas:

$$
P[\text{being inside small circle}]=\frac{\pi R^{2}}{\pi r^{2}}=\frac{1}{r^{2}}
$$

Number of points in the small circle will be then binomial of the kind ($n=N,p=1/r^{2}$). Now, in the limit as $N\to\infty$, $r\to\infty$ s.t. the average number of points per unit area $N/(\pi r^{2})=\lambda$ is still constant: $\lambda$ is indeed the density of points. It follows that $N/r^{2}=\pi\lambda$ will be fixed as well. Recall that when in a Binomial distribution we let in the limit $N\to\infty$ and $p\to 0$ keeping their product constant, we obtain a Poisson distribution with parameter $\lambda\pi$, that is the average number of points in the inner circle.


We have shown that when we pick a large number of uniformly distributed points in a surface, it can be assimilated to a 2-dim Poisson process because the probability of falling in any area in the limit where  $N, r \to \infty$  will be Poisson.

![[Stochastic_Processes_2020_p170_img58.jpeg]]
Figure (4.24) - Sketch depicting the situation of problem, where the inner circle has radius 1 while the other  $r$ .


For  $i = 1, \dots, n$  let  $\{X_i(t); t \geqslant 0\}$  be independent Poisson processes, each with the same parameter  $\lambda$ . Find the distribution of the first time that at least one event has occurred in every process.

# Solution.

![[Stochastic_Processes_2020_p170_img59.jpeg]]
Figure (4.25) - Problem 4.7.6. Time  $T$  is the maximum time  $t$  where we have at least one arrival per every process

We want then to find the time distribution according to which, for all  $n$  processes we have, one event has occurred. Note that interarrival times for a Poisson process distribute exponentially with the same parameter  $\lambda$ . The time for which all processes will have at least counted one event will be the biggest among all the  $n$  exponentials, namely the time where the last process has counted one event:

$$
T = \max \{T _ {i}, \quad i = 0, 1, \dots , n \}
$$

Now we need to compute its statistics. In order to do so, one should note that we are trying to compute the probability where all first interarrival times for all processes have expired. Therefore the first time it occurs is when the last first-interarrival time itself has expired, that is the maximum among  $n$  exponentials. Having we denoted by  $T$  this maximum, the probability we are asked for is:

$$
P [ T \leqslant t ] = P [ \text {a l l e x p o n e n t i a l s} \leqslant t ] = (1 - e ^ {- \lambda t}) ^ {n}
$$

where the last equality holds because all processes are independent. And so the joint probability is the product of the probability for every single term to be less than  $t$ .



Customers arrive at a holding facility at random according to a Poisson process having rate  $\lambda$ . The facility processes in batches of size  $Q$ . That is, the first  $Q - 1$  customers wait until the arrival of the  $Q$ -th customer. Then all are passed simultaneously, and the process repeats. Service times are instantaneous. Let  $N(t)$  be the number of customers in the holding facility at time  $t$ . Assume that  $N(0) = 0$  and let  $T = \min(t \geqslant 0; N(t) = Q)$  be the first dispatch time.

Show that:

1.  $\mathbb{E}[T] = Q / \lambda$
2. the expected total waiting time is  $\mathbb{E}[\int_0^T N(t)dt] = [1 + 2 + \dots + (Q - 1)] / \lambda = Q(Q - 1) / 2\lambda$ .

![[Stochastic_Processes_2020_p171_img60.jpeg]]
Figure (4.26) - Sketch depicting the situation of problem 4.7.7

Solution. a) First it is to be noted that interarrival times between customers are exponential because we are dealing with a Poisson process with parameter  $\lambda$ . Obviously  $T$  will be the time we need to wait for the  $Q$ -th customer to arrive, and so it is the sum of probability of  $Q$  exponentials all with parameter  $\lambda$ . Its expected value will be Poisson:

$$
\mathbb {E} [ T ] = \sum_ {i = 1} ^ {Q} \frac {1}{\lambda} = \frac {Q}{\lambda} = \frac {\# \mathrm {o f u s e r s}}{\mathrm {a v e r a g e t i m e b e t w e e n u s e r s}}
$$

b) Recall that the expected time we are requested to compute is the area subtended by curves shown in figure (4.26), but in addition we should note that both  $T$  and  $N(t)$  are random variables. Now we see that first user has to wait  $Q - 1$  arrivals before being dispatched, the second one  $Q - 2$  and so forth, up to the  $Q$ -th customer that has no waiting time. The total amount time waited will be the sum of the all the waiting time of the users, that is the sum of all integers from 1 through  $Q - 1$ , normalized to the size of the interval  $\lambda$ . We could have noted instead, that the sum we are looking for is the sum of  $Q$  rectangles, whose height goes from 0 through  $Q - 1$ , while its base is an exponential random variable that on average measures  $1 / \lambda$  for all of them. Using the Gauss summation formula for the first  $Q$  integers, or


eventually making the product in order to compute the area, we finally obtain the value we are looking for:

$$
\mathbb{E}\left[\int_{0}^{T}N(t)dt\right]=[1+2+...+(Q-1)]/\lambda=Q(Q-1)/2\lambda
$$


Let $\{X(t);t\geqslant 0\}$ be a Poisson process of rate $\lambda$. Suppose it is known that in the first unit interval we have $n$ arrivals: $X(1)=n$. For $n=1,2,...$ determine the mean of the first arrival time $W_{1}$.

Solution. If we condition on the number of arrivals, the arrival times are jointly distributed as independent and uniform. Consequently, $W_{1}$ has the same statistics of the minimum of $n$ uniform random variables:

$$
W_{1}=min(U_{i},i=1,2...,n)
$$

So the probability of the minimum to be bigger than a certain value $a$, given we have $n$ arrivals, is equivalent to the probability for all the random variables to be bigger than the same value:

$$
P[W_{1}>a]=P[\text{all }U_{i}^{\prime}s<a,i=1,2...,n]=(P[U>a])^{n}=(1-a)^{n}
$$

Where we used the property that all $U_{i}$’s are independent, and we assumed that $a\in[0,1]$, so the probability for $U_{i}$ to be bigger than it is just $1-a$ for each of them. Recall that this is all conditioned on the event that we have $n$ arrivals. The expectation value of $W_{1}$ given $n$ arrivals will be the integral of the tail distribution $P[W_{1}>a]$:

$$
\mathbb{E}[W_{1}|n\text{ arrivals in }[0,1]]=\int_{0}^{1}P[W_{1}>a]da=\int_{0}^{1}(1-a)^{n}da=\frac{1}{n+1}
$$

Thus concluding our exercise.


Customers arrive at a certain facility according to a Poisson process of rate $\lambda$. Suppose that it is known that five customers arrived in the first hour. Determine the mean total waiting time $\mathbb{E}[W_{1}+W_{2}+W_{3}+W_{4}+W_{5}]$.

Solution. As the previous exercise, we are given the number of arrivals that is 5: the $W_{i}$’s have a joint probability distribution that is like i.i.d. uniform random variables in the interval $[0,1]$h. Each of them has an average of 1/2hr, consequently their sum will be 2h30min.


###### Exercise 4.7.10 (Chap V - Ex. 4.5):

Customers arrive at a certain facility according to a Poisson process of rate $\lambda$. Suppose that is know that five customers arrived in the first hour. Each customer spends a time in the store that is a random variable, exponentially distributed with parameter $\alpha$ and independent of the other customer times, and then departs. What is the probability that the store is empty at the end of the first hour?

Solution. We can start again by conditioning on the number of arrivals that is 5, and each of them will distribute according to an i.i.d uniform distribution in the interval $[0,1]$h. The probability that the store is empty is the probability that all users have left after the first hour, a single user indeed does not depart within time $t$ with probability:

$$
P[\text{user has not departed}]=P[W+Y>t]=\vspace*{-0.1cm}
$$

Where $W$ is the arrival time and $Y$ is the service time. We now need to condition over the number of arrivals, and then replace the variable $W$ with $U$ that distributes uniformly. Picking moreover $t$ to be 1hr and conditioning over the uniform arrival time, we obtain:

$$
=P[U+Y>1]=\int_{0}^{1}P[Y>1-u]du=\int_{0}^{1}e^{-\alpha(1-u)}du=\frac{1-e^{-\alpha}}{\alpha}
$$

Where we used the fact that $Y$ distributes exponentially and then we integrated. We have just found the probability that a user is still in the system, consequently its complementary to 1 will be the probability that a user has already departed. Finally, since the times for all the users are independent of each other, the joint probability will be their product and thus obtaining:

$$
P[\text{system is empty}|5\text{ arrivals in }[0,1]]=P[\text{all users have left}|\text{ we had 5 users}]=\vspace*{-0.1cm}
=\left(1-\frac{1-e^{-\alpha}}{\alpha}\right)^{5}
$$


