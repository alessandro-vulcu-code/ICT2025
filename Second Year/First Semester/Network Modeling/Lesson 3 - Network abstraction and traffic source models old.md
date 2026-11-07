# Lesson 3 — Network abstraction and traffic source models

## How to build a network model

A network model keeps the features needed to predict a chosen performance metric. It supports
dimensioning, evaluation and resource allocation; its predictions depend on the details retained.

The main components of a communication system are:

1. **Data source:** generates traffic; a source model describes its rate and time pattern.
2. **Admission control (CAC):** accepts a new flow only if its requirements can be supported
   alongside existing flows.
3. **Resource manager:** decides how much capacity to allocate to admitted flows.
4. **Scheduler:** decides when each flow uses the allocated resources.
5. **Switching elements:** forward packets; buffers hold packets waiting for service and can
   introduce delay or loss.
6. **End user:** perceives a *quality of experience* (QoE), which depends on the application.

### Network abstraction

Describe a network through four elements:

- **Users/customers** $s\in\mathcal S$: entities that request service, such as data sources or
  destinations. Their objective and QoE depend on the application.
- **Resources** $k\in\mathcal K$: finite capacities shared among users. Let $c_k$ denote the
  available amount of resource $k$, and $d_s(k)$ the amount requested by user $s$.
- **Resource manager:** assigns $r_s(k)$ units of resource $k$ to user $s$. The allocation
  vector is $\mathbf r_s=(r_s(k))_{k\in\mathcal K}$.
- **Utility metrics:** quantify how well allocations meet user or system objectives.

**Example — classroom Wi-Fi.** Downloaders want short file transfer times; video watchers
want smooth playback. Both share Wi-Fi capacity and the access point's Internet connection.
For a user whose traffic traverses both links, achievable throughput is bounded by the
**bottleneck**:

$$
x_s\leq\min\{r_s(\mathrm{WiFi}),r_s(\mathrm{Internet})\}.
$$

Allocating 10 Mb/s on Wi-Fi and 6 Mb/s on the Internet link therefore cannot provide more
than 6 Mb/s end to end. A watcher whose video reaches full quality at 2 Mb/s gains no
further quality from a higher rate.

### Resource allocation constraints

A resource manager normally respects:

$$
\sum_{s\in\mathcal S}r_s(k)\leq c_k\quad\forall k\in\mathcal K
\qquad\text{(feasibility)},
$$

$$
0\leq r_s(k)\leq d_s(k)\quad\forall s,k
\qquad\text{(least privilege)}.
$$

Feasibility limits *actual* allocations. Reservations can exceed capacity when demand is
uncertain, but simultaneous use still cannot exceed physical capacity.

**Example — overbooking.** Let $\hat d_s\in\{0,1\}$ indicate a reservation and
$d_s\in\{0,1\}$ actual attendance. Suppose
$\Pr(d_s=1\mid\hat d_s=1)=0.98$. With $C=300$ seats and exactly 300 reservations,
expected occupancy is $300(0.98)=294$ and expected utilization is $0.98$. Accepting more
reservations may improve utilization, at the cost of a nonzero probability of turning away
customers. For an unreserved customer, the notes also illustrate
$\Pr(d_s=1\mid\hat d_s=0)=0.001$; these probabilities are example assumptions.

**Equal sharing** assigns each of $D+W$ downloaders and watchers
$r_s(k)=c_k/(D+W)$. It is feasible, but can give a watcher more than requested while a
downloader needs more. With 15 downloaders, 5 watchers, 100 Mb/s of Wi-Fi and 20 Mb/s of
Internet capacity, each gets 5 Mb/s and 1 Mb/s respectively; Internet access is the
bottleneck.

### Utility functions and optimization

User utility $U_s(\mathbf r_s)$ measures the value of an allocation. Its shape reflects the
application: download utility may grow with throughput, while video utility may rise
sharply around a usable rate and saturate once full quality is reached. A cost can enter as
negative utility.

System utility $U_0(\mathbf r)$ can combine user utilities and resource costs. One possible
choice is $U_0=\sum_s w_sU_s(\mathbf r_s)$, with weights $w_s$ expressing system priorities.
Resource allocation then becomes:

$$
\max_{\mathbf r}\;U_0(\mathbf r)
\quad\text{subject to}\quad
\sum_s r_s(k)\leq c_k,\;
0\leq r_s(k)\leq d_s(k),\;
U_s(\mathbf r_s)\geq u_s^{\min}\ \text{when required}.
$$

Minimum utility constraints can make the problem infeasible when capacity is insufficient.

**Example — video calls.** Ten employees make about two calls per day, each lasting 30–90
minutes. The shared resource is Internet link capacity $C$ (consider $C=10$ Mb/s). Suppose
an active call needs 0.5 Mb/s for minimum usable quality and 1.5 Mb/s for full quality. A
simple user utility, with allocated rate $x$ in Mb/s, is

$$
U_s(x)=
\begin{cases}
0, & x<0.5,\\
x-0.5, & 0.5\leq x<1.5,\\
1, & x\geq1.5.
\end{cases}
$$

To size the link, a system metric can be the **blocking probability** $P_{\mathrm{block}}(C)$:
the probability that a new call cannot obtain its required rate. It generally decreases as
$C$ grows. Its value at 10 Mb/s requires a model of when calls start, how long they last,
and how they overlap; mean traffic alone is insufficient.

## Traffic source models

An average information flow helps with rough dimensioning and stability analysis. Delay,
peaks and buffer sizing also require the *temporal* traffic pattern. The needed abstraction
depends on the question:

- **Session level:** session start/end and average traffic (e.g., an HTTP session).
- **Activity level:** alternating active and idle periods and their durations.
- **Packet level:** packet arrival times and packet sizes within those periods.

### Point process and equivalent representations

> [!info] Definition — Point process
> A point process describes discrete events on a continuous axis, here the times at which
> traffic arrives. An event may represent a session start, an activity change or packet
> generation, according to the chosen abstraction.

Set $T_0=0$ and let $T_i$ be the time of arrival $i\geq1$. The inter-arrival times and
counting process are

$$
A_i=T_i-T_{i-1},\qquad
N(t)=\sum_{i\geq1}\mathbf 1_{\{T_i\leq t\}},\qquad
N(t_1,t_2)=N(t_2)-N(t_1).
$$

$N(t_1,t_2)$ counts arrivals in $(t_1,t_2]$. Arrival times $\{T_i\}$, intervals
$\{A_i\}$ and counts $N(t)$ are equivalent descriptions of the same point process.

### Batches, weights and offered traffic

A **marked point process** adds $B_i$, the number of information units (IUs) generated at
arrival $i$ (*batch size*). Marks may depend on arrival times. A **marked and weighted
point process** also assigns weight $W_{i,j}$ to IU $j$ of batch $i$:

$$
(\{T_i\},\{B_i\},\{W_{i,j}\}).
$$

For packets, $W_{i,j}$ can be packet length in bits; more generally it can represent energy
or processing work. The aggregate offered workload and average offered rate are

$$
S_g(t)=\sum_{i=1}^{N(t)}\sum_{j=1}^{B_i}W_{i,j},\qquad
\bar G(t)=\frac{S_g(t)}{t},
$$

$$
G(t_1,t_2)=\frac{S_g(t_2)-S_g(t_1)}{t_2-t_1}.
$$

If weights are bits, $G$ is a bit rate. For a source producing one $M$-byte message every
$T$ seconds, $A_i=T$, $B_i=1$ and $W_{i,1}=M$ bytes. If each message is split into $K$
equal packets, $B_i=K$ and each packet weighs $M/K$ bytes; the average offered bit rate
remains $8M/T$.

### Renewal processes

> [!info] Definition — Renewal process
> A point process is a renewal process when its inter-arrival times $A_i$ are positive,
> finite, independent and identically distributed (i.i.d.). At each arrival, the next
> inter-arrival time has the same distribution independently of earlier intervals.

If $A_i\sim\operatorname{Exp}(\lambda)$ i.i.d., the result is a **homogeneous Poisson
process** with constant rate $\lambda$. For disjoint intervals, arrival counts are independent;
for an interval of length $\Delta t$,
$N(t,t+\Delta t)\sim\operatorname{Poisson}(\lambda\Delta t)$.

- $A_i=5$ s for every $i$: periodic renewal process; not Poisson.
- If $A_{i+1}$ depends on $A_i$ (for example, equals $A_i$ with probability 0.1), the
  intervals are not independent; the process is not renewal.

### Renewal–reward process and theorem

Attach reward $R_i$ to renewal $i$ and define cumulative reward

$$
Y(t)=\sum_{i=1}^{N(t)}R_i.
$$

The pairs $(A_i,R_i)$ are i.i.d. across renewals; $A_i$ and $R_i$ *within a pair* may be
correlated. Rewards can represent batch size, workload or cost.

> [!info] Theorem — Long-run reward rate
> If $0<\mathbb E[A_i]<\infty$ and $\mathbb E[|R_i|]<\infty$, then
> $$
> \lim_{t\to\infty}\frac{Y(t)}{t}
> =\frac{\mathbb E[R_i]}{\mathbb E[A_i]}
> \quad\text{almost surely}.
> $$

For traffic, choose $R_i=\sum_{j=1}^{B_i}W_{i,j}$. Thus long-run offered rate is
$\mathbb E[R_i]/\mathbb E[A_i]$. Only when batch size and individual weights satisfy the
relevant independence assumptions can its numerator simplify to
$\mathbb E[B_i]\,\mathbb E[W_{i,j}]$.
