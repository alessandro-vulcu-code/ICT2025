# Chapter 1 — Probability and Statistics

## Table of Contents

- [[#Introduction|Introduction]]
- [[#Stochastic Processes|Stochastic Processes]]
- [[#Quick Review of Probability Theory|Quick Review of Probability Theory]]
  - [[#Random Variables|Random Variables]]
  - [[#Moments and Expected Values|Moments and Expected Values]]
  - [[#Many Variables|Many Variables]]
  - [[#Sum of Variables|Sum of Variables]]
  - [[#Conditional Probabilities (Basics)|Conditional Probabilities (Basics)]]
  - [[#Characteristic Functions|Characteristic Functions]]
  - [[#Probability Generating Function|Probability Generating Function]]
- [[#Discrete Distributions|Discrete Distributions]]
  - [[#Bernoulli Distribution|Bernoulli Distribution]]
  - [[#Binomial Distribution|Binomial Distribution]]
  - [[#Geometric Distribution|Geometric Distribution]]
  - [[#Poisson Distribution|Poisson Distribution]]
- [[#Continuous Distributions|Continuous Distributions]]
  - [[#Normal Distribution|Normal Distribution]]
  - [[#Exponential Distribution|Exponential Distribution]]
  - [[#Uniform Distribution|Uniform Distribution]]
  - [[#Gamma Distribution|Gamma Distribution]]
- [[#Conditional Probabilities (Full Treatment)|Conditional Probabilities (Full Treatment)]]
  - [[#Discrete Case|Discrete Case]]
  - [[#Distribution of a Random Sum|Distribution of a Random Sum]]
  - [[#Continuous Case|Continuous Case]]
- [[#Summary Table|Summary Table]]

---

## Introduction

**Modeling** a natural phenomenon consists of linking its elements to *abstractions* in a *logical system* in order to deduce properties or behaviour. A model is **deterministic** if it predicts a single outcome from a given set of circumstances. A **stochastic model** predicts a set of possible outcomes weighted by their *probabilities*.

There is no universal best model. A useful model reflects all aspects relevant to the question at hand and allows calculations and predictions.

---

## Stochastic Processes

A **stochastic process** is a family of random variables $X_t$, where $t$ is a parameter running over a suitable index set $T$. It maps an independent variable $t \in T$ to a random outcome $X(t) \in S$; its graph *changes* every time the experiment is run.

- $T$ may be **discrete** (e.g. $T = \mathbb{N}$, $X(n)$ = outcome of the $n$-th dice toss) or **continuous** (e.g. $T = [0, \infty)$, $X(t)$ = temperature at time $t$).
- $T$ need not represent time — it can be spatial (e.g. pixel coordinates of an image). This course restricts to $d = 1$.
- The possible values of $X(t)$ lie in the **state space** $S$ (e.g. $S = [0,\infty)$ for temperature, $S = \{1,\ldots,6\}$ for a die).

> [!Important] Definition — Chain
> A stochastic process with **discrete index set** and **discrete state space** is called a **chain**.

To describe a stochastic process fully one must specify the joint distribution of any finite set $\{X_t : t \in \bar{T}\}$ for every $\bar{T} \subseteq T$. This is a huge amount of information; fortunately, special properties (such as the Markov property) allow full description with few parameters.

If all $X_t$ share the same distribution the process is said to be **stationary**.

---

## Quick Review of Probability Theory

Core concepts:

- **Sample space** $\Omega$: set of all possible outcomes.
- **Event** $E \subseteq \Omega$: any subset of outcomes.
- **Probability** $\mathbb{P}$: a measure on events with $\mathbb{P}[\Omega] = 1$, $\mathbb{P}[\varnothing] = 0$, values in $[0,1]$.

For two events $A$, $B$:

$$
\mathbb{P}[A \cup B] = \mathbb{P}[A] + \mathbb{P}[B] - \mathbb{P}[A \cap B]
$$

> [!Important] Law of Total Probability
> **Statement:** Let $\{A_i\}$ be a disjoint partition of $\Omega$ (i.e. $\bigcup_i A_i = \Omega$, $A_i \cap A_j = \varnothing$ for $i \neq j$). Then for any event $B$:
> $$\mathbb{P}[B] = \sum_i \mathbb{P}[B \cap A_i]$$
>
> **Intuition:** We decompose $B$ according to which partition element it intersects; summing over all parts gives the full probability.

> [!Important] Definition — Independence of Events
> $n$ events $A_1, \ldots, A_n$ are **independent** if and only if:
> $$\mathbb{P}\left[\bigcap_{i=1}^n A_i\right] = \prod_{i=1}^n \mathbb{P}[A_i]$$

---

### Random Variables

A **random variable** $X$ is a "variable that takes on its values by chance" — a placeholder for the outcome of an experiment. By convention: random variables in capitals ($X, Y, Z$), real numbers in lowercase ($x, y, z$).

> [!Important] Definition — Cumulative Distribution Function (CDF)
> The **(cumulative) distribution function** of $X$ is:
> $$F_X(x) = \mathbb{P}[\{X \leq x\}] \qquad F_X : \mathbb{R} \to [0,1]$$
>
> **Properties:**
> - $F(-\infty) = 0$, $F(+\infty) = 1$
> - Non-decreasing
> - Right-continuous: $\lim_{x \to c^+} F_X(x) = F_X(c)$ for all $c \in \mathbb{R}$

- If $X$ is **discrete**, $F_X(x)$ is a step function with jumps of size $\mathbb{P}[X = x_i]$ at each value $x_i$.
- If $\mathbb{P}[X = x] = 0$ for all $x$, then $F_X$ is continuous.

![[Stochastic_Processes_2020_p9_img1.jpeg]]
*Figure 1.1a — CDF for a discrete random variable: staircase shape with jumps of height $\mathbb{P}[X = x_i]$ at each mass point $x_i$.*

![[Stochastic_Processes_2020_p9_img2.jpeg]]
*Figure 1.1b — CDF for a continuous random variable: smooth, continuous, and non-decreasing curve from 0 to 1.*

> [!Important] Definition — Probability Density Function (PDF)
> If $F_X(x)$ is differentiable, its derivative is the **probability density function (pdf)**:
> $$f_X(x) \equiv \frac{\mathrm{d}F_X(x)}{\mathrm{d}x}$$
>
> By the fundamental theorem of calculus:
> $$F_X(x) = \int_{-\infty}^x f(\xi)\,\mathrm{d}\xi; \qquad \mathbb{P}[a < X \leq b] = \int_a^b f(\xi)\,\mathrm{d}\xi$$

---

### Moments and Expected Values

**Moments** summarize the shape of a distribution with numbers.

> [!Important] Definition — $m$-th Moment
> For a **discrete** random variable $X$:
> $$\mathbb{E}[X^m] = \sum_i x_i^m \, \mathbb{P}[X = x_i]$$
>
> For a **continuous** random variable $X$:
> $$\mathbb{E}[X^m] = \int_{-\infty}^{+\infty} x^m f(x)\,\mathrm{d}x$$
>
> The first moment $\mathbb{E}[X]$ is called the **mean**.

> [!Important] Definition — Central Moments and Variance
> The **$m$-th central moment** is $\mathbb{E}[(X - \mathbb{E}[X])^m]$.
>
> The **variance** is the second central moment:
> $$\operatorname{Var}[X] = \mathbb{E}[(X - \mathbb{E}[X])^2]$$

The **expected value of a function** $g(x)$:

$$\mathbb{E}[g(x)] = \sum_i \mathbb{P}[X = x_i]\, g(x_i) \tag{1.1}$$

in the discrete case, and:

$$\mathbb{E}[g(x)] = \int_{\mathbb{R}} g(x) f(x)\,\mathrm{d}x \tag{1.2}$$

in the continuous case. Both are unified by the *Lebesgue-Stieltjes* notation:

$$\mathbb{E}[g(x)] = \int_{\mathbb{R}} g(x)\,\mathrm{d}F(x) \tag{1.3}$$

---

### Many Variables

> [!Important] Definition — Joint CDF and Independence of Random Variables
> The **joint CDF** of a pair $(X, Y)$ is:
> $$F_{XY}(x, y) = \mathbb{P}[X \leq x \text{ and } Y \leq y]$$
>
> $X$ and $Y$ are **independent** if and only if their joint CDF factorizes everywhere:
> $$F(x, y) = F_X(x)\,F_Y(y) \quad \forall x, y$$
>
> The same factorization holds for their pdfs if they exist.

> [!Important] Definition — Uncorrelation
> $X$ and $Y$ are **uncorrelated** if:
> $$\mathbb{E}[(X - \mu_X)(Y - \mu_Y)] = 0 \qquad \mu_X = \mathbb{E}[X],\; \mu_Y = \mathbb{E}[Y]$$
>
> **Proof that independence implies uncorrelation:**
> Expand the covariance by linearity of expectation:
> $$\mathbb{E}[(X-\mu_X)(Y-\mu_Y)] = \mathbb{E}[XY] - \mu_X \mathbb{E}[Y] - \mu_Y \mathbb{E}[X] + \mu_X\mu_Y$$
> By independence $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y] = \mu_X\mu_Y$, so:
> $$= \mu_X\mu_Y - \mu_X\mu_Y - \mu_Y\mu_X + \mu_X\mu_Y = 0$$
>
> **Note:** The converse is false — uncorrelated does not imply independent.

---

### Sum of Variables

For $Z = X + Y$:

$$F_Z(z) = \mathbb{P}[Z \leq z] = \mathbb{E}_Y[\mathbb{P}[X \leq z - Y \mid Y]] = \int_{\mathbb{R}} F_X(z - \xi)\,\mathrm{d}F_Y(\xi)$$

By symmetry:

$$F_Z(z) = \int_{\mathbb{R}} F_Y(z - \eta)\,\mathrm{d}F_X(\eta)$$

This is a **convolution**. If both $X$ and $Y$ have pdfs, taking the derivative gives:

$$f_Z(z) = \int_{\mathbb{R}} f_X(z - \xi)\,f_Y(\xi)\,\mathrm{d}\xi$$

Key linearity results (always true):

$$\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$$

$$\operatorname{Var}[X + Y] = \operatorname{Var}[X] + \operatorname{Var}[Y] \qquad \text{if } X, Y \text{ are uncorrelated}$$

---

### Conditional Probabilities (Basics)

> [!Important] Definition — Conditional Probability
> For events $A$ and $B$ with $\mathbb{P}[B] \neq 0$:
> $$\mathbb{P}[A \mid B] = \frac{\mathbb{P}[A \cap B]}{\mathbb{P}[B]}$$
>
> **Product rule:** $\mathbb{P}[A \cap B] = \mathbb{P}[A \mid B]\,\mathbb{P}[B]$
>
> **Law of total probability (conditional form):** if $\{B_i\}$ partitions $\Omega$:
> $$\mathbb{P}[A] = \sum_i \mathbb{P}[A \mid B_i]\,\mathbb{P}[B_i]$$

---

### Characteristic Functions

> [!Important] Definition — Characteristic Function
> Let $X$ be a random variable with CDF $F$. Its **characteristic function** is:
> $$\phi_X(t) = \int_{\mathbb{R}} e^{it\lambda}\,\mathrm{d}F(\lambda) = \mathbb{E}[e^{itX}] \tag{1.6}$$
>
> - **Discrete case:** $\phi_X(t) = \sum_{k=0}^{+\infty} e^{it\lambda_k}\,\mathbb{P}[X = \lambda_k]$
> - **Continuous case:** $\phi_X(t) = \int_{\mathbb{R}} e^{it\lambda}\,p(\lambda)\,\mathrm{d}\lambda$
>
> The characteristic function is the **Fourier transform** of the probability distribution. It has a one-to-one correspondence with the CDF (*Lévy's inversion formula*).

> [!Important] Key Properties of Characteristic Functions
> 1. **Convolution → product:** If $X_1, \ldots, X_n$ are independent, the characteristic function of their sum equals the *product* of their individual characteristic functions (because the Fourier transform of a convolution is the product of Fourier transforms).
>
> 2. **Moment extraction:** Moments can be recovered by differentiating at $t = 0$:
> $$\mathbb{E}[X^k] = \frac{1}{i^k}\,\phi^{(k)}(0)$$
>
> **Proof for first two moments:**
> $$\phi'(t) = \frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[e^{itX}] = \mathbb{E}[iX e^{itX}] \Rightarrow \phi'(0) = i\mathbb{E}[X]$$
> $$\phi''(t) = \mathbb{E}[i^2 X^2 e^{itX}] \Rightarrow \phi''(0) = i^2 \mathbb{E}[X^2]$$
> (The derivative passes inside the expectation by linearity.)

---

### Probability Generating Function

> [!Important] Definition — Probability Generating Function (PGF)
> For a discrete random variable $X \in \mathbb{N}$ (nonnegative integers), the **probability generating function** is:
> $$g(s) = \sum_{k=0}^{\infty} \underbrace{\mathbb{P}[X=k]}_{p_k} s^k = \mathbb{E}[s^X] \qquad s \in \mathbb{C}$$
>
> Since $p_k \geq 0$ and $\sum_k p_k = 1$, $g(s)$ converges for $|s| \leq 1$ and is infinitely differentiable for $|s| < 1$.
>
> **Relation to characteristic function:**
> $$\phi(t) = \mathbb{E}[e^{itX}] = \mathbb{E}[(e^{it})^X] = g(e^{it})$$
>
> **Factorial moment formula:**
> $$\mathbb{E}[X(X-1)\cdots(X-k)] = g^{(k+1)}(1) \tag{1.9}$$
>
> **First two moments:**
> $$g'(s) = \sum_{k=1}^{+\infty} k p_k s^{k-1} \Rightarrow g'(1) = \mathbb{E}[X]$$
> $$g''(s) = \sum_{k=2}^{+\infty} k(k-1) p_k s^{k-2} \Rightarrow g''(1) = \mathbb{E}[X(X-1)]$$

The PGF shares the same features as the characteristic function: recovery of the CDF, convolution property (sum of independent r.v. → product of PGFs), and moment extraction.

> [!Example] Example 1 — Sum of a Random Number of Random Variables
> **Problem:** Let $\{X_i\}_{i=1,\dots,N}$ be i.i.d. discrete nonneg-integer-valued r.v. with PGF $g(s)$. Let $N$ be an independent discrete r.v. with $N \in \mathbb{N}$ and PGF $g_N(s)$. Find the mean and variance of $R = X_1 + \cdots + X_N$.
>
> **Approach:** $N$ is random so the convolution property cannot be applied directly. Use the law of total probability: condition on $N = n$, apply convolution for fixed $n$, then average over $N$.
>
> **Solution:**
>
> 1. Compute $g_R(s) = \mathbb{E}[s^R]$ by iterated expectation:
> $$g_R(s) = \mathbb{E}\{\mathbb{E}[s^{X_1+\cdots+X_N} \mid N]\}$$
>
> 2. Expand the outer expectation:
> $$= \sum_{n=0}^{+\infty} \mathbb{E}[s^{X_1+\cdots+X_n} \mid N=n]\,\mathbb{P}[N=n]$$
>
> 3. Since $\{X_i\}$ and $N$ are independent, $\mathbb{E}[s^{X_1+\cdots+X_n}\mid N=n] = \mathbb{E}[s^{X_1+\cdots+X_n}]$.
>
> 4. Apply convolution: $\mathbb{E}[s^{X_1+\cdots+X_n}] = g(s)^n$. Thus:
> $$g_R(s) = \sum_{n=0}^{+\infty} g(s)^n\,\mathbb{P}[N=n] = \mathbb{E}[g(s)^N] = g_N[g(s)]$$
>
> 5. **Mean:** differentiate $g_R(s) = g_N[g(s)]$ and evaluate at $s=1$:
> $$\mathbb{E}[R] = g_R'(1) = g_N'[g(1)]\cdot g'(1)$$
> Since $g(1) = \sum_k p_k = 1$ (normalization) and $g'(1) = \mathbb{E}[X]$:
> $$\mathbb{E}[R] = g_N'(1)\cdot\mathbb{E}[X] = \mathbb{E}[N]\cdot\mathbb{E}[X]$$
>
> 6. **Second derivative for variance:**
> $$g_R''(s) = g_N''[g(s)](g'(s))^2 + g_N'(g(s))\,g''(s)$$
> At $s=1$:
> $$g_R''(1) = g_N''(1)\,\mathbb{E}[X]^2 + g_N'(1)\,\mathbb{E}[X^2-X]$$
> $$= \mathbb{E}[N^2-N]\,\mathbb{E}[X]^2 + \mathbb{E}[N]\,(\mathbb{E}[X^2]-\mathbb{E}[X])$$
> $$= \mathbb{E}[N^2]\mathbb{E}[X]^2 + \mathbb{E}[N]\operatorname{Var}(X) - \mathbb{E}[N]\mathbb{E}[X]$$
>
> 7. **Variance:**
> $$\operatorname{Var}(R) = \mathbb{E}[R^2] - \mathbb{E}[R]^2 = g_R''(1) + g_R'(1) - (g_R'(1))^2$$
> $$= \mathbb{E}[N]\,\operatorname{Var}(X) + \mathbb{E}[X]^2\,\operatorname{Var}(N)$$
>
> **Result:**
> $$\mathbb{E}[R] = \mathbb{E}[N]\cdot\mathbb{E}[X]$$
> $$\operatorname{Var}(R) = \mathbb{E}[N]\,\operatorname{Var}(X) + \mathbb{E}[X]^2\,\operatorname{Var}(N)$$
>
> **Takeaway:** The first term $\mathbb{E}[N]\operatorname{Var}(X)$ is the "fixed-$N$" variance scaled by the expected count. The second term $\mathbb{E}[X]^2\operatorname{Var}(N)$ captures the extra randomness from the random number of summands.

---

## Discrete Distributions

### Bernoulli Distribution

> [!Important] Definition — Bernoulli Distribution
> A random variable $X \in \{0,1\}$ with:
> $$\mathbb{P}(X=x) = \begin{cases} p & x=1 \\ 1-p & x=0 \end{cases}$$
> $$\mathbb{E}[X] = p; \qquad \operatorname{Var}(X) = p(1-p)$$
>
> **Indicator variable:** for any event $A$, define:
> $$\mathbb{1}(A) \equiv \mathbb{1}_A = \begin{cases} 1 & \text{if } A \text{ occurs} \\ 0 & \text{otherwise} \end{cases}$$
> This is a Bernoulli r.v. with parameter $p = \mathbb{P}[A]$.

---

### Binomial Distribution

> [!Important] Definition — Binomial Distribution
> Let $Y$ count the number of successes in $n$ independent trials each with success probability $p$. Then $Y$ has the **binomial distribution**:
> $$p_Y(k) = \mathbb{P}(Y=k) = \binom{n}{k} p^k (1-p)^{n-k} \quad k = 0, 1, \ldots, n$$
>
> Writing $Y = \mathbb{1}(A_1) + \cdots + \mathbb{1}(A_n)$ as a sum of $n$ Bernoulli r.v.:
> $$\mathbb{E}[Y] = np; \qquad \operatorname{Var}(Y) = np(1-p)$$

---

### Geometric Distribution

> [!Important] Definition — Geometric Distribution
> Let $Z$ be the number of **failures before the first success** in a sequence of i.i.d. trials each with success probability $p$. Then:
> $$p_Z(k) = \mathbb{P}[Z=k] = p(1-p)^k \qquad k \in \mathbb{N}$$
>
> *(Alternatively, $Z' = Z + 1$ counts the total number of attempts to get one success.)*
>
> **Mean:**
> $$\mathbb{E}[Z] = \frac{1-p}{p}$$
>
> **Variance:**
> $$\operatorname{Var}(Z) = \frac{1-p}{p^2}$$

> [!Important] Proof of $\mathbb{E}[Z]$ (two methods)
> **Method 1 — Direct sum:**
> $$\mathbb{E}[Z] = \sum_{k=0}^{+\infty} k\,p(1-p)^k = p(1-p)\sum_{k=1}^{+\infty} k(1-p)^{k-1}$$
> Recognise the sum as the derivative of the geometric series $\sum_{k=0}^\infty a^k = \frac{1}{1-a}$:
> $$\sum_{k=1}^{+\infty} k a^{k-1} = \frac{\mathrm{d}}{\mathrm{d}a}\frac{1}{1-a} = \frac{1}{(1-a)^2} \quad a = 1-p$$
> Substituting: $\mathbb{E}[Z] = \frac{p(1-p)}{p^2} = \frac{1-p}{p}$.
>
> **Method 2 — Tail sum formula:**
> For any non-negative integer-valued r.v. $Z$:
> $$\mathbb{E}[Z] = \sum_{k=0}^{+\infty} \mathbb{P}[Z > k] = \sum_{k=1}^{+\infty} \mathbb{P}[Z \geq k] \tag{1.10}$$
> Here $\mathbb{P}[Z \geq k] = (1-p)^k$ (probability of at least $k$ failures), so:
> $$\mathbb{E}[Z] = \sum_{k=1}^{+\infty}(1-p)^k = (1-p)\sum_{k=0}^{+\infty}(1-p)^k = (1-p)\cdot\frac{1}{1-(1-p)} = \frac{1-p}{p}$$
>
> **Proof of (1.10):** Write $\mathbb{E}[Z] = \sum_k k p_k = 0 \cdot p_0 + 1\cdot p_1 + 2\cdot p_2 + \ldots$. Replace each coefficient $k$ by a sum of $k$ ones, then regroup by columns: the $j$-th column sum equals $\mathbb{P}[Z > j-1]$, giving $\sum_{k=0}^\infty \mathbb{P}[Z > k]$.

---

### Poisson Distribution

> [!Important] Definition — Poisson Distribution
> The **Poisson distribution** with parameter $\lambda > 0$ has pmf:
> $$p(k) = \frac{\lambda^k e^{-\lambda}}{k!} \qquad k = 0, 1, 2, \ldots \tag{1.11}$$
>
> **Normalization** follows from $e^\lambda = \sum_{k=0}^\infty \frac{\lambda^k}{k!}$.
>
> **Moments:**
> $$\mathbb{E}[X] = \lambda; \qquad \operatorname{Var}[X] = \lambda$$
>
> **Proof:**
> $$\mathbb{E}[X] = \sum_{k=0}^{+\infty} k\frac{\lambda^k e^{-\lambda}}{k!} = \lambda e^{-\lambda}\underbrace{\sum_{k=1}^{+\infty}\frac{\lambda^{k-1}}{(k-1)!}}_{e^\lambda} = \lambda$$
> $$\mathbb{E}[X(X-1)] = \lambda^2 e^{-\lambda}\sum_{k=2}^{+\infty}\frac{\lambda^{k-2}}{(k-2)!} = \lambda^2$$
> $$\mathbb{E}[X^2] = \mathbb{E}[X(X-1)] + \mathbb{E}[X] = \lambda^2 + \lambda$$
> $$\operatorname{Var}[X] = \lambda^2 + \lambda - \lambda^2 = \lambda$$
>
> **Poisson limit theorem (law of rare events):** Binomial$(n, p)$ converges to Poisson$(\lambda)$ as $n \to \infty$, $p \to 0$, with $np = \lambda$ fixed.

---

## Continuous Distributions

### Normal Distribution

> [!Important] Definition — Normal (Gaussian) Distribution
> The **normal distribution** with mean $\mu$ and variance $\sigma^2$:
> $$\phi(x;\mu,\sigma^2) = \frac{1}{\sqrt{2\pi}\,\sigma}\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$
> *(Used sparingly in this course.)*

---

### Exponential Distribution

> [!Important] Definition — Exponential Distribution
> A non-negative r.v. $T$ has **exponential distribution** with parameter $\lambda > 0$ if:
> $$f_T(t) = \begin{cases}\lambda e^{-\lambda t} & t \geq 0 \\ 0 & t < 0\end{cases}$$
>
> **CDF:**
> $$F_T(t) = \begin{cases}1 - e^{-\lambda t} & t \geq 0 \\ 0 & t < 0\end{cases}$$
>
> **Moments:**
> $$\mathbb{E}[T] = \frac{1}{\lambda}; \qquad \operatorname{Var}[T] = \frac{1}{\lambda^2}; \qquad \mathbb{E}[T^k] = \frac{1}{\lambda^k}$$
>
> **Proof of mean (continuous tail sum):**
> $$\mathbb{E}[T] = \int_0^{+\infty} \mathbb{P}[T > t]\,\mathrm{d}t = \int_0^{+\infty} e^{-\lambda t}\,\mathrm{d}t = \frac{1}{\lambda}$$

> [!Important] Memoryless Property of the Exponential Distribution
> **Statement:** For the exponential distribution, conditional survival probabilities depend only on the elapsed time:
> $$\mathbb{P}[T > t + x \mid T > t] = e^{-\lambda x} = \mathbb{P}[T > x]$$
>
> **Proof:**
> $$\mathbb{P}[T > t+x \mid T > t] = \frac{\mathbb{P}[T > t+x,\; T > t]}{\mathbb{P}[T > t]}$$
> Since $x > 0$, $T > t+x$ implies $T > t$, so the numerator simplifies:
> $$= \frac{\mathbb{P}[T > t+x]}{\mathbb{P}[T > t]} = \frac{e^{-\lambda(t+x)}}{e^{-\lambda t}} = e^{-\lambda x}$$
>
> **Intuition:** A particle still alive at time $t$ has "forgotten" its age — its future survival statistics are identical to those of a newly born particle. This is the **memoryless property**, unique to the exponential distribution among continuous distributions. It models processes where past history carries no information (e.g. thermal bath interactions in statistical mechanics).

---

### Uniform Distribution

> [!Important] Definition — Uniform Distribution
> A r.v. $U$ is **uniformly distributed** on $[a,b]$ ($a < b$) if:
> $$f_U(u) = \begin{cases}\frac{1}{b-a} & a \leq u \leq b \\ 0 & \text{elsewhere}\end{cases}$$
>
> **CDF:**
> $$F_U(x) = \begin{cases}0 & u \leq a \\ \frac{x-a}{b-a} & a < x \leq b \\ 1 & x > b\end{cases}$$
>
> **Moments:**
> $$\mathbb{E}[U] = \int_a^b \frac{u}{b-a}\,\mathrm{d}u = \frac{b+a}{2}; \qquad \operatorname{Var}(U) = \frac{(b-a)^2}{12}$$

---

### Gamma Distribution

> [!Important] Definition — Gamma Distribution
> The **gamma distribution** with parameters $\alpha > 0$ and $\lambda > 0$ has pdf:
> $$f(x) = \frac{\lambda}{\Gamma(\alpha)}(\lambda x)^{\alpha-1} e^{-\lambda x} \qquad x > 0$$
>
> For integer $\alpha$, the gamma distribution is the distribution of the sum of $\alpha$ i.i.d. Exp$(\lambda)$ random variables.
>
> **Moments:**
> $$\mathbb{E}[X_\alpha] = \frac{\alpha}{\lambda}; \qquad \operatorname{Var}[X_\alpha] = \frac{\alpha}{\lambda^2}$$
> *(These hold for all $\alpha \in \mathbb{R}$.)*

---

## Conditional Probabilities (Full Treatment)

### Discrete Case

> [!Important] Definition — Conditional CDF (Discrete Conditioning)
> Let $Y$ be a discrete r.v. and $X$ arbitrary. The **conditioned distribution of $X$ given $Y$** is:
> $$F_{X|Y}(x|y) = \frac{\mathbb{P}[X \leq x, Y = y]}{\mathbb{P}[Y = y]} \qquad \text{if } \mathbb{P}[Y=y] \neq 0 \tag{1.16}$$
>
> $F_{X|Y}$ is a proper distribution in $x$ for each fixed $y$.

**Joint CDF** via conditioning:

$$\mathbb{P}[X \leq x, Y \leq y] = \sum_{\eta \leq y} F_{X|Y}(x|\eta)\,\mathbb{P}[Y=\eta] = \int_{\eta \leq y} F_{X|Y}(x|\eta)\,\mathrm{d}F_Y(\eta)$$

**Marginal CDF** (set $y = +\infty$):

$$\mathbb{P}[X \leq x] = \mathbb{E}[\mathbb{P}[X \leq x \mid Y]] = \int_{\mathbb{R}} F_{X|Y}(x|\eta)\,\mathrm{d}F_Y(\eta)$$

**Expected value via iterated conditioning:**

$$\mathbb{E}[g(X)] = \mathbb{E}[\mathbb{E}[g(X)|Y]] = \int_{\mathbb{R}} \mathbb{E}[g(X)|Y=\eta]\,\mathrm{d}F_Y(\eta) \tag{1.17}$$

where:
- If $X$ discrete: $\mathbb{E}[g(X)|Y=\eta] = \sum_x g(x)\,\mathbb{P}[X=x|Y=\eta]$
- If $X$ continuous: $\mathbb{E}[g(X)|Y=\eta] = \int_{\mathbb{R}} g(x)\,f_{X|Y}(x|\eta)\,\mathrm{d}x$

> [!Example] Example 2 — Composition of Binomials
> **Problem:** Let $X \mid N \sim \text{Binomial}(N, p)$ and $N \sim \text{Binomial}(M, q)$. Find the marginal distribution of $X$.
>
> **Approach:** Apply the law of total probability, summing the product of conditional and marginal pmfs over all valid values of $N$.
>
> **Solution:**
>
> 1. Conditional pmf of $X$ given $N = n$:
> $$p_{X|N}(k|n) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, \ldots, n$$
>
> 2. Marginal pmf of $N$:
> $$p_N(n) = \binom{M}{n} q^n (1-q)^{M-n}, \quad n = 0, \ldots, M$$
>
> 3. Law of total probability (note: $p_{X|N}(k|n) = 0$ for $k > n$, so sum starts at $n=k$):
> $$\mathbb{P}[X=k] = \sum_{n=k}^M \binom{n}{k} p^k (1-p)^{n-k} \binom{M}{n} q^n (1-q)^{M-n}$$
>
> 4. Extract terms not depending on $n$:
> $$= \frac{M!}{k!} p^k (1-q)^M \sum_{n=k}^M \frac{(1-p)^{n-k} q^n (1-q)^{-n}}{(n-k)!(M-n)!}$$
>
> 5. Factor out $\left(\frac{q}{1-q}\right)^k$ and substitute $j = n-k$:
> $$= \frac{M!}{k!} p^k (1-q)^M \left(\frac{q}{1-q}\right)^k \sum_{j=0}^{M-k} \frac{(M-k)!}{j!(M-k-j)!} (1-p)^j \left(\frac{q}{1-q}\right)^j$$
>
> 6. Recognise the binomial sum $\sum_{j=0}^{M-k}\binom{M-k}{j}(1-p)^j\left(\frac{q}{1-q}\right)^j = \left(1+\frac{q(1-p)}{1-q}\right)^{M-k}$:
>
> $$= \binom{M}{k}(pq)^k(1-q)^{M-k}\left(\frac{1-pq}{1-q}\right)^{M-k} = \binom{M}{k}(pq)^k(1-pq)^{M-k}$$
>
> **Result:** $X \sim \text{Binomial}(M, pq)$.
>
> **Takeaway:** Two consecutive thinning operations (keep with prob $q$, then keep with prob $p$) are equivalent to a single thinning with probability $pq$. This result generalises to Poisson processes (thinning property).

> [!Example] Exercise 1.6.1 — Composition of Binomial and Poisson
> **Problem:** $X \mid N \sim \text{Binomial}(N, p)$ and $N \sim \text{Poisson}(\lambda)$. Find the marginal distribution of $X$.
>
> **Approach:** Law of total probability summing over $n = 0, 1, 2, \ldots$
>
> **Solution:**
>
> $$\mathbb{P}[X=k] = \sum_{n=k}^{+\infty} \binom{n}{k} p^k (1-p)^{n-k} \frac{\lambda^n e^{-\lambda}}{n!}$$
>
> Extract terms independent of $n$ and substitute $j = n - k$:
>
> $$= \frac{p^k e^{-\lambda}}{k!} \sum_{j=0}^{+\infty} \frac{[\lambda(1-p)]^j \lambda^k}{j!} = \frac{(\lambda p)^k e^{-\lambda}}{k!} e^{\lambda(1-p)} = \frac{(\lambda p)^k e^{-\lambda p}}{k!}$$
>
> **Result:** $X \sim \text{Poisson}(\lambda p)$.
>
> **Takeaway:** Poisson-thinning: if arrivals are Poisson$(\lambda)$ and each is independently kept with probability $p$, the retained count is Poisson$(\lambda p)$.

> [!Example] Exercise 1.6.2 — Moments of Random Sums
> **Problem:** Let $\xi_k$ be i.i.d. with $\mathbb{E}[\xi_k]=\mu$, $\operatorname{Var}[\xi_k]=\sigma^2$, and $N$ independent with $\mathbb{E}[N]=\nu$, $\operatorname{Var}[N]=\tau^2$. Show, using conditional distributions, that for $X = \xi_1 + \cdots + \xi_N$:
> $$\mathbb{E}[X] = \mu\nu; \qquad \operatorname{Var}[X] = \nu\sigma^2 + \mu^2\tau^2$$
>
> **Solution:**
>
> **Mean:**
> $$\mathbb{E}[X] = \mathbb{E}[\mathbb{E}[X|N]] = \mathbb{E}[N\mu] = \mu\mathbb{E}[N] = \mu\nu$$
>
> **Variance** via the *law of total variance*:
> $$\operatorname{Var}(X) = \mathbb{E}[\operatorname{Var}(X|N)] + \operatorname{Var}(\mathbb{E}[X|N])$$
>
> - Given $N = n$: $\operatorname{Var}(X|N=n) = n\sigma^2$, so $\mathbb{E}[\operatorname{Var}(X|N)] = \sigma^2 \mathbb{E}[N] = \nu\sigma^2$.
> - $\mathbb{E}[X|N] = N\mu$, so $\operatorname{Var}(\mathbb{E}[X|N]) = \operatorname{Var}(N\mu) = \mu^2\tau^2$.
>
> $$\operatorname{Var}(X) = \nu\sigma^2 + \mu^2\tau^2$$
>
> **Takeaway:** Consistent with the PGF derivation in Example 1. The two terms decompose variance into "within-group" and "between-group" contributions.

---

### Distribution of a Random Sum

> [!Important] $n$-fold Convolution
> Let $\{\xi_i\}$ be continuous i.i.d. r.v. with pdf $f(z)$. The pdf of the fixed sum $\xi_1 + \cdots + \xi_n$ is the **$n$-fold convolution** $f^{(n)}(z)$, defined recursively:
> $$f^{(1)}(z) = f(z)$$
> $$f^{(n)}(z) = \int_{\mathbb{R}} f^{(n-1)}(z-u)\,f(u)\,\mathrm{d}u \qquad \forall n > 1$$

> [!Example] Example 3 — Geometric Sum of Exponential Random Variables
> **Problem:** Let $\xi_i \overset{\text{i.i.d.}}{\sim} \text{Exp}(\lambda)$. Let $N \sim \text{Geometric}$ with:
> $$p_N(n) = \beta(1-\beta)^{n-1} \quad n \in \mathbb{N}\setminus\{0\} \tag{1.18}$$
> Find the distribution of $Z = \xi_1 + \cdots + \xi_N$.
>
> **Known fact:** The $n$-fold convolution of Exp$(\lambda)$ is the Gamma density:
> $$f^{(n)}(z) = \frac{\lambda^n}{(n-1)!} z^{n-1} e^{-\lambda z}, \quad z \geq 0 \tag{1.19}$$
>
> **Solution (via law of total probability):**
>
> 1. Apply total probability ($p_N(0) = 0$):
> $$f_Z(z) = \sum_{n=1}^{+\infty} f^{(n)}(z)\,p_N(n) = \sum_{n=1}^{+\infty} \frac{\lambda^n}{(n-1)!} z^{n-1} e^{-\lambda z}\,\beta(1-\beta)^{n-1}$$
>
> 2. Extract constants:
> $$= \lambda\beta e^{-\lambda z} \sum_{n=1}^{+\infty} \frac{[\lambda(1-\beta)z]^{n-1}}{(n-1)!}$$
>
> 3. Shift index, recognise exponential series:
> $$= \lambda\beta e^{-\lambda z} e^{\lambda(1-\beta)z} = \lambda\beta e^{-\lambda\beta z}, \quad z \geq 0$$
>
> **Alternative (via characteristic functions):**
> $$g_N(s) = \frac{\beta s}{1-(1-\beta)s}; \qquad \phi(t) = \frac{\lambda}{\lambda - it}$$
> $$g_N(\phi(t)) = \frac{\beta\lambda}{\beta\lambda - it}$$
> This is the characteristic function of Exp$(\beta\lambda)$, confirming the result.
>
> **Result:** $Z \sim \text{Exp}(\lambda\beta)$.
>
> **Takeaway:** A geometric mixture of gamma (i.e. convolutions of exponential) distributions is again exponential. The effective rate is $\lambda\beta$: the exponential rate $\lambda$ is deflated by the geometric success probability $\beta$.

---

### Continuous Case

> [!Important] Definition — Conditional PDF (Continuous Conditioning)
> If $Y$ is continuous, $\mathbb{P}[Y=y] = 0$ for all $y$, so (1.16) is undefined. Instead define the **conditional pdf**:
> $$f_{X|Y}(x|y) = \frac{f_{XY}(x,y)}{f_Y(y)} \qquad \text{if } f_Y(y) \neq 0 \tag{1.20}$$
>
> And accordingly:
> $$F_{X|Y}(x|y) = \int_{-\infty}^x f_{X|Y}(\xi|y)\,\mathrm{d}\xi$$

**Joint distribution:**

$$\mathbb{P}[X \leq x, Y \leq y] = \int_{-\infty}^y F_{X|Y}(x|\eta)\,\mathrm{d}F_Y(\eta)$$

**Marginal:**

$$\mathbb{P}[X \leq x] = \int_{-\infty}^{+\infty} F_{X|Y}(x|\eta)\,\mathrm{d}F_Y(\eta)$$

**Iterated expectation:**

$$\mathbb{E}[g(X)] = \int_{\mathbb{R}} \mathbb{E}[g(X)|Y=\eta]\,\mathrm{d}F_Y(\eta) = \mathbb{E}[\mathbb{E}[g(X)|Y]]$$

These are the same formulas as in the discrete case, confirming that definition (1.20) is consistent.

---

## Summary Table

| Distribution | Type | PMF / PDF | Mean | Variance | Key property |
|---|---|---|---|---|---|
| Bernoulli$(p)$ | Discrete | $p$ for $X=1$, $1-p$ for $X=0$ | $p$ | $p(1-p)$ | Indicator of an event |
| Binomial$(n,p)$ | Discrete | $\binom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ | Sum of $n$ Bernoullis |
| Geometric$(p)$ | Discrete | $p(1-p)^k$, $k\geq 0$ | $\frac{1-p}{p}$ | $\frac{1-p}{p^2}$ | Failures before first success; used with tail sum formula |
| Poisson$(\lambda)$ | Discrete | $\frac{\lambda^k e^{-\lambda}}{k!}$ | $\lambda$ | $\lambda$ | Limit of Binomial; law of rare events |
| Normal$(\mu,\sigma^2)$ | Continuous | $\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ | Central limit theorem |
| Exponential$(\lambda)$ | Continuous | $\lambda e^{-\lambda t}$, $t\geq 0$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | Memoryless; models lifetimes |
| Uniform$[a,b]$ | Continuous | $\frac{1}{b-a}$, $a\leq u\leq b$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | Equal probability on interval |
| Gamma$(\alpha,\lambda)$ | Continuous | $\frac{\lambda}{\Gamma(\alpha)}(\lambda x)^{\alpha-1}e^{-\lambda x}$ | $\frac{\alpha}{\lambda}$ | $\frac{\alpha}{\lambda^2}$ | Sum of $\alpha$ i.i.d. Exp$(\lambda)$ |

| Tool | Formula | When to use |
|---|---|---|
| Characteristic function | $\phi_X(t) = \mathbb{E}[e^{itX}]$ | Sums of independent r.v.; moment extraction via $\mathbb{E}[X^k]=\frac{1}{i^k}\phi^{(k)}(0)$ |
| Probability generating function | $g(s) = \mathbb{E}[s^X]$ | Discrete nonneg-integer r.v.; random sums; factorial moments via $g^{(k)}(1)$ |
| Law of total probability | $\mathbb{P}[A]=\sum_i \mathbb{P}[A\mid B_i]\mathbb{P}[B_i]$ | Marginalising over a partition; conditioning on a discrete r.v. |
| Iterated expectation | $\mathbb{E}[g(X)]=\mathbb{E}[\mathbb{E}[g(X)\mid Y]]$ | Computing moments of random sums; any two-stage randomness |
| Tail sum formula | $\mathbb{E}[Z]=\sum_{k=0}^\infty \mathbb{P}[Z>k]$ | Nonneg integer r.v.; avoids direct series computation |
| Continuous tail sum | $\mathbb{E}[T]=\int_0^\infty \mathbb{P}[T>t]\,\mathrm{d}t$ | Nonneg continuous r.v.; especially Exponential |
| Convolution | $f_Z(z)=\int f_X(z-\xi)f_Y(\xi)\,\mathrm{d}\xi$ | PDF of sum of independent continuous r.v. |
