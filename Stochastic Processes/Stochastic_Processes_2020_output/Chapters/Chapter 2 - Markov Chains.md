# Chapter 2 Markov Chains

A Markov process $\{X_{t}\}$ is a stochastic process with the property that, given the value of $X_{t}$, the values of the process in the future, i.e. $X_{s}$ for $s>t$, are not influenced by the values of $X_{u}$ in the past $u<t$. In other words, all the necessary information for predicting the system’s future is contained in the present state.

A Markov process with discrete values ($X_{t}$ assumes values in a countable set) and discrete index (i.e. the index set $T$ is countable too) is called a Markov chain. In this case the Markov property states:

$$
\mathbb{P}\{X_{n+1}=j|X_{0}=i_{0},\ldots,X_{n-1}=i_{n-1},X_{n}=i\}=\mathbb{P}\{X_{n+1}=j|X_{n}=i\}
$$

for any possible choice of the states $i_{0},\ldots,i_{n}$, $i$, $j$, and for all time points $n$. We will usually label the states (i.e. values of $X_{t}$) with the non-negative integers $\mathbb{N}$.

The probability of $X_{n+1}$ being in state $j$ given that the previous state $X_{n}$ is in state $i$ is called the one-step transition probability and is denoted with $P^{n,n+1}_{ij}$:

$$
\mathbb{P}^{n,n+1}_{ij}=\mathbb{P}\{X_{n+1}=j|X_{n}=i\}
$$

If $P^{n,n+1}_{ij}\equiv P_{ij}$ independent of $n$, then the Markov chain is called homogeneous, or that it has stationary transition probabilities. Most of the interesting cases have this property.

We can interpret $P_{ij}$ as entries in a matrix $\mathbf{P}$, which is called transition probability matrix. Each row $i$ contains the probability distribution of the values of $X_{n+1}$ given that the present state is $X_{n}=i$. So, all elements in any row must sum to unity:

$$
P_{ij}\geq 0\quad\forall i,j\in\mathbb{N};\qquad\sum_{j=0}^{+\infty}P_{ij}=1\quad\forall j\in\mathbb{N}
$$

The matrix $P$ and the initial state $X_{0}$ (or, in general, the initial probability distribution over all states) fully specify a Markov chain.

Markov process


Proof. Suppose that the initial distribution is given by $\mathbb{P}(X_{0}=i)=p_{i}$. The Markov chain is *fully specified* if we can compute the (joint) probability of *any sequence of states* $\{i_{0},\ldots,i_{n}\}$:

$$
\mathbb{P}\{X_{0}=i_{0},X_{1}=i_{1},\ldots,X_{n}=i_{n}\}
$$

Then the probability of any event $E$ will be just the *sum* of the probabilities associated with the sequences *contained* in that event. For example, if we wish to compute the probability of $X_{i}=j$, we sum the probabilities of all possible *evolutions* of the system that verify this equation, which are always in the form (2.1).

By definition of conditional probabilities we can rewrite (2.1) as follows:

$$
\mathbb{P}\{X_{0}=i_{0},X_{1}=i_{1},\ldots,X_{n}=i_{n}\}=\mathbb{P}\{X_{n}=i_{n}|X_{0}=i_{0},\ldots,X_{n-1}=i_{n-1}\}\cdot
\cdot\mathbb{P}\{X_{0}=i_{0},X_{1}=i_{1},\ldots,X_{n-1}=i_{n-1}\}
$$

Then we apply the Markov property:

$$
\mathbb{P}\{X_{n}=i_{n}|X_{0}=i_{0},\ldots,X_{n-1}=i_{n-1}\}=\mathbb{P}\{X_{n}=i_{n}|X_{n-1}=i_{n-1}\}=P_{i_{n-1},i_{n}}
$$

Substituting (2.3) in (2.2) we obtain:

$$
\mathbb{P}\{X_{0}=i_{0},X_{1}=i_{1},\ldots,X_{n}=i_{n}\}=P_{i_{n-1},i_{n}}\mathbb{P}\{X_{0}=i_{0},X_{1}=i_{1},\ldots,X_{n-1}=i_{n-1}\}
$$

Reiterating:

$$
\mathbb{P}\{X_{0}=i_{0},X_{1}=i_{1},\ldots,X_{n}=i_{n}\}=p_{i_{0}}P_{i_{0},i_{1}}\cdots P_{i_{n-2},i_{n-1}}P_{i_{n-1},i_{n}}
$$

And so all joint probabilities can be computed if we know $\{p_{i}\}_{i\in\mathbb{N}}$ and the transition matrix $\mathbf{P}$.

To understand the behaviour of a Markov Chain we may inspect the $n$-step transition probabilities, i.e. the probabilities of the process going from a certain state $i$ to a state $j$ in exactly $n$ transitions:

$$
P_{ij}^{(n)}\equiv\mathbb{P}\{X_{m+n}=j|X_{m}=i\}
$$

which is independent on $m$ for a homogeneous Markov Chain.


The $n$-step transition probabilities of a Markov chain can be written recursively as:

$$
P_{ij}^{(n)}=\sum_{k=0}^{+\infty}P_{ik}P_{kj}^{(n-1)}
$$


where:

$$
P^{(0)}_{ij}\equiv\begin{cases}1&\text{if }i=j\\
0&\text{if }i\neq j\end{cases}
$$

Proof. We start from the definition, taking $m=0$ (as the process is homogeneous):

$$
P^{(n)}_{ij}=\mathbb{P}\{X_{n}=j|X_{0}=i\}=
$$

We consider the state $X_{1}$ at time $1$, and apply the law of total probability, noting that events $X_{1}=k$ for different values of $k$ are both mutually exclusive and exhaustive:

$$
=\sum_{k=0}^{+\infty}\mathbb{P}\{X_{n}=j,X_{1}=k|X_{0}=i\}=
$$

Recall that:

$$
\mathbb{P}(AB)=\mathbb{P}(A|B)\mathbb{P}(B)
$$

Equivalently, we can condition each probability to any event $C$:

$$
\mathbb{P}(AB|C)=\mathbb{P}(A|B,C)\mathbb{P}(B|C)
$$

And so:

$$
P^{(n)}_{ij}=\sum_{k=0}^{+\infty}\mathbb{P}\{X_{n}=j|X_{1}=k,X_{0}=i\}\mathbb{P}(X_{1}=k|X_{0}=i)=
$$

Applying the Markov property we can *remove* the condition $X_{0}=i$ in the first term, as all the information about the *past* will be still contained in $X_{1}$:

$$
=\sum_{k=0}^{+\infty}\underbrace{\mathbb{P}\{X_{n}=j|X_{1}=k\}}_{P^{(n-1)}_{kj}}\underbrace{\mathbb{P}(X_{1}=k|X_{0}=i)}_{P_{ik}}=
=\sum_{k=0}^{+\infty}P_{ik}P^{(n-1)}_{kj} \square
$$

Note that (2.4) is a matrix multiplication:

$$
\mathbf{P}^{(n)}=\mathbf{P}\times\mathbf{P}^{(n-1)}
$$

Reiterating:

$$
\mathbf{P}^{(n)}=\underbrace{\mathbf{P}\times\cdots\times\mathbf{P}}_{n\text{ factors}}=\mathbf{P}^{(n)}
$$


![[Stochastic_Processes_2020_p30_img3.jpeg]]
Figure (2.1) - Markov chain graph for exercise 4.


From exercise (3.)1.1 on the book. A Markov chain  $\{X_{i}\}_{i\in \mathbb{N}}$  on states 0, 1, 2 has the transition probability matrix:

$$
\mathbf {P} = \left( \begin{array}{c c c} 0. 1 & 0. 2 & 0. 7 \\ 0. 9 & 0. 1 & 0 \\ 0. 1 & 0. 8 & 0. 1 \end{array} \right)
$$

and initial distribution:

$$
\boldsymbol {p} = (p _ {0}, p _ {1}, p _ {2}) ^ {T} = \left( \begin{array}{c} 0. 3 \\ 0. 4 \\ 0. 3 \end{array} \right)
$$

Determine  $\mathbb{P}\{X_0 = 0, X_1 = 1, X_2 = 2\}$ .

Solution. We follow the diagram. The probability of starting at  $X_0$  is  $p_0$ , and then we multiply by each transition:

$$
\begin{array}{l} \mathbb {P} \left\{X _ {0} = 0, X _ {1} = 1, X _ {2} = 1 \right\} = p _ {0} P _ {0 1} P _ {1 1} = \\ = 0. 3 \cdot 0. 2 \cdot 0. 1 = 0. 0 0 6 \\ \end{array}
$$

More in general, we may have non-consecutive states, for example in computing  $\mathbb{P}\{X_0 = 0,X_1 = 1,X_3 = 1\}$ . In this case we need the 2-step transition probability - summing over all intermediate states:

$$
\begin{array}{l} \mathbb {P} \left\{X _ {0} = 0, X _ {1} = 1, X _ {3} = 1 \right\} = p _ {0} \cdot P _ {0 1} P _ {1 1} ^ {(2)} = \\ = \sum_ {k = 0} ^ {2} p _ {0} P _ {0 1} P _ {1 k} P _ {k 1} = p _ {0} P _ {0 1} \sum_ {k = 0} ^ {2} P _ {1 k} P _ {k 1} \\ \end{array}
$$

And the last sum is just the scalar product between row 1 and column 1.

One more case is when we have conditional probabilities, such as  $\mathbb{P}[X_3 = 1, X_1 = 1 | X_0 = 0]$ . In this case we already know the initial state, so we do


not need to account for its probability, meaning that:

$$
\mathbb{P}[X_{3}=1,X_{1}=1|X_{0}=0]=P_{01}\cdot P_{11}^{(2)}
$$

### 2.1 Models

Many natural physical processes can be approximately modelled by Markov chains, leading to several interesting analytical results. In this section we will study some of such examples.

#### 2.1.1 Discrete Queueing

Consider a situations when customers arrive for service. In each time slot a single customer can be served, if there is one - otherwise nothing happens. If several people arrive at the same time, they will queue and wait for their turn.

Let’s denote with $X_{n}$ the number of users in the system at the beginning of slot $n$. At any time slots we will have a certain (random) number of arrivals $\xi_{n}$, with is a r.v. with probability distribution:

$$
\mathbb{P}[\xi_{n}=k]=a_{k}
$$

where we assume that $a_{k}$ is independent of $n$ (the arrival rate is uniform, and arrivals are uncorrelated). If the system contains at least a customer at time slot $n$ (i.e. $X_{n}>0$), we will have a departure, otherwise not:

$$
X_{n+1}=\begin{cases}X_{n}-1+\xi_{n}&X_{n}>0\\
\xi_{n}&X_{n}=0\end{cases}
$$

We can rewrite this more compactly as:

$$
X_{n+1}=(X_{n}-1)^{+}+\xi_{n}
$$

where $Y^{+}\equiv\max(Y,0)$. Note that if we know $X_{n}$, we can fully characterize $X_{n+1}$ without knowing the states $X_{u}$ with $u<n$ - and so this is indeed a Markov chain.

The transition probability matrix is given by:

$$
\mathbf{P}=\left(\begin{array}[]{cccccc}a_{0}&a_{1}&a_{2}&a_{3}&a_{4}&\cdots\\
a_{0}&a_{1}&a_{2}&a_{3}&a_{4}&\cdots\\
0&a_{0}&a_{1}&a_{2}&a_{3}&\cdots\\
0&0&a_{0}&a_{1}&a_{2}&\cdots\\
0&0&0&a_{0}&a_{1}&\cdots\\
\vdots&\vdots&\vdots&\vdots&\vdots&\ddots\end{array}\right)
$$


The first row ($n=0$) is given by the probability distribution $\{a_{i}\}_{i\in\mathbb{N}}$: the system starts empty, $k$ customers enter with probability $a_{k}$, and so the system moves to the state $X_{k}$.

For the second line ($n=1$), we start with 1 customer, that is served and goes away. So, at the end we will just have the $k$ arrivals - recreating the same situation of the first line.

The situation changes from the third ($n=2$) line on, as now $n-1>0$ customers remain in queue, and so the system cannot transition to states $X_{k}$ with $k<n-1$, meaning that $0s$ appear in $\mathbb{P}.$ All transitions to the other states have probabilities $\{a_{k}\}$, which are shifted to the right by the queue size $n-1$.

The arrival rate is defined by the average:

$$
\langle\xi_{k}\rangle=\sum_{k=0}^{+\infty}ka_{k}
$$

If $\langle\xi_{k}\rangle>1$, then the size of the queue will diverge, as at every time slot more customers arrive than depart. We say that, in this case, the system is unstable. On the other hand, if $\langle\xi_{k}\rangle<1$, the queue size will remain finite. The boundary case, where $\langle\xi_{k}\rangle=1$ is trickier to analyse. We will see that if the arrivals are deterministic, in the sense that exactly one customer arrives at every time slot, then the system will be stable. But as soon the arrivals are non-deterministic, the system exhibits instability.

### 2.2 Poisson Process

An important class of Markov chains is given by Poisson processes, which can be used to model situations where independents events occur at random points in time.

Let $X_{t}$ be the number of events (e.g. arrivals) occurring in $[0,t]$. Then we define:

1. $X_{0}=0$, meaning that no events can happen if the “experiment” is run for 0 time.
2. Increments are both stationary and independent. With increments we denote differences of random variables, such as $X_{t_{2}}-X_{t_{1}}$ for $t_{2}>t_{1}$, representing the number of events contained in $[0,t_{2}]$ which are not present in $[0,t_{1}]$. Equivalently, $X_{t_{2}}-X_{t_{1}}$ is the number of events happening in $[t_{1},t_{2}]$.

Independent increments means that, if we take disjoint intervals $I_{1}=[t_{1},t_{2}]$ and $I_{2}=[t_{3},t_{4}]$, with $I_{1}\cap I_{2}=\varnothing$, then the number of events happening in $I_{1}$ and $I_{2}$ are independent:

$$
X_{t_{2}}-X_{t_{1}}\text{ and }X_{t_{4}}-X_{t_{3}}\text{ independent r.v.}\Leftrightarrow[t_{1},t_{2}]\cap[t_{3},t_{4}]=\varnothing
$$


Stationary increments means that the the numbers of events occurring in (disjoint) time intervals of the same size follow the same distribution:

$$
X_{s+t}-X_{s}\sim X_{s^{\prime}+t}-X_{s^{\prime}}\text{ if }[s,s+t]\cap[s^{\prime},s^{\prime}+t]=\varnothing
$$

In other words, the distribution of the number of events inside an interval depends only on that interval’s size $t$.
3. The probability of $n$ events occurring inside an interval of size $t$, regardless of its position, is given by a Poisson distribution:

$$
\mathbb{P}[X_{t+s}-X_{s}=n]=\frac{e^{-\lambda t}(\lambda t)^{n}}{n!}
$$

where $\lambda$ represents the average number of events occurring per unit time.

Equivalently, we can specify the distribution by requiring that:

$$
\mathbb{P}[X_{h}\geq 1] =\lambda h+o(k)=p(k)
\mathbb{P}[X_{h}\geq 2] =o(h)
$$

with $o(h)$ denoting a function such that:

$$
\lim_{h\to 0}\frac{o(h)}{h}=0
$$

This means that in a *very small interval* $[0,h]$, the probability of at least one event happening (i.e. that $X_{h}\geq 1$) is linear in $h$, whereas the probability of 2 or more events happening in that interval is negligible. In other words, “simultaneous arrivals”, i.e. events occurring “really close to each others” is very small, and can be neglected (in this sense, events are “rare”).

(The proof of the equivalence between these two definitions is omitted).


In a Poisson process, the inter-arrival times (i.e. the time between two consecutive events) are i.i.d. exponential random variables, with parameter $\lambda$.

Proof. Let $\{S_{i}\}_{i\in\mathbb{N}}$ be the inter-arrival times, and $W_{n}$ the *cumulative* arrival times, defined as:

$$
W_{n}=\sum_{i=0}^{n}S_{i}
$$

Let’s consider the first difference:

$$
\mathbb{P}[S_{0}>t]=\mathbb{P}[0\text{ arrivals in }[0,t]]\underset{(2.5)}{=}e^{-\lambda t}
$$

and so $S_{0}$ follows an exponential distribution with parameter $\lambda$.


We now consider the next one:

$$
\mathbb{P}[S_{1}>t|S_{0}=s]=\mathbb{P}[0\text{ arrivals in }(s,s+t]|S_{0}=s]
$$

But the number of arrivals in disjoint intervals are independent, and so we can drop the condition $S_{0}=s$. Applying stationarity we know that this probability depends only on the size of the interval, which is the same as that of $[0,t]$, and so we get the same result as before:

$$
=e^{-\lambda t}
$$

This means that also $S_{1}$ follows an exponential distribution with parameter $\lambda$, and is independent of $S_{0}$.

The same argument can be repeated for any given $S_{n}$:

$$
\mathbb{P}[S_{n}>t|S_{i}=s_{i},i=0,\ldots,n-1]=
\mathbb{P}[0\text{ arrivals in }(s_{0}+\cdots+s_{n-1},s_{0}+\cdots+s_{n-1}+t)|S_{i}=s_{i}]=e^{-\lambda t}
$$

which completes the proof of the theorem.

### 2.3 M/G/1 Queue

A more complex model for the queueing system is given by considering different service times for each customer, and treat arrivals as a Poisson process. This leads to the M/G/1 model.

- The first letter denotes the type of the interarrival distribution, which in this case is intended to be “Memoryless”, and thus exponential.
- The second letter describes the distribution of the service time. $G$ stands for “general”, meaning that we don’t make any assumption on that pdf.
- The 1 at the end is the number of servers, i.e. the number of clients that can be served at once.

As in the previous case, a customer arriving when the server is free will go immediately to the service, while others will wait their turn in an orderly queue. If at any time there are no customers being served and no arrivals, no service will be given.

We could be tempted to define $X(t)$ as the number of customers in the system at $t$, and then consider the stochastic process $\{X(t),t\geq 0\}$. Unfortunately, this is not a Markovian process, as it not satisfies the Markovian property. The amount time elapsed from the last arrival *does not matter* for the distribution of arrival times (as it is memoryless). However, the departure times *do* depend on past information. As we assume a *generic* distribution for the service time, it won’t necessarily be memoryless, meaning that the time until the next departure depends on how much time has passed from the service’s start, which is information *not contained* in just the state $X_{t}$.


Note that in the previous example we circumvented this problem by fixing a definite, deterministic, duration for the service: one customer is served in a single time slot. Here we are not making such assumption.

To reduce the system to a Markov process, we can just include the necessary information (how much time the user currently being served has been there) in the current state. However, this will make the model much more complex.

Another way is to discretize time, by sampling  $X_{t}$  just at the departures' time. This is a variation of the "time slots" we used in the first examples - however in this case the time slots are not all of the same size, and their duration is not deterministic.

In fact, when a customer departs at instant  $\bar{t}$ , the behaviour of the system is fully specified by the  $X_{\bar{t}}$  at that time. If  $X_{\bar{t}} > 0$ , then the next user in queue will be served, and if  $X_{\bar{t}} = 0$ , nothing happens.

This is one example of a more general trick: often a process  $\{X_{t}\}_{t\in \mathbb{R}^{+}}$  is not a Markov process, but a "discretized sample"  $\{X_{t_i}\}_{i\in \mathbb{N}}$  for a certain "good" choice of instants  $\{t_i\}$  is a Markov process.

![[Stochastic_Processes_2020_p35_img4.jpeg]]
Figure (2.2) - Example of evolution for the MG1 queuing system

So, let's denote with  $t_n$  the time of the  $n$ -th departure, and with  $X_n \equiv X(t_n^+)$  ( $n \geq 1$ ) the number of customers in the system left behind by the  $n$ -th departure $^1$ , as illustrated in fig. 2.2.

We also denote with  $Y_{n}$  ( $n \geq 0$ ) the number of arrivals occurring during the service time for the  $n$ -th customer, which is given by the difference between  $t_{n}$  and the arrival time of that customer. If the queue size is  $> 0$ , then the latter will simply be  $t_{n-1}$ , as illustrated in fig. 2.3.

With this notation, we can describe the system's evolution similarly to the previous example:

$$
X _ {n + 1} = \left\{ \begin{array}{l l} X _ {n} - 1 + Y _ {n} & X _ {n} \geqslant 1 \\ Y _ {n} & X _ {n} = 0 \end{array} \right. \tag {2.6}
$$


![[Stochastic_Processes_2020_p36_img5.jpeg]]
Figure (2.3) - Service times and departure times for the MG1 queuing system. Note that  $X_{1} \equiv X(t_{1}^{+}) = 1$ , and so  $X_{2} = 2$ ,  $X_{3} = 1$ ,  $X_{4} = 0$  and  $X_{5} = 1$ .

The system starts empty ( $X_0 = 0$ ). One customer arrives, is served, and then departs, meaning that he/she will not count towards  $X_1$ , which is evaluated after their departure. What we need to count is the number of arrivals  $Y_1$  in that service time, and so  $X_1 = Y_1$ , which is equal to 1 in the case of fig. 2.3.

If the system is not empty at time  $t_n$ , then one customer from the queue will immediately enter service, meaning that  $X_{n+1} = (X_n - 1)$ , plus again the number of arrivals  $Y_n$  in the previous service time. For example, in 2.3, we have that  $X_1 = 1$ ,  $Y_1 = 2$  (2 arrivals in that service time), and so  $X_2 = 1 - 1 + 2 = 2$ .

So, the only difference of (2.6) from the previous simpler case is that now  $Y_{n}$  is the number of arrivals during an interval of random size. If the interval's size  $X$  had a fixed value  $x$ , we could write:

$$
\mathbb {P} \{Y _ {n} = j \} = e ^ {- \lambda x} \frac {(\lambda x) ^ {j}}{j !}
$$

But since  $X$  is not fixed, but it's a random variable with cdf  $G(x)$ , we need to construct an average:

$$
a _ {j} \equiv \mathbb {P} \{Y _ {n} = j \} = \int_ {0} ^ {\infty} e ^ {- \lambda x} \frac {(\lambda x) ^ {j}}{j !} \mathrm {d} G (x) \qquad j \in \mathbb {N}
$$

These probabilities represent the  $a_{j}$  from the previous example, and as the evolution equation is also the same, we obtain the same transition probability matrix:

$$
\mathbf {P} = \left( \begin{array}{c c c c c c} a _ {0} & a _ {1} & a _ {2} & a _ {3} & a _ {4} & \dots \\ a _ {0} & a _ {1} & a _ {2} & a _ {3} & a _ {4} & \dots \\ 0 & a _ {0} & a _ {1} & a _ {2} & a _ {3} & \dots \\ 0 & 0 & a _ {0} & a _ {1} & a _ {2} & \dots \\ 0 & 0 & 0 & a _ {0} & a _ {1} & \dots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{array} \right)
$$

## 2.4 G/M/1 queue

Suppose now that the interarrival times are i.i.d. random variables with a generic distribution  $G$  (not necessarily memoryless), while the service times


follow a memoryless distribution, which we suppose to be exponential with rate $\mu$.

Again, if we denote with $X_{t}$ the number of customers in the system at time $t$, $\{X(t)\}_{t\geq 0}$ is not a Markov process, due to the fact that $G$ is, in general, not memoryless. In particular, the elapsed time from the previous arrival is necessary information for constructing the distribution of the next arrival time, and it is not contained in the state $X_{t}$.

So, the idea is to consider - as before - a discrete subset $\{X_{t_{i}}\}_{i\in{\bf N}}$, choosing the instants $t_{i}$ such that the information missing in $X_{t}$ becomes irrelevant for describing the system’s behaviour at times $t_{i}$. In this case, the correct choice is to identify the $t_{i}$ with the arrival times: if we know that a customer has just arrived and the queue is free, then they will be served; otherwise they will wait in line. As the service time follows a memoryless distribution - meaning that it is completely characterized by the state at any time - the resulting $\{X_{t_{i}}\}$ is indeed a random process.

So, let’s fix $t_{n}$ to be the time of the $n$-th arrival, and $X_{n}\equiv X(t_{n}^{-})$ the number of customers in the system just before the $n$-th arrival. The interarrival time is denoted by $T\sim G(t)$, while the service times are $\alpha_{k}$ i.i.d. r.v. with exponential distribution $\exp(\mu)$.

We then consider the transition probabilities:

$$
P_{i,i+1-j}={\rm I\kern-1.79993ptP}[j\ \mbox{departures}]\qquad j=0,1,\ldots,i+1
$$

In other words, if a customer arrives at $t_{n}$, while there are $i$ customers in the system ($X_{n}=i$), then the number of customers just before the next arrival $X_{n+1}$ will be $i$ (customers initially in queue) $+1$ (the customer previously arrived) $-j$ (the departures happened during the interarrival time $T$). Note that there cannot be more departures than the number of clients $i+1$. and so $j\leq i+1$.
To compute the transition probabilities (2.7) we distinguish between three cases:

- If $j<i+1$, then some customers remain in the system. We rewrite (2.7) noting that if $j$ departures occur during the time interval $T$, it means that the sum of $j$ inter-departure times $\alpha_{k}$ “fits” in $T$, but if we add also the time needed for another departure we surpass $T$:

$$
{\rm I\kern-1.79993ptP}[j\ \mbox{departures}|X_{n}=i] = {\rm I\kern-1.79993ptP}\left[\sum_{k=1}^{j}\alpha_{k}\leq T<\sum_{k=1}^{k+1}\alpha_{k}\right]=
$$
$$
\mathbb{P}(\text{exactly } k \text{ Poisson events})
$$
$$
=\int_{0}^{+\infty}\frac{e^{-\mu t}(\mu t)^{j}}{j!}\,{\rm d}G(t)
$$
- If $j=i+1$, then all users depart. The only thing that changes is that


there is no “next departure” to consider in step (a), leading to:

$$
\mathbb{P}[i+1\text{ departures}|X_{n}=i] =\mathbb{P}\left[\sum_{k=1}^{i+1}\alpha_{k}\leq T\right]=
=\mathbb{P}[\text{at least }i+1\text{ Poisson events in }[0,T]]=
=\int_{0}^{+\infty}\sum_{k=i+1}^{+\infty}\frac{e^{-\mu t}(\mu t)^{k}}{k!}\,\mathrm{d}G(t)
$$

In fact, while in the first case more than $j$ departures would have changed the system, in this case a “subsequent departure event” results in no change, as there is no customer that can leave.

We can then rewrite the infinite sum by noting that, by normalization:

$$
1=\int_{0}^{+\infty}\sum_{k=0}^{+\infty}\frac{e^{-\mu t}(\mu t)^{k}}{k!}\,\mathrm{d}G(t)=
=\int_{0}^{+\infty}\sum_{k=0}^{i}\frac{e^{-\mu t}(\mu t)^{k}}{k!}\,\mathrm{d}G(t)+\int_{0}^{+\infty}\sum_{k=i+1}^{+\infty}\frac{e^{-\mu t}(\mu t)^{k}}{k!}\,\mathrm{d}G(t)
$$

and so:

$$
\mathbb{P}[i+1\text{ departures}|X_{n}=i]=1-\int_{0}^{+\infty}\sum_{k=0}^{i}\frac{e^{-\mu t}(\mu t)^{k}}{k!}\,\mathrm{d}G(t)
$$
- As previously commented, there cannot be more than $i+1$ departures:

$$
\mathbb{P}[\text{More than }i+1\text{ departures}|X_{n}=i]=P_{i,l}=0\qquad l>i+1
$$

### 2.5 Data transmission protocols

Another example of system that can be modelled by Markov processes is given by data transmission protocols.

In particular, we consider a buffer that receives some data, and relays it to some other machine. For simplicity, we discretize time in equal slots of $T$ seconds each, and specify that during each slot data is transmitted (if available).

Denote with $\xi_{k}$ the amount of data generated during the time slot $n$. $\xi_{k}$ are random variables with statistics given by:

$$
\mathbb{P}[k\text{ data units generated in slot }n]\equiv\mathbb{P}[\xi_{k}=k]=a_{k}\qquad k\geq 0
$$

We then consider different protocols for sending data:

1. At the beginning of each slot, all data is scheduled for transmission, up to a max of $M$ units (link capacity), which is given by the product of the output speed and the time slot duration $T$. All remaining data will be left in the buffer, and will be served during next slots.


2. In a real case, sending data will require attaching headers and controls to packets, introducing a certain amount of overhead in the system. If the amount of data sent is sufficiently high, this kind of overhead is relatively small. However, if the buffer sends only a few bytes, the overhead will be significant, and the procedure inefficient.

So, a better protocol will prevent the sending of "too little" data by specifying a minimum data size  $m$  for transmission. In other words, the buffer will wait for at least  $m$  units of data before sending them. So, at the start of each time slot:

(a) If there is less than  $m$  data in the buffer, do nothing.
(b) If more than  $m$  data: send all data, up to a max of  $M$  units.

Note that in both protocols, the choice of what data to send is scheduled at the start of each time slot. In this way, all data that arrives during a slot will be sent at best during the next time slot.

So, let's denote with  $X_{n}$  the amount of data in the buffer at the beginning of the  $n$ -th time slot.  $\{X_{n}\}_{n\in \mathbb{N}}$  is then a Markov chain, because the buffer status at any given time  $X_{n + 1}$  depends only on the content at the previous step  $(X_{n})$  and the amount of data  $(\xi_{n})$  arriving during the time slot  $n$ , with  $\{\xi_n\}$  being i.i.d. random variables.

### Protocol 1

If at the beginning of time slot  $n$  there is less than  $M$  data in the buffer, then we send of all it, and the buffer at the next time will only contain the newly arrived data  $\xi_{n}$ . Otherwise, we send  $M$  units of data, leaving  $X_{n} - M$  in the buffer, plus again the newly arrived data  $\xi_{n}$ . So the system's evolution can be described by:

$$
X _ {n + 1} = \left\{ \begin{array}{l l} \xi_ {n} & X _ {n} \leq M \\ X _ {n} - M + \xi_ {n} & X _ {n} > M \end{array} \right.
$$

The full transition matrix becomes:

$$
P _ {i j} = \left\{ \begin{array}{l l} a _ {j} & i \leq M \\ a _ {j + M - i} & i > M \end{array} \right. \quad \mathbf {P} = \begin{array}{c c c c c c c c} 0 & a _ {0} & a _ {1} & a _ {2} & \dots & \dots & \dots & \dots \\ 0 & a _ {0} & a _ {1} & a _ {2} & \dots & \dots & \dots & \dots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ a _ {0} & a _ {1} & a _ {2} & \dots & \dots & \dots & \dots & \dots \\ 0 & a _ {0} & a _ {1} & a _ {2} & \dots & \dots & \dots & \dots \\ 0 & 0 & a _ {0} & a _ {1} & a _ {2} & \dots & \dots & \dots \\ \vdots & \ddots & \ddots & \ddots & \ddots & \ddots & \ddots & \ddots \end{array}
$$

and is represented by the block diagram in fig. 2.4.


![[Stochastic_Processes_2020_p40_img6.jpeg]]
Figure (2.4) - Block diagram for protocol 1. The transition probabilities between the first  $M$  states are all the same, and "start to change" for the  $M + 1$  state onwards.

### Protocol 2

We examine two variants: one where  $M = +\infty$  (a), and one with finite  $M$  (b). For the case (2a) the evolution becomes:

|  Xn+1 = {ξn Xn +ξn otherwise | 0 | 1 | 2 | ... | m-2 | m-1 | ...  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|   |  0 | a0 | a1 | a2 | ... | ... | ...  |

In other words, if the data is enough  $(\geq m)$ , we send it all (as there is no size limit), and the next state will be the one holding just the newly arrived data  $\xi_{n}$ . Otherwise, we keep all the current data  $X_{n}$ , without sending anything, and also add the newly arrived data  $\xi_{n}$ .

The transition matrix becomes:

|  Pij = {aj Xn ≥ m aj-1 Xn < m | P = | 0 | 1 | 2 | ... | m-2 | m-1 | ...  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |   |  0 | a0 | a1 | ... | ... | ... | ...  |
|   |   |  1 | ... | ... | ... | ... | ... | ...  |
|   |   |  ... | 0 | 0 | ... | 0 | a0 | ...  |
|   |   |  a0 | a1 | a2 | a3 | ... | ... | ...  |
|   |   |  a0 | a1 | a2 | a3 | ... | ... | ...  |
|   |   |  : | : | : | : | : | : | :  |

And the block diagram is represented in fig. 2.5.

Finally, case (2b) is a combination of protocol 1 and (2a). The system's evolu


![[Stochastic_Processes_2020_p41_img7.jpeg]]
Figure (2.5) - Block diagram for protocol (2a), with minimum transfer size  $m$  and unlimited bandwidth.

tion is described by:

|  Xn+1 = | Xn +ξn | Xn < m  |
| --- | --- | --- |
|   |  ξn | m ≤ Xn ≤ M  |
|   |  Xn - M +ξn | Xn > M  |

The transition matrix becomes:

|   | 0 | 1 | 2 | ... | m-2 | m-1 | ...  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  0 | a0 | a1 | a2 | ... | ... | ... | ...  |
|  1 | 0 | a0 | a1 | ... | ... | ... | ...  |
|  : | . | . | . | . | . | . | :  |
|  m-1 | 0 | 0 | 0 | ... | 0 | a0 | ...  |
|  m | a0 | a1 | a2 | a3 | ... | ... | ...  |
|  m+1 | a0 | a1 | a2 | a3 | ... | ... | ...  |
|  : | . | . | . | . | . | . | :  |
|  M | a0 | a1 | a2 | a3 | ... | ... | ...  |
|  M+1 | 0 | a0 | a1 | a2 | ... | ... | ...  |
|  M+2 | 0 | 0 | a0 | a1 | ... | ... | ...  |
|  : | . | . | . | . | . | . | :  |

with the block diagram represented in fig. 2.6.

Protocol 2, while more realistic than the version 1, may lead to problem. For example, suppose that we receive too little data to send, and for many consecutive time slots we do not receive any more data. In this situation, the buffer's content will be sent after a lot of time - and so, paradoxically, the optimization we considered to make the system more efficient now leads to a very inefficient behaviour. We can fix this by limiting the maximum number of consecutive empty slots when the queue is not empty. In other words, if we have some data  $(\leq m)$  in the buffer, and do not receive enough data to surpass  $m$  for a certain


![[Stochastic_Processes_2020_p42_img8.jpeg]]
Figure (2.6) - Block diagram for protocol (2b), with minimum transfer size  $m$  and limited bandwidth  $M$ .

number of time slots (e.g. 2), we will send all the buffer's content anyway. This leads to the block diagram of fig. 2.7, where we "replicate states", as we are keeping track of both  $X_{n}$  and a "timeout counter" for sending data.

![[Stochastic_Processes_2020_p42_img9.jpeg]]
Figure (2.7) - Block diagram for protocol 2, with minimum transfer size  $m$  and a "timeout" for sending data of 2 time slots. If the  $m$  threshold is not reached after 2 time slots, then the buffer's content is sent anyway.

# 2.6 First step analysis

A very useful technique for studying Markov chains is the so-called first step analysis, where essentially we study the probabilities conditioned to the initial state, and write recursive relations for the system's state.

For example, consider the Markov chain with transition probability matrix


given by:

$$
\mathbf {P} = \begin{array}{c c c} 0 & 1 & 2 \\ 0 & 1 & 0 \\ 1 & \alpha & \beta \\ 2 & 0 & 1 \end{array} \tag {2.8}
$$

The relative block diagram is represented in fig. 2.8.

![[Stochastic_Processes_2020_p43_img10.jpeg]]
Figure (2.8) - Block diagram for the Markov chain (2.8).

We note that states 0 and 2 do not admit transitions to other states, and so they are called absorbing states: if the system enters one of them, then it can never leave. On the other hand, state 1 does not admit transition from other states, and so is called a transient state: the system can be in state 1 for a time, but after that it will never return there.

We are interested in the general behaviour of the system, and in particular:

- What is the probability that the system will get "trapped" in either state 0 or 2?
- How long will it take to reach one of the absorbing state?

First of all, we define the time of absorption as the minimum number of steps (i.e. minimum time index  $n$ ) needed to reach one of the absorbing states:

$$
T \equiv \min \{n \geq 0: X _ {n} \in \{0, 2 \} \}
$$

The absorption probability of state 0 is given by:

$$
u = \mathbb {P} [ X _ {t} = 0 | X _ {0} = 1 ]
$$

(We need to start from 1, otherwise the system would be already in an absorbing state.)

Finally, we denote with  $\nu$  the average absorption time:

$$
\nu = \mathbb {E} [ T | X _ {0} = 1 ]
$$

In first step analysis we condition the value of a parameter of interest (e.g.  $u$ ) to the possible values  $X_{1}$  that the system can take after the first step. Formally, we use the law of total probability to write:

$$
\begin{array}{l} u = \mathbb {P} [ X _ {t} = 0 | X _ {0} = 1 ] = \\ = \sum_ {k = 0} ^ {2} \mathbb {P} [ X _ {t} = 0 | X _ {0} = 1, X _ {1} = k ] \mathbb {P} [ X _ {1} = k | X _ {0} = 1 ] \\ \end{array}
$$


And then apply the Markovian property to remove all conditions but the latest one:

$$
=\sum_{k=0}^{2}\mathbb{P}[X_{t}=0|X_{1}=k]\mathbb{P}[X_{1}=k|X_{0}=1]
$$

Expanding the sum and using the transition probabilities from (2.8) we have:

$$
=1\cdot\alpha+u\cdot\beta+0\cdot\gamma
$$

We can interpret this result by *imagining* all *possible first steps*, starting from $X_{0}=1$.

- From $X_{0}=1$ we may go to $X_{1}=0$ with probability $\alpha$. In this case we have reached $0$, and so the probability of “reaching $0$ after some time” is $1$ (we already did it!), meaning that $u=1$.
- From $X_{0}=1$ we could also go to $X_{1}=2$ with probability $\gamma$. The latter is an absorbing state, meaning that the system cannot escape it - thus reaching $0$ at a latter time is impossible, and $u=0$.
- In the remaining case, the system is again in $X_{1}=1$, with probability $\beta$. Afterwards, because of the Markovian property, the system “forgets” its past behaviour. So the following step will be *exactly* like the first one we’ve just considered, and in particular the absorption probability $u$ will remain the same.

Note that now we have $u$ also in the rhs. To find it, we just rearrange:

$$
u=\frac{\alpha}{1-\beta}=\frac{\alpha}{\alpha+\gamma}
$$

We can apply a similar reasoning to $\nu$:

$$
\nu =1+\alpha\cdot 0+\beta\cdot\nu+\gamma\cdot 0=
=1+\beta\nu
$$

Here we need to count the first step (the absorption time must be $\geq 1$, as we are not starting in an absorbing state). With probability $\alpha$ and $\gamma$ the system moves to an absorbing state, meaning that no more steps are required to reach them. However, with probability $\beta$ the system remains in $1$, where the expected absorption time is still $\nu$. Rearranging:

$$
\nu=\frac{1}{1-\beta}
$$

We can check this by noting that the amount of time spent in state $1$ has a geometric distribution. Then, as every transition to other states from $1$ leads to an absorbing states, meaning that the absorption time is exactly the time “spent” by the system in state $1$, we have:

$$
\mathbb{P}[T>k|X_{0}=1]=\beta^{k}\Rightarrow\mathbb{E}[T|X_{0}=1]=\sum_{k=0}^{+\infty}\mathbb{P}[T>k|X_{0}=1]=\frac{1}{1-\beta}
$$


However, this direct computation will be impossible in more complex case, while the first-step approach will still remain feasible.

For example, consider the slightly more complex case of a 4-state system:

$$
\mathbf {P} = \begin{array}{c c c c} 0 & 1 & 2 & 3 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 2 & P _ {1 0} & P _ {1 1} & P _ {1 2} \\ 2 & P _ {2 0} & P _ {2 1} & P _ {2 2} \\ 3 & 0 & 0 & 0 \end{array} \tag {2.9}
$$

![[Stochastic_Processes_2020_p45_img11.jpeg]]
Figure (2.9) - Block diagram for the Markov chain (2.9).

As before, we define the absorption time as the minimum time index needed to reach an absorbing state:

$$
T = \min \{n \geq 0: X _ {n} \in \{0, 3 \} \}
$$

We now have two possible initial states, and thus two absorption probabilities (concerning the final state 0):

$$
u _ {i} = \mathbb {P} [ X _ {t} = 0 | X _ {0} = i ] \qquad i = 1, 2
$$

And two averages:

$$
\nu_ {i} = \mathbb {E} [ T | X _ {0} = i ] \qquad i = 1, 2
$$

First-step analysis applied to the initial state 1 leads to:

$$
u _ {1} = 1 \cdot P _ {1 0} + 0 \cdot P _ {1 3} + u _ {1} \cdot P _ {1 1} + u _ {2} \cdot P _ {1 2} \tag {2.10}
$$

Similarly, for initial state 2 we have:

$$
u _ {2} = 1 \cdot P _ {2 0} + 0 \cdot P _ {2 3} + u _ {1} \cdot P _ {2 1} + u _ {2} \cdot P _ {2 2} \tag {2.11}
$$


Equations (2.10) and (2.11) can then be solved to find $u_{1}$ and $u_{2}$.

The same reasoning can be applied to $\nu_{i}$:

$$
\nu_{1} =1+0\cdot(P_{10}+P_{13})+\nu_{1}\cdot P_{11}+\nu_{2}\cdot P_{12}
\nu_{2} =1+0\cdot(P_{20}+P_{23})+\nu_{1}\cdot P_{21}+\nu_{2}\cdot P_{22}
$$

In a more general case, we will have a number of states $0,1,\ldots,N$. Suppose that $0,1,\ldots,r-1$ are transient states, and $r,\ldots,N$ are absorbing. The transition matrix has the form:

$$
\mathbf{P}=\begin{array}[]{c}0\cdots N-r+1\\
N-r\cdots N\end{array}\left(\begin{array}[]{cc}0\cdots N-r+1&N-r\cdots N\\
\mathbf{Q}&\mathbf{R}\\
\mathbf{0}&\mathbf{I}\end{array}\right)
$$

In fact the last $N-r$ states have a certain transition probability only to themselves, and so their rows have $0s$ for the first $r$ entries, and exactly a single $1$ in the rest. The $\mathbf{Q}$ block regulates transition between transient states, while the $\mathbf{R}$ block the ones between transients and absorbing.

As in general there are more than 2 absorbing states, we need to specify which one we are considering for the absorption probabilities:

$u_{i}\equiv U_{ik}$ $=\mathbb{P}[\text{Absorption in }k|X_{0}=i]=\qquad(0\leq i<r)$
$=\sum_{j=0}^{N}\mathbb{P}[\text{Absorption in }k|X_{0}=i,X_{1}=j]P_{ij}=$
$=\underbrace{P_{ik}\cdot 1}_{\text{Abs. state we are
considering}}+\underbrace{\sum_{j=r}^{N}P_{ij}\cdot 0}_{\text{Other
abs. states}}+\underbrace{\sum_{j=0}^{r-1}P_{ij}\cdot u_{j}}_{\text{Transient states}}=$
$=P_{ik}+\sum_{j=0}^{r-1}P_{ij}U_{jk}\qquad i=0,1,\ldots,r-1$

### 2.7 General Absorbing Markov Chain

Consider some kind of metric $g(X)$, as a function mapping each transient state to a real number. We suppose that every time the chain visits a state $j$, the metric rises by the value of $g(j)$. In other words, $g(j)$ is the “reward” earned by the process by visiting $j$.

As before, we label all states so that the first $r$ are transient, and the last $N-r$ are absorbing.

Denoting with $T$ the absorption time for a process starting in state $i$. The


average cumulative value of the metric is given by:

$w_{i}=\mathbb{E}\left[\sum_{n=0}^{T-1}g(X_{n})|X_{0}=i\right]\qquad i=0,\ldots,r-1$

If we choose $g(i)=1\,\forall i$, then the cumulative value of the metric is just the lifetime of a certain realization of the process:

$\sum_{n=0}^{T-1}g(X_{n})=\sum_{n=0}^{T-1}1=T$

And so $\nu_{i}=\mathbb{E}[T|X_{0}=i]$ is the mean time until absorption.

If we instead choose:

$$
g(i)=\begin{cases}1&i=k\\
0&i\neq k\end{cases}
$$

for a transient state $k$, then we are only counting visits to that single state. In this case, $w_{i}$ is the probability of transition $W_{ik}$ from the initial state to the $k$ state.

We can compute the explicit values by first-step analysis:

$$
w_{i}=g(i)+\sum_{j=0}^{r-1}P_{ij}w_{j}\qquad i=0,\ldots,r-1
$$

As the process starts from $i$, the “reward” $g(i)$ is always earned. Then the process moves to a transient state $j$, earning an average reward of $w_{j}$. We get a system of $r$ equations in $r$ unknowns, that can be solved to find all the $\{w_{j}\}_{j=0,\ldots,r-1}$.

In the case of (2.13), i.e. $g(j)=\delta_{jk}$, (2.14) reduces to:

$$
w_{i}=\delta_{ik}+\sum_{j=0}^{r-1}P_{ij}w_{j}
$$

In this case we have $w_{i}=W_{ik}$, and so:

$$
W_{ik}=\delta_{ik}+\sum_{j=0}^{r-1}P_{ij}W_{jk}\qquad\forall i=0,1,\ldots,r-1
$$

### 2.8 Two-State Markov Chain

Consider the Markov Chain with transition matrix:

$$
\mathbf{P} = 
\begin{matrix} 
  & \begin{matrix} 0 & 1 \end{matrix} \\
  \begin{matrix} 0 \\ 1 \end{matrix} & 
  \begin{pmatrix} 1-a & a \\ b & 1-b \end{pmatrix}
\end{matrix}
\qquad 0 < a, b < 1
$$


![[Stochastic_Processes_2020_p48_img12.jpeg]]
Figure (2.10) - Block diagram for the two-state Markov Chain

In this particular case we can compute analytically the  $n$ -step transition matrix:

$$
\mathbf {P} ^ {n} = \frac {1}{a + b} \left( \begin{array}{l l} b & a \\ b & a \end{array} \right) + \frac {(1 - a - b) ^ {n}}{a + b} \left( \begin{array}{c c} a & - a \\ - b & b \end{array} \right) \tag {2.16}
$$

We can rewrite it in a more compact form by introducing:

$$
\mathbf {A} = \left( \begin{array}{c c} b & a \\ b & a \end{array} \right) \qquad \mathbf {B} = \left( \begin{array}{c c} a & - a \\ - b & b \end{array} \right)
$$

So that (2.16) becomes:

$$
\mathbf {P} ^ {n} = (a + b) ^ {- 1} \left[ \mathbf {A} + (1 - a - b) ^ {n} \mathbf {B} \right] \tag {2.17}
$$

Proof. By induction, we start with proving the  $n = 1$  case, and then show that if (2.16) holds up to  $n$ , then it holds also for  $n + 1$ . Explicitly:

$$
\begin{array}{l} \mathbf {P} ^ {1} = \frac {1}{a + b} \left( \begin{array}{c c} b & a \\ b & a \end{array} \right) + \frac {1 - a - b}{a + b} \left( \begin{array}{c c} a & - a \\ - b & b \end{array} \right) = \\ = \frac {1}{a + b} \left( \begin{array}{c c} b + a - a ^ {2} - a b & a - a + a ^ {2} + a b \\ b - b + a b + b ^ {2} & a + b - a b - b ^ {2} \end{array} \right) = \\ = \frac {1}{a + b} \left( \begin{array}{c c} (1 - a) (a + b) & a (a + b) \\ b (a + b) & (1 - b) (a + b) \end{array} \right) = \\ = \left( \begin{array}{c c} 1 - a & a \\ b & 1 - b \end{array} \right) = \mathbf {P} \\ \end{array}
$$

For the induction step:

$$
\mathbf {P} ^ {n + 1} = \mathbf {P} ^ {n} \mathbf {P} \underset {(2. 1 7)} {=} (a + b) ^ {- 1} [ \mathbf {A} + (1 - a - b) ^ {n} \mathbf {B} ] \mathbf {P}
$$

Note that:

$$
\mathbf {A P} = \left( \begin{array}{c c} b & a \\ b & a \end{array} \right) \times \left( \begin{array}{c c} 1 - a & a \\ b & 1 - b \end{array} \right) = \left( \begin{array}{c c} b & a \\ b & a \end{array} \right) = \mathbf {A}
\mathbf {B P} = \left( \begin{array}{c c} a & - a \\ - b & b \end{array} \right) \times \left( \begin{array}{c c} 1 - a & a \\ b & 1 - b \end{array} \right) = (1 - a - b) \mathbf {B}
$$


And so:

$$
\mathbf{P}^{n+1}=(a+b)^{-1}[\mathbf{A}+(1-a-b)^{n+1}\mathbf{B}]=\mathbf{P}^{n+1}\qquad\square
$$

We can now use (2.16) to study the asymptotic behaviour. Suppose that $|1-a-b|<1$ (always true in the non trivial cases $0<a,b<1$), then $|1-a-b|^{n}\xrightarrow[n\to\infty]{}0$, and:

$$
\lim_{n\to\infty}\mathbf{P}^{n}=\frac{1}{a+b}\left(\begin{array}[]{cc}b&a\cr b&a\end{array}\right)
$$

Note that the two rows are equal, meaning that the asymptotic probability distribution does not depend on the initial state: the system will be in state $0$ with probability $b/(a+b)$, and in $1$ with $p=a/(a+b)$. In other words, the system “forgets” its initial condition. As we will see, this is a typical behaviour for many cases of Markov chains.

Packet transmission and the two-state model. One possible application of the two-state model is given by modelling the error rate of a packet transition system with memory. Denote with state $0$ the event of a correct transmission, and with $1$ that of an error. Then the average packet error probability is given by:

$$
P_{e}=\frac{a}{a+b}
$$

Another interesting quantity is the mean length of a burst of errors, i.e. how long (on average) does the system spend in state $1$. The mean length $L$ of such a sequence of erroneous states is a geometric random variable (in the two-state model), whose average is the inverse of the probability of moving out of state $1$:

$$
\langle L\rangle=\frac{1}{P_{10}}=\frac{1}{b}
$$

In a real scenario, we will need to provide redundancy so that the system can tolerate $\langle L\rangle$ consecutive errors.

#### 2.8.1 Markov Chains Defined by Independent r.v.

Let $\xi$ denote a discrete-valued random variable whose possible values are the nonnegative integers and where $\mathbb{P}[\xi_{i}=i]=a_{i}\geq 0$ for $i\in\mathbb{N}$, and $\sum_{i=0}^{n}a_{i}=1$. Let $\xi_{1},\xi_{2},\ldots,\xi_{n},\ldots$ represent independent measurements of $\xi$.

We can use that sequence to construct Markov chains.


1. We let $X_{n}=\xi_{n}$. The probability transition matrix then becomes:

$$
\mathbf{P}=\left[\begin{array}[]{cccc}a_{0}&a_{1}&a_{2}&\cdots\\
a_{0}&a_{1}&a_{2}&\cdots\\
a_{0}&a_{1}&a_{2}&\cdots\\
\vdots&\vdots&\vdots&\ddots\end{array}\right]
$$

All rows are equal because all the $\xi_{n}$ are independent of each other.
2. Successive maxima. We define $X_{n}$ to be the maximum value assumed by the first $n$ r.v. $\xi_{i}$:

$$
X_{n}=\max\{\xi_{1},\ldots,\xi_{n}\}\qquad n=1,2,\ldots
$$

This is a Markov chain. In fact, any future state $X_{n+1}$ is completely determined by the current state $X_{n}$ and the outcome of the next r.v. $\xi_{n+1}$, which is i.i.d.:

$$
X_{n+1}=\max\{X_{n},\xi_{n+1}\}
$$

The transition probability matrix is then:

$$
\mathbf{P}=\left(\begin{array}[]{cccc}A_{0}&a_{1}&a_{2}&a_{3}&\cdots\\
0&A_{1}&a_{2}&a_{3}&\cdots\\
0&0&A_{2}&a_{3}&\cdots\\
0&0&0&A_{3}&\cdots\\
\vdots&\vdots&\vdots&\vdots&\ddots\end{array}\right)
$$

where $A_{k}=\sum_{i=0}^{k}a_{k}$.
3. Partial sums. Similarly to the previous example, we define:

$$
X_{n}=\xi_{1}+\cdots+\xi_{n}\qquad n=1,2,\ldots
$$

with $X_{0}\equiv 0$.

#### 2.8.2 One-Dimensional Random Walks

Consider a particle moving on a line, such that, at any given time, it can only remain in the current state $i$ with probability $r_{i}$, or move to the neighbouring ones with probability $q_{i}$ (left) or $p_{i}$ (right). This process is a special Markov


Chain called a random walk, with transition matrix:

$$
\mathbf {P} = \begin{array}{c c c c c c c c} & 0 & 1 & 2 & & i - 1 & i & i + 1 \\ & 0 & r _ {0} & p _ {0} & 0 & \dots & 0 & 0 & 0 \\ & 1 & q _ {1} & r _ {1} & p _ {1} & \dots & 0 & 0 & 0 \\ & 2 & 0 & q _ {2} & r _ {2} & \dots & 0 & 0 & 0 \\ & \vdots & & & & & & & \\ & i & 0 & 0 & 0 & \dots & q _ {i} & r _ {i} & p _ {i} \\ & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \ddots \end{array} .
$$

To "keep the walk going" we need  $p_i, q_i > 0$ , while  $r_i \geq 0$ . All rows sum to 1, meaning that  $q_i + r_i + p_i = 1 \forall i$ .

Random walks and games. Random walks can be used to model games, by identifying the state  $i$  with the player's score at a given time. If the player wins the next match, their score will go up. Conversely, if they lose, the state will recess. Note that draws can be modelled by the player remaining in the same state.

Similarly, the state can model the amount of resources available to the player (i.e. wealth, or "health points"). If the player runs out of resources, i.e. they reach state 0, then they lose. Conversely, the same holds for the opponent. So the state with maximum resources for the player (i.e.  $N$ ), corresponds to the loss of the opponent. In this situation there are two absorbing states. We will study the asymptotic behaviour in the next sections.

Suppose we are modelling a game's score with a random walk. States 0 and  $N$  correspond respectively to the player losing or winning, and so they are absorbing states. We also suppose that, at each turn, the score always changes.

The transition matrix is then given by:

$$
\mathbf {P} = \begin{array}{c c c c c c} & 0 & 1 & 2 & 3 & \dots & N \\ & 0 & 1 & 0 & 0 & \dots & 0 \\ & 1 & q & 0 & p & 0 & \dots & 0 \\ & 2 & 0 & q & 0 & p & \dots & 0 \\ & \vdots & \vdots & \vdots & \vdots & & \vdots \\ & N & 0 & 0 & 0 & \dots & 1 \end{array}
$$

with  $p + q = 1$

If the initial state (i.e. initial amount of resources) is  $k$ , the average time needed to reach one of the absorbing states is:

$$
T = \min \{n \geq 0; X _ {n} \in \{0, N \} \}
$$

The probability of losing is given by:

$$
u _ {k} = \mathbb {P} [ X _ {t} = 0 | X _ {0} = k ] \tag {2.18}
$$


To compute it, we can use first-step analysis:

$$
u_{k}=pu_{k+1}+qu_{k-1}\qquad k=1,\ldots,N-1
$$

Each step can only lead to the next state (with probability $p$) or to the previous state (with probability $q$). If we start at $0$, then the player instantly loses, i.e. $u_{0}=1$. Conversely, $u_{N}=0$.

To solve the system, we start by rewriting (2.18):

$$
u_{k}=(p+q)u_{k}=pu_{k}+qu_{k}=pu_{k+1}+qu_{k-1}
\Rightarrow q\underbrace{(u_{k}-u_{k-1})}_{x_{k}}=p(u_{k+1}-u_{k})
$$

Then we change variables, introducing:

$$
x_{k}\equiv u_{k}-u_{k-1}
$$

So that (2.19) may be rewritten as:

$$
k=1 0=p(u_{2}-u_{1})-q(u_{1}-u_{0})=px_{2}-qx_{1}
k=2 0=p(u_{3}-u_{2})-q(u_{2}-u_{1})=px_{3}-qx_{2}
\vdots
k=N-1 0=p(u_{N}-u_{N-1})-q(u_{N-1}-u_{N-2})=px_{N}-qx_{N-1}
$$

Note that we can express each $x_{k+1}$ in terms of $x_{k}$, and substitute the result in the successive equation, leading to:

$$
x_{2}=\frac{q}{p}x_{1}\Rightarrow x_{3}=\frac{q}{p}x_{2}=\left(\frac{q}{p}\right)^{2}x_{1}\Rightarrow\cdots\Rightarrow x_{N}=\left(\frac{q}{p}\right)^{N-1}x_{1}
$$

Now we need to *invert* the change of variables. Note that $u_{k}$ is equal to the sum of the first $k$ $\{x_{i}\}$, up to a constant:

$$
\sum_{i=1}^{k}x_{i}=\sum_{i=1}^{k}(u_{i}-u_{i-1})=u_{k}-u_{0}=\underset{(a)}{=}u_{k}-1
$$

where in (a) we used the *first* boundary condition: $u_{0}=1$.
Rearranging:

$$
u_{k}=1+\sum_{i=1}^{k}x_{i}\underset{(2.20)}{=}1+x_{1}\sum_{i=1}^{k}\left(\frac{q}{p}\right)^{i-1}=1+x_{1}\frac{1-(q/p)^{k}}{1-(q/p)}\qquad q\neq p
$$

To compute $x_{1}$ we use the *second* boundary condition $u_{N}=0$:

$$
u_{N}=0\underset{(2.22)}{=}1+x_{1}\frac{1-(q/p)^{N}}{1-(q/p)}\Rightarrow x_{1}=-\frac{1-q/p}{1-(q/p)^{N}}
$$


And substituting back in (2.22) we arrive to the final result:

$$
u_{k}=1-\frac{1-(q/p)^{k}}{\underline{1-(q/p)}}\frac{\underline{1-q/p}}{1-(q/p)^{N}}=\frac{(q/p)^{k}-(q/p)^{N}}{1-(q/p)^{N}}\qquad q\neq p
$$

In the special case of $p=q=1/2$ we go back and directly compute the sum in (2.22):

$$
u_{k}=1+x_{1}\sum_{i=1}^{k}1=1+kx_{1}\qquad p=q
$$

Where $x_{1}$ is obtained from $u_{N}=0$:

$$
u_{N}=0=1+Nx_{1}\Rightarrow x_{1}=-\frac{1}{N}
$$

So that:

$$
u_{k}=1-\frac{k}{N}=\frac{N-k}{N}
$$

In summary, the probability of the player’s losing (i.e. reaching state 0) if the system starts in state $k$ is given by:

$$
u_{k} = \begin{cases}(N-k)/N&p=q=1/2\\
\frac{(q/p)^{k}-(q/p)^{N}}{1-(q/p)^{N}}&p\neq q\end{cases}\qquad k=1,\ldots,N-1
$$

$$
u_{0} = 1
$$

$$
u_{N} = 0
$$

If we fix $k$, a larger $N$ leads to a higher probability of losing $u_{k}$, as the resources $N-k$ available to the opponent rise. Conversely, for $N$ fixed, $u_{k}$ vanishes for large $k$.

If we let $N\to\infty$ (opponent “infinitely rich”, as a casino), then:

$$
u_{k}\xrightarrow[N\to\infty]{}\begin{cases}1&p\leq q\\
(q/p)^{k}&p>q\end{cases}
$$

This means that if the player is at a disadvantage ($p<q$), then there they will certainly lose. However, if the player is likely to win each game ($p>q$), then they may (in principle) continue playing indefinitely. However, note that for any finite $k$ there is still a finite non-zero probability of losing nonetheless, equal to $(q/p)^{k}$, that vanishes for $k\to+\infty$.
Note that the player will certainly lose even if the game is fair ($p=q$). This can be intuitively understood by looking at fig. 2.11.


![[Stochastic_Processes_2020_p54_img13.jpeg]]
Figure (2.11) - The ratio  $p / q$  defines the slope of the trend followed by the player's score. If  $p / q < 1$ , the player will certainly lose after some time. If  $p / q = 1$  (fair game), the average player's score remains fixed to that of the initial state, and given infinite time a sufficiently high fluctuation will bring the player to ruin. If  $p / q > 1$ , the player can still lose the game, but on average their score will rise, making their situation "safer".

# 2.8.3 Success Runs

Consider the Markov Chain with the following transition matrix:

|   | 0 | 1 | 2 | 3 | 4 | ...  |
| --- | --- | --- | --- | --- | --- | --- |
|  0 | p0 | q0 | 0 | 0 | 0 | ...  |
|  1 | p1 | r1 | q1 | 0 | 0 | ...  |
|  2 | p2 | 0 | r2 | q2 | 0 | ...  |
|  3 | p3 | 0 | 0 | r3 | q3 | ...  |
|  : | : | : | : | : | : | ...  |

Starting at state  $i$ , the system can move to  $i + 1$  with probability  $q_{i}$ , remain at  $i$  with probability  $r_{i}$ , or go back to the starting line at state 0 with probability  $p_{i}$ .

![[Stochastic_Processes_2020_p54_img14.jpeg]]
Figure (2.12) - Block diagram for the success run Markov Chain

Timeouts. This kind of chain can be used to model, for example, timeout processes - that is processes where a reset happens after a certain time, except when something else prevents it.


We apply this kind of model to a layer 2 protocol $^2$ , where we want to send data packets between nodes connected by a link. The receiving node confirms the success of transmission by returning an acknowledgment message. If this does not happen, the packet needs to be re-transmitted. In practice, this is done for a maximum of  $L + 1$  total trials (including the first transmission), after which the packet is discarded (otherwise the system would be clogged with untransmitted data).

In particular, we denote with  $X_{n}$  the number of failed transmissions of a packet. At every state  $i < L$ , there can be another transmission failure with probability  $\epsilon$ , leading to state  $i + 1$ , or the packet can be correctly sent with probability  $1 - \epsilon$ , leading to the final state  $S$  (success), after which the process stops. If the system reaches  $L$  and fails one more time, then it will evolve to the final state  $F$ , where data is discarded, and no more trials are done.

The transition probability matrix is given by:

![[Stochastic_Processes_2020_p55_img15.jpeg]]

![[Stochastic_Processes_2020_p55_img16.jpeg]]
Figure (2.13) - Block diagram for the layer 2 protocol

We are interested in the probability of the chain being absorbed in  $S$ , given it started in state  $i$ . This can be computed by first-step analysis:

$$
u _ {i} = \mathbb {P} [ X _ {T} = S | X _ {0} = i ] =
= \sum_{j=0}^{L} P_{ij} u_j + P_{iS} \cdot 1 + P_{iF} \cdot 0 = \begin{cases} \epsilon u_{i+1} + 1 - \epsilon & i < L \\ 1 - \epsilon & i = L \end{cases}
$$

Note that we know $u_L$, and from $u_{i+1}$ we can determine $u_i$. So we can start at the last state, and work our way backwards to the start:

$$
\begin{aligned}
u_0 &= \epsilon u_1 + 1 - \epsilon = \epsilon (\epsilon u_2 + 1 - \epsilon) + 1 - \epsilon = \\
&= \epsilon^2 u_2 + (1 - \epsilon) \epsilon + (1 - \epsilon) = \\
&= \epsilon^L u_L + \sum_{j=0}^{L-1} \epsilon^j (1 - \epsilon) = \\
&= \epsilon^L (1 - \epsilon) + (1 - \epsilon) \frac{1 - \epsilon^L}{1 - \epsilon} = 1 - \epsilon^{L+1}
\end{aligned}
$$

This makes sense, as the probability of having at least a success in $L + 1$ trials is equal to the probability of not failing $L + 1$ consecutive times, which is $1 - \epsilon^{L+1}$.

The average number of attempts per packet is just the mean time for absorption:

$$
\nu_i = \epsilon v_{i+1} + 1 \quad i < L
$$

and $\nu_L = 1$. As before, we iterate:

$$
\begin{aligned}
\nu_0 &= \epsilon \nu_1 + 1 = \epsilon (\epsilon \nu_2 + 1) + 1 = \epsilon^2 \nu_2 + \epsilon + 1 = \\
&= \epsilon^3 \nu_3 + \epsilon^2 + \epsilon + 1 = \epsilon^L \nu_L + \sum_{j=0}^{L-1} \epsilon^j = \\
&= \epsilon^L + \frac{1 - \epsilon^L}{1 - \epsilon} = \frac{\epsilon^L - \epsilon^{L+1} + 1 - \epsilon^L}{1 - \epsilon} = \frac{1 - \epsilon^{L+1}}{1 - \epsilon}
\end{aligned}
$$

Let's consider a sequence of transmissions. Each packet has a probability $u_0 = 1 - \epsilon^{L+1}$ of being correctly sent, and so the average number of packets sent is $u_0$. The mean sending time is $\nu_0 = (1 - \epsilon^{L+1}) / (1 - \epsilon)$. The ratio of these two averages is the mean **throughput** of the channel:

$$
\mathrm{Throughput} = \frac{u_0}{\nu_0} = 1 - \epsilon
$$

We will prove this *intuitive* result in a later section.

## 2.8.4 First Passage Times

We define the first passage time $\theta_{ij}$ from state $i$ to $j$ as the number of transitions to reach $j$ from $i$ for the first time. Its distribution is given by:

$$
\mathbb{P}[\theta_{ij} = u] = f_{ij}(u) = \mathbb{P}[X_n = j, X_m \neq j, m = 1, \dots, n - 1 | X_0 = i]
$$

Note that we are interested in events where $j$ is the last state, and it has not been visited before. So, in other words, $\theta_{ij}$ is the number of transitions from $i$


to states *different* from $j$ needed to reach $j$ for the first time.

We then define $f_{ij}(0)\equiv 0$ $\forall i\neq j$, as the probability of reaching $j$ from a different state *without moving* is obviously null.

We can compute $f_{ij}$ by first-step analysis:

$$
f_{ij}(n)=P_{ij}\delta(n-1)+\sum_{i\neq j}P_{ik}f_{kj}(n-1)\qquad\delta(n)=\begin{cases}1&n=0\\
0&n\neq 0\end{cases}
$$

In fact, $f_{ij}$ is $P_{ij}$ if $n=1$, i.e. if we are asking the probability of $i\to j$ in one step. Otherwise, the system has to go to a different state $k\neq i$ (with probability $P_{ik}$), where the first passage time to $j$ becomes $f_{kj}(n-1)$ (as we have done already a step). By reiterating (2.24) we can express $f_{ij}(n)$, for any $n$, as a only a function of $\mathbf{P}$.

For example, let’s do this for the two-state chain, where the transition matrix is:

$$
\mathbf{P}=\left(\begin{array}[]{cc}1-a&a\\
b&1-b\\
\end{array}\right)
$$

Suppose the system starts at $0$, and we are interested in the first passage time to $1$. Expanding (2.24) leads to:

$$
f_{01}(n)=P_{01}\delta(n-1)+P_{00}f_{01}(n-1)=\begin{cases}a&n=1\\
(1-a)f_{01}(n-1)&n>1\end{cases}
$$

Then:

$$
f_{01}(2) =a(1-a)
f_{01}(3) =a(1-a)^{2}
\Rightarrow f_{01}(n) =(1-a)^{n-1}a\qquad n\geq 1
$$

Similarly:

$$
f_{11}(n) =P_{11}\delta(n-1)+P_{10}f_{01}(n-1)=
=(1-b)\delta(n-1)+bf_{01}(n-1)\underset{(2.25)}{=}\begin{cases}1-b&n=1\\
ab(1-a)^{n-2}&n>1\end{cases}
$$

And we can compute $f_{10}$ and $f_{00}$ by substituting $a\leftrightarrow b$ in $f_{01}$ and $f_{11}$ (by symmetry).

All these results are rather obvious in the case of the two-state model, as they can be computed by using the geometric distribution. For example, $f_{10}(n)$ is equal to the probability of reaching $0$ from $1$ after exactly $n$ steps, which is equivalent to the probability of *not leaving* $0$ for $n-1$ steps (which is $(1-a)^{n-1}$), and then leaving it on the last step (which is $a$).


Similarly, for $f_{11}(n)$ we first need to move to $0$ (probability $a$), remain there for $n-2$ steps (probability $(1-a)^{n-2}$) and finally return to $0$ (probability $b$). Clearly, this kind of explicit reasoning is only possible in this case, because there are only two states. In a general situation, first-step analysis is required.

First passage times are closely related with multi-step transition probabilities. For example, suppose we are interested in the probability of finding a process in state $j$ after $n$ steps, given it started at state $X_{0}=i$.

We can then consider all the paths that reach $j$ for the first time in $m\leq n$ steps, and then transition from $j$ to $j$ in the remaining $m-n$ steps. Note that all these paths are disjoint events, as each path can reach $j$ for the first time only once!

Then:

$$
P_{ij}^{(n)}=\sum_{m=1}^{n}f_{ij}(m)P_{jj}^{(n-m)}\qquad n\geq 1
$$

As we know $P_{ij}^{(n)}$ for any $n$ from $\mathbf{P}$, we can then compute $f_{ij}(m)$ by solving a system of $n$ equations.

We can make the problem a bit simpler by highlighting the last term in the sum:

$$
P_{ij}^{(n)}=\sum_{m=1}^{n-1}f_{ij}(m)P_{jj}^{(n-m)}+f_{ij}(n)
$$

Rearranging:

$$
f_{ij}(n)=\begin{cases}0&n=0\\
P_{ij}&n=1\\
P_{ij}^{(n)}-\sum_{m=1}^{n-1}f_{ij}(m)P_{jj}^{(n-m)}&n\geq 2\end{cases}
$$

which can be solved by recursion.

Note that computing $f_{ij}(n)$ in this way does not require $f_{kj}(m)$ $\forall m<n$ and $\forall k\neq j$ (unlike the first-step analysis method), but only $f_{ij}(m)$ $\forall m<n$. However, we need all powers $\mathbf{P}^{m}$ for $m<n$. So, at the end, the computational complexity is of the same order.

Often, however, we are interested merely in the moments of $\theta_{ij}$, and not in the full statistics $f_{ij}$. We start by noting that:

$$
\theta_{ij}=\begin{cases}1&\text{with prob. }P_{ij}\\
1+\theta_{kj}&\text{with prob. }P_{ik},\,k\neq j\end{cases}
$$

In fact, if we reach $j$ in only one step (which happens with probability $P_{ij}$), then $\theta_{ij}=1$. Otherwise, with probability $P_{ik}$ we will travel to another state $k\neq j$, meaning that the first passage time $i\rightarrow j$ will be $1$ (as we already did a step) plus the number $\theta_{kj}$ of steps yet to make from $k$.


Averaging both sides of (2.27) leads to:

$$
\mathbb{E}[\theta_{ij}] =P_{ij}+\sum_{k\neq j}^{N}P_{ik}(1+\mathbb{E}[\theta_{kj}])=
=\underbrace{\sum_{k=0}^{N}P_{ik}}_{1}+\sum_{k\neq j}^{N}P_{ik}\mathbb{E}[\theta_{kj}]=
\underset{(a)}{=}1+\sum_{k\neq j}^{N}P_{ik}\mathbb{E}[\theta_{kj}]\qquad\forall i,j
$$

where in (a) we used the fact that all rows of $\mathbf{P}$ sum to $1$ due to normalization.

For a fixed $j$, we have $N+1$ possible values for $i$, so we can write $N+1$ independent equations. These can then be solved to determine all the $\mathbb{E}[\theta_{ij}]$. More precisely, note that $\mathbb{E}[\theta_{jj}]$ does not appear in the rhs of (2.28), and so we have only $N$ equations to solve:

$$
\mathbb{E}[\theta_{ij}]=1+\sum_{k\neq j}P_{ik}\mathbb{E}[\theta_{kj}]\qquad i\neq j
$$

After having found all the $\mathbb{E}[\theta_{ij}]$ for $i=0,\ldots,N$ and $i\neq j$, we can then compute:

$$
\mathbb{E}[\theta_{jj}]=1+\sum_{k\neq j}P_{jk}\mathbb{E}[\theta_{kj}]
$$

For example, in the two-state model we have:

$$
\mathbb{E}[\theta_{01}]=1+P_{00}\mathbb{E}[\theta_{01}]\Rightarrow\mathbb{E}[\theta_{01}]=\frac{1}{1-P_{00}}=\frac{1}{a}
\mathbb{E}[\theta_{10}]=1+P_{11}\mathbb{E}[\theta_{10}]\Rightarrow\mathbb{E}[\theta_{10}]=\frac{1}{1-P_{11}}=\frac{1}{b}
$$

And then we can compute the cases with $i=j$:

$$
\mathbb{E}[\theta_{00}]=1+P_{01}\mathbb{E}[\theta_{10}]=1+\frac{a}{b}=\frac{a+b}{b}=\left(\frac{b}{a+b}\right)^{-1}
\mathbb{E}[\theta_{11}]=1+P_{10}\mathbb{E}[\theta_{01}]=1+\frac{b}{a}=\frac{a+b}{a}=\left(\frac{a}{a+b}\right)^{-1}
$$

Note that $\mathbb{E}[\theta_{00}]$ and $\mathbb{E}[\theta_{11}]$ are the reciprocals of the long-run probabilities of remaining respectively in state $0$ or $1$. Intuitively, if the system returns from state $0$ to state $0$ after, on average, $(a+b)/b$ time units, then the fraction of time spent on state $0$ is the inverse of that quantity - because the systems visit $0$ “once every $\mathbb{E}[\theta_{00}]$” steps. This kind of result is actually a property of many Markov Chains, as we will see in a later section.
$$
\mathbf{P} = 
￼\begin{array}{c|cc}
  & 0 & 1 \\
\hline
0 & 1-a & a \\
1 & b & 1-b
\end{array}
\qquad 0 < a, b < 1
$$
$$
\mathbf{P} = 
￼\begin{array}{c|cc}
  & 0 & 1 \\
\hline
0 & 1-a & a \\
1 & b & 1-b
\end{array}
\qquad 0 < a, b < 1
$$
For second moments we have:

$$
\mathbb{E}[\theta_{ij}^{2}]=P_{ij}\cdot 1^{2}+\sum_{k\neq j}^{N}P_{ik}\mathbb{E}[(1+\theta_{kj})^{2}]=
$$
Expanding the square:
$$
=\underbrace{P_{ij}+\sum_{k\neq j}^{N}P_{ik}}_{1}+2\sum_{k\neq j}^{N}P_{ik}\mathbb{E}[\theta_{kj}]+\sum_{k\neq j}^{N}P_{ik}\mathbb{E}[\theta_{kj}^{2}]=
\underset{(2.28)}{=}1+2(\mathbb{E}[\theta_{ij}]-1)+\sum_{k\neq j}^{N}P_{ik}\mathbb{E}[\theta_{kj}^{2}]=
=2\mathbb{E}[\theta_{ij}]-1+\sum_{k\neq j}P_{ik}\mathbb{E}[\theta_{kj}^{2}]
$$

In the two-state case this becomes:

$$
\mathbb{E}[\theta_{01}^{2}]=2\mathbb{E}[\theta_{01}]-1+P_{00}\mathbb{E}[\theta_{01}^{2}]\Rightarrow\mathbb{E}[\theta_{01}^{2}]=\frac{2\mathbb{E}[\theta_{01}]-1}{1-P_{00}}=\frac{2/a-1}{a}=\frac{2}{a^{2}}-\frac{1}{a}
$$

And so:

$$
\mathrm{Var}(\theta_{01})=\frac{1-a}{a^{2}}
$$

which is exactly the same result we could get by reasoning with the geometric distribution.
Similarly:

$$
\mathbb{E}[\theta_{10}^{2}]=2\mathbb{E}[\theta_{10}]-1+P_{11}\mathbb{E}[\theta_{10}^{2}]\Rightarrow\mathrm{Var}(\theta_{10})=\frac{1-b}{b^{2}}
$$

For the $i=j$ case we have, for example:

$$
\mathbb{E}[\theta_{00}^{2}] =2\mathbb{E}[\theta_{00}]-1+P_{01}\mathbb{E}[\theta_{10}^{2}]=2\left(1+\frac{a}{b}\right)-1+a\left(\frac{2}{b^{2}}-\frac{1}{b}\right)=
=1+\frac{a}{b}+\frac{2a}{b^{2}}
\mathrm{Var}(\theta_{00}) =\mathbb{E}[\theta_{00}^{2}]-\mathbb{E}[\theta_{00}]^{2}=1+\frac{a}{b}+\frac{2a}{b^{2}}-\left(1+\frac{2a}{b}+\frac{a^{2}}{b^{2}}\right)=
=\frac{2a-a^{2}}{b^{2}}-\frac{a}{b}=\frac{a(2-a-b)}{b^{2}}
$$

### 2.9 Alternative First Step Analysis

All the results we obtained from first-step analysis (the average number of first passage times to a state, the mean absorption time, and the absorption probabilities) can be re-derived by using the $n$-step probability matrix, at the cost of a lengthier computation. The idea is to compute the value of each of these quantities for a $n$-long evolution, and then study the asymptotic behaviour for


$n\to\infty$.

Consider a (general) Markov chain with states $N+1$ states labelled as $0,1,\ldots,N$. Suppose that the first $r$ ones (i.e. $0,1,\ldots,r-1$) are transient - meaning that, given a sufficient time, the system does not visit them anymore, and so $P_{ij}^{(n)}\xrightarrow[n\to\infty]{}0$ for $0\leq i,j<r$ - while the remaining states $(r,\ldots,N)$ are absorbing - i.e. the system cannot escape them ($P_{ii}=1$ for $r\leq i\leq N$).

The resulting transition matrix can be decomposed in 4 blocks:

$$
\mathbf{P}=\left(\begin{array}[]{cc}\mathbf{Q}&\mathbf{R}\\
\mathbf{O}&\mathbf{\mathbb{1}}\end{array}\right)
$$

We now compute explicitly the $n$-step transition matrix, i.e. the $n$-th power of $\mathbf{P}$. We start from the $n=2$ case:

$$
\mathbf{P}^{2}=\left(\begin{array}[]{cc}\mathbf{Q}^{2}&\mathbf{R}+\mathbf{Q}\mathbf{R}\\
\mathbf{O}&\mathbf{\mathbb{1}}\end{array}\right)
$$

And for $n=3$ we have:

$$
\mathbf{P}^{3}=\left(\begin{array}[]{cc}\mathbf{Q}&\mathbf{R}\\
\mathbf{O}&\mathbf{\mathbb{1}}\end{array}\right)\times\left(\begin{array}[]{cc}\mathbf{Q}^{2}&\mathbf{R}+\mathbf{Q}\mathbf{R}\\
\mathbf{O}&\mathbf{\mathbb{1}}\end{array}\right)=\left(\begin{array}[]{cc}\mathbf{Q}^{3}&\mathbf{R}+\mathbf{Q}\mathbf{R}+\mathbf{Q}^{2}\mathbf{R}\\
\mathbf{O}&\mathbf{\mathbb{1}}\end{array}\right)
$$

Generalizing, we arrive to:

$$
\mathbf{P}^{n}=\left(\begin{array}[]{cc}\mathbf{Q}^{n}&(\mathbf{\mathbb{1}}+\mathbf{Q}+\cdots+\mathbf{Q}^{n-1})\mathbf{R}\\
\mathbf{O}&\mathbf{\mathbb{1}}\end{array}\right)
$$

Suppose now that the system starts in state $i$, and makes a total of $n$ transitions. Given this time window, the mean number of visits to a certain state $j$ is given by:

$$
W_{ij}^{(n)}=\mathbb{E}\left[\sum_{l=0}^{n}\mathbf{1}\{X_{l}=j\}|X_{0}=i\right]\qquad\mathbf{1}\{X_{l}=j\}=\begin{cases}1&X_{l}=j\\
0&X_{l}\neq j\end{cases}
$$

and $\mathbf{1}(A)$ is the indicator function of the set $A$.

Bringing the expectation inside the sum (by linearity), and noting that $\mathbb{E}[\mathbf{1}\{X_{l}=j\}|X_{0}=i]=\mathbb{P}\{X_{l}=j|X_{0}=i\}=P_{ij}^{(l)}$, we get:

$W_{ij}^{(n)}=\sum_{l=0}^{n}\mathbb{E}[\mathbf{1}\{X_{l}=j\}|X_{0}=i]=\sum_{l=0}^{n}P_{ij}^{(l)}$ (2.30)

This expression holds for any pair of states $i$ and $j$. However, if the initial state $i$ is absorbing, the evolution of the chain is trivial (nothing changes), while if $j$ is absorbing the mean number of visit will be either 0 (if the state is never reached), or something diverging with $n$ (because if $j$ is reached, then the system will never leave it). So the only real interesting case is when $i$ and


$j$ are both transient, meaning that $0\leq i,j<r$ and so $P_{ij}^{(l)}=Q_{ij}^{(l)}$:

$W_{ij}^{(n)}=Q_{ij}^{(0)}+Q_{ij}^{(1)}+\cdots+Q_{ij}^{(n)}\qquad 0\leq i,j<r$

with:

$$
Q_{ij}^{(0)}=\begin{cases}1&i=j\\
0&i\neq j\end{cases}
$$

We can rewrite this in matrix notation as:

$\mathbf{W}^{(n)}$ $=\mathbb{1}+\mathbf{Q}+\mathbf{Q}^{2}+\cdots+\mathbf{Q}^{n}=$ (2.31)
$=\mathbb{1}+\mathbf{Q}(\mathbb{1}+\mathbf{Q}+\cdots+\mathbf{Q}^{n-1})=$
$=\mathbb{1}+\mathbf{Q}\mathbf{W}^{(n-1)}$ (2.32)

In terms of matrix entries:

$W_{ij}^{(n)}=\delta_{ij}+\sum_{k=0}^{r-1}Q_{ik}W_{kj}^{(n-1)}=\delta_{ij}+\sum_{k=0}^{r-1}P_{ik}W_{kj}^{(n-1)}$

In other words, the mean number of visits $W_{ij}^{(n)}$ to state $j$ in the first $n$ transitions starting from initial state $i$ includes the initial visit if $i=j$, and the future visits during the $n-1$ remaining steps - each weighted by the appropriate transition probabilities.

If we let $n\to\infty$, $W_{ij}^{(n)}$ becomes the (average) count of the total number of visits to state $j$ - because the system will definitely be trapped in an absorbing state given a sufficient time:

$W_{ij}\equiv\lim_{n\to\infty}W_{ij}^{(n)}=\mathbb{E}[\text{Total visits to }j|X_{0}=i]\qquad 0\leq i,j<r$

Clearly $\lim_{n\to\infty}\mathbf{W}^{(n)}=\lim_{n\to\infty}\mathbf{W}^{(n-1)}\equiv\mathbf{W}$, and so (2.32) leads to:

$\mathbf{W}=\mathbb{1}+\mathbf{Q}\mathbf{W}$ (2.33)

In terms of entries, this is the same result that was previously obtained through first-step analysis in (2.15, pag. 47):

$W_{ij}=\delta_{ij}+\sum_{l=0}^{r-1}P_{il}W_{li}\qquad\forall i,j=0,\ldots,r-1$ (2.34)

We can explicitly solve (2.33) by rearranging:

$\mathbf{W}-\mathbf{Q}\mathbf{W}=(\mathbb{1}-\mathbf{Q})\mathbf{W}=\mathbb{1}\Rightarrow\mathbf{W}=(\mathbb{1}-\mathbf{Q})^{-1}$

When taking the limit $n\to\infty$ of (2.30) we can *stop* the sum at the instant $T$ of absorption. That is, let $T$ be the number of steps required, for a specific evolution $X_{n}$, to go from initial state $i$ to *any* absorbing state $r,\ldots,N$ for the


first time:

$$
T = \min \{n \geq 0; r \leq X _ {n} \leq N \}
$$

Then:

$$
W _ {i j} = \lim  _ {n \rightarrow \infty} W _ {i j} ^ {(n)} = \mathbb {E} \left[ \sum_ {n = 0} ^ {T - 1} \mathbf {1} \{X _ {n} = j \} \mid X _ {0} = i \right] \quad 0 \leq i, j <   r \tag {2.35}
$$

In fact, for every  $n \geq T$ , we have  $r \leq X_n \leq N$ , and so clearly  $X_n \neq j$ , meaning that  $\mathbf{1}\{X_n = j\} = 0$ .

Note that, before absorption, the system evolves only through transient states, and so:

![[Stochastic_Processes_2020_p63_img17.jpeg]]

So, if we sum over all transient states in (2.35) and apply linearity:

$$
\begin{array}{l} \sum_ {j = 0} ^ {r - 1} W _ {i j} = \sum_ {j = 0} ^ {r - 1} \mathbb {E} \left[ \sum_ {n = 0} ^ {T - 1} \mathbf {1} \{X _ {n} = j \} | X _ {0} = i \right] = \\ = \mathbb {E} \left[ \sum_ {j = 0} ^ {r - 1} \sum_ {n = 0} ^ {T - 1} \mathbf {1} \{X _ {n} = j \} | X _ {0} = i \right] = \\ \underset {(2. 3 6)} {=} \mathbb {E} [ T | X _ {n} = j ] \equiv \nu_ {i} \quad 0 \leq i <   r \tag {2.37} \\ \end{array}
$$

where  $\nu_{i}$  represents the mean time to absorption for a system starting in state  $i$ .

All that's left is to substitute the expression for  $W_{ij}$  found in (2.34) in (2.37):

$$
\begin{array}{l} \nu_ {i} = \sum_ {j = 0} ^ {r - 1} W _ {i j} \underset {(2. 3 4)} {=} \underbrace {\sum_ {j = 0} ^ {r - 1} \delta_ {i j}} _ {1} + \sum_ {j = 0} ^ {r - 1} \sum_ {k = 0} ^ {r - 1} P _ {i k} W _ {k j} \quad i = 0, 1, \ldots , r - 1 = \\ = 1 + \sum_ {k = 0} ^ {r - 1} P _ {i k} \nu_ {k} \quad i = 0, 1, \dots , r - 1 \tag {2.38} \\ \end{array}
$$

which is again the same result that can be obtained by first-step analysis.

In matrix form, denoting with  $\pmb{\nu} = (\nu_{0},\dots,\nu_{r - 1})^{T}$  and with  $\mathbf{1} = (1,\ldots ,1)^T\in$ $\mathbb{R}^{r - 1}$ , (2.38) becomes:

$$
\boldsymbol {\nu} = \mathbf {W} \times \mathbf {1} = (\mathbb {1} - \mathbf {Q}) ^ {- 1} \times \mathbf {1} \tag {2.39}
$$

Note that matrix multiplication with a column vector of ones results in a column


vector with entries equal to the sum of all entries in each row of the original matrix.

Finally, we can study the probabilities of the system being absorbed by a certain state $k\in\{r,\ldots,N\}$. As before, we start by focusing only on the first $n$ steps, i.e. on the probability $U^{(n)}_{ik}$ of the system being absorbed in state $k$ during the first $n$ steps given it started at $i$. As state $k$, once entered, cannot be left, if the system reaches it before the $n$-th step then $X_{n}=k$, and so $U^{(n)}_{ik}$ is just the $n$-step probability of reaching $k$ from $i$:

$U^{(n)}_{ik}=P^{(n)}_{ik}=\mathbb{P}\{X_{n}=k|X_{0}=i\}$

Equivalently, we can focus on the state reached after the absorption time $T$:

$U^{(n)}_{ik}=\mathbb{P}\{T\leq n\wedge X_{T}=k|X_{0}=i\}\qquad\forall 0\leq i<r;\,r\leq k\leq N$

As $i$ is transient and $k$ is absorbing, we know the form of $P^{(n)}_{ik}$ from (2.29), and so, in matrix form:

$\mathbf{U}^{(n)}=(\mathbb{1}+\mathbf{Q}+\cdots+\mathbf{Q}^{n-1})\mathbf{R}\underset{(2.31)}{\equiv}\mathbf{W}^{(n-1)}\mathbf{R}$ (2.40)

Then we take the limit $n\to\infty$, obtaining the absorption probabilities $U_{ik}$ (also called hitting probabilities, as $U_{ik}$ is the probability of “hitting” the final state $k$):

$U_{ik}\equiv\lim_{n\to\infty}U^{(n)}_{ik}=\mathbb{P}\{X_{T}=k|X_{0}=i\}\quad\forall 0\leq i<r;\,r\leq k\leq N$

And from the limit of (2.40) we have:

$\mathbf{U}=\mathbf{W}\mathbf{R}\Leftrightarrow U_{ik}=\sum_{j=0}^{r-1}W_{ij}R_{jk}\quad 0\leq i<r;\,r\leq k\leq N$

#### 2.9.1 A matrix approach for average fpt

We can now elaborate a matrix approach for computing the average first passage times from any state $i\neq N$ to state $N$. The idea is to consider the $N$-th state as absorbing - discarding all the chain evolution after reaching $N$ for the first time.

Explicitly, we start from a transition matrix $\mathbf{P}$ in the form of:

$$
\mathbf{P}=\begin{array}[]{c c c}0\cdots N-1&N\\
0&\mathbf{Q}&{\bf r}\\
N&\*&\*&\end{array}
$$


and replace the last row with:

$$
\hat {\mathbf {P}} = \begin{array}{c c} 0 \dots N - 1 & N \\ \mathbf {Q} & \mathbf {r} \\ 0 & 1 \end{array} \tag {2.42}
$$

In the expressions above, $\mathbf{Q}$ is a $N\times N$ matrix, $\pmb{r}$ is a $N\times 1$ vector, and $\mathbf{0}$ is $1\times N$.

Note that (2.41) and (2.42) describe exactly the same system until state $N$ is visited, and so are completely equivalent in the regime we are interested on. However, the average first arrival time $\mathbb{E}[\theta_{iN}]$ from any state $i$ to $N$ in (2.41) is exactly the mean absorption time $\nu_{i}$ from state $i$ in (2.42):

$$
\mathbb {E} [ \theta_ {i N} ] = \nu_ {i}
$$

which can then be computed using (2.39):

$$
\boldsymbol {\nu} \equiv \left[ \begin{array}{c} \nu_ {0} \\ \dots \\ \nu_ {N - 1} \end{array} \right] = (\mathbb {1} - \mathbf {Q}) ^ {- 1} \times \mathbf {1}
$$

Finally, note that there is nothing special about the choice of state $N$ - we can always relabel states so that the one we are interested on is the $N$-th.


