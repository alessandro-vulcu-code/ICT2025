# Chapter 5 - Renewal Phenomena

## Table of Contents

- [[#5.1 Renewal Processes|5.1 Renewal Processes]]
- [[#5.2 Examples of Renewal Processes|5.2 Examples of Renewal Processes]]
  - [[#Processes Associated with queues|Processes Associated with queues]]
- [[#5.3 The Poisson Process|5.3 The Poisson Process]]
  - [[#The Renewal Function  $\\mathbf{N}(t)$|The Renewal Function $\\mathbf{N}(t)$]]
  - [[#Excess Life  $\\gamma_{t}$|Excess Life $\\gamma_t$]]
  - [[#Current Life  $\\delta_t$|Current Life $\\delta_t$]]
  - [[#Joint Distribution of  $\\gamma_{t}$  and  $\\delta_t$|Joint Distribution of $\\gamma_t$ and $\\delta_t$]]
  - [[#Mean Total Life $\\mathbb{E}[\\beta_t]$|Mean Total Life $\\mathbb{E}[\\beta_t]$]]
  - [[#5.3.1 The sampling paradox|5.3.1 The sampling paradox]]
  - [[#Bus Stop - Example|Bus Stop - Example]]
- [[#5.4 Long run Behaviour|5.4 Long run Behaviour]]
  - [[#The Renewal Function|The Renewal Function]]
- [[#5.5 The Renewal Argument|5.5 The Renewal Argument]]
  - [[#Applications - $\\mathbb{E}[S_{N(t)+1}]$|Applications - $\\mathbb{E}[S_{N(t)+1}]$]]
- [[#5.6 The Elementary Renewal Theorem|5.6 The Elementary Renewal Theorem]]
  - [[#5.6.1 The Basic Renewal Theorem|5.6.1 The Basic Renewal Theorem]]
  - [[#Asymptotic results of N(t)|Asymptotic results of N(t)]]
  - [[#Asymptotic results of Age and Excess Life|Asymptotic results of Age and Excess Life]]
  - [[#5.6.2 Delayed Renewal Processes|5.6.2 Delayed Renewal Processes]]
  - [[#5.6.3 Alternating Renewal Process|5.6.3 Alternating Renewal Process]]
  - [[#5.6.4 Proof of basic limit theorem for M.C.|5.6.4 Proof of basic limit theorem for M.C.]]
- [[#5.7 Renewal Reward Processes|5.7 Renewal Reward Processes]]
  - [[#5.7.1 Regenerative processes|5.7.1 Regenerative processes]]
- [[#5.8 Semi-Markov Processes|5.8 Semi-Markov Processes]]
  - [[#5.8.1 Some clarifications on Regenerative and Semi-Markov Processes|5.8.1 Some clarifications on Regenerative and Semi-Markov Processes]]
  - [[#5.8.2 Semi-Markov process probabilities|5.8.2 Semi-Markov process probabilities]]
- [[#Summary Table|Summary Table]]

---

In renewal phenomena we can always find a time called renewal or regeneration time. This is a special time for which the process, in a statistical sense, begins anew, i.e. starts from scratch.
![[Stochastic_Processes_2020_p174_img61.jpeg]]
*Figure 5.1 - In a renewal process, every time that a renewal occurs we can consider as if the process anew starts.*

 What happens is that we are looking into a phenomenon that starts from time 0. After some random time, an event occurs. In order to characterize the evolution of the system from the starting point, we need to describe the distribution according to which events occur. But the peculiarity of renewal phenomena is that, given that an event has occurred, the future statistics from that moment on will be identical to the one that started from time 0.

 Summarizing: any time there is an event, the system renews itself and statistically the evolution of the system starting from any of these events is indistinguishable. The renewal property comes from the fact that the times between two consecutive events are independent and identically distributed. The renewal theory essentially studies the times that passes between two consecutive events, and the properties that such class of functions of i.d.d., nonnegative random variables shares among its members.

## 5.1 Renewal Processes

> [!Important] Definition - Renewal Counting Process
> **Statement:** A renewal counting process $\{N(t), t\geq 0\}$ counts successive occurrences of an event in $(0,t]$ when the interoccurrence times are positive, independent, identically distributed random variables.
>
> **Intuition:** At every renewal instant the system statistically starts over, so one cycle is representative of all future cycles.

A renewal (counting) process  $\{N(t), t \geqslant 0\}$  is a nonnegative integer-valued stochastic process that registers the successive occurrences of an event during the time interval  $(0, t]$ , where the times between consecutive events are positive, independent, identically distributed random variables.

Let the successive durations between events be  $\{X_{k}\}_{k = 1}^{\infty}$  (often representing


the lifetimes of some units successively placed into service) such that  $X$  is the elapsed time from the  $(i - 1)$ st event until the occurrence of the  $i$ -th event. We refer to their common distribution as:

$$
F (x) = P [ X _ {k} \leqslant x ] \quad k = 1, 2, 3, \dots
$$

that is the probability of  $X_{k}$  being less than  $x$ , for any  $k$ , since they are independent.

A renewal process is a counting process, so a quite basic property is that at time zero  $X(0) = 0$  we count no events. Consequently, we set the probability that the time between two consecutive being equal to 0 is null:  $F(0) = 0$ . In other words we stipulate that two events can not occur at the same time. We will see later that this is not a necessary condition in order to prove some results we will show.

The last assumption we make, for now, is that  $F(\infty) = 1$ : hence  $X$ 's are finite random valued. If any of them were infinite, meaning that  $F(\infty) < 1$ , there would have been a non-null probability that at a certain point the system would stop, being a time between two consecutive events infinite. This special case is represented by the class of stopped random processes, that takes into account these special random variables, whose values may be infinite.

Up to now we have assumed that  $X_{i}$ 's are positive and finite valued random variables. The absolute time for the  $n$ -th event to occur is defined as:

$$
W _ {n} = X _ {1} + X _ {2} + \ldots + X _ {n} \qquad n \geqslant 1
$$

where by definition  $W_0 = 0$ . We can relate relate all these variables we have introduced by using  $N(t)$ :

$$
N (t) = \# \text { of indices } n \text { for which } 0 <   W _ {n} \leqslant t = \max  (n: W _ {n} \leqslant t)
$$

that counts the number of events occurred so far. The relation between interoccurrence times  $\{X_k\}$  and the renewal counting process  $\{N(t), t \geqslant 0\}$  is depicted in the following figure (5.2).
![[Stochastic_Processes_2020_p175_img62.jpeg]]
*Figure 5.2 - The relation between the interoccurrence times  $X_{i}$ , the total time  $W_{i}$  and the renewal counting process  $N(t)$ .*

This process can be described in three equivalent ways: the interoccurrence times  $X(t)$ , the counting process  $N(t)$  and finally the partial time process  $W(t)$ . All of them will contain the same information about the renewal process


we are considering and are interchangeably.
The most common example for renewal processes is the one of the light bulb. Let us supposed we have installed a new light bulb in a lamp at the starting time $0$, and that it will work for some random time before breaking. We are required then to replace it with one of the same kind, and let suppose we can do it instantaneously. When at time $X_{1}$ the first light bulb breaks, we immediately after replace it with a bulb that will work for a random time that is denoted by $X_{2}$ before burning in turn. At time $W_{2}=X_{1}+X_{2}$ we will replace it by an other one. The latter will work for a random time $X_{3}$, and so forth. In general, the $n$-th bulb will burn after $X_{n}$ time it has been replaced, and after a total time of $W_{n}$.

The main objective of renewal theory is to derive properties of certain random variables associated with the process: $\{N(t)\}$ and $\{W_{n}\}$ from knowledge of the distribution of the interoccurrence times $F(x)$. For example we want to know whether characterizing the distribution of $X$’s is sufficient to know how the process behaves.
The simplest, but not the least important, metric we can compute is the expected number of renewals for the time duration $(0,t]$:

$$
\mathbb{E}[N(t)]=M(t)
$$

that is called the renewal function, which we will discover plays a fundamental role in renewal theory.
We want to study now $M(t)$. We have already seen that $F(x)$ is the statistics of $X$’s, but we have not said anything yet about the statistics of $W$’s. They are linked by the relationship:

$$
P[W_{n}\leqslant x]=F_{n}(x)
$$

So we can find the statistics of $W_{n}$ by computing the $n$-th time convolution of $F(x)$ with itself. The general result states that the sum of independent random variables has a distribution that is the convolution of the single terms distributions in the sum. For this special case, where the single variables are i.i.d., then distribution will be made of the $n$ times convolution of the common distribution with itself. We can compute recursively $F_{n}(x)$ as:

$$
F_{n}(x)=\int_{0}^{\infty}F_{n-1}(x-y)dF(y)=\int_{0}^{x}F_{n-1}(x-y)dF(y)
$$

Where again:

$$
F_{n-1}(x)=\int_{0}^{x}F_{n-2}(x-y)dF(y)
$$

and so forth, up to the $n=1$ term that is $F(x)$ itself: $F_{1}(x)=F(x)$. Computations might be tedious, but in principle we need to go through them in order to obtain $F_{n}(x)$.
By the help of figure 5.2 we can now point out the connecting link between the


total waiting time process $\{W_n\}$ and the renewal counting process $\{N(t)\}$:

$$
N(t) \geqslant k \quad \Longleftrightarrow \quad W_k \leqslant t \tag{5.2}
$$

In other words: the number of events $N(t)$ we have counted up to time $t$ is at least $k$ if $W_k$ occurs, or has already occurred, within time $t$. We will prove in a later exercise that the equal sign for both the inequalities is necessary, or else the equivalence above would not be true any more.

It follows that the tail distribution:

$$
P[N(t) \geqslant k] = P[W_k \leqslant t] = F_k(t) \quad t \geqslant 0, k = 1, 2 \dots \tag{5.3}
$$

according to (5.2) and (5.1). Consequently we can find the probability of counting exactly $k$ events:

$$
\begin{array}{l}
P[N(t) = k] = P[N(t) \geqslant k] - P[N(t) \geqslant k + 1] = \\
= P[W_k \leqslant t] - P[W_{k+1} \leqslant t] \quad = F_k(t) - F_{k+1}(t) \quad t \geqslant 0, \quad k = 1, 2 \dots
\end{array}
$$

Where we used first (5.2) and then (5.1) to replace the $W$'s distribution.

Having we computed the full statistics of $N(t)$, we want now to obtain its expected value. For a non-negative random variable, when summing on all over the possible tail distributions of the kind (5.3), we obtain its average:

$$
\mathbb{E}[N(t)] = \sum_{k=1}^{\infty} P[N(t) \geqslant k]
$$

therefore:

$$
M(t) = \mathbb{E}[N(t)] = \sum_{k=1}^{\infty} P[N(t) \geqslant k] = \sum_{k=1}^{\infty} P[W_k \leqslant t] = \sum_{k=1}^{\infty} F_k(t)
$$

We know that $F_k(x)$ is a distribution for every $k$. But still we do need to prove that the infinite sum above converges, being it not obvious. Indeed we will do it later.

There are basically three random variables of particularly interest in renewal theory and are the following ones:

$$
\gamma_t = W_{N(t)+1} - t \quad \text{excess or residual time}
\delta_t = t - W_{N(t)} \quad \text{current life or age random variable}
\beta_t = \gamma_t + \delta_t \quad \text{total life}
$$

A pictorial description of these random variables is the one in the picture 5.3.

Recall that $N(t)$ is the number of renewals up to time $t$, whereas $W_N(t)$ is the time of the latest renewal up to (or at) time $t$. The next renewal will occur indeed at time $W_{N(t)+1}$. Being in $t$, the latest renewal occurred at $\delta_t$ ago, while the next renewal will occur at the next time $\gamma_t$. **The sum of these two random variables, that is the total length of the renewal interval, will be the total life as defined above**.
![[Stochastic_Processes_2020_p178_img63.jpeg]]
*Figure 5.3 - The excess life  $\gamma_{t}$ , the current life  $\delta_{t}$ , and the total life  $\beta_{t}$ .*

## 5.2 Examples of Renewal Processes

Among renewal processes we can consider some examples that are:

- **Poisson Processes**: A Poisson process  $\{N(t), t \geqslant 0\}$  with parameter  $\lambda$  is a renewal counting process having the exponential interoccurrence distribution:

$$
F (x) = 1 - e ^ {\lambda x} \qquad x \geqslant 0
$$

- **Traffic flow**: The distances between successive cars on an indefinitely long single-lane highway are often assumed to for a renewal process. So also the time durations between consecutive cars passing on a fixed location
- **Processes Associated with queues**: In a single-server queueing process there are embedded many natural renewal processes. We cite two examples:
	- If the customer arrival times form a renewal process, then the times of the starts of successive busy periods generate a second renewal process
	- For the situation in which the input process (the arrival pattern of customers) is Poisson, the successive moments in which the server passes from a busy to a free state determine a renewal process

- **Renewal Processes in Markov Chains**: Let  $Z_0, Z_1 \ldots$  be a recurrent Markov chain. Suppose  $Z_0 = i$ , and note that it is indeed irrelevant how we reached this state in order to determine the future behavior of the system. Every time we land to a given state, evolution will be statistically indistinguishable from the previous/future ones. Consider now the durations (elapsed number of steps) between successive visits to state  $i$ . Specifically, let  $W_0 = 0$ ,

$$
W _ {1} = \min (n > 0; Z _ {n} = i)
$$


and

$$
W_{k+1}=min(n>W_{k};Z_{n}=i)\qquad k=1,2...
$$

Since each of these times is computed from the same starting state $i$, the Markov property guarantees that $X_{k}=W_{k}-W_{k-1}$ are independent and identically distributed, and thus each visit of a generic state $X_{k}$ generates a renewal process.
![[Stochastic_Processes_2020_p179_img64.jpeg]]
*Figure 5.4 -  We can identify some interesting moments when dealing with queue processes, for example the moments when the first user arrives (white dots) or the last one departs (black dots). **The latters are renewal instants if arrivals are i.i.d. memoryless**, while the **formers are renewal instants** for delayed renewal processes if arrival times are i.i.d..*

### Processes Associated with queues

We see that whenever the system empties, meaning that it finds itself in state $0$, previous customers are not important to determine the future evolution of the system. Practically the system will have no memory of previous users and service times once it has emptied. These are indeed renewal instants.
Note that if the arrival process is memoryless, arrivals to an empty system will have all the same full distribution, as it we would start from time $0$. This guarantees that there is no need to remember when the last arrival occurred. So, starting at the point where the system empties, the memorylessness property will tell us that the next user will arrive according to an exponential distribution. Consequently the instants when the system becomes empty are renewal times (black dots in 5.4). In other words, at any of these points we only know that the next arrival will be Poisson so we can forget about whatever happened in the past.
If arrivals were not Poisson, the just stated points would not be renewal instants: the times passed from the last arrival would be correlated to the residual time for the next arrival to occur.
However, when there is an arrival to an empty queue (white dots in 5.4) the next state of the system will be $1$. These time instants are renewal times as well: statistically the evolutions starting from them are indistinguishable. Note that it is different from before, when we considered a class of points equivalent to the "time $t=0$" one, now the situation is the same when we the very first arrival occurred. For this class of points we can even relax the constraints and forget about the memoryless assumption for the interarrival times: they just need to be i.i.d. in order to be a renewal process. This class is called delayed renewal processes.

## 5.3 The Poisson Process

We have just stated that the Poisson process with parameter  $\lambda$  is a renewal process, one of the simplest ones, and so let us study it under this point of view. Its interoccurrence times are exponentially distributed as  $F(x) = 1 - e^{-\lambda x}, x \geqslant 0$ .

### The Renewal Function  $\mathbf{N}(t)$

We know that  $N(t)$  is Poisson distributed:

$$
P [ N (t) = k ] = \frac {(\lambda t) ^ {k} e ^ {- \lambda t}}{k !} \qquad k = 0, 1 \dots .
$$

and its expectation value is linear in  $t$ :

$$
M (t) = \mathbb {E} [ N (t) ] = \lambda t
$$

### Excess Life  $\gamma_{t}$

Recall that it is the time elapsed up to the next event.

$P[\gamma_t > x]$  is the probability of no events in the interval  $[0, t]$ , and it is only dependent on the length of the just mentioned interval. Formally:

$$
P [ \gamma_ {t} > x ] = P [ N (t + x) - N (t) = 0 ] = P [ N (x) = 0 ] = e ^ {- \lambda x}
$$

We can observe that, for a Poisson process, excess life is in turn exponentially distributed with parameter  $\lambda$ . This is due to the memorylessness property, so we do not need to know when the last event occurred:

$$
P [ \gamma_ {t} \leqslant x ] = 1 - e ^ {\lambda x} \quad x \geqslant 0
$$
![[Stochastic_Processes_2020_p180_img65.jpeg]]
*Figure 5.5 - The excess life  $x$ , at time  $t$ , is how long we will have to wait after the present instant in order to make the next event occur*

### Current Life  $\delta_t$

We now look backwards starting from  $t$ .

$P[\delta_t \geqslant x]$  is the probability that we have no events in the interval  $[t - x, t]$ ,


that is equivalent to the probability of no events in the interval of length  $[0, x]$ . We thus obtain the same exponential distribution for the Excess life, but with one more condition:  $0 \leqslant \delta_t \leqslant t$ . It is quite reasonable, since current life cannot be bigger than  $t$ . We can write this as:

$$
P [ \delta_ {t} \leqslant x ] = \left\{ \begin{array}{l l} 1 - e ^ {- \lambda x} & \text {f o r} 0 \leqslant x <   t \\ 1 & \text {f o r} t \leqslant x \end{array} \right.
$$

One should have noticed that looking backwards or forwards statistically does not make any big difference: we do find a similar distribution, but the truncation at time  $t = 0$ . It does not make any sense indeed to look back before the starting point, whereas future is in principle infinite. This is formally translated into the fact that the distribution of  $\delta$  is truncated at  $t = 0$ , meanwhile the exponential distribution for  $\gamma$  might be infinite.
![[Stochastic_Processes_2020_p181_img66.jpeg]]
*Figure 5.6 - We require now that both events  $\gamma_t > x, \delta_t > y$  hold, that is equivalent to require that no events occur in the interval  $[0, x + y]$  because of the property of Poisson processes.*

### Joint Distribution of  $\gamma_{t}$  and  $\delta_t$

We want now to compute the probability of the joint event  $(\gamma_{t} > x, \delta_{t} > y)$  at a generic instant  $t$ . This can happen only when no events occur in both intervals (see fig.5.6): looking backwards we must not see any event later than  $t - y$  and, in addition, in the future no events must occur before  $t + x$ . Since we are dealing with a Poisson process, this can be translated as having no events in a longer interval, that is the sum of the previous two:  $(t - y, t + x]$ . Or equivalently we can require no events in the interval of a total length of  $(0, y + x]$ , being the process memoryless. The joint distribution we are looking for will be thus exponential and² for any  $y < t$ :

$$
P [ \gamma_ {t} > x, \delta_ {t} > y ] = \left\{ \begin{array}{l l} e ^ {- \lambda (x + y)} & \text {if} \space x > 0, 0 <   y <   t \\ 0 & \text {if} \space y \geqslant t \end{array} \right.
$$

For a Poisson process, one should observe that  $\gamma_{t}$  and  $\delta_t$  are independent, since their joint distribution factors as the product of their marginal distributions. We would have expected this: sitting on the time instant  $t$ ,  $\gamma_{t}$  depends on the past whereas $\delta_t$ depends on the future, which are indeed disjoint time intervals.

### Mean Total Life $\mathbb{E}[\beta_t]$

We can find the expectation of $\beta_t$ as follows, recalling its definition as the sum $\beta_t = \gamma_t + \delta_t$ and exploiting the linearity of the operator $\mathbb{E}(\cdot)$:

$$
\mathbb{E}[\beta_t] = \mathbb{E}[\gamma_t] + \mathbb{E}[\delta_t] =
= \frac{1}{\lambda} + \int_0^\infty P[\delta_t > x] \, dx = \frac{1}{\lambda} + \int_0^t e^{-\lambda x} \, dx = \frac{1}{\lambda} + \frac{1}{\lambda} (1 - e^{-\lambda x}) \tag{5.4}
$$

Where we used the fact that $\delta_t$ is a truncated exponential, **non null only in the interval $(0,t]$,** and $\gamma_t$ distributes exponentially with parameter $\lambda$ so its expectation value is $1/\lambda$. We note that being the time between events exponential, so the mean has a $1/\lambda$ common factor.

Observe that the mean total life is significantly larger than the mean life of $1/\lambda = \mathbb{E}[X_k]$ of any particular renewal interval. Recall that $X_k$ is the interoccurrence times between two events, and in this case relates to $\gamma_t$ and $\delta_t$. We moreover note as $t >> 1$, the expression (5.4) for $\mathbb{E}[\beta_t]$ is approximately twice the mean life $1/\lambda$. In the next section we will go deeper into it.

### 5.3.1 The sampling paradox

Now we are going to discuss how it is possible for $\beta_t$ to have an expected value that is twice as large as the $1/\lambda = \mathbb{E}[X_k]$.

Let us consider the following renewal process: let us take a sequence of $X_i$'s which are separate and consecutive events as depicted in the figure 5.7.
![[Stochastic_Processes_2020_p182_img67.jpeg]]
*Figure 5.7 -  When we pick at random a time $t$, it is more likely that it falls in a longer interval. In this case it would be $X_2$ because it is the largest one.*

We want to compute $\mathbb{E}[X_k]$, **once an index $k$ has been picked at random with an uniform probability**. In this way are **sure that the result we will find is valid in general**: index has been chosen randomly, and all $X_k$'s do follow the same statistics. We can indeed select the index $k$ an other way: once we have chosen a time $t$, the correspondent $X_k$ will be the interval that contains time $t$. We want to evaluate whether the statistics obtained by these two ways of selecting $X_k$ are the same one.

> [!Important] Note - Sampling Bias
> The answer is no. In the first case, where we pick the index $k$ randomly, each $X_k$ will have the same probability of being chosen and so the statistics will be the same of $F(x)$.

Whereas, sampling in time we bias our statistics towards longer intervals because the probability of  $t$  to fall in them is obviously higher. The latter way is indeed the same way as we choose  $\beta_{t}$ : we first pick a time instant  $t$ , and  $\beta_{t}$  will be the interval which contains this time. Consequently, the statistics of  $\beta_{t}$  will be biased towards longer intervals because they are the intervals where  $t$  is more likely to fall. This is the reason why  $\mathbb{E}[\beta_t]$  is larger than the  $\mathbb{E}[X_k]$  of a generic interval  $X_{k}$  sampled according to the first rule.

### Bus Stop - Example

An other example is given by the following situation: let us suppose we have a bus that runs twice every hour. However, it does not run precisely every half an hour: so that the intervals of the two runs are not equally large. This process can be seen as two asynchronous buses that have two different travel-times so that one of them lags and runs some time later. Let us suppose that we do not know at what time the bus goes and we, at a random time  $t$ , go to the bus station. The only thing known is that there are two lines that run once per hour. We may think that, since there are two lines, the expected time between two buses is 1/2hr, and so the average waiting time is 1/4hr (15min). This argument is actually wrong, and now we will show it.

Let us suppose that  $a$  is the time lag between two consecutive runs, that are by assumption made by the two different lines.

If  $a \to 0$ , both buses come at the same time and so the amount of time we need to wait for the next run (that are indeed two runs!) is 1hr. So the time we will need to wait, on average, becomes 30min.

Whereas, if  $a \to 1/2\mathrm{hr}$ , we obtain the previous argument where the average waiting time turns out to be  $1/4\mathrm{hr}$  and so  $15\mathrm{min}$ . We clearly see how the average waiting time depends on the time lag  $a$  between two runs.
![[Stochastic_Processes_2020_p183_img68.jpeg]]
*Figure 5.8 - There are two buses that come twice per hour to a bus stop at two different moments. The difference in time between two consecutive runs is respectively  $a$  and  $1 - a$ . The system therefore has period 1hr.*

Now let us suppose, since the system is periodic with period 1hr, that we go to the bus stop randomly in the interval  $(0,t)$  according to an uniform distribution. We know that the bus of the first line comes at time  $t = 0$ , after some time  $t = a$  the bus of the second line comes, whereas at  $t = 1$  hr we expect the second run of the first bus. We want to know what our waiting time will be. Note that if we go to the bus stop at time  $t \in (0,a)$ , our waiting time up to time  $a$  will be consequently  $a - t$ . On the other hand, if we come at a time  $t > a$  and so  $t \in (a,1)$ , our waiting time will be  $1 - t$  since the following run is at time  $t = 1$ . The waiting time function  $\gamma_{t}$  is therefore defined differently in the two intervals:

$$
\gamma_{t}=w(t)=\begin{cases}t-a&0<t\leqslant a\\
1-t&a<t\leqslant 1\end{cases}
$$

One should note that if we go to the bus stop at a uniform random time $t$, the average waiting time will be the sum of the averages for the two different definitions of the function over the 1hr interval. Formally:

$$
\mathbb{E}[w(t)]=\int_{0}^{1}w(t)dt=\int_{0}^{a}(a-t)dt+\int_{a}^{1}(1-t)dt=
=-\frac{(a-t)^{2}}{2}\Big{|}_{0}^{a}-\frac{(1-t)^{2}}{2}\Big{|}_{a}^{1}=a\cdot\frac{a}{2}+(1-a)\cdot\frac{1-a}{2}
\mathbb{E}[w(t)]=a\cdot\frac{a}{2}+(1-a)\cdot\frac{1-a}{2}
$$

Each term in the last expression can be split into the product of two factors according to a same pattern. The first term is the probability to choose respectively a time $t$ in a certain interval, that is $a$ in $[0,a]$, and $1-a$ in $[a,t]$. This is multiplied by the average waiting times respectively for the two different intervals: $a/2$ for the first one, and $(1-a)/2$ for the second one.

Consequently, for larger intervals we both have larger waiting times and a larger probabilities to be chosen. This is indeed the same argument we have seen before for the sampling rule: it tends to privilege intervals that are longer. In our situation it translates into the fact that, when we go at a random time to the bus stop, we tend to arrive there in a larger gap between two consecutive buses and therefore our average waiting time increases.

Observe that, as an example, if $a=1/2$hr our waiting time is indeed $1/4$hr$=15$min as we would expect!

Whereas in the case $a=1/6$hr$=10$min, the average waiting time is $13/36$hr$\simeq 21.50min$. We see that the more $a$ decreases, the more our average waiting time will tend to be equal to $1/2$hr.

This is an other example of a situation where sampling a sequence of intervals by choosing at random time and see in which interval it falls may bias our statistics.

## 5.4 Long run Behaviour

We want now to study as usual the asymptotic behaviour for the renewal processes.

We start by showing some simple asymptotic results, but before doing so, it is needed to make explicit a notation: $S_{n}\equiv W_{n}=\sum_{k=1}^{n}X_{k}$, that is the **absolute time of the $n-th$ event**, will be called sometimes $S_{n}$ according to the notation used in some books.

The first result we prove comes from the Law of large numbers: we want to find:

$$
\lim_{n\to\infty}\frac{S_{n}}{n}=\lim_{n\to\infty}\frac{\sum_{k=1}^{n}X_{k}}{n}=\mathbb{E}[X]=\mu>0\qquad\text{w. prob. 1}
$$

where we used the fact that $X_{k}$’s are i.i.d. and their sum, divided by their number, with probability 1 tends to their expectation value. Under the assumption that $X_{k}$’s are positive random variables: $\mu>0$. This is reasonable: the time that it takes to observe $n$ events normalized to the total number of events returns the time average between two events, and so in the limit it will tend to its statistical average, namely $\mu$.

**When we count an infinite number of renewals, for $n\to\infty$, the time taken to count them must also be infinite.** We have just stated that $\mu>0$, and so in the limit it is needed that $S_{n}\to\infty$ too, since $\mu\neq 0$. Consequently we cannot have infinite number of renewals in finite time:

$$
\lim_{n\to\infty}S_{n}=\infty
$$

**Proposition from Ross p.101**
The converse is also true: we cannot have finite renewals in infinite time. In order to show this let us denote by $N(\infty)=\lim_{t\to\infty}N(t)$ the total number of renewals that occurs in an infinite time. Then:

$$
N(\infty)=\infty\qquad\text{with probability 1}
$$

The only way in which $N(\infty)$ can be finite, is for one of the interarrival times to be infinite. This means that we stop counting because, after a given event has occurred, it takes an infinite amount of time to count the next event. We can say equivalently that after a certain event nothing will happen. Shortly, this is the only way where we can have a finite number of events, otherwise if they kept happening then their number would be surely infinite.

$$
P[N(\infty)<\infty]=P[X_{n}=\infty\text{ for some }n]=P[\cup_{n=1}^{\infty}\{X_{n}=\infty\}]
$$

Last two expressions are equivalent. We now use the Boole’s inequality and set an upper bound for the last term:

$$
P\left[\bigcup_{n=1}^{\infty}\{X_{n}=\infty\}\right]\leqslant\sum_{n=1}^{\infty}P[X_{n}=\infty]=0
$$

Recall that we excluded that $X_{i}=\infty$ for all $i$’s when we defined the renewal processes, so $F(x)=1$ as $x\to\infty$. Consequently all probabilities in the sum are 0, and therefore the probability that the total number of renewals is finite is null. Conversely, the probability $P[N(\infty)=\infty]=1$.

We can note indeed a correspondence between the time of observations and renewals. Finite times correspond to finite number of renewals, whereas infinite times correspond to infinite number of renewals. Thus $N(t)$ goes to infinity as $t$ goes to infinity, but we would like to know the rate at which $N(t)$ does it, whether it is linear, logarithmic, exponential and so forth. Formally, we want to compute $\lim_{t\to\infty}N(t)/t$.


We start by stating the following:

> [!Important] Proposition - Linear Growth Rate of $N(t)$
> **Proposition**. With probability 1
> 
> $$
> \frac{N(t)}{t}\to\frac{1}{\mu}+o(t)\qquad\text{as }t\to\infty
> $$
> 
> where $\mu$ is the expectation value of $X$.
> 
> This proposition tells us that the *rate* at which $N(t)\to\infty$ is linear in $t$.
> 
> **Proof** which comes out very often at the exam
> Given a time $t$, note that the index of the latest event that has occurred is $N(t)$. Consequently, $N(t)+1$ will be the index of the *next* renewal. Let $S_{N(t)}$ represents the time of the last renewal *prior to or at* time $t$, whereas $S_{N(t)+1}$ represents the time of the *first* renewal *after* time $t$.
> Clearly $t$ will be such that is between these two times: $S_{N(t)}\leqslant t<S_{N(t)+1}$. Dividing this last expression by $N(t)$:
> 
> $$
> \frac{S_{N(t)}}{N(t)}\leqslant\frac{t}{N(t)}<\frac{S_{N(t)+1}}{N(t)}
> $$
> 
> The first term of the inequality, thanks to the Law of large numbers, in the limit as $N(t)\to\infty$ will converge to the statistical average $\mu$.
> Recalling that $N(t)\xrightarrow{t\to\infty}\infty$ we obtain:
> 
> $$
> \lim_{N(t)\to\infty}\frac{S_{N(t)}}{N(t)}\to\mu\qquad\text{as }t\to\infty
> $$
> 
> Furthermore the most r.h.s. term can be factorized as:
> 
> $$
> \frac{S_{N(t)+1}}{N(t)}=\left[\frac{S_{N(t)+1}}{N(t)+1}\right]\left[\frac{N(t)+1}{N(t)}\right]
> $$
> 
> and, in the limit as $N(t),t\to\infty$, the first term will converge to $\mu$ and the second to $1$.
> **Recalling that *in the limit strict inequalities must become large inequalities*:**
> 
> $$
> \mu\leqslant\frac{t}{N(t)}\leqslant\mu
> $$
> 
> that is verified only when $\frac{N(t)}{t}=\mu$. **This happens *with probability 1* because our result is based on something that in turn is valid with prob 1, namely *Law of large numbers*.** In addition, being $N(t)$ a random variable this is not a limit in the "regular sense", nevertheless we can say that the limit is true *with probability 1*. Consequently, the probability for the statement not being true is null, thus concluding our proof. ∎
> 
### The Renewal Function

Recall now the formula we derived for the expected number of counts in the interval $(0,t]$:

$$
M(t)=\mathbb{E}[N(t)]=\sum_{j=1}^{\infty}F_{j}(t)
$$

where

$$
F_{j}(t)=P[S_{j}\leqslant t]\qquad t\geqslant 0
$$

Our first task will be to *show* that $M(t)$ is finite $\forall t>0$: we assumed this when we derived the first formula, but actually we had not proved it yet.

$F_{n}(t)$ is the distribution of the sum of $n$ *i.i.d.* *random variables*, namely the $X$’s. The sum can be split into two components: the sum $\sum_{0}^{m}$ and the remaining $\sum_{n-m}^{m}$, where $0<m<n$.

The distribution of these partial sums is the convolution between $F_{n-m}$ and $F_{m}$:

$$
F_{n}(t)=\int_{0}^{t}F_{n-m}(t-\xi)dF_{m}(\xi)\leqslant F_{n-m}(t)F_{m}(t)\qquad 1\leqslant m\leqslant n-1
$$

Where the inequality holds being $F_{n}(t)$ *monotone*. In addition we can bound it by using the product of two terms whose indices must sum to $n$.

$M(t)$ can in turn be rewritten as the double sum over the indices $k,r$ that, it can be checked, spans all the values for the index $j=1,2,...,\infty$:

$$
M(t)=\sum_{j=1}^{\infty}F_{j}(t)=\sum_{n=0}^{\infty}\sum_{k=1}^{r}F_{nr+k}(t)
$$

The last term can be *upperbounded* in a *similar way* we shown above, using the product $F_{r}(t)F_{n-1r+k}$. The latter can be in turn upperbounded by $F_{r}(t)F_{n-2r+k}$ and so forth, iteratively, for $n$ times:

$$
\sum_{n=0}^{\infty}\sum_{k=1}^{r}F_{nr+k}(t)\leqslant\sum_{n=0}^{\infty}\sum_{k=1}^{r}(F_{r}(t))^{n}\;F_{k}(t)=\overbrace{\left(\sum_{n=0}^{\infty}(F_{r}(t))^{n}\right)}^{\text{converges geom. if }F_{r}(t)<1}\underbrace{\left(\sum_{k=1}^{r}F_{k}(t)\right)}_{\leqslant r}
$$

Last inequality holds because $F_{k}(t)$ is independent of $n$ and $(F_{r}(t))^{n}$ of $k$, it is allowed then to factorize these terms. The second one is both finite and less than $r$, being $F_{k}(t)$ a distribution with values between $0$ and $1$.

It can be observed that the first term *converges geometrically* if $F_{r}(t)<1$, because $F_{r}(t)$ is a probability. The condition that $F_{r}(t)<1$ holds only when we choose $r$ appropriately. Let us prove now that we can *always* choose an $r$ in order to make the *infinite sum converge*. Before doing so, one should note that the first inequality holds *without any condition* on $r$, except the one that $r$  must be finite.

> [!Important] Theorem 5.4.1 - Finiteness of the Renewal Function
> $\forall t, \exists r$  such that  $F_{r}(t) < 1$
> 
![[Stochastic_Processes_2020_p188_img69.jpeg]]
*Figure 5.9 - Clearly having fixed  $F(t = 0) = 0$ , we will be always able to find a  $t_0 \neq 0$  for which  $F(t_0) < 1$  because  $F(t)$  is continuous.*
> 
> *Proof*. Clearly we can always find a  $t_0 > 0$  s.t.  $F(t_0) < 1$  and  $F(t) < 1$  for  $t < t_0$ . This is always valid because we stated that  $F(0) = 0$ . The only case in which would not be possible to find such  $t_0$  would be if immediately  $F(0) = 1$ , which cannot be.
> 
> As we can see in the picture (5.21) at a certain point  $F(t)$  will be equal to 1. Given that  $F(0) = 0$  and  $F(t)$  is continuous, the function cannot reach 1 by "jump", and consequently there will be for sure some  $t_0$  s.t.  $F(t') < 1$  where  $t' < t_0$ , no matter how close  $t_0$  is to zero.
> 
> Once we have found  $t_0$ , we still need to show that  $1 - F(r) < 1$ . This is equivalent to the probability  $P[S_r > t]$ , but only if we choose all  $X_i > t / r \quad \forall i = 1, \dots, r$  and so  $S_r > t$ . Note that there may be also other ways to make the just mentioned condition to be true. Therefore, the assumption we made over all  $X_i'$ 's is just a subset of all the useful possibilities:
> 
> $$
> 1 - F _ {r} (t) = P [ S _ {r} > t ] \geqslant (P [ X _ {i} > t / r, \forall i = 1, \dots , r ]) = (P [ X _ {i} > t / r ]) ^ {r} = (1 - F (t / r)) ^ {r} > 0
> $$
> 
> Where we can rewrite the joint probability for all the  $X_{i}$ 's as their product, being them i.i.d. Note that last inequality holds only when  $F(t / r) < 1$ , so we are needed to make it to be less than 1 by choosing an appropriate  $r$  s.t.  $t / r < t_0$ . This possible because we have picked  $t_0$  in order to  $F(t) < 1$  for  $t < t_0$ .
> 
> Finally, given  $t$ , we can always find  $r$  s.t.  $r > t / t_0$ , which makes the term  $F(t / r) < 1$ , and therefore the whole probability  $(1 - F(t / r)) > 0$  and consequently  $1 - F_r(t) > 0$ , thus concluding our proof.
> 
> We have just shown that for any  $t$ , we can make  $F_{r} < 1$  by choosing an appropriate value for  $r$ : the rhs expression in (5.5) can be made finite. Recall that we were looking for an upperbound to be set for  $M(t)$ , and we have just shown that is finite, thus making  $M(t)$  finite as well.
> 
> What we have just found has two important consequences, the first one is:
> 
> $F_{n}(t)\to 0$  as  $n\to \infty$  (this happens at least geometrically fast)
> 
> 
> because $F_{r}(t)<1$ for an appropriate choice of $r$. In addition:
> 
> $$
> M(t)<\infty\qquad\text{for all }t
> $$
> 
> So we cannot have an infinite number of renewals in a finite time.
> 

## 5.5 The Renewal Argument


We will now show that $M(t)$, the renewal function, satisfies the following integral equation:

$$
M(t)=F(t)+\int_{0}^{t}M(t-x)dF(x)\qquad t\geqslant 0
$$

or alternatively in the equivalent convolution formalism:

$$
M(t)=F(t)+F*M(t)\qquad t\geqslant 0
$$

where $F(t)$ is the common distribution of inter event times. In order to prove that the equation above holds, we need to invoke the so-called Renewal Argument. It is a very important way of reasoning related to the renewal property of these processes, and it might explain us why renewal processes are very popular among the stochastic processes family.

In order to invoke it, we need first to condition on the first time of the renewal $X_{1}$ and then write recursive equations, so that we can find the quantities we want to compute. Note that, after this instant, everything restarts as if from scratch because of the condition that there must be a renewal.

As an example, let us try to compute $\mathbb{E}[N(t)]=M(t)$. This situation is sketched in the next image.

(a) – If $X>t$, obviously we do not count any event.

(b) – If $X\leqslant t$, an event has already been and therefore the process starts again. We are allowed to shift the time axis starting from $X$.

Given that the first renewal occurs at time $t=x$, for $t\leqslant x$, obviously we have not observed any event yet. Consequently the statistics of expected renewals will be zero.

Meanwhile, in the case where $t>x$, we know that there has already been a renewal and from that moment the process will start as if from scratch. So, being at time $t$, we will have observed stated renewal at time $x$ plus whatever renewals may occur in time $t-x$. Their expected number will be only function of the time passed starting from time $t-x$. An other point of view is that we shift the time axis by $x$, starting our counting from that instant and setting it to be our reference time. On average we will have, for $t\geqslant x$, that we will have counted $1+M(t-x)$. Summarizing:

$$
\mathbb{E}[N(t)|X_{1}=x]=\begin{cases}0&\text{if }x>t\\
1+M(t-x)&\text{if }x\leqslant t\end{cases}
$$

We have seen that as a first step we need to condition on the time of the first renewal $X_{1}$, in order to find the conditional expectation. Finally, averaging over the $X_{1}$ statistics, we are able to remove the dependence on the condition we introduced.

By conditioning on a renewal at time $x$, however, there might be different cases depending on which side of the time axis we leave $x$. In other words we need to take into account whether we are considering sooner or later instants with respect to $x$, thus leading to multiple definitions as above. Considering all of them we can finally compute the unconditional distribution.

When removing the condition, we exploit the law of total probability:

$$
M(t)=\mathbb{E}[N(t)]=\int_{0}^{\infty}\mathbb{E}[N(t)|X_{1}=x]dF(x)=\int_{0}^{t}[1+M(t-x)]dF(x)=\\
=F(t)+\int_{0}^{t}M(t-x)]dF(x)
$$

Where first we applied the definition (5.13) for the integrand, noting that it is different from zero only in the interval $x\in(0,t]$. We know then that $\int_{0}^{t}1dF(x)=F(t)$, while the other term is the convolution between $F(x)$ and $M(t-x)$. We have finally shown that (5.6) holds.

We can note that the latter is special case of the so called Renewal Equations, that are the ones of the kind:

$A(t)=a(t)+\int_{0}^{t}A(t-x)dF(x)\qquad t\geqslant 0$ (5.8)

The function we want to find, namely the unknown of our equation, is $A(t)$. In the previous example, the role of unknown was played by $M(t)$.

$F(t)$ is as always the distribution of the inter event times, while $a(t)$ is a known function. These last two quantities are to be given. In general it is not true that $a(t)=F(t)$: it happens only when $A(t)=M(t)$, as in the previous example. Any time we apply the Renewal Argument, we will end up in a equation of the kind (5.8) once we want to remove the condition over $X_{1}$.

An other important fact of Renewal Equations, is that under pretty mild conditions we can show that the solution for (5.8) is unique and explicit. It is not obvious since $A(t)$ appears on both side of the equations, and so solving it might be very difficult. We introduce now a theorem that will help us:


Suppose $a(t)$ is a bounded function, even for $t\to\infty$. Then there exists one and only one function $A(t)$ bounded on finite intervals that satisfies

$A(t)=a(t)+\int_{0}^{t}A(t-y)dF(y)$ (5.9)


This solution is:

$A(t)=a(t)+\int_{0}^{t}a(t-x)dM(x)$ (5.10)

where $M(t)=\sum_{k=1}^{\infty}F_{k}(t)$ is the renewal function.

> [!Important] Theorem - Solution of the Renewal Equation
> **Statement:** If $a(t)$ is bounded, then the renewal equation
>
> $$
> A(t)=a(t)+\int_{0}^{t}A(t-y)dF(y)
> $$
>
> has a unique solution bounded on finite intervals:
>
> $$
> A(t)=a(t)+\int_{0}^{t}a(t-x)dM(x).
> $$
>
> **Proof:** The source states that the proof is not provided in the source.
>
> **Intuition:** Renewal equations become explicit once every possible renewal after the first is accumulated through the renewal function $M(t)$.

The proof is not provided in the source.

We can see that (5.9) and (5.10) differ only by the convolution arguments. One should note in addition that in (5.10) everything that is known stands on the rhs: once $\sum_{k=1}^{\infty}F_{k}(t)$ is specified, $M(t)$ can be easily found, while the unknown term is on the lhs. This shows that the solution is explicit. Computing the integral may be difficult and might not even be solvable analytically, but this is just a practical matter. The most important thing is that the integral can be computed, being it explicit.

Renewal theory allows us to solve the problem of finding some interesting statistical quantities by first conditioning over $X_{1}$, and then by removing this condition when considering the different cases in the Renewal Equations that follow. Their solution is generally unique and is given by (5.10).

### Applications - $\mathbb{E}[S_{N(t)+1}]$

We want now to consider one more case where we can exploit the Renewal Argument. We want to compute the expectation value of the time of renewal that immediately follows time $t$. Formally:

$\mathbb{E}[S_{N(t)+1}]=\mathbb{E}[X_{1}+X_{2}+...+X_{N(t)+1}]=$
Here one should note that the sum in the rhs is a random variable, being all the terms i.i.d. random variables themselves. We now recall the exercise done in the first week of class (1) at page 13, where both $X$’s and the number of terms $N(t)$ were independent r.v. Clearly this is not the case, being them correlated. For example, once fixed a time interval that is long $t$, if the number of events $N(t)+1$ occurred is large, then each of the durations $X$’s must be small. There is an obvious dependence between the number of renewals and the duration between two renewals, so we cannot apply the above mentioned results. However the final expression is still the same one, even if we invoke a different argument:

$\mathbb{E}[S_{N(t)+1}]=\mathbb{E}[X_{1}]\cdot\mathbb{E}[N(t)+1]=\mathbb{E}[X_{1}]\cdot\mathbb{E}[M(t)+1]$

It is even more strange that, in the case we decide to truncate the sum up to the $N(t)$-th event, the result we have just stated does not apply any more.
It is always true for any distribution of $X$ that:

$\mathbb{E}[S_{N(t)+1}]=\mathbb{E}[X]\cdot\mathbb{E}[N(t)+1]$ (5.11)

But, actually, it is not true in general that the similar one applies:

$\mathbb{E}[S_{N(t)}]\neq\mathbb{E}[X]\cdot\mathbb{E}[N(t)]$ (5.12)


There might be some special cases where the last expression holds, but in general it does not.

We should note that on the lhs the only difference is the renewal interval we are dealing with: (5.11) does not contain $t$ because it is right after it, whereas the (5.12) it does. In the rhs the difference is in the expectation values $\mathbb{E}[N(t)+1]$ and $\mathbb{E}[N(t)]$. In addition we know that a renewal interval that contains time $t$ is not *typical*: it is indeed larger, and its expectation value $\mathbb{E}[X]$ is larger itself because of the sampling bias. In order to prove (5.11) we need to show that the equality is always true, whereas for (5.12) it is sufficient to find an example where it is not true.
![[Stochastic_Processes_2020_p192_img70.jpeg]]
*Figure 5.11 -  We have two different cases that correspond to the relative position to $X$ wrt the time we pick. In the case that a general $t^{\prime}>X$, we count a renewal and reshift our time axis as we did before and the other quantities rescale accordingly.*

For the first expression, we start again by invoking the *Renewal Argument*:

$$
\mathbb{E}[S_{N(t)+1}|X_{1}=x]=\begin{cases}x&\text{if }x>t\\
x+A(t-x)&\text{if }x\leqslant t\end{cases}
$$

In the first case we note that, when we consider an instant before $t$ given no renewals occurred, the next renewal time will occur at time $x$. Whereas for $t\geqslant x$ there has already been a renewal at time $x$, and in that moment the process essentially restarts. The time axis is shifted of a quantity $x$.

The expectation value of the time of the next renewal is $\mathbb{E}[S_{N(t-x)+1}]$, so that we recognize:

$$
\mathbb{E}[S_{N(t-x)+1}]=A(t-x)
$$

as the time-shifted version of the quantity introduced as:

$$
A(t)=\mathbb{E}[S_{N(t)+1}]
$$

By using the law of total probability we can remove the conditional event:

$$
A(t)=\mathbb{E}[S_{N(t)+1}]=\int_{0}^{\infty}\mathbb{E}[S_{N(t)+1}|X_{1}=x]dF(x)=
$$

But now recalling that we have different cases when we are on different sides wrt to $x$:

$$
=\int_{0}^{t}[x+A(t-x)]dF(x)+\int_{t}^{\infty}xdF(x)=\int_{0}^{\infty}xdF(x)+\int_{0}^{t}A(t-x)dF(x)=
$$


The first term obtained is $\mathbb{E}[X_1]$, while the second term is a convolution:

$$
A(t) = \mathbb{E}[X_1] + \int_0^t A(t - x) \, dF(x)
$$

Recall that the unknown is $A(t) = \mathbb{E}[S_{N(t) + 1}]$. When comparing it to (5.8), we see that the known term is $a(t) = \mathbb{E}[X_1]$. Consequently, having $X_1$ a finite value, its mean is bounded and constant for all $t$.

Holding all its hypotheses, we can use the theorem (5.5.1) and find an unique and explicit solution for the equation.

We can write the equation tailoring it to our problem:

$$
A(t) = a(t) + \int_0^t a(t - x) \, dM(x) = \mathbb{E}[X_1] + \int_0^t \mathbb{E}[X_1] \, dM(x) = \mathbb{E}[X_1] \left(1 + M(t)\right)
$$

$\mathbb{E}[X_1]$ is constant and can be factorized, and consequently the integral $\int_0^t dM(x) = M(t)$. This way we obtain the last result and we can conclude our small proof. We have shown in fact that (5.11) holds, no matter what is the distribution of $X$.

**Exercise 5.5.1:**

> [!Example] Exercise 5.5.1 - Failure of Wald-like Identity for $S_{N(t)}$
> **Problem:** Prove that (5.12), $\mathbb{E}[S_{N(t)}]\neq\mathbb{E}[X]\mathbb{E}[N(t)]$ in general. Use a Poisson process as a hint.
>
> **Approach:** Compare the stopped sum at the renewal before $t$ with the product of the mean interarrival time and expected renewal count.
>
> **Solution:** The complete solution and counterexample setup are transcribed below.
>
> **Takeaway:** $N(t)$ and the renewal intervals are dependent, so identities requiring independence cannot be applied blindly.

Prove that (5.12) in general is not true. As a hint, use a renewal process that is a Poisson process.

**Solution.** We need first to find the lhs $\mathbb{E}[S_{N(t)}]$. Then we need to compute the two factors in the rhs: the expected interarrival time $\mathbb{E}[X]$ and the expected number of arrivals $\mathbb{E}[N(t)]$ in the time interval $(0, t]$. Once we have made these computations, it can be shown that lhs and rhs are actually different, thus stating that for a Poisson Process (5.12) is not true.

One other example we can use to prove (5.12) in general is not true, is the following one. Let the interevent times distribution $X_i$ be:

$$
X_i = \begin{cases}
1 & \text{with probability } p \\
a & \text{with probability } 1 - p \quad a \geqslant 2
\end{cases}
$$

and let us take $t = 1.5$. By computing the same quantities stated above, we can show that (5.11) is always true, whereas (5.12) is not in general.

## 5.6 The Elementary Renewal Theorem

We recall now a result we obtained for the Renewal processes in the lung run:

$$
N(\infty) = \infty \quad \text{with probability } 1
$$


In addition we have shown the way how $N(t)\to\infty$, that is almost linear:

$$
\lim_{t\to\infty}\qquad\frac{t}{N(t)}\to\frac{1}{\mu}
$$

where $\mu$ is $\mathbb{E}[X]$.

One other result for $t\to\infty$ is the so called Elementary Renewal Theorem (proof not provided in the source), that states the following:

> [!Important] Theorem - Elementary Renewal Theorem
> **Statement:** If $\mu=\mathbb{E}[X]$, then:
>
> $$
> \lim_{t\to\infty}\frac{M(t)}{t}=\frac{1}{\mu}.
> $$
>
> **Proof:** The source states that the proof is not provided in the source.
>
> **Intuition:** In the long run, the expected number of renewals is approximately elapsed time divided by the mean interarrival time.

$$
\lim_{t\to\infty}\frac{M(t)}{t}=\lim_{t\to\infty}\frac{\mathbb{E}[N(t)]}{t}=\frac{1}{\mu}
$$

It differs from the result we mentioned above by the fact that in the first case $N(t)$ was a random variable: so the limit as $t\to\infty$ was to be interpreted as with probability $1$. In this case, however, $M(t)$ is an expectation value or, in other words, a function. This ensures us that the limit is valid in the regular sense. Recall that we have seen for a Poisson Process that $M(t)=\lambda t$: it is the expected value of number of events in an interval of length $t$.

Now we want to know if, given the fact that some random variables go to some value with probability 1, this is enough to say that its expectation also must converge to the same limit. The answer is NO: if something goes to a certain value with probability 1, it is not sufficient to determine the behavior of its expectation value.

In order to prove this, let us consider the following case. Let $U$ be a random variable uniformly distributed in the interval $(0,1)$. Now let us define a sequence of random variables $Y_{n},n\geqslant 1$ as:

$$
Y_{n}=\begin{cases}0&\text{if }U>1/n\\
n&\text{if }U\leqslant 1/n\end{cases}
$$

Now, since $U$ will be greater than $0$ with probability $1$, it follows that $Y_{n}$ will equal $0$ for all sufficiently large $n$. Consequently $Y_{n}$ will equal $0$ for all $n$ large enough, so that $1/n<U$. And so, in the limit, we have that:

$$
Y_{n}\to 0\qquad\text{as }n\to\infty\qquad\text{w. prob. 1}
$$

In other words, with probability $1$, the limit of the random sequence $Y_{n}$ is $0$.

On the other hand, computing the expectation value for $Y_{n}$ simply applying its definition:

$$
\mathbb{E}[Y_{n}]=nP\left[U\leqslant\frac{1}{n}\right]=n\frac{1}{n}=1
$$

Where the probability $P[Y_{n}=0]=1-1/n$ from the definition of $U$, while for $P[Y_{n}=n]=1/n$.

We have just shown that $\mathbb{E}[Y_{n}]=1$ for every $n$, and so it will be true also in the limit as $n\to\infty$. Therefore we conclude by summarizing:

$$
Y_{n}\to 0\qquad\text{as }n\to\infty\quad\neq\quad\mathbb{E}[Y_{n}]=1\qquad\text{as }n\to\infty
$$


where the lhs occurs with probability 1.

If we want to understand why this is true, we should have noted that is in the first limit we were considering the probability $P[Y_{n}=n]\to 0$ for $n$ sufficiently large. This event will have a probability that in the limit vanishes, thanks to its definition.

Meanwhile, computing its expectation value, we have that every contribution for a given $n$ of the sequence is $n\cdot 1/n$. Each term will increase linearly with $n$, whereas its probability will decrease according to $1/n$ and even go to $0$. Each contribution will compensate to $1$ for every $n$.

In the case that we had chosen $Y_{n}=n^{2}$, then the expectation would have diverged. This tells us that in the limit, for a random variable, the only thing that matters is how probability in function of $n$ behaves, whereas for the expectation value both probability and its value itself are important. It is possible that an event with vanishing probability still gives a finite contribution to the expectation value, depending particularly on the values that the random variable may take, which must be somewhat infinite.

Recalling now the theorem we have stated before, whose proof is not provided in the source, we can now sketch what its statement asserts:
![[Stochastic_Processes_2020_p195_img71.jpeg]]
*Figure 5.12 -  In the limit as $t\to\infty$, $M(t)$ will grow linearly.*

Note as $M(t)$ is linearly increasing wrt $t$, and so as $t\to\infty\quad M(t)\simeq\frac{t}{\mu}$.

It is a very intuitive result: if $\mu$ is the average renewal time, we will approximately count the ratio of the time $t$ passed, normalized to the mean time between two consecutive events $\mu$. This is not obvious indeed, and it is shown in the proof, which we will not consider.

### 5.6.1 The Basic Renewal Theorem

The elementary renewal theorem asserts that, for infinite time horizons:

$$
\lim_{t\to\infty}\frac{M(t)}{t}=\frac{1}{\mu}
$$

But we want now to show what happens when the time intervals are not infinite any more. Let us consider the following situation:

We want to compute now on average how many renewals occur in the shorter interval we highlighted in the figure, namely $(t,t+h)$, for any value of $h$. In other words we want to know what is the increment of the process $M(t)$ in a
![[Stochastic_Processes_2020_p196_img72.jpeg]]
*Figure 5.13 - For any value of  $h$ , we want to compute the average increment in the interval  $(t, t + h)$ . This increment will be  $N(t + h) - N(t)$ , while their expectation value  $M(t + h) - M(t)$ .*

generic interval of length  $h$ .

The number of renewals in such interval will be obviously  $N(t + h) - N(t)$ , and its expectation will be:

$$
\mathbb {E} [ N (t + h) - N (t) ] = M (t + h) - M (t) \equiv M (t, t + h ]
$$

The renewal theorem states that this expectation value, as  $t \to \infty$ , will be proportional to the length of the interval  $h$  according to the constant term  $1 / \mu$ :

$$
\lim _ {t \to \infty} M (t, t + h ] = h / \mu \qquad \mathrm {f o r a n y f i x e d} h > 0
$$

This theorem applies to intervals of finite duration as long as already some time has passed since the start of the process. It lets then the process to settle to some asymptotic behaviour, not taking into account the possible transient at the beginning. Whereas the elementary theorem referred to intervals of infinite duration. We have now introduced a result that is stronger than the basic theorem.

An other formulation for this theorem is the following, given by Karlin-Taylor's book:

Theorem 5.6.1. Let  $F$  be the distribution function of a positive random variable with mean  $\mu$ . Let  $M(t) = \sum_{k=1}^{\infty} F_k(t)$  be the renewal function associated with  $F$ . Let  $h > 0$  be fixed. Then:

> [!Important] Theorem 5.6.1 - Basic Renewal Theorem
> **Statement:** Let $F$ be the distribution function of a positive random variable with mean $\mu$, and let $M(t)=\sum_{k=1}^{\infty}F_k(t)$. For fixed $h>0$:
>
> 1. If $F$ is not arithmetic, then $\lim_{t\to\infty}[M(t+h)-M(t)]=h/\mu$.
> 2. If $F$ is arithmetic, the same limit holds when $h$ is a multiple of the span $\lambda$.
>
> **Proof:** The surrounding text states the theorem and explains its meaning; the source does not provide the full proof here.
>
> **Intuition:** After the transient beginning has disappeared, the expected renewal count in any fixed window of length $h$ is proportional to $h$.

1. If  $F$  is not arithmetic, then:

$$
\lim _ {t \to \infty} [ M (t + h) - M (t) ] = h / \mu
$$

2. If  $F$  is arithmetic, the same limit holds, provided  $h$  is a multiple of the span  $\lambda$ .

We see that the theorem distinguishes two cases: whether  $F$  is arithmetic or not. For our purposes,  $F$  not arithmetic means that the random variable, which describes the inter event time  $X$ , has a continuous distribution. In this case,


regardless of the value of $h$, the previous formulation of the theorem applies.
Whereas if $F$ is arithmetic and therefore $X$ distribution is discrete, the only possible values that $X$ can take are multiple of a common value named span and denoted by $\lambda$.
An issue with the granularity arises: $h$ can not be anything but a multiple of $\lambda$, otherwise some boundaries effect would make our thesis not true.
In conclusion the Renewal theorem states that the average increment of the process in an interval of length $h$, in the long run, is proportional to the length of this interval $h$ according to the constant $1/\mu$. This is valid for any $h$ if the $X$’s are continuous, while for $h$ such that are multiples of $\lambda$ if the $X$’s are discrete.

### Asymptotic results of N(t)

One other asymptotic result is: standardizing $N(t)$ by subtracting its asymptotic mean and normalizing to its standard deviation, it converges to the normal distribution:

$$
\lim_{t\to\infty}P\left[\frac{N(t)-t/\mu}{\sqrt{t\sigma^{2}/\mu^{3}}}\leqslant x\right]=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{x}e^{-y^{2}/2}dy
$$

### Asymptotic results of Age and Excess Life

Other useful results deal with the Limiting Distribution of Age and Limiting Distribution of Excess Life ($\gamma_{t}$).
Let us assume that the lifetimes $X_{i}$’s are continuous random variables with finite mean $\mu$. Let $\gamma_{t}=W_{N(t)+1}-t$ be the excess life at time $t$. The excess life has the limiting distribution:

$$
\lim_{t\to\infty}P[\gamma_{t}\leqslant x]=\frac{1}{\mu}\int_{0}^{x}[1-F(y)]dy
$$

This result, whose proof is not provided in the source, can be found once again by mean Renewal Argument.

We can now compute the corresponding density function which is the derivative of: $h(y)=\mu^{-1}[1-F(y)]$.
Its mean is:

$$
\mathbb{E}[\gamma_{t}] =\int_{0}^{\infty}yh(y)dy=\frac{1}{\mu}\int_{0}^{\infty}y[1-F(y)]dy=\frac{1}{\mu}\int_{0}^{\infty}y\left[\int_{y}^{\infty}f(t)dt\right]dy=
=\frac{1}{\mu}\int_{0}^{\infty}f(t)\left[\int_{0}^{t}ydy\right]dt=\frac{1}{\mu}\int_{0}^{\infty}\frac{t^{2}}{2}f(t)dt=\frac{\sigma^{2}+\mu^{2}}{2\mu}=\frac{\mathbb{E}[X^{2}]}{2\mathbb{E}[X]}
$$

The joint distribution of Residual life $P[\gamma_{t}\geqslant x]$ and Current life $P[\delta_{t}\geqslant y]$


is:

$$
\lim_{t\to\infty}P[\gamma_{t}\geqslant x\ ,\ \delta_{t}\geqslant y]=\lim_{t\to\infty}P[\gamma_{t-y}\geqslant x+y]=\mu^{-1}\int_{x+y}^{\infty}[1-F(z)]dz
$$
*Figure 5.14 -  $\{\delta_{t}\geqslant y\ \mbox{and}\ \gamma_{t}\geqslant x\}$ if and only if $\{\gamma_{t-y}\geqslant x+y\}$*

Where we require to see no events looking forward and looking backwards. It is equivalent of having no events in the interval of length $x+y$, once we have put ourselves in the instant $t-y$. But, as $t\to\infty$, $\gamma_{t}$ and $\gamma_{t-y}$ are the same distribution as long as $y$ is finite.

Consequently, for the marginal distribution we need to condition on either $x$ or $y$, in order to make it as the certain event.

As an example, if we want to compute the distribution for $\gamma_{t}$ we can pick $y=0$: we know that $\delta\geqslant 0$, thus we obtain the expression we have already computed. But, since (5.14) is symmetric wrt $x$ and $y$, we can pick $x=0$ as well and get the distribution for $\delta_{t}$:

$$
\lim_{t\to\infty}P[\delta_{t}\geqslant y]=P[\gamma_{t}\geqslant 0\ ,\ \delta_{t}\geqslant y]=\mu^{-1}\int_{y}^{\infty}[1-F(z)]dz=1-H(y)
$$

In conclusion, when in a Renewal Process we put ourselves at time $t$ and look forward and backwards we see the same statistics, as long as we are in the limit $t\to\infty$. Note that it does not apply any more the issue we faced for the Poisson processes, where the future was infinite and the past was not. Since $t\to\infty$, the past becomes infinite as well, thus solving our problem.

Based on this result, we can now write the Asymptotic expansion of the Renewal Function. Note that all the following arguments will have already assumed that $t\to\infty$. Recall that:

$$
\mathbb{E}[\gamma_{t}]=\frac{\mathbb{E}[X^{2}]}{2\mathbb{E}[X]}=\frac{\mu^{2}+\sigma^{2}}{2\mu}
$$

Let us introduce again $S_{N(t)+1}=t+\gamma_{t}$, whose expectation value is:

$$
\mathbb{E}[S_{N(t)+1}]=\mu(1+M(t))=\mathbb{E}[t+\gamma_{t}]=t+\mathbb{E}[\gamma_{t}]
$$

Where in the last passage we used the fact that $t$ is a constant.

We can substitute the expectation value for $\mathbb{E}[\gamma_{t}]$ with (5.15) and then divide


by $\mu$, thus rewriting:

$$
M(t)-\frac{t}{\mu}=\frac{1}{\mu}\mathbb{E}[\gamma_{t}]-1
\lim_{t\to\infty}\left(M(t)-\frac{t}{\mu}\right)=\frac{\sigma^{2}+\mu^{2}}{2\mu^{2}}-1=\frac{\sigma^{2}-\mu^{2}}{2\mu^{2}}
$$

See as the rhs is *constant*.
We can conclude by noting that in the asymptotic behavior of $M(t)$, the strongest term in $M(t)$ is *linear* in $t$. In other words $M(t)\sim t/\mu+o(t)+$ constant, where the other terms either go to infinity slower than the linear one, or are constant and of the kind we have found above.

### 5.6.2 Delayed Renewal Processes

We may want to introduce some variations on *Renewal Processes*, so let us consider the so-called *Delayed Renewal Processes*.
For definition it is a *renewal process* where all $X$’s after the first one are i.i.d. random variables. $X_{1}$ is still *independent* of the other $X$’s, but may have a *different distribution* $G$.

As an example, let us consider again a light bulb. Let us imagine that at time $t=0$ the bulb is *not new* any more. The following ones will have an "entire lifetime" distribution, whereas the *first one* will be *partial* and, in particular, it will be equal to the residual lifetime having it already been in operation for a while. So, unless the lifetime distribution is memoryless, $X_{1}$ will follow an other distribution. *After the first* renewal, where we install a new component, the *distribution will be the usual*, "complete" one. Such process is called *Delayed renewal process*.

For this kind of processes the number of renewals $M_{D}(T)=\mathbb{E}[N(t)]$ is no longer $M(t)=\sum_{k=1}^{\infty}F_{k}(t)$ as in normal renewal processes. The elementary renewal theorem now becomes:

$$
\lim_{t\to\infty}\frac{M_{D}(t)}{t}=\frac{1}{\mu}\qquad\text{where }\mu=\mathbb{E}[X_{2}]
$$

Where for a long time $t$ the actual distribution will depend only on the distribution of the $X$’s after the first renewal, or, in other words, on the common distribution $F(x)$ of $X_{2},X_{3}...$. Therefore the renewal theorem states that:

$$
\lim_{t\to\infty}[M_{D}(t)-M_{D}(t-h)]=\frac{h}{\mu}
$$

provided $X_{2},X_{3},...$ are continuous random variables.

We now study a particular case: let us the *initial distribution* (first life) have the *same distribution* function as for the *asymptotical residual life*:

$$
G(x)=\mu^{-1}\int_{0}^{x}[1-F(y)]dy
$$


This is called Stationary Renewal Process. Indeed it is the distribution for a renewal to occur once we have left it run for a long time.

Making this assumption at the very beginning of our process, it will be like as if our process will have started already following the asymptotic behavior for any values of  $t$  coming. Equivalently we can tell that the process started infinitely far in the past. Its properties will be the ones we have already found for the long run processes:

$$
M _ {D} (t) = \mathbb {E} [ N (t) ] = \frac {t}{\mu}
$$

and

$$
P [ \gamma_ {t} ^ {D} \leqslant x ] = G (x)
$$

for all  $t$ . Thus, what generally is only an asymptotic renewal relation now becomes an identity holding for all  $t$ , in a stationary renewal process.

### 5.6.3 Alternating Renewal Process

An other important type of renewal process, that is often found in exercise, is the so called Alternating Renewal Process.

Let us suppose that we have a renewal process with the usual sequence of  $X$ 's that represent the time intervals between two consecutive events. Let us suppose that  $Y_{i}$  represents a portion of the duration  $X_{i}$ , as depicted in the figure (5.15):
![[Stochastic_Processes_2020_p200_img73.jpeg]]
*Figure 5.15 - A renewal process in which an associated random variable  $Y$  represents a portion of the  $i$ -th renewal interval.*

We moreover assume that  $Y$ 's are i.i.d. as the  $X$ 's are, and in addition  $X_{j}$  and  $Y_{i}$  are independent of each other for all indexes such that  $i \neq j$ . In other words, the only dependent random variable are  $X_{i} = Y_{i}$ . One other obvious condition is that  $Y_{i}$  cannot exceed  $X_{i}$ .

Let us now compute the probability that picking a random time  $t$  it will fall into an  $Y_{i}$  interval, rather than its complementary  $X_{i} - Y_{i}$ . In other words, we want to know the fraction of times the system is in state 1 (ON state), having denoted  $Y_{i}$  in this way, rather than in the remaining interval having it labelled as state 0 (OFF state). In particular we are looking for these fractions in the limit  $t \to \infty$ , taking into account that all these ON/OFF cycles are


independent of each other and have the same distributions.

Let  $p(t)$  the probability that  $t$  falls in a portion denoted by  $Y_{i}$  (ON state). When  $X_{1}, X_{2}, \ldots$  are continuous random variables, the renewal theorem implies the following important asymptotic evaluation:

$$
\lim _ {t \to \infty} p (t) = \frac {\mathbb {E} [ Y _ {1} ]}{\mathbb {E} [ X _ {1} ]}
$$

One should have noticed that this is the fraction of time that the system is in  $ON$  state during each cycle/renewal interval. Moreover, it is reasonable that a long run behavior, that is  $\lim_{t\to \infty}p(t)$ , will reduce to a simple fraction: different intervals of the renewal processes are statistically equivalent. Each one of them is thus representative for the whole process, which is the repetition of identically distributed and independent intervals. When we know what happens in a single interval, anything about the whole process will be characterized as well being it its repetition. This is indeed a very important example, and many times there are exercises where we need to apply this result.
![[Stochastic_Processes_2020_p201_img74.jpeg]]
*Figure 5.16 - A system can be either in  $BUSY$  or in  $IDLE$  state, depending on the presence of users.*

A Queueing Model Let us now study again a queueing model, but using Renewal processes formalism.

Recall that a queueing process is a process in which customers arrive at some designated place where a service of some kind is being rendered. When an user arrives, the service will take place until the last customer leaves the system. For some times then the system will be empty, and after one other arrival the service will start again.

As depicted in fig.(5.16), we can tell two different different type of intervals: IDLE when no users are there, and BUSY when service is taking place. We have already discussed that, once there is an arrival in an empty system, those are renewal instants, whereas the moments where the system empties may be renewal instants as well, as long as inter arrival times are memoryless.

This labelling leads us to a Delayed Renewal process, having the first interval a distribution different from the others. Each cycle repeats for ever, and it starts with a  $BUSY$  state before being  $IDLE$  and so forth. A very common question is to compute the fraction of time spent by the system in the two different states. The answer is the ratio between the average of the  $BUSY$  and  $IDLE$  intervals, once we have been able to characterize these time


intervals. Formally:

$$
\lim_{t\to\infty}p(t)=\frac{\mathbb{E}[BUSY]}{\mathbb{E}[BUSY+IDLE]}
$$

As a Network-fashioned consideration, note that when the system is busy, it produces useful work. As an example we can consider a server that can send some data out of a node. If there is no data, the server is still able to send in principle, but cannot send anything because there is nothing to be sent (IDLE). On the other hand, if data is present, the server will be BUSY until it will have sent all the data out of the node, producing some useful work. The traffic that the system will handle usefully will be the datarate available, that is a specific of the system, times the probability that the system is busy, that is the probability above.

### 5.6.4 Proof of basic limit theorem for M.C.

Now that we have studied Renewal and Delayed Renewal processes we are finally able to proof the Basic Limit Theorem for Markov Chains. We recall that the theorem statement is the following:


> [!Important] Theorem - Basic Limit Theorem for Markov Chains via Renewal Theory
> **Statement:** For a recurrent irreducible and aperiodic Markov chain, or equivalently for a recurrent and aperiodic class,
>
> $$
> \lim_{n\to\infty}P_{jj}^{(n)}=\lim_{n\to\infty}P_{ij}^{(n)}=\pi_{j}=\frac{1}{\sum_{n=1}^{\infty}nf_{jj}^{(n)}}=\frac{1}{m_{j}}.
> $$
>
> **Proof:** The full renewal-theoretic proof is transcribed below.
>
> **Intuition:** Visits to a recurrent state form a renewal process; the long-run probability of being in that state is therefore the reciprocal of the mean return time.

For a recurrent irreducible and aperiodic Markov Chain or, equivalenty, for a recurrent and aperiodic class it holds that:

$$
\lim_{n\to\infty}P_{jj}^{(n)}=\lim_{n\to\infty}P_{ij}^{(n)}=\pi_{j}=\frac{1}{\sum_{n=1}^{\infty}nf_{jj}^{(n)}}=\frac{1}{m_{j}}
$$


In order to prove the theorem, let us first fix a time $t$ and introduce the number of visits to state $j$ up to time $t$: namely $N_{j}(t)$. Note as $j$ is recurrent since it belongs to a recurrent class.
Now, in the case that the chain starts at state $j$, then $N_{j}(t)$ is a traditional renewal process, being the initial and final states the same. The distribution of interevent times is therefore discrete: every time we visit state $j$ there is a renewal, and by the Markov property every visit is a renewal itself. Obviously, we can return only in a discrete non-negative number of steps not less than 1: the recurrence time or inter event time is an integer, positive random variable. Using the terminology of renewal theory, the distribution of inter event times $X$’s is arithmetic with span $\lambda=1$. Inter event times can be obviously only multiple of this number.
Renewal theorem ensures us that, for any increment $h$ that is multiple of the span, we have:

$$
\lim_{t\to\infty}[M(t+h)-M(t)]=h/\mu
$$

Where we need to tell what is $\mu$.
Now one should note that the increment in a single time unit step $N_{j}(n)$ can


be rewritten as the sum:

$$
N_{j}(n)=N_{j}(n-1)+\mathbb{1}[X_{n}=j]
$$

Where the indicator function denotes the possible visit to state $j$ at time $n$, that may or may not occur. Let us take now the expectation value of the equation (5.16), conditioned on the initial state $X_{0}=j$.

$\mathbb{E}[\mathbb{1}[X_{n}=j]]$ is the probability of being in state $j$ at a time step $n$, given it started in $j$ at time $0$. Whereas $\mathbb{E}[N_{j}(n)]=M(n)$, being it a renewal process. We obtain:

$$
\mathbb{E}[\ \mathbb{1}[X_{n}=j|X_{0}=j]\ ]=P_{jj}^{(n)}=M(n)-M(n-1)\xrightarrow{n\to\infty}\frac{1}{m_{j}}
$$

One should note that, taking the limit as $n\to\infty$, the time span of this difference $M(n)-M(n-1)$ is indeed a multiple of $h=\lambda=1$. Therefore the hypotheses of Renewal theorem hold, and the latter can be applied. We can obtain the mean $\mu=m_{j}$ from the comparison of the two expressions above. This means that, given we start our process in state $j$, the mean $\mu$ is the average recurrence time $m_{j}$. Hence the probability for large $n$ to return in state $j$, once we have started in it, is the inverse of the average recurrent time.

Now let us consider the case where the chain is *periodic* with period $d$. We can take the difference between the counters in two different moments:

$$
N_{j}(nd)-N_{j}(nd-d)=\sum_{i=nd-d+1}^{nd}\mathbb{1}[Y_{i}=j]
$$

that is equal to the sum of indicators function in the times between $[nd-d+1,nd]$. Because of the periodicity, in the case where we start at state $j$ all the terms in the sum are $0$ except the one $i=nd$: we cannot visit that state in a time-step different than a multiple of the period.

Now we take the expectation of both members in (5.17) and condition onto the fact that we have started in $Y_{0}=j$. We finally obtain a similar expression to the one we have already seen, that differs only by the times difference that now is a period $d$:

$$
\mathbb{E}\left[\sum_{i=nd-d+1}^{nd}\mathbb{1}[Y_{n}=j|Y_{0}=j]\ \right]=P_{jj}^{(nd)}=M(nd)-M(nd-d)\xrightarrow{n\to\infty}\frac{1}{m_{j}}
$$

Obviously, being the chain periodic, the average return times will be a multiple of the period $d$. The span for this case will be $\lambda=d$ that is equal to the time difference $h$ itself: $h=\lambda=d$. Therefore the Renewal theorem can be applied, and thus we obtain the result we have already found for the periodic case.

Note that, up to now, we only have proved a little piece of the equations in the statement of the theorem, namely for the *aperiodic* case when we start in $j$:

$$
\lim_{n\to\infty}P_{jj}^{(n)}=\frac{1}{m_{j}}
$$


Now we want to start in a state $i\neq j$, and so prove that:

$$
\lim_{n\to\infty}P^{(n)}_{jj}=\lim_{n\to\infty}P^{(n)}_{ij}
$$

For this case we note that $N_{j}(t)$ is a *delayed* renewal process: all $X$’s except the very first one are equal to a return time $j\to j$. The initial $X_{1}$ will be instead the first passage time $i\to j$, so it will have a different distribution from the other $X$’s. Finally, being a delayed renewal process, we know that the same-as-before asymptotic results apply regardless of the choice of state $i$, by simply applying the same arguments. We have not made any statement about the way passages to state $j$ occur, and so the renewal process may be of *any* kind. In this way we have shown that the limit (5.18) is not dependent on the starting state as long as it belongs to the same class, thus concluding our proof.

$$
\square
$$

## 5.7 Renewal Reward Processes

A large number of probability models are special cases of the following model. Consider a renewal process $\{N(t),t\geqslant 0\}$ having interarrival times $X_{n},n\geqslant 1$ with common distribution $F$, and suppose that each time a renewal occurs we receive a reward. Other equivalent statements may refer to rewards as *metric*, or *cost*. We denote by $\mathbf{R_{n}}$ the reward earned at the time of the $n$-th renewal: it can be earned at different times of the renewal interval, and so different models can be implemented, but asymptotic results are still unique despite of this choice.

We shall assume that the $R_{n},n\geqslant 1$, are independent and identically distributed. However, we do allow only for the possibility that $R_{n}$ *may depend on the correspondent* $X_{n}$, that is the length of the $n$-th renewal interval, *and nothing more*. A natural consequence is that the pairs $(X_{n},R_{n}),\ n\geqslant 1$ are i.i.d..

We can now compute how much reward we have accumulated up to time $t$, and it is:

$$
R(t)=\sum_{n=1}^{N(t)}R_{n}
$$

Note as this equations is correct as long as we assume that we earn the correspondent reward $R_{i}$ only at the *end* of a certain renewal interval $X_{i}$. Then we define:

$$
\mathbb{E}[R]=\mathbb{E}[R_{n}]\qquad\mathbb{E}[X]=\mathbb{E}[X_{n}]
$$

where both $R$ and $X$ have lost their index because are i.i.d..

One of the main results in *Reward* theory is the following theorem:


> [!Important] Theorem 5.7.1 - Renewal Reward Theorem
> **Statement:** If $\mathbb{E}[R]<\infty$ and $\mathbb{E}[X]<\infty$, then:
>
> $$
> \frac{R(t)}{t}\to\frac{\mathbb{E}[R]}{\mathbb{E}[X]}\quad\text{with probability 1}
> $$
>
> and:
>
> $$
> \frac{\mathbb{E}[R(t)]}{t}\to\frac{\mathbb{E}[R]}{\mathbb{E}[X]}.
> $$
>
> **Proof:** The proof for the almost-sure statement is transcribed below; the source states that the proof for the expectation statement is not provided in the source.
>
> **Intuition:** A long run is made of many statistically identical renewal cycles, so reward per unit time converges to reward per cycle divided by time per cycle.

If $\mathbb{E}[R]<\infty$ and $\ \mathbb{E}[X]<\infty$, then:

1. with probability 1, it holds that the average number of rewards per unit time in the long run is:

$$
\frac {R (t)}{t} \rightarrow \frac {\mathbb {E} [ R ]}{\mathbb {E} [ X ]} \quad \text{as } t \rightarrow \infty
$$

2. the same result applies to the function  $\mathbb{E}[R(t)]$  in the limit:

$$
\frac {\mathbb {E} [ R (t) ]}{t} \rightarrow \frac {\mathbb {E} [ R ]}{\mathbb {E} [ X ]} \quad \text{as } t \rightarrow \infty
$$

Proof. In order to prove 1), we can rewrite:

$$
\frac {R (t)}{t} = \frac {\sum_ {n = 1} ^ {N (t)} R _ {n}}{t} = \left(\frac {\sum_ {n = 1} ^ {N (t)} R _ {n}}{N (t)}\right) \left(\frac {N (t)}{t}\right)
$$

Recall that in the limit  $N(t) \xrightarrow{t \to \infty} \infty$  with probability 1. Applying the strong law of large numbers we obtain for the first factor:

$$
\frac {\sum_ {n = 1} ^ {N (t)} R _ {n}}{N (t)} \rightarrow \mathbb {E} [ R ] \quad t \rightarrow \infty
$$

and by the same law for renewal processes:

$$
\frac {N (t)}{t} \rightarrow \frac {1}{\mathbb {E} [ X ]} \quad t \rightarrow \infty
$$

thus ending the proof for 1).

The proof for 2) is not provided in the source. One should note that is not so obvious: the reason is that if a limit is true in the probabilistic way, it does not imply the same result when taking the true limit, thus needing to be shown.

$\frac{R(t)}{t}$  can be interpreted as the average reward per unit time, but we can also compute the average reward per some other quantities but the time, so using a different metric. As an example we can compute the average energy spent per correctly delivered packet, a relevant quantity in packet transmission systems. In this way we end up having the average metric of one kind per unit of another metric.

This situation is described in the following corollary:

Corollary. Let  $R_{1}(t)$  and  $R_{2}(t)$  be two reward functions. Then:

> [!Important] Corollary - Ratio of Two Renewal Rewards
> **Statement:** For two reward functions $R_1(t)$ and $R_2(t)$, the long-run ratio is the ratio of their one-cycle expectations.
>
> $$
> \frac{R_1(t)}{R_2(t)}\xrightarrow{t\to\infty}\frac{\mathbb{E}[R_1]}{\mathbb{E}[R_2]}.
> $$
>
> **Intuition:** The common renewal time scale cancels when comparing two accumulated rewards.

$$
\frac {R _ {1} (t)}{R _ {2} (t)} \xrightarrow {t \to \infty} \frac {\mathbb {E} [ R _ {1} ]}{\mathbb {E} [ X ]} \frac {\mathbb {E} [ X ]}{\mathbb {E} [ R _ {2} ]} = \frac {\mathbb {E} [ R _ {1} ]}{\mathbb {E} [ R _ {2} ]} \quad \text{with probability 1}
\frac {\mathbb {E} [ R _ {1} (t) ]}{\mathbb {E} [ R _ {2} (t) ]} \xrightarrow {t \to \infty} \frac {\mathbb {E} [ R _ {1} ]}{\mathbb {E} [ R _ {2} ]} \quad \text{with probability 1}
$$

3recall that $R(t)$ is indeed a random variable in $t$


Where  $R_{1}(t)$  and  $R_{2}(t)$  can be any metric.

As an example if  $R_{1}(t)$  is the energy spent and  $R_{2}(t)$  is the number of the correctly distributed packets up to time  $t$ , then the energy per packet will be the ratio between these two quantities.

Once again we see that what happens in an infinitely long evolution time, is the same as for  $\frac{R(t)}{t}$ : it is totally represented by metric valid at the shorter renewal interval level. This is because a renewal process repeats for ever intervals that are statistically identical, therefore a metric computed on one of them is representative for the overall evolution of the process.

### 5.7.1 Regenerative processes

Let us consider a stochastic process  $\{X(t), t \geqslant 0\}$  with state space  $\{0,1,2,\ldots\}$  having the property that there exist time instants at which the process (probabilistically) restarts itself. That is equivalent to say that, with probability 1, we can find a time  $S_{1}$  such that the continuation of the process beyond  $S_{1}$  is a probabilistic replica of the whole process starting from 0. If the process was in state  $j$  at the beginning, there will be a moment  $S_{1}$  when the process will be in state  $j$  and restart again.

Note that it is a necessary condition, and not a sufficient: being in the same state as the starting one does not imply that the evolution will be identically to the one as if we have started anew. There is one exception indeed, that are the Markov Chains: when we find ourselves in the same state as the initial one, we know that is sufficient to say that the process will renew itself from that point on.

Now we want to state the relationship between the a Renewal process and a Regenerative process. The latter refers to the actual evolution of the process.
![[Stochastic_Processes_2020_p206_img75.jpeg]]
*Figure 5.17 - In a regenerative process, when we sit at the starting point  $t = 0$ , or at  $S_{1}$  or  $S_{2}$  it does not make any difference when we look forward to the statistically evolution of the process. Note that we may visit  $j$ -th state at some instants that does not necessarily are regeneration instants. This would be actually different for a Markov chain.*

Note as every regenerative process contains a renewal process: the instants at which the process regenerates are renewal instants. However the renewal process only counts time and tells where renewal instants are, whereas the regenerative process has more than only the renewal structure. It refers to the actual evolution of the process as well, that can take only integer-valued states: regenerative process has got in addition the statistics of the different states and hence the evolution among them.


Let  $X$  be a renewal process. In each renewal interval we can define some portion that we label with  $Y_{i}$ . This should remind us of Alternating processes, where  $X_{i}$  and  $Y_{i}$  started at the same time instants, and so  $Y_{i}$  belong to the initial part of the renewal interval  $X_{i}$ .

Now, instead, the only condition for every  $Y_{i}$  is that the sum of its corresponding disjoint intervals must be a number between 0 and  $X_{i}$ .
![[Stochastic_Processes_2020_p207_img76.jpeg]]
*Figure 5.18 - A more general formulation for an alternating process, where the "ON" states may be disjoint and more than one per renewal interval.*

We want to compute the probability for the process to be in an interval labelled with  $Y$ . We denote it this probability by  $p(t)$ , and it can be found using the renewal argument:

$$
p (t) = P [ t \text {f a l l s i n} Y ]
$$

and in the limit:

$$
\lim  _ {t \to \infty} p (t) = \frac {\mathbb {E} [ Y ]}{\mathbb {E} [ X ]}
$$

These results are true even if  $Y_{i}$  are disconnected.

For a Regenerative process we want indeed to know what is the probability, in the limit as  $t \to \infty$ , for the system to be in state  $j$ . It is indeed the ratio of two local quantities, that refer to a single cycle. By cycle we mean every interval of time between two regeneration instants: it is a renewal interval. We can write:

$$
\lim  _ {t \rightarrow \infty} P [ X (t) = j ] = \frac {\mathbb {E} [ \text {t i m e i n} j \text {d u r i n g a c y c l e} ]}{\mathbb {E} [ \text {t i m e o f a c y c l e} ]}
$$

In order to compute  $\mathbb{E}[\text{time in } j \text{ during a cycle}]$  we sum all the time spent in a certain regenerative state during a whole cycle, and then take the expectation value.

The proof for this statement is a direct consequence of the result for the alternating processes: if we label with  $Y$ 's the time spent in the regenerative state, then we will obtain the same results we mentioned above where  $\mathbb{E}[\text{time in } j \text{ during a cycle}] = \mathbb{E}[Y]$ .

The same limit applies to the total amount of time that system spends in state  $j$  in an interval of length  $t$ . Then, the long run average:

$$
\lim  _ {t \rightarrow \infty} \frac {\text {t i m e i n} j \text {i n} [ 0 , t ]}{t} = \frac {\mathbb {E} [ \text {t i m e i n} j \text {d u r i n g a c y c l e} ]}{\mathbb {E} [ \text {t i m e o f a c y c l e} ]} \quad \text {w i t h p r o b .} 1
$$

This result is very similar to what happens in ergodic systems, where in the long run the statistical quantities (i.e. the probabilities) and time averages


actually *coincide*. In addition, these quantities would usually depend on the initial state, but if we let the process run for a while this information will be irrelevant as long as we passed a renewal instant. So, after a renewal instant, these quantities are independent of the initial state.

## 5.8 Semi-Markov Processes

Semi-Markov processes can be seen as a generalization for Markov chains: we indeed drop the requirement that each transition will take exactly one time unit. In fact for a Semi-Markov process *durations for each transition can be random*.
More specifically, let us consider a stochastic process with states $0,1,...$ which is such that, whenever it enters state $i$ ($i\geqslant 0$) we have for the evolution of our process:

1. the next state it will enter is any state $j$ with probability $P_{ij},i,j\geqslant 0$
2. given that the next state to be entered is state $j$, the time for the transition $i\to j$ to occur has distribution $F_{ij}$

Different transitions may have different duration statistics. If we denote by $Z(t)$ the state at time $t$, then $\{Z(t),t\geqslant 0\}$ is called a *semi-Markov process*. Note that now we take into account the *actual* time $t$, as well.
Therefore $Z(t)$ does not possess the Markovian property: if we knew the state at a certain time $t$, *we need to know also how long we have been there up to time $t$ in order to fully determine the future evolution of the system*. It is indeed the same reason why the $M/G/1$ model was not a Markovian process: it is peculiar of processes that are not memoryless. Information on how much time we have been in a state is relevant as well.
Conversely, a Markov chain can be seen as a special case of the semi-Markovian processes where:

$$
F_{ij}(t)=\begin{cases}0&t<1\\
1&t\geqslant 1\end{cases}
$$

that is, *all transition times of a Markov chain are identically 1*.

An other special case is when in *semi-Markov process* transition times are exponentially distributed each with its own parameter. *This kind of process possesses the Markov property* because of the memorylessness of the exponential distribution. Therefore, it would be sufficient for us to know only in which state we are at the moment in order to fully determine the evolution of the system.

Up to this moment we have analyzed the process and tried to find the distributions $F_{ij}$ once the transition $i\to j$ has been given, where $j$ can be *any*. Let us now do the other way round: we want to know how much time we will spend in state $i$ before making a generic transition. We denote this


quantity by $H_{i}$, and it can be computed by conditioning $F_{ij}$ on all possible next states $j$, times the probabilities of the transition:

$$
H_{i}(t)=\sum_{j}P_{ij}F_{ij}(t)
$$

We can denote its mean by $\mu_{i}$, and it is computed by:

$$
\mu_{i}=\int_{0}^{\infty}xdH_{i}(x)
$$

Let now take the ordered sequence of all states visited during the evolution of the process and denote it by $X_{n}$, where we ignore the time at which transitions occurred. This is called the Embedded Markov Chain of the semi-Markov process.

The next state we will visit, given we are in $i$, is fully determined by probabilities $P_{ij}$. Thus $X_{n}$ is a Markov chain itself, and can be seen as a sampled version of the semi-Markov process at transition times. Now we choose the $i$-th state and look at the time when the process makes the transition into state $i$, then $T_{ii}$ is the time between successive transitions into a single state $i$ and $\mu_{ii}=\mathbb{E}[T_{ii}]$ is its expected value.
![[Stochastic_Processes_2020_p209_img77.jpeg]]
*Figure 5.19 -  Z(t) is a semi-Markov process, every time there is a transition to state $i$ a new cycle begins and so those are regenerative instants. Note as it may happen that between two consecutive renewal instants we do not visit any other state (see $S_{2},S_{3}$).*

As depicted in figure (5.19), every time we enter state $i$ the process restarts as if anew. More generally, a semi-Markov process is a regenerative process with the property: every cycle starts when we enter state $i$, then we may either remain for some times or some cycles or move away from it, until we go back to $i$ and the process restarts.

We have defined $\mu_{i}$ as the average time in $i$ before making a transition, whereas $\mu_{ii}=\mathbb{E}[S]$ is the average time between consecutive visits to state $i$, and so the average duration of a cycle. We can write now the long run probability that our process at time $t$ is in state $i$, given in started in $j$:

> [!Important] Theorem - Long-Run State Probability in a Semi-Markov Process
> **Statement:** For a semi-Markov process, the long-run probability of being in state $i$ is:
>
> $$
> \lim_{t\rightarrow\infty}P[Z(t)=i|Z(0)=j]=P_{i}=\frac{\mu_i}{\mu_{ii}}.
> $$
>
> **Intuition:** The process regenerates at visits to $i$; the probability of observing $i$ is the average time spent in $i$ during a cycle divided by the average cycle length.

$$
\lim_{t\rightarrow\infty}P[Z(t)=i|Z(0)=j]=P_{i}=\frac{\mu_{i}}{\mu_{ii}}
$$

It is clearly an alternating process, where the "ON" state is $i$ and $\mu_{i}$ the average time spent in the latter. On the other hand, the average duration of a cycle is $\mu_{ii}$. Its ratio will be therefore the long run probability for the process to be in state $i$.


Similarly, we want now to sum all the time intervals that we spent in state $i$ up to a fixed time $t$, thus obtaining the total time spent in state $i$. Dividing this amount by $t$ we obtain the fraction of time that our system spends in state $i$. In the limit:

$$
\lim_{t\to\infty}\frac{\text{total time in state in }}{t}=\frac{\mu_{i}}{\mu_{ii}}\quad\text{with prob. 1}
$$

Once again we notice that the total time average that the process spends in state $i$, in the long run, is equal *with probability* 1 to the probability of finding the process in the same state.

The only problem in these results is that, despite theoretically are very useful, practically the averages $\mu_{ii}$ are very *difficult to compute*. We would need to take into account, once have started in state $i$, all possible evolutions that soon or later would lead us to the same state $i$ after different time intervals. Its number, as one can easily understand, is really huge, except some particular cases.

On the other hand, $\mu_{i}$ can be easily found once we know the process and the time distribution $F_{ij}$ with the correspondent probabilities $P_{ij}$ and lastly averaging over $j$, unless some technical difficulties. This is why $P_{i}$ needs to be computed in a different, easier, way as we will see.

### 5.8.1 Some clarifications on Regenerative and Semi-Markov Processes

In this paragraph we will briefly clarify some results we have obtained so far. Regarding Regenerative processes in the long run we have that:

$$
\lim_{t\to\infty}P[X(t)=j]=\frac{\mathbb{E}[\text{time in during a cycle}]}{\mathbb{E}[\text{time of a cycle}]}
$$

This last result relies directly on the generalization we have made for *Alternating processes*, where we labelled some portions of larger intervals $X_{i}$ by using $Y_{i}$ (fig. 5.18). In the long run, the process will have the probability to find itself in a portion $Y$, that is equal to the ratio between the average duration of time intervals $\mathbb{E}[Y]$ normalized to the average duration of an entire cycle $\mathbb{E}[X]$. The second result we stated, that is the time average of the fraction of time that the process spends in $j$, is indeed a direct consequence of first point of the theorem (5.7.1) for the *Renewal reward processes*. Since reward can be any, as long as its expectation is finite, we choose to take as reward the *amount of time* that the process spends in $j$. $R_{n}$ will be therefore, for every renewal interval, the *total time* that the process will spend in time $j$. It follows from the i.i.d. property that $R_{n}=R$, and so it can be generalized.

Using these arguments we can write:

$$
\lim_{t\to\infty}\frac{R(t)}{t}=\lim_{t\to\infty}\frac{\text{time spent in in }}{t}=\frac{\mathbb{E}[\text{time spent in during a cycle}]}{\mathbb{E}[\text{time of a cycle}]}\quad\text{with prob. 1}
$$


that is equal to the ratio of the two expectations values, following from the property of Renewal Rewards processes.

Similarly for a Semi-Markov process we have that:

$$
\lim_{t\to\infty}P[Z(t)=i|Z(0)=j]=P_{i}=\frac{\mu_{i}}{\mu_{ii}}
$$

this also comes from the special case of Alternating processes we have already studied. The state $i$, we are interested in, is now at the beginning of the renewal interval (see fig. 5.15).

The second result:

$$
\lim_{t\to\infty}\frac{\text{total time in state in }}{t}=\frac{\mu_{i}}{\mu_{ii}}\quad\text{with prob. 1}
$$

can be obtained as well by defining as reward $R(t)$ the time spent by the system in state $i$, that is positioned at the beginning of the renewal interval, and finally invoking the theorem (5.7.1).

A semi-Markov process is a special case of a regenerative process: every time it lands in a certain state, $i$ is a regenerative instant. Because of the Markovian property the future evolution of the system will be independent of the past, and so it is like as if the process renews starting from those instants.

We assumed up to now that landing in a given state $i$ would bring us back as if starting from time $0$. This is true only if we consider $0$ as a renewal instant itself, but we may have defined an other state $j$ as a reference.

It is actually possible to generalize to the case where we start in a state $i$ different from the regenerative state $j$, so the moments when we come to $j$ are statistically indistinguishable. This is true for both Regenerative and Semi-Markov processes. We should note, however, that the first renewal interval is indeed different from the others as it was for the Delayed Renewal processes. In fact, once we have started in state $i$, we still need some time in order to land in the regenerative state $j$. From that moment on, by the way, renewal intervals will be i.i.d. and different from the first one.

### 5.8.2 Semi-Markov process probabilities

We are now interested in computing the long run probabilities for Semi-Markov processes, or in other words their asymptotic behavior. We will study first the independent problem, and later on see how this assumption has affected our computation.

Let $X_{n}$ be a usual Markov chain, and let us define some metrics $r_{n}$ (reward) associated to transition. In particular, let us introduce the random variable:

$$
r_{ij}=\text{ reward for transition }i\to j
$$

Its expectation value will be:

$$
R_{ij}=\mathbb{E}[r_{ij}]
$$


The key assumption for our argument is if we fix the transition $i\to j$, and so $i$ and $j$ are given, then $\mathbf{r_{ij}}$ is independent of all the rewards for all the other transitions. In other words, both all past and future transitions will not affect in any measure the reward we obtain in the present step from $i\to j$. Clearly, after some time passes, we will have earned some reward when going for the first time to state $j$, which has been accumulated through the all transitions started from state $i$ up to that moment. We can define then:

$$
\theta_{ij}=\text{ total reward earned going from to for the first time}
$$

which in turn is a random variable: both rewards and evolution among states are random variables themselves. Its expectation value is then:

$$
\rho_{ij}=\mathbb{E}[\theta_{ij}]
$$

Instead of fixing our initial state, in this case $i$, we can find the average reward obtained by visiting a given state and leaving for any other one averaging over $j$ the weighted probabilities:

$$
R_{i}=\sum_{k}P_{ik}R_{ik}=\text{ average reward for visiting state }
$$

We can compute then:

$$
\theta_{ij}=\begin{cases}r_{ij}&\text{with prob. $P_{ij}$}\\
r_{ik}+\theta_{kj}&\text{with probab. $P_{ik},k\neq j$}\end{cases}
$$

In the first case we directly reach the final state $j$ with a single transition, while in the second one we need to average over all possible transitions that in more than one step will lead us to $j$, through some intermediate states $k$.

Thanks to the first step $i\to k$ we will earn the reward $r_{ik}$ and, later on, a total of $\theta_{kj}$ for reaching $j$ for the first time. Taking the expectation value for both sides, applying its definition and finally using the first step analysis for a generic transition $i\to k$:

$$
\rho_{ij}=\mathbb{E}[\theta_{ij}]=\sum_{k=0}^{\infty}\mathbb{E}[\theta_{ij}|X_{1}=k]P_{ik}=\overbrace{R_{ij}P_{ij}}^{k=j}+\sum_{k\neq j}(R_{ij}+\rho_{ik})P_{ik}=
$$

Including the $k=j$ term in the sum, we obtain:

$$
\sum_{k=0}^{+\infty}R_{ik}P_{ik}+\sum_{k\neq j}\rho_{ik}P_{ik}=R_{i}+\sum_{k\neq j}\rho_{kj}P_{ik}
$$

where the first term is the definition for $R_{i}$, that is the reward obtained for visiting $i$-th state.

Thus we can write the following set of equations, valid for any $i$, $j$ and


moreover for any metric $r_{ij}$, since we have not made assumptions up on it:

$$
\rho_{ij}=R_{i}+\sum_{k\neq j}P_{ik}\rho_{kj}\quad\forall i,j
$$

Now let us assume that the Markov chain $X_{n}$ is recurrent and irreducible, so we are allowed to define its stationary probability:

$$
\pi_{i}=\lim_{n\to\infty}P[X_{n}=i|X_{0}=j]
$$

Averaging (5.20) wrt state $i$ and left-multiplying by $\pi_{i}$ its both sides, we obtain:

$$
\sum_{i}\pi_{i}\rho_{ij}=\sum_{i}\pi_{i}R_{i}+\sum_{i}\pi_{i}\sum_{k\neq j}P_{ik}\rho_{kj}=\sum_{i}\pi_{i}R_{i}+\sum_{k\neq j}\rho_{kj}\sum_{i}\pi_{i}P_{ik}
$$

where the second sum over $i$ is the solution of the stationary equations, namely $\pi_{i}$. We obtain:

$$
\sum_{i}\pi_{i}\rho_{ij}=\sum_{i}\pi_{i}R_{i}+\sum_{k\neq j}\pi_{k}\rho_{kj}
$$

The first and the third sums are actually the same one: index for the first is $i$, while for the second is $j$, except for a unique term that does not cancels out. This term is obviously the one where $k=j$, and so we can write:

$$
\pi_{j}\rho_{jj}=\sum_{i}\pi_{i}R_{i}
$$

Recall that we have not made any assumption about the reward: now we interpret it as the time. This would make our model a semi-Markov chain model: beside an underlying Markov model, we assign to each transition a metric with the meaning of time.
As for the lhs of (5.21), $\rho_{jj}$ can be interpreted as the metric we accumulate returning the first time to $j$ once we started from $j$. Specially for this metric this will be the overall time passed from starting to $j$ and returning back, that is $\mu_{jj}$. Whereas $R_{i}$ will be the time spent in state $i$ once we make a transition to it.
It holds that, under the assumption of the time metric:

$$
\pi_{j}\mu_{jj}=\sum_{i}\pi_{i}\mu_{i}
$$

In this way we can compute in an easier way the limiting probability $P_{j}$ (5.19), that before we told it was difficult to find.
The ratio (5.19) now becomes, thanks to (5.22):

> [!Important] Formula - Semi-Markov Long-Run Distribution from the Embedded Chain
> **Statement:** If $\pi_j$ is the stationary probability of the embedded Markov chain and $\mu_j$ is the mean sojourn time in state $j$, then:
>
> $$
> P_j=\frac{\pi_j\mu_j}{\sum_i\pi_i\mu_i}.
> $$
>
> **Intuition:** A state is seen often in real time when it is visited often and when each visit lasts a long time.

$$
P_{j}=\frac{\mu_{j}}{\mu_{jj}}=\frac{\pi_{j}\mu_{j}}{\sum_{i}\pi_{i}\mu_{i}}
$$

One should note that the probability $\mathbf{P_{j}}=\lim_{t\to\infty}P[Z(t)=j]$ is proportional both to how frequently state $j$ is visited (namely $\pi_{j}$) and how long each


visit is (i.e. $\mu_{j}$). As we have seen, $\pi_{j}$ is the stationary distribution of the embedded Markov chain that just counts the visits to state $j$.

It is quite obvious that, in the limit, the probability to find our system in a certain state will be proportional to the frequency of visits for each state and how much time we spend in it before making a transition. $P_{j}$ is a distribution, being it in addition normalized: at the denominator we have $\sum_{i}\pi_{i}\mu_{i}$.

This term can be in principle easily computed: recall that for defining a semi-Markov chain we do need information about both the transition probabilities $P_{ij}(t)$, that is the embedded Markov Chain, and the distribution of time transitions $F_{ij}$. Out of these, we have all the information required to compute distribution of time that the process spends in state $i$:

$$
H_{i}(t)=\sum_{j}P_{ij}F_{ij}(t)
$$

and in turn its mean $\mu_{i}$. The normalization term finally follows from the information we were given.

Let us consider now a semi-Markov process and let us run for some time $t$, making a generic number of transitions. Let us moreover consider a generic metric $r_{ij}$, as before, and let $R(t)$ be the accumulated value of this metric up to time $t$. We have that the total reward per unit time:

$$
\lim_{t\rightarrow\infty}\frac{R(t)}{t}=\frac{\mathbb{E}[R]}{\mathbb{E}[X]}\quad\text{with prob. 1}
$$

That is a known result from the theory of Renewal reward processes. In addition in holds that:

$$
\lim_{t\rightarrow\infty}\frac{\mathbb{E}[R(t)]}{t}=\frac{\mathbb{E}[R]}{\mathbb{E}[X]}
$$

Where in this case $\mathbb{E}[R]=\rho_{jj}$ is the average reward in a cycle, while $\mathbb{E}[X]=\mu_{jj}$ is the average cycle duration. Thus:

$$
\frac{\mathbb{E}[R]}{\mathbb{E}[X]}=\frac{\rho_{jj}}{\mu_{jj}}=\frac{\sum_{i}\pi_{i}R_{i}/\pi_{j}}{\sum_{i}\pi_{i}\mu_{i}/\mu_{j}}=\frac{\sum_{i}\pi_{i}\sum_{k}P_{ik}R_{ik}}{\sum_{i}\pi_{i}\sum_{k}P_{ik}\mu_{ik}}
$$

where we substituted the values we have just computed, and applied the definitions for $R_{i}$ and $\mu_{i}$. Recall that:

$$
\mu_{ik}=\mathbb{E}[\text{expected duration of transition }i\rightarrow k]=\int_{0}^{\infty}xdF_{ik}(x)
$$

Note as in (5.23) the dependence on $\pi_{j}$ disappears while taking the ratio: we are trying to compute the long run average reward per unit time. We may take different reference states, which in this case is $j$, but could be any: $l,k$ and so forth.

The quantity $\mathbb{E}[R]\mathbb{E}[X]$ must not obviously depend on the choice of the different reference state, and this is why it cancels out while taking the ratio. In addition, we want to stress that in (5.23) everything we need is the $\pi$’s,


obtained from the embedded Markov Chain transition matrix, and the average duration and reward. It follows that, given all this information, conceptually $\mathbb{E}[R]\mathbb{E}[X]$ can be computed easily unless some technical difficulties.

We now discuss the last case, where we consider two generic rewards $R^{(1)}_{ij}$ $R^{(2)}_{ij}$. Being the second different from time, the first metric will not be "per unit time" any more:

$$
\lim_{t\to\infty}\frac{R^{(1)}_{ij}(t)}{R^{(2)}_{ij}(t)}=\frac{\sum_{i}p_{i}R^{(1)}_{i}}{\sum_{i}p_{i}R^{(2)}_{i}}=\frac{\sum_{i}p_{i}\sum_{k}P_{ik}R^{(1)}_{ik}}{\sum_{i}p_{i}\sum_{k}P_{ik}R^{(2)}_{ik}}
$$

Some examples for the choice of rewards and their meaning are the following:

- successes and time $\to$ throughput
- energy cost and successes $\to$ energy efficiency
- successes and transmissions $\to$ average success rate

This is indeed a very powerful framework: if we can assume some Markov structure for transitions in our network, and in addition define some metrics whose we only need to compute the average, we are able to characterize the long run behavior of our system. This is essentially the ratio that gives us, for large times, what is the average reward of some metric per unit of some other metric. It be done quite easily once we have found the distribution of $\pi$’s and some linear combinations for the metrics for all transitions.

> [!Example] Exercise 5.8.1 - Mean and Variance from a Renewal Function
> **Problem:** Suppose that a renewal function has the form $M(t)=t+[1-\exp(-\alpha t)]$. Determine the mean and the variance of the interoccurrence distribution.
>
> **Approach:** Use the Elementary Renewal Theorem for $\mu$ and the second-order asymptotic expression for $M(t)-t/\mu$ to recover $\sigma^2$.
>
> **Solution:** The complete solution is transcribed below.
>
> **Takeaway:** The first-order growth of $M(t)$ gives the mean interrenewal time; the constant correction gives the variance.

[CMS:2018:1000] (Chapter 5.8.1 (Chap VII- Prob. 4.1)) Suppose that a renewal function has the form $M(t)=t+[1-exp(-\alpha t)]$. Determine the mean and the variance of the interoccurrence distribution.

Solution. From the Elementary Renewal theorem we know that:

$$
\lim_{t\to\infty}\frac{M(t)}{t}=\frac{1}{\mu}=\lim_{t\to\infty}\frac{t+1-e^{-\alpha t}}{t}=1\quad\implies\mu=1
$$

In addition we know that:

$$
\lim_{t\to\infty}\left(M(t)-\frac{t}{\mu}\right)=\frac{\sigma^{2}-\mu^{2}}{2\mu^{2}}=\lim_{t\to\infty}(1-e^{-\alpha t})
$$

where we replaced $\mu=1$. This leads us to:

$$
\frac{\sigma^{2}-\mu^{2}}{2\mu^{2}}=1\quad\implies\frac{\sigma^{2}-1}{2}=1\quad\implies\sigma^{2}=3
$$



> [!Example] Exercise 5.8.2 - Sojourns and Long-Run Fraction in State 1
> **Problem:** A Markov chain has the transition probability matrix shown below. Determine the mean duration of a typical sojourn in state 0 and, using renewal theory, determine the long-run fraction of time that the process is in state 1.
>
> **Approach:** Use geometric sojourn times and treat visits to state 1 as renewal instants.
>
> **Solution:** The complete worked solution is transcribed below.
>
> **Takeaway:** A Markov chain can be analyzed as a renewal process by choosing a regenerative state.

A Markov chain  $X_0, X_1, X_2 \ldots$  has the transition probability matrix:

$$
\mathbf {P} = \begin{array}{c c c c} & 0 & 1 & 2 \\ 0 & \left[ \begin{array}{c c c} 0.3 & 0.7 & 0 \\ 0.6 & 0 & 0.4 \\ 0 & 0.5 & 0.5 \end{array} \right] \end{array}
$$

A sojourn in a state is an uninterrupted sequence of consecutive visits to that state. Hence it begins when we come to a state and finish once we leave it.

1. Determine the mean duration of a typical sojourn in state 0
2. Using renewal theory, determine the long run fraction of time that the process is in state 1.
![[Stochastic_Processes_2020_p216_img78.jpeg]]
*Figure 5.20 - Transition diagram for problem 5.8.2.*

Solution. 1) It can be easily computed once we remember that, for a Markov chain, the mean duration of the stay in a state is a geometric random variable, whose parameter is the probability of leaving the state, namely 0.7. Its inverse will correspond to the average of the distribution, and so the mean duration is:

$$
\mathbb {E} [ \text {s t a y i n 0} ] = \frac {1}{0 . 7} = \frac {1 0}{7} \simeq 1. 4 2
$$

Similarly we can compute the expected stay in state 2:

$$
\mathbb {E} [ \text {s t a y i n 2} ] = \frac {1}{0 . 5} = 2
$$

and the expected stay in state 1.

$$
\mathbb {E} [ \text {s t a y i n 1} ] = 1
$$

The latter is indeed 1, because once we are in this state, with probability 1 we know that we will go out next time step.

2) Note that every time we visit state 1 is a renewal instant. Any time we land into it we will move exactly after 1 time unit to either 0 or 2 state. We will stay there some time, according to a geometric distribution, before a new renewal instant when going back to 1.

This should remind us of the Alternating renewal processes: we may define
![[Stochastic_Processes_2020_p217_img79.jpeg]]
*Figure 5.21 - For this particular exercise (5.8.2), we have that 1 is a regenerative state. Using renewal formalism, it is an alternating renewal process, and so we can refer to the duration of our stay in 1, as  $Y_{i}$ .*

state 1 by  $Y$ , where our stay will deterministically last exactly 1 time-step before leaving for some other state. We can therefore compute the expectation values for both the  $Y$ 's and the  $X$ 's, the latter being the average duration of a cycle, namely how much time is needed in order to come back to 1. Starting from state 1, after one time unit, we may leave with different probability either to state 0 or state 2, and spend there some time before returning to 1 and so starting a new cycle.

$$
\mathbb {E} [ Y ] = 1
\mathbb{E}[\text{return time to 1}] = \mathbb{E}[X] = 1 + P_{10}\cdot \mathbb{E}[\text{stay in 0}] + P_{12}\cdot \mathbb{E}[\text{stay in 2}] = 1 + 0.6\cdot \frac{10}{7} +0.4\cdot 2 = \frac{93}{35}
$$

We can finally compute the probability for the chain being in state 1:

$$
\pi_ {1} = P [ \text {chain is in state 1} ] = \frac {1}{93 / 35} = \frac {35}{93}
$$

Note that for this specific case, where the chain spends exactly one time unit in state 1,  $\mathbb{E}[X]$  is the average return time and  $\pi_1$  is the inverse of the average recurrence time. We could have also gone through this problem also by solving the system of stationary equations  $\vec{\pi} = \vec{\pi} \cdot P$ , finally obtaining the same result for  $\pi$ .


> [!Example] Exercise 5.8.3 - Asymptotic Renewal Count for a Triangular Lifetime
> **Problem:** Consider the triangular lifetime density $f(x)=2x$ for $0<x<1$. Determine an asymptotic expression for the expected number of renewals up to time $t$.
>
> **Approach:** Compute $\mu$ and $\sigma^2$, then use the asymptotic expansion of $M(t)$.
>
> **Solution:** The complete worked solution is transcribed below.
>
> **Takeaway:** The asymptotic renewal function depends on both the mean and the variance of the lifetime distribution.

Consider the triangular lifetime density  $f(x) = 2x$  for  $0 < x < 1$ . Determine an asymptotic expression for the expected number of renewals up to time  $t$ . Hint. Use the equation:

$$
\lim _ {t \to \infty} \left[ M (t) - \frac {t}{\mu} \right] = \frac {\sigma^ {2} - \mu^ {2}}{2 \mu^ {2}}
$$

Solution. We obviously have that:

$$
M (t) \simeq \frac {t}{\mu} + \frac {\sigma^ {2} - \mu^ {2}}{2 \mu^ {2}}
$$

where we need to compute  $\mu, \sigma$ .
![[Stochastic_Processes_2020_p218_img80.jpeg]]
*Figure 5.22 - $\mathrm{pdf(x)}$  for the triangular lifetime density  $f(x) = 2x$  for both problems (5.8.3) and (5.8.4) in the interval  $0 < x < 1$ .*

$$
\mathbb {E} [ X ] = \mu = \int_ {0} ^ {1} x f (x) d x = \int_ {0} ^ {1} 2 x ^ {2} d x = \frac {2}{3}
\mathbb {E} [ X ^ {2} ] = \mu^ {2} + \sigma^ {2} = \int_ {0} ^ {1} x ^ {2} f (x) d x = \int_ {0} ^ {1} 2 x ^ {3} d x = \frac {1}{2}
\sigma^ {2} = \mathbb {E} [ X ^ {2} ] - \mu^ {2} = \frac {1}{2} - \frac {4}{9} = \frac {1}{18}
\frac {\sigma^ {2} - \mu^ {2}}{2 \mu^ {2}} = \frac {1 / 18 - 4 / 9}{2 \cdot 4 / 9} = - \frac {7}{16}
$$

Finally we can write:

$$
M (t) \simeq \frac {t}{\mu} + \frac {\sigma^ {2} - \mu^ {2}}{2 \mu^ {2}} = \frac {3}{2} t - \frac {7}{16}
$$

**Exercise 5.8.4 (Chap VII- Ex. 4.2):**

> [!Example] Exercise 5.8.4 - Excess Life for a Triangular Lifetime
> **Problem:** Consider the triangular lifetime density $f(x)=2x$ for $0<x<1$. Determine an asymptotic expression for the probability distribution of excess life, then determine the limiting mean excess life and compare it with the general result.
>
> **Approach:** Apply the limiting excess-life distribution and integrate the tail probability to obtain the mean.
>
> **Solution:** The complete worked solution is transcribed below.
>
> **Takeaway:** The limiting excess-life mean agrees with $\mathbb{E}[X^2]/(2\mathbb{E}[X])$.

Consider the triangular lifetime density  $f(x) = 2x$  for  $0 < x < 1$ . Determine an asymptotic expression for the probability distribution of excess life. Using this distribution, determine the limiting mean excess life and compare with the general result following equation:

$$
\lim  _ {t \rightarrow \infty} P [ \gamma_ {t} \leqslant x ] = \frac {1}{\mu} \int_ {0} ^ {x} [ 1 - F (y) ] d y \tag {5.25}
$$

**Solution.** With respect to the density distribution  $f(x) = 2x$ , its corresponding distribution is  $F(X) = X^2$  in (0,1). We can compute either (5.25) or its complementary:

$$
\lim _ {t \to \infty} P [ \gamma_ {t} > x ] = \frac {1}{\mu} \int_ {x} ^ {\infty} (1 - F (y)) d y
$$

that we have already studied previously. Replacing  $F(y)$  with its value and considering the interval where the integrand is non zero:

$$
\frac {1}{\mu} \int_ {x} ^ {1} (1 - y ^ {2}) d y = \frac {1}{\mu} \left[ \frac {2}{3} - x + \frac {x ^ {3}}{3} \right] = \frac {3}{2} \left[ \frac {2}{3} - x + \frac {x ^ {3}}{3} \right] = 1 - \frac {3}{2} x + \frac {x ^ {3}}{2} = \lim _ {t \to \infty} P [ \gamma_ {t} \geqslant x ]
$$


$\mu$ was the one from the previous exercise. The expectation value, in the limit, will be the integral:

$$
\mathbb{E}[\gamma_{t}]=\int_{0}^{\infty}P[\gamma_{t}>x]dx=\int_{0}^{1}\left(1-\frac{3}{2}x+\frac{x^{3}}{2}\right)dx=1-\frac{3}{4}+\frac{1}{8}=\frac{3}{8}
$$

where this is the asymptotic expected value for the excess life for this problem. We have seen previously (see eq. 5.15 at page 198) that we can compute $\mathbb{E}[\gamma_{t}]$ by using $\sigma$ and $\mu$. Therefore:

$$
\frac{\sigma^{2}+\mu^{2}}{2\mu}=\frac{1/18+4/9}{2\cdot 2/3}=\frac{1/2}{4/3}=\frac{3}{8}
$$

that is the same result we obtained before, thus concluding this problem.


> [!Example] Exercise 5.8.5 - Excess Life for Uniform Lifetimes
> **Problem:** What is the limiting distribution of excess life when renewal lifetimes have the uniform density $f(x)=1$, for $0<x<1$?
>
> **Approach:** Substitute $F(x)=x$ and $\mu=1/2$ in the limiting excess-life formula.
>
> **Solution:** The complete worked solution is transcribed below.
>
> **Takeaway:** Even uniform lifetimes produce a non-uniform limiting excess-life distribution because of length bias.

What is the limiting distribution of excess life when renewal lifetimes have the uniform density $f(x)=1$, for $0<x<1$?

Solution. Being $f(x)=1$ uniform in $(0,1)$, we easily know that $\mu=1/2$ and $F(X)=X$. Its limiting distribution follows the general result written in the previous exercise (5.25):

$$
\lim_{t\to\infty}P[\gamma_{t}>z]=\frac{1}{\mu}\int_{z}^{\infty}(1-F(x))dx=\frac{1}{\mu}\int_{z}^{1}(1-x)dx=\int_{z}^{1}2(1-x)dx=(1-z)^{2}\quad z\in(0,1)
$$

where we replaced $\mu$ with its value $1/2$. The complementary to $1$ probability will consequently be:

$$
\lim_{t\to\infty}P[\gamma_{t}\leqslant z]=1-(1-z)^{2}\quad z\in(0,1)
$$


> [!Example] Exercise 5.8.6 - Loss System with Poisson Arrivals
> **Problem:** Jobs arrive according to a Poisson process of rate $\lambda$. The server accepts an arriving customer only if idle; otherwise the customer is lost. Service times are independent with mean $\mu$. Find the long-run idle fraction and the long-run fraction of lost customers.
>
> **Approach:** Model IDLE and BUSY periods as an alternating renewal process, then use PASTA for the loss probability.
>
> **Solution:** The complete worked solution is transcribed below.
>
> **Takeaway:** Renewal cycles give time averages, while Poisson arrivals see those same time averages.

Jobs arrive at a certain service system according to a Poisson process of rate $\lambda$. The server will accept an arriving customer only if it is idle at time of arrival. Potential customers arriving when the system is busy are lost. Suppose that the service times are independent random variables with mean service time $\mu$.

- Show that the long run fraction of time that the server is idle is $1/(1+\lambda\mu)$.
- What is the long run fraction of potential customers that are lost?

Solution. Let us suppose that we start when the system is empty (IDLE) and we wait for the first arrival. After an average time $1/\lambda$ an user will arrive according to an exponential distribution, and will set the system state in BUSY
![[Stochastic_Processes_2020_p220_img81.jpeg]]
*Figure 5.23 - Graphical description of exercise (5.8.6). We start with our system in IDLE state and, after a period whose average value is  $1 / \lambda$ , an user arrives and will be served in a period of time whose average is  $\mu$ , in which the system will be BUSY. Clearly the sum IDLE+BUSY is a renewal interval.*

for an average time period of  $\mu$ . Once the system is emptied again, it will wait for an other customer to arrive and repeat this process. Note that the distribution of arrivals is memoryless, and therefore independent of the time when the system empties. This is indeed an Alternating renewal process.

We recall, from the theory, that the probability for the system to be  $IDLE$  is the ratio between the expected time duration for  $BUSY$  time, and for a single cycle:

$$
P [ \mathrm {s e r v e r I D L E} ] = \frac {\mathbb {E} [ I D L E ]}{\mathbb {E} [ I D L E + B U S Y ]} = \frac {1 / \lambda}{1 / \lambda + \mu} = \frac {1}{1 + \lambda \mu}
$$

We can now find the fraction of potential customers that are lost in two different ways. Let us consider the renewal process we are dealing with, and define two different rewards: the first one is the number of users that have been accepted, that for each cycle is obviously one. So the its expected number is deterministically known:

$$
\mathbb {E} [ \text {a c c e p t e d u s e r s i n a r e n e w a l c y c l e} ] = 1
$$

Conversely, the number of arriving users in a cycle is the average time duration of the cycle times the arrival rate:

$$
\mathbb {E} [ \text {a r r i v i n g u s e r s i n a r e n e w a l c y c l e} ] = (1 / \lambda + \mu) \lambda = 1 + \lambda \mu
$$

Among this number of users, we know that only one will be accepted, while the remaining ones will not. Therefore, the probability:

$$
\begin{array}{l} P [ \text {u s e r i s r e j e c t e d} ] = \frac {\mathbb {E} [ \text {r e j e c t e d u s e r s} ]}{\mathbb {E} [ \text {a r r i v i n g u s e r s} ]} = \\ = \frac {\mathbb {E} [ \text {a r r i v i n g u s e r s} ] - \mathbb {E} [ \text {a c c e p t e d u s e r s} ]}{\mathbb {E} [ \text {a r r i v i n g u s e r s} ]} = \frac {\lambda \mu}{1 + \lambda \mu} \\ \end{array}
$$

The second way to obtain the same result is the following one.

Instead of computing  $P[\text{server IDLE}]$ , we could have looked for the  $P[\text{server BUSY}]$  that is its complementary to 1. In addition, the probability for a user to be rejected is the same one as the probability for an arriving user to find the system BUSY. Recall now that Poisson Arrivals See Time Averages, and so the probability seen by an arriving user is the probability  $P[\text{server BUSY}]$ . And


so:

$$
P[\text{server BUSY}]=1-P[\text{server IDLE}]=\frac{\lambda\mu}{1+\lambda\mu}
$$

This result could be obtained also using renewal theory: we should have defined the rewards in a renewal cycle we introduced above, and finally compute the ratio. Alternatively, we could have found what is the probability for an arriving user to find the system BUSY, that would be statistically equivalent for him to be rejected.


> [!Example] Exercise 5.8.7 - Two-Component Parallel System
> **Problem:** A system has two independent components, each alternating between OFF and OPERATING with exponential repair and failure rates. Determine the long-run inoperational fraction, the mean failed-state duration, the mean cycle duration, and the mean operating duration between failures.
>
> **Approach:** Use alternating renewal processes for each component and for the whole system, then exploit independence and exponential minima.
>
> **Solution:** The complete worked solution is transcribed below.
>
> **Takeaway:** System-level reliability can often be reduced to renewal-cycle averages.

A certain type component has two states:

$$
0=\text{OFF}\qquad 1=\text{OPERATING}
$$

In state 0, the process remains there a random length of time, which is exponentially distributed with parameter $\alpha$, and then moves to state 1. The time in state 1 is exponentially distributed with parameter $\beta$, after which the process returns to state 0.

The system has two of these components, A and B with distinct parameters, as shown in the table (LABEL:eq:system) below.

In order for the system to operate, at least one of the components A and B must be operating (a parallel system). Assume that the component stochastic processes are independent one of another.

1. In the long run, what fraction of time is the system inoperational (not operating)?
2. Once the system enters the failed state, what is the mean duration there prior to returning to operation?
3. Define a cycle as the time between the instant that the system first enters the failed state and the next such instant. Using renewal theory, find the mean duration of a cycle.
4. What is the mean system operating duration between successive system failures?

|  Component | Operating Failure Rate | Repair Rate  |
| --- | --- | --- |
|  A | $\beta_{A}$ | $\alpha_{A}$  |
|  B | $\beta_{B}$ | $\alpha_{B}$  |
*Table 5.1 -  Table depicting all parameters for both components A and B in exercise (5.8.7).*

Solution. 1) We should note that for a single component there are many intervals statistically equal one to another. These are indeed Renewal intervals,
![[Stochastic_Processes_2020_p222_img82.jpeg]]
*Figure 5.24 - A possible evolution in time for a single component of the process, that may be working or not for different time intervals exponentially distributed whose averages are respectively  $1 / \alpha$  and  $1 / \beta$ . Note as every time we return to state 0 it is a Renewal instant.*

where the Renewal instants are the ones where we land in state 0. More specifically we can identify an Alternating renewal process, whose state are  $ON$  or  $OFF$ . The probability that a single component is operating will consequently be:

$$
P [ \text {c o m p o n e n t} i \text {w o r k i n g} ] = \frac {1 / \beta_ {i}}{1 / \alpha_ {i} + 1 / \beta_ {i}} = \frac {\alpha_ {i}}{\alpha_ {i} + \beta_ {i}} \tag {5.26}
$$

Recall now that the system has two components, whose  $\alpha_{i}$  and  $\beta_{i}$  are different, and independent of each other. Clearly, the two probabilities for a component to be down are the complementary to 1 of (5.26):

$$
P [ A d o w n ] = \frac {\beta_ {A}}{\alpha_ {A} + \beta_ {A}} \qquad P [ B d o w n ] = \frac {\beta_ {B}}{\alpha_ {B} + \beta_ {B}}
$$

We have just stated that the two processes are independent, and so the joint probability for both of them of being down is their product:

$$
P [ A d o w n, B d o w n ] = P [ A d o w n ] \cdot P [ B d o w n ] = \left(\frac {\beta_ {A}}{\alpha_ {A} + \beta_ {A}}\right) \left(\frac {\beta_ {B}}{\alpha_ {B} + \beta_ {B}}\right)
$$
![[Stochastic_Processes_2020_p222_img83.jpeg]]
*Figure 5.25 - Diagram for point 2 of ex. 5.8.7. We start when both components are OFF, and we wait until either of the two independent exponential processes with rate  $\alpha_{A}$  and  $\alpha_{B}$  occurs, in order for the system to be recovered. We denote with  $T_{A}$  and  $T_{B}$  the times for respectively component  $A$  and  $B$  to recover.*

2) It is requested to compute the probability, once both  $A$  and  $B$  are down, for the system to recover. We know that this happens when one of the components recovers, which eventually occurs according to an exponential with rate  $\alpha_{A}$  or  $\alpha_{B}$ . We denote by  $T_{A}$  and  $T_{B}$  the times when recover happens for the two components, and so the time for which the system will be down:

$$
\text {t i m e s y s t e m i s d o w n} = \min  \left(T _ {A}, T _ {B}\right)
$$

We need now to find the statistics of this minimum. See that when the minimum


of two values is bigger of a certain number, it implies that both of them will be bigger than the same number:

$$
P[min(T_{A},T_{B})>a]=P[T_{A}>a\ ,\ T_{B}>a]=P[T_{A}>a]\cdot P[T_{B}>a]=\
$$

Where we used the fact that the single statistics of $T_{A}$ and $T_{B}$ are independent of each other. We indeed know them, as they are exponentially distributed. And so we can write:

$$
=P[T_{A}>a]\cdot P[T_{B}>a]=e^{-\alpha_{A}a}\cdot e^{-\alpha_{B}a}=e^{-(\alpha_{A}+\alpha_{B})a}
$$

Note as the probability for the minimum being bigger than $a$ is itself an exponential random variable, whose rate is the sum of the two different parameters $(\alpha_{A}+\alpha_{B})$. This is obviously valid only for exponential random variables, or for combined random processes, but does not apply for more general cases. The average time the system will remain down is therefore the inverse of the rate just found, and so:

$$
\mathbb{E}[\text{Sojourn System down}]=\frac{1}{\alpha_{A}+\alpha_{B}}
$$
![[Stochastic_Processes_2020_p223_img84.jpeg]]
*Figure 5.26 -  Diagram for point 3 of ex. 5.8.7. We start in state $(0,0)$, and so where both components are down. Successively it will be alternatively in states $(0,1),(1,0),(1,1)$ where the system will be working, until both goes down again and we fall back into $(0,0)$ state. This is indeed a Renewal instant. We can define an alternating renewal process out of this, where our $Y$ will be the period while the system is not working.*

3) We should notice as every time we enter state $(0,0)$, the future evolution starting from this point will be statistically indistinguishable: since both components are down, the system will not work. Note as the repair time is exponential in both cases and therefore memoryless. It is indeed a renewal instant included in an alternating renewal process.
The probability that the system is down is the ratio between the two intervals $\mathbb{E}[\text{system down}]$ and $\mathbb{E}[\text{cycle}]$. We know both the the expected value for the duration of time interval while the system is down and the ratio value, computed in the previous points of the exercise.
So we can invert the formula, thus obtaining:

$$
\mathbb{E}[\text{cycle}]=\frac{\mathbb{E}[\text{system down}]}{P[\text{system down}]}=\frac{1/(\alpha_{A}+\alpha_{B})}{\left(\frac{\beta_{A}}{\alpha_{A}+\beta_{A}}\right)\left(\frac{\beta_{B}}{\alpha_{B}+\beta_{B}}\right)}
$$

4) We are requested to find the expected time duration of the interval that is complementary to the duration of a cycle, and so the second interval denoted


as  $(0,1),(1,0),(1,1)$  in image (5.26). As we can clearly see graphically:

$$
\mathbb{E}[\mathrm{cycle}] = \mathbb{E}[\mathrm{system~down}] + \mathbb{E}[\mathrm{system~working}]
$$

Where we can compute it by using the results obtained previously, therefore:

$$
\mathbb{E}[\mathrm{system~working}] = \mathbb{E}[\mathrm{cycle}] - \mathbb{E}[\mathrm{system~down}] = \left(\frac{1}{\alpha_A + \alpha_B}\right)\left(\frac{(\alpha_A + \beta_A)(\alpha_B + \beta_B)}{\beta_A\beta_B} -1\right)
$$

Note that if we wanted to compute directly  $\mathbb{E}[\mathrm{system~working}]$  we could have done it, in principle. But we also would have to take into account that the number of trajectories leading us to a failure of the system, namely  $(0,0)$ , is infinite.

In order to obtain its average duration, we would need first to count all possible combinations and therefore their probability making the calculations very risky and tedious. Whereas Renewal theory comes in our help, giving us a shortcut to compute the average stay in a single state. Once we have the average stay in a single state, in this case  $(0,0)$ , we can model our problem as an alternating process and leading us to simple formula that can be easily inverted.


> [!Example] Exercise 5.8.8 - Two Bulbs and Half-Lit Office
> **Problem:** A ceiling fixture has two light bulbs. When one fails, replacement is delayed until the second fails, then both are replaced. Determine the long-run fraction of time the office is half lit for exponential lifetimes and for uniform $(0,1)$ lifetimes.
>
> **Approach:** Treat each replacement-to-replacement interval as a renewal cycle, compute the expected time with exactly one working bulb, and divide by the expected cycle length.
>
> **Solution:** The complete worked solution is transcribed below.
>
> **Takeaway:** Memorylessness changes the fraction of half-lit time; for non-exponential lifetimes the order statistics of lifetimes determine the cycle fractions.

A lazy professor has a ceiling fixture in his office that contains two light bulbs. To replace a bulb, the professor must fetch a ladder, and being lazy, when a single bulb fails, he waits until the second bulb fails before replacing them both. Assume that the length of life of the bulbs are independent random variables.

- If the lifetimes of the bulbs are exponentially distributed, with the same parameter, what fraction of time, in the long run, is our professor's office half lit (only one bulb is working)?
- What fraction of time, in the long run, is our professor's office half lit if the bulbs that he buys have the same uniform  $(0,1)$  lifetime distribution?
![[Stochastic_Processes_2020_p224_img85.jpeg]]
*Figure 5.27 - Representation for point 1 of ex. 5.8.8. We start our problem when both bulbs are working, and after the second one breaks, we assume that the replacement is instantaneous and it is a renewal instant. Under these assumptions, it is a Alternating renewal process.*

Solution. 1) Obviously, as depicted in figure (5.27), it is an Alternating renewal process between the states where both bulbs are working (2) and only one is working (1). This is indeed true only in the case where the replacement


is instantaneous, otherwise we would have taken into account also the time needed in order to replace the bulb, and so defining a new state.

The probability for the office to be half lit is therefore the probability of being in state 1, using the renewal theory. We assumed, for this point, that each lifetime  $X_{i}$  is exponentially distributed with parameter  $\beta$ . So, the time when one of them breaks is an exponential random variable itself, whose rate of failure is the rate of failure of two single bulbs  $(2 \cdot 1\beta)$ . This means the average of this time is half of the time for one of them to break. Once the first one is burnt, the time elapsed for the second one to break in turn is an exponential random variable with parameter  $1 / \beta$ . Recall that the exponential distribution is memoryless, and therefore the second remaining light bulb has a whole lifetime  $1 / \beta$  ahead, being it as if new. The probability we are looking for is:

$$
P [ \mathrm {h a l f} \mathrm {l i t} ] = \frac {1 / \beta}{2 / \beta + 1 / \beta} = \frac {2}{3}
$$

Note that the last result is valid only when the distribution is memoryless, but more in general we have a situation as depicted in figure (5.28)
![[Stochastic_Processes_2020_p225_img86.jpeg]]
*Figure 5.28 - More general case for ex. 5.8.8. Cycle is still the same, but distributions for the time intervals intervals may change.*

In order to find the statistics of the moment where the first bulb breaks, we do consider a certain time value  $a$  and find the probability for  $\min(X_1, X_2)$  to be greater than it. Note as it is equivalent to state that both of them must be greater than  $a$ , and so if we assume that lifetimes are independent one another, and in a later passage that they are identically distributed:

$$
P [ \min (X _ {1}, X _ {2}) > a ] = P [ X _ {1} > a, X _ {2} > a ] = P [ X _ {1} > a ] \cdot P [ X _ {2} > a ] = (P [ X > a ]) ^ {2} = (1 - F (a)) ^ {2}
$$

Conversely, when we want to find the statistics of the maximum between  $MAX(X_1, X_2)$  we can set it to be smaller than  $a$ . And so, using in addition the fact that lifetimes are identically distributed, and so their distribution is the same one:

$$
P [ M A X (X _ {1}, X _ {2}) \leqslant a ] = P [ X _ {1} \leqslant a, X _ {2} \leqslant a ] = P [ X _ {1} \leqslant a ] \cdot P [ X _ {2} \leqslant a ] = (P [ X \leqslant a ]) ^ {2} = (F (a)) ^ {2}
$$

We now compute their expectation values:

$$
\mathbb {E} [ \min ] = \int_ {0} ^ {\infty} P [ \min > a ] d a = \int_ {0} ^ {\infty} (1 - F (a)) ^ {2} d a
\mathbb{E}[MAX]=\int_{0}^{\infty}P[MAX>a]da=\int_{0}^{\infty}(1-F(a)^{2})da
$$

This result is valid for any distribution $F(a)$, as long as they are independent one another.
If $X\sim exp(\beta)$, then its distribution is $F(a)=1-e^{-\beta a}$, hence the expectation values:

$$
\mathbb{E}[min]=\int_{0}^{\infty}e^{-2\beta a}da=\frac{1}{2\beta}
\mathbb{E}[MAX]=\int_{0}^{\infty}(2e^{-\beta a}-e^{-2\beta a})da=\frac{3}{2\beta}
$$

2) In the case where this distribution is $X\sim U[0,1]$, then $F(a)=a,\;a\in(0,1)$. Expectation values are then:

$$
\mathbb{E}[min]=\int_{0}^{1}(1-a)^{2}da=\frac{1}{3}
\mathbb{E}[MAX]=\int_{0}^{1}(1-a^{2})da=\frac{2}{3}
$$

And so the probability for the office to be half lit, in the long run:

$$
P[\text{half lit}]=1-\frac{\mathbb{E}[min]}{\mathbb{E}[MAX]}=\frac{1}{2}
$$

that is less than what we obtained in the exponential lifetime case.

---

## Summary Table

| Concept | Definition / Formula | Conditions / Notes |
|---|---|---|
| **Renewal process** | $N(t)=\max(n:W_n\leq t)$ with $W_n=X_1+\cdots+X_n$ | Interoccurrence times $X_i$ are positive, finite, i.i.d. |
| **Renewal function** | $M(t)=\mathbb{E}[N(t)]=\sum_{k=1}^{\infty}F_k(t)$ | $F_k$ is the $k$-fold convolution distribution of the interarrival law |
| **Tail relation** | $N(t)\geq k \Longleftrightarrow W_k\leq t$ | Links the counting process and arrival epochs |
| **Excess life** | $\gamma_t=W_{N(t)+1}-t$ | Residual waiting time until the next renewal |
| **Current life / age** | $\delta_t=t-W_{N(t)}$ | Time elapsed since the last renewal |
| **Total life** | $\beta_t=\gamma_t+\delta_t$ | Length of the renewal interval containing $t$ |
| **Poisson renewal process** | $F(x)=1-e^{-\lambda x}$, $M(t)=\lambda t$ | Memorylessness makes excess life exponential |
| **Sampling paradox** | Random-time sampling favors longer intervals | Explains why $\mathbb{E}[\beta_t]$ can exceed $\mathbb{E}[X]$ |
| **Almost-sure renewal rate** | $N(t)/t\to 1/\mu$ | With probability 1, where $\mu=\mathbb{E}[X]$ |
| **Elementary Renewal Theorem** | $M(t)/t\to 1/\mu$ | Regular limit for the expectation |
| **Basic Renewal Theorem** | $M(t+h)-M(t)\to h/\mu$ | Non-arithmetic $F$; arithmetic case requires $h$ multiple of the span |
| **Limiting excess-life distribution** | $\lim_{t\to\infty}P[\gamma_t\leq x]=\mu^{-1}\int_0^x[1-F(y)]dy$ | Continuous lifetimes with finite mean |
| **Mean limiting excess life** | $\mathbb{E}[\gamma_t]\to \mathbb{E}[X^2]/(2\mathbb{E}[X])$ | Shows length-bias in the interval containing a random time |
| **Delayed renewal process** | $X_1\sim G$, while $X_2,X_3,\ldots\sim F$ i.i.d. | Long-run rate still depends on $\mu=\mathbb{E}[X_2]$ |
| **Stationary renewal process** | $G(x)=\mu^{-1}\int_0^x[1-F(y)]dy$ | Makes the long-run residual-life law hold for all $t$ |
| **Alternating renewal process** | $\lim_{t\to\infty}p(t)=\mathbb{E}[Y]/\mathbb{E}[X]$ | Fraction of time in the labeled part of each renewal cycle |
| **Renewal reward process** | $R(t)=\sum_{n=1}^{N(t)}R_n$ | Long-run reward rate is $\mathbb{E}[R]/\mathbb{E}[X]$ |
| **Reward ratio** | $R_1(t)/R_2(t)\to \mathbb{E}[R_1]/\mathbb{E}[R_2]$ | Useful for energy per packet, throughput, success rate |
| **Regenerative process** | Process probabilistically restarts at regeneration times | Regeneration instants form an embedded renewal process |
| **Semi-Markov process** | Next state follows $P_{ij}$; transition duration has law $F_{ij}$ | Generalizes Markov chains by randomizing transition times |
| **Embedded Markov chain** | Sequence of visited states ignoring transition times | Its stationary distribution $\pi_i$ helps compute semi-Markov limits |
| **Semi-Markov long-run probability** | $P_j=\dfrac{\pi_j\mu_j}{\sum_i\pi_i\mu_i}$ | State probability is proportional to visit frequency times mean sojourn time |
