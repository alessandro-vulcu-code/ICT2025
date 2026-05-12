
---

## 1.1 Introduction

Modeling a natural phenomenon consists of associating its elements with *abstractions* in a *logical system*, so that we can deduce properties or predict behaviour. For instance, to compute the distance between two cities, we treat them as *geometric points* and apply spherical geometry to find the great-circle length connecting them.

A model is **deterministic** if it produces a single outcome from a given set of initial conditions. A **stochastic model**, by contrast, predicts a *set* of possible outcomes, each weighted by its *probability* — a measure of how plausible that outcome is.

There is no universally "best" model for a phenomenon. The choice depends on what is *useful* for the task at hand. A good model captures every aspect of the phenomenon relevant to the question being asked, while remaining tractable enough to allow calculations and predictions.

---

## 1.2 Stochastic Processes

A **stochastic process** is a family of random variables $\{X_t\}$, indexed by a parameter $t$ ranging over a set $T$. Intuitively, it is a "stochastic function": each time the experiment is run, the mapping $t \mapsto X(t)$ produces a different graph.

**The index set $T$** can be:
- **Discrete**: e.g. $T = \mathbb{N}$, where $X(n)$ is the outcome of the $n$-th dice toss.
- **Continuous**: e.g. $T = [0, \infty)$, where $X(t)$ is the temperature at time $t$ at a weather station.

$T$ need not represent time; it can be a spatial index. For example, an image can be modelled as a stochastic process with $\boldsymbol{t} = (t_1, t_2)$ being pixel coordinates. In this course, however, we restrict to the one-dimensional case $d = 1$.

**The state space $S$** is the set of all values that $X(t)$ can take. For temperature, $S = [0, \infty)$; for a dice toss, $S = \{1,2,3,4,5,6\}$.

> **Definition.** A stochastic process with a *discrete* index set and a *discrete* state space is called a **chain**.

To fully characterise a stochastic process, one must in principle specify the *joint distribution* of $\{X_t : t \in \bar{T}\}$ for every finite subset $\bar{T} \subseteq T$. This is an enormous amount of information, especially when $T$ is continuous. In practice, many processes of interest possess special structure (such as the Markov property) that allows a complete description with only a few parameters.

---

## 1.3 Quick Review of Probability Theory

### Foundational concepts

| Concept | Definition |
|---------|-----------|
| **Sample space** $\Omega$ | Set of all possible outcomes of an experiment |
| **Event** $E$ | Any subset $E \subseteq \Omega$ |
| **Probability** $\mathbb{P}$ | A measure assigning each event $E$ a number $\mathbb{P}[E] \in [0,1]$, with $\mathbb{P}[\Omega]=1$ and $\mathbb{P}[\varnothing]=0$ |

**Union of events.** For any two events $A$ and $B$, the *inclusion-exclusion* formula gives:

$$
\mathbb{P}[A \cup B] = \mathbb{P}[A] + \mathbb{P}[B] - \mathbb{P}[A \cap B]
$$

The subtraction corrects for double-counting the overlap $A \cap B$.

**Law of Total Probability.** Let $\{A_i\}$ be a disjoint partition of $\Omega$, meaning:

$$
\bigcup_i A_i = \Omega, \qquad \mathbb{P}[\Omega] = 1, \qquad A_i \cap A_j = \varnothing \quad \forall\, i \neq j
$$

Then, for any event $B$:

$$
\mathbb{P}[B] = \sum_i \mathbb{P}[B \cap A_i]
$$

This holds because the $A_i$ partition $\Omega$, so they also partition $B$; summing over all pieces recovers $\mathbb{P}[B]$ exactly.

**Independence.** Two events $A$ and $B$ are **independent** if and only if:

$$
\mathbb{P}[A \cap B] = \mathbb{P}[A]\,\mathbb{P}[B]
$$

More generally, $n$ events $A_1, \ldots, A_n$ are mutually independent if and only if every sub-collection satisfies the product formula. In particular:

$$
\mathbb{P}\!\left[\bigcap_{i=1}^n A_i\right] = \prod_{i=1}^n \mathbb{P}[A_i]
$$

---

### 1.3.1 Random Variables

A **random variable** (r.v.) is a variable whose value is determined by the outcome of a random experiment. It serves as a placeholder for an uncertain numerical result. By convention, random variables are denoted with capital letters ($X$, $Y$, $Z$) and their realised values with lowercase letters ($x$, $y$, $z$).

An event can always be expressed in terms of a random variable. For instance, $\{X \leq x\}$ is the event that $X$ takes a value no greater than $x$. Its probability, $\mathbb{P}[\{X \leq x\}]$, is a function of the real number $x$.

**Cumulative Distribution Function (CDF).** The CDF of $X$ is:

$$
F_X(x) = \mathbb{P}[\{X \leq x\}], \qquad F_X : \mathbb{R} \to [0,1]
$$

Key properties:
- $F_X(-\infty) = 0$ and $F_X(+\infty) = 1$.
- $F_X$ is **non-decreasing**: increasing $x$ can only include more outcomes in the event.
- $F_X$ is **right-continuous**:

$$
\lim_{x \to c^+} F_X(x) = F_X(c) \qquad \forall\, c \in \mathbb{R}
$$

**Discrete random variables** take values in a countable set $\{x_n\}_{n \in T}$. Their CDF is a step function: constant on each interval $[x_{i-1}, x_i)$ and jumping by $\mathbb{P}[X = x_i]$ at $x = x_i$.

**Continuous random variables** satisfy $\mathbb{P}[X = x] = 0$ for all $x$, so their CDF has no jumps and is continuous.

**Probability Density Function (pdf).** When $F_X$ is differentiable, we define:

$$
f_X(x) \equiv \frac{\mathrm{d}F_X(x)}{\mathrm{d}x}
$$

By the fundamental theorem of calculus:

$$
F_X(x) = \int_{-\infty}^x f(\xi)\,\mathrm{d}\xi, \qquad \mathbb{P}[a < X \leq b] = \int_a^b f(\xi)\,\mathrm{d}\xi
$$

![[Stochastic_Processes_2020_p9_img1.jpeg]]
*(a) — CDF for a discrete random variable*

![[Stochastic_Processes_2020_p9_img2.jpeg]]
*(b) — CDF for a continuous random variable*

**Figure 1.1** — Examples of Cumulative Distribution Functions (CDF)

---

### 1.3.2 Moments and Expected Values

**Moments** summarise the shape of a distribution with numbers.

The **$m$-th moment** of $X$ is:

$$
\mathbb{E}[X^m] = \sum_i x_i^m\,\mathbb{P}[X = x_i] \quad \text{(discrete)}
\qquad \text{or} \qquad
\mathbb{E}[X^m] = \int_{-\infty}^{+\infty} x^m f(x)\,\mathrm{d}x \quad \text{(continuous)}
$$

- The **first moment** $\mathbb{E}[X]$ is called the **mean**.
- The **$m$-th central moment** subtracts the mean first: $\mathbb{E}[(X - \mathbb{E}[X])^m]$.
- The **second central moment** is the **variance**:

$$
\mathrm{Var}[X] = \mathbb{E}[(X - \mathbb{E}[X])^2]
$$

**Expected value of a function.** For a function $g(x)$:

$$
\mathbb{E}[g(x)] = \sum_i \mathbb{P}[X = x_i]\,g(x_i) \tag{1.1}
$$

(discrete), or

$$
\mathbb{E}[g(x)] = \int_{\mathbb{R}} g(x) f(x)\,\mathrm{d}x \tag{1.2}
$$

(continuous). Both unify into the **Lebesgue–Stieltjes** form:

$$
\mathbb{E}[g(x)] = \int_{\mathbb{R}} g(x)\,\mathrm{d}F(x) \tag{1.3}
$$

We interpret (1.3) as (1.1) or (1.2) according to the nature of $X$.

---

### Many Variables

Given a pair $(X, Y)$ of random variables, their **joint CDF** is:

$$
F_{XY}(x, y) = \mathbb{P}[X \leq x \text{ and } Y \leq y]
$$

**Independence.** $X$ and $Y$ are independent if and only if their joint distribution *factorises everywhere*:

$$
X, Y \text{ independent} \iff F(x,y) = F_X(x)\,F_Y(y) \quad \forall\, x, y \tag{1.4}
$$

The same factorisation holds for their pdfs when they exist.

**Uncorrelation.** $X$ and $Y$ are **uncorrelated** if:

$$
\mathbb{E}[(X - \mu_X)(Y - \mu_Y)] = 0, \qquad \mu_X = \mathbb{E}[X],\ \mu_Y = \mathbb{E}[Y] \tag{1.5}
$$

> **Important:** Independence $\Rightarrow$ uncorrelation, but the converse is *false* in general.

**Proof that independence implies uncorrelation.** Expanding (1.5) by linearity of expectation:

$$
\mathbb{E}[(X-\mu_X)(Y-\mu_Y)] = \mathbb{E}[XY] - \mu_X\underbrace{\mathbb{E}[Y]}_{\mu_Y} - \mu_Y\underbrace{\mathbb{E}[X]}_{\mu_X} + \mu_X\mu_Y
$$

Under independence (1.4), $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y] = \mu_X\mu_Y$. Substituting:

$$
= \mu_X\mu_Y - \mu_X\mu_Y - \mu_Y\mu_X + \mu_X\mu_Y = 0 \qquad \square
$$

---

### Sum of Variables

Let $Z = X + Y$. Applying the law of total probability (conditioned on $Y$):

$$
\begin{aligned}
F_Z(z) &= \mathbb{P}[X + Y \leq z] = \mathbb{E}_Y[\mathbb{P}[X \leq z - Y \mid Y]] \\
&= \mathbb{E}_Y[F_X(z - Y)] = \int_{\mathbb{R}} F_X(z - \xi)\,\mathrm{d}F_Y(\xi)
\end{aligned}
$$

Since the roles of $X$ and $Y$ are symmetric:

$$
F_Z(z) = \int_{\mathbb{R}} F_Y(z - \eta)\,\mathrm{d}F_X(\eta)
$$

This is a **convolution**. If $X$ and $Y$ both have pdfs, differentiating gives the pdf of $Z$:

$$
f_Z(z) = \frac{\mathrm{d}F_Z}{\mathrm{d}z} = \int_{\mathbb{R}} f_X(z-\xi)\,f_Y(\xi)\,\mathrm{d}\xi
$$

In general, for any two random variables:

$$
\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y] \quad \text{(always)}
$$
$$
\mathrm{Var}[X + Y] = \mathrm{Var}[X] + \mathrm{Var}[Y] \quad \text{(if uncorrelated)}
$$

*(Proof: exercise)*

---

### Conditional Probabilities

For any events $A$ and $B$ with $\mathbb{P}[B] \neq 0$, the **conditional probability** of $A$ given $B$ is:

$$
\mathbb{P}[A \mid B] = \frac{\mathbb{P}[A \cap B]}{\mathbb{P}[B]}
$$

Rearranging gives the **product rule**: $\mathbb{P}[A \cap B] = \mathbb{P}[A \mid B]\,\mathbb{P}[B]$.

Substituting into the law of total probability, for a disjoint partition $\{B_i\}$ of $\Omega$:

$$
\mathbb{P}[A] = \sum_i \mathbb{P}[A \mid B_i]\,\mathbb{P}[B_i]
$$

---

### 1.3.3 Characteristic Functions

**Definition.** Let $X$ be a random variable with CDF $F$. Its **characteristic function** is:

$$
\phi_X(t) = \int_{\mathbb{R}} e^{it\lambda}\,\mathrm{d}F(\lambda) = \mathbb{E}[e^{itX}] \tag{1.6}
$$

For a *discrete* r.v. with possible values $\{\lambda_k\}$:

$$
\phi_X(t) = \sum_{k=0}^{+\infty} e^{it\lambda_k}\,\mathbb{P}[X = \lambda_k]
$$

For a *continuous* r.v. with pdf $p(x)$:

$$
\phi_X(t) = \int_{\mathbb{R}} e^{it\lambda}\,p(\lambda)\,\mathrm{d}\lambda
$$

The characteristic function is precisely the **Fourier transform** of the probability distribution. Because the Fourier transform is invertible, there is a one-to-one correspondence between characteristic functions and distribution functions. The formula recovering the CDF from its characteristic function is **Lévy's inversion formula**.

**Key properties:**

1. **Convolution property.** If $X_1, \ldots, X_n$ are independent, then:
   $$\phi_{X_1 + \cdots + X_n}(t) = \prod_{i=1}^n \phi_{X_i}(t)$$
   This follows because the pdf of a sum of independent r.v. is the convolution of their individual pdfs, and the Fourier transform converts convolution to pointwise multiplication.

2. **Moment recovery.** The $k$-th moment of $X$ (when it exists) is obtained by:
   $$\mathbb{E}[X^k] = \frac{1}{i^k}\,\phi^{(k)}(0) \tag{1.7}$$

**Derivation for the first two moments:**

$$
\phi'(t) = \frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[e^{itX}] = \mathbb{E}\!\left[\frac{\mathrm{d}e^{itX}}{\mathrm{d}t}\right] = \mathbb{E}[iX e^{itX}]
\quad \Rightarrow \quad \phi'(0) = i\,\mathbb{E}[X]
$$

$$
\phi''(t) = \mathbb{E}[i^2 X^2 e^{itX}] \quad \Rightarrow \quad \phi''(0) = i^2\,\mathbb{E}[X^2]
$$

(The interchange of derivative and expectation is justified by linearity.)

---

### 1.3.4 Probability Generating Function

For a discrete r.v. $X$ taking values in $\mathbb{N}_0 = \{0, 1, 2, \ldots\}$, the **probability generating function (pgf)** is:

$$
g(s) = \sum_{k=0}^{\infty} \underbrace{\mathbb{P}[X=k]}_{p_k} s^k = \mathbb{E}[s^X], \qquad s \in \mathbb{C} \tag{1.8}
$$

Since $p_k \geq 0$ and $\sum_{k=0}^\infty p_k = 1$, the series converges for $|s| \leq 1$ and is infinitely differentiable for $|s| < 1$.

**Relation to the characteristic function:**

$$
\phi(t) = \mathbb{E}[e^{itX}] = \mathbb{E}[(e^{it})^X] = g(e^{it})
$$

So the pgf is a reparametrisation of the characteristic function. All properties carry over:
- It uniquely determines the distribution of $X$.
- The pgf of a sum of independent r.v. is the product of their individual pgfs.
- Factorial moments are recovered by differentiation at $s = 1$:

$$
\mathbb{E}[X(X-1)\cdots(X-k+1)] = g^{(k)}(1) \tag{1.9}
$$

**Derivation for the first two factorial moments:**

$$
g'(s) = \sum_{k=1}^{+\infty} k\,p_k\,s^{k-1} \quad \Rightarrow \quad g'(1) = \sum_{k=1}^{+\infty} k\,p_k = \mathbb{E}[X]
$$

$$
g''(s) = \sum_{k=2}^{+\infty} k(k-1)\,p_k\,s^{k-2} \quad \Rightarrow \quad g''(1) = \mathbb{E}[X(X-1)]
$$

From these, one recovers $\mathbb{E}[X^2] = g''(1) + g'(1)$ and $\mathrm{Var}[X] = g''(1) + g'(1) - (g'(1))^2$.

---

**Example 1 — Sum of a Random Number of Random Variables**

Let $\{X_i\}_{i=1,\ldots,N}$ be i.i.d. r.v. taking values in $\mathbb{N}_0$, with common pgf $g(s)$. Let $N$ be an independent r.v. in $\mathbb{N}_0$ with pgf $g_N(s)$. Define:

$$
R = X_1 + \cdots + X_N
$$

We cannot simply write $g_R(s) = (g(s))^N$ because $N$ is random. Instead, we condition on $N$ and apply the law of total probability:

$$
\begin{aligned}
g_R(s) &= \mathbb{E}[s^R] = \mathbb{E}\bigl[\mathbb{E}[s^{X_1+\cdots+X_N} \mid N]\bigr] \\
&= \sum_{n=0}^{+\infty} \mathbb{E}[s^{X_1+\cdots+X_n} \mid N=n]\,\mathbb{P}[N=n]
\end{aligned}
$$

Since $\{X_i\}$ and $N$ are independent, conditioning on $N = n$ is superfluous for the $X_i$:

$$
= \sum_{n=0}^{+\infty} \mathbb{E}[s^{X_1+\cdots+X_n}]\,\mathbb{P}[N=n]
$$

Applying the convolution property for the fixed-$n$ sum:

$$
= \sum_{n=0}^{+\infty} g(s)^n\,\mathbb{P}[N=n] = \mathbb{E}[g(s)^N] = g_N[g(s)]
$$

**The pgf of $R$ is the composition $g_N \circ g$.**

**Mean.** Differentiating and using $g(1) = 1$ (normalization):

$$
\mathbb{E}[R] = g_R'(1) = g_N'[g(1)]\cdot g'(1) = g_N'(1)\cdot\mathbb{E}[X] = \mathbb{E}[N]\cdot\mathbb{E}[X]
$$

Intuitively: if $N$ were fixed, $\mathbb{E}[R] = N\,\mathbb{E}[X]$; since $N$ is random, we replace it by its mean.

**Variance.** Differentiating $g_R(s) = g_N[g(s)]$ twice:

$$
g_R''(s) = g_N''[g(s)]\,(g'(s))^2 + g_N'[g(s)]\,g''(s)
$$

Evaluating at $s = 1$:

$$
\begin{aligned}
g_R''(1) &= g_N''(1)\,\mathbb{E}[X]^2 + g_N'(1)\,\mathbb{E}[X(X-1)] \\
&= \mathbb{E}[N(N-1)]\,\mathbb{E}[X]^2 + \mathbb{E}[N]\,(\mathbb{E}[X^2] - \mathbb{E}[X]) \\
&= \mathbb{E}[N^2]\,\mathbb{E}[X]^2 - \mathbb{E}[N]\,\mathbb{E}[X]^2 + \mathbb{E}[N]\,\mathbb{E}[X^2] - \mathbb{E}[N]\,\mathbb{E}[X]
\end{aligned}
$$

Finally, using $\mathrm{Var}[R] = g_R''(1) + g_R'(1) - (g_R'(1))^2$:

$$
\boxed{\mathrm{Var}(R) = \mathbb{E}[N]\,\mathrm{Var}(X) + \mathbb{E}[X]^2\,\mathrm{Var}(N)}
$$

**Interpretation:** The first term $\mathbb{E}[N]\,\mathrm{Var}(X)$ is the variance due to the randomness *within* each $X_i$ (as if $N$ were fixed at its mean). The second term $\mathbb{E}[X]^2\,\mathrm{Var}(N)$ is the extra variance introduced by not knowing how many terms appear in the sum.

---

## 1.4 Discrete Distributions

### 1.4.1 Bernoulli Distribution

A random variable $X$ with exactly two possible values, 0 and 1, follows the **Bernoulli distribution** with parameter $p \in [0,1]$:

$$
\mathbb{P}(X = x) = \begin{cases} p & x = 1 \\ 1 - p & x = 0 \end{cases}
$$

$$
\mathbb{E}[X] = p, \qquad \mathrm{Var}(X) = p(1-p)
$$

**Indicator random variables.** For any event $A$, define its **indicator**:

$$
\mathbf{1}_A = \begin{cases} 1 & \text{if } A \text{ occurs} \\ 0 & \text{otherwise} \end{cases}
$$

This is a Bernoulli r.v. with $p = \mathbb{P}[A]$. Indicators are extremely useful for turning events into random variables.

---

### 1.4.2 Binomial Distribution

Consider $n$ independent trials $A_1, \ldots, A_n$, each succeeding with probability $p$. Let $Y$ count the total number of successes. Then $Y$ follows the **binomial distribution**:

$$
p_Y(k) \equiv \mathbb{P}(Y = k) = \binom{n}{k} p^k (1-p)^{n-k}, \qquad k = 0, 1, \ldots, n
$$

The binomial coefficient $\binom{n}{k}$ counts the number of ways to choose which $k$ of the $n$ trials succeed; each such pattern has probability $p^k(1-p)^{n-k}$.

Since $Y = \mathbf{1}(A_1) + \cdots + \mathbf{1}(A_n)$ is a sum of $n$ independent Bernoulli r.v., linearity gives:

$$
\mathbb{E}[Y] = np, \qquad \mathrm{Var}(Y) = np(1-p)
$$

---

### 1.4.3 Geometric Distribution

Consider an infinite sequence of i.i.d. trials. Let $Z$ be the number of **failures before the first success**, where each trial succeeds with probability $p$. The **geometric distribution** has:

$$
p_Z(k) = \mathbb{P}[Z = k] = p(1-p)^k, \qquad k \in \mathbb{N}_0
$$

This follows because the first $k$ trials all fail (probability $(1-p)^k$) and the $(k+1)$-th succeeds (probability $p$); since trials are independent, these probabilities multiply.

*Note:* An alternative convention defines $Z' = Z + 1$ as the number of trials until the first success (counting the success itself). The two conventions are interchangeable; context clarifies which is used.

**Mean by direct calculation:**

$$
\mathbb{E}[Z] = \sum_{k=0}^{+\infty} k\,p(1-p)^k = p(1-p)\sum_{k=1}^{+\infty} k(1-p)^{k-1}
$$

Recognising the sum as the derivative of a geometric series (with $a = 1-p < 1$):

$$
\sum_{k=1}^{+\infty} k\,a^{k-1} = \frac{\mathrm{d}}{\mathrm{d}a}\!\left(\sum_{k=0}^{+\infty} a^k\right) = \frac{\mathrm{d}}{\mathrm{d}a}\frac{1}{1-a} = \frac{1}{(1-a)^2}
$$

Substituting $a = 1-p$:

$$
\mathbb{E}[Z] = \frac{p(1-p)}{p^2} = \frac{1-p}{p}
$$

$$
\mathrm{Var}(Z) = \frac{1-p}{p^2}
$$

**Mean via tail sum formula.** For any non-negative integer-valued r.v. $Z$:

$$
\mathbb{E}[Z] = \sum_{k=0}^{+\infty} \mathbb{P}[Z > k] = \sum_{k=1}^{+\infty} \mathbb{P}[Z \geq k] \tag{1.10}
$$

*Proof of (1.10):* Writing $\mathbb{E}[Z] = \sum_{k=0}^{\infty} k\,p_k$ and expanding each multiple $k = 1 + 1 + \cdots + 1$ ($k$ times) as a column sum:

$$
\mathbb{E}[Z] = \sum_{k=0}^\infty \mathbb{P}[Z > k]
$$

Each column in the triangular array corresponds to a tail probability. $\square$

For the geometric distribution, $\mathbb{P}[Z \geq k] = (1-p)^k$, so:

$$
\mathbb{E}[Z] = \sum_{k=1}^{+\infty} (1-p)^k = (1-p)\cdot\frac{1}{1-(1-p)} = \frac{1-p}{p}
$$

confirming the earlier result.

---

### 1.4.4 Poisson Distribution

The **Poisson distribution** with parameter $\lambda > 0$ has probability mass function:

$$
p(k) = \frac{\lambda^k e^{-\lambda}}{k!}, \qquad k = 0, 1, 2, \ldots \tag{1.11}
$$

**Normalization.** Using the Taylor series $e^\lambda = \sum_{k=0}^\infty \frac{\lambda^k}{k!}$:

$$
\sum_{k=0}^{+\infty} p(k) = e^{-\lambda}\sum_{k=0}^{+\infty} \frac{\lambda^k}{k!} = e^{-\lambda} \cdot e^\lambda = 1 \tag{1.12}
$$

**Mean and variance:**

$$
\mathbb{E}[X] = \sum_{k=0}^{+\infty} k\,\frac{\lambda^k e^{-\lambda}}{k!} = \lambda e^{-\lambda} \underbrace{\sum_{k=1}^{+\infty} \frac{\lambda^{k-1}}{(k-1)!}}_{e^\lambda} = \lambda
$$

$$
\mathbb{E}[X(X-1)] = \sum_{k=2}^{+\infty} k(k-1)\frac{\lambda^k e^{-\lambda}}{k!} = \lambda^2 e^{-\lambda}\sum_{k=2}^{+\infty}\frac{\lambda^{k-2}}{(k-2)!} = \lambda^2
$$

$$
\mathbb{E}[X^2] = \mathbb{E}[X(X-1)] + \mathbb{E}[X] = \lambda^2 + \lambda \quad \Rightarrow \quad \mathrm{Var}[X] = \lambda
$$

**Poisson as a limit of the binomial.** A binomial distribution $\mathrm{Bin}(n,p)$ converges to $\mathrm{Poisson}(\lambda)$ when $n \to \infty$ and $p \to 0$ with the product $np = \lambda$ held fixed. This is the **law of rare events**: the Poisson distribution describes the number of occurrences of a rare event across a very large number of nearly-independent trials.

---

## 1.5 Continuous Distributions

### 1.5.1 Normal Distribution

The **normal (Gaussian) distribution** with mean $\mu$ and variance $\sigma^2$ has pdf:

$$
\phi(x;\mu,\sigma^2) = \frac{1}{\sqrt{2\pi}\,\sigma}\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

This distribution is ubiquitous due to the Central Limit Theorem. It will not be used extensively in this course.

---

### 1.5.2 Exponential Distribution

A non-negative r.v. $T$ has an **exponential distribution** with parameter $\lambda > 0$ if:

$$
f_T(t) = \begin{cases} \lambda e^{-\lambda t} & t \geq 0 \\ 0 & t < 0 \end{cases}
\qquad
F_T(t) = \begin{cases} 1 - e^{-\lambda t} & t \geq 0 \\ 0 & t < 0 \end{cases}
$$

**Moments:**

$$
\mathbb{E}[T] = \frac{1}{\lambda}, \qquad \mathrm{Var}[T] = \frac{1}{\lambda^2}, \qquad \mathbb{E}[T^k] = \frac{k!}{\lambda^k}
$$

**Computing the mean via the tail formula** (continuous analogue of (1.10)):

$$
\mathbb{E}[T] = \int_0^{+\infty} \mathbb{P}[T > t]\,\mathrm{d}t = \int_0^{+\infty} e^{-\lambda t}\,\mathrm{d}t = \frac{1}{\lambda}
$$

**Memoryless property.** The exponential distribution is the *only* continuous memoryless distribution. Formally, for any $t, x > 0$:

$$
\mathbb{P}[T > t + x \mid T > t] = \frac{\mathbb{P}[T > t + x]}{\mathbb{P}[T > t]} = \frac{e^{-\lambda(t+x)}}{e^{-\lambda t}} = e^{-\lambda x}
$$

This equals $\mathbb{P}[T > x]$ — the survival probability is identical regardless of how long the system has already survived. A particle that is still alive at time $t$ behaves statistically as if it were just born. This property makes the exponential distribution natural for modelling lifetimes, inter-arrival times in queues, and radioactive decay. In statistical mechanics, rapid chaotic interactions destroy memory of the initial state, so exponential waiting times arise frequently.

---

### 1.5.3 Uniform Distribution

A r.v. $U$ is **uniformly distributed** on $[a,b]$ (with $a < b$) if:

$$
f_U(u) = \begin{cases} \dfrac{1}{b-a} & a \leq u \leq b \\ 0 & \text{elsewhere} \end{cases}
\qquad
F_U(x) = \begin{cases} 0 & x \leq a \\ \dfrac{x-a}{b-a} & a < x \leq b \\ 1 & x > b \end{cases}
$$

Every subinterval of equal length has the same probability. Mean and variance:

$$
\mathbb{E}[U] = \frac{a+b}{2}, \qquad \mathrm{Var}(U) = \frac{(b-a)^2}{12}
$$

---

### 1.5.4 Gamma Distribution

The **gamma distribution** with parameters $\alpha > 0$ and $\lambda > 0$ has pdf:

$$
f(x) = \frac{\lambda}{\Gamma(\alpha)}(\lambda x)^{\alpha-1} e^{-\lambda x}, \qquad x > 0
$$

where $\Gamma(\alpha) = \int_0^\infty t^{\alpha-1}e^{-t}\,\mathrm{d}t$ is the gamma function (satisfying $\Gamma(n) = (n-1)!$ for positive integers).

**Key fact.** For integer $\alpha = n$, the sum of $n$ i.i.d. $\mathrm{Exp}(\lambda)$ r.v. follows $\mathrm{Gamma}(n, \lambda)$. This generalises to real $\alpha$:

$$
\mathbb{E}[X_\alpha] = \frac{\alpha}{\lambda}, \qquad \mathrm{Var}[X_\alpha] = \frac{\alpha}{\lambda^2}
$$

The gamma distribution generalises the exponential ($\alpha=1$) and connects to the chi-squared distribution ($\lambda = 1/2$, $\alpha = k/2$).

---

## 1.6 Conditional Probabilities

### Setup

The conditional probability of $A$ given $B$ (assuming $\mathbb{P}[B] \neq 0$) is:

$$
\mathbb{P}[A \mid B] = \frac{\mathbb{P}[A \cap B]}{\mathbb{P}[B]}
$$

Rearranging: $\mathbb{P}[A \cap B] = \mathbb{P}[A \mid B]\,\mathbb{P}[B]$ (the **product rule**).

**Law of Total Probability (full statement).** For a disjoint partition $\{B_i\}$ of $\Omega$:

$$
\mathbb{P}[A] = \sum_i \mathbb{P}[A \cap B_i] = \sum_i \mathbb{P}[A \mid B_i]\,\mathbb{P}[B_i]
$$

---

### 1.6.1 Conditioned on a Discrete Variable

Let $Y$ be discrete and $X$ arbitrary. The **conditional distribution** of $X$ given $Y = y$ is:

$$
F_{X|Y}(x \mid y) = \frac{\mathbb{P}[X \leq x,\, Y = y]}{\mathbb{P}[Y = y]}, \quad \text{provided } \mathbb{P}[Y=y] \neq 0 \tag{1.16}
$$

This is a valid CDF in $x$ for each fixed $y$.

The **joint CDF** can be reconstructed from conditional distributions:

$$
\mathbb{P}[X \leq x,\, Y \leq y] = \sum_{\eta \leq y} F_{X|Y}(x \mid \eta)\,\mathbb{P}[Y = \eta] = \int_{\eta \leq y} F_{X|Y}(x \mid \eta)\,\mathrm{d}F_Y(\eta)
$$

The **marginal distribution** of $X$ (setting $y \to +\infty$) is:

$$
\mathbb{P}[X \leq x] = \mathbb{E}[\mathbb{P}[X \leq x \mid Y]] = \int_{\mathbb{R}} F_{X|Y}(x \mid \eta)\,\mathrm{d}F_Y(\eta)
$$

**Law of Total Expectation (tower property):**

$$
\mathbb{E}[g(X)] = \mathbb{E}[\mathbb{E}[g(X) \mid Y]] = \int_{\mathbb{R}} \mathbb{E}[g(X) \mid Y = \eta]\,\mathrm{d}F_Y(\eta) \tag{1.17}
$$

where the inner conditional expectation is:
- **Discrete $X$:** $\mathbb{E}[g(X) \mid Y = \eta] = \sum_x g(x)\,\mathbb{P}[X = x \mid Y = \eta]$
- **Continuous $X$:** $\mathbb{E}[g(X) \mid Y = \eta] = \int_{\mathbb{R}} g(x)\,f_{X|Y}(x \mid \eta)\,\mathrm{d}x$

---

**Example 2 — Composition of Two Binomials**

Let $N \sim \mathrm{Bin}(M, q)$ and, given $N = n$, let $X \sim \mathrm{Bin}(n, p)$. What is the marginal distribution of $X$?

**Solution.** By the law of total probability:

$$
\mathbb{P}[X = k] = \sum_{n=0}^M \mathbb{P}[X = k \mid N = n]\,\mathbb{P}[N = n]
$$

Since $X$ cannot have more successes than trials, $\mathbb{P}[X = k \mid N = n] = 0$ for $n < k$. Restricting the sum and substituting the distributions:

$$
= \sum_{n=k}^M \binom{n}{k} p^k(1-p)^{n-k} \cdot \binom{M}{n} q^n(1-q)^{M-n}
$$

After algebraic manipulation (index shift $j = n-k$, highlighting a binomial sum):

$$
= \binom{M}{k}(pq)^k(1-pq)^{M-k}
$$

So $X \sim \mathrm{Bin}(M, pq)$.

**Probabilistic interpretation.** Start with $M$ balls. Each ball independently survives the first round with probability $q$ and the second round with probability $p$. The probability of surviving both is $pq$. Performing both rounds at once yields $X \sim \mathrm{Bin}(M, pq)$ directly.

---

**Exercise 1.6.1 — Composition of Binomial and Poisson**

Suppose $X \mid N \sim \mathrm{Bin}(N, p)$, where $N \sim \mathrm{Poisson}(\lambda)$. What is the marginal distribution of $X$?

*(Solution: $X \sim \mathrm{Poisson}(\lambda p)$)*

---

**Exercise 1.6.2 — Moments of Random Sums**

Assume $\xi_k$ and $N$ have finite moments:

$$
\mathbb{E}[\xi_k] = \mu; \quad \mathrm{Var}[\xi_k] = \sigma^2 \qquad \mathbb{E}[N] = \nu; \quad \mathrm{Var}[N] = \tau^2
$$

Show, using conditional distributions (not generating functions), that the mean and variance of $X = \xi_1 + \cdots + \xi_N$ are:

$$
\mathbb{E}[X] = \mu\nu, \qquad \mathrm{Var}[X] = \nu\sigma^2 + \mu^2\tau^2
$$

*(These match the results obtained via generating functions in Example 1.)*

---

### 1.6.2 Distribution of a Random Sum

Let $\{\xi_i\}$ be continuous i.i.d. r.v. with common pdf $f(z)$. The pdf of the fixed sum $\xi_1 + \cdots + \xi_n$ is the **$n$-fold convolution** $f^{(n)}(z)$, defined recursively:

$$
f^{(1)}(z) = f(z)
$$
$$
f^{(n)}(z) = \int_{\mathbb{R}} f^{(n-1)}(z - u)\,f(u)\,\mathrm{d}u, \qquad n > 1
$$

---

**Example 3 — Geometric Sum of Exponential Random Variables**

Let $\xi_i \sim \mathrm{Exp}(\lambda)$ i.i.d., and let $N$ have geometric distribution:

$$
p_N(n) = \beta(1-\beta)^{n-1}, \qquad n \in \{1, 2, 3, \ldots\} \tag{1.18}
$$

Set $Z = \xi_1 + \cdots + \xi_N$.

We know the $n$-fold convolution of $\mathrm{Exp}(\lambda)$ is the Gamma density:

$$
f^{(n)}(z) = \frac{\lambda^n}{(n-1)!}\,z^{n-1}\,e^{-\lambda z}, \qquad z \geq 0 \tag{1.19}
$$

**Finding the pdf of $Z$ by total probability:**

$$
\begin{aligned}
f_Z(z) &= \sum_{n=1}^{+\infty} f^{(n)}(z)\,p_N(n) = \sum_{n=1}^{+\infty} \frac{\lambda^n}{(n-1)!}\,z^{n-1}\,e^{-\lambda z}\,\beta(1-\beta)^{n-1}
\end{aligned}
$$

Factoring out terms independent of $n$ and shifting the index ($m = n-1$):

$$
= \lambda\beta\,e^{-\lambda z}\sum_{m=0}^{+\infty} \frac{[\lambda(1-\beta)z]^m}{m!} = \lambda\beta\,e^{-\lambda z}\,e^{\lambda(1-\beta)z} = \lambda\beta\,e^{-\lambda\beta z}
$$

**Conclusion:** $Z \sim \mathrm{Exp}(\lambda\beta)$.

**Verification via characteristic functions:**

$$
g_N(s) = \sum_{n=1}^{+\infty} \beta(1-\beta)^{n-1}s^n = \frac{\beta s}{1-(1-\beta)s}, \qquad \phi_\xi(t) = \frac{\lambda}{\lambda - it}
$$

The characteristic function of the random sum is $g_N(\phi_\xi(t))$:

$$
g_N\!\left(\frac{\lambda}{\lambda - it}\right) = \frac{\beta\lambda}{\beta\lambda - it}
$$

This has the same form as $\phi_\xi$ with $\lambda$ replaced by $\beta\lambda$, confirming $Z \sim \mathrm{Exp}(\lambda\beta)$.

---

### 1.6.3 Conditioned on a Continuous Variable

If $Y$ is continuous, $\mathbb{P}[Y = y] = 0$ for all $y$, so definition (1.16) breaks down. Instead, we define the **conditional pdf**:

$$
f_{X|Y}(x \mid y) = \frac{f_{XY}(x, y)}{f_Y(y)}, \quad \text{provided } f_Y(y) \neq 0 \tag{1.20}
$$

where $f_{XY}$ is the joint pdf of $(X, Y)$, and $f_Y$ is the marginal pdf of $Y$. Then:

$$
F_{X|Y}(x \mid y) = \int_{-\infty}^x f_{X|Y}(\xi \mid y)\,\mathrm{d}\xi
$$

**Joint distribution:**

$$
\mathbb{P}[X \leq x,\, Y \leq y] = \int_{-\infty}^y F_{X|Y}(x \mid \eta)\,f_Y(\eta)\,\mathrm{d}\eta = \int_{-\infty}^y F_{X|Y}(x \mid \eta)\,\mathrm{d}F_Y(\eta)
$$

**Marginal distribution** ($y \to +\infty$):

$$
\mathbb{P}[X \leq x] = \int_{\mathbb{R}} F_{X|Y}(x \mid \eta)\,\mathrm{d}F_Y(\eta)
$$

**Tower property.** Expected values of functions of $X$ satisfy the same formula as in the discrete case:

$$
\mathbb{E}[g(X)] = \int_{\mathbb{R}} \mathrm{d}\eta\,f_Y(\eta)\int_{\mathbb{R}} g(\xi)\,f_{X|Y}(\xi \mid \eta)\,\mathrm{d}\xi = \mathbb{E}[\mathbb{E}[g(X) \mid Y]]
$$

This confirms that definition (1.20) is consistent with the earlier discrete treatment: the tower property $\mathbb{E}[g(X)] = \mathbb{E}[\mathbb{E}[g(X) \mid Y]]$ holds regardless of whether $Y$ is discrete or continuous.
