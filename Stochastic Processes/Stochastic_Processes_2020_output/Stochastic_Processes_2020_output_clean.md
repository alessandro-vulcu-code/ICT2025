Stochastic Processes

PROF. Michele Zorzi

UNIVERSITY OF PADOVA

WRITTEN BY: Francesco Manzali, Andrea Nicolai

ACADEMIC YEAR 2019/20

Compiled on August 14, 2021


Contents

1  Probability and Statistics  6
1.1  Introduction  6
1.2  Stochastic Processes  6
1.3  Quick Review of Probability Theory  7
1.3.1  Random variables  8
1.3.2  Moments and Expected Values  9
1.3.3  Characteristic Functions  11
1.3.4  Probability generating function  12
1.4  Discrete Distributions  15
1.4.1  Bernoulli Distribution  15
1.4.2  Binomial Distribution  15
1.4.3  Geometric Distribution  16
1.4.4  Poisson Distribution  17
1.5  Continuous Distributions  18
1.5.1  Normal distribution  18
1.5.2  Exponential distribution  18
1.5.3  Uniform distribution  20
1.5.4  Gamma distribution  20
1.6  Conditional probabilities  21
1.6.1  Discrete distributions  21
1.6.2  Distribution of a Random Sum  24
1.6.3  Continuous  26

2  Markov Chains  27
2.1  Models  31
2.1.1  Discrete Queueing  31
2.2  Poisson Process  32
2.3  M/G/1 Queue  34
2.4  G/M/1 queue  36
2.5  Data transmission protocols  38
2.6  First step analysis  42
2.7  General Absorbing Markov Chain  46
2.8  Two-State Markov Chain  47
2.8.1  Markov Chains Defined by Independent r.v.  49


2.8.2 One-Dimensional Random Walks 50
2.8.3 Success Runs 54
2.8.4 First Passage Times 56

2.9 Alternative First Step Analysis 60

2.9.1 A matrix approach for average fpt 64

## 3 Long Run Behaviour of Markov Chains 66

3.1 Regular Markov Chains 66

3.1.1 Interpretation of the Limiting Distribution 68

3.2 Non regular Markov chains 69
3.3 Classification of States 70

3.3.1 Periodicity 72
3.3.2 Recurrence 74
3.3.3 Fubini's theorem 78

3.4 Basic Limit Theorem of Markov Chains 80

3.4.1 Periodic generalization 95

3.5 Reducible Markov chains 96

3.5.1 Another behaviour of infinite Markov chains 99

3.6 Absorption probabilities 102
3.7 Transient states 108

## 4 Poisson Processes 126

4.1 The Poisson Distribution 126
4.2 The Poisson Process 127
4.3 The Law of Rare Events 129
4.4 Properties of Poisson Processes 131
4.5 Other distributions 133

4.5.1 M/G/∞ queue 140
4.5.2 Shot Noise process 143

4.6 Binomial theorem 146
4.7 P.A.S.T.A. property 158

## 5 Renewal Phenomena 174

5.1 Renewal processes 174
5.2 Examples of Renewal Processes 178
5.3 The Poisson Process 180

5.3.1 The sampling paradox 182

5.4 Long run Behaviour 184
5.5 The Renewal Argument 189
5.6 The Elementary Renewal Theorem 193

5.6.1 The Basic Renewal Theorem 195
5.6.2 Delayed Renewal Processes 199
5.6.3 Alternating Renewal Process 200
5.6.4 Proof of basic limit theorem for M.C. 202

5.7 Renewal Reward Processes 204
5.7.1 Regenerative processes 206

5.8 Semi-Markov Processes 208

5.8.1 Some clarifications on Regenerative and Semi-Markov Processes 210


5.8.2 Semi-Markov process probabilities 211

## 6 Analysis of the GoBackN Protocol 227

6.0.1 Markov packet errors - Error free feedback 229
6.0.2 Bidirectional Markov packet errors - 4 states model 231
6.0.3 Bidirectional Markov packet errors - 3 states model 233
6.0.4 Bidirectional Markov packet errors - 2 states model 235

6.1 Counting processes and their statistics 237

6.1.1 Transform methods for recursive equations 240
6.1.2 Generalization 243
6.1.3 GoBackN protocol - Transform approach 246
6.1.4 GoBackN protocol - Generalization 248


# Introduction

Francesco Manzali, 20/02/2019


# Chapter 1 Probability and Statistics

### 1.1 Introduction

Modeling a natural phenomenon consists of linking its elements to *abstractions* in a *logical system* in order to deduce its properties or behaviour. For example, to compute the distance between two cities, we think of them as *geometrical points* of no dimension, and then use spherical geometry to determine the length of the great-circle connecting them.

A model is said to be deterministic if it predicts a single outcome from a given set of circumstances. On the other hand, a stochastic model predicts a set of possible outcomes weighted by their *plausibility* - or *probabilities*.

In general, there is no thing as a best model for any given phenomenon. What to use in what circumstance is an arbitrary choice, directed by seeking the most *usefulness* for a specific task of interest. A useful model is one that reflect all aspects of the phenomenon under study that are relevant to the question at hand, and that allow us to make calculations and predictions.

### 1.2 Stochastic Processes

A stochastic process is a family of random variables $X_{t}$, where $t$ is a parameter running over a suitable index set $T$. We could interpret it as a “stochastic function”, that maps an independent variable $t\in T$ to a random outcome $X(t)\in S$ - so that its graph *changes* every time we run the experiment.

$T$ may be a discrete set - for example $T=\mathbb{N}$ and $X(n)$ being the outcome of the $n$-th dice toss - or a continuos set - for example $T=[0,\infty)$ and $X(t)=$ temperature at time $t$ at a weather station.

$T$ does not need to be a *time* or *iteration number*. For example, we could model an image as a stochastic process, with $\boldsymbol{t}=(t_{1},t_{2})$ being the coordinates of a pixel (so, more like a *spatial* index). However, in this course we will limit ourselves to the $d=1$ case.

The possible values of $X(t)$ lie in a space $S$ denoted as the state space. For *


example, for a temperature we have $S=[0,\infty)$, while for a dice toss $S=\{1,2,3,4,5,6\}$.

A stochastic process with discrete index and discrete state space is called a chain.

To describe a stochastic process, we may start by specifying the statistics of each random variable $X_{t}$ - for example their distribution. If all $X_{t}$ distribute the same, the process is said to be stationary.

In the general case, however, $X_{t}$ and $X_{t^{\prime}}$ at different times $t\neq t^{\prime}$ may be correlated, meaning that the distribution of the latter depends on the outcome of the former. So, a full description of a stochastic process necessarily involves knowing the joint distribution of any set $\{X_{t}\colon t\in\bar{T}\}$ for any subset $\bar{T}\subseteq T$. This is clearly a huge amount of information, especially if $T$ is continuous. Fortunately, in many cases, stochastic processes possess some special properties that allow to describe them fully with only a few parameters.

### 1.3 Quick Review of Probability Theory

Recall the main concepts of probability theory:

- Sample space: set of all possible outcomes of an experiment, usually denoted with $\Omega$
- Event: any subset of $E\subseteq\Omega$
- Probability: a measure of events, i.e. a way to associate any event $E$ to a real positive number $\mathbb{P}[E]\in[0,1]$. We have $\mathbb{P}[\Omega]=1$ and $\mathbb{P}[\varnothing]=0$.

If $A$ and $B$ are events, their union $A\cup B$ is the event representing the realization of either $A$, $B$ or both. To measure its size (probability) we need to pay attention not to count two times the intersection of $A$ and $B$, and so:

$$
\mathbb{P}[A\cup B]=\mathbb{P}[A]+\mathbb{P}[B]-\mathbb{P}[A\cap B]
$$

Consider a disjoint partition $\{A_{i}\}$ of the sample space $\Omega$:

$$
\bigcup_{i}A_{i}=\Omega;\qquad\mathbb{P}[\Omega]=1;\qquad A_{i}\cap A_{j}=\varnothing\quad\forall i\neq j
$$

We can rewrite the probability of any event $B$ as the sum of its intersections with the partition elements $A_{i}$, leading to the law of total probability:

$$
\mathbb{P}[B]=\sum_{i}\mathbb{P}[B\cap A_{i}]
$$

Two events are said to be independent if and only if:

$$
\mathbb{P}[A\cap B]=\mathbb{P}[A]\mathbb{P}[B]
$$


Generalizing, $n$ events are independent if and only if:

$$
\mathbb{P}\left[\bigcap_{i}^{n}A_{i}\right]=\prod_{i}^{n}\mathbb{P}[A_{i}]
$$

#### 1.3.1 Random variables

A random variable is a “variable that takes on its values by chance”. It acts as a “placeholder” for the outcome of an experiment that may result in a range of possible values. For example, we may denote with $X$ the act of tossing a dice. After doing the experiment, we obtain, for example, the outcome 4, and we then say that $X$ “assumes” the value of 4 in this “realization” of the experiment.

By convention, we denote random variables with capital letters ($X$, $Y$, $Z$), and real numbers with lowercase letters ($x$, $y$, $z$). As an event is just a set of outcomes, we can specify it as a subset of the values that a random variable $X$ may assume. For example $\{X\leq x\}$ is the event that the random variable $X$ assumes a value that is less than or equal to the real number $x$. The measure of that set is its probability, denoted with $\mathbb{P}[\{X\leq x\}]$. In this case it is a function of the real number $x$.

We define the (cumulative) distribution function of the random variable $X$ as the quantity:

$$
F_{X}(x)=\mathbb{P}[\{X\leq x\}]\qquad F_{X}\colon\mathbb{R}\to[0,1]
$$

Clearly, $F(-\infty)=0$, $F(\infty)=1$ and it is non-decreasing: if we rise the value of $x$ we are either including new possible outcomes in the event, or leaving it the same, and so its size (probability) cannot decrease. It can also be shown that $F_{X}(x)$ is right-continuous, meaning that:

$$
\lim_{x\to c^{+}}F_{X}(x)=F_{X}(c)\qquad\forall c\in\mathbb{R}
$$

Suppose that $X$ is a discrete random variable, meaning that it “assumes” values in a discrete set $X\in\{x_{n}\}_{n\in T}$. Then $F_{X}(x)$ is a “step function”, that is constant in the intervals $[x_{i-1},x_{i})$ and makes jumps of size $\mathbb{P}[X=x_{i}]$ at $x=x_{i}$, as can be seen in fig. 1.1a.
If $\mathbb{P}[X=x]=0$ $\forall x$, then $F_{X}(x)$ does not make any discontinuous jump, and its graph is continuous (fig. 1.1b).

If $F_{X}(x)$ is differentiable, we call its derivative the probability density function (pdf):

$$
f_{X}(x)\equiv\frac{\mathrm{d}F_{X}(x)}{\mathrm{d}x}
$$

Then, from the fundamental theorem of calculus, we have:

$$
F_{X}(x)=\int_{-\infty}^{x}f(\xi)\,\mathrm{d}\xi\,;\qquad F(b)-F(a)=\mathbb{P}[a<X\leq b]=\int_{a}^{b}f(\xi)\,\mathrm{d}\xi
$$


![[Stochastic_Processes_2020_p9_img1.jpeg]]
(a) - CDF for a discrete random variable

![[Stochastic_Processes_2020_p9_img2.jpeg]]
(b) - CDF for a continuous random variable
Figure (1.1) - Examples of Cumulative Probability Distributions (CDF)

# 1.3.2 Moments and Expected Values

Moments are a way to summarize the shape of a distribution with numbers.

For a discrete random variable  $X$ , the  $m$ -th moment is defined by:


$$
\mathbb {E} [ X ^ {m} ] = \sum_ {i} x _ {i} ^ {m} \mathbb {P} [ X = x _ {i} ]
$$

where the sum is over all possible values that  $X$  can assume. In the continuous case, we substitute the sum with an integral:

$$
\mathbb {E} [ X ^ {m} ] = \int_ {- \infty} ^ {+ \infty} x ^ {m} f (x) \mathrm {d} x
$$

The first moment  $\mathbb{E}[x]$  is also called the mean.

We define the  $m$ -th central moment as the  $m$ -th moment of the random variable  $X$  obtained after subtracting its mean:


$$
\mathbb {E} [ (X - \mathbb {E} [ X ]) ^ {m} ]
$$

The second central moment is also called the variance of  $X$ :


$$
\operatorname {V a r} [ X ] = \mathbb {E} [ (X - \mathbb {E} [ X ]) ^ {2} ]
$$

The expected value of a function  $g(x)$  is defined as:


$$
\mathbb {E} [ g (x) ] = \sum_ {i} \mathbb {P} [ X = x _ {i} ] g \left(x _ {i}\right) \tag {1.1}
$$

in the discrete case, and as:

$$
\mathbb {E} [ g (x) ] = \int_ {\mathbb {R}} g (x) f (x) \mathrm {d} x \tag {1.2}
$$

in the continuous case.

We can unify both definitions by writing:


$$
\mathbb {E} [ g (x) ] = \int_ {\mathbb {R}} g (x) \mathrm {d} F (x) \tag {1.3}
$$


The measure $\mathrm{d}F(x)$ has a rigorous mathematical meaning (as a Lebesgue-Stieltjes integral) - but we will simply interpret (1.3) as equivalent to either (1.1) or (1.2) depending on the nature of the random variable $X$ at hand.

### Many variables

We can generalize everything to multiple dimensions. For example, given a pair $(X,Y)$ of random variables, their joint (cumulative) distribution function is defined as:

$$
F_{XY}(x,y)=F(x,y)=\mathbb{P}[X\leq x\text{ and }Y\leq y]
$$

Two random variables $X$ and $Y$ are said to be independent if their joint distribution function factorizes everywhere:

$$
X,Y\text{ are independent}\Leftrightarrow F(x,y)=F_{X}(x)F_{Y}(Y)\quad\forall x,y
$$

The same happens with their pdfs.

A related concept is that of correlation. Specifically, $X$ and $Y$ are said to be uncorrelated if the expectation of their product (after removing the mean) is null:

$$
\mathbb{E}[(X-\mu_{X})(Y-\mu_{Y})]=0\qquad\mu_{X}=\mathbb{E}[X],\,\mu_{Y}=\mathbb{E}[Y]
$$

We note that independence implies uncorrelation, but the converse is not true. In fact, by linearity of the expected value we can expand (1.5) to:

$$
\mathbb{E}[(X-\mu_{X})(Y-\mu_{Y})]=\mathbb{E}[XY]-\mu_{X}\underbrace{\mathbb{E}[Y]}_{\mu_{Y}}-\mu_{Y}\underbrace{\mathbb{E}[X]}_{\mu_{X}}+\mu_{X}\mu_{Y}
$$

and then use the independence property (1.4) to factorize the expectation $\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]=\mu_{X}\mu_{Y}$, so that:

$$
=\mu_{X}\mu_{Y}-\mu_{X}\mu_{Y}-\mu_{Y}\mu_{X}+\mu_{X}\mu_{Y}=0
$$

### Sum of variables

Consider the sum $Z=X+Y$ of two random variables $X$ and $Y$. Then:

$$
F_{Z}(z)=\mathbb{P}[Z\leq z] =\mathbb{P}[X+Y\leq z]\underset{(a)}{=}\mathbb{E}_{Y}[P[X+Y\leq z|Y]]=
=\mathbb{E}_{Y}[\mathbb{P}[X\leq z-Y|Y]]\underset{(b)}{=}\mathbb{E}_{Y}[F_{X}(z-Y)]=
\underset{(1.3)}{=}\int_{\mathbb{R}}F_{X}(z-\xi)\,\mathrm{d}F_{Y}(\xi)
$$

where in (a) we are taking the average over all conditional probabilities (which is just an application of the law of total probability), and the in (b) we recognize the distribution function of $X$, evaluated at $z-Y$.


Note that nothing changes if we exchange the roles of $X$ and $Y$, and so:

$$
F_{Z}(z)=\int_{\mathbb{R}}F_{Y}(z-\eta)\,\mathrm{d}F_{X}\left(\eta\right)
$$

This final operation is a convolution. We can see it explicitly if we suppose that $X$ and $Y$ have pdfs, so that:

$$
F_{Z}(z)=\int_{\mathbb{R}}F_{X}(z-\xi)
$$

Then we can take the derivative:

$$
f_{Z}(z) =\frac{\mathrm{d}F_{z}(z)}{\mathrm{d}z}=\int_{\mathbb{R}}\frac{\mathrm{d}}{\mathrm{d}z}F_{X}(z-\xi)\,\mathrm{d}F_{Y}(\xi)=\int_{\mathbb{R}}f_{X}(z-\xi)\,\mathrm{d}F_{Y}(\xi)=
\mathop{\equiv}_{(1.2)}\int_{\mathbb{R}}f_{X}(z-\xi)f_{Y}(\xi)
$$

In general:

$$
\mathbb{E}[X+Y] =\mathbb{E}[X]+\mathbb{E}[Y]\qquad\text{always}
$$
$$
\mathrm{Var}[X+Y] =\mathrm{Var}[X]+\mathrm{Var}[Y]\qquad\text{if are uncorrelated}
$$

(Prove it as exercise)

#### Conditional probabilities

Previously, we used the concept of a conditional probability, that we now define precisely.
For any events $A$ and $B$, the conditional probability of $A$ given $B$ is written $\mathbb{P}[A|B]$ and defined by:

$$
\mathbb{P}[A|B]=\frac{\mathbb{P}[A\cap B]}{\mathbb{P}[B]}\qquad\text{if }
$$

Then, substituting this definition in the law of total probability we arrive to:

$$
\mathbb{P}[A]=\sum_{i}\mathbb{P}[A|B_{i}]\mathbb{P}[B_{i}]
$$

where $B_{i}$ are a disjoint partition of the sample space $\mathbf{\Omega}$.

#### 1.3.3 Characteristic Functions

Let $X$ be a random variable with (cumulative) distribution function $F$. We define its characteristic function $\phi_{X}$ as follows:

$$
\phi_{X}(t)=\int_{\mathbb{R}}e^{it\lambda}\,\mathrm{d}F(\lambda)=\mathbb{E}[e^{itX}]
$$

If $X$ is a discrete random variable, (1.6) is equivalent to:


$$
\phi_{X}(t)=\sum_{k=0}^{+\infty}e^{it\lambda_{k}}\mathbb{P}[X=\lambda_{k}]
$$

where $\{\lambda_{k}\}_{k=0,\ldots,\infty}$ are the possible values of $X$.
On the other hand, if $X$ is a continuous random variable with pdf $p(x)$, (1.6) becomes:

$$
\phi_{X}(t)=\int_{\mathbb{R}}e^{it\lambda}p(\lambda)\,\mathrm{d}\lambda
$$

So the characteristic function is just the Fourier transform of the probability distribution of a random variable. As a Fourier transform can be inverted, there is a one-to-one relation between characteristic functions and distribution functions, meaning that given one we can uniquely compute the other. In particular, the equation which expresses the (cumulative) distribution function in terms of the respective characteristic function is known as Levy’s inversion formula.

Moreover, characteristic functions have two important features:

- If $X_{1},\ldots,X_{n}$ are independent random variables, the characteristic function of their sum is the product of their individual characteristic functions. In fact, by changing random variables it is possibly to show that the pdf for a sum of independent variables is the convolution of their individual pdfs, and the Fourier transform of a convolution is the product of Fourier transforms of the convolved arguments (by the convolution theorem).
- It is possible to compute the moments of a random variable $X$ (if they exist) by differentiating the characteristic function and evaluating it at $0$:

$$
\mathbb{E}[X^{k}]=\frac{1}{i^{k}}\phi^{(k)}(0)
$$

Let’s see this for the first two moments:

$$
\phi^{\prime}(t) =\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[e^{itX}]=\mathbb{E}\left[\frac{\mathrm{d}e^{itX}}{\mathrm{d}t}\right]=\mathbb{E}[iXe^{itX}]\Rightarrow\phi^{\prime}(0)=\mathbb{E}[iX]=i\mathbb{E}[X]
\phi^{\prime\prime}(t) =\mathbb{E}[iXiXe^{itX}]\Rightarrow\phi^{\prime\prime}(0)=i^{2}\mathbb{E}[X^{2}]
$$

(We can bring the derivative inside the expected value because of linearity).

#### 1.3.4 Probability generating function

For a discrete random variable whose only possible values are the nonnegative integers we can define its probability generating function:

$$
g(s)=\sum_{k=0}^{\infty}\underbrace{\mathbb{P}[X=k]}_{p_{k}}s^{k}=\mathbb{E}[s^{X}]\qquad s\in\mathbb{C}
$$


Since $p_k \geq 0$ and $\sum_{k=0}^{\infty} p_k = 1$ (because they are probabilities), $g(s)$ converges inside $|s| \leq 1$, and is infinitely differentiable for $|s| < 1$.

Note that the probability generating function is closely related to the characteristic function of the same random variable $X$. In fact:

$$
\phi(t) = \mathbb{E}[e^{itX}] = \mathbb{E}[(e^{it})^X] = g(e^{it})
$$

In particular, this means that it has the same features of a characteristic function: we can use it to recover the cdf; the generating function of a sum of independent r.v. is the product of their individual generating function; we can differentiate it to compute (factorial) moments.

Explicitly:

$$
\mathbb{E}[X(X-1)\cdots(X-k)] = g^{(k+1)}(1) \tag{1.9}
$$

Let's see this for the first two moments.

$$
\begin{array}{l}
\frac{\mathrm{d}g(s)}{\mathrm{d}s} = \sum_{k=1}^{+\infty} k p_k s^{k-1} \Rightarrow \left. \frac{\mathrm{d}g(s)}{\mathrm{d}s} \right|_{s=1} = \sum_{k=1}^{+\infty} k p_k = \mathbb{E}[X] \\
g''(s) = \sum_{k=2}^{+\infty} k(k-1) p_k s^{k-2} \Rightarrow g''(1) = \sum_{k=2}^{+\infty} k(k-1) p_k = \mathbb{E}[X(X-1)]
\end{array}
$$


> [!example] Example 1 (Sum of a random number of random variables)
>
> Let $\{X_i\}_{i=1,\dots,N}$ be a set of independent and identically distributed r.v. (i.i.d. for short), which are discrete and non-negative integer-valued ($X_i \in \mathbb{N}$), with probability generating function $g(s)$. Let $N$ be another discrete r.v. with $N \in \mathbb{N}$ and generating function $g_N(s)$, which is independent of all the $\{X_i\}$. We want to find the statistics of the sum of the $N$ random variables:
>
> $$
> R = X_1 + \cdots + X_N
> $$
>
> Note that we cannot directly apply the "convolution property" of the generating function, i.e. write:
>
> $$
> g_R(s) = \mathbb{E}[s^R] = \prod_{i=1}^{N} g(s)
> $$
>
> because $N$ is a random variable, with no definite value.
>
> However, we can compute $\mathbb{E}[s^R]$ for a fixed value of $N$ - denoting the result as $\mathbb{E}[s^R|N]$ - and then average this result over all possible choices of $N$. This procedure is just an application of the law of total probability, and in this way we can use the convolution property for all the averaged terms:
>
> $$
> \begin{array}{l}
> g_R(s) = \mathbb{E}[s^R] = \mathbb{E}[s^{X_1 + \cdots + X_N}] = \\
> = \mathbb{E}\{\mathbb{E}[s^{X_1 + \cdots + X_N}|N]\} =
> \end{array}
> $$
>
>
> Expanding the outer average:
>
> $$
> = \sum_{n=0}^{+\infty} \mathbb{E}[s^{X_1 + \dots + X_n} | N = n] \mathbb{P}[N = n] =
> $$
>
> Since $\{X_i\}$ and $N$ are independent, $\mathbb{E}[s^{X_1 + \dots + X_n} | N = n] = \mathbb{E}[s^{X_1 + \dots + X_n}]$, and so:
>
> $$
> = \sum_{n=0}^{+\infty} \overline{\mathbb{E}[s^{X_1 + \dots + X_n}]} \mathbb{P}[N = n] =
> $$
>
> Finally we can apply the convolution property:
>
> $$
> = \sum_{n=0}^{+\infty} g(s)^n \mathbb{P}[N = n] =
> $$
>
> And we recognize the expression for the generating function of $N$:
>
> $$
> = \mathbb{E}[g(s)^N] = g_N[g(s)]
> $$
>
> We can now compute mean and variance by applying (1.9):
>
> $$
> \mathbb{E}[R] = \left. \frac{\mathrm{d} g_R(s)}{\mathrm{d} s} \right|_{s=1} = g_N'[g(s)] \cdot g'(s) \Big|_{s=1} = g_N'[g(1)] \cdot \mathbb{E}[X]
> $$
>
> And note that:
>
> $$
> g(1) = \sum_{k=0}^{+\infty} \mathbb{P}[X = k] = 1
> $$
>
> by normalization. So:
>
> $$
> \mathbb{E}[R] = g_N'(1) \cdot \mathbb{E}[X] = \mathbb{E}[N] \cdot \mathbb{E}[X]
> $$
>
> Intuitively, if $N$ were fixed, the mean of $R$ would be exactly $N$ times the mean of each summed variable. Here $N$ is not fixed, and so we use its mean instead.
>
> For the variance, we first need the second (factorial) moment, and so we derive once again:
>
> $$
> g_R''(s) = g_N''[g(s)] (g'(s))^2 + g_N'(g(s)) g''(s)
> $$
>
> And then we evaluate at $s = 1$:
>
> $$
> \begin{aligned}
> g_R''(1) &= g_N''[1] \mathbb{E}[X]^2 + g_N'(1) \mathbb{E}[X^2 - X] = \\
> &= \mathbb{E}[N^2 - N] \cdot \mathbb{E}[X]^2 + \mathbb{E}[N] \cdot \mathbb{E}[X^2 - X] = \\
> &= \mathbb{E}[N^2] \mathbb{E}[X]^2 - \mathbb{E}[N] \mathbb{E}[X]^2 + \mathbb{E}[N] \mathbb{E}[X^2] - \mathbb{E}[N] \mathbb{E}[X] = \\
> &= \mathbb{E}[N^2] \mathbb{E}[X]^2 + \mathbb{E}[N] \operatorname{Var}(X) - \mathbb{E}[N] \mathbb{E}[X]
> \end{aligned}
> $$
>
> And finally:
>
> $$
> \begin{aligned}
> \operatorname{Var}(R) &= \mathbb{E}[R^2] - \mathbb{E}[R]^2 = g_R''(1) + g_R'(1) - (g_R'(1))^2 = \\
> &= \mathbb{E}[N^2] \mathbb{E}[X]^2 + \mathbb{E}[N] \operatorname{Var}(X) - \underbrace{\mathbb{E}[N] \mathbb{E}[X]} + \underbrace{\mathbb{E}[N] \mathbb{E}[X]}_{\text{var}} \\
> &\quad - \mathbb{E}[N]^2 \mathbb{E}[X]^2 =
> \end{aligned}
> =\mathbb{E}[N]\,\mathrm{Var}(X)+\mathbb{E}[X]^{2}\,\mathrm{Var}(N)
> $$
>
> If $N$ were fixed, the variance of $R$ would just be the sum of the variances of the $X_{i}$, i.e. $N$ times $\mathrm{Var}(X)$. So, as $N$ is not fixed, we would expect to see $\mathbb{E}[N]\,\mathrm{Var}(X)$ - which is indeed the first term. However, there is also $\mathbb{E}[X]^{2}\,\mathrm{Var}(N)$. Intuitively, this is because the random number of elements in the sum introduces “more randomness”, making the distribution more “spread out”.

### 1.4 Discrete Distributions

We now discuss some important examples of probability distributions, starting from the discrete case.

#### 1.4.1 Bernoulli Distribution

Consider a random variable $X$ with only two possible values - 0 and 1. The resulting probability mass function is the Bernoulli distribution:

$$
\mathbb{P}(X=x)=\begin{cases}p&x=1\\
1-p&x=0\end{cases}
$$

It can be shown that:

$$
\mathbb{E}[X] =p
\mathrm{Var}(X) =p(1-p)
$$

Bernoulli r.v. can be constructed as indicators of events. For a generic event $A$, its indicator r.v. denoted with $\mathbb{1}(A)$ is defined as:

$$
\mathbb{1}(A)\equiv\mathbb{1}_{A}=\begin{cases}1&\text{if $A$ occurs}\\
0&\text{if $A$ does not occur}\end{cases}
$$

#### 1.4.2 Binomial Distribution

Consider $n$ independents events $A_{1},\ldots,A_{n}$, all having the same probability $p=\mathbb{P}[A_{i}]$ of occurrence. Let $Y$ be the random variable which counts the total number of events among $A_{1},\ldots,A_{n}$ that occur. In other words, $Y$ counts the number of “successes” in $n$ independent trials, if each of them has a constant probability $p$ of success. The distribution of $Y$ is called the binomial distribution, and is given by:

$$
p_{Y}(k)\equiv\mathbb{P}(Y=k)=\frac{n!}{k!(n-k)!}p^{k}(1-p)^{n-k}\quad\forall k=0,1,\ldots,n
$$


Note that we can rewrite $Y$ as the sum of $n$ Bernoulli r.v.:

$$
Y=\mathbb{1}(A_{1})+\cdots+\mathbb{1}(A_{n})
$$

This allows to quickly compute mean and variance:

$$
\mathbb{E}[Y] =\mathbb{E}[\mathbb{1}(A_{1})]+\cdots+\mathbb{E}[\mathbb{1}(A_{n})]=np
\mathrm{Var}(Y) =\mathrm{Var}[\mathbb{1}(A_{1})]+\cdots+\mathrm{Var}[\mathbb{1}(A_{n})]=np(1-p)
$$

#### 1.4.3 Geometric Distribution

Consider a number of i.i.d. events (e.g. a sequence of repeated experiments) $\{A_{i}\}_{i=1,\ldots,\infty}$. If $A_{i}$ occurs, we have a success, while if it does not occur, we say it is a failure. Let $Z$ be the number of failures before the first success in the sequence $A_{1},\ldots,A_{n}$. The distribution of such $Z$ is called geometric distribution.

Alternatively, we can consider the number $Z^{\prime}$ of attemps needed to get exactly one success. In this case, we are counting also the success at the end, and so $Z^{\prime}=Z+1$. Sometimes this is the case used to define the geometric distribution. Clearly the final result is the same - the only difference is of interpretation, and will be clarified in the context.

The probability mass function of $Z$ can be directly found as:

$$
p_{z}(k)=\mathbb{P}[Z=k]=p(1-p)^{k}\qquad k\in\mathbb{N}
$$

In fact, as all events are independent, we can get the probability of a sequence by just multiplying the probabilities of each event happening or not. In this case the first $k$ events do not happen (and so we have a $(1-p)^{k}$ term), but the $k+1$-th does happen (and so we need to multiply by $p$).

Let’s compute the mean and variance of $Z$:

$$
\mathbb{E}[Z]=\sum_{k=0}^{+\infty}kp_{k}=\sum_{k=0}^{+\infty}kp(1-p)^{k}=p(1-p)\sum_{k=1}^{+\infty}k(1-p)^{k-1}
$$

Then we rewrite the sum as the derivative of a geometric series:

$$
\sum_{k=1}^{+\infty}ka^{k-1}=\frac{\mathrm{d}}{\mathrm{d}a}\left(\sum_{k=0}^{+\infty}a^{k}\right)=\frac{\mathrm{d}}{\mathrm{d}a}\frac{1}{1-a}=\frac{1}{(1-a)^{2}}\qquad a=1-p<1
$$

Substituting back:

$$
\mathbb{E}[Z]=\frac{p(1-p)}{(1-(1-p))^{2}}=\frac{p(1-p)}{p^{2}}=\frac{1-p}{p}
$$

A similar procedure leads to the variance:

$$
\mathrm{Var}(Z)=\frac{1-p}{p^{2}}
$$


Another way to compute $\mathbb{E}[Z]$, which will be useful also for later problems, is the following.

Let $Z$ be a non-negative integer-valued random variable. Then its expectation is equal to the sum of its *tail distribution*:

$$
\mathbb{E}[Z]=\sum_{k=0}^{+\infty}\mathbb{P}[Z>k]=\sum_{k=1}^{+\infty}\mathbb{P}[Z\geq k]
$$

In our specific case, $\mathbb{P}[Z\geq k]=(1-p)^{k}$ - as it is the probability of having *at least* $k$ failures. Then:

$$
\mathbb{E}[Z]=\sum_{k=1}^{+\infty}(1-p)^{k}=\sum_{(a)}^{+\infty}(1-p)^{k+1}=(1-p)\sum_{k=0}^{+\infty}(1-p)^{k}=
$$

where in (a) we *shifted* the index of summation. Note that the final expression is just a geometric series, and so:

$$
=(1-p)\cdot\frac{1}{1-(1-p)}=\frac{1-p}{p}
$$

To understand why (1.10) is true, consider the following. We can rewrite the expectation of the r.v. $Z$ as follows:

$$
\mathbb{E}[Z]=\sum_{k=0}^{+\infty}kp_{k}=0\cdot p_{0}+1\cdot p_{1}+2\cdot p_{2}+\ldots
$$

We then write the multiplications as repeated sums:

$$
= \!\!\!\begin{array}[]{c}p_{1}\cr p_{2}\cr p_{3}\cr\end{array}+ \!\!\!\begin{array}[]{c}p_{2}\cr p_{3}\cr\end{array}+
= \!\!\!\begin{array}[]{c}p_{3}\cr p_{3}\cr\end{array}+
\vdots \vdots \vdots
$$

Note that the first column is the sum of all $p_{k}$ with $k\geq 1$, and so is equal to $\mathbb{P}[Z>0]$. The second column is $\mathbb{P}[Z>1]$, and so on:

$$
=\sum_{k=0}^{+\infty}\mathbb{P}[Z>k]
$$

which proves (1.10).

#### 1.4.4 Poisson Distribution

The Poisson distribution with parameter $\lambda>0$ has the probability mass function:

$$
p(k)=\frac{\lambda^{k}e^{-\lambda}}{k!}\qquad\forall k=0,1,\ldots
$$


Using the series expansion for the exponential:

$$
e^{\lambda}=1+\lambda+\frac{\lambda^{2}}{2!}+\frac{\lambda^{3}}{3!}+\ldots
$$

we can see that (1.11) is correctly normalized:

$$
\sum_{k=0}^{+\infty}p_{k}=1
$$

We can reuse (1.12) to compute mean and variance:

$$
\mathbb{E}[X]=\sum_{k=0}^{+\infty}k\frac{\lambda^{k}e^{-\lambda}}{k!}=\lambda e^{-\lambda}\underbrace{\sum_{k=1}^{+\infty}\frac{\lambda^{k-1}}{(k-1)!}}_{e^{\lambda}}=\lambda
\mathbb{E}[X(X-1)]=\sum_{k=0}^{+\infty}k(k-1)p(k)=\sum_{k=2}^{+\infty}k(k-1)\frac{\lambda^{k}e^{-\lambda}}{k!}=\lambda^{2}e^{-\lambda}\sum_{k=2}^{+\infty}\frac{\lambda^{k-2}}{(k-2)!}=\lambda^{2}
\mathbb{E}[X^{2}]=\mathbb{E}[X(X-1)]+\mathbb{E}[X]=\lambda^{2}+\lambda\Rightarrow\mathrm{Var}[X]=\mathbb{E}[X^{2}]-\mathbb{E}[X]^{2}=\lambda
$$

It can be shown that a binomial distribution with parameters $n$ and $p$ converges to the Poisson with parameter $\lambda$ if $n\to\infty$ and $p\to 0$ in such a way that $np=\lambda$ remains constant. In other words, the Poisson distribution emerges as the distribution of a large number of trials, each with very little probability of success. This is, in essence, the law of rare events.

### 1.5 Continuous Distributions

#### 1.5.1 Normal distribution

The normal distribution (or gaussian) with mean $\mu$ and variance $\sigma^{2}$ is defined as:

$$
\phi(x;\mu,\omega^{2})=\frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x-\mu)^{2}}{2\sigma^{2}}\right)
$$

We limit ourselves to this definition, as we will not use it often in this course.

#### 1.5.2 Exponential distribution

A non-negative random variable $T$ is said to have an exponential distribution with parameter $\lambda>0$ if its probability density function is:

$$
f_{T}(t)=\begin{cases}\lambda e^{-\lambda t}&t\geq 0\\
0&t<0\end{cases}
$$


The corresponding distribution function (CDF) is:

$$
F_{T}(t)=\begin{cases}1-e^{-\lambda t}&t\geq 0\\
0&t<0\end{cases}
$$

Mean and variance are:

$$
\mathbb{E}[T]=\frac{1}{\lambda};\qquad\mathrm{Var}[T]=\frac{1}{\lambda^{2}}
$$

In general:

$$
\mathbb{E}[T^{k}]=\frac{1}{\lambda^{k}}
$$

We can show that by explicit computation:

$$
\mathbb{E}[T]=\int_{0}^{+\infty}t\lambda e^{-\lambda t}\,\mathrm{d}t
$$

which can be solved by integrating by parts. Alternatively, we can use the *continuous* analogue of (1.10):

$$
\mathbb{E}[T]=\int_{0}^{+\infty}\mathbb{P}[T>t]\,\mathrm{d}t=\int_{0}^{+\infty}e^{-\lambda t}\,\mathrm{d}t=\frac{e^{-\lambda t}}{-\lambda}\Big{|}_{0}^{+\infty}=\frac{1}{\lambda}
$$

which is much simpler.

The exponential distribution is often used to model *lifetimes* - for example the mean working time of a machine before it breaks, or the time elapsed before a particle decays.

In particular, the exponential distribution is memoryless - in the sense that conditional probabilities such as $\mathbb{P}[T>t^{\prime}|T>t]$ depend only on the *difference* $t-t^{\prime}$. For example, this means that if a particle is still “alive” at time $t$, the probability that it is still alive at a later time $t^{\prime}$ does not depend on the entire *history* of the particle, but only on the elapsed time $t^{\prime}-t$.

To see this explicitly, suppose that a particle’s survival time follows the exponential distribution, and at time $t$ the particle still exists. Let $t^{\prime}=t+x$, with $x>0$, be a *later time*. The probability that the particle still exists at $t^{\prime}$ is given by:

$$
\mathbb{P}[T>t^{\prime}=t+x|T>t]=\frac{\mathbb{P}[T>t+x,T>t]}{\mathbb{P}[T>t]}=
$$

Where we applied the product rule for probabilities. As $x>0$, if the particle survives up to $t^{\prime}$, then it definitely has survived up to $t<t^{\prime}$, and so the joint probability at the numerator reduces to:

$$
=\frac{\mathbb{P}[T>t+x]}{\mathbb{P}[T>t]}=\frac{e^{-\lambda(t+x)}}{e^{-\lambda t}}=e^{-\lambda x}
$$

where $x=t^{\prime}-t$.


In other words, the survival statistics at any time are the same. A particle that is still alive at time $t$ behaves the same as if it was just “born” - it has “forgot” all of its past.

In physics, many processes can be modelled as if they were memoryless. For example, in statistical mechanics, the chaotic interactions with a thermal bath quickly destroy any information about the starting state - meaning that the system has “little memory”, and so its statistics can be well approximated by using the exponential distribution.

#### 1.5.3 Uniform distribution

A random variable $\mathcal{U}$ is uniformly distributed over the interval $[a,b]$, with $a<b$, if it has the probability density function:

$$
f_{U}(u)=\begin{cases}\frac{1}{b-a}&a\leq u\leq b\\
0&\text{elsewhere}\end{cases}
$$

The corresponding CDF is:

$$
F_{U}(x)=\begin{cases}0&u\leq a\\
\frac{x-a}{b-a}&a<x\leq b\\
1&x>b\end{cases}
$$

And its mean and variance are:

$$
\mathbb{E}[U]=\int_{a}^{b}\frac{u}{b-a}\,\mathrm{d}u=\frac{b-a}{2}\qquad\operatorname{Var}(U)=\frac{(b-a)^{2}}{12}
$$

#### 1.5.4 Gamma distribution

The gamma distribution with parameters $\alpha>0$ and $\lambda>0$ has probability density function:

$$
f(x)=\frac{\lambda}{\Gamma(\alpha)}(\lambda x)^{\alpha-1}e^{-\lambda x}\qquad x>0
$$

Given an integer number $\alpha$ of independent exponentially distributed random variables $Y_{1},\ldots,Y_{n}$ having common parameter $\lambda$ (i.i.d.), then their sum $X_{\alpha}=Y_{1}+\cdots+Y_{\alpha}$ has the gamma density. Its moments are:

$$
\mathbb{E}[X_{\alpha}]=\frac{\alpha}{\lambda}\qquad\operatorname{Var}[X_{\alpha}]=\frac{\alpha}{\lambda^{2}}
$$

And this formulas hold for $\alpha\in\mathbb{R}$.


### 1.6 Conditional probabilities

The probability of an event $A$ given the occurrence of another event $B$ is defined as:

$$
\mathbb{P}[A|B]=\frac{\mathbb{P}[A\cap B]}{\mathbb{P}[B]}\text{ if }\mathbb{P}[B]\neq 0
$$

Rearranging we obtain the product rule for probabilities:

$$
\mathbb{P}[A\cap B]=\mathbb{P}[A|B]\mathbb{P}[B]
$$

We can now state the theorem of total probability in its most common form. Let $B_{i}$ be a partition of the sample space $\Omega$, such that:

$$
\bigcup_{i}B_{i}=\Omega\qquad B_{i}\cap B_{j}=\varnothing\;\forall i\neq j
$$

Then:

$$
\mathbb{P}[A]=\sum_{i}\mathbb{P}[A\cap B_{i}]=\sum_{i}\mathbb{P}[A|B_{i}]\mathbb{P}[B_{i}]
$$

#### 1.6.1 Discrete distributions

Let $Y$ be a discrete random variable, and $X$ an arbitrary r.v. (discrete or continuous). We define the conditioned distribution of $X$ given $Y$ as follows:

$$
F_{X|Y}(X|Y)=\frac{\mathbb{P}[X\leq x,Y=y]}{\mathbb{P}[Y=y]}\text{ if }\mathbb{P}[Y=y]\neq 0
$$

$F_{X|Y}$ is a probability distribution in $x$ for all values of $y$, and just a function of $y$ if we fix the value of $x$ (not necessarily normalized, and so definitely not a distribution).

The joint (cumulative) distribution of $X$ and $Y$ is given by:

$$
\mathbb{P}[X\leq x,Y\leq y] =\sum_{\eta\leq y}\mathbb{P}[X\leq x,Y=\eta]=\sum_{\eta\leq y}F_{X|Y}(x|\eta)\mathbb{P}[Y=\eta]=
=\int_{\eta\leq y}F_{X|Y}(x|\eta)\,\mathrm{d}F_{Y}(\eta)
$$

The marginal probability is obtained by setting $y=+\infty$, making the occurring of $Y$ certain:

$$
\mathbb{P}[X\leq x]=\sum_{\eta=-\infty}^{+\infty}F_{X|Y}(x|\eta)\mathbb{P}[Y=\eta]=\mathbb{E}[\mathbb{P}[X\leq x|Y]]=\int_{\mathbb{R}}F_{X|Y}(x|\eta)\,\mathrm{d}F_{Y}(\eta)
$$

In general, we can compute the expected value of a function of $X$ as the average over the same quantity conditioned over $Y$:

$$
\mathbb{E}[g(X)]=\mathbb{E}[\mathbb{E}[g(X)|Y]]=\int_{\mathbb{R}}\mathbb{E}[g(X)|Y=\eta]\,\mathrm{d}F_{Y}(\eta)
$$


where the inner expectation is over the conditioned distribution:

$$
\mathbb {E} [ g (X) | Y = \eta ] = \int_ {\mathbb {R}} g (x) \mathrm {d} F _ {X | Y = \eta} (x) \tag {1.17}
$$

If $X$ is discrete, (1.17) becomes:

$$
\mathbb {E} [ g (X) | Y = \eta ] = \sum_ {x = - \infty} ^ {+ \infty} g (x) \mathbb {P} [ X = x | Y = \eta ]
$$

On the other hand, if $X$ is continuous, (1.17) can be written as:

$$
\mathbb {E} [ g (X) | Y = \eta ] = \int_ {\mathbb {R}} g (x) f _ {X | Y} (x | \eta) \mathrm {d} x
$$

**Example 2 (Composition of binomials):**

Let $X$ have a binomial distribution with parameter $p$ and $N$, where $N$ is again a r.v. with binomial distribution with parameters $q$ and $M$. What is the marginal distribution of $X$?

**Solution.** We know how $X$ is distributed given a fixed value of $N$:

$$
p _ {X | N} (k | n) = \binom {n} {k} p ^ {k} (1 - p) ^ {n - k} \qquad k = 0, 1, \ldots , n
$$

And that $N$ is distributed as:

$$
p _ {N} (n) = \binom {M} {n} q ^ {n} (1 - q) ^ {M - n} \qquad n = 0, 1, \ldots , M
$$

To compute the distribution of $X$ we apply the law of total probability:

$$
\mathbb {P} [ X = k ] = \sum_ {n = 0} ^ {M} p _ {X | N} (k | n) p _ {N} (n) =
$$

Note that if $k > n$, $p_{X|N}(k|n) = 0$, as it's not possible to obtain more successes than trials. This restricts the sum from $k$ to $M$. Then, expanding the distributions we get:

$$
= \sum_ {n = k} ^ {M} \frac {\varkappa !}{k ! (n - k) !} p ^ {k} (1 - p) ^ {n - k} \frac {M !}{\varkappa ! (M - n) !} q ^ {n} (1 - q) ^ {M - n} =
$$

We extract from the sum all terms that do not contain $n$:

$$
= \frac {M !}{k !} p ^ {k} (1 - q) ^ {M} \sum_ {n = k} ^ {M} \frac {1}{(n - k) ! (M - n) !} (1 - p) ^ {n - k} q ^ {n} (1 - q) ^ {- n} =
$$

The idea is to multiply and divide by a constant factor so that every exponent inside the sum is $n - k$:

$$
= \frac {M !}{k !} p ^ {k} (1 - q) ^ {M} \left(\frac {q}{1 - q}\right) ^ {k} \sum_ {n = k} ^ {M} \frac {1}{(n - k) ! (M - n) !} (1 - p) ^ {n - k} \left(\frac {q}{1 - q}\right) ^ {n - k}
$$


Then we change the index of summation so that it starts from $0$, defining $j = n - k$:

$$
= \frac {M !}{k !} p ^ {k} (1 - q) ^ {M} \left(\frac {q}{1 - q}\right) ^ {k} \sum_ {j = 0} ^ {M - k} \frac {1}{j ! (M - j - k) !} (1 - p) ^ {j} \left(\frac {q}{1 - q}\right) ^ {j} =
$$

Multiplying and dividing by $(M - k)!$ we can highlight a binomial coefficient:

$$
= \frac {M !}{k !} p ^ {k} \frac {(1 - q) ^ {M}}{(M - k) !} \left(\frac {q}{1 - q}\right) ^ {k} \sum_ {j = 0} ^ {M - k} \underbrace {\frac {(M - k) !}{j ! (M - k - j) !}} _ {\binom {M - k} {j}} (1 - p) ^ {j} \left(\frac {q}{1 - q}\right) ^ {j} \cdot 1 ^ {M - k - j}
$$

Note that the sum is a binomial sum, which is equal to the power of a binomial:

$$
\begin{array}{l}
= \frac {M !}{k !} p ^ {k} \frac {(1 - q) ^ {M}}{(M - k) !} \left(\frac {q}{1 - q}\right) ^ {k} \left(1 + \frac {q (1 - p)}{1 - q}\right) ^ {M - k} = \\
= \frac {M !}{k ! (M - k !)} (p q) ^ {k} (1 - q) ^ {M - k} \left[ 1 + \frac {q (1 - p)}{1 - q} \right] ^ {M - k} = \\
= \binom {M} {k} (p q) ^ {k} (1 - q) ^ {M - k} \left[ \frac {1 - q + q - p q}{1 - q} \right] ^ {M - k} = \\
= \binom {M} {k} (p q) ^ {k} (1 - p q) ^ {M - k} \\
\end{array}
$$

Meaning that the distribution of $X$ is again a binomial distribution, with parameters $M$ and $pq$.

This should be expected, as we defined $X$ as two binomial processes one right after the other. To see that, consider the following experiment. Suppose we have $M$ balls. For each of them we toss a dice, keeping the ball with probability $q$, and otherwise discarding it. At the end we will have $N$ balls. Note that the distribution of $N$ is binomial with parameters $M$ and $q$, by construction.

Then, we repeat the same experiment starting with the $N$ balls, keeping each of them with probability $p$. The final number of balls will be $X$ - which follows a binomial distribution with parameters $N$ and $p$.

Note that, equivalently, we can obtain $X$ from $M$ with a single pass, by keeping each ball with probability $pq$, which is equal to the probability of surviving both rounds of the former experiment. This proves that the statistic of $X$ is binomial with parameters $M$ and $pq$.


> [!question] Exercise 1.6.1 (Composition of binomial and Poisson)
>
> Suppose $X$ has a binomial distribution with parameters $p$ and $N$, where $N$ has a Poisson distribution with mean $\lambda$. What is the marginal distribution for $X$?
>
> Solution.

> [!question] Exercise 1.6.2 (Moments of random sums)
>
> Assume that $\xi_{k}$ and $N$ have finite moments:
>
> $$
> \mathbb{E}[\xi_{k}] = \mu; \quad \operatorname{Var}[\xi_{k}] = \sigma^{2}
> \mathbb{E}[N] = \nu; \quad \operatorname{Var}[N] = \tau^{2}
> $$
>
> Show, by using conditional distributions, that the mean and variance of the sum $X = \xi_{k} + \cdots + \xi_{N}$ are:
>
> $$
> \mathbb{E}[X] = \mu \nu; \qquad \operatorname{Var}[X] = \nu \sigma^{2} + \mu^{2} \tau^{2}
> $$
>
> which are the same results we obtained by using characteristic functions.
>
> Solution.

#### 1.6.2 Distribution of a Random Sum

Suppose that $\{\xi_i\}_{i=1,\dots,\infty}$ are continuous i.i.d. random variables having a probability density function $f(z)$. For $n \geq 1$, the probability density function for the fixed sum $\xi_1 + \dots + \xi_n$ is the $n$-fold convolution of the density $f(z)$, denoted by $f^{(n)}(z)$ and recursively defined by:

$$
f^{(1)}(z) = f(z)
$$

and:

$$
f^{(n)}(z) = \int_{\mathbb{R}} f^{(n-1)}(z - u) f(u) \, \mathrm{d}u \qquad \forall n > 1
$$

> [!example] Example 3 (Geometric sum of exponential r.v.)
>
> Consider a set of i.i.d. random variables $\xi_{i}$ with exponential distribution:
>
> $$
> f(z) = \begin{cases}
> \lambda e^{-\lambda z} & z \geq 0 \\
> 0 & z < 0
> \end{cases}
> $$
>
> We consider the sum $Z = \xi_1 + \dots + \xi_N$, where $N$ is a discrete random variable with geometric distribution:
>
> $$
> p_N(n) = \beta (1 - \beta)^{n-1} \quad \forall n \in \mathbb{N} \setminus \{0\} \tag{1.18}
> $$
>
>
> We already know that the distribution for the sum of a fixed number $n$ of exponential r.v. (i.e. the $n$-fold convolution of $f(z)$) is the Gamma density:
>
> $$
> f^{(n)}(z) = \begin{cases}
> \frac{\lambda^n}{(n-1)!} z^{n-1} e^{-\lambda z} & z \geq 0 \\
> 0 & z < 0
> \end{cases} \tag{1.19}
> $$
>
> So, to derive the pdf of $Z$ we apply the law of total probability, noting that $p_N(0) = 0$:
>
> $$
> \begin{aligned}
> f_X(z) &= \sum_{n=1}^{+\infty} f^{(n)}(z) p_N(n) = \\
> &= \sum_{\substack{(1.19) \\ (1.18)}}^{+\infty} \sum_{n=1}^{+\infty} \frac{\lambda^n}{(n-1)!} z^{n-1} e^{-\lambda z} \beta (1 - \beta)^{n-1} = \\
> \end{aligned}
> $$
>
> We bring out some factors so that all exponents in the sum are $n - 1$:
>
> $$
> = \lambda \beta e^{-\lambda z} \sum_{n=1}^{+\infty} \sum_{n=1}^{+\infty} \frac{[\lambda(1 - \beta)z]^{n-1}}{(n-1)!} =
> $$
>
> Shifting to 0 the index of summation we obtain the exponential series:
>
> $$
> \begin{aligned}
> &= \lambda \beta e^{-\lambda z} \sum_{n=0}^{+\infty} \frac{1}{n!} [\lambda(1 - \beta)z]^{n-1} = \\
> &= \lambda \beta e^{-\lambda z} e^{\lambda(1 - \beta)z} = \lambda \beta e^{-\lambda \beta z} \qquad z \geq 0
> \end{aligned}
> $$
>
> So $X$ has an exponential distribution with parameter $\lambda \beta$.
>
> Equivalently, we could do this with characteristic functions:
>
> $$
> \begin{aligned}
> g_N(s) &= \sum_{n=1}^{+\infty} \beta (1 - \beta)^{n-1} s^k = \frac{\beta s}{1 - (1 - \beta)s} \\
> \phi(t) &= \mathbb{E}[e^{it\xi}] = \int_0^{+\infty} e^{it\xi - \lambda\xi} \lambda \, d\xi = \frac{\lambda}{\lambda - it}
> \end{aligned}
> $$
>
> The characteristic function of the random sum is obtained by composition:
>
> $$
> \begin{aligned}
> g_N(\phi(t)) &= \frac{\beta \frac{\lambda}{\lambda - it}}{1 - (1 - \beta) \frac{\lambda}{\lambda - it}} = \frac{\beta \lambda}{\lambda - it - (\lambda - \beta) \lambda} = \\
> &= \frac{\beta \lambda}{\beta \lambda - it}
> \end{aligned}
> $$
>
> Comparing this result with $\phi(t)$ we see that they are characteristic functions of the same distribution, with the substitution $\lambda \leftrightarrow \beta \lambda$. So, the distribution of the random sum is, in fact, an exponential distribution with parameter $\beta \lambda$.

#### 1.6.3 Continuous

If $Y$ is continuous, then $P[Y=y]=0$ $\forall y$, and so we cannot use the previous definition for the conditioned distribution (1.16). So, we instead define the conditioned pdf:

$$
f_{X|Y}(x|y)=\frac{f_{X|Y}(x,y)}{f_{Y}(y)}\text{ if }f_{Y}(y)\neq 0
$$

and then:

$$
F_{X|Y}(x|y)=\int_{-\infty}^{x}f_{X|Y}(\xi|y)\,\mathrm{d}\xi
$$

The joint distribution of $X$ and $Y$ is then:

$$
\mathbb{P}[X\leq x,Y\leq y] =\int_{-\infty}^{x}\mathrm{d}\xi\int_{-\infty}^{y}\mathrm{d}\eta\,f_{XY}(\xi,\eta)=
=\int_{-\infty}^{y}\mathrm{d}\eta\,f_{Y}(\eta)\int_{-\infty}^{x}\mathrm{d}x\,f_{X|Y}(\xi|\eta)=\int_{-\infty}^{y}F_{X|Y}(x|y)f_{Y}(\eta)\,\mathrm{d}\eta=
=\int_{-\infty}^{y}F_{X|Y}(x|\eta)\,\mathrm{d}F_{Y}(\eta)
$$

With $y\to\infty$ we obtain the marginal distribution:

$$
\mathbb{P}[X\leq x]=\int_{-\infty}^{+\infty}F_{X|Y}(x|\eta)\,\mathrm{d}F_{Y}(\eta)
$$

And again we can compute expected values of functions of only $X$ by averaging over the joint pdf:

$$
\mathbb{E}[g(X)] =\int_{\mathbb{R}}\mathrm{d}\xi\int_{\mathbb{R}}\mathrm{d}\eta\,g(\xi)f_{XY}(X,\eta)=
=\int_{\mathbb{R}}\underbrace{\mathrm{d}\eta\,f_{Y}(\eta)}_{\mathrm{d}F_{Y}(\eta)}\underbrace{\int_{\mathbb{R}}\mathrm{d}\xi\,g(\xi)f_{X|Y}(\xi|\eta)}_{\mathbb{E}[g(X)|Y=\eta]}=\int_{\mathbb{R}}\mathbb{E}[g(X)|Y=\eta]\,\mathrm{d}F_{Y}(\eta)=
=\mathbb{E}[\mathbb{E}[g(X)|Y]]
$$

All these results are the same we had obtained in the discrete case, meaning that the new definition (1.20) is consistent.


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


> [!note] Proof. Suppose that the initial distribution is given by $\mathbb{P}(X_{0}=i)=p_{i}$. The Markov chain is *fully specified* if we can compute the (joint) probability of *any sequence of states* $\{i_{0},\ldots,i_{n}\}$
> Proof. Suppose that the initial distribution is given by $\mathbb{P}(X_{0}=i)=p_{i}$. The Markov chain is *fully specified* if we can compute the (joint) probability of *any sequence of states* $\{i_{0},\ldots,i_{n}\}$:
>
> $$
> \mathbb{P}\{X_{0}=i_{0},X_{1}=i_{1},\ldots,X_{n}=i_{n}\}
> $$
>
> Then the probability of any event $E$ will be just the *sum* of the probabilities associated with the sequences *contained* in that event. For example, if we wish to compute the probability of $X_{i}=j$, we sum the probabilities of all possible *evolutions* of the system that verify this equation, which are always in the form (2.1).
>
> By definition of conditional probabilities we can rewrite (2.1) as follows:
>
> $$
> \mathbb{P}\{X_{0}=i_{0},X_{1}=i_{1},\ldots,X_{n}=i_{n}\}=\mathbb{P}\{X_{n}=i_{n}|X_{0}=i_{0},\ldots,X_{n-1}=i_{n-1}\}\cdot
> \cdot\mathbb{P}\{X_{0}=i_{0},X_{1}=i_{1},\ldots,X_{n-1}=i_{n-1}\}
> $$
>
> Then we apply the Markov property:
>
> $$
> \mathbb{P}\{X_{n}=i_{n}|X_{0}=i_{0},\ldots,X_{n-1}=i_{n-1}\}=\mathbb{P}\{X_{n}=i_{n}|X_{n-1}=i_{n-1}\}=P_{i_{n-1},i_{n}}
> $$
>
> Substituting (2.3) in (2.2) we obtain:
>
> $$
> \mathbb{P}\{X_{0}=i_{0},X_{1}=i_{1},\ldots,X_{n}=i_{n}\}=P_{i_{n-1},i_{n}}\mathbb{P}\{X_{0}=i_{0},X_{1}=i_{1},\ldots,X_{n-1}=i_{n-1}\}
> $$
>
> Reiterating:
>
> $$
> \mathbb{P}\{X_{0}=i_{0},X_{1}=i_{1},\ldots,X_{n}=i_{n}\}=p_{i_{0}}P_{i_{0},i_{1}}\cdots P_{i_{n-2},i_{n-1}}P_{i_{n-1},i_{n}}
> $$
>
> And so all joint probabilities can be computed if we know $\{p_{i}\}_{i\in\mathbb{N}}$ and the transition matrix $\mathbf{P}$.
>
> To understand the behaviour of a Markov Chain we may inspect the $n$-step transition probabilities, i.e. the probabilities of the process going from a certain state $i$ to a state $j$ in exactly $n$ transitions:
>
> $$
> P_{ij}^{(n)}\equiv\mathbb{P}\{X_{m+n}=j|X_{m}=i\}
> $$
>
> which is independent on $m$ for a homogeneous Markov Chain.

> [!abstract] Theorem 2.0.1.
>
> The $n$-step transition probabilities of a Markov chain can be written recursively as:
>
> $$
> P_{ij}^{(n)}=\sum_{k=0}^{+\infty}P_{ik}P_{kj}^{(n-1)}
> $$
>
>
> where:
>
> $$
> P^{(0)}_{ij}\equiv\begin{cases}1&\text{if }i=j\\
> 0&\text{if }i\neq j\end{cases}
> $$

> [!note] Proof. We start from the definition, taking $m=0$ (as the process is homogeneous)
> Proof. We start from the definition, taking $m=0$ (as the process is homogeneous):
>
> $$
> P^{(n)}_{ij}=\mathbb{P}\{X_{n}=j|X_{0}=i\}=
> $$
>
> We consider the state $X_{1}$ at time $1$, and apply the law of total probability, noting that events $X_{1}=k$ for different values of $k$ are both mutually exclusive and exhaustive:
>
> $$
> =\sum_{k=0}^{+\infty}\mathbb{P}\{X_{n}=j,X_{1}=k|X_{0}=i\}=
> $$
>
> Recall that:
>
> $$
> \mathbb{P}(AB)=\mathbb{P}(A|B)\mathbb{P}(B)
> $$
>
> Equivalently, we can condition each probability to any event $C$:
>
> $$
> \mathbb{P}(AB|C)=\mathbb{P}(A|B,C)\mathbb{P}(B|C)
> $$
>
> And so:
>
> $$
> P^{(n)}_{ij}=\sum_{k=0}^{+\infty}\mathbb{P}\{X_{n}=j|X_{1}=k,X_{0}=i\}\mathbb{P}(X_{1}=k|X_{0}=i)=
> $$
>
> Applying the Markov property we can *remove* the condition $X_{0}=i$ in the first term, as all the information about the *past* will be still contained in $X_{1}$:
>
> $$
> =\sum_{k=0}^{+\infty}\underbrace{\mathbb{P}\{X_{n}=j|X_{1}=k\}}_{P^{(n-1)}_{kj}}\underbrace{\mathbb{P}(X_{1}=k|X_{0}=i)}_{P_{ik}}=
> =\sum_{k=0}^{+\infty}P_{ik}P^{(n-1)}_{kj} \square
> $$
>
> Note that (2.4) is a matrix multiplication:
>
> $$
> \mathbf{P}^{(n)}=\mathbf{P}\times\mathbf{P}^{(n-1)}
> $$
>
> Reiterating:
>
> $$
> \mathbf{P}^{(n)}=\underbrace{\mathbf{P}\times\cdots\times\mathbf{P}}_{n\text{ factors}}=\mathbf{P}^{(n)}
> $$
>
>
> ![[Stochastic_Processes_2020_p30_img3.jpeg]]
> Figure (2.1) - Markov chain graph for exercise 4.

> [!example] Example 4 (Markov chain)
>
> From exercise (3.)1.1 on the book. A Markov chain  $\{X_{i}\}_{i\in \mathbb{N}}$  on states 0, 1, 2 has the transition probability matrix:
>
> $$
> \mathbf {P} = \left( \begin{array}{c c c} 0. 1 & 0. 2 & 0. 7 \\ 0. 9 & 0. 1 & 0 \\ 0. 1 & 0. 8 & 0. 1 \end{array} \right)
> $$
>
> and initial distribution:
>
> $$
> \boldsymbol {p} = (p _ {0}, p _ {1}, p _ {2}) ^ {T} = \left( \begin{array}{c} 0. 3 \\ 0. 4 \\ 0. 3 \end{array} \right)
> $$
>
> Determine  $\mathbb{P}\{X_0 = 0, X_1 = 1, X_2 = 2\}$ .
>
> Solution. We follow the diagram. The probability of starting at  $X_0$  is  $p_0$ , and then we multiply by each transition:
>
> $$
> \begin{array}{l} \mathbb {P} \left\{X _ {0} = 0, X _ {1} = 1, X _ {2} = 1 \right\} = p _ {0} P _ {0 1} P _ {1 1} = \\ = 0. 3 \cdot 0. 2 \cdot 0. 1 = 0. 0 0 6 \\ \end{array}
> $$
>
> More in general, we may have non-consecutive states, for example in computing  $\mathbb{P}\{X_0 = 0,X_1 = 1,X_3 = 1\}$ . In this case we need the 2-step transition probability - summing over all intermediate states:
>
> $$
> \begin{array}{l} \mathbb {P} \left\{X _ {0} = 0, X _ {1} = 1, X _ {3} = 1 \right\} = p _ {0} \cdot P _ {0 1} P _ {1 1} ^ {(2)} = \\ = \sum_ {k = 0} ^ {2} p _ {0} P _ {0 1} P _ {1 k} P _ {k 1} = p _ {0} P _ {0 1} \sum_ {k = 0} ^ {2} P _ {1 k} P _ {k 1} \\ \end{array}
> $$
>
> And the last sum is just the scalar product between row 1 and column 1.
>
> One more case is when we have conditional probabilities, such as  $\mathbb{P}[X_3 = 1, X_1 = 1 | X_0 = 0]$ . In this case we already know the initial state, so we do
>
>
> not need to account for its probability, meaning that:
>
> $$
> \mathbb{P}[X_{3}=1,X_{1}=1|X_{0}=0]=P_{01}\cdot P_{11}^{(2)}
> $$

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

> [!abstract] Theorem 2.2.1.
>
> In a Poisson process, the inter-arrival times (i.e. the time between two consecutive events) are i.i.d. exponential random variables, with parameter $\lambda$.

> [!note] Proof. Let $\{S_{i}\}_{i\in\mathbb{N}}$ be the inter-arrival times, and $W_{n}$ the *cumulative* arrival times, defined as
> Proof. Let $\{S_{i}\}_{i\in\mathbb{N}}$ be the inter-arrival times, and $W_{n}$ the *cumulative* arrival times, defined as:
>
> $$
> W_{n}=\sum_{i=0}^{n}S_{i}
> $$
>
> Let’s consider the first difference:
>
> $$
> \mathbb{P}[S_{0}>t]=\mathbb{P}[0\text{ arrivals in }[0,t]]\underset{(2.5)}{=}e^{-\lambda t}
> $$
>
> and so $S_{0}$ follows an exponential distribution with parameter $\lambda$.
>
>
> We now consider the next one:
>
> $$
> \mathbb{P}[S_{1}>t|S_{0}=s]=\mathbb{P}[0\text{ arrivals in }(s,s+t]|S_{0}=s]
> $$
>
> But the number of arrivals in disjoint intervals are independent, and so we can drop the condition $S_{0}=s$. Applying stationarity we know that this probability depends only on the size of the interval, which is the same as that of $[0,t]$, and so we get the same result as before:
>
> $$
> =e^{-\lambda t}
> $$
>
> This means that also $S_{1}$ follows an exponential distribution with parameter $\lambda$, and is independent of $S_{0}$.
>
> The same argument can be repeated for any given $S_{n}$:
>
> $$
> \mathbb{P}[S_{n}>t|S_{i}=s_{i},i=0,\ldots,n-1]=
> \mathbb{P}[0\text{ arrivals in }(s_{0}+\cdots+s_{n-1},s_{0}+\cdots+s_{n-1}+t)|S_{i}=s_{i}]=e^{-\lambda t}
> $$
>
> which completes the proof of the theorem.

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
$$\mathbb{P}(\text{exactly } k \text{ Poisson events})$$
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
$$ (2.12)

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
$$ (2.13)

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

> [!note] Proof. By induction, we start with proving the  $n = 1$  case, and then show that if (2.16) holds up to  $n$ , then it holds also for  $n + 1$ . Explicitly
> Proof. By induction, we start with proving the  $n = 1$  case, and then show that if (2.16) holds up to  $n$ , then it holds also for  $n + 1$ . Explicitly:
>
> $$
> \begin{array}{l} \mathbf {P} ^ {1} = \frac {1}{a + b} \left( \begin{array}{c c} b & a \\ b & a \end{array} \right) + \frac {1 - a - b}{a + b} \left( \begin{array}{c c} a & - a \\ - b & b \end{array} \right) = \\ = \frac {1}{a + b} \left( \begin{array}{c c} b + a - a ^ {2} - a b & a - a + a ^ {2} + a b \\ b - b + a b + b ^ {2} & a + b - a b - b ^ {2} \end{array} \right) = \\ = \frac {1}{a + b} \left( \begin{array}{c c} (1 - a) (a + b) & a (a + b) \\ b (a + b) & (1 - b) (a + b) \end{array} \right) = \\ = \left( \begin{array}{c c} 1 - a & a \\ b & 1 - b \end{array} \right) = \mathbf {P} \\ \end{array}
> $$
>
> For the induction step:
>
> $$
> \mathbf {P} ^ {n + 1} = \mathbf {P} ^ {n} \mathbf {P} \underset {(2. 1 7)} {=} (a + b) ^ {- 1} [ \mathbf {A} + (1 - a - b) ^ {n} \mathbf {B} ] \mathbf {P}
> $$
>
> Note that:
>
> $$
> \mathbf {A P} = \left( \begin{array}{c c} b & a \\ b & a \end{array} \right) \times \left( \begin{array}{c c} 1 - a & a \\ b & 1 - b \end{array} \right) = \left( \begin{array}{c c} b & a \\ b & a \end{array} \right) = \mathbf {A}
> \mathbf {B P} = \left( \begin{array}{c c} a & - a \\ - b & b \end{array} \right) \times \left( \begin{array}{c c} 1 - a & a \\ b & 1 - b \end{array} \right) = (1 - a - b) \mathbf {B}
> $$
>
>
> And so:
>
> $$
> \mathbf{P}^{n+1}=(a+b)^{-1}[\mathbf{A}+(1-a-b)^{n+1}\mathbf{B}]=\mathbf{P}^{n+1}\qquad\square
> $$
>
> We can now use (2.16) to study the asymptotic behaviour. Suppose that $|1-a-b|<1$ (always true in the non trivial cases $0<a,b<1$), then $|1-a-b|^{n}\xrightarrow[n\to\infty]{}0$, and:
>
> $$
> \lim_{n\to\infty}\mathbf{P}^{n}=\frac{1}{a+b}\left(\begin{array}[]{cc}b&a\cr b&a\end{array}\right)
> $$
>
> Note that the two rows are equal, meaning that the asymptotic probability distribution does not depend on the initial state: the system will be in state $0$ with probability $b/(a+b)$, and in $1$ with $p=a/(a+b)$. In other words, the system “forgets” its initial condition. As we will see, this is a typical behaviour for many cases of Markov chains.
>
> Packet transmission and the two-state model. One possible application of the two-state model is given by modelling the error rate of a packet transition system with memory. Denote with state $0$ the event of a correct transmission, and with $1$ that of an error. Then the average packet error probability is given by:
>
> $$
> P_{e}=\frac{a}{a+b}
> $$
>
> Another interesting quantity is the mean length of a burst of errors, i.e. how long (on average) does the system spend in state $1$. The mean length $L$ of such a sequence of erroneous states is a geometric random variable (in the two-state model), whose average is the inverse of the probability of moving out of state $1$:
>
> $$
> \langle L\rangle=\frac{1}{P_{10}}=\frac{1}{b}
> $$
>
> In a real scenario, we will need to provide redundancy so that the system can tolerate $\langle L\rangle$ consecutive errors.

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
$$ (2.24)

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
$$ (26)

which can be solved by recursion.

Note that computing $f_{ij}(n)$ in this way does not require $f_{kj}(m)$ $\forall m<n$ and $\forall k\neq j$ (unlike the first-step analysis method), but only $f_{ij}(m)$ $\forall m<n$. However, we need all powers $\mathbf{P}^{m}$ for $m<n$. So, at the end, the computational complexity is of the same order.

Often, however, we are interested merely in the moments of $\theta_{ij}$, and not in the full statistics $f_{ij}$. We start by noting that:

$$
\theta_{ij}=\begin{cases}1&\text{with prob. }P_{ij}\\
1+\theta_{kj}&\text{with prob. }P_{ik},\,k\neq j\end{cases}
$$ (27)

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
$$ (2.29)

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
$$ (2.41)


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


# Chapter 3 Long Run Behaviour of Markov Chains

### 3.1 Regular Markov Chains

A Markov Chain is said to be regular if:

1. It has a finite number of states $0,1,\ldots,N$.
2. There is an integer $k\in\mathbb{Z}$ so that $(\mathbf{P}^{k})_{ij}>0\;\forall i,j$, i.e. all $k$-step transition probabilities are non-zero.

From these two conditions it follows that, given enough time, the system can (in principle) evolve from any state $i$ to any other state $j$. We will see (later on) that this guarantees the existence of a unique limiting probability distribution $\pi=(\pi_{0},\pi_{1},\ldots,\pi_{N})$, where $\pi_{j}>0\;\forall j=0,\ldots,N$ and $\sum_{j}\pi_{j}=1$, such that:

$$
\lim_{n\to\infty}P^{(n)}_{ij}=\pi_{j}>0\quad\forall j=0,1,\ldots,N
$$

This means that:

- There is a definite asymptotic behaviour - i.e. the limit $\lim_{n\to\infty}P^{(n)}_{ij}$ exists.
- This limit is independent of the initial state $i$, and so the system completely “forgets” where it came from.
- All states will keep being visited, because $\pi_{j}>0$, i.e. $\pi_{j}\neq 0$.

> [!abstract] Theorem 3.1.1.
>
> Let P be a regular transition probability matrix on the states $0,1,\ldots,N$. Then the limiting distribution $\boldsymbol{\pi}=(\pi_{0},\pi_{1},\ldots,\pi_{N})^{T}$ is the unique, nonnegative solution of the equations:
>
> $$
> \pi_{j}=\sum_{k=0}^{N}\pi_{k}P_{kj}\qquad j=0,1,\ldots,n
> $$
>
>
> with $\pi_{k}\geq 0$ and the normalization constraint:
>
> $$
> \sum_{k=0}^{N}\pi_{k}=1
> $$

> [!note] Proof. First note that the system in (3.1) is homogeneous, meaning that if $\pi_{0}$ is a solution then also $a\pi_{0}$, with $a\in\mathbb{R}\setminus\{0\}$ is a solution - and so it admits an infinite number of solutions. So, to have only a unique $\pi$ we need the constraint of (3.2), which also serves to guarantee that $\pi$ correctly represents a probability distribution.
> Proof. First note that the system in (3.1) is homogeneous, meaning that if $\pi_{0}$ is a solution then also $a\pi_{0}$, with $a\in\mathbb{R}\setminus\{0\}$ is a solution - and so it admits an infinite number of solutions. So, to have only a unique $\pi$ we need the constraint of (3.2), which also serves to guarantee that $\pi$ correctly represents a probability distribution.
>
> 1. Existence. As the Markov chain is regular, it admits a limiting distribution $\lim_{n\to\infty}P^{(n)}_{ij}=\pi_{j}$, for which $\sum_{k=0}^{N}\pi_{k}=1$. In fact:
>
> $$
> \sum_{j=0}^{N}P^{(n)}_{ij}=1\qquad\forall i\in\{0,\ldots,N\},n\geq 1
> $$
>
> Taking the limit of both sides:
>
> $$
> \lim_{n\to\infty}\sum_{j=0}^{N}P^{(n)}_{ij}=1=\sum_{j=0}^{N}\pi_{j}
> $$
>
> And so the $\pi_{j}$ are correctly normalized.
>
> All that’s left is to show that they verify (3.1). To do so, we start from:
>
> $$
> \mathbf{P}^{(n)}=\mathbf{P}^{(n-1)}\times\mathbf{P}\Leftrightarrow P^{(n)}_{ij}=\sum_{k=0}^{N}P^{(n-1)}_{ik}P_{kj}\quad j=0,\ldots,N
> $$
>
> And take the limit $n\to\infty$:
>
> $$
> \lim_{n\to\infty}P^{(n)}_{ij} =\lim_{n\to\infty}\sum_{k=0}^{N}P^{n-1}_{ik}P_{kj}
> \Rightarrow\pi_{j} =\sum_{k=0}^{N}\lim_{n\to\infty}P^{n-1}_{ik}P_{kj}=\sum_{k=0}^{N}\pi_{k}P_{kj}
> $$
>
> which is exactly (3.1). Exchanging the limit and the sum can be done because $N$ is finite, and so we do not have problems of convergence.
> 2. Uniqueness. Suppose that $\boldsymbol{x}$ is a solution of (3.1), i.e. that:
>
> $$
> x_{j}=\sum_{k=0}^{N}x_{k}P_{kj}\quad j=0,\ldots,N\qquad\sum_{k=0}^{N}x_{k}=1
> $$
>
> We want to show that $x_{j}=\pi_{j}$, and so there is only one limiting probability. In matrix notation:
>
> $$
> \boldsymbol{x}=\boldsymbol{x}\mathbf{P}
> $$
>
>
> Multiplying to the right by $\mathbf{P}$:
>
> $$
> \boldsymbol{x}\mathbf{P}=\boldsymbol{x}\mathbf{P}^{(2)}
> $$
>
> In terms of entries, this equates to:
>
> $$
> x_{l}\underset{(3.11)}{=}\sum_{j=0}^{N}x_{j}P_{jl}=\sum_{j=0}^{N}\sum_{k=0}^{N}x_{k}P_{kj}P_{jl}=\sum_{k=0}^{N}x_{k}P_{kl}^{(2)}
> $$
>
> where we *exchanged* the order of the two sums (as they are over a finite number of elements) to highlight the 2-step transition matrix.
>
> Note that $\boldsymbol{x}=\boldsymbol{x}\mathbf{P}=\boldsymbol{x}\mathbf{P}^{(2)}$. Reiterating $n$ times:
>
> $$
> \boldsymbol{x}=\boldsymbol{x}\mathbf{P}^{(n)}\Leftrightarrow x_{l}=\sum_{k=0}^{N}x_{k}P_{kl}^{(n)}\quad l=0,\ldots,N
> $$
>
> As this holds for all values of $n$, it holds also in the limit $n\to\infty$:
>
> $$
> x_{l}=\lim_{n\to\infty}\sum_{k=0}^{N}x_{k}P_{kl}^{(n)}=\underbrace{\sum_{k=0}^{N}x_{k}}_{1}\pi_{l}=\pi_{l}\qquad l=0,\ldots,N
> $$
>
> which proves uniqueness.

#### 3.1.1 Interpretation of the Limiting Distribution

Given a regular transition matrix $\mathbf{P}$ for a Markov process on $N+1$ states $0,\ldots,N$, we can find the limiting distribution by solving (3.1):

$$
\pi_{i}=\sum_{k=0}^{N}\pi_{k}P_{ki}\quad i=0,\ldots,N\qquad\sum_{i=0}^{N}\pi_{i}=1
$$

This means that the probability of finding the system in state $j$ *after a long time* does not depend on the initial state $i$, and it is given by $\pi_{j}$:

$$
\pi_{j}=\lim_{n\to\infty}P_{ij}^{(n)}=\lim_{n\to\infty}\mathbb{P}\{X_{n}=j|X_{0}=i\}
$$

Equivalently, each $\pi_{j}$ represents the *fraction of time* spent by the system in state $j$. In particular, this is useful to compute the long run average of *functional* of the states. For example, if each visit to state $j$ is associated with a *cost* $c_{j}$, then the long run mean cost $C$ (per unit time) associated with the Markov chain is:

$$
C=\sum_{j=0}^{N}\pi_{j}c_{j}
$$

This second interpretation comes from the fact that if a sequence $\{a_{n}\}_{n\in\mathbf{\mathbb{N}}}$ converges to a limit $a$, then also the *running averages* over the first $m$ elements


converge to $a$:

$$
\lim_{k\to\infty}a_{k}=a\Rightarrow\lim_{m\to\infty}\frac{1}{m}\sum_{k=0}^{m-1}a_{k}=a
$$

(but the converse is not true in general).

With respect to our problem, we note that the *fraction of time* spent by the system in state $j$ over a $m$-long run can be written as:

$$
\frac{1}{m}\sum_{k=0}^{m-1}\mathbf{1}\{X_{k}=j\}
$$

The *mean* fraction of visits of state $j$ (over a $m$-long run) is then:

$$
\mathbb{E}\left[\frac{1}{m}\sum_{k=0}^{m-1}\mathbf{1}\{X_{k}=j\}|X_{0}=i\right] =\frac{1}{m}\sum_{k=0}^{m-1}\mathbb{E}[\mathbf{1}\{X_{k}=j\}|X_{0}=i]=
=\frac{1}{m}\sum_{k=0}^{m-1}\mathbb{P}\{X_{k}=j|X_{0}=i\}=
=\frac{1}{m}\sum_{k=0}^{m-1}P_{ij}^{(k)}
$$

Taking the limit $n\to\infty$, we know that:

$$
\lim_{n\to\infty}P_{ij}^{(n)}=\pi_{j}\Rightarrow\lim_{n\to\infty}\frac{1}{m}\sum_{k=0}^{m-1}P_{ij}^{(k)}=\pi_{j}
$$

And so:

$$
\lim_{n\to\infty}\mathbb{E}\left[\frac{1}{m}\sum_{k=0}^{m-1}\mathbf{1}\{X_{k}=j\}|X_{0}=i\right]=\lim_{m\to\infty}\frac{1}{m}\sum_{k=0}^{m-1}P_{ij}^{(k)}=\pi_{j}
$$


### 3.2 Non regular Markov chains

Not all Markov chains are regular, that is there are Markov chains such that their $n$-step probability matrix $\mathbf{P}^{n}$ always contains some $0$ entries. In these cases, the previously derived results about the limiting distribution may not hold, and in particular:

- The limiting distribution $\lim_{n\to\infty}P_{ij}^{(n)}$ may not exist at all
- There could be several limiting distributions, each depending on the initial state
- The system may stop visiting certain states in the long-run, i.e. $\lim_{n\to\infty}P_{ij}=\pi_{j}$ holds, but not $\pi_{j}\neq 0$ $\forall j$.

We can show explicit examples for all these cases (fig. 3.1):

Examples of non-regular MC


![[Stochastic_Processes_2020_p70_img18.jpeg]]
(a) - There are two limiting distributions, depending on the initial state

![[Stochastic_Processes_2020_p70_img19.jpeg]]
(b) - The chain is periodic: no limiting distribution exist.

![[Stochastic_Processes_2020_p70_img20.jpeg]]
(c) - A unique limiting distribution (independent of initial state) exists, but certain states (0 in this case) are never visited in the long run.
Figure (3.1) - Examples of non-regular Markov chains.

1.  $\left[ \begin{array}{ll}1 & 0\\ 0 & 1 \end{array} \right] = \mathbb{1}\qquad \mathbf{P}^n = \mathbf{P}\quad \forall n$

In this case the Markov chain just remains fixed in the initial state. Clearly the limiting distribution exists, but it is not independent of the initial state (or else all the rows in the limit would have been equal). Moreover, depending on the case, some states are not visited anymore in the long run: if the chain starts at 0, it will never visit 1, meaning that  $\pi_1 = 0$ .

2.  $\left[ \begin{array}{ll}0 & 1\\ 1 & 0 \end{array} \right]\qquad \mathbf{P}^n = \left\{ \begin{array}{ll}\mathbf{P} & n\text{odd}\\ \mathbb{1} & n\text{even} \end{array} \right.$

In this case the limiting distribution does not even exist, since  $\mathbf{P}^n$  keeps oscillating.

3.  $\left[ \begin{array}{cc}\frac{1}{2} & \frac{1}{2}\\ 0 & 1 \end{array} \right]\qquad \mathbf{P}^n = \left[ \begin{array}{cc}(\frac{1}{2})^n & 1 - (\frac{1}{2})^n\\ 0 & 1 \end{array} \right]$

Here the limit exists, it is independent of initial state, but not all limiting probabilities are strictly positive:

$$
\lim  _ {n \to \infty} \mathbf {P} ^ {n} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 1 \end{array} \right]
$$

# 3.3 Classification of States

All non-regular Markov chains, by definition, arise from the presence of states that are isolated from each other, i.e. there is no possible chain of transitions - however long - linking them.

So, it is useful to formalize the concepts of accessibility and communication between states.

A state  $j$  is said to be accessible from state  $i$  if  $P_{ij}^{(n)} > 0$  for some integers  $n \geqslant 0$ , thus meaning that it is possible to reach state  $j$ , starting from  $i$ , in a certain number of steps.

If states  $i$  and  $j$  are accessible to each other, then they are said to communicate, and we denote this with  $i \leftrightarrow j$ . Two non-communicating states are such that either  $P_{ij}^{(n)} = 0$  or  $P_{ji}^{(n)} = 0$  (or both) for all  $n \geqslant 0$ .

Accessibility

Communication


Communication between states is an equivalence relation, i.e. it satisfies the following three key properties:

1. Reflexivity $(i \leftrightarrow i)$. Clearly $i$ can access itself, without even moving:

$$
P_{ij}^{(0)} = \delta_{ij} = \begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases}
$$

2. Symmetry $(i \leftrightarrow j$ then $j \leftrightarrow i)$, which follows directly from the definition of communication
3. Transitivity $(i \leftrightarrow j, j \leftrightarrow k$ then $i \leftrightarrow k)$

In order to prove 3, let $i \leftrightarrow j$ and $j \leftrightarrow k$. By hypothesis, this means that there exist integers $n$ and $m$ such that $P_{ij}^{(n)} > 0$ and $P_{jk}^{(m)} > 0$. Consequently, since each $P_{ji}^{(t)}$ is non-negative, we conclude:

$$
P_{ik}^{(n + m)} = \sum_{r = 0}^{\infty} P_{ir}^{(n)} P_{rk}^{(m)} \geqslant P_{ij}^{(n)} P_{jk}^{(m)} > 0
$$

where in (a) we used the fact that a sum of non-negative terms is always greater or equal each of its addends. This proves that the transition $i \to k$ is possible, i.e. it has a non-zero probability. By a similar argument one can prove that also the reverse transition $(k \to i)$ is possible, i.e. there exists an integer $\nu$ s.t. $P_{ki}^{(\nu)} > 0$, thus proving $i \leftrightarrow k$.

Because of these properties, we can now partition the totality of states into equivalence classes, each formed by inter-communicating states.

Note that different classes are not isolated: it may be possible to start in one class $A$ and move to some other class $B$ with non-zero probability. However, in this case the reverse transition $(B \to A)$ is impossible: otherwise the two classes would together form a single class. In other words, different classes can be connected only by one-way transitions.

If chain is made up of one single class, then it is said to be irreducible, otherwise it is said to be reducible. In other words, in an irreducible class, all states communicate with each other. For example, the following transition probability matrix describes a Markov chain with two different non-interacting classes:

Irreducibility

$$
\mathbf{P} = \begin{vmatrix}
\frac{1}{2} & \frac{1}{2} & 0 & 0 & 0 \\
\frac{1}{4} & \frac{3}{4} & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & \frac{1}{2} & 0 & \frac{1}{2} \\
0 & 0 & 0 & 1 & 0
\end{vmatrix} = \begin{vmatrix}
\mathbf{P_1} & 0 \\
0 & \mathbf{P_2}
\end{vmatrix}
$$


Another example is given by the following random-walk model:

$$
\mathbf {P} = \left[ \begin{array}{c c c c c c c c} 1 & 0 & 0 & 0 & \dots & 0 & 0 & 0 \\ q & 0 & p & 0 & \dots & 0 & 0 & 0 \\ 0 & q & 0 & p & \dots & 0 & 0 & 0 \\ \vdots & & & & & \vdots & \vdots & \vdots \\ 0 & \dots & \dots & \dots & \dots & q & 0 & p \\ 0 & \dots & \dots & \dots & \dots & 0 & 0 & 1 \end{array} \right] \begin{array}{l} 0 \\ 1 \\ 2 \\ \vdots \\ a - 1 \\ a \end{array} \tag {3.4}
$$

Here $p, q > 0$ are respectively the probabilities of forward/backward motion. Note that states 0 and $a$ are absorbing, and so we have three classes: $A = \{0\}$, $B = \{1,2,\ldots,a - 1\}$ and $C = \{a\}$. Starting anywhere in class $B$ can lead to $A$ or $C$, but the reverse transition cannot happen.

## 3.3.1 Periodicity

A Markov chain exhibits a periodic behaviour when it cyclically visits some states. More precisely, we focus on a single state $i$ and say that it is periodic with a certain period $d(i)$ if the system may visit it only every $n$ steps. In other words, if the system starts at $i$, then it may return to $i$ after $n$, $2n$, $3n$ or any multiple of $n$ steps - but never during an "in-between" step such as $n - 1$.

So, we formally define the period $d(i)$ of state $i$ as the greatest common divisor (g.c.d.) of all integers $n \geqslant 1$ for which $P_{ii}^{(n)} > 0$.

In the case that the system never returns to $i$, i.e. $P_{ii} = 0 \quad \forall n \geqslant 1$, we conventionally define $d(i) = 0$.

Note that if $P_{ii} > 0$, then $d(i) = 1$, since the system can remain in this state any length of time.

The most obvious example of periodicity is given by a chain cycling through $N$ states:

$$
\mathcal {M} _ {n \times n} \ni \mathbf {P} = \left( \begin{array}{c c c c c c} 0 & 1 & 0 & 0 & \dots & 0 \\ 0 & 0 & 1 & 0 & \dots & 0 \\ \vdots & & & & & \vdots \\ 0 & \dots & & \dots & \dots & 1 \\ 1 & 0 & 0 & \dots & \dots & 0 \end{array} \right)
$$

Here $d(i) = N$ for every $i = 0, \dots, N - 1$, as can be seen from the block diagram in fig. 3.2.

Periodicity


Another example is given by:

$$
\mathbf {P} = \begin{array}{c c c c c} & 0 & 1 & 2 & 3 \\ 0 & 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 1 & 0 \\ 2 & 0 & 0 & 0 & 1 \\ 3 & 1 & 0 & \frac {1}{2} & 0 \end{array} \tag {3.5}
$$

with the block diagram represented in fig. 3.3. Starting from 0, the system can return to 0 after 4, 6, 8, etc. steps (depending on how many iterations it spends between states 2 and 3), meaning that  $d(0) = 2$ .

Similarly, in the case of a random walk (3.4) every transient state 1, 2, ...,  $N - 1$  has period 2. In fact, starting from  $i$ , the system can return to it after an even number of steps: half spent "getting away" from  $i$ , and the other half "returning towards"  $i$ . In other words,  $P_{ii}^{n} = 0$  for every  $n$  odd.

> [!abstract] Theorem 3.3.1. Period is a class property
> Theorem 3.3.1. Period is a class property:
>
> $$
> i \leftrightarrow j \quad \Longrightarrow \quad d (i) = d (j)
> $$
>
> In other words, all states that communicate with each other, i.e. are contained in the same class, share the same period.

> [!note] Proof. The basic idea is shown in fig. 3.4. Essentially, we want to show that  $d(j) \leq s$ , where  $s$  is the length of any path  $i \to i$ . This implies that  $d(j) \leq d(i)$ . Then, exchanging the roles of  $i$  and  $j$ , we reach the equality  $d(i) = d(j)$ .
> Proof. The basic idea is shown in fig. 3.4. Essentially, we want to show that  $d(j) \leq s$ , where  $s$  is the length of any path  $i \to i$ . This implies that  $d(j) \leq d(i)$ . Then, exchanging the roles of  $i$  and  $j$ , we reach the equality  $d(i) = d(j)$ .
>
> Let  $S_{i}$  be the set containing the lengths of all possible paths starting from  $i$  and returning to  $i$ :  $S_{i} = \{s > 0 : P_{ii}^{(s)} > 0\}$ . Then the period of  $i$  is  $d(i) = gcd(S_{i})$ .
>
> By hypothesis,  $i \leftrightarrow j$ , and so there are two integers  $m, n$  such that  $P_{ij}^{(m)} > 0$ ,  $P_{ji}^{(n)} > 0$ .
>
> So, it is possible to have a path from  $j \to i$  in  $n$  steps, then from  $i \to i$  in  $s \in S_i$  steps and finally going from  $i \to j$  in  $m$  steps:
>
> $$
> P _ {j j} ^ {(n + s + m)} = \sum_ {h, k} P _ {j h} ^ {(n)} P _ {h k} ^ {(s)} P _ {k j} ^ {(m)} \geqslant P _ {j i} ^ {(n)} P _ {i i} ^ {(s)} P _ {i j} ^ {(m)} > 0
> $$
>
> ![[Stochastic_Processes_2020_p73_img21.jpeg]]
> Figure (3.2) - Block diagram for a  $N = 6$  cyclic Markov chain
>
>
> ![[Stochastic_Processes_2020_p74_img22.jpeg]]
> Figure (3.3) - Block diagram for (3.5)
>
> Since all terms in the sum are non-negative, it is certainly greater or equal to a particular addend, which is chosen to be strictly greater than 0.
>
> Similarly, the path that repeats the  $i \to i$  cycle two times is possible:
>
> $$
> P _ {i i} ^ {(2 s)} \geqslant \left(P _ {i i} ^ {(s)}\right) ^ {2} > 0 \quad \Rightarrow \quad P _ {j j} ^ {(n + 2 s + m)} > 0
> $$
>
> So we have found two possible path lengths that start from  $j$  and return to  $j$ , i.e.  $\forall s \in S_i$  both  $(n + s + m)$  and  $(n + 2s + m) \in S_j$ . By definition of  $d(j)$ , all elements of  $S_j$  are integer multiples of  $d(j)$ :
>
> $$
> n + s + m = k _ {1} d (j); \quad n + 2 s + m = k _ {2} d (j) \qquad k _ {1}, k _ {2} \in \mathbb {N}
> $$
>
> Subtracting member to member we get:
>
> $$
> s = (k _ {2} - k _ {1}) d (j)
> $$
>
> And so also  $s$  is a integer multiple of  $d(j)$ . This holds  $\forall s \in S_i$ , meaning that  $d(j)$  is a common divisor of all elements of  $S_i$ . As  $d(i)$  is the greatest common divisor of  $S_i$ , then  $d(i)$  must be a multiple of  $d(j)$ .
>
> Finally, note that we can switch the roles of  $i$  and  $j$  and repeat all these arguments, concluding that also  $d(j)$  must be a multiple of  $d(i)$ . Clearly this can happen only if:
>
> $$
> d (i) = d (j)
> $$
>
> □

## 3.3.2 Recurrence

The smallest path-length  $s$  needed for starting in a state  $i$  and returning to  $i$  is the first return time  $\theta_{ii}$ . Its distribution is given by:

Recurrence

$$
f _ {i i} ^ {(n)} = \mathbb {P} \{\theta_ {i i} = n \} = \mathbb {P} \{X _ {n} = i, X _ {\nu} \neq i, \nu = 1, 2 \dots , n - 1 | X _ {0} = i \} \quad \forall n \geqslant 1
$$


![[Stochastic_Processes_2020_p75_img23.jpeg]]
Figure (3.4) - Suppose that  $d(i) = 3$ . Then all paths that start from  $i$  and return to  $i$  must have a length that is a multiple of 3 - in particular  $n + m$  must be divisible by 3. Now focus on  $j$ , and note that  $d(j)$  cannot be  $< 3$ . In fact, if  $d(j)$  were, for example, 2, then it would exist a 2-step path  $j \rightarrow j$ . But then we could construct a path  $i \rightarrow i$  of  $n + m + 2$  steps ( $i \rightarrow j$  in  $n$  steps,  $j \rightarrow j$  in 2 steps and  $j \rightarrow i$  in  $m$  steps), which is not a multiple of 3. Similarly,  $d(j)$  cannot be  $> 3$ : because we can construct two paths  $j \rightarrow j$  with length  $n + m$  and  $n + m + 3$ , and their g.c.d. is  $\leq 3$ . So  $d(j) = d(i) = 3$

So  $f_{ii}^{(n)}$  is the probability that, starting from the  $i$ -th state, the first return to  $i$  occurs exactly at the  $n$ -th transition.

Clearly this is just a special case of first passage time, and in particular we can compute  $f_{ii}^{(n)}$  recursively according to 2.26, keeping in mind that  $i = j$ .

Consider a process starting from state  $i$ . The probability  $f_{ii}$  that it will return to state  $i$  (after any amount of time) is given by the sum of the single probabilities of first arrival times for different  $n$  steps, since they are disjoint events (we can arrive for the first time only once):

$$
f _ {i i} = \sum_ {n = 0} ^ {\infty} f _ {i i} ^ {(n)} = \lim _ {N \to \infty} \sum_ {n = 0} ^ {N} f _ {i i} ^ {(n)}
$$

When  $f_{ii} = 1$ , a state is said to be recurrent, because we are guaranteed that sooner or later we will come back to it. If a state is not recurrent, then it is said to be transient.

Considering a transient state  $i$ , then  $f_{ii} < 1$  for definition. Supposing we come back once, because of Markov property we forget about past events, and so the probability of coming back again is  $f_{ii} < 1$  one more time. This means that the probability of returning at least twice is  $(f_{ii})^2 < 1$ . By iterating this argument, we obtain that the probability to come back to  $i$ -th state at least  $k$  times is:  $(f_{ii})^k$ ,  $k = 1, 2 \ldots$ .

Let  $M$  be the random variable that counts how many times the chain returns to state  $i$ . Its distribution is geometric:

$$
\mathbb {P} \{M \geqslant k | X _ {0} = i \} = (f _ {i i}) ^ {k} \quad \text {for} \mathrm {k} = 1, 2 \dots
$$

The expectation of  $M$  is then:

$$
\mathbb {E} [ M | X _ {0} = i ] = \sum_ {k = 1} ^ {\infty} \mathbb {P} \{M \geq k | X _ {0} = i \} = \sum_ {k = 1} ^ {\infty} (f _ {i i}) ^ {k} = \frac {f _ {i i}}{1 - f _ {i i}}
$$

Transient states


![[Stochastic_Processes_2020_p76_img24.jpeg]]
Figure (3.5) - Cumulative probabilities for proper and non proper random variables. Notice as, for the non proper random variable, while  $X \to \infty$ ,  $P(X)$  asymptotically tends to a value different than 1.

For a recurrent state  $i$ , however, we are certain that the chain will return to it. By the Markovian property, at each return the chain "forgets" about its past - and so the probability of returning will be always 1, meaning that given infinite time the system will visit  $i$  an infinite number of times. This kind of behaviour cannot be captured by random variables in their current definition. In fact, one of the basic properties of proper or finite-values random variables, is that:

$$
\lim  _ {x \rightarrow \infty} \mathbb {P} [ X \leqslant x ] = \lim  _ {x \rightarrow \infty} F (x) = 1
$$

However, in the case of  $M$  for a recurrent state  $i$ , we have  $\mathbb{P}[M \leq x] = 0$  for all finite  $x$ , because the chain will surely return to  $i$  an infinite amount of times! So:

$$
\lim  _ {x \rightarrow \infty} \mathbb {P} [ M \leq x ] = 0 \neq 1
$$

and thus  $M$  is not a proper random variable. So, to study these kind of variables, we need a generalized definition, leading to the so-called improper random variables.

## Improper random variables

We now introduce the improper random variables, for which we admit:

$$
\lim  _ {x \rightarrow \infty} \mathbb {P} [ X > x ] = P _ {\infty} > 0
$$

We interpret  $P_{\infty}$  as the probability that  $X$  will take an infinite value, thus denoting it (formally) with:

$$
\mathbb {P} [ X = \infty ] = P _ {\infty}
$$

In other words, proper random variables cannot ever assume infinite values, as their probability of assuming greater and greater values must vanish. On the other hand, improper random variables may have a finite probability of assuming an infinite value.

Recurrent states


> [!example] Example 5 (Recurrent states)
>
> Let $n$ be the number of visits to a recurrent state $i$. Then $\mathbb{P}[n\geqslant k]=1\ \forall k$ because of the definition of recurrent state, and also the probability of visiting $i$ any number of times is also $1$. Taking the limit of the tail probability as $k\to\infty$:
>
> $$
> P_{\infty}=\lim_{k\to\infty}\mathbb{P}[n>k]=\mathbb{P}[n=\infty]=1.
> $$
>
> This means that, in the limit, $n$ can’t take any possible finite value.
>
> For non-negative improper r.v.s, we have in the continuous case:
>
> $$
> \mathbb{E}[X]=\int_{0}^{+\infty}x\,\mathrm{d}F(x)=\int_{0}^{+\infty}\mathbb{P}[X>x]\,\mathrm{d}x=\infty
> $$
>
> So the expectation of an improper r.v. diverges, since $\lim_{x\to\infty}\mathbb{P}[X>x]>0$.
>
> The same holds for discrete non-negative improper r.v.s
>
> $$
> \mathbb{E}[X]=\int_{0}^{+\infty}x\,\mathrm{d}F(x)=\sum_{k=0}^{+\infty}\mathbb{P}[X>k]=\infty
> $$

> [!abstract] Theorem 3.3.2.
>
> $$
> \text{state }i\text{ is recurrent}\ \ \Longleftrightarrow\ \sum_{n=1}^{\infty}P_{ii}^{(n)}=\infty
> $$
>
> Equivalently, state $i$ is transient if and only if $\sum_{n=1}^{\infty}P_{ii}^{(n)}<\infty$.
>
> Note that this is just a restatement of the second Borel-Cantelli lemma, since all paths $i\to i$ of different length $n$ form independent events.

> [!note] Proof.
>
> Let $M$ be the number of visits to $i$-th state:
>
> $$
> M=\sum_{n=1}^{+\infty}\mathbf{1}\{X_{n}=i\}
> $$
>
> Its expectation is given by:
>
> $$
> \mathbb{E}[M|X_{0}=i] =\mathbb{E}\left[\sum_{n=1}^{+\infty}\mathbf{1}\{X_{n}=i\}|X_{0}=i\right]=
> \underset{(a)}{=}\sum_{n=1}^{+\infty}\mathbb{E}\left[\mathbf{1}\{X_{n}=i\}|X_{0}=i\right]=\sum_{n=1}^{+\infty}P_{ii}^{(n)}
> $$
>
> In other words, the sum of the *return* probabilities $P_{ii}^{(n)}$ is exactly the average number of returns to state $i$.
>
> However, step (a) needs justification. In fact, we know we are allowed to bring the expectation inside the sum (because of linearity), but this is always true only when we are summing a finite number of terms - which is not the case
>
>
> here. When dealing with infinite sums, we are implicitly considering limits - one for the expectation, and one for the sum. In general, their order may actually matter, and so we cannot exchange them without providing some kind of justification. For now, we will assume that (a) is legitimate, delaying its proof to argument 3.3.3.
>
> All that’s left is to examine two cases:
>
> 1. If $i$ is a transient state, then $f_{ii}<1$, so:
>
> $$
> \sum_{n=1}^{+\infty}P_{ii}^{(n)}=\mathbb{E}[M|X_{0}=i]=\sum_{k=1}^{+\infty}P[M\geqslant k|X_{0}=i]=\sum_{k=1}^{+\infty}(f_{ii})^{k}=\frac{f_{ii}}{1-f_{ii}}<\infty
> $$
> 2. If $i$ is a recurrent state, then $f_{ii}=1$, leading to:
>
> $$
> \sum_{n=1}^{+\infty}P_{ii}^{(n)}=\mathbb{E}[M|X_{0}=i]=\sum_{k=1}^{+\infty}P[M\geqslant k|X_{0}=i]=\sum_{k=1}^{+\infty}(f_{ii})^{k}=\infty
> $$
>
> Summarizing, for a transient state the expectation of $M$ is finite, while for a recurring state it is infinite - which concludes the proof. ∎

#### 3.3.3 Fubini’s theorem

In many cases we use the linearity property of the operators $\sum$, $\int$, $\mathbb{E}$ to swap their position. This happens for example when, for $x$ and $y$ belonging to some sets $D_{x}$ and $D_{y}$ we write:

$$
\sum_{x\in D_{x}}\sum_{y\in D_{y}}f(x,y)=\sum_{y\in D_{y}}\sum_{x\in D_{x}}f(x,y)
$$

or when we exchange a sum with an expected value: $\mathbb{E}\sum=\sum\mathbb{E}$.
The mathematical tool allowing us to do so is the Fubini’s Theorem, that states that if any one of the sums $\sum_{x}\sum_{y}f(x,y)$ or $\sum_{y}\sum_{x}f(x,y)$ converges absolutely, meaning that the sum with $|f(x,y)|$ is finite, then the exchange is valid.
In order to have a better understanding of this result, consider the following. We can rewrite any function $f(x,y)$ as the difference of its positive and negative parts $f_{\pm}(x,y)$:

$$
f(x,y)=f_{+}(x,y)-f_{-}(x,y)
$$

where:

$$
f_{+}(x,y)=\max(f(x,y),0)\qquad f_{-}(x,y)=-\min(f(x,y),0)
$$

Basically, $f_{\pm}(x,y)$ are the modulus of the positive and negative values that $f$ can take.


Then the double sum $\sum_{x}\sum_{y}f(x,y)$ can be rewritten as:

$$
\sum_{x}\sum_{y}f(x,y)=\sum_{x}\sum_{y}f_{+}(x,y)-\sum_{x}\sum_{y}f_{-}(x,y)
$$

Similarly, the double sum of $|f(x,y)|$ is given by:

$$
\sum_{x}\sum_{y}|f(x,y)|=\sum_{x}\sum_{y}f_{+}(x,y)+\sum_{x}\sum_{y}f_{-}(x,y)
$$

As stated by Fubini’s theorem, if $\sum_{x}\sum_{y}|f(x,y)|<\infty$, then both $\sum_{x}\sum_{y}f_{+}<\infty$ and $\sum_{x}\sum_{y}f_{-}<\infty$ as well, and their difference $f_{+}-f_{-}$ is well defined, too. On the other hand it may happen that $\sum_{x}\sum_{y}|f|$ is infinite while $\sum_{x}\sum_{y}f$ is finite, because $f(x,y)\leqslant|f(x,y)|$. In this case $\sum_{x}\sum_{y}|f|$ may be made up by two possible diverging components. Then, it may occur that $\sum_{x}\sum_{y}f=\sum_{x}\sum_{y}f_{+}-\sum_{x}\sum_{y}f_{-}=\infty-\infty=\text{\sf?}$ which is an indeterminate form.

Example Let $X_{i}$ be a non-negative random variable. We want now to establish whether it is legitimate for us to exchange $\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]=\sum_{i=0}^{+\infty}\mathbb{E}\left[X_{i}\right]$.

- If $\sum_{i=0}^{+\infty}\mathbb{E}[X_{i}]<\infty$ and recalling that in the non-negative case absolute convergence and simple convergence refer to the same concept, from Fubini’s theorem we know that $\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]<\infty$ too. This means that both $\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]$ and $\sum_{i=0}^{+\infty}\mathbb{E}\left[X_{i}\right]$ exist, and share the same value. In conclusion the exchange is valid.
- If $\sum_{i=0}^{+\infty}\mathbb{E}[X_{i}]=\infty$, then the other expression is infinite as well:

$$
\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]\geqslant\mathbb{E}\left[\sum_{i=0}^{M}X_{i}\right]=\sum_{i=0}^{M}\mathbb{E}[X_{i}]\quad\forall M
$$

We could lowerbound the sum since $X_{i}$ is a non-negative random variable and the sum is monotonically increasing in $i$, note that this argument is valid for any value $M$ that we may choose. But since even the lowerbounded sum diverges itself:

$$
\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]\geqslant\lim_{M\to\infty}\sum_{i=0}^{M}\mathbb{E}\left[X_{i}\right]=\infty
$$

And therefore $\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]=\infty$ as well, thus making the exchange not possible.

In conclusion, in a certain sense, for non-negative random variables $X_{i}$, it always holds that they share the same value:

$$
\sum_{i=0}^{+\infty}\mathbb{E}[X_{i}]=\mathbb{E}\left[\sum_{i=0}^{+\infty}X_{i}\right]
$$

No matter either that value is finite, or infinite.


Note that when we made the truncation of the sum we applied *Lebesgue’s convergence theorem*: for $X_{i}\geqslant 0$, $\sum_{i=0}^{M}X_{i}$ is monotonic in M. Therefore the exchange of the limits, i.e. $\lim_{M\to\infty}\sum_{i=0}^{M}$ and $\mathbb{E}$, is guaranteed in Lebesgues’s monotonic convergence theorem.

Recalling what we did while proving 3.3.2, the exchange was indeed valid since we were dealing with a non-negative random variable i.e. the indicator function, which can take values either 0 or 1. Because of the arguments we have just seen, the exchange was therefore valid.

We will now introduce a corollary of the just mentioned theorem 3.3.2, which states that also *recurrence* is a *class property*:

###### Corollary.

If $i\leftrightarrow j$ and if i is recurrent, then j is recurrent.

> [!note] Proof.
>
> Since $i$ and $j$ are communicating, for sure there exists two integers $m,n\geqslant 1$ s.t.
>
> $$
> P_{ij}^{(n)}>0\qquad\text{and}\qquad P_{ji}^{(m)}>0
> $$
>
> Now let $\nu\geqslant 0$ and consider, as we did for proving 3.3.1, the probability of returning in j in $(m+n+\nu)$ number of steps: $P_{jj}^{(m+n+\nu)}=\sum_{h,k}^{\infty}P_{jh}^{(m)}P_{hk}^{(\nu)}P_{kj}^{(n)}\geqslant P_{ji}^{(m)}P_{ii}^{(\nu)}P_{ij}^{(n)}$ and, on summing:
>
> $$
> \sum_{\nu=0}^{\infty}P_{jj}^{(m+n+\nu)}\geqslant\sum_{\nu=0}^{\infty}P_{ji}^{(m)}P_{ii}^{(\nu)}P_{ij}^{(n)}=P_{ji}^{(m)}P_{ij}^{(n)}\sum_{\nu=0}^{\infty}P_{ii}^{(\nu)}
> $$
>
> But we are assuming that $i$ is recurrent, then the sum $\sum_{\nu=0}^{\infty}P_{ii}^{(\nu)}$ diverges. In addition, since $P_{ij}^{(n)},P_{ji}^{(m)}>0$ the whole product in the r.h.s. diverges as well, making $\sum_{\nu=0}^{\infty}P_{jj}^{(m+n+\nu)}$ diverge itself, too, because it is bigger. We also notice that the first term $\sum_{\nu=0}^{\infty}P_{jj}^{(m+n+\nu)}$ starts at step $(m+n)$ and moreover we know it is infinite. Therefore the $\sum_{\nu=0}^{\infty}P_{jj}^{(\nu)}$ diverges being it even bigger, because this time we considered $\nu=0$ as the starting point. ∎
>
> We have just proved that recurrence, as well as periodicity, is a class property: it means that all states in a class are either recurrent or nonrecurrent.

### 3.4 Basic Limit Theorem of Markov Chains

We are finally able to formalize and *prove* the intuitive fact that the *long-run* probability of returning to a state $i$ is the *reciprocal* of the average return time $m_{i}$: that is, if the system is at $i$ every $m_{i}$ steps, then it spends $1/m_{i}$ of the total time in $i$, and so if we inspect the state at a random step (of a *infinitely long* experiment) we will find the system at $i$ with probability $1/m_{i}$. Moreover,


we will also find the appropriate conditions that are necessary for this result to hold.

Consider a recurrent state $i$. As we have seen before, the first return time $R_{i}$ can be defined as:

$$
R_{i}=\min\{n\geq i;X_{n}=i\}
$$

and is distributed according to:

$$
f_{ii}^{(n)}=\mathbb{P}\{R_{i}=n|X_{0}=i\}=\mathbb{P}\{X_{n}=i,X_{\nu}\neq i\,\forall\nu=1,\ldots,n-1|X_{0}=i\}
$$

Since the state $i$ is recurrent, $f_{ii}=\sum_{n=1}^{\infty}f_{ii}^{(n)}=1$, and so $R_{i}$ is a finite-valued random variable. In other words, $R_{i}$ can never be infinite, since the system will return to $i$ *for sure*. More precisely, the probability of $R_{i}$ being arbitrarily high *vanishes*.

The mean duration between visits to state $i$ is the expectation of $R_{i}$:

$$
m_{i}=\mathbb{E}[R_{i}|X_{0}=i]=\sum_{n=1}^{\infty}nf_{ii}^{(n)}
$$

In other words, the system *on average* returns to $i$ once every $m_{i}$ units of time.

Note that the fact that $R_{i}$ is a finite-valued random variable does not prevent $m_{i}$ from being infinite. This in fact happens if $\mathbb{P}[R_{i}=n]$ decreases *sufficiently slowly* as $n\to\infty$.

> [!abstract] Theorem 3.4.1.
>
>
> Consider a recurrent, irreducible, aperiodic Markov chain. Let $P_{ii}^{(n)}$ be the probability of entering state $i$ at the $n$-th transition, with $n\in\mathbb{N}$, given that the initial state is $i$ ($X_{0}=i$). Let $f_{ii}^{(n)}$ be the probability of first returning to state $i$ at the $n$-th transition. Then:
>
> $$
> \lim_{n\to\infty}P_{ii}^{(n)}=\frac{1}{\sum_{n=1}^{\infty}nf_{ii}^{(n)}}=\frac{1}{m_{i}}
> $$
> **Also:**
>
> $$
> \lim_{n\to\infty}P_{ji}^{(n)}=\pi_{i}=\lim_{n\to\infty}P_{ii}^{(n)}=\frac{1}{m_{i}}
> $$
>
> for all states $j$.
>
> The proof is referred to a later chapter.
>
> Note that theorem 3.4.1 can be applied also to aperiodic recurrent classes in a Markov Chain. In fact, we noted that different classes can only be linked by *one-way* transitions - meaning that after leaving a class $C$, the system cannot return in it. So a *recurrent class* must necessarily be isolate, i.e. such that
>
>
> $P_{ij}^{(n)} = 0$  for all  $i \in C$ ,  $j \notin C$ , and for all  $n$ . So we can consider the submatrix  $\| \mathbf{P}_{ij}\|$ , with  $i, j \in C$ , as the transition probability matrix of a separate irreducible Markov Chain, for which the basic limit theorem directly applies.
>
> Depending on the finiteness of  $m_{i}$ , we distinguish two cases:
>
> - If the average return time  $m_i$  is finite, then  $\lim_{n \to \infty} P_{ii}^{(n)} > 0$ , and the same applies to all states  $j \leftrightarrow i$ . This means that  $\pi_j > 0$  for every  $j$ , and so all states in the aperiodic recurrent class continue to be visited in the long run. Classes with this property are said to be positive recurrent, or strongly ergodic.
> - If  $m_i = \infty$ , then  $\pi_j = 0$  for every  $j$ , then the class is said to be null recurrent, or weakly ergodic. In a sense, this is the critical line separating transient states from recurrent ones, where the system will return to  $i$  surely, but it needs infinite time to do so.
>
> Since these are all class properties, there cannot be positive recurrent and null recurrent states in the same class. So, a state can be either transient, positive recurrent or null recurrent, with all the properties summarized in table 3.1.
>
> |  Type of State | fii=∑n=1∞f(ni)ii | limk→∞P[M>k|X0=i] | E[M|X0=i] | mi=∑n=1∞nf(ni)ii | πi=1/mi  |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> |  Transient | <1 | 0 | fii/1-fii<∞ | ∞ | 0  |
> |  Null Recurrent | 1 | 1 | ∞ | ∞ | 0  |
> |  Positive Recurrent | 1 | 1 | ∞ | <∞ | >0  |
>
> Table (3.1) - Summary of the main properties for the different categories of states.  $f_{ii}$  is the probability of returning to  $i$ ,  $M$  is the number of returns to  $i$ ,  $m_i$  the average time between returns and  $\pi_i$  the probability of the system being in  $i$  in the long run.
>
> A positive recurrent aperiodic class behaves, when taken by itself, the same as a regular Markov chain, and so the same result about the limiting distribution still holds:

> [!abstract] Theorem 3.4.2. Limit distribution of a positive recurrent aperiodic class.
>
> In a positive recurrent aperiodic class with states  $j \in \mathbb{N}$ , we have:
>
> $$
> \lim  _ {n \rightarrow \infty} P _ {j j} ^ {(n)} = \pi_ {j} = \sum_ {i = 0} ^ {\infty} \pi_ {i} P _ {i j} \quad \sum_ {i = 0} ^ {\infty} \pi_ {i} = 1
> $$
>
> and  $\pi$  is uniquely determined by the set of equations:
>
> $$
> \pi_ {i} \geq 0, \sum_ {i = 0} ^ {\infty} \pi_ {i} = 1 \quad \pi_ {j} = \sum_ {i = 0} ^ {\infty} \pi_ {i} P _ {i j} \quad j \in \mathbb {N} \tag {3.7}
> $$
>
> In general, any set  $(\pi_i)_{i=0}^{\infty}$  satisfying (3.7) is called a stationary probability distribution.
>
>
> Note, however, that theorem 3.4.2 is actually more general than the result we got for regular Markov chain, as here we are not assuming a *finite* number of states. In fact, we cannot employ the same proof - because there we needed to exchange the order of two sums, which needs justification in the infinite case. Of course, we could use Fubini’s theorem to generalize the previous arguments, but in this case is actually more instructive to restart from first principles.

> [!note] Proof.
>
> As before, we need to prove two things: that the limiting probabilities $\pi_{j}$ are indeed the solution of (3.7), and that this solution is unique.
>
> Existence:
>
> 1. We start from the normalization condition for rows in the $n$-step transition matrix:
>
> $$
> 1=\sum_{j=0}^{+\infty}P_{ij}^{(n)}\qquad\forall n
> $$
>
> Since all the addends are non-negative, the total sum cannot be lower than any *truncated* sum:
>
> $$
> 1=\sum_{j=0}^{+\infty}P_{ij}^{(n)}\geq\sum_{j=0}^{M}P_{ij}^{(n)}\qquad\forall n,M
> $$
>
> We then take the limit $n\to\infty$, and bring it inside the sum, since it is over a *finite* number of elements:
>
> $$
> 1\geq\lim_{n\to\infty}\sum_{j=0}^{M}P_{ij}^{(n)}=\sum_{j=0}^{M}\lim_{n\to\infty}P_{ij}^{(n)}=\sum_{j=0}^{M}\pi_{j}\qquad\forall M
> $$
>
> Finally we take also the $M\to\infty$ limit, leading to:
>
> $$
> \lim_{M\to\infty}\sum_{j=0}^{M}\pi_{j}=\sum_{j=0}^{+\infty}\pi_{j}\leq 1
> $$
>
> So we have found that the sum of $\pi_{j}$ converges. Clearly, we would like to prove that it is *exactly* $1$.
> 2. Again we start from a known relationship:
>
> $$
> P_{ij}^{(m+n)}=\sum_{k=0}^{+\infty}P_{ik}^{(m)}P_{kj}^{(n)}\qquad\forall m,n
> $$
>
> Again we can truncate the sum to write an inequality:
>
> $$
> P_{ij}^{(m+n)}\geq\sum_{k=0}^{M}P_{ik}^{(m)}P_{kj}^{(n)}\qquad\forall m,n,M
> $$
>
>
> Taking the limit $m\to\infty$ and taking it into the finite sum:
>
> $$
> \pi_{j}=\lim_{m\to\infty}P_{ij}^{(m+n)}\geq\lim_{m\to\infty}\sum_{k=0}^{M}P_{ik}^{(m)}P_{kj}^{(n)} =\sum_{k=0}^{M}\lim_{m\to\infty}P_{ik}^{(m)}P_{kj}^{(n)}=
> =\sum_{k=0}^{M}\pi_{k}P_{kj}^{(n)}\quad\forall M,n
> $$
>
> Finally, we take also $M\to\infty$, leading to:
>
> $$
> \pi_{j}\geq\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}\qquad\forall n
> $$
> 3. We want to show that (3.9) hold as an equality, and we do this by contradiction. Suppose that there exist an index $j$ for which (3.9) holds *strictly*:
>
> $$
> \exists j\colon\pi_{j}>\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}
> $$
>
> Summing over $j$, the inequality remains strict:
>
> $$
> \sum_{j=0}^{+\infty}\pi_{j}>\sum_{j=0}^{+\infty}\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}
> $$
>
> Let’s evaluate this last sum. Again, we first *truncate* the inner sum to the first $M$ elements, so that we can exchange the two sums and obtain an inequality that remains valid also in the limit $M\to\infty$:
>
> $$
> \sum_{j=0}^{+\infty}\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}\geq\sum_{j=0k=0}^{+\infty}\sum_{k=0}^{M}\pi_{k}P_{kj}^{(n)}=\sum_{k=0}^{M}\pi_{k}\sum_{j=0}^{+\infty}P_{kj}^{(n)}=\sum_{k=0}^{M}\pi_{k}\quad\forall M
> $$
>
> And in particular:
>
> $$
> \sum_{j=0}^{+\infty}\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}\geq\lim_{M\to\infty}\sum_{k=0}^{M}\pi_{k}=\sum_{k=0}^{+\infty}\pi_{k}
> $$
>
> Substituting in (3.10) we get:
>
> $$
> \sum_{j=0}^{+\infty}\pi_{j}>\sum_{j=0}^{+\infty}\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}\geq\sum_{k=0}^{+\infty}\pi_{k}
> $$
>
> which is absurd, as no quantity can be strictly greater than itself. So, by contradiction it must be:
>
> $$
> \pi_{j}=\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}\quad\forall n
> $$
>
>
> Setting $n=1$ we obtain part of the thesis we wish to prove.
> 4. All that’s left is to deal with the normalization property, i.e. show that (3.8) holds as an equality.
>
> First, note that $|P_{kj}^{(n)}|\leq 1$ $\forall n$ (they are uniformly bounded). This, along with the convergence of $\sum_{k=0}^{+\infty}\pi_{k}\leq 1$ (3.8) allows to bring the limit inside the sum in the following:
>
> $$
> \pi_{j}=\lim_{n\to\infty}\sum_{k=0}^{+\infty}\pi_{k}P_{kj}^{(n)}=\sum_{k=0}^{+\infty}\pi_{k}\lim_{n\to\infty}P_{kj}^{(n)}=\left(\sum_{k=0}^{+\infty}\pi_{k}\right)\pi_{j}
> $$
>
> Since $\pi_{j}>0$ (because the chain is positive recurrent by hypothesis), we can divide both sides by $\pi_{j}$, leading to:
>
> $$
> \sum_{k=0}^{+\infty}\pi_{k}=1
> $$
>
> This finally proves the existence of the solution of (3.7).
>
> Uniqueness.
> Let $\boldsymbol{x}$ be a solution, i.e. such that:
>
> $$
> x_{j}=\sum_{i=0}^{+\infty}x_{i}P_{ij};\qquad\sum_{i=0}^{+\infty}x_{i}=1
> $$
>
> We then proceed as we did for regular MC$s$, rewriting the $x_{i}$ in the rhs of (3.11) by using (3.11) itself. Then we apply again the trick of truncating the inner sum to exchange the sums:
>
> $$
> x_{j} =\sum_{i=0}^{+\infty}\left(\sum_{k=0}^{+\infty}\pi_{k}P_{ki}\right)P_{ij}\geq\sum_{i=0}^{+\infty}\left(\sum_{k=0}^{M}x_{k}P_{ki}\right)P_{ij}=
> =\sum_{k=0}^{M}x_{k}\sum_{i=0}^{+\infty}P_{ki}P_{ij}=\sum_{k=0}^{M}x_{k}P_{kj}^{(2)}\quad\forall M
> $$
>
> And this holds also in the limit $M\to\infty$. Therefore:
>
> $$
> x_{j}\geq\sum_{k=0}^{+\infty}x_{k}P_{kj}^{(2)}
> $$
>
> And by iterating this argument:
>
> $$
> x_{j}\geq\sum_{k=0}^{+\infty}x_{k}P_{kj}^{(n)}\qquad\forall n
> $$
>
> To prove that this is indeed an equality, we proceed as in point 3 of the previous proof, and assume that there is an index $j$ for which (3.12) is strict. By a similar
>
>
> reasoning, this leads to a contradiction:
>
> $$
> \sum_{j=0}^{+\infty}x_{j}>\sum_{k=0}^{+\infty}x_{k}
> $$
>
> Therefore (3.12) must hold as an equality:
>
> $$
> x_{j}=\sum_{k=0}^{+\infty}x_{k}P_{kj}^{(n)}\qquad\forall n
> $$
>
> Finally, letting $n\to\infty$ and using the same argument as in point 4 to bring the limit inside the sum:
>
> $$
> x_{j}=\lim_{n\to\infty}\sum_{k=0}^{+\infty}x_{k}P_{kj}^{(n)}=\sum_{k=0}^{+\infty}x_{k}\lim_{n\to\infty}P_{kj}^{(n)}=\left(\sum_{k=0}^{+\infty}x_{k}\right)\pi_{j}
> $$
>
> and since $\sum_{k=0}^{+\infty}x_{k}=1$ we have $x_{j}=\pi_{j}$, thus concluding the proof. ∎
>
> Solving (3.7) suffices to say that an aperiodic Markov chain is positive recurrent. Conversely, proving that (3.7) does not admit solutions, means that the aperiodic Markov chain is not positive recurrent.
>
> For a general Markov chain, however, a stationary distribution is not necessarily the same as the limiting distribution. In fact, if a limiting distribution exists, then it is stationary (i.e. it is the solution of (3.7)), but the converse is not true: sometimes (3.7) can be solved, but the Markov chain is periodic and so that solution is clearly not the limiting distribution (that does not exist).
>
> The simplest example of this kind of behaviour is given by:
>
> $$
> \mathbf{P}=\begin{bmatrix}0&1\\
> 1&0\end{bmatrix}
> $$
>
> This is a non-regular Markov chain that always cycles between states $0$ and $1$, thus presenting no limiting distribution. However it admits a stationary distribution, which is $\boldsymbol{\pi}=(1/2,1/2)^{T}$. In fact:
>
> $$
> \left(\begin{array}[]{cc}\frac{1}{2}&\frac{1}{2}\end{array}\right)\times\begin{bmatrix}0&1\\
> 1&0\end{bmatrix}=\left(\begin{array}[]{cc}\frac{1}{2}&\frac{1}{2}\end{array}\right)
> $$

> [!example] Example 6 (Stationary distribution for a random walk)
>
> Consider the following random walk:
>
> $$
> \mathbf{P}=\begin{bmatrix}0&1&0&\cdots&\cdots\\
> q_{1}&0&p_{1}&\cdots&\cdots\\
> 0&q_{2}&0&p_{2}&\cdots\\
> \vdots&\ddots&\ddots&\ddots&\ddots\end{bmatrix}
> $$
>
>
> $q_{i},p_{i}>0$, then the chain is irreducible, with $d(i)=2$ (to return to the same state $i$, we need an equal number of steps in one direction, and in the opposite one, thus all $P^{(n)}_{ii}$ with $n$ odd are $0$). So it is not aperiodic, meaning that theorem 3.4.2 cannot be applied. However, there is a stationary distribution, i.e. we can solve:
>
> $$
> \mbox{\boldmath }=\mbox{\boldmath }\mbox{\boldmath }\Leftrightarrow x_{i}=\sum_{j=0}^{+\infty}x_{j}P_{ji}=p_{i-1}x_{i-1}+q_{i+1}x_{i+1}\qquad i>0 (3.13)
> $$
>
> under the normalization:
>
> $$
> \sum_{i=0}^{+\infty}x_{i}=1
> $$
>
> and with $p_{0}=1$, and $x_{0}=q_{1}x_{1}$.
>
> Recall that we previously solved a similar equation while doing first-step analysis:
>
> $$
> \mbox{\boldmath }=\mbox{\boldmath }\mbox{\boldmath } (3.14)
> $$
>
> However we cannot directly apply the same method, as in (3.14) $\mathbf{P}$ multiplies the vector from the left and not from the right as in (3.13).
>
> However, the idea is similar. We start by solving the first equation:
>
> $$
> x_{0}=q_{1}x_{1}\Rightarrow x_{1}=\frac{x_{0}}{q_{1}}
> $$
>
> And substitute in the second one:
>
> $$
> x_{1}=x_{0}+q_{2}x_{2}\Rightarrow x_{2}=\frac{x_{1}-x_{0}}{q_{2}}=\frac{\left(1-q_{1}\right)\ x_{1}}{q_{2}}=\frac{p_{1}x_{0}}{q_{1}q_{2}}
> $$
>
> where we used the row-normalization of $\mathbf{P}$, for which $p_{i}+q_{i}=1$.
> Repeating one more time:
>
> $$
> x_{2}=p_{1}x_{1}+q_{3}x_{3}\Rightarrow x_{3}=\frac{x_{2}-p_{1}x_{1}}{q_{3}}\underset{(3.15)}{=}\frac{p_{1}x_{1}(1-q_{2})}{q_{2}q_{3}}=\frac{p_{1}p_{2}x_{0}}{q_{1}q_{2}q_{3}}
> $$
>
> From that we can guess the form of the general solution:
>
> $$
> x_{i}=x_{0}\frac{p_{i-1}p_{i-2}\cdots p_{1}}{q_{i}q_{i-1}\cdots q_{1}}\underset{p_{0}=1}{=}x_{0}\prod_{k=0}^{i-1}\frac{p_{k}}{q_{k+1}}\qquad i>0
> $$
>
> and substitute it back in (3.13) to check if it is right:
>
> $$
> p_{i-1}x_{i-1}+q_{i+1}x_{i+1} =p_{i-1}\frac{p_{i-2}\cdots p_{1}}{q_{i-1}\cdots q_{1}}+q_{i+1}\frac{p_{i}\cdots p_{1}}{q_{i+1}\cdots q_{1}}=
> =\frac{p_{i-1}\cdots p_{1}}{q_{i}\cdots q_{1}}\underbrace{(q_{i}+p_{i})}_{1}=x_{i}
> $$
>
>
> All that's left is to fix the value of  $x_0$  by imposing the normalization:
>
> $$
> \sum_ {i = 0} ^ {+ \infty} x _ {i} = x _ {0} \sum_ {i = 0} ^ {+ \infty} \prod_ {k = 0} ^ {i - 1} \frac {p _ {k}}{q _ {k + 1}} = 1 \Rightarrow x _ {0} = \left(\sum_ {i = 0} ^ {+ \infty} \prod_ {k = 0} ^ {i - 1} \frac {p _ {k}}{q _ {k + 1}}\right) ^ {- 1} \tag {3.17}
> $$
>
> (with the convention that a product with no elements is equal to 1, the neutral element of the product:  $\prod_{k=0}^{0}(\dots) = 1$ ).
>
> The stationary solution (3.16) exists only if the infinite sum in (3.17) converges to a non-zero finite value. If it were diverging, then  $x_0 = 0$ , and so all  $x_i = 0 \forall i$ , meaning that the normalization constraint is not respecting.
>
> Suppose that  $p_k \equiv p$  and  $q_k \equiv q$ , i.e. the probabilities of moving in one or the other direction are independent of the system's state. In this case we can directly inspect the convergence of the sum in (3.17):
>
> - If  $p < q$ , the sum converges, and the chain is positive recurrent. Intuitively, in this case the system "tends to return over its steps", thus visiting the same states over and over.
> - If  $p \geq q$ , the sum diverges and no solution exists, meaning that the chain is not positive recurrent. Intuitively, in this case the system tends to "escape" towards infinity, always visiting new transient states.
>
> ![[Stochastic_Processes_2020_p88_img25.jpeg]]
> Figure (3.6) - Block diagram for the success run Markov Chain

> [!example] Example 7 (Recurrence of success runs)
>
> Consider now the following Markov chain, describing the success runs of a sequence of binomial trials:
>
> $$
> \mathbf {P} = \left| \left| \begin{array}{c c c c c} p _ {0} & 1 - p _ {0} & 0 & 0 & \dots \\ p _ {1} & 0 & 1 - p _ {1} & 0 & \dots \\ p _ {1} & 0 & 0 & 1 - p _ {2} & \dots \\ \vdots & \ddots & \ddots & \ddots & \ddots \end{array} \right| \right| \quad (0 <   p _ {k} <   1)
> $$
>
> with the block diagram shown in figure 3.6. Clearly the chain is irreducible, and so all states are of the same type, meaning that to study their recurrence we can focus on only one of them, for example the 0-th.
>
>
> So, let’s define the first return time $R_{0}$ to state 0:
>
> $$
> R_{0}=\min\{n\geq 1;X_{n}=0\}
> $$
>
> By just observing the diagram in fig. 3.6 we can compute the statistics of $R_{0}$:
>
> $$
> \mathbb{P}\{R_{0}>1|X_{0}=0\}=(1-p_{0})
> \mathbb{P}\{R_{0}>2|X_{0}=0\}=(1-p_{0})(1-p_{1})
> \mathbb{P}\{R_{0}>3|X_{0}=0\}=(1-p_{0})(1-p_{1})(1-p_{2})
> $$
>
> In fact the probability $\mathbb{P}\{R_{0}>i|X_{0}=0\}$ of returning to 0 for the first time after $i$ steps is equivalent to the probability of not returning to 0 for $i$ consecutive steps, which is necessarily the probability of travelling through states $1,\ldots,i$, as this is the only possible path that does not return to 0. So:
>
> $$
> \mathbb{P}\{R_{0}>k|X_{0}=0\}=(1-p_{0})(1-p_{1})\cdots(1-p_{k-1})=\prod_{i=0}^{k-1}(1-p_{i})
> $$
>
> Then note that:
>
> $$
> f_{00}^{(n)}=\mathbb{P}\{R_{0}=n|X_{0}=0\}\Rightarrow\mathbb{P}\{R_{0}>k|X_{0}=0\}=1-\sum_{n=1}^{k}f_{00}^{(n)}
> $$
>
> and rearranging:
>
> $$
> \sum_{n=1}^{k}f_{00}^{(n)}=1-\mathbb{P}\{R_{0}>k|X_{0}=0\}=1-\prod_{i=0}^{k-1}(1-p_{i})
> $$
>
> By definition, state 0 is recurrent if the sum in (3.19) is 1 for $k\to\infty$, i.e. if:
>
> $$
> \lim_{k\to\infty}\prod_{i=0}^{k-1}(1-p_{i})=\prod_{i=0}^{\infty}(1-p_{i})=0
> $$
>
> (3.20) is equivalent to:
>
> $$
> \sum_{i=0}^{\infty}p_{i}=\infty
> $$
>
> by the application of lemma 3.4.3.
>
> State 0 is positive recurrent when the average return time $m_{0}=\mathbb{E}[R_{0}|X_{0}=0]$ is finite:
>
> $$
> m_{0}=\sum_{k=0}^{\infty}\mathbb{P}\{R_{0}>k|X_{0}=0\}=
> \underset{(3.18)}{=}1+\sum_{k=1}^{\infty}\prod_{i=0}^{k-1}(1-p_{i})
> $$
>
>
> And $m<\infty$ only if:
>
> $$
> \sum_{k=1}^{\infty}\prod_{i=0}^{k-1}(1-p_{i})<\infty
> $$
>
> which is a *stronger* requirement than (3.19), as expected. In this case, we can compute the stationary probability $\pi_{0}$ as the reciprocal of $m_{0}$:
>
> $$
> \pi_{0}=\frac{1}{m_{0}}=\frac{1}{1+\sum_{k=1}^{\infty}\prod_{i=0}^{k-1}(1-p_{i})}
> $$
>
> And then derive all the other stationary probabilities from the equations for the stationary distribution:
>
> $$
> (1-p_{0})\pi_{0} =\pi_{1}
> (1-p_{1})\pi_{1} =\pi_{2}
> (1-p_{2})\pi_{2} =\pi_{3}
> \vdots
> $$
>
> leading to:
>
> $$
> \pi_{1} =(1-p_{0})\pi_{0}
> \pi_{2} =(1-p_{1})\pi_{1}=(1-p_{1})(1-p_{0})\pi_{0}
> \pi_{3} =(1-p_{2})\pi_{2}=(1-p_{2})(1-p_{1})(1-p_{0})\pi_{0}
> $$
>
> And in general:
>
> $$
> \pi_{k}=\pi_{0}\prod_{i=0}^{k-1}(1-p_{i})\qquad k\geq 1
> $$
>
> In the special case where all the $p_{i}$ are equal to a constant $p=1-q$, then:
>
> $$
> \prod_{i=0}^{k-1}(1-p_{i})=q^{k}\Rightarrow m_{0}=1+\sum_{k=1}^{\infty}q^{k}=\frac{1}{p}
> $$
>
> and $\pi_{k}=pq^{k}$ for $k\in\mathbb{N}$.

> [!abstract] Theorem 3.4.3.
>
> If $0<p_{i}<1$, $i\in\mathbb{N}$, then:
>
> $$
> u_{m}=\prod_{i=0}^{m}(1-p_{i})\xrightarrow[m\to\infty]{}0\Leftrightarrow\sum_{i=0}^{\infty}p_{i}=\infty
> $$

> [!note] Proof.
>
> Suppose that:
>
> $$
> \sum_{i=0}^{\infty}p_{i}=\infty
> $$
>
>
> Then:
>
> $$
> 1-p_{i}<1-p_{i}+\frac{p_{i}^{2}}{2!}-\frac{p_{i}^{3}}{3!}+\cdots=e^{-p_{i}}\qquad i\in\mathbb{N}
> $$
>
> In fact $y=1-x$ is the tangent of $y=e^{-x}$ at $x=0$, and because $e^{-x}$ is convex, it is always higher than its tangents.
> Since (3.22) holds for any $i$, it holds also for the product:
>
> $$
> \prod_{i=0}^{m}(1-p_{i})<\exp\left(-\sum_{i=0}^{m}p_{i}\right)\xrightarrow[n\to\infty]{(3.21)}0
> $$
>
> And so we have proved:
>
> $$
> \sum_{i=0}^{\infty}p_{i}=\infty\Rightarrow\prod_{i=0}^{\infty}(1-p_{i})=0
> $$
>
> To prove the converse, we assume:
>
> $$
> \lim_{m\to\infty}\prod_{i=0}^{m}(1-p_{i})=0
> $$
>
> Then we make use of the following inequality:
>
> $$
> \prod_{i=j}^{m}(1-p_{i})>(1-p_{j}-p_{j+1}-\cdots-p_{m})=1-\sum_{i=j}^{m}p_{i}\qquad m\geq j+1
> $$
>
> which can be proved by induction. It holds for $m=j+1$:
>
> $$
> (1-p_{j})(1-p_{j+1})=1-p_{j}-p_{j+1}+p_{j}p_{j+1}>1-p_{j}-p_{j+1}
> $$
>
> because all the $p_{k}$ are non-zero, and so $p_{j}p_{j+1}>0$.
> So, assuming it holds for $m$, we can prove that it holds for $m+1$:
>
> $$
> \prod_{i=j}^{m+1}(1-p_{i}) =(1-p_{m+1})\prod_{i=j}^{m}(1-p_{i})\underset{(3.24)}{\geq}(1-p_{m+1})\left(1-\sum_{i=j}^{m}p_{i}\right)=
> =1-\sum_{i=j}^{m}p_{i}-p_{m+1}+\underbrace{p_{m+1}\sum_{i=j}^{m}p_{i}}_{>0}>1-\sum_{i=j}^{m+1}p_{i}
> $$
>
> and so it is true for every $m$.
> Then we proceed by contradiction. Suppose that the sum (3.21) actually converges:
>
> $$
> \sum_{i=0}^{\infty}p_{i}<\infty
> $$
>
>
> This means that the tail sum must vanish:
>
> $$
> \lim_{j\to\infty}\sum_{i=j}^{\infty}p_{i}=0
> $$
>
> So it must become arbitrarily small, and in particular it must be *definitely* between $0$ and $1$:
>
> $$
> \exists j_{0}>1\text{ s.t. }0<\sum_{i=j}^{\infty}p_{i}<1\quad\forall j>j_{0}
> $$
>
> But in that case, applying (3.24) leads to:
>
> $$
> \lim_{m\to\infty}\prod_{i=j}^{m}(1-p_{i})>\lim_{m\to\infty}\Bigg{(}1-\underbrace{\sum_{i=j}^{m}p_{i}}_{<1}\Bigg{)}>0
> $$
>
> Now note that the lhs of (3.27) differs from (3.23) by only a finite number of non-zero factors (because the $p_{i}\neq 1$). So:
>
> $$
> \lim_{m\to\infty}\prod_{i=j}^{m}(1-p_{i})>0\Rightarrow\lim_{m\to\infty}\prod_{i=0}^{\infty}(1-p_{i})>0
> $$
>
> But this contradicts our hypothesis (3.23), meaning that (3.25) cannot be true, and so:
>
> $$
> \prod_{i=0}^{\infty}(1-p_{i})=0\Rightarrow\sum_{i=0}^{\infty}p_{i}=\infty
> $$
>
> which concludes the proof.
>
> ∎
>
> ###### Example 8 (Recurrence of G/M/1 queue):
>
> Let’s now examine when the G/M/1 queue is positive recurrent. We already computed the transition probabilities in (2.4) at page 36:
>
> $$
> P_{i,i+1-j} =\int_{0}^{\infty}e^{-\mu t}\frac{(\mu t)^{j}}{j!}\,\mathrm{d}G(t)\qquad j=0,1,\ldots,i
> P_{i0} =\int_{0}^{\infty}\sum_{k=i+1}^{\infty}e^{-\mu t}\frac{(\mu t)^{k}}{k!}\,\mathrm{d}G(t)\qquad i\geq 0
> $$
>
> The chain is irreducible, meaning that all states are in the same class, and also aperiodic. So, to prove positive recurrence, we just need to solve the stationarity equation:
>
> $$
> \pi_{k}=\sum_{i}\pi_{i}P_{ik}\quad k\geq 0\qquad\sum_{k}\pi_{k}=1
> $$
>
>
> which in this case becomes:
>
> $$
> \pi_{k}=\sum_{i=k-1}^{\infty}\pi_{i}\int_{0}^{\infty}e^{-\mu t}\frac{(\mu t)^{i+1-k}}{(i+1-k)!}\,\mathrm{d}G(t)\quad k\geq 1\qquad\sum_{k=0}^{\infty}\pi_{k}=1
> $$
>
> We ignore the case $k=0$, which is more complicated, as we will be able to compute $\pi_{0}$ by imposing normalization.
>
> To solve (3.28) we use the ansatz $\pi_{k}=c\beta^{k}$, leading to:
>
> $$
> c\beta^{k}=c\sum_{i=k-1}^{\infty}\beta^{i}\int_{0}^{\infty}e^{-\mu t}\frac{(\mu t)^{i+1-k}}{(i+1-k)!}\,\mathrm{d}G(t)=
> $$
>
> We exchange the integral and the sum (which is allowed because we are dealing with all non-negative terms, meaning that the partial sums are monotone functions, and we can apply Lebesgue’s monotone convergence theorem). We also split $\beta^{i}$ in two factors, bringing one inside the inner sum, constructing an exponential:
>
> $$
> =c\int_{0}^{\infty}e^{-\mu t}\beta^{k-1}\sum_{i=k-1}^{\infty}\frac{(\beta\mu t)^{i+1-k}}{(i+1-k)!}\;\mathrm{d}G(t)=
> =c\int_{0}^{\infty}e^{-\mu t}\beta^{k-1}\ e^{\beta\mu t}\ \mathrm{d}G(t)
> $$
>
> Rearranging:
>
> $$
> \beta=\int_{0}^{\infty}e^{-\mu t(1-\beta)}\,\mathrm{d}G(t)
> $$
>
> Note that this result does not depend on $k$ - so if we find a solution for $\beta$ such that $\pi_{k}=c\beta^{k}$ is normalizable we would have the entire stationary distribution, proving positive recurrence.
>
> Clearly it must be $0<\beta<1$, otherwise $\sum_{k}\pi_{k}=\sum_{k}c\beta^{k}$ would either be $0$ or diverge.
>
> We rewrite (3.29) as follows:
>
> $$
> \beta=\int_{0}^{+\infty}e^{-\mu t(1-\beta)}\,\mathrm{d}G(t)=\mathbb{E}[e^{-\mu T(1-\beta)}]=A(\beta)
> $$
>
> and study the intersections of the curves $y=\beta$ and $y=A(\beta)$.
>
> First we examine the two extrema:
>
> $$
> A(0)=\int_{0}^{+\infty}e^{-\mu t}\,\mathrm{d}G(t)>0
> A(1)=\int_{0}^{+\infty}\mathrm{d}G(t)=1
> $$
>
> Then the first two derivatives:
>
> $$
> A^{\prime}(\beta)=\int_{0}^{+\infty}\mu te^{-\mu t(1-\beta)}\,\mathrm{d}G(t)>0\qquad\forall\beta
> A^{\prime\prime}(\beta)=\int_{0}^{+\infty}(\mu t)^{2}e^{-\mu t(1-\beta)}\,\mathrm{d}G(t)>0\qquad\forall\beta
> $$
>
>
> Summarizing, $A(\beta)$ is strictly increasing and convex, and goes from $(0,A(0))$ with $A(0)>0$ to $(1,1)$.
>
> So, with respect to $y=\beta$, there are only two possible behaviours, as illustrated in fig. 3.7:
>
> 1. $A(\beta)$ reaches $(1,1)$ “from above”, i.e. $A^{\prime}(1)<1$, meaning that:
>
> $$
> A^{\prime}(1)=\mu{\rm I\kern-1.79993ptE}[T]=\frac{\mu}{\lambda}<1\Leftrightarrow\lambda>\mu
> $$
>
> where $\lambda=1/{\rm I\kern-1.79993ptE}[T]$ is the arrival rate in the queue.
>
> In this case there are no intersections with $y=\beta$ except the trivial one at $(1,1)$, which is not acceptable (because we need $0<\beta<1$). Thus (3.29) has no solutions.
>
> Note that this does not prove that the chain is not positive recurrent, but only that the ansatz we started from is not valid. However, from other considerations, we know that the Markov chain is transient for $\lambda>\mu$ - because more people arrive than depart, and so the system’s state in the long run will “escape towards infinity”.
> 2. $A(\beta)$ reaches $(1,1)$ from below, i.e. $A^{\prime}(1)>1$. This happens if:
>
> $$
> A^{\prime}(1)=\mu{\rm I\kern-1.79993ptE}[T]=\frac{\mu}{\lambda}>1\Leftrightarrow\lambda<\mu
> $$
>
> In this case there is a non-trivial intersection with $y=\beta$, which is denoted as $\beta^{*}\in(0,1)$. This is a valid solution for (3.29), thus proving both that our ansatz was valid, and that the chain is positive recurrent.
>
> This case corresponds to an arrival rate $\lambda$ that is less than that one of departures, and so intuitively we expect the system to be stable, returning over and over to the same “low” states.
>
> In summary: we started with the stationarity equation (3.28), introduced an ansatz leading to the integral equation (3.29), for which we have found a solution in the case $\lambda<\mu$.
>
> As the chain is irreducible and aperiodic, if a stationary solution exists then it is unique, and corresponds to the limiting distribution. So, the solution we have found by guessing its form is rigorous, and it’s the only correct solution in its domain.
>
> However, outside that domain, we can only say that the ansatz was not useful, and we need to employ other methods to actually draw any conclusion about the chain’s recurrence.
>
> Finally, we spend some words on the critical case $\lambda=\mu$, with $A^{\prime}(1)=1$. Here there is a double intersection with $y=\beta$ at $(1,1)$, and so (3.29) has no solution, and we cannot draw any conclusion with our method.
>
> However, it can be shown that in this case the chain is null recurrent. So:
>
> - $\lambda<\mu$: chain is positive recurrent (or stable)
>
>
> - $\lambda = \mu$: chain is null recurrent
> - $\lambda > \mu$: chain is transient (or unstable)
>
> ![[Stochastic_Processes_2020_p95_img26.jpeg]]
> Figure (3.7) – There are only two possible behaviours for $A(\beta)$, resulting in either 0 or exactly 1 intersections with $y = \beta$.

## 3.4.1 Periodic generalization

We proved the existence of a limiting distribution for irreducible, positive recurrent, aperiodic Markov chains. In the periodic case, clearly the limiting distribution cannot exist:

$$
\breve{\Delta} \lim_{n \to \infty} P_{ij}^{(n)}
$$

However, we can inspect $P_{ij}^{(n)}$ only for $n$ that are multiples of the period $d$ of the chain. In this case, it can be shown that:

$$
\lim_{n \to \infty} P_{ii}^{(nd)} = \frac{d}{m_i}
$$

We can always consider the mean time that the system spends in state $i$, and define a "limiting distribution" as follows:

$$
\lim_{n \to \infty} \frac{1}{n} \sum_{m = 0}^{n - 1} P_{ii}^{(m)} \equiv \pi_i = \frac{1}{m_i} \tag{3.30}
$$

In fact now the sum is over all states, also the ones that are non-multiples of $d$. However, by periodicity we know that $P_{ii}^{n} = 0$ if $n$ is not a multiple of $d$, while $P_{ii}^{(nd)} \xrightarrow[n \to \infty]{} d / m_i$. So, during a single period from $1 \to d$, we find null values for $d - 1$ terms because we can not be in the $i$-th state before the period ends, and $d / m_i$ for the last one, leading to an average of exactly $1 / m_i$.

Again, the $\pi_j$ so defined can be found as the unique nonnegative solution to


the stationarity equations:

$$
\pi_ {j} = \sum_ {k = 0} \pi_ {k} P _ {k j} \qquad \sum_ {j = 0} ^ {\infty} \pi_ {j} = 1
$$

## 3.5 Reducible Markov chains

While most Markov chains encountered in stochastic modelling are irreducible, sometimes it can happen to deal with a reducible case.

One such example is the following:

$$
\mathbf {P} = \left\| \begin{array}{c c c c} \frac {1}{2} & \frac {1}{2} & 0 & 0 \\ \frac {1}{4} & \frac {3}{4} & 0 & 0 \\ 0 & 0 & \frac {1}{3} & \frac {2}{3} \\ 0 & 0 & \frac {2}{3} & \frac {1}{3} \end{array} \right\| = \left\| \begin{array}{c c} \mathbf {P} _ {1} & \mathbf {O} \\ \mathbf {O} & \mathbf {P} _ {2} \end{array} \right\| \qquad \mathbf {P} _ {1} = \left\| \begin{array}{c c} \frac {1}{2} & \frac {1}{2} \\ \frac {1}{4} & \frac {3}{4} \end{array} \right\|; \mathbf {P} _ {2} = \left\| \begin{array}{c c} \frac {1}{3} & \frac {2}{3} \\ \frac {2}{3} & \frac {1}{3} \end{array} \right\|
$$

This chain contains two isolate classes, which can be modelled as two separate chains with transition matrices  $\mathbf{P}_1$  and  $\mathbf{P}_2$ . Their evolution can be completely separated, and in fact:

$$
\mathbf {P} ^ {n} = \left\| \begin{array}{c c} \mathbf {P} _ {1} ^ {n} & \mathbf {O} \\ \mathbf {O} & \mathbf {P} _ {2} ^ {n} \end{array} \right\|
$$

In general, however, one-way transitions between different classes can happen.

We can apply the basic limit theorem to any aperiodic recurrent class in a reducible Markov chain. As we previously noted, a recurrent class must be isolate from the others, meaning that if  $i$  is in that class and  $j$  in another, then  $P_{ij}^{(n)} = 0 \forall n$ . On the other hand, for states in the same class we have, in the long run:

$$
\lim  _ {n \rightarrow \infty} P _ {i j} ^ {(n)} = \frac {1}{m _ {j}} \geq 0 \tag {3.31}
$$

If a class is transient, then the system will stay in it for a finite time, and then leave it and never return. So, for any transient state  $j$  we have:

$$
\lim  _ {n \rightarrow \infty} P _ {i j} ^ {(n)} = 0 \quad \forall i \tag {3.32}
$$

Summarizing, (3.31) covers transitions between recurrent states, and (3.32) the ones to a transient state.

The only remaining case to examine is that of a starting transient state  $i$ , and final recurrent state  $j$ .


Let's see what happens with an example:

$$
\mathbf {P} = \left. \begin{array}{c c c c c} 0 & 0 & 1 & 2 & 3 \\ 0 & \frac {1}{2} & \frac {1}{2} & 0 & 0 \\ 1 & \frac {1}{4} & \frac {3}{4} & 0 & 0 \\ 2 & \frac {1}{4} & \frac {1}{4} & \frac {1}{4} & \frac {1}{4} \\ 3 & 0 & 0 & 0 & 1 \end{array} \right| \tag {3.33}
$$

There are three classes:  $A = \{0,1\}$ ,  $B = \{2\}$  and  $C = \{3\}$ .

Looking at the block diagram in fig. 3.8, we can see that:

- If the system starts in  $A$ , it will remain there forever. Note that  $A$  is aperiodic, because of the non-zero probabilities of same-state transitions  $0 \to 0$  and  $1 \to 1$ .

We can then search for the stationary distribution:

$$
\pi_ {j} = \sum_ {i = 0} ^ {1} \pi_ {i} P _ {i j} \quad j = 0, 1 \qquad \pi_ {0} + \pi_ {1} = 1
$$

leading to the following system of equations:

$$
\left\{ \begin{array}{l} \pi_ {0} = \pi_ {0} \cdot \frac {1}{2} + \pi_ {1} \cdot \frac {1}{4} \\ \pi_ {1} = \pi_ {0} \cdot \frac {1}{2} + \pi_ {1} \cdot \frac {3}{4} \end{array} \right.
$$

We need to solve only one of them, and then impose the normalization:

$$
\pi_ {0} = \frac {\pi_ {1}}{2} \wedge \pi_ {0} + \pi_ {1} = 1 \Rightarrow \pi_ {0} = \frac {1}{3} \quad \pi_ {1} = \frac {2}{3}
$$

And so  $A$  is positive recurrent.

-  $C$  is formed by a single absorbing state, and so here the chain's behaviour is trivial: the class is aperiodic, positive recurrent, with limiting probability merely given by  $\pi_3 = 1$ .
- Class  $B$  is transient: its only state cannot ever be reached from different states, and it is not absorbing. Transitions  $B \to C$  and  $B \to A$  are possible, but one-way.

In the long run, clearly  $\pi_{22} \equiv \lim_{n \to \infty} P_{22}^{(n)} = 0$ , because 2 is transient. To get the other probabilities we can apply first-step analysis to classes. Explicitly, let  $u \equiv \pi_A$  denote the probability of absorption in class  $A$  if the system starts at 2. Then  $1 - u \equiv \pi_C$  is the probability of absorption in  $C$ . So:

$$
u = (P _ {2 0} + P _ {2 1}) \cdot 1 + \frac {1}{4} \cdot u + \frac {1}{4} \cdot 0 = \frac {1}{2} + \frac {1}{4} u \Rightarrow u = \frac {2}{3}
$$

In this case we could have just noted that, if starting at 2, the probability of going to  $C$  is half that of going to  $A$ . Imposing normalization this leads


directly to  $\pi_{23} = 1 / 3$ , and  $\pi_A = \pi_{20} + \pi_{21} = 2 / 3$ .

When the system is in  $A$ , the probabilities of being in 0 or 1 (in the limit), are the ones found before, i.e.  $\pi_0$  and  $\pi_1$ .

So, to get from 2 to 0, we first need to move from  $B$  to class  $A$ , and then to be in the correct state in the limit:

$$
\pi_ {2 0} = \lim _ {n \to \infty} \mathbb {P} (X _ {n} = 0 | X _ {n} \in A) \mathbb {P} (X _ {n} \in A | X _ {0} = 2) = \pi_ {0} \cdot \pi_ {A} = \frac {2}{3} \cdot \frac {1}{3} = \frac {2}{9}
$$

Similarly, for  $2\to 1$

$$
\pi_ {2 1} = \pi_ {A} \cdot \pi_ {1} = \frac {2}{3} \cdot \frac {2}{3} = \frac {4}{9}
$$

Summarizing, the limiting distribution for the whole chain is given by:

|  limn→∞Pn= | 0 | 1 | 2 | 3 | 0 | 1 | 2 | 3  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |  π0 | π1 | 0 | 0 | 1 | 2 | 3 |   |
|   |  π0 | π1 | 0 | 0 | 1 | 2 | 3 |   |
|   |  π20 | π21 | 0 | π23 | 2 | 3 | 0 | 1  |
|   |  0 | 0 | 0 | 1 | 3 | 0 | 0 | 1  |

![[Stochastic_Processes_2020_p98_img27.jpeg]]
Figure (3.8) - Block diagram for the Markov chain in (3.33).

> [!question] Exercise 3.5.1 (Chap III - n 2.2)
>
> Consider the problem of sending a binary message 0,1 through a signal channel consisting of several stages, where transmission through each stage is subject to a fixed probability of error  $\alpha$ . Let  $X_0$  be the signal that is sent and let  $X_n$  be the signal that is received at the  $n$ -th stage. Suppose that  $X_n$  is a Markov chain with transition probabilities:
>
> $$
> P _ {0 0} = P _ {1 1} = 1 - \alpha \quad P _ {0 1} = P _ {1 0} = \alpha , \quad (0 <   \alpha <   1)
> $$
>
> Determine  $Pr\{X_5 = 0 | X_0 = 0\}$  that is the probability of correct transmission through five stages.
>
> Solution.

#### 3.5.1 Another behaviour of infinite Markov chains

It is possible for all states of a infinite Markov chain to be either transient or null recurrent, such that the transition probability linking any two of them $i$, $j$ vanishes in the limit: $\lim_{n\to \infty}P_{ij}^{(n)} = 0$ [1, p. 220].

A trivial example is given by the Markov chain with the update rule:

$$
\left\{ \begin{array}{l} X _ {n} = X _ {n - 1} + 1 \\ X _ {0} = 0 \end{array} \right.
$$


Infinite chain of non-recurring states

meaning that $X_{n} = X_{0} + n$, and the transition matrix is:

$$
\mathbf {P} = \left[ \begin{array}{c c c c c} 0 & 1 & 2 & 3 & \dots \\ 0 & 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 1 & 0 \\ 2 & 0 & 0 & 0 & 1 \\ 3 & 0 & 0 & 0 & 0 \\ \vdots & \vdots & \vdots & \vdots & \vdots \end{array} \right]
$$

In this case each state can be visited at most one time. More precisely the $n$-th state will be visited at time step $n$ and then abandoned forever. As a consequence, all states of the chain are transient, and each one of them forms a class by itself.

Clearly, such kind of behaviour can be realized only in Markov chains with infinitely many possible states - meaning that a MC with a finite number $N$ of states, must have no null recurrent states, and not all of its states can be transient. Informally: the chain must always be "somewhere", and given infinite time and only a finite number of states, then it is forced to return to some states it visited before. Let's prove this in two steps [2, day 10/04]:

1. First we will prove the presence of at least a positive recurrent state
2. Then we will prove the absence of null recurrent states

Lemma 3.5.1. In a Markov chain with a finite number of states, there must be at least one positive recurrent state.

> [!note] Proof. 
> Proof. We proceed by contradiction. Consider a chain with a finite number $M < \infty$ of states, and suppose that there are no positive recurrent states, meaning that:
>
> $$
> \lim  _ {n \rightarrow \infty} P _ {i j} ^ {(n)} = 0 \tag {3.34}
> $$
>
> By normalization, we know that summing over the $i$-th of the $n$-step transition matrix leads to 1:
>
> $$
> \sum_ {j = 1} ^ {N} P _ {i j} ^ {(n)} = 1 \qquad \forall n
> $$
>
> 1. Finite states $\Rightarrow$ at least one is positive recurrent
>
>
> This must hold also in the limit:
>
> $$
> \lim _ {n \to \infty} \sum_ {j = 1} ^ {N} P _ {i j} ^ {(n)} \stackrel {!} {=} 1
> $$
>
> However, as  $N$  is finite, we can exchange the order of sum and limit, leading to:
>
> $$
> 1 \stackrel {!} {=} \lim  _ {n \rightarrow \infty} \sum_ {j = 1} ^ {N} P _ {i j} ^ {(n)} = \sum_ {j = 1} ^ {N} \lim  _ {n \rightarrow \infty} P _ {i j} ^ {(n)} = 0 \tag {3.35}
> $$
>
> which is clearly a contradiction. Therefore we conclude that our initial assumption was wrong, so there must be at least one positive recurrent state in the chain. In other words, in the long run, a finite chain must "find itself somewhere".
>
> Conversely, any chain in which all states are transient must be infinite. In this case the exchange of the sum with the limit in (3.35) would not be legitimate, thus not leading to a contradiction.
>
> Lemma 3.5.2. In a Markov chain with a finite number of states there cannot be any null recurrent states.

> [!note] Proof. 
> Proof. We proceed again by contradiction. Suppose there is one null recurrent state. Recalling that it is a class property, we then know that it must belong to a finite null recurrent class (as there are is only a finite number of states available). On the other hand a null recurrent class can be considered a Markov chain by itself: once we arrive into it, we are not supposed to leave. But from the previous result this is not possible: a finite class cannot be made by only null recurrent states, as it must have at least one positive recurrent state - thus contradicting our hypothesis.  $\square$
>
> A corollary of these two lemmas is is that null recurrent states are only allowed in infinite chains.

> [!example] Example 9
>
> We want to study the limiting behaviours i.e. computing using any kind of software (Python, R, MATLAB...) the two limits:  $\lim_{n\to \infty}\mathbf{P}^{(n)}$  and  $\lim_{n\to \infty}\mathbf{P}^{(2n + 1)}$  for the following two matrices:
>
> $$
> \mathbf {P} _ {1} = \left\| \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ \frac {1}{3} & \frac {1}{3} & \frac {1}{6} & \frac {1}{6} \\ 0 & 0 & 0 & 1 \end{array} \right\| \qquad \mathbf {P} _ {2} = \left\| \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ \frac {1}{6} & \frac {1}{3} & \frac {1}{3} & \frac {1}{6} \\ 0 & 0 & 0 & 1 \end{array} \right\|
> $$
>
> and then comment the results.
>
> Solution. For both matrices can be easily identified the upper-left block  $\left( \begin{array}{ll}0 & 1\\ 1 & 0 \end{array} \right)$  that has period 2, then the two subsequences for  $n$  even and  $n$
>
> 2. Finite states  $\Rightarrow$  no null recurrent
>
> Null recurrent states are possible only in infinite MCs
>
>
> odd will individually converge, but each one for a different value. Therefore the general limits will not exist since they oscillate.
>
> In particular for  $\mathbf{P_2}$  we expect that the general limit for the terms in the third row do not exist, because of the oscillating nature of the upper-left block. The third row refers to the probability that, given we started in the transient state 2, we end up in the periodic absorbing class  $\{0,1\}$ . Numerically we can see that both the two subsequences  $\lim_{n\to \infty}\mathbb{P}^{2n}$  and  $\lim_{n\to \infty}\mathbb{P}^{2n + 1}$  converge, but to different values:
>
> $$
> (\mathbf {P} _ {2}) ^ {1 0 0 0} = (\mathbf {P} _ {2}) ^ {1 0 0 2} = \left\| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ \frac {7}{1 6} & \frac {5}{1 6} & 0 & \frac {1}{4} \\ 0 & 0 & 0 & 1 \end{array} \right\| \qquad (\mathbf {P} _ {2}) ^ {1 0 0 1} = \left\| \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ \frac {5}{1 6} & \frac {7}{1 6} & 0 & \frac {1}{4} \\ 0 & 0 & 0 & 1 \end{array} \right\|
> $$
>
> This can be summarised by saying that the two limits individually exist and converge to different values, whereas the general limit does not since it keeps oscillating. Note that the probability of being in the absorbing class on the right side, is the proportion of going outside the transient state (2/3) and finally enter the state absorbing class (1/6).
>
> On the other hand when we do the same with the first matrix  $\mathbf{P}_1$ :
>
> $$
> (\mathbf {P} _ {1}) ^ {1 0 0 0} = (\mathbf {P} _ {1}) ^ {1 0 0 2} = \left\| \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ \frac {4}{1 0} & \frac {4}{1 0} & 0 & \frac {2}{1 0} \\ 0 & 0 & 0 & 1 \end{array} \right\| \qquad (\mathbf {P} _ {1}) ^ {1 0 0 1} = \left\| \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ \frac {4}{1 0} & \frac {4}{1 0} & 0 & \frac {2}{1 0} \\ 0 & 0 & 0 & 1 \end{array} \right\|
> $$
>
> Everything is very similar to the example above. The probability of going out of the state 2 is now  $5/6$ . Starting from there we can be absorbed either into the class  $\{0,1\}$  with probability  $2/3$ , or end up in the absorbing class on the right side with probability  $1/6$ . Once we are absorbed by the  $\{0,1\}$  class, however, we can find ourselves with equal probability either in 0 or in 1 state. This is valid for any value of  $n$  when taking the limit, that is both for odd and even values, whereas before they were different.
>
> Finally we can conclude that, for this special case, despite the presence of the periodic upper-left class, the two subsequences converge to an unique value, thus making the limit  $\lim_{t\to \infty}P_{2j}^{(n)}$  exist.
>
>
> ![[Stochastic_Processes_2020_p102_img28.jpeg]]
> Figure (3.9) - Markov chain for example n. 10

> [!example] Example 10
>
> In order to generalize the previous example, let us consider the following chain:
>
> $$
> \mathbf {P} = \left\| \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ a & b & c & 1 - a - b - c \\ 0 & 0 & 0 & 0 \end{array} \right\|
> $$
>
> Here we can tell easily that 2 is a transient state. It may lead either to the periodic  $\{0,1\}$  class or to an other recurrent class that we can consider, for our purposes, as a single absorbing state. This chain has a transition matrix of the  $\mathbf{P}_1$  kind written above.
>
> Compute  $\mathrm{P}[X_{2n} = 0|X_0 = 2]$  and  $\mathrm{P}[X_{2n + 1} = 0|X_0 = 2]$  and find under which conditions on the transition rates  $a, b, c$  it holds that:
>
> $$
> \lim _ {n \to \infty} P [ X _ {2 n} = 0 | X _ {0} = 2 ] = \lim _ {n \to \infty} P [ X _ {2 n + 1} = 0 | X _ {0} = 2 ]
> $$
>
> Comment the result on the conditions just found in a probabilistic fashion. Solution. Will be provided next lecture. See (13).

# 3.6 Absorption probabilities

We have seen through an example (3.33, pag. 97) that the  $n$ -step transition probability  $\mathbb{P}^{(n)}(A \to B)$  to go from a transient state  $A$  to a recurrent state  $B$ , in the long run ( $n \to \infty$ ), is the product between two values: the probability of being absorbed in the recurrent class of  $B$ , and the limiting probability of  $B$  within that class. Let's now formalize this statement [3, p. 91].

Let  $i \in T$  be a transient state, and  $k \in C$  a recurrent one (with this property extending to the respective classes). Suppose we start at  $X_0 = i$ . The probability of entering  $C$  for the first time at step  $n$  by reaching state


$k\in C$ is given by:

$$
\pi^{(n)}_{ik}(C)=\mathbb{P}[X_{n}=k,\;X_{m}\notin C,\;m=1,2,...,n-1|X_{0}=i]
$$

Summing over all possible states $k\in C$ we get the probability of entering $C$ from state $i$ at time step $n$ for the first time:

$$
\pi^{(n)}_{i}(C)=\sum_{k\in C}\pi^{(n)}_{ik}(C)
$$

The events of entering $C$ for the first time at different timesteps are clearly disjoint. Summing over all possible $n$, we get the “generic” probability of entering class $C$ at any time from state $i$:

$$
\pi_{i}(C)=\sum_{n=1}^{+\infty}\pi^{(n)}_{i}(C)
$$

Having established this notation, we can state the following theorem *[3, p. 91]*:

> [!abstract] Theorem 3.6.1.
>
> Let $j\in C$ and $i\in T$, where $C$ is an aperiodic recurrent class and $T$ is a transient one. Then it holds that:
>
> $$
> \lim_{n\to\infty}P^{(n)}_{ij}=\pi_{i}(C)\lim_{n\to\infty}P^{(n)}_{jj}=\pi_{i}(C)\cdot\pi_{j}
> $$
>
> (Note that the limit depends on both $i$ and $j$).

> [!note] Proof. Omitted.
> Proof. Omitted.

> [!abstract] Theorem 3.6.1 
>
> $$
> \lim_{n\to\infty}\sum_{m=0}^{n-1}P^{(m)}_{ij}
> $$
>
> Limiting transition probability transient $\to$ recurrent
>
> Limiting transition matrix (3.38).

> [!question] Exercise 3.6.1 (Limiting behaviour of a MC)
>
> Let us take a look on an exercise assigned on the 05-09-2007 written exam, that is very similar to the ones that we should expect to find in tests.
>
> Consider a Markov chain with the following transition matrix:
>
> $$
> \mathbf {P} = \left| \begin{array}{c c c c c} 0 & 1 & 2 & 3 & 4 \\ 0 & 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 & 0 \\ 2 & 0 & 0 & 0.4 & 0.6 \\ 3 & 0.5 & 0 & 0 & 0.2 \\ 4 & 0 & 0 & 0.6 & 0.4 \end{array} \right| \tag {3.38}
> $$
>
> 1. Classify the states and identify the classes
> 2. Compute the probabilities of absorption in all recurrent classes starting from each transient state
> 3. Compute  $\lim_{n\to \infty}\mathbf{P}^n$  and  $\lim_{n\to \infty}\frac{1}{n}\sum_{k = 1}^{n}\mathbf{P}^k$
> 4. Compute the average recurrence times for all states

## Solution.

1. As can be seen from the block diagram (fig. 3.10) there are three distinct classes:  $\mathbf{A} = \{0,1\}$ ,  $\mathbf{B} = \{3\}$ ,  $\mathbf{C} = \{2,4\}$ .

If the system starts in state 2 or 4, it never visits other states, so  $C$  is a positive recurrent class. Moreover it is aperiodic because the system may stay in the same state with non-zero probability.

The same occurs if we start in either 0 or 1, thus  $A$  is a positive recurrent class. However, in this case it is periodic, because the system deterministically goes back and forth from state 0 to state 1 with period  $d = 2$ .

Finally, class  $B$  consists only of the transient state 3, since no connections from other states lead back to it, but it leads to other states with non-zero probability.

2. Noting that there is only one transient state and two different absorbing classes, it is enough to compute just one of the two absorption probabilities - the other one will be its complementary to 1.

Starting in 3, we leave the state with probability  $0.3 + 0.5 = 0.8$ . Supposing that this happens, the system will go to  $C$  with a probability of  $\pi_3(\{2,4\}) \equiv \pi_3(C) = 0.3 / 0.8 = 3 / 8$ , given by the ratio of the total probability of transitions to  $C$  (0.3, only  $3 \to 4$  counts) and the total probability of leaving  $B$  in the first place (0.8). Similarly, the system goes to  $A$  with  $\pi_3(\{0,1\}) \equiv \pi_3(A) = 0.5 / 0.8 = 5 / 8$  - and both results sum to 1 as expected.


3. We start with the limit of the  $n$ -step transition matrix:

|  limn→∞P^n = | 0 | 1 | 2 | 3 | 4  |
| --- | --- | --- | --- | --- | --- |
|   |  0 | ? | ? | ? | ?  |
|   |  1 | ? | ? | ? | ?  |
|   |  2 | ? | ? | ? | ?  |
|   |  3 | ? | ? | ? | ?  |
|   |  4 | ? | ? | ? | ?  |

Since  $A$  is a periodic class, no limit exists for transition probabilities between elements of  $A$ , i.e.  $\{0,1\}$  - we denote this with a “ $\times$ ”. Clearly there is no way to exit  $A$ , and so the probabilities from  $\{0,1\}$  to any other state are 0:

|  limn→∞P^n = | 0 | 1 | 2 | 3 | 4  |
| --- | --- | --- | --- | --- | --- |
|   |  0 | × | × | 0 | 0  |
|   |  1 | × | × | 0 | 0  |
|   |  2 | ? | ? | ? | ?  |
|   |  3 | ? | ? | ? | ?  |
|   |  4 | ? | ? | ? | ?  |

Similarly, if the system starts in  $C = \{2,4\}$  it will remain there, as it is a recurrent class. As transition probabilities  $2 \leftrightarrow 4$  are symmetric, we expect the limiting/stationary probability to be the same for both states, i.e.  $\pi_2 = \pi_4 = 1/2$ :

|  limn→∞P^n = | 0 | 1 | 2 | 3 | 4  |
| --- | --- | --- | --- | --- | --- |
|   |  0 | × | × | 0 | 0  |
|   |  1 | × | × | 0 | 0  |
|   |  2 | 0 | 0 | 1/2 | 0  |
|   |  3 | ? | ? | ? | ?  |
|   |  4 | 0 | 0 | 1/2 | 0  |

Finally, as 3 is transient,  $\pi_{33} = 0$ . We have seen (theorem 3.6.1) that the limiting probabilities are the product between the probability of going to a class, and the limiting distribution within that class, so:

$$
\pi_{30} = \pi_3(A)\pi_0 \pi_{32} = \pi_3(C)\pi_2
\pi_{31} = \pi_3(A)\pi_1 \pi_{34} = \pi_3(C)\pi_4
$$

However,  $\pi_0$  and  $\pi_1$  do not exist (as  $A$  is periodic) and thus neither do  $\pi_{30}$  and  $\pi_{31}$ . On the other hand, we obtain:

$$
\pi_{32} = \pi_{34} = \frac{3}{8}\cdot \frac{1}{2} = \frac{3}{16}
$$


leading to:

![[Stochastic_Processes_2020_p106_img29.jpeg]]

Note that, as certain entries are missing, not all rows sum to 1.

All that's left is to compute:

$$
\lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 0} ^ {n} \mathbf {P} ^ {k}
$$

We know that anywhere  $\lim_{n\to \infty}\mathbf{P}^n$  exists,  $\lim_{n\to \infty}\frac{1}{n}\sum_{k = 1}^{n}\mathbf{P}^k$  will exist and will be equal. Whereas, for periodic cases where the limiting probabilities didn't exist before, they now do exist - and are given by the average fraction of time spent in those states. So:

$$
\pi_ {0} = \pi_ {1} = \frac {1}{d} = \frac {1}{2}
$$

And from (thm. 3.6.1):

$$
\pi_ {3 0} = \pi_ {3 1} = \pi_ {3} (A) \cdot \frac {1}{2} = \frac {5}{8} \cdot \frac {1}{2} = \frac {5}{1 6}
$$

leading to:

![[Stochastic_Processes_2020_p106_img30.jpeg]]

As a fast check, we note as all rows sum to 1, so our computations should be correct.

4. Let  $m_i$  be the average recurrence time of state  $m_i$ , and denote with  $\pmb{m}$  the  $d = 5$  vector containing all the  $m_i$ .

For an aperiodic recurrent class (such as  $C$ ) we know that, from the Basic Limit Theorem (3.6, pag. 81)  $m_i$  is the reciprocal of the limiting probability  $\pi_i$ :

$$
m _ {2} = m _ {4} = \left(\frac {1}{2}\right) ^ {- 1} = 2
$$


For the periodic recurrent class  $A$  we use the generalization (3.30, pag. 95):

$$
m _ {i} = \left(\lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 1} ^ {n} P _ {i i} ^ {(n)}\right) ^ {- 1} \Rightarrow m _ {0} = m _ {1} = \left(\frac {1}{2}\right) ^ {- 1} = 2
$$

For transient state 3, the same computation would lead  $m_3 = 1 / 0 = \infty$ . We can justify this result proceeding with first-step analysis. From state 3 only two types transitions are possible:  $3 \rightarrow 3$  with  $p = 0.2$  (leading to a recurrence time of 1) and  $3 \rightarrow 0 \lor 4$  with  $p = 0.8$  (leading to an infinite recurrence time, as then 3 is never visited again). So the average return time will be bigger than any number with a finite probability  $p = 0.8$ . This makes the average recurrence time for a transient state an improper random variable, thus necessarily implying that its average value must be infinite, and so  $m_3 = \infty$ .

In summary:

$$
\boldsymbol {m} = \left( \begin{array}{c} 2 \\ 2 \\ 2 \\ \infty \\ 2 \end{array} \right)
$$

Note that return times must be at least 1: they can not be zero even for transient states, since any transition requires at least one step. We denote the fact of "never returning" by saying that the (average) return time is infinite.

Let us summarize all possible cases in one table:

|  Start: i | End: j | limn→∞Pij(n)  |
| --- | --- | --- |
|  Any | Transient | 0  |
|  Recurrent ∈ C | Recurrent∉C | 0  |
|  Recurrent ∈ C | Recurrent ∈ C | πj=1/mj  |
|  Transient | Recurrent ∈ C | πi(C)πj=πi(C)/mj  |

Limiting transition probabilities between all types of states

Table (3.2) - Summary of limiting transition probabilities  $i \rightarrow j$  between all possible types of states.  $\pi_i(C)$  denotes the probability of entering class  $C$  from state  $i$ , given by (3.36), and  $C$  is a aperiodic recurrent class.

Table 3.2 can be extended to the case of  $C$  being a periodic recurrent class by just substituting  $\lim_{n\to \infty}P_{ij}^{(n)}$  with:

$$
\lim  _ {n \to \infty} \frac {1}{n} \sum_ {k = 1} ^ {n} P _ {i j} ^ {(k)}
$$


### 3.7 Transient states

In this section we will derive a criterion (i.e. a necessary and sufficient condition) for transiency for irreducible Markov chains, as sometimes using the recurrence definition (thm. 3.3.2) may not be convenient *[4, p. 78–82]*.

Let $S$ be a fixed set of states (arbitrarily chosen) of some irreducible Markov chain $\{X_{n}\}$. We denote with $Y_{i}(n)$ the probability that a system starting at state $i\in S$ will not leave $S$ for $n$ steps:

$$
Y_{i}(n)\equiv\mathbb{P}\{X_{j}\in S\quad\forall j=1,2,...,n|X_{0}=i\},\ i\in S
$$

In other words, $Y_{i}(n)$ is the probability of a system “surviving” $n$ steps in set $S$. For $n=1$ this amounts to the sum of transition probabilities to states inside $S$:

$$
Y_{i}(1)=\sum_{j\in S}P_{ij}
$$

And for $n>1$ we proceed by first-step analysis:

$$
Y_{i}(n)=\sum_{j\in S}P_{ij}Y_{j}(n-1)
$$

We now proceed to show several properties of $Y_{i}(n)$ *[2, day 10/04]*.

###### Lemma 3.7.1.

$Y_{i}(n)$ is a non-increasing function of $n$ $\forall i\in S$.

> [!note] Proof.
>
> We proceed by induction. First we prove that it holds for $n=2$:
>
> $$
> Y_{i}(2)=\sum_{j\in S}P_{ij}Y_{j}(1)\underset{Y_{j}(1)\leq 1}{\leq}\sum_{j\in S}P_{ij}=Y_{i}(1)
> $$
>
> as $Y_{j}(1)$ is a probability.
>
> Now, suppose the hypothesis holds up to $n$:
>
> $$
> Y_{i}(n)\leq Y_{i}(n-1)\leq\cdots\leq Y_{i}(1)
> $$
>
> Given that, we want to prove that it holds up to $n+1$ too:
>
> $$
> Y_{i}(n+1)\leq Y_{i}(n)
> $$
>
> Using (3.39) we get:
>
> $$
> Y_{i}(n+1)\underset{(3.39)}{\equiv}\sum_{j\in S}P_{ij}Y_{j}(n)\underset{(3.40)}{\leq}\sum_{j\in S}P_{ij}Y_{j}(n-1)=Y_{i}(n)\leq\cdots\leq Y_{i}(1)
> $$
>
> which concludes the proof. ∎
>
> We have just found that $Y_{i}$ is a monotone (non-increasing) sequence, which is also bounded in the interval $[0,1]$ since it is a probability. Thus, it is convergent, i.e. $\lim_{n\to\infty}Y_{i}^{(n)}\equiv Y_{i}$ exists. Then, taking the limit of both sides of (3.39) leads to:
>
> “Survival” probabilities are converging
>
>
> $$
> \lim_{n\to\infty}Y_{i}(n)=\lim_{n\to\infty}\sum_{j\in S}P_{ij}Y_{j}(n-1)\underset{(a)}{=}\sum_{j\in S}P_{ij}\lim_{n\to\infty}Y_{j}(n-1)
> \Rightarrow Y_{i}=\sum_{j\in S}P_{ij}Y_{j}
> $$
>
> where exchanging the sum with the limit in (a) is allowed by the Lebesgue monotonic convergence theorem.
>
> In summary, $Y_{i}$ can be interpreted as the probability that a Markov chain starting from state $i$, never leaves the set $S$, and it must satisfy (3.41).
>
> We can then proceed backwards and try to solve (3.41) to determine $Y_{i}$. However, this requires some caution - as (3.41) is a set of homogeneous equations, allowing an infinite number of proportional solutions. Explicitly, if $\boldsymbol{Z}=(Z_{1},\ldots,Z_{N})^{T}$ solves (3.41), then $\boldsymbol{Z}^{\prime}=\alpha\boldsymbol{Z}\ \forall\alpha\in\mathbb{R}$ is a solution too.
>
> As we are interested in finding $Y_{i}$, which are probabilities, we focus on the solutions $\boldsymbol{Z}$ which are bounded by 1:
>
> $$
> Z_{i}=\sum_{j\in S}P_{ij}Z_{j},\qquad|Z_{i}|\leq 1,\qquad i\in S
> $$
>
> It can be proved that if $Z_{i}$ is a solution of (3.42) and $Y_{i}$ is a solution of (3.41), we can say that $Y_{i}$ is the biggest solution of that set. More formally:
>
> ###### Lemma 3.7.2.
>
> Let $Z_{i}$ be any bounded solution of the system (3.42), with $|Z_{i}|\leq 1$. Then:
>
> $$
> |Z_{i}|\leq Y_{i}=\lim_{n\to\infty}Y_{i}(n)
> $$
>
> In other words, $Y_{i}$ is the largest between all possible bounded solutions of (3.42):
>
> $$
> Y_{i}=\underset{\boldsymbol{Z}\text{ solution of }\eqref{2.42}}{\max}Z_{i}
> $$

> [!note] Proof.
>
> Again we proceed by induction. At the beginning we have that:
>
> $$
> |Z_{i}|=\left|\sum_{j\in S}P_{ij}Z_{j}\right|\underset{(a)}{\leq}\sum_{j\in S}P_{ij}|Z_{j}|\underset{|Z_{i}|\leq 1}{\leq}\sum_{j\in S}P_{ij}=Y_{i}(1)
> $$
>
> where in (a) we used the triangular inequality and the fact that probabilities are non-negative: $|P_{ij}|=P_{ij}$.
>
> Now suppose that $|Z_{i}|\leq Y_{i}(n)$ for some $n$. Then, we prove that it holds also for $n+1$:
>
> $$
> |Z_{i}|\leq\sum_{j\in S}P_{ij}|Z_{j}|\leq\sum_{j\in S}P_{ij}Y_{j}(n)=Y_{i}(n+1)
> $$
>
> Thus:
>
> $$
> |Z_{i}|\leq Y_{i}(n)\leq Y_{i}(n+1)\qquad\forall n
> $$
>
>
> As it holds for all $n$, it is valid also in the limit:
>
> $$
> |Z_{i}|\leq\lim_{n\to\infty}Y_{i}(n)\equiv Y_{i}
> $$
>
> which concludes our proof. ∎
>
> We can now make a step forward and make some considerations about the system (3.42). Since it is homogeneous, there are two obvious solutions: $Z_{i}=0$ $\forall i$ and $Z_{i}=\infty$ $\forall i$. But if we can find a solution $|Z_{i}|$ that is both bounded and nonzero, then since $Y_{i}$ is the maximal solution it must be non zero, too:
>
> $$
> 0<|Z_{i}|\leq Y_{i}\Rightarrow Y_{i}>0
> $$
>
> Conversely, if the only bounded solution $Z_{i}$ that the system (3.42) has is the zero one, then $Y_{i}=0$ must be zero, because of (3.43).
>
> Before proceeding, we need two more results. The first one is a recurrence criterion for irreducible Markov chain:
>
> ###### Lemma 3.7.3.
>
> An irreducible Markov chain with state space $\mathbb{N}$ is recurrent if and only if:
>
> $$
> f_{i0}=\sum_{n=1}^{\infty}f_{i0}^{(n)}=1\qquad\forall i\neq 0
> $$
>
> $f_{i0}^{(n)}$ is the probability of a system starting at state $i$ and reaching state $0$ for the first time at the $n$-th step. Then, summing over all possible $n$ leads to the probability of visiting $0$ at any time from state $i$. Thus, $f_{i0}=1$ means that the system will certainly visit state $0$ in the future.

> [!note] Proof.
>
> We proceed in two steps:
>
> 1. Necessity ($\Leftarrow$). Assuming that $f_{i0}=1$ $\forall i\neq 0$, then the probability of returning to the state $0$ given the fact we started from $i$ is given by first step analysis:
>
> $$
> f_{00}=P_{00}+\sum_{i\neq 0}P_{0i}f_{i0}
> $$
>
> Since all $f_{i0}=1$ $\forall i\neq 0$, this becomes:
>
> $$
> f_{00}=P_{00}+\sum_{i\neq 0}P_{0i}=\sum_{i}P_{0i}=1
> $$
>
> by normalization. Thus the probability of starting at $0$ and returning to $0$ is unity, meaning that state $0$ is recurrent (and so all other states, because the chain is irreducible).
> 2. Sufficiency ($\Rightarrow$). Formally, proving $A\Rightarrow B$ is equivalent to proving $\neg B\Rightarrow\neg A$. Hence, we want to prove that if (3.44) is false, then the MC is non-recurrent.
>
>
> So, suppose that $f_{i0}$ is not 1 for all $i\neq 0$, meaning that there exists some $i\neq 0$ such that $f_{i0}<1$. This means that, if the system starts at $i$, then it is not certain that it will ever visit 0. The idea is then to note that there is a non-zero probability of going from 0 to $i$, and then never returning back, meaning that $f_{00}<1$, and so 0 (and all the other states) are non-recurrent.
>
> In fact, as the MC is irreducible, all states communicate, and so there is a way to go from 0 to $i$ given a sufficient number $m$ of steps: $\exists m$ s.t. $P^{(m)}_{0i}>0$. Let $n$ be the minimum number of steps required to travel from 0 to $i$, i.e.:
>
> $$
> n=\min_{m>0}\left\{P^{(m)}_{0i}>0\right\}
> $$
>
> Consider one of these “optimal paths” $A=(a_{1},\ldots,a_{n})$, with $a_{1}=0$ and $a_{n}=i$. $A$ cannot reach 0 in any intermediate step: $a_{j}\neq 0$ $\forall j\neq n$. If it were so, then it would clearly exist a path connecting $0\rightarrow i$ in $j<n$ steps, but $n$ is already the minimum number of steps for such a path.
>
> Then, an event where the system never returns to 0 is one where it first goes from $0\rightarrow i$ in $n$ steps, and then never goes back to 0. The probability of such an event is the product of the probability $P^{(n)}_{0i}$ of getting to $i$ in $n$ steps, and $(1-f_{i0})$ - and it is nonzero. Clearly, there could be many other events where the chain never returns to 0 - so the full probability of not returning, i.e. $1-f_{00}$, must be greater than that product:
>
> $$
> 1-f_{00}\geq P^{(n)}_{0i}(1-f_{i0})>0\Rightarrow f_{00}<1
> $$
>
> Thus 0 is non-recurrent, and so are all other states.
>
> ∎
>
> We are now ready to prove the transience criterion we are interested in:

> [!abstract] Theorem 3.7.1.
>
> An irreducible Markov chain with state space $\mathbb{N}=\{0,1,2,\ldots\}$ has all transient states if and only if the system of equations:
>
> $$
> Z_{i}=\sum_{j=1}^{\infty}P_{ij}Z_{j}\qquad i=1,2,\ldots
> $$
>
> has a nonzero bounded solution.
>
> Note that the just stated system and (3.42) are the same, they only differ by the sum that starts from $j=1$ and by the equation for $i=0$, that is not included in the statement of the theorem.

> [!note] Proof.
>
> Let $S$ be the set of all states $1,2,\ldots$ (all except 0). Then $Y_{i}$, i.e. the probability of not leaving $S$, is just the probability that starting from $i$ we never reach state 0, i.e. $1-f_{i0}$:
>
> $$
> Y_{i}=1-f_{i0}
> $$
>
>
> ![[Stochastic_Processes_2020_p112_img31.jpeg]]
> Figure (3.11) - Markov chain for exercise 3.7.1
>
> Now, since we have supposed there exists a nonzero bounded solution, using the result provided by lemma 3.7.2, we know that  $Y_{i}$  must be at least greater or equal than that particular solution, and so  $Y_{i} > 0$  for some  $i$ , meaning that  $1 - f_{i0} > 0 \Rightarrow f_{i0} < 1$ , which implies that state 0 is transient through lemma 3.7.3.
>
> Conversely, if the only bounded solution of the system (3.45) is given by  $Y_{i} = 0 \forall i$ , then  $Y_{i} = 1 - f_{i0} = 0 \Rightarrow f_{i0} = 1 \forall i$ , meaning (lemma 3.7.3) that the chain is recurrent, thus concluding our proof.

> [!question] Exercise 3.7.1 (Problem Ch. IV n.8)
>
> An urn contains five red and three green balls. The balls are chosen at random, one by one, from the urn. If a red ball is chosen it is removed. Any green ball that is chosen is returned to the urn. This selection process continues until all of the red balls have been removed from the urn. What is the mean duration of the game?
>
> Let  $X_{n}$  is the Markov process that refers to the number of red balls we have at time step  $n$ . Its transition matrix is:
>
> ![[Stochastic_Processes_2020_p112_img32.jpeg]]
>
> Clearly by "duration of the game" we are asked to compute  $\nu_{5}$ : the mean absorption time starting from state 5, since the game ends when there are no more red balls. We then write the system of equations using first step analysis, in order to try to compute it recursively. The first term will be:
>
> $$
> \nu_ {5} = 1 + \frac {3}{8} \nu_ {5} + \frac {5}{8} \nu_ {4} \Longrightarrow \nu_ {5} = \frac {8}{5} + \nu_ {4} \tag {3.46}
> $$
>
> and, in general:
>
> $$
> \nu_ {i} = 1 + a _ {i} \nu_ {i} + (1 - a _ {i}) \nu_ {i - 1}
> $$
>
>
> where we can see from 3.46 that for  $i = 5$  we have  $a_5 = \frac{3}{8}$ . While, taking a look at the transition matrix we have that for  $i = 4$ $a_4 = \frac{4}{7}$ , for  $i = 3$ $a_3 = \frac{1}{2}$  and so on, until  $i = 0$  where  $a_0 = 1$ . As before, we write the last equation recursively:
>
> $$
> (1 - a _ {i}) \nu_ {i} = 1 + (1 - a _ {i}) \nu_ {i - 1} \Longrightarrow v _ {i} = \frac {1}{1 - a _ {i}} + \nu_ {i - 1}
> $$
>
> It can be thus solved recursively by substituting each  $a_i$ , and by noticing that  $\frac{1}{1 - a_i}$  returns the inverse of the probability of changing the state to a lower one. Finally we conclude:
>
> $$
> \nu_ {5} = \frac {8}{5} + \frac {7}{4} + 2 + \frac {5}{2} + 4 = 1 1. 8 5
> $$
>
> Note that the time spent in each state distributes geometrically, and so its average is the inverse of the outgoing probability. Therefore, the average absorption time is nothing more than the sum of the average time spent in each of the states.

> [!question] Exercise 3.7.2 (Problem Ch. IV n.10)
>
> You have five fair coins. You toss them all so that they randomly fall heads or tails. Those that fall tails in the first toss you pick up and toss again. You toss again those that show tails after the second toss, and so on, until all show heads. Let  $X$  be the number of coins involved in the last toss.
>
> Find  $\operatorname{Pr}\{X = 1\}$ , that is the probability of having only one coin while tossing for the last time.
>
> Let us start by discussing about our Markov chain. First we note that, since  $X$  is the number of coins that is not heads, the state can not increase but only decrease or remain equal.
>
> In order to compute the probability that we have exactly 1 coin in the last toss, we make 1 an absorbing state. Note that 0 state is an absorbing state as well, since we do not have any more coins to toss. Therefore, being absorbed in 0 means we have never visited in state 1 and so the last toss was involving more than one coin. On the other hand, if we get absorbed in the state 1, our last toss will involve exactly one coin that is the event asked by the problem. Transition matrix for this process is:
>
> |  P = | 0 | 1 | 2 | 3 | 4 | 5  |
> | --- | --- | --- | --- | --- | --- | --- |
> |   |  1 | 0 | 0 | 0 | 0 | 0  |
> |   |  0 | 1 | 0 | 0 | 0 | 0  |
> |   |  1/4 | 1/2 | 1/4 | 0 | 0 | 0  |
> |   |  1/8 | 3/8 | 3/8 | 1/8 | 0 | 0  |
> |   |  1/16 | 4/16 | 6/16 | 4/16 | 1/16 | 0  |
> |   |  1/32 | 5/32 | 10/32 | 10/32 | 5/32 | 1/32  |
>
> In order to answer the question of the problem we want, given we started in state 5 i.e. with 5 coins to flip, to compute the probability of getting absorbed
>
>
> in state 1. This can be obtained again using first step analysis and application of absorption probabilities for the specific state 1, thus solving the following system:
>
> $$
> \left\{ \begin{array}{l} u _ {0} = 1 \cdot 0 \\ u _ {1} = 0 u _ {0} + 1 \\ u _ {2} = \frac {1}{4} u _ {0} + \frac {1}{2} u _ {1} + \frac {1}{4} u _ {2} \\ u _ {3} = \frac {1}{8} u _ {0} + \frac {3}{8} u _ {1} + \frac {3}{8} u _ {2} + \frac {1}{8} u _ {3} \\ u _ {4} = \frac {1}{1 6} u _ {0} + \frac {4}{1 6} u _ {1} + \frac {6}{1 6} u _ {2} + \frac {4}{1 6} u _ {3} + \frac {1}{1 6} u _ {4} \\ u _ {5} = \frac {1}{3 2} u _ {0} + \frac {5}{3 2} u _ {1} + \frac {1 0}{3 2} u _ {2} + \frac {1 0}{3 2} u _ {3} + \frac {5}{3 2} u _ {4} + \frac {1}{3 2} u _ {5} \end{array} \right.
> $$
>
> and the result we are looking for is:  $u_{5} = 0.7235$ .

> [!question] Exercise 3.7.3 (Problem Ch. IV n.12)
>
> A Markov chain  $X_0, X_1, X_2, \ldots$  has the transition probability matrix:
>
> $$
> \mathbf {P} = \left. \begin{array}{l l l l} & 0 & 1 & 2 \\ 0 & 0. 3 & 0. 2 & 0. 5 \\ 1 & 0. 5 & 0. 1 & 0. 4 \\ 2 & 0 & 0 & 1 \end{array} \right\|
> $$
>
> and is known to start in state  $X_0 = 0$ . Eventually, the process will end up in state 2. What is the probability that when the process moves into state 2, it does from state 1?
>
> Hint: Let  $T = \min \{n \geqslant 0; X_n = 2\}$  and let  $z_i = Pr\{X_{T-1} = 1 | X_0 = i\}$  for  $i = 0, 1$ . We note that  $X_{T-1}$  is the state just prior to absorption.
>
> Establish and solve the first step equations:
>
> $$
> z _ {0} = \quad 0. 3 z _ {0} + 0. 2 z _ {1}
> z _ {1} = 0. 4 + 0. 5 z _ {0} + 0. 1 z _ {1}
> $$
>
> In first equation there is a blank space: it refers to the event where, starting from state 0, we suddenly get absorbed. Therefore the particular event requested by the problem, that is being absorbed in state 2 coming from state 1, does not occur. So it is the probability times 0, that returns 0.
>
> While in the second equation, that refers to state 1, we can be absorbed by state 2 with probability 0.4. But, since it is the event that we want to occur, it is the probability times 1. What is requested by the problem is therefore to compute  $z_0$ .
>
> Another way to solve this problem is the following one. Let us consider the following transition matrix:
>
>
> where we split the state 2 into two different states: one refers to state 2 but only in the case that we come from state 1, which is denoted by win. It is indeed the event we want! On the other hand the second one refers to the event where we are absorbed by state 2, but coming from state 0, and it is denoted by lose. In the end we want to compute the probability that we end up in the win state, given the fact we started in 0 state. Again we are in the same situation of the exercise 3.7.2. Since there are two absorbing states, we shall continue by using first step analysis, solving the following system of equations:
>
>$$
> \begin{cases}
> u_{\text{lose}} = 0 \\
> u_{\text{win}} = 0u_{\text{lose}} + 1 \\
> u_{1} = 0u_{\text{lose}} + 0.4u_{\text{win}} + 0.1u_{1} + 0.5u_{0} \\
> u_{0} = 0.5u_{\text{lose}} + 0u_{\text{win}} + 0.2u_{1} + 0.3u_{0}
> \end{cases}
> $$
> thus finally finding that:
>
> $$
> z_{0}=u_{0,win}=\frac{8}{53}
> $$
>
> ###### Example 11 (Random Walk with variable Parameters $[4$, p. 79]):
>
> Let’s see an application of the transience criterion seen in (3.45, pag. 111). Consider a random walk with states $0,1,2...$ for which:
>
> $$
> P_{i,i+1}=p_{i}\quad P_{i,i-1}=q_{i}=1-p_{i}\qquad i=0,1,2...
> $$
>
> with reflecting boundary condition $p_{0}=1$. In this case, (3.45) becomes:
>
> $$
> Z_{1}=p_{1}Z_{2}, i=1
> Z_{i}=p_{i}Z_{i+1}+q_{i}Z_{i-1} i>1
> $$
>
> and can be solved recursively.
> The idea is to evaluate the difference between consecutive $Z_{i}$. In the first case we have:
>
> $$
> Z_{2}-Z_{1}=Z_{2}-p_{1}Z_{2}=\underbrace{Z_{2}}_{Z_{1}/p_{1}}\underbrace{(1-p_{1})}_{(3.48)}\frac{(1-p_{1})}{q_{1}}=\frac{q_{1}}{p_{1}}Z_{1}
> $$
>
>
> For general $i$ we start from (2) instead:
>
> $$
> Z_i \underbrace{(p_i + q_i)}_{1} = p_i Z_{i+1} + q_i Z_{i-1}
> $$
>
> and rearranging:
>
> $$
> q_i (Z_i - Z_{i-1}) = p_i (Z_{i+1} - Z_i) \Rightarrow Z_{i+1} - Z_i = \frac{q_i}{p_i} (Z_i - Z_{i-1}), \quad i > 1
> $$
>
> The factor $(Z_i - Z_{i-1})$ in turn can be rewritten in terms of the previous difference:
>
> $$
> Z_i - Z_{i-1} = \frac{q_{i-1}}{p_{i-1}} (Z_{i-1} - Z_{i-2})
> $$
>
> and so on, until we reach $Z_2 - Z_1$ given by (3.50) leading to a recurrence relation.
>
> Therefore the $Z_{i+1} - Z_i$ can be written as:
>
> $$
> Z_{i+1} - Z_i = \left[ \prod_{j=2}^{i} \frac{q_j}{p_j} \right] (Z_2 - Z_1) \underset{(3.50)}{=} Z_1 \prod_{j=1}^{i} \frac{q_j}{p_j} \quad i \geq 1
> $$
>
> If we sum over $i$:
>
> $$
> \begin{aligned}
> \sum_{i=0}^{n} (Z_{i+1} - Z_i) &= (Z_{n+1} - Z_n) + (Z_n - Z_{n-1}) + \dots + (Z_1 - Z_0) \\
> &= Z_{n+1} - Z_0 \\
> &= Z_1 \sum_{i=0}^{n} \underbrace{\left( \prod_{j=1}^{i} \frac{q_j}{p_j} \right)}_{\rho_i} = Z_1 \sum_{i=0}^{n} \rho_i \tag{3.51}
> \end{aligned}
> $$
>
> with the convention that $\prod_{i=1}^{0} \equiv 1$, and $\rho_0 \equiv 1$. If this solution is bounded, then by applying theorem 3.7.1 we have proven that all states are transient. The solution (3.51) is bounded only if and only if the sum over $\rho_i$ converges to a finite value:
>
> $$
> \lim_{n \to \infty} Z_n < \infty \Leftrightarrow \sum_{i=0}^{\infty} \rho_i < \infty
> $$
>
> This, along with the results found in the example 6 in page 86, provides a complete classification of the states in the random walk MC:
>
> 1. Positive recurrent if and only if:
>
> $$
> \sum_{j=0}^{\infty} \frac{p_0 \cdots p_j}{q_0 \cdots q_{j+1}} < \infty
> $$
>
> 2. Transient if and only if:
>
> $$
> \sum_{j=1}^{\infty} \frac{q_1 \cdots q_j}{p_1 \cdots p_j} < \infty
> $$
>
>
> Note that this condition is essentially the inverse of positive recurrence one, and moreover they are mutually exclusive. In other words one can show that if the condition 1) holds, then the sum in 2) must diverge, and viceversa. It’s thus impossible for both sum to converge, but actually they both can diverge as the case 3) below.
> 3. Null recurrent if and only if:
>
> $$
> \sum_{j=0}^{\infty}\frac{p_{0}\cdots p_{j}}{q_{0}\cdots q_{j+1}}=\infty\vee\sum_{j=1}^{\infty}\frac{q_{1}\cdots q_{j}}{p_{1}\cdots q_{j}}=\infty
> $$
>
> this case may happen for example when, for $j\to\infty$, $q_{j}$ and $p_{j}$ either go to zero too slowly or don’t even go zero. This means that both sums may diverge, thus the Markov chain being null recurrent.

> [!example] Example 12 (Classification of states in M/G/1 Queueing system *[4, p. 80]*)
>
> We want to proceed classifying the Markov chain M/G/1 system, that we have previously discussed in sec. 2.3. Its transition matrix is the following, recalling that we sample at departure times:
>
> $$
> \mathbf{P}=\begin{bmatrix}a_{0}&a_{1}&a_{2}&a_{3}&a_{4}&\cdots\\
> a_{0}&a_{1}&a_{2}&a_{3}&a_{4}&\cdots\\
> 0&a_{0}&a_{1}&a_{2}&a_{3}&\cdots\\
> 0&0&a_{0}&a_{1}&a_{2}&\cdots\\
> 0&0&0&a_{0}&a_{1}&\cdots\\
> \vdots&\vdots&\vdots&\vdots&\vdots&\ddots\end{bmatrix}
> $$ (3.52)
>
> Where each $a_{i}$ is drawn from the distribution of arrivals during the service period. Let $\rho$ be the average of this distribution, i.e. the average number of arrivals during a service time:
>
> $\rho=\sum_{n=0}^{\infty}na_{n}$ (3.53)
>
> This chain has 3 possible classifications according to the value of $\rho$:
>
> 1. Positive recurrent if $\rho<1$
> 2. Null recurrent if $\rho=1$
> 3. Transient if $\rho>1$
>
> Part 1. Let’s prove that, starting with positive recurrence.
>
> This can be done by solving the stationarity equations:
>
> $\pi_{i}=\sum_{j}P_{ji}\pi_{j}\quad i\geq 0$ (3.54)
>
>
> f we can find the a set of solutions $\pi_{i}$, then we know that they will be also the limiting distribution and conclude that the chain is *positive recurrent*. Otherwise, if there is no solution, it cannot be positive recurrent.
>
> Equation (3.54) can be rewritten in matrix form as:
>
> $\boldsymbol{\pi}=\boldsymbol{\pi}\mathbf{P}$
>
> meaning that the $i$-th element of $\boldsymbol{\pi}$ is the *scalar product* between the $i$-th column of $\mathbf{P}$ and $\boldsymbol{\pi}$ itself. Given the form of $\mathbf{P}$ in (3.52), this means that $\pi_{0}$ multiplies $a_{i}$, $\pi_{1}$ multiplies $a_{i}$, $\pi_{2}$ multiplies $a_{i-1}$, $\pi_{3}$ multiplies $a_{i-2}$, and so on until we reach the last element in the column different from zero, that is $a_{0}$:
>
> $\pi_{i}=\pi_{0}a_{i}+\sum_{j=1}^{i+1}\pi_{j}a_{i-j+1}\qquad i\geq 0$ (3.55)
>
> The idea to solve this equations is to rewrite them in terms of *probability generating functions* *[2, day 17/04]*. Recall that, for a (discrete) probability mass function with non-negative integer values such as $\{\pi_{j}\}_{j\in\mathbf{\mathcal{N}}}$, the probability generating function is defined by the power expansion:
>
> $\pi(s)\equiv\sum_{j=0}^{+\infty}\pi_{j}s^{j}$ (3.56)
>
> Similarly, the same can be done for $\{a_{i}\}_{i\in\mathbf{\mathcal{N}}}$:
>
> $A(s)\equiv\sum_{i=0}^{+\infty}a_{i}s^{i}$ (3.57)
>
> To rewrite (3.55) in terms of (3.56) and (3.57) we just need to multiply the left and right sides by $s^{i}$, and then sum over $i\in\mathbf{\mathcal{N}}$. We do this one step at a time, starting with the left side:
>
> $\pi_{i}\to\sum_{i=0}^{+\infty}\pi_{i}s^{i}\underset{\eqref{eq:def1}}{=}\pi(s)$ (3.58)
>
> And the first term of the right side:
>
> $\pi_{0}a_{i}\to\sum_{i=0}^{+\infty}\pi_{0}a_{i}s^{i}=\pi_{0}\sum_{i=0}^{+\infty}a_{i}s^{i}\underset{\eqref{eq:def2}}{=}\pi_{0}A(s)$ (3.59)
>
> The remaining term is a *shifted convolution* of $\{\pi_{j}\}$ and $\{a_{i}\}$. First, let’s deal with the *shift* $+1$ in the index of $a_{i}$:
>
> $a_{i+1}\to\sum_{i=0}^{+\infty}a_{i+1}s^{i}\underset{\eqref{eq:def3}}{=}\sum_{i=1}^{+\infty}a_{i}s^{i-1}\underset{\eqref{eq:def4}}{=}\frac{1}{s}\sum_{i=0}^{+\infty}a_{i}s^{i}a_{0}s^{0}\underset{\eqref{eq:def5}}{=}\frac{A(s)-a_{0}}{s}$ (3.60)
>
> where in (a) we shifted the index of summation, and in (b) we added and subtracted the 0-th term, so that we may use (3.57) in the last step.
>
>
> On the other hand, the transform of a convolution is just the product of the transformed terms:
>
> $$
> (\pi * a) _ {i} = \sum_ {j = 0} ^ {i} \pi_ {j} a _ {i - j} \rightarrow \sum_ {i = 0} ^ {+ \infty} \sum_ {j = 0} ^ {i} \pi_ {j} a _ {i - j} s ^ {i} = _ {(a)} \sum_ {i = 0} ^ {+ \infty} a _ {i} s ^ {i} \sum_ {j = 0} ^ {+ \infty} \pi_ {j} s ^ {j} = A (s) \pi (s) \tag {3.61}
> $$
>
> This can be thought in analogy with the convolution theorem for Fourier transforms (which are just a particular type of power series transform). Explicitly, the equivalence (a) can be shown as just a matter of rearranging addends. Consider the sum:
>
> $$
> A (s) \pi (s) = \sum_ {i = 0} ^ {+ \infty} a _ {i} s ^ {i} \sum_ {j = 0} ^ {+ \infty} \pi_ {j} s ^ {j} = \sum_ {j = 0} ^ {+ \infty} \pi_ {j} \left(\sum_ {i = 0} ^ {+ \infty} a _ {i} s ^ {i + j}\right) \tag {3.62}
> $$
>
> Graphically, we can write each term with index  $j$  and  $i$  as the entry  $(j,i)$  of a  $\infty \times \infty$  matrix:
>
> $$
> \begin{array}{c c c c} \pi_ {0} a _ {0} & \pi_ {0} a _ {1} s & \pi_ {0} a _ {2} s ^ {2} & \dots \\ \pi_ {1} a _ {0} s & \pi_ {1} a _ {1} s ^ {2} & \pi_ {1} a _ {2} s ^ {3} & \dots \\ \pi_ {2} a _ {0} s ^ {2} & \pi_ {2} a _ {1} s ^ {3} & \pi_ {3} a _ {2} s ^ {4} & \dots \\ \vdots & \vdots & \vdots & \ddots \end{array} \tag {3.63}
> $$
>
> Assuming (3.62) converges, the result will not change if we vary the order of summation. As (3.62) is currently written, we are first summing over all the  $i$ -th row elements, multiplying the result by  $\pi_i$ , then repeating for each row and summing again. Alternatively, we could first sum over elements with the same power of  $s$ , i.e. the ones on the (highlighted) diagonals of (3.63):
>
> $$
> \begin{array}{l} A (s) \pi (s) = \pi_ {0} a _ {0} s ^ {0} + (\pi_ {0} a _ {1} + \pi_ {1} a _ {0}) s ^ {1} + (\pi_ {0} a _ {2} + \pi_ {1} a _ {1} + \pi_ {2} a _ {0}) s ^ {2} + \dots = \\ = \pi_ {0} a _ {0 - 0} s ^ {0} + (\pi_ {0} a _ {1 - 0} + \pi_ {1} a _ {1 - 1}) s ^ {1} + (\pi_ {0} a _ {2 - 0} + \pi_ {1} a _ {2 - 1} + \pi_ {2} a _ {2 - 2}) s ^ {2} + \dots = \\ = \sum_ {i = 0} ^ {+ \infty} s ^ {i} \left(\sum_ {j = 0} ^ {i} \pi_ {j} a _ {i - j}\right) = \sum_ {i = 0} ^ {+ \infty} \sum_ {j = 0} ^ {i} \pi_ {j} a _ {i - j} s ^ {i} \\ \end{array}
> $$
>
> This is called the Cauchy product of two infinite sequences. Note that the argument works only in the infinite case, as there the size of diagonals grows indefinitely. In the finite case, the diagonals grow in size until the main diagonal is reached, and then shrink, meaning that the equivalence (3.61) needs to be corrected.
>
> We can then put together (3.60) and (3.61), obtaining the transform for a shifted convolution. First, denote for simplicity:
>
> $$
> \sum_ {j = 0} ^ {i} \pi_ {j} a _ {i - j} \equiv \mathcal {A} _ {i}
> $$
>
>
> Then the transform of $\mathcal{A}_{i+1}$ is:
>
> $$
> \sum_{j=0}^{i+1} \pi_j a_{i-j+1} \equiv \mathcal{A}_{i+1} \rightarrow \sum_{i=0}^{+\infty} \mathcal{A}_{i+1} = \frac{\sum_{i=0}^{+\infty} \mathcal{A}_i s^i - \mathcal{A}_0}{s} = \frac{\sum_{i=0}^{+\infty} \sum_{j=0}^{i} \pi_j a_{i-j} - \pi_0 a_0}{s} = \frac{A(s) \pi(s) - \pi_0 a_0}{s} \tag{3.64}
> $$
>
> This is close to the transform of the rightmost term in (3.55), with the only difference that the sum in (3.64) starts at 0 and not at 1 as in (3.55). This can be solved by just removing the 0-th "excess" term:
>
> $$
> \sum_{i=0}^{+\infty} \sum_{j=1}^{i+1} \pi_j a_{i-j+1} = \underbrace{\sum_{i=0}^{+\infty} \sum_{j=0}^{i+1} \pi_j a_{i-j+1}}_{(3.64)} - \underbrace{\sum_{i=0}^{+\infty} \pi_0 a_{i+1}}_{\pi_0 \cdot (3.60)} = \frac{A(s) \pi(s) - \pi_0 a_0}{s} - \pi_0 \frac{A(s) - a_0}{s} = \frac{A(s) \pi(s) - \pi_0 A(s)}{s} \tag{3.65}
> $$
>
> And so (3.65) is finally the transform of the rightmost term in (3.55).
>
> Putting (3.58), (3.59) and (3.65) together, we get the full transform of (3.55):
>
> $$
> \pi(s) = \pi_0 A(s) + \frac{A(s) \pi(s) - \pi_0 A(s)}{s} \tag{3.66}
> $$
>
> Supposing the distribution of arrivals is known, $A(s)$ is known. By rearranging we can then find $\pi(s)$:
>
> $$
> \pi(s) = \pi_0 \frac{(s-1) A(s)}{s - A(s)} \tag{3.67}
> $$
>
> $\pi_0$ is a constant factor that can be determined by normalization, noting that:
>
> $$
> \pi(s = 1) = \left. \sum_{i=0}^{+\infty} \pi_i s^i \right|_{s=1} = \sum_{i=0}^{+\infty} \pi_i \stackrel{!}{=} 1
> $$
>
> And the same clearly holds for $A(s)$. Then:
>
> $$
> \lim_{s \to 1^-} \pi(s) = \lim_{s \to 1^-} \pi_0 \frac{(s-1) A(s)}{s - A(s)} = \pi_0 \left( \lim_{s \to 1^-} \frac{s-1}{s - A(s)} \right) \underbrace{\left( \lim_{s \to 1^-} A(s) \right)}_{1} = \pi_0 \lim_{s \to 1^-} \left( 1 - \frac{1 - A(s)}{1 - s} \right)^{-1} = \pi_0 \left[ 1 - A'(1) \right]^{-1} = \frac{\pi_0}{1 - \rho} \stackrel{!}{=} 1
> $$
>
> Where in (a) we used the moment generating property of $A(s)$:
>
> $$
> \left. \frac{\mathrm{d}}{\mathrm{d}s} A(s) \right|_{s=1} = \left. \frac{\mathrm{d}}{\mathrm{d}s} \sum_{i=0}^{+\infty} a_i s^i \right|_{s=1} = \left. \sum_{i=1}^{+\infty} i a_i s^{i-1} \right|_{s=1} = \sum_{i=0}^{+\infty} i a_i = \mathbb{E}[\{a_i\}] \equiv \tag{3.53}
> $$
>
>
> If $\rho < 1$, then $\pi_0 = 1 - \rho$ is an acceptable solution, and can be inserted in (3.67) to find $\pi(s)$, which can then be anti-transformed (either analytically or numerically) to find $\{\pi_j\}$. Clearly, the result will depend on the specific choice of $\{a_i\}$, and so we cannot go further without making more assumptions.
>
> In summary, we distinguish between three cases according to the value of $\rho$:
>
> - $\rho < 1$: our solution is acceptable
> - $\rho = 1$: we do not find a nonzero solution because all $\pi_0 = 0$
> - $\rho > 1$: it would be meaningless since $\pi_0 < 0$
>
> So, we have just shown that the only case where we can find a solution for the stationary equation is when $\rho < 1$, thus making the chain positive recurrent. If the condition on $\rho < 1$ does not hold, a similar procedure can show that the chain can not be positive recurrent.
>
> **Part 2.** Now let us continue by considering the question of transience.
>
> We want then to seek a bounded solution to the equations (3.45), that considering the specific transition matrix $\mathbf{P}$ (3.52) take the form:
>
> $$
> Z_1 = \sum_{j=1}^{\infty} a_j Z_j \tag{3.68}
> Z_i = \sum_{j=0}^{\infty} a_j Z_{i+j-1} \quad i > 1 \tag{3.69}
> $$
>
> Note that we are ignoring the 0-th row of the matrix because the sum in the system (3.45) starts from 1. So in the first equation (3.68) we consider $Z_1$, that is the product between the first row of the matrix $\mathbf{P}$ and the vector $\mathbf{Z}$, and the form of (3.69) follows by using almost the same argument.
>
> To find a solution, we consider the ansatz $Z_i = 1 - s^i$. The first equation (3.68) becomes:
>
> $$
> \begin{aligned}
> i = 1: & 1 - s = \sum_{j=1}^{+\infty} a_j (1 - s^j) = \Big( \underbrace{\sum_{j=0}^{+\infty} a_j}_{1} - a_0 \Big) - \Big( \underbrace{\sum_{j=0}^{+\infty} a_j s^j}_{A(s)} - a_0 \Big) = \\
> & = 1 - g_0 \cdot A(s) + g_0 = 1 - A(s) \Rightarrow s = A(s)
> \end{aligned}
> $$
>
> And similarly for (3.69) we have:
>
> $$
> i > 1: \qquad 1 - s^i = \sum_{j=0}^{+\infty} a_j (1 - s^{i+j-1}) = 1 - s^{i-1} A(s) \Rightarrow s = A(s)
> $$
>
> Both equations take an unique form:
>
> $$
> s = A(s) \tag{3.70}
> $$
>
> which we have already studied before in the example (8) at page 92.
>
>
> We want our solution $Z_{i}=1-s^{i}$ not to be zero, so we need to find a value of $s<1$ that solves (3.70), thus proving that the chain is transient. So we need to study (3.70) and find the intersection between the two curves shown in fig. 3.12.
>
> In the graph we exploit the fact that we have already met $A(s)=\mathbb{E}[s^{x}]$ in the example mentioned above - and in particular we know that $A(s)$ in the interval $s\in[0,1]$ has a value strictly greater than zero, it is *increasing* and *convex*, and lastly $A(1)=1$. A intersection is then present if and only if $A^{\prime}(1)=\rho>1$ holds, meaning that $A(s)$ reaches $1$ “from below”.
>
> This proves that, for $\rho>1$, (3.70) can be solved, and thus the MC is transient due to theorem 3.7.1. However, this is just a sufficient condition, as we are merely consider *one possible way* to solve (3.69) - i.e. one in the form of $Z_{i}=1-s^{i}$ - which we have not proven to be the only possible one. So, if $\rho\leq 1$, the fact that (3.70) has no bounded solution just tells us that the ansatz we made is not valid, with no consequences for the characterization of the MC.
>
> Part 3. In summary, we have demonstrated that if $\rho<1$ then the chain is *positive recurrent*, while if $\rho>1$ the chain is *transient*. Now we want to study the last case, where $\rho=1$.
>
> For $\rho=1$ our chain can either be transient or null recurrent. In order to find which, we will now introduce a new criterion for *recurrence*.

> [!abstract] Theorem 3.7.2.
>
> Recurrence criterion. Consider the following set of inequalities:
>
> $Z_{i}\geq\sum_{j=0}^{+\infty}P_{ij}Z_{j}\quad i\geq 1$ (3.71)
>
> If we are able to find a solution $Z_{i}$ for (3.71) that diverges $Z_{i}\overset{i\to\infty}{\to}\infty$ then the Markov chain is recurrent (either positive or null).

> [!note] Proof.
>
> Omitted. ∎
>
> In our case, (3.71) becomes:
>
> $Z_{i}\geq\sum_{j=0}^{+\infty}P_{ij}Z_{j}=a_{0}Z_{i-1}+a_{1}Z_{i}+a_{2}Z_{i+1}+...=\sum_{j=0}^{+\infty}a_{j}Z_{i+j-1}\quad i\geq 1$
>
> Let us try an obviously divergent solution $Z_{i}=i$:
>
> $i\geq\sum_{j=0}^{+\infty}a_{j}(i+j-1)=i\underbrace{\sum_{j=0}^{+\infty}a_{j}}_{1}+\underbrace{\sum_{j=0}^{+\infty}ja_{j}}_{\rho}-1=i+\rho-1$
>
> The inequality is thus satisfied for all $i\geq 1$ when $\rho\leq 1$, thus concluding that the Markov chain is recurrent thanks to the just introduced criterion.
>
> Now recalling that the MC is:
>
> - Positive recurrent $\Leftrightarrow\rho<1$
>
>
> ![[Stochastic_Processes_2020_p123_img33.jpeg]]
> Figure (3.12) - We need to find the solution of equation 3.70 by drawing the two curves. It is indeed a plot we have already seen before.
>
> - Transient if  $\rho > 1$
>
> We have that for  $\rho = 1$  the Markov chain can not be positive recurrent, but still is recurrent because of the result we have just found, and so it must be null recurrent.

> [!example] Example 13
>
> We want now to provide the solution to the example (10) at page 102 assigned last lecture. We recall its transition matrix:
>
> $$
> \mathbf {P} = \left| \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ a & b & c & 1 - a - b - c \\ 0 & 0 & 0 & 0 \end{array} \right|
> $$
>
> Solution. We were asked to find under which conditions on  $a, b, c$  it holds that:
>
> $$
> \lim _ {n \to \infty} P [ X _ {2 n} = 0 | X _ {0} = 2 ] = \lim _ {n \to \infty} P [ X _ {2 n + 1} = 0 | X _ {0} = 2 ]
> $$
>
> First we set the condition on  $c$ , that must be  $c < 1$ , otherwise the problem would not make sense any more since we are stuck in state 2, and moreover later we would face some mathematical issues.
>
> We start by noting that, given we start in state 2, the only ways we have to end up in state 0 at an even time-step are the following ones. We can either remain in 2 with probability  $c$  for an odd number of time steps and then make the transition to 0 with probability  $a$ , or alternatively stay in 2 for an even number of time steps, make the transition to 1 with probability  $b$ , and finally jump to state 0. These are the only ways we have to end up in state 0 in an even number of time steps, and we have already taken into account that, once we are in the  $\{0,1\}$ , we keep on oscillating between the
>
>
> two states. Explicitly:
>
> $P[X_{2n}=0|X_{0}=2]=\sum_{i=0}^{n-1}c^{2i+1}a+\sum_{i=0}^{n-1}c^{2i}b=(ac+b)\sum_{i=0}^{n-1}c^{2i}=(ac+b)\frac{1-c^{2n}}{1-c^{2}}$
>
> Where in the last passage we recognized that the sum is a geometric truncated. Note moreover that, in the sums, the time we spent in state 2 before the transition distributes geometrically as we expected.
>
> The second expression indeed requests us to be in state 0 in an odd time. There are essentially two ways in which this can occur, similar to the previous ones. We can spend either an *even* number of steps in 2 and then make the transition to state 1, or alternatively remain in 2 for an *odd* time and then do the transition to 0. In the latter however, note as we sum up to $n$ and not $n-1$ as in the previous cases: this is nevertheless irrelevant since the following step will be to consider the limit. Making it explicitly:
>
> $P[X_{2n+1}=0|X_{0}=2]=\sum_{i=0}^{n-1}c^{2i+1}b+\sum_{i=0}^{n}c^{2i}a=bc\frac{1-c^{2n}}{1-c^{2}}+a\frac{1-c^{2n+2}}{1-c^{2}}$
>
> Computing the limit as $n\to\infty$ for both cases we obtain:
>
> $\lim_{n\to\infty}P_{20}^{(2n)}=\frac{ac+b}{1-c^{2}}\quad\lim_{n\to\infty}P_{20}^{(2n+1)}=\frac{bc+a}{1-c^{2}}$
>
> The two limits are the same, thus making the general limit $\lim_{n\to\infty}P_{20}^{(n)}$ exist, only when the two numerators are equal, so:
>
> $ac+b=bc+a\to b(1-c)=a(1-c)\iff a=b$
>
> This is a reasonable solution: if $a$ and $b$ were different, thus privileging a state against the other, then we would introduce a bias in our statistic wrt to the time the entrance to either state 1 or 0. It would reflect into the fact that the evolution may not be balanced, thus making the relative terms of the matrix oscillate for ever (as in the example (9) just before the one we are considering). In this case, there is nothing we can do to make the two limits of the subsequences converge. But on the other hand, having the same probability of entering either state 0 or state 1, is like considering the average over a period: since the transitions rates are now *uniform*, it will make the two limits converge and finally the general one will exist.
> We have just shown that even if we are dealing with classes that show a period, in the case where we start in there, we know we will keep oscillating for ever. Moreover the behaviour of these classes will generally affect also the transition probabilities, in the long run, of entering them starting from a transient states. Nevertheless in some special cases, that are for example when we have a uniform probability to enter either one of the states in the periodic class, the subsequences may converge and the limit may exist.

> [!example] Example 14
>
> Now let us consider a slightly more complex Markov chain with the following transition matrix:
>
> $$
> \mathbf {P} = \left\| \begin{array}{c c c} \mathbf {Q} & \mathbb {R} _ {1} & \mathbb {R} _ {2} \\ 0 & \mathbb {A} & 0 \\ 0 & 0 & 1 \end{array} \right\|
> $$
>
> Where $\mathbf{Q}$ is the transient class, $\mathbb{A}$ is the matrix $\left( \begin{array}{ll}0 & 1\\ 1 & 0 \end{array} \right)$ that has period 2, while $\mathbb{R}_1$ and $\mathbb{R}_2$ are the absorbing classes. We can see as the center block is the periodic block we have seen before.
>
> Try to find the powers of the matrix, in particular even and odd powers and see what the expressions will become for each block. The interesting part is to see under which conditions the $\mathbb{R}_1$ block will not be oscillating any more.
>
> Solution. See (4.7.1) at page 164.
>
>
> CHAPTER 4
>
> Poisson Processes
>
> Poisson processes play a distinct role in modeling many natural phenomena, at least in a first approximation. Moreover, they are mathematically simple, allowing to derive important analytical results and gain some relevant fundamental understanding.
>
> In the following chapter, we will focus on defining and studying the properties of Poisson Processes.

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

> [!abstract] Theorem 4.1.1. Let  $X$  and  $Y$  be independent random variables having Poisson distributions with parameters  $\mu$  and  $\nu$ , respectively. Then the sum  $X + Y$  has a Poisson distribution with parameter  $\mu + \nu$ .
> Theorem 4.1.1. Let  $X$  and  $Y$  be independent random variables having Poisson distributions with parameters  $\mu$  and  $\nu$ , respectively. Then the sum  $X + Y$  has a Poisson distribution with parameter  $\mu + \nu$ .

> [!note] Proof. We proceed by direct computation of the distribution of  $X + Y$ , by searching an expression for  $\mathbb{P}[X + Y = n]$ . Each event  $\{X + Y = n\}$  is made up by the sequence of mutually exclusive events where  $X = k$  for some  $k = 0, \ldots, n$  and consequently  $Y = n - k$ . Thus, due to the law of total probability
> Proof. We proceed by direct computation of the distribution of  $X + Y$ , by searching an expression for  $\mathbb{P}[X + Y = n]$ . Each event  $\{X + Y = n\}$  is made up by the sequence of mutually exclusive events where  $X = k$  for some  $k = 0, \ldots, n$  and consequently  $Y = n - k$ . Thus, due to the law of total probability:
>
> $$
> \mathbb {P} [ X + Y = n ] = \sum_ {k = 0} ^ {n} \mathbb {P} [ X = k, Y = n - k ]
> $$
>
>
> Poisson distribution
>
> Sum of Poisson variables is Poisson
>
>
> Since $X$ and $Y$ are independent, the joint probabilities factorize:
>
> $=\sum_{k=0}^{n}\mathbb{P}[X=k]\mathbb{P}[Y=n-k]=$
> $\mathop{\equiv}_{(4.1)}\sum_{k=0}^{n}\frac{\mu^{k}e^{-\mu}}{k!}\frac{\nu^{n-k}e^{-\nu}}{(n-k)!}=$
>
> Then we pull out a factor $e^{-\mu-\nu}$ that does not depend on $k$, and multiply and divide by $n!$ to highlight a *binomial sum*:
>
> $=\frac{e^{-(\mu+\nu)}}{n!}\underbrace{\sum_{k=0}^{n}\frac{n!}{k!(n-k)!}\mu^{k}\nu^{n-k}}_{(\mu+\nu)^{k}}$
>
> So:
>
> $\mathbb{P}[X+Y=n]=\frac{e^{-(\mu+\nu)}(\mu+\nu)^{n}}{n!}\qquad n=0,1,\ldots$ (4.2)
>
> which is exactly the Poisson Distribution (4.1) with parameter $\mu+\nu$. ∎
>
> Another relevant fact is that *composing* a Poisson distribution with a Binomial one results in another Poisson distribution. More precisely:

> [!abstract] Theorem 4.1.2.
>
> Let $N$ be a Poisson random variable with parameter $\mu$, and conditional on $N$, let $M$ have a binomial distribution with parameters $N$ and $p$. Then the unconditional distribution of $M$ is Poisson with parameter $\mu p$.
>
> In other words, if we pick $N$ objects, with $N$ following a Poisson distribution, and then *keep* each one of them with a given probability $p$, the number $M$ of remaining objects at the end will follow a Poisson distribution with parameter $\mu p\leq\mu$. In a sense, the second *binomial process* acts just as a “filter”, reducing the *effective rate* of the whole process without modifying the form of its distribution.

> [!note] Proof.
>
> See ex. 1.6.1 at page 24. ∎

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

> [!question] Exercise 4.2.1
>
> Defects occur along an undersea cable according to a Poisson process of rate $\lambda=0.1$ per mile.
>
> - What is the probability that no defects appear in the first two miles of the cable?
>
> $X(2)$ has a Poisson distribution with parameter $\lambda t=0.1\cdot 2=0.2$, and so:
>
> $\mathbb{P}[X(2)=0]=e^{-0.2}=0.8187$
> - Given that there are no defects in the first two miles of cable, what is the conditional probability of no defects between mile two and three?
>
> Here we use the independence of $X(3)-X(2)$ and $X(2)-X(0)=X(2)$. So it follows that the conditional probability is the same as the unconditional probability:
>
> $\mathbb{P}[X(3)-X(2)=0]=\mathbb{P}[X(1)=0]=e^{-0.1}=0.9048$

> [!question] Exercise 4.2.2
>
> Customers arrive in a certain store according to a Poisson process of rate $\lambda = 4$ per hour.
>
> - Given that the store opens at 9.00 AM, what is the probability that exactly one customer has arrived by 9.30 and a total of five have arrived by 11.30 AM?
>
> First we set as our unity time the hour, starting from 9.00 AM. We are asked to determine $\mathbb{P}[X(1/2) = 1, X(5/2) = 5]$. Using the independence of $X(5/2) - X(1/2)$ and $X(1/2)$, we reformulate the request as:
>
> $$
> \begin{array}{l}
> \mathbb{P}[X(1/2) = 1, X(5/2) = 5] = \mathbb{P}[X(1/2) = 1, X(5/2) - X(1/2) = 4] = \\
> = \left(\frac{e^{-4(1/2)} \left[4(\frac{1}{2})\right]^1}{1!}\right) \left(\frac{e^{-4(2)} [4(2)]^4}{4!}\right) = (2e^{-2}) \left(\frac{512}{3}e^{-8}\right) = 0.0155
> \end{array}
> $$
>
> **Non-homogeneous processes.** A possible generalization of the Poisson process definition is to *relax* the stationarity hypothesis, by letting the rate $\lambda$ be a function of time: $\lambda(t)$.
>
> This means that the average rate of number of counts per unit of time is not constant anymore, but changes with respect to time. In fact, the probability of a single event occurring in an infinitesimal interval $h$ of time is proportional to $\lambda$:
>
> $$
> \mathbb{P}[X(t + h) - X(t) = 1] = \frac{(\lambda h) e^{-\lambda h}}{1!} = (\lambda h)(1 - \lambda h + O(h^2))) = \lambda h + o(h)
> $$
>
> The probability of $k$ events happening in a time interval $(s, s + t]$ would then be given by:
>
> $$
> \mathbb{P}[X(t + s) - X(s) = k] = \frac{1}{k} \int_{s}^{t + s} (\lambda(t)t)^k e^{-\lambda(t)t}
> $$

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

> [!abstract] Theorem 4.3.1.
>
> Let $\boldsymbol{\epsilon}_{1}$, $\boldsymbol{\epsilon}_{2}...$ be independent Bernoulli random variables, where:
>
> $\mathbb{P}[\boldsymbol{\epsilon}_{i}=1]=p_{i}\quad\text{and}\quad\mathbb{P}[\boldsymbol{\epsilon}_{i}=0]=1-p_{i}$
>
> and let $S_{n}=\boldsymbol{\epsilon}_{1}+\cdots+\boldsymbol{\epsilon}_{n}$. The distribution of $S_{n}$ is given by:
>
> $$
> \mathbb{P}[S_{n}=k]=\!\!\sum_{\begin{subarray}{c}x_{i}=\pm 1\\
> x_{1}+\cdots+x_{n}=k\end{subarray}}\prod_{i=1}^{n}p_{i}^{x_{i}}(1-p_{i})^{1-x_{i}}
> $$ (4.3)
>
> which differs from a Poisson distribution with rate $\mu=p_{1}+\cdots+p_{n}$ by at most:
>
> $$
> \left|\mathbb{P}[S_{n}=k]-\frac{\mu^{k}e^{-\mu}}{k!}\right|\leq\sum_{i=1}^{n}p_{i}^{2}
> $$
>
> In particular, if all $p_{i}\equiv p$ and $Np=\mu$ is kept fixed, in the limit $N\to+\infty$, $p=\mu/N\to 0$, and so does the RHS of 4.4.
>
> An analog of the Law of Rare Events holds for stochastic processes, stating that the total counts of events generated by many independent processes can be approximately described by a single Poisson process.
>
> In other words, consider a high number $M$ of processes (not necessarily Poisson processes) generating events at random times. Each of them can be described by a separate time axis with a certain number of points (representing events) on it. If we combine all axes, and consider only the total number of events $X(t)$ occurred before a given time $t$, without considering their different origin, then, in the limit $M\to\infty$, $X(t)$ would be described by a Poisson process.
>
> Law of Rare Events, fixed probability case
>
> Law of Rare Events: general case
>
> Law of Rare Events applied to Poisson processes
>
>
> As the sum of many discrete random variables will approximately follow a Poisson distribution, so does the combination of many stochastic processes.
>
> This is really useful in reality, because often the events we are interested in can be produced in different ways by different natural phenomena, each following a different law, destroying any hope of a complete description. However, thanks to the Law of Rare Events, we can still describe the counts of these events with a unique Poisson process — even if no one of the underlying stochastic processes is Poisson.

# 4.4 Properties of Poisson Processes

Poisson processes share many of the important properties of the Poisson distribution.

For example, in analogy with theorem 4.1.1, combining two Poisson processes leads to another Poisson process. More formally [2, day 21/04]:

> [!abstract] Theorem 4.4.1. Let  $X_{1}(t)$  and  $X_{2}(t)$  be two independent Poisson Processes with rates  $\lambda_{1}, \lambda_{2}$ . Then, the variable that counts both of them  $X(t) = X_{1}(t) + X_{2}(t)$  is a Poisson process itself with rate  $\lambda = \lambda_{1} + \lambda_{2}$ .
> Theorem 4.4.1. Let  $X_{1}(t)$  and  $X_{2}(t)$  be two independent Poisson Processes with rates  $\lambda_{1}, \lambda_{2}$ . Then, the variable that counts both of them  $X(t) = X_{1}(t) + X_{2}(t)$  is a Poisson process itself with rate  $\lambda = \lambda_{1} + \lambda_{2}$ .
>
> Sum of Poisson processes
>
> ![[Stochastic_Processes_2020_p131_img34.jpeg]]
> Figure (4.1) - Graphical representation of two combined Poisson processes, where their sum is a Poisson process itself with its parameter that is the sum of the two parameters

> [!note] Proof. To prove that  $X(t)$  is a Poisson process, we just need to verify that it satisfies the three requirements in definition 1.
> Proof. To prove that  $X(t)$  is a Poisson process, we just need to verify that it satisfies the three requirements in definition 1.
>
> 1. At the starting time  $t = 0$ , the number of events counted for both processes will be zero ( $X_{1}(0) = X_{2}(0) = 0$ ), and so their sum:  $X(0) = 0$
> 2. Since  $X_{1}$  and  $X_{2}$  have stationary and independent increments separately, so does  $X$  that is their sum. This can be shown explicitly by writing the distribution of  $X$ .
> 3. Given the fact that the random variables  $X_{1}(t)$  and  $X_{2}(t)$  are Poisson distributed with parameter  $\lambda_1 t$  and  $\lambda_2 t$  and are independent of each other, their sum  $X(t) = X_{1}(t) + X_{2}(t)$  is therefore a Poisson distribution with parameter  $(\lambda_1 t + \lambda_2 t)$  as a consequence of theorem 4.1.1.
>
> □
>
> Similarly, filtering a Poisson process by selecting each generated event with a fixed probability  $p$ , results again in a Poisson process in the end, in analogy of what happens in theorem 4.1.2. More formally:

> [!abstract] Theorem 4.4.2. Let  $X(t)$  be a Poisson Process with rate  $\lambda$  and let each event be independently marked as either type 1 with probability  $p$ , or type 2 with probability  $1 - p$ . Then, the events of the type 1 and 2 follow two independent Poisson Processes with rates  $\lambda p$  and  $\lambda (1 - p)$ .
> Theorem 4.4.2. Let  $X(t)$  be a Poisson Process with rate  $\lambda$  and let each event be independently marked as either type 1 with probability  $p$ , or type 2 with probability  $1 - p$ . Then, the events of the type 1 and 2 follow two independent Poisson Processes with rates  $\lambda p$  and  $\lambda (1 - p)$ .
>
> ![[Stochastic_Processes_2020_p132_img35.jpeg]]
> Figure (4.2) - Graphical representation of two split Poisson processes with the conditions stated in theorem 4.4.2

> [!note] Proof. As before, we start by verifying the 3 requirements of definition 1
> Proof. As before, we start by verifying the 3 requirements of definition 1:
>
> 1. When we start counting since there are no events at all, so  $X_{1}(0) = X_{2}(0) = 0$
> 2. Since  $X$  has stationary and independent increments and the marking of events occurs independently, then  $X_{1}$  and  $X_{2}$  inherit from  $X$  the stationarity and independence of their respective increments.
> 3. The joint distribution of the number of arrivals in the two sub-processes before a fixed time  $t$  is:
>
> $$
> \mathbb {P} [ X _ {1} (t) = n, X _ {2} (t) = m ] = \mathbb {P} [ X _ {1} (t) = n | X (t) = n + m ] \mathbb {P} [ X (t) = n + m ] =
> $$
>
> since if  $X(t) = n + m$  and  $X_{1}(t) = n$ , then  $X_{2}(t) = m$ . Note that  $\mathbb{P}[X_1(t) = n|X(t) = n + m]$  is the probability of accepting exactly  $n$  events from  $n + m$  trials, where the success probability of each trial is  $p$ , which is given by a Binomial distribution, leading to:
>
> $$
> \begin{array}{l} = \left( \begin{array}{c} n + m \\ n \end{array} \right) p ^ {n} (1 - p) ^ {m} \frac {e ^ {- \lambda t} (\lambda t) ^ {n + m}}{(n + m) !} = \\ = \frac {(n + m) !}{n ! m !} p ^ {n} (1 - p) ^ {m} e ^ {- \lambda p t} e ^ {- \lambda (1 - p) t} \frac {(\lambda t) ^ {n + m}}{(n + m) !} = \\ = \frac {(\lambda p t) ^ {n} e ^ {- \lambda p t}}{n !} \frac {(\lambda t (1 - p)) ^ {m} e ^ {- \lambda (1 - p) t}}{m !} \\ \end{array}
> $$
>
> which is exactly the product of two Poisson distributions, with rates  $\lambda tp$  and  $\lambda t(1 - p)$  respectively.
>
> From the last point we know that  $X_{1}(t)$  and  $X_{2}(t)$  are independent random variables when they are evaluated at the same instant  $t$ . However, to prove that  $X_{1}$  and  $X_{2}$  are independent Poisson processes, we need to show that the increments  $X_{1}(t_{3}) - X_{1}(t_{1})$  and  $X_{2}(t_{4}) - X_{2}(t_{2})$  are independent for every possible choice of the intervals  $[t_1,t_3]$  and  $[t_2,t_4]$ .
>
>
> - Let's start from the case  $t_1 < t_2 < t_3 < t_4$ , where there is a partial overlap in  $[t_2, t_3]$  (fig. 5.10a). We can split it into two non-overlapping parts  $[t_1, t_2]$  and  $[t_3, t_4]$ , and the overlap  $[t_2, t_3]$ , by rewriting:
>
> $$
> X_{1}(t_{3}) - X_{1}(t_{1}) = [X_1(t_3) - X_1(t_2)] + [X_1(t_2) - X_1(t_1)]
> X_{2}(t_{4}) - X_{2}(t_{2}) = [X_{2}(t_{4}) - X_{2}(t_{3})] + [X_{2}(t_{3}) - X_{2}(t_{2})]
> $$
>
> Since  $X_{1}(t)$  and  $X_{2}(t)$  are independent when evaluated at the same time, the increments on the overlap  $X_{1}(t_{3}) - X_{1}(t_{2})$  and  $X_{2}(t_{3}) - X_{2}(t_{2})$  are independent. In all other cases we are dealing with Poisson increments on disjoint time intervals, which are guaranteed to be independent. Finally, sums of pairwise independent random variables are independent, and so  $X_{1}(t_{3}) - X_{1}(t_{1})$  and  $X_{2}(t_{4}) - X_{2}(t_{2})$  are independent of each other.
>
> - The same reasoning can be applied to all the other overlaps. If  $t_1 < t_2 < t_4 < t_3$ , i.e. if one interval  $[t_2, t_4]$  is inside the other  $[t_1, t_3]$  (fig. 5.10b), we can again split the intervals in three regions: two non-overlapping  $([t_1, t_2]$  and  $[t_4, t_3])$ , and one overlapping  $([t_2, t_4])$ . We then proceed as before.
> - The final case (fig. 4.3c) is trivial, since there is no overlap.
>
> ![[Stochastic_Processes_2020_p133_img36.jpeg]]
> (a) - The two time intervals may be overlapping in some part of them.
>
> ![[Stochastic_Processes_2020_p133_img37.jpeg]]
> (b) - Another case is when a time interval fully contains the other one.
>
> ![[Stochastic_Processes_2020_p133_img38.jpeg]]
> (c) - The last case is where the two time intervals are disjoint.
> Figure (4.3) - All the possible overlaps of two intervals  $[t_1, t_3]$  and  $[t_2, t_4]$ .

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

> [!abstract] Theorem 4.5.1. Inter-arrival times $S_{i}$ are i.i.d. exponential random variables with rate $\lambda$ [1, thm 5.5].
> Theorem 4.5.1. Inter-arrival times $S_{i}$ are i.i.d. exponential random variables with rate $\lambda$ [1, thm 5.5].
>
> Inter-arrival $W_{i} \sim$ Exponential

> [!note] Proof. See the proof theorem (2.2.1) at page 33.
> Proof. See the proof theorem (2.2.1) at page 33.
>
> For the waiting times, we have instead:

> [!abstract] Theorem 4.5.2. The waiting time $W_{n}$, i.e. the time needed for the $n$-th event to occur, has the gamma distribution whose probability density function is [1, thm 5.4]
> Theorem 4.5.2. The waiting time $W_{n}$, i.e. the time needed for the $n$-th event to occur, has the gamma distribution whose probability density function is [1, thm 5.4]:
>
> Waiting times $W_{i} \sim$ Gamma
>
> $$
> f _ {W _ {n}} (t) = \frac {\lambda^ {n} t ^ {n - 1}}{(n - 1) !} e ^ {- \lambda t} \qquad n = 1, 2, \ldots \quad t \geq 0
> $$

> [!note] Proof. Recall the fact that we defined the Gamma distribution in (1.5.4 at pag. 20) with parameters $n, \lambda$, as the distribution of the sum of $n$ i.i.d. exponential random variables with parameter $\lambda$. So, since
> Proof. Recall the fact that we defined the Gamma distribution in (1.5.4 at pag. 20) with parameters $n, \lambda$, as the distribution of the sum of $n$ i.i.d. exponential random variables with parameter $\lambda$. So, since:
>
> $$
> W _ {n} = \sum_ {i = 0} ^ {n - 1} S _ {i}
> $$
>
> where $S_{i}$, $i = 0, \dots, n - 1$ are all exponential random variables with rate $\lambda$, it follows that the sum $W_{n}$ is a Gamma distribution.
>
> If we fix the number $n$ of events occurring in the time interval $(0, t)$, then the joint probability of the arrival times $\{W_i\}_{i=1,\dots,n}$ is that of an ordered sequence of uniformly chosen points, which can be derived from the uniform distribution as follows.
>
> Suppose we choose independently $n$ points $U_{i}$ uniformly in the interval $(0, t)$ (fig. 4.5). The joint distribution of $\{U_{i}\}_{i=1,\dots,n}$ is given by the product of $n$
>
>
> ![[Stochastic_Processes_2020_p135_img40.jpeg]]
> Figure (4.5) - Let us draw some points  $(U_i$ 's) on the interval  $(0, t)$  that distribute uniformly. Then consider also their ordered version  $W_i$ 's. The goal is to compute their statistics.
>
> uniform pdfs.
>
> The situation drastically changes when we consider the order of the points. Let's call  $\{W_i\}$  the sequence of ordered  $U_i$ , with  $0 \leq W_1 < W_2 < \dots < W_n \leq t$ . Note that the  $W_i$  are not independent of each other, since they must satisfy the ordering. This makes much more difficult to compute their joint probability.
>
> So, let us start with the simplest case where we have only two points, and then proceed to generalize. Since we are working with continuous variables, we consider the probability of  $W_{1}$  and  $W_{2}$  respectively being inside two small intervals  $[w_{1}, w_{1} + \Delta w_{1}]$  and  $[w_{2}, w_{2} + \Delta w_{2}]$  (fig. 4.6).
>
> ![[Stochastic_Processes_2020_p135_img41.jpeg]]
> Figure (4.6) - Now let us consider only to points and their corresponding intervals  $[w_i, w_i + \Delta w_i]$ . Note that in either one of the two ordered intervals may be contained either  $U_1$  or  $U_2$ , and there are two possible combinations when assigning them.
>
> In the limit of  $\Delta w_{1},\Delta w_{2}\to 0$  , the probability density  $f_{W_1,W_2}(w_1,w_2)$  is constant inside these intervals, and so:
>
> $$
> f _ {W _ {1}, W _ {2}} \left(w _ {1}, w _ {2}\right) \Delta w _ {1} \Delta w _ {2} = \mathbb {P} \left[ w _ {1} \leq W _ {1} \leq w _ {1} + \Delta w _ {1}, w _ {2} \leq W _ {2} \leq w _ {2} + \Delta w _ {2} \right] \tag {4.5}
> $$
>
> The latter is equal to the probability of  $U_{1}$  (or  $U_{2}$ ) being in  $[w_{1}, w_{1} + \Delta w_{1}]$  and the other in  $[w_{2}, w_{2} + \Delta w_{2}]$ . This is because every permutation of the same  $\{U_{i}\}$ , once ordered, will result in the same collection of  $\{W_{i}\}$ , and so we must count all of them:
>
> $$
> \begin{array}{l} = \mathbb {P} [ w _ {1} \leq U _ {1} \leq w _ {1} + \Delta w _ {1}, w _ {2} \leq U _ {2} \leq w _ {2} + \Delta w _ {2} ] + \\ \mathbb {P} \left[ w _ {1} \leq U _ {2} \leq w _ {1} + \Delta w _ {1}, w _ {2} \leq U _ {1} \leq w _ {2} + \Delta w _ {2} \right] = \\ \end{array}
> $$
>
> Note that we may sum the probabilities of all different permutations since they are mutually exclusive.
>
> Since  $U_{1}$  and  $U_{2}$  are both uniform and independent, we have:
>
> $$
> \mathbb {P} [ w _ {1} \leq U _ {1} \leq w _ {1} + \Delta w _ {1}, w _ {2} \leq U _ {2} \leq w _ {2} + \Delta w _ {2} ] = \frac {\Delta w _ {1}}{t} \frac {\Delta w _ {2}}{t}
> $$
>
>
> and the same holds for every other permutation, leading to:
>
> $$
> f_{W_{1},W_{2}}(w_{1},w_{2})\Delta w_{1}\Delta w=2\left(\frac{\Delta w_{1}}{t}\right)\left(\frac{\Delta w_{2}}{t}\right)=2t^{-2}\Delta w_{1}\Delta w_{2}
> $$
>
> Now, by dividing both (4.5) and (4.6) for $\Delta w_{1}\Delta w_{2}$ and passing to the limit we obtain that:
>
> $$
> f_{W_{1},W_{2}}(w_{1},w_{2})=2t^{-2}
> $$
>
> The 2 comes from the fact that there are only two possible ways in which we can dispose $U_{1}$ and $U_{2}$ in the two intervals.
> By repeating the same reasoning, (4.7) can be generalized to the case of 3 points: $U_{1}$, $U_{2}$, $U_{3}$. This time, there are $2\cdot 3$ possible ways in which we can arrange the 3 elements, and the exponent of $t$ will be $-3$.
> Generalizing this argument up to $n$ elements, the number of permutations of $n$ elements $U_{1},U_{2}...U_{n}$ is $n!$, whereas the joint pdf will be proportional to $t^{-n}$. So, the joint probability density function for $W_{1},W_{2},\ldots,W_{n}$ is given by:
>
> $$
> f_{W_{1},W_{2}...W_{n}}(w_{1},w_{2},...,w_{n})=n!t^{-n}\qquad\mbox{for }0<w_{1}<w_{2}<...<w_{n}\leq t
> $$
>
> Note that the pdf’s domain is not the entire $(0,t)^{n}$, since the $w_{i}$ must be in ascending order.
> On the other hand, the joint pdf for $n$ uniform points in $(0,t)$ is given by:
>
> $$
> f_{U_{1},U_{2},...,U_{n}}(w_{1},w_{2},...,w_{n})=t^{-n}
> $$
>
> with the domain spanning the entire $(0,t)^{n}$, since the $U_{i}$ need not be ordered.
>
> We are finally able to formally state and prove the link between Poisson processes and the ordered uniform distribution:

> [!abstract] Theorem 4.5.3.
>
> Let $W_{1},W_{2},\ldots$ be the ordered occurrence times in a Poisson process of rate $\lambda>0$. Let us condition on $X(t)\equiv N(t)=n$, that is the fact that in interval $(0,t)$ we observe exactly $n$ events. Given their number, the arrival times of $n$ events $\{W_{1},W_{2},\ldots,W_{n}\}$ have the joint probability density function *[1, thm 5.7]*:
>
> $$
> f_{W_{1},...,W_{n}|X(t)=n}(w_{1},\ldots,w_{n})=n!t^{-n}\qquad\mbox{for }0<w_{1}<\cdots<w_{n}\leq t
> $$
>
> Note that this theorem holds only if we are told how many events ($N(t)=n$) we have observed in interval $(0,t)$. In other words the theorem states that, given their number, the arrival times of $n$ events have the joint probability that is equal to the distribution obtained by ordering $n$ independent and uniform random variables.

> [!note] Proof.
>
> Let’s first assume that all $w_{i}$’s are distinct. This can be done because, in a Poisson process, the probability of two events occurring at the same time is negligibly small, and so can be neglected. This is a consequence of the fact that the probability of one arrival in a given interval goes to zero linearly w.r.t. the size of the interval (see section (2.2)). Thus, as the interval’s length goes
>
>
> to zero, the only relevant events will be either one arrival or no arrivals at all. Informally, in a Poisson process "simultaneous events are impossible".
>
> If all  $w_{i}$  are distinct, we can choose intervals  $[w_{i}, w_{i} + \Delta w_{i}]$  such that they are all disjoint, since  $\Delta w_{i}$  can be as small as needed. We can then consider the probability that, given exactly  $n$  arrivals, there  $i$ -th arrival  $W_{i}$  lies inside the  $i$ -th interval  $[w_{i}, w_{i} + \Delta w_{i}]$ :
>
> $$
> \mathbb {P} [ w _ {i} \leq W _ {i} \leq w _ {i} + \Delta w _ {i}, i = 1, \dots , n | X (t) = n ] = \tag {4.11}
> $$
>
> which, in the limit of  $\Delta w_{i}\to 0$ , is linear in the joint probability density  $f_{W_1,\ldots ,W_n|X(t) = n}(w_1,\ldots ,w_n)$ :
>
> $$
> = f _ {W _ {1}, \dots , W _ {n} | X (t) = n} (w _ {1}, \dots , w _ {n}) \Delta w _ {1} \dots \Delta w _ {n} + o (\Delta w _ {1}, \dots , \Delta w _ {n})
> $$
>
> If we can compute (4.11), dividing by the  $n$ -dim volume and taking the limit leads to an expression for the density.
>
> ![[Stochastic_Processes_2020_p137_img42.jpeg]]
> Figure (4.7) - We note as the expression (4.11) requires as there must be no arrivals outside each interval  $[w_i, w_i + \Delta w_i]$ . Each increment, since belongs to a disjoint interval, is independent of the others.
>
> So, let's proceed by computing the probability (4.11). This is the probability that we have exactly one arrival for each interval  $[w_i, w_i + \Delta w_i]$ , while having zero arrivals outside them (fig. 4.7), given that  $n$  events have occurred. Since Poisson increments over disjoint intervals are independent, we have:
>
> $$
> \begin{array}{l} = \mathbb {P} [ \text {o n e a r r i v a l i n} [ w _ {i}, w _ {i} + \Delta w _ {i} ], i = 1, \dots , n \text {a n d} \\ \text {z e r o a r r i v a l s e v e r y w h e r e e l s e i n} [ 0, t ] \mid X (t) = n ] = \\ = \frac {\lambda \Delta w _ {1} e ^ {- \lambda \Delta w _ {1}} \lambda \Delta w _ {2} e ^ {- \lambda \Delta w _ {2}} \dots \lambda \Delta w _ {n} e ^ {- \lambda \Delta w _ {n}} e ^ {- \lambda (t - \sum_ {i = 1} ^ {n} \Delta w _ {i})}}{e ^ {- \lambda t} (\lambda t) ^ {n} / n !} = \\ \end{array}
> $$
>
> Where we recognize the first factors as the probability of exactly one event in each interval  $\Delta w_{i}$ , and the last one as having no events at all in the remaining  $(t - \sum_{i=1}^{n} \Delta w_{i})$ . In order to condition the probability on an event, we had to divide the denominator by the probability of the event to occur. But since  $X(t) = n$  is a Poisson process, this is simply  $e^{-\lambda t} (\lambda t)^{n} / n!$ , that is the probability of having  $n$  events in a time interval of length  $t$ .
>
> Note now that at the numerator the terms  $e^{\lambda \Delta w_1} \ldots e^{\lambda \Delta w_n} = e^{\lambda \sum_{i=1}^{n} \Delta w_i}$  cancel out, and so do  $e^{-\lambda t}$  and  $\lambda$ . At the end we obtain:
>
> $$
> f _ {W _ {1}, \dots , W _ {n} | X (t) = n} (w _ {1}, \dots , w _ {n}) \Delta w _ {1} \dots \Delta w _ {n} + o (\Delta w _ {1}, \dots , \Delta w _ {n}) = n! t ^ {- n} \Delta w _ {1} \dots \Delta w _ {n}
> $$
>
> Dividing both terms by  $\Delta w_{1}\cdot \cdot \cdot \cdot \Delta w_{n}$  and taking the limit  $\Delta w_{i}\to 0\quad i =$
>
>
> $1,\ldots ,n$  completes the proof:
>
> $$
> f _ {W _ {1}, \dots , W _ {n} | X (t) = n} (w _ {1}, \dots , w _ {n}) = n! t ^ {- n}
> $$
>
> We can summarize this result by saying that, if we know how many arrivals we have in a Poisson process in an interval  $(0,t)$ , the joint distribution, conditioned on the number  $n$  of arrivals, is the same that would be obtained by considering  $n$  ordered uniform random variables each distributed in the same interval.
>
> Suppose now that  $n$  events have happened in  $(0, t)$ . Then, the probability of  $k \leq n$  events happening in  $(0, u)$ , with  $u \leq t$ , is given by a Binomial distribution:

> [!abstract] Theorem 4.5.4. Let  $X(t)$  be a Poisson process with rate  $\lambda$ . Given the fact we know that in the interval  $(0, t)$  we have  $n$  arrivals, that is  $X(t) = n$ , we want to find the probability that the number of arrivals in a subset  $0 < u < t$  is  $0 \leq k \leq n$ . Then, in formulas [1, thm 5.6]
> Theorem 4.5.4. Let  $X(t)$  be a Poisson process with rate  $\lambda$ . Given the fact we know that in the interval  $(0, t)$  we have  $n$  arrivals, that is  $X(t) = n$ , we want to find the probability that the number of arrivals in a subset  $0 < u < t$  is  $0 \leq k \leq n$ . Then, in formulas [1, thm 5.6]:
>
>
> ![[Stochastic_Processes_2020_p138_img43.jpeg]]
> Figure (4.8) - Since we know that  $(0,t)$  contains  $n$  events, the arrival times  $X_{n}$  are uniform in  $X_{n}$ , and so each of them will fall into  $(0,u)$  with a probability  $p = u / t$ . So, the probability of  $k$  events being in  $(0,u)$  is that of obtaining  $k$  successes (each with probability  $p$ ) after  $n$  trials, which is given by a Binomial distribution.

> [!note] Proof. In order to prove it we use the results provided by the previous theorem: since given  $X(t) = n$  the  $n$  arrival times are i.i.d. uniformly distributed in the interval  $(0, t)$ , the probability that each falls in the interval  $[0, u]$  is  $u / t$  and therefore  $X(u)$  is binomial with parameters  $(n, u / t)$  thus concluding the proof. This is moreover shown in figure 4.8
> Proof. In order to prove it we use the results provided by the previous theorem: since given  $X(t) = n$  the  $n$  arrival times are i.i.d. uniformly distributed in the interval  $(0, t)$ , the probability that each falls in the interval  $[0, u]$  is  $u / t$  and therefore  $X(u)$  is binomial with parameters  $(n, u / t)$  thus concluding the proof. This is moreover shown in figure 4.8
>
> A similar result holds for the combination of two Poisson processes:

> [!abstract] Theorem 4.5.5. Let  $X_{1}(t), X_{2}(t)$  be two concurrent independent Poisson processes with rates  $\lambda_{1}, \lambda_{2}$ . Given the total number of arrivals in interval  $(0, t)$  i.e.  $X_{1}(t) + X_{2}(t) = n$ , the probability of having  $k$  arrivals in the first process is
> Theorem 4.5.5. Let  $X_{1}(t), X_{2}(t)$  be two concurrent independent Poisson processes with rates  $\lambda_{1}, \lambda_{2}$ . Given the total number of arrivals in interval  $(0, t)$  i.e.  $X_{1}(t) + X_{2}(t) = n$ , the probability of having  $k$  arrivals in the first process is:
>
> $$
> \mathbb {P} \left[ X _ {1} (t) = k \mid X _ {1} (t) + X _ {2} (t) = n \right] = \binom {n} {k} \left(\frac {\lambda_ {1}}{\lambda_ {1} + \lambda_ {2}}\right) ^ {k} \left(\frac {\lambda_ {2}}{\lambda_ {1} + \lambda_ {2}}\right) ^ {n - k} \tag {4.12}
> $$
>
>
> As expected, this probability is given by a binomial distribution.
>
> In fact, the probability $p_{1}$ of a generic event belonging to 1 is the ratio between the rate $\lambda_{1}$ of 1, and the total rate $\lambda_{1}+\lambda_{2}$ of both processes. If $\lambda_{1}=\lambda_{2}$, $p_{1}=1/2$ as expected, since in this case we are combining two equal Poisson processes. If, for instance, $\lambda_{1}=2\lambda_{2}$, then $p_{1}=2/3$, while $p_{2}=1/3=1-p_{1}$ is the probability of an event belonging to 2.

> [!note] Proof.
>
> We proceed by direct computation of the LHS of (4.12) by applying the definition of conditional probability, leading to:
>
> $$
> \frac{\mathbb{P}[X_{1}(t)=k,\ X_{1}(t)+X_{2}(t)=n]}{\mathbb{P}[X_{1}(t)+X_{2}(t)=n]}=
> $$
>
> If $X_{1}(t)+X_{2}(t)=n$ and $X_{1}(t)=k$, then $X_{2}(t)=n-k$. Then, since $X_{1}$ and $X_{2}$ are independent processes, we can factorize the joint probability:
>
> $$
> =\frac{\mathbb{P}[X_{1}(t)=k\ ,\ X_{2}(t)=n-k]}{\mathbb{P}[X_{1}(t)+X_{2}(t)=n]}=
> =\frac{e^{-\lambda_{1}t}(\lambda_{1}t)^{k}}{k!}\frac{e^{-\lambda_{2}t}(\lambda_{2}t)^{n-k}}{(n-k)!}\frac{n!}{e^{-(\lambda_{1}t+\lambda_{2}t)}(\lambda_{1}t+\lambda_{2}t)^{n}}=
> =\binom{n}{k}\left(\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}\right)^{k}\left(\frac{\lambda_{2}}{\lambda_{1}+\lambda_{2}}\right)^{n-k}
> $$
>
> which completes the proof. ∎
>
> Finally, we can compose theorems 4.5.4 and 4.5.5 as follows:

> [!abstract] Theorem 4.5.6.
>
> Let $X_{1}(t)$ and $X_{2}(t)$ be two independent Poisson processes with rates $\lambda_{1}$, $\lambda_{2}$ in the interval $(0,t)$. Let $s$ be a subset of $t$ s.t. $0<s<t$. Given we know the total number $n$ of arrivals in the interval $(0,t)$ i.e. $X_{1}(t)+X_{2}(t)=n$, the probability of $0\leq k\leq n$ events occurring for process $1$ in the subset $(0,s)$ is given by:
>
> $$
> \mathbb{P}[X_{1}(s)=k|X_{1}(t)+X_{2}(t)=n]=\frac{n!}{k!(n-k)!}\left(\frac{\lambda_{1}s}{(\lambda_{1}+\lambda_{2})t}\right)^{k}\left(\frac{\lambda_{1}(t-s)+\lambda_{2}t}{(\lambda_{1}+\lambda_{2})t}\right)^{n-k}
> $$

> [!note] Proof.
>
> We proceed again by direct computation. By applying the definition of conditional probability we have:
>
> $$
> \mathbb{P}[X_{1}(s)=k|X_{1}(t)+X_{2}(t)=n]=\frac{\mathbb{P}[X_{1}(s)=k,\ X_{1}(t)+X_{2}(t)=n]}{\mathbb{P}[X_{1}(t)+X_{2}(t)=n]}=
> $$
>
> If $n$ events have occurred in $X_{1}+X_{2}$ during $(0,t)$, $k$ of which belonging to 1 in the interval $(0,s)$, then $n-k$ events must have occurred in $X_{2}$ during $(0,t)$ or in $X_{1}$ during $(s,t)$, i.e. $X_{1}(t)-X_{1}(s)+X_{2}(t)=n-k$. Now all of these random variables are independent, and so the joint probability factorizes:
>
> $$
> =\frac{\mathbb{P}[X_{1}(s)=k,\ X_{1}(t)-X_{1}(s)+X_{2}(t)=n-k]}{\mathbb{P}[X_{1}(t)+X_{2}(t)=n]}=
> $$
>
>
> ![[Stochastic_Processes_2020_p140_img44.jpeg]]
>
> ![[Stochastic_Processes_2020_p140_img45.jpeg]]
> Figure (4.9) - The situation can be described by using this graph: we are dealing with a large interval  $(0, t)$  which contains  $(0, s)$ , that is the base of rectangle. There are moreover two processes  $\lambda_1$  and  $\lambda_2$  that rule the number of arrivals, and either them individually or their sum can be drawn onto the vertical axis. The product between the two sides of the rectangle returns the parameters defining the Poisson process we are interested in.
>
> This result has a geometric interpretation (fig. 4.9). In particular, the term  $\left(\frac{\lambda_1s}{(\lambda_1 + \lambda_2)t}\right)^k$  is the ratio between the small area in the figure, representing the event we are looking for, and the larger area, i.e. the conditional event.

# 4.5.1  $\mathbf{M} / \mathbf{G} / \infty$  queue

We want now to use the theorems we have just proved by analyzing the following example, dealing with a radioactive mass material.

A similar one would be a service station where each user arrives according to a Poisson process at time  $W_{k}$ . A customer will remain in the station for a certain amount of time  $Y_{k}$  and then will depart. The difference between these examples and the ones we saw in the previous lectures ( $M / G / XX$ ), is that in this case there is no waiting times for service: once a customer enters the system he will not wait his turn and will be immediately served, no matter how many clients are already being served. We can then state that the number of services is therefore infinite, and describe our problem as a  $\mathbf{M} / \mathbf{G} / \infty$  queue. In this formalism  $M(t)$  is the Poisson distribution that describes our arrivals, whereas  $G(t)$  denotes the generic distribution of waiting times, while  $\infty$  tells that we can serve an infinite number of customers at the same time.


![[Stochastic_Processes_2020_p141_img46.jpeg]]
Figure (4.10) – The figure depicts example (15). Particle created at time $W_{k} \leqslant t$ still exists at time $t$ if $W_{k} + Y_{k} \geqslant t$

> [!example] Example 15
>
> Viewing a fixed mass of a certain radioactive material, suppose that *alpha* particles appear in time according to a Poisson process of intensity $\lambda$. Each particle exists for a random duration and is then annihilated. Suppose that the successive lifetimes $Y_{1}, Y_{2}, \ldots$ of distinct particles are independent random variables having the common distribution function $G(y) = Pr\{Y_{k} \leqslant y\}$. Let $X(t)$ be the total number of particles created up to time $t$, and let $M(t)$ count the number of alpha particles existing at time $t$. Obviously it must hold that $M(t) \leqslant X(t)$, since the number of existing particles cannot exceed the number of particles created. The problem is depicted in figure 4.10.
>
> We want now to find the number of particles present at time $t$: so we want to compute $M(t)$ given that at the beginning the timer was zero, i.e. $M(0) = 0$. We moreover condition on the number $n$ of particles emitted up to time $t$, that is $X(t) = n$, where $W_{1},\ldots ,W_{n}\leqslant t$ are the times when particles were created. Then, for each particle emitted, we have that the particle $k$ still exists if and only if $W_{k} + Y_{k}\geqslant t$: the sum of its arrival and service times must be greater than the actual time $t$. Let us introduce the indicator function such that indicates whether a particle still exists at time $t$:
>
> $$
> \mathbb {1} \{W _ {k} + Y _ {k} \geqslant t \} = \left\{ \begin{array}{l l} 1 & \quad \text{if } W _ {k} + Y _ {k} \geqslant t \\ 0 & \quad \text{if } W _ {k} + Y _ {k} < t \end{array} \right.
> $$
>
> Summing on all indicator functions corresponding to all particles, we then obtain the probability that the number of existing particles is equal to $m$, conditioned on the total number of particles created up to time $t$ that is $n$.
>
> $$
> Pr\{M(t) = m \mid X(t) = n\} = Pr\left\{\sum_{k=1}^{n} \mathbb{1}\{W_k + Y_k \geqslant t\} = m \mid X(t) = n\right\} = \tag{4.13}
> $$
>
> We can notice that on the rhs we have something in function of $W_{k}$ given the total number of arrivals $n$. It should remind us that given the condition on $n$, the theorem we proved last lecture states that the joint statistics of
>
>
> the $W_{1},...,W_{n}$ is the same statistics we would have by dealing with ordered version of i.i.d. random variables in $(0,t)$. Moreover we can see that the expression $\{W_{k}+Y_{k}\geqslant t\}$ does not depend on the order of $W_{k}$. For example, in the case we had the following quantity $\sum_{k=1}^{n}kW_{k}$, we would notice that actually it depends on the arrival times: the later it is, the more it weights in the sum. So in this case the order would be important.
> But since $\{W_{k}+Y_{k}\geqslant t\}$ is completely symmetric i.e. it is invariant on the permutation of $W$’s and we have the condition $X(t)=n$, the theorem (4.11) allows us to replace the $W_{i}$’s with the same number of i.i.d. uniform random variables $U_{i}$’s in the interval $(0,t]$, not facing any issue. We thus obtain:
>
> $$
> Pr\Big{\{}\sum_{k=1}^{n}\mathbb{1}\{W_{k}+Y_{k}\geqslant t\}=m|X(t)=n\Big{\}}=Pr\Big{\{}\sum_{k=1}^{n}\mathbb{1}\{U_{k}+Y_{k}\geqslant t\}=m\Big{\}}=
> $$
>
> Note that the rhs becomes now independent of the total number of arrivals $X(t)=n$, since we are already considering it by taking the sum. Moreover both $U_{k}$ and $Y_{k}$ are i.i.d., so each of indicator function is a binary random variable independent of all others. The sum of these $n$ indicator function is thus binomial with parameters $n$ and $p$ that is computed as:
>
> $$
> p=Pr\{U_{k}+Y_{k}\geqslant t\}=\frac{1}{t}\int_{0}^{t}Pr\{Y_{k}\geqslant t-u\}du=
> $$
>
> Where we brought $U_{k}$ to the rhs and then condition it to $U_{k}$, thus obtaining $u$. In order to remove the latter condition, we can average over the distribution of $U_{k}$’s that is uniform in the interval $(0,t)$, so we need to divide it by the length of the interval. Moreover we notice that $Pr\{Y_{k}\geqslant t-u\}$ is the complementary distribution of $G(y=t-u)$:
>
> $$
> =\frac{1}{t}\int_{0}^{t}(1-G(t-u))du=\frac{1}{t}\int_{0}^{t}[1-G(z)]dz
> $$
>
> Where in the last step we just introduced a new variable $z=t-u$.
> Now that we have obtained the probability of the binomial distribution we can rewrite (4.13) as:
>
> $$
> Pr\{M(t)=m|X(t)=n\}=\frac{n!}{m!(n-m)!}p^{m}(1-p)^{n-m}
> $$
>
> Where $p$ is the one we have just computed. In order to remove the condition $X(t)=n$ we marginalize over the distribution of $X$ that we know is Poisson. Given that we have a binomial distribution of parameters $(n,p)$ and $n$ is Poisson distributed itself, if we want to find the unconditional distribution of $M(t)$ we obtain a new Poisson, where the new $\lambda$ is then scaled according to $p$ of the binomial. Mathematically:
>
> $$
> Pr\{M(t)=m\}=\sum_{n=m}^{\infty}Pr\{M(t)=m|X(t)=n\}Pr\{X(t)=n\}=
> =\sum_{n=m}^{\infty}\frac{n!}{m!(n-m)!}p^{m}(1-p)^{n-m}\frac{(\lambda t)^{n}e^{-\lambda t}}{n!}=e^{-\lambda t}\frac{(\lambda pt)^{m}}{m!}\sum_{n=m}^{\infty}\frac{(1-p)^{n-m}(\lambda t)^{n-m}}{(n-m)!}
> $$
>
> Where the infinite sum is an exponential series and reduces according to:
>
> $$
> \sum_{n=m}^{\infty}\frac{(1-p)^{n-m}(\lambda t)^{n-m}}{(n-m)!}=\sum_{j=0}^{\infty}\frac{[\lambda t(1-p)]^{j}}{j!}=e^{\lambda t(1-p)}
> $$
>
> Thus obtaining the unconditional distribution that is nothing more than the $X(t)$ distribution, where we are rescaling $\lambda$ using the probability $p$ as we have already told before:
>
> $$
> Pr\{M(t)=m\}=\frac{e^{-\lambda pt}(\lambda pt)^{m}}{m!}\qquad for\ m=0,1,...
> $$
>
> But recalling how we introduced $p$, we have that at any time the number of particles existing at time $t$ has a Poisson distribution whose mean is:
>
> $$
> \lambda pt=\lambda\int_{0}^{t}[1-G(y)]dy
> $$
>
> Note that the parameter is time varying, but it is worth to see what is the behaviour of the system for long times, since it might be settled into some stationary values. As $t\to\infty$ (4.14) becomes the expected service time, since the integrand is $[1-G(y)]$, that is the tail of the distribution $G(y)$. For a generic $t$, the value of the integral depends on the details of the specific distribution $G(y)$, whereas in the long run it depends only on the mean $\mu$. This implies that in the long run two distributions will converge, despite they are different, if both have the same mean. Note also that in the case where the lifetime of a particle has a maximum finite value $t_{MAX}$, as long as we are integrating in a region ($t^{\prime}>t_{MAX}$) exceeding this upper bound value, the tail distribution $[1-G(y)]\to 0$ since $G(y)=1$. This implies that the asymptotic behaviour for the two different distributions, observed for $t\to\infty$, can be found also for $t$ exceeding the maximum lifetime of a particle, if it is finite.
> Finally, we conclude by saying that in inference terminology $\int_{0}^{\infty}[1-G(y)]dy$ is the inverse of the average service rate $\mu$. In other words:
>
> $$
> \lambda pt=\lambda\int_{0}^{\infty}[1-G(y)]dy=\lambda/\mu
> $$

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

> [!abstract] Theorem 4.6.1. Let  $[X(t)]$  be a Poisson process of rate  $\lambda >0$ . Then for  $0 < u < t$  and  $0\leqslant k\leqslant n$ ,
> Theorem 4.6.1. Let  $[X(t)]$  be a Poisson process of rate  $\lambda >0$ . Then for  $0 < u < t$  and  $0\leqslant k\leqslant n$ ,
>
> $$
> P r \{X (u) = k | X (t) = n \} = \frac {n !}{k ! (n - k) !} \left(\frac {u}{t}\right) ^ {k} \left(1 - \frac {u}{t}\right) ^ {n - k}
> $$
>
> We have already proved this theorem by using (4.5.3), but there is also an other way that is often requested during written tests and it is worth to see and understand better. We will now see how to prove this theorem directly.

> [!note] Proof. Straightforward computations give
> Proof. Straightforward computations give:
>
> $$
> P r \{X (u) = k | X (t) = n \} =
> = \frac {P r \{X (u) = k \text{ and } X (t) = n \}}{P r \{X (t) = n \}} = \frac {P r \{X (u) = k \text{ and } X (t) - X (u) = n - k \}}{P r \{X (t) = n \}}
> $$
>
> Where we simply used the definition of conditional event. The situation is described by the figure:
>
> ![[Stochastic_Processes_2020_p146_img48.jpeg]]
> Figure (4.12) - Note as the two intervals  $(0, u)$  and  $(u, t)$  are disjoint, so increments are independent of each other. Whereas  $(0, u)$  and  $(0, t - u)$  overlap, thus not being independent despite they share the same statistics.
>
> The numerator of the fraction above expresses the joint probability of having  $k$  events in the shorter interval  $(0, u)$  and  $n$  overall in interval  $(0, t)$ . This second
>
>
> event can be written as having $n-k$ arrivals in the shorter interval $(u,t)$. Note that the two intervals $(0,u)$ and $(u,t)$ are disjoint, and so the two corresponding events are independent random variables: this is the first property we use in this passage. Secondly, we must say that the increment in the interval $(u,t)$ is the same as the increment in interval $(0,t-u)$: it is based on the Poisson property that the increments are stationary and so depend only on the length of the interval. For the last property we could have replaced $X(t)-X(u)$ with $X(t-u)$ making no errors since they both share the same statistics, but ONLY AFTER an intermediate step where we have factorized the two probabilities: the two increments $X(u)$ and $X(t-u)$ refer to the two superimposing intervals $(0,u)$ and $(0,t-u)$, thus not being independent of each other.
>
> This allows us to write it as the product of the two individual probabilities, and we know that all of them are Poisson:
>
> $$
> =\frac{\{e^{-\lambda u}(\lambda u)^{k}/k!\}\{e^{-\lambda(t-u)}[\lambda(t-u)]^{n-k}/(n-k)!\}}{e^{-\lambda t}(\lambda t)^{n}/n!}=
> $$
>
> And simplifying:
>
> $$
> =\frac{n!}{k!(n-k)!}\frac{u^{k}(t-u)^{n-k}}{t^{n}}
> $$
>
> That is an other way to write the expression pointed out in the theorem, so concluding our proof. $\Box$
>
> Let us consider the dual situation of the theorem we have just introduced:

> [!abstract] Theorem 4.6.1
>
> (dual version)
>
> $$
> Pr\{X(s)=k|X(t)=n\}\qquad 0\leqslant n\leqslant k,\quad 0<t<s
> $$
>
> Here we want to compute the probability of having $k$ arrivals in the largest interval $(0,s)$, conditioned on the fact that we have already had $n$ arrivals in the interval $(0,t)$. Obviously this is equivalent to have $k-n$ arrivals in the interval $(t,s)$ as it is shown in the picture, thus having two probabilities referring to two different disjoint intervals. By using the definition of conditioned probability:
>
> $$
> \frac{Pr\{X(s)=k\ ,\ X(t)=n\}}{Pr\{X(t)=n\}}=
> \frac{Pr\{X(t)=n\ ,\ X(s)-X(t)=k-n\}}{Pr\{X(t)=n\}}=
> $$
> But since the two joint probabilities refer to two disjoint intervals, they are independent of each other, so factorizable.
>
> $$
> =\frac{Pr\{X(t)=n\ \}Pr\{\ X(s)-X(t)=k-n\}}{Pr\{X(t)=n\}}=Pr\{X(s-t)=k-n\}=
> $$
>
>
> Where in the last passage we used the fact that the two increments are stationary, so $X(s)-X(t)$ and $X(s-t)$ actually have the same statistics. Recall that this must be done ONLY AFTER we have factorized the two terms as shown above. In fact, $X(t)$ and $X(s)-X(t)$ are independent since they refer to disjoint intervals, whereas $X(t)$ and $X(t-s)$ refer to overlapping intervals thus not being independent even if they share the same statistics: skipping the intermediate passage would be wrong. We finally recognize the last probability as a Poisson process:
>
> $$
> Pr\{X(s-t)=k-n\}=\frac{e^{-\lambda(s-t)}(\lambda(s-t))^{k-n}}{(k-n)!}
> $$
>
> ###### Exercise 4.6.1 (Written test - June 27, 2016)
>
> Consider two independent Poisson processes $X_{1}(t)$ and $X_{2}(t)$, where $X_{i}(t)$ is the number of arrivals for process $i$ during $[0,t]$. The average number of arrivals per unit time of the two processes is $\lambda_{1}=0.5$ and $\lambda_{2}=1$ respectively.
>
> 1. Compute $P[X_{1}(2)=1|X_{1}(3)=2]$ and $P[X_{1}(3)=2|X_{1}(2)=1]$
> 2. Compute $P[X_{1}(1)=1|X_{1}(2)+X_{2}(2)=3]$ and $P[X_{1}(2)+X_{2}(2)=3|X_{1}(1)=1]$
> 3. Compute $P[X_{1}(2)+X_{2}(2)=3|X_{1}(3)=0]$ and $P[X_{1}(2)+X_{2}(2)=3|X_{1}(3)=1]$
>
> Solution.
>
> 1) The first probability we need to compute refers to the same process, but different intervals. We know, from the previous theorem (4.6.1) that, given the number of arrivals in the large interval, the probability of having a certain number of events in the smaller one is binomially distributed with parameters $(n=2,p=2/3)$, where $p$ is given by the ratio of the length of the two intervals. So the computations return:
>
> $$
> P[X_{1}(2)=1|X_{1}(3)=2]={2\choose 1}\left({2\over 3}\right)^{1}\left({1\over 3}\right)^{2-1}={4\over 9}\simeq 0.44
> $$
>
> Now we do the opposite: we want to know, given the number of arrivals in the small interval that is $X_{1}(2)=1$, what is the probability of having a certain number of events $X_{1}(3)=2$ in the large one. In other words, we want to compute the probability that $X_{1}(3)-X_{1}(2)=3-2=1$. In formulas:
>
> $$
> P[X_{1}(3)=2|X_{1}(2)=1] =P[X_{1}(3)-X_{1}(2)=1]=
> =P[X_{1}(1)=1]=0.5e^{-0.5}\simeq 0.3
> $$
>
> 2) The second question involves $X_{1}$ given the condition of the sum of $X_{1}+X_{2}$. This should reminds us of the theorem (4.5.5), where recalling the picture
>
>
> (4.9) we can associate the bigger rectangle with the event that gives us the condition where the two processes are combined in the large interval $(0,t)$: its area will indeed be the parameter $(\lambda_{1}+\lambda_{2})t$ of the corresponding Poisson event. Whereas the small rectangle is associated to the probability we are request to compute. We will have then a binomial with parameters $(n,p)$, where $n$ is the total number of arrivals, and $p$ is the ratio between the two areas. Let us compute the probability:
>
> $$
> P[X_{1}(1)=1|X(2)=3]=\binom{3}{1}\binom{1}{6}^{1}\binom{5}{6}^{3-1}=\frac{25}{72}\simeq 0.347
> $$
>
> where we introduced as a new variable $X(t)=X_{1}(t)+X_{2}(t)$.
>
> Now we want to switch the roles: given that the area of the small rectangle, we want to find the probability that the large one will have a certain area. This is, obviously, equivalent to constraint the value of the difference between the large and the small surfaces. What happens in the difference is itself a Poisson variable with parameter that is the area of the region, i.e. the sum of the two rectangles ($[\lambda_{1},\lambda_{1}+\lambda_{2}]\times[0,2]\cup[0,\lambda_{1}]\times[1,2]$) that is $2.5$. In formulas:
>
> $$
> P[X(2)=3|X_{1}(1)=1]=P[X_{2}(2)+X_{1}(2)-X_{1}(1)=2]=\frac{(2.5)^{2}e^{-2.5}}{2}\simeq 0.2565
> $$

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


> [!question] Exercise 4.6.2 (Chap IV - Prob. 1.3)
>
> A Markov chain has the transition probability:
>
> |   | 0 | 1 | 2 | 3 | 4 | 5  |
> | --- | --- | --- | --- | --- | --- | --- |
> |  0 | α1 | α2 | α3 | α4 | α5 | α6  |
> |  1 | 1 | 0 | 0 | 0 | 0 | 0  |
> |  2 | 0 | 1 | 0 | 0 | 0 | 0  |
> |  3 | 0 | 0 | 1 | 0 | 0 | 0  |
> |  4 | 0 | 0 | 0 | 1 | 0 | 0  |
> |  5 | 0 | 0 | 0 | 0 | 1 | 0  |
>
> where  $\alpha_{i}\geqslant 0$ ,  $i = 1,\ldots ,6$  and  $\sum_{i = 1}^{6}\alpha_{i} = 1$ .
>
> - Determine the limiting probability of being in state 0.
>
> ![[Stochastic_Processes_2020_p151_img50.jpeg]]
> Figure (4.14) - Transition matrix of exercise 4.6.2
>
> Solution. For a process as depicted in figure 4.14 we can write the following stationary equations, where we have obtained the row vector  $\vec{\pi}$  by multiplying itself for each column of the matrix  $\mathbf{P}$ :
>
> |  π0= π0α1+π1  |
> | --- |
> |  π1= π0α2+π2  |
> |  π2= π0α3+π3  |
> |  π3= π0α4+π4  |
> |  π4= π0α5+π5  |
> |  π5= π0α6  |
>
> We can then start rewriting the system starting from the last row, and then replace recursively the  $\pi_i$  with the  $\pi_{i + 1}$  computed in the row below, thus obtaining the following system:
>
> |  π0=(α1+α2+α3+α4+α5+α6)π0  |
> | --- |
> |  π1=(α2+α3+α4+α5+α6)π0  |
> |  π2=(α3+α4+α5+α6)π0  |
> |  π3=(α4+α5+α6)π0  |
> |  π4=(α5+α6)π0  |
> |  π5=α6π0  |
>
>
> Where we know that  $\sum_{i=1}^{6} \alpha_i = 1$ , so for each  $i$ -th row of the system we note that the limiting probability becomes  $1 - \alpha_i$ , that is the probability of being at least in the  $i$ -th state. We can now proceed to solve the system and find the stationary solutions, that are all determined except for the common factor  $\pi_0$  which will be computed by applying the normalization condition  $\sum_{i=0}^{5} \pi_i = \left( \sum_{k=1}^{6} k \alpha_k \right) \pi_0 = 1$ , that is the mean of the distribution of the  $\alpha$ 's. Now we want to understand what the distribution does: as shown in the image 4.14 starting from the state 0, it selects a generic  $i$ -th state and then deterministically goes back to zero one step per time, so taking  $i + 1$  steps to go back to the starting point. For example, if from 0 we go to state 4 with probability  $\alpha_5$ , then it will take 5 time steps to come back to 0. If we go to state 2 with probability  $\alpha_3$ , then we will be back in 3 time steps, and so on. Generalizing: given we start from 0, with probability  $\alpha_k$  my return time in 0 will be  $k$ .
>
> Note as the formula  $\left(\sum_{k=1}^{6} k\alpha_{k}\right)\pi_{0} = 1$  is the average return time to 0, that corresponds to the inverse of the probability of being in that state in the long run, as we would expect from theory. Finally we conclude that:
>
> $$
> \pi_ {0} = \frac {1}{\sum_ {i = 1} ^ {6} k a _ {k}} = \frac {1}{\text {mean of} \alpha \text {distribution}}
> $$

> [!question] Exercise 4.6.3 (Chap IV - Prob. 4.4)
>
> A similar exercise to the previous one is the following: let  $\{\alpha_{i}:i = 1,2,\ldots \}$  be a probability distribution, and consider the Markov chain whose transition probability matrix is:
>
> |   | 0 | 1 | 2 | 3 | 4 | 5 | ...  |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> |  0 | α1 | α2 | α3 | α4 | α5 | α6 | ...  |
> |  1 | 1 | 0 | 0 | 0 | 0 | 0 | ...  |
> |  2 | 0 | 1 | 0 | 0 | 0 | 0 | ...  |
> |  3 | 0 | 0 | 1 | 0 | 0 | 0 | ...  |
> |  4 | 0 | 0 | 0 | 1 | 0 | 0 | ...  |
> |  5 | 0 | 0 | 0 | 0 | 1 | 0 | ...  |
> |  : | : | : | : | : | : | : | ..  |
>
> Note that the difference with the previous one is that we are now dealing with an infinite Markov chain.
>
> - What condition on the probability distribution  $\{\alpha_{i} : i = 1,2,\ldots\}$  is necessary and sufficient in order that a limiting distribution exist, and what is this limiting distribution? Assume  $\alpha_{1} > 0$  and  $\alpha_{2} > 0$  so that the chain is aperiodic.
>
> Solution. The solution is similar to the previous problem. Recall that the row vector  $\vec{\pi}$  is obtained by multiplying itself for each column of the matrix  $\mathbf{P}$ .
>
> The first component becomes  $\pi_0 = \alpha_1\pi_0 + \pi_1$ . Thus solving for  $\pi_1 = (1 -$
>
>
> $\alpha_{1})\pi_{0}$.
> The second equation will become: $\pi_{1}=\alpha_{2}\pi_{0}+\pi_{2}$ and replacing with the value we have just found for $\pi_{1}$ we can write: $\pi_{2}=(1-\alpha_{1}-\alpha_{2})\pi_{0}$. Iteratively we find that for a generic $\pi_{n}$ the limiting distribution will be:
>
> $$
> \pi_{n}=\left(\sum_{k=n+1}^{\infty}\alpha_{k}\right)\pi_{0}
> $$
>
> Here we recall that $\sum_{n=0}^{\infty}\pi_{n}=1$, and by imposing this condition by summing over all $\pi$’s and finally solving the equation for $\pi_{0}$ we obtain:
>
> $$
> \pi_{0}=\left(\sum_{n=0}^{\infty}\sum_{k=n+1}^{\infty}\alpha_{k}\right)^{-1}=\left(\sum_{n=0}^{\infty}P[X>n]\right)^{-1}
> $$
>
> Obviously the double sum $\sum_{n=0}^{\infty}\sum_{k=n+1}^{\infty}\alpha_{k}$ must converge to a finite value, otherwise the $\alpha_{k}$’s distribution would not exist and we could have not solved for $\pi_{0}$. In that case the $\vec{\pi}$ would be made of all $0$’s thus not being an acceptable solution for the system, that is why the double sum must converge. We recall moreover the meaning of $\alpha_{k}$, that is the probability $P[x=k]$. When we sum $\sum_{k=n+1}^{\infty}$ we are then considering the probability $P[x>n]$. On the other hand, the sum $\sum_{n=0}^{\infty}P[x>n]$ is the average of the distribution, so once again we find that $\pi_{0}$ is the inverse of the average distribution of the return times in $0$. This is indeed valid only because when we pick a value $n$ for the distribution $\alpha_{n}$, then the first return time to the starting point will be exactly of $n$ time steps.
>
> ###### Exercise 4.6.4 (Chap IV - Prob. 1.4):
>
> A finite state regular Markov chain has transition probability matrix $\mathbf{P}=|P_{ij}|$ and limiting distribution $\pi=|\pi_{i}|$. In the long run, what fraction of the transitions are from a prescribed state $k$ to a prescribed state $m$?
>
> Solution. First we should recall that transition probabilities are conditional probabilities, indeed we want to compute the probability to come to a certain state $m$ given we started in an other one $k$. For any transition, it must hold that first we must find ourselves in state $k$, and then from state $k$ we must go to state $m$. The problem thus asks us to compute:
>
> $$
> \pi_{k}P_{km}=\lim_{n\rightarrow\infty}P[X_{n}=k\ ,\ X_{n+1}=m]
> $$
>
> We could even have added the condition on the initial state, but since the chain is regular we know from theory that it is not important where we start, so we can neglect it.

> [!question] Exercise 4.6.5 (Chap IV - Prob. 1.6)
>
> Determine the following limits in terms of the transition probability matrix $\mathbf{P} = |P_{ij}|$ and limiting distribution $\pi = |\pi_i|$ of a finite state regular Markov chain $\{X_{n}\}$:
>
> 1. $\lim_{n\to \infty}P[X_{n + 1} = j|X_0 = i]$
> 2. $\lim_{n\to \infty}P[X_n = k, X_{n + 1} = j|X_0 = i]$
> 3. $\lim_{n\to \infty}P[X_{n - 1} = k, X_n = j|X_0 = i]$
>
> Solution. 1) Here the precise step, being it either $n$ or $n + 1$ or $n - 1$, is not so important because we are considering the limit as $\lim_{n\to \infty}$. Moreover, since the chain is regular, this limit will be independent of the starting condition, so we basically need to compute:
>
> $$
> \lim _ {n \to \infty} P [ X _ {n + 1} = j | X _ {0} = i ] = \pi_ {j}
> $$
>
> 2) Here we neglect as well the initial condition since the chain is regular. There is in addition a joint probability referring to two consecutive states: we are requested to be in state $k$ in the long run, that happens with probability $\pi_{k}$, and starting from there going to state $j$ according to the transition probability $P_{kj}$. So we need to compute:
>
> $$
> \lim _ {n \to \infty} P [ X _ {n + 1} = j | X _ {n} = k, X _ {0} = i ] P [ X _ {n} = k | X _ {0} = i ]
> $$
>
> Where we first used the definition of conditional probability, and noting that we can drop the initial condition $X_0 = i$ in the first factor since it is older than $X_n = k$. We have already found $\lim_{n\to \infty}P[X_n = k|X_0 = i] = \lim_{n\to \infty}P[X_{n + 1} = k|X_0 = i] = \pi_k$. Finally, knowing that the first term is the one step transition probability we can write:
>
> $$
> \lim _ {n \to \infty} P [ X _ {n} = k, X _ {n + 1} = j | X _ {0} = i ] = \pi_ {k} P _ {k j}
> $$
>
> 3) The third one, in the limit as $n \to \infty$ is the time shifted version of the probability we had to find in the point 2), namely:
>
> $$
> \lim _ {n \to \infty} P [ X _ {n} = k, X _ {n + 1} = j | X _ {0} = i ] = \lim _ {n \to \infty} P [ X _ {n - 1} = k, X _ {n} = j | X _ {0} = i ] = \pi_ {k} P _ {k j}
> $$

> [!question] Exercise 4.6.6 (Chap IV - Prob. 1.13)
>
> A Markov chain has the transition probability matrix:
>
> $$
> \mathbf{P}=\begin{array}[]{c c c c}0&1&2\\
> 0&\left|\begin{array}[]{c c c}0.4&0.4&0.2\\
> 1&0.6&0.2&0.2\\
> 2&0.4&0.2&0.4\end{array}\right|\\
> \end{array}
> $$
>
> After a long period of time, you observe the chain and see that it is in state 1. What is the conditional probability that the previous state was state 2? That is, find:
>
> $$
> \lim_{n\to\infty}P[X_{n-1}=2|X_{n}=1]
> $$
>
> Solution. Note that this problem is slightly different from the ones we have already solved: we are now looking at the chain backward. We write the definition of conditional probability:
>
> $$
> P[X_{n-1}=2|X_{n}=1]=\frac{P[X_{n-1}=2\ ,\ X_{n}=1]}{P[X_{n}=1]}=
> \frac{P[X_{n}=1|X_{n-1}=2]P[X_{n-1}=2]}{P[X_{n}=1]}=P_{21}\frac{P[X_{n-1}=2]}{P[X_{n}=1]}=
> $$
>
> Where we wrote the joint probability in the numerator as a conditional one. We recognized that the first term is the one step transition probability, namely $P_{21}$. Note that in the limit, as $n\to\infty$, both the numerator and denominator converge respectively to $\pi_{2}$ and $\pi_{1}$ since the Markov chain is regular and it does not depend on the initial state.
>
> $$
> =\lim_{n\to\infty}P_{21}\frac{\pi_{2}}{\pi_{1}}=\frac{6}{35}\simeq 0.1714
> $$
>
> Where $P_{21}=0.2$ and $\pi_{1}$ and $\pi_{2}$ must be computed by solving the stationary equations.

> [!question] Exercise 4.6.7 (Chap IV - Prob 4.7)
>
> An individual either drives his car or walks in going from his home to his office in the morning, and from his office to his home in the afternoon. He uses the following strategy: if it is raining in the morning, then he drives the car, provided it is at home to be taken. Similarly, if it is raining in the afternoon and his car is at the office, them he drives the car home. He walks on any morning or afternoon that it is not raining or the car is not where he is. Assume that, independent of the past, it rains during successive mornings and afternoon with constant probability $p$. In the long run, on what fraction of *days* does our man walk in the rain? What if he owns two cars?
>
>
> Solution. First let us consider the time in "trips" unit, and not as we would normally do in days: every day there will be two trips. Let us define the following states:
>
> - $X_{n}=1$ if the car is available, i.e. at the same place of our man
> - $X_{n}=0$ otherwise
>
> Let us now think about the transition matrix of the problem. For the first row we reason as it follows: if the guy does not have the car, so we are in state $X_{n}=0$, in the next trip he will not be able to do anything but walk. Note that when he walks, he will walk to the place where the car actually is, so necessarily $X_{n+1}=1$.
>
> On the other hand, if he has the car, so being in $X_{n}=1$, at the place where he is and he walks back he will have to leave the car, so the at the next trip he will not have the car, thus being $X_{n+1}=0$. But we know that he drives only when it is raining, so $P_{10}=1-p$, namely the probability that it does not rain. Whereas, if it rains with probability $p$, he will drive thus having the car available for the following trip, thus remaining in $X_{n+1}=1$. The transition probability matrix takes the form:
>
> It is indeed a Markov chain: whether the car will be next step depends on where it is now, and on whether it rains with probability $p$. These two present notions will let us to fully characterize the next step, without any knowledge about previous states required.
>
> Now we want to find the long run probability $\pi_{0}$ and $\pi_{1}$ to characterize the behaviour of the chain for long times. Recall now that they are proportional to the incoming probability, so $1-p$ and $1$, and normalized by the sum of the twos. Namely:
>
> $$
> \pi_{0}=\frac{1-p}{2-p}\qquad\pi_{1}=\frac{1}{2-p}
> $$
>
> We want now to find the probability for a given day that the guy walks in the rain. In order to do that, let us condition on what happens in the morning, whether he has the car or not:
>
> $$
> \pi_{0}p+\pi_{1}(1-p)p=\frac{2p(1-p)}{2-p}
> $$
>
>
> Where the first term corresponds to the event that he does not have the car, which happens with probability $\pi_{0}$ in the long run, and then he walks to the office where his car was left the previous day. In this trip he may get wet, according to the fact that is raining or not with probability $p$. While, for the second term, if he does have the car in the morning which occurs with probability $\pi_{1}$, he will not get wet if it is already raining: he would drive to the office and then have the car for the rest of the day. Whereas, if in the morning it is not raining with probability $1-p$, he will walk to the office leaving the car at home. In the case that in the afternoon rains with probability $p$, he will not have the car and thus get wet walking.
>
> In the case where the man has two cars things are slightly different. We define as $X_{n}$ the number of the car where our man is, so if we are in state $X_{n}=0$ then our man will have no cars at his disposal, while for $X_{n}=2$ he will have both of them. The transition probability matrix will be:
>
> $$
> \mathbf{P}=\begin{array}[]{c c c c}&0&&1&2\\
> 0&&0&0&1\\
> 1&&0&1-p&p\\
> 2&&1-p&p&0\end{array}
> $$
>
> Where, as before, the last row describes the situation where the guy starts and has no cars $X_{n}=0$: he will surely go in the next step where there are both of them, so $X_{n+1}=2$ with probability $1$. Then, on the following trip i.e. starting with one car $X_{n}=1$, it will not be allowed for him to go state $0$: if it will be raining then he will drive thus having two cars $X_{n+1}=2$ with probability $p$, if not he will leave the car where it is and remain in state $X_{n+1}=1$ with probability $1-p$. The last case is where he starts having two cars $X_{n}=2$, in the case in rains with probability $p$ he will be able to drive only one car thus having one car for the following trip $X_{n+1}=1$. Otherwise, cars will remain as they actually are, and our man will have no cars at his disposal $X_{n+1}=0$ with probability $1-p$. Obviously, the third possibility is impossible, he can either leave both cars to the place he leaves, or drive either one of them.
>
> Applying a similar reasoning as before we can find the stationary probability for the three different states, that are respectively:
>
> $$
> \pi_{0}=\frac{1-p}{3-p}\qquad\pi_{1}=\frac{1}{3-p}\qquad\pi_{2}=\frac{1}{3-p}
> $$
>
> The possibility that, in the long run, the guy gets wet will be then:
>
> $$
> \pi_{0}p+\pi_{2}(1-p)p=\frac{2p(1-p)}{3-p}
> $$

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

> [!note] Proof.
>
> In order to prove this we need a couple of assumptions. The first one is that the system is stable, in other words it must be able to reach all $n$ possible steady states with probability larger than zero: the chain must be positive recurrent. The second one is that $\mathbf{N(t)}$, that describes the number of users in the system at time $t$, must change by unit steps like it happens in
>
>
> Random Walk processes. This is reasonable: we are allowed to have a single arrival thanks to the Poisson process property where multiple arrivals can not occur. On the other hand, assuming that we have only one server, only one person will leave after each service, so decrementing  $N(t)$  by a unit. These are actually not strong assumptions for our system: a relatively simple one may satisfy them.
>
> ![[Stochastic_Processes_2020_p162_img53.jpeg]]
> Figure (4.19) - For a stable system we know that we will find it empty with probability 1 an infinite number of times. We can prove it by fixing a value  $n$  a see how many transition upward or downward we encounter with respect to this level.
>
> The first consequence we face once we have assumed that the system is stable, is that in the long run it will be empty an infinite number of times with probability 1. Having fixed a value of  $n$ , for each upward transition there must the relative downward transition, or else the system would not be stable: we know that we will come back to 0 for sure in the future.
>
> Moreover, when we reach a larger value than  $n$  obviously we had to pass through  $n$  itself: no jumps are allowed because the second condition stated above.
>
> In summary, any time the queue empties we will count both a upward and a downward transitions.
>
> Clearly when transition  $n \to n + 1$  occurs, i.e. an user arrives, the latter will find the system in the  $n$ -th state. It is true also the converse: any time a downward transition occurs, i.e.  $n + 1$ -th customer leaves the system, we will find ourselves in state  $n$ .
>
> Let us now compute the total number of transitions  $\mathbf{n} \to \mathbf{n} + \mathbf{1}$  in the generic interval  $[0, t]$ . This is equivalent to compute the number of arrivals in  $[0, t]$  which find the system in state  $n$ . Let us normalize it to the number of the total upward transitions from a generic state  $k$ :
>
> $$
> \frac {\# \text {o f} n \rightarrow n + 1 \text {t r a n s i t i o n s i n} [ 0 , t ]}{\# \text {o f} k \rightarrow k + 1 \text {t r a n s i t i o n s i n} [ 0 , t ] \forall k}
> $$
>
> We note that the denominator is the total number of arrivals in the  $[0, t]$  interval. The ratio is then the fraction of arrivals in interval  $[0, t]$  that find our system in state  $n$ .
>
> Following the same procedure for the departures:
>
> $$
> \frac {\# \text {o f} n + 1 \rightarrow n \text {t r a n s i t i o n s i n} [ 0 , t ]}{\# \text {o f} k + 1 \rightarrow k \text {t r a n s i t i o n s i n} [ 0 , t ] \forall k}
> $$
>
> where this is indeed the fraction of departures that leave behind the system in state  $n$ .
>
> Recalling that for each upward transition there must be a downward one, there-
>
>
> fore the difference between the two numerators must return at most 1, depending on the instant when we sample our system. Sampling, for example, when the system is in a state  $j > n$ , then their difference will return one. In the other case, sampling at  $j' < n$ , will return 0 because either we haven't made any upward transition over the  $n$ -th state, or we have already made its relative downward one.
>
> The fact that the system is stable ensures that, in the limit as  $t \to \infty$ , all the terms in both fractions go to infinity. On the other hand, the difference between the number of upward and downward transitions, that is at most 1, must vanish being it a finite number.
>
> Finally both fractions will converge to an unique value. It holds that:
>
> $$
> \lim_{t\to \infty}\frac{\# \mathrm{of} n\to n + 1\mathrm{transitions~in~}[0,t]}{\# \mathrm{of} k\to k + 1\mathrm{transitions~in~}[0,t]\forall k} = \lim_{t\to \infty}\frac{\# \mathrm{of} n + 1\to n\mathrm{transitions~in~}[0,t]}{\# \mathrm{of} k + 1\to k\mathrm{transitions~in~}[0,t]\forall k}
> $$
>
> In the limit, the probability that an arriving user finds the system in state  $n$  will be the same for a departing user to leave the state in state  $n$ .
>
> This basically proves the equality:
>
> $$
> d _ {n} = a _ {n} \qquad n = 0, 1, \dots .
> $$
>
> Consequently our previous analysis made for  $M / G / 1$  queue was consistent and legitimate: even when we considered the embedded Markov Chain subsampling at specific instants, we obtained a result that was representative of the whole behaviour of the chain.
>
> ![[Stochastic_Processes_2020_p163_img54.jpeg]]
> Figure (4.20) - Sketch depicting the situation of problem 14. We have a transient block, that can lead either to an absorbing block or to a periodic class.

> [!question] Exercise 4.7.1
>
> Now we want to discuss the solution for the periodic class exercise (14) at page 125. Recalling its transition matrix:
>
> $$
> \mathbb {P} = \left\| \begin{array}{c c c} \mathbb {Q} & \mathbb {R} _ {1} & \mathbb {R} _ {2} \\ 0 & \mathbb {A} & 0 \\ 0 & 0 & 1 \end{array} \right\| \qquad \text {w h e r e}   \mathbb {A} = \left\| \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right\| \qquad \text {a n d}   \mathbb {A} ^ {n} = \left\{ \begin{array}{c c c} \left\| \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right\| & n o d d \\ 1 & 0 \\ 0 & 1 \end{array} \right\} n e v e n
> $$
>
>
> As we can see our chain has a recurrent periodic class  $\mathbb{A}$  of period 2, a transient class  $\mathbb{Q}$  that is connected to the first one thanks to the block  $\mathbb{R}_1$ , and to the last absorbing class thanks to  $\mathbb{R}_2$ . Note that the block  $\mathbb{A}$  will never have a limit because it will oscillate deterministically between the its two states for ever.
>
> Now we want to study the behaviour of  $\mathbb{P}^n$  as  $n$  increases, in particular focusing on the behaviour of the block  $\mathbb{R}_1$ , that may have a limit under certain assumptions. Recall that we know already, from (13) at page 123, that the two subsequences for  $\mathbb{P}^{2n}$  and  $\mathbb{P}^{2n + 1}$  present different limits, but now we wonder whether they might converge to the same one according to some conditions, and therefore making the general limit to exist. We can then easily compute  $\mathbb{P}^2$  and  $\mathbb{P}^3$ :
>
> $$
> \mathbb {P} ^ {2} = \left[ \begin{array}{c c c} \mathbb {Q} ^ {2} & \mathbb {Q R} _ {1} + \mathbb {R} _ {1} \mathbb {A} & \mathbb {Q R} _ {2} + \mathbb {R} _ {2} \\ 0 & \mathbb {A} ^ {2} & 0 \\ 0 & 0 & \mathbb {1} \end{array} \right]
> \mathbb {P} ^ {3} = \left[ \begin{array}{c c c} \mathbb {Q} ^ {3} & \mathbb {Q} ^ {2} \mathbb {R} _ {1} + \mathbb {Q} \mathbb {R} _ {1} \mathbb {A} + \mathbb {R} _ {1} \mathbb {A} ^ {2} & \mathbb {Q} ^ {2} \mathbb {R} _ {2} + \mathbb {Q} \mathbb {R} _ {2} + \mathbb {R} _ {2} \\ 0 & \mathbb {A} ^ {3} & 0 \\ 0 & 0 & \mathbb {1} \end{array} \right]
> $$
>
> We then recognize a pattern, that can be proven by induction as well, while computing  $\mathbb{P}^{n + 1}$ :
>
> $$
> \begin{array}{l} \mathbb {P} ^ {n + 1} = \left[ \begin{array}{c c c} \mathbb {Q} ^ {n + 1} & \mathbb {Q} ^ {n} \mathbb {R} _ {1} + \mathbb {Q} ^ {n - 1} \mathbb {R} _ {1} \mathbb {A} + \ldots + \mathbb {Q} \mathbb {R} _ {1} \mathbb {A} ^ {n - 1} + \mathbb {R} _ {1} \mathbb {A} ^ {n} & \left(\sum_ {i = 0} ^ {n} \mathbb {Q} ^ {i}\right) \mathbb {R} _ {2} \\ 0 & \mathbb {A} ^ {n + 1} & 0 \\ 0 & 0 & \mathbb {1} \end{array} \right] = \\ = \left[ \begin{array}{c c c} \mathbb {Q} ^ {n + 1} & \sum_ {i = 0} ^ {n} \mathbb {Q} ^ {i} \mathbb {R} _ {1} \mathbb {A} ^ {n - i} & \left(\sum_ {i = 0} ^ {n} \mathbb {Q} ^ {i}\right) \mathbb {R} _ {2} \\ 0 & \mathbb {A} ^ {n + 1} & 0 \\ 0 & 0 & \mathbb {1} \end{array} \right] = \mathbb {P} ^ {n + 1} \\ \end{array}
> $$
>
> and we want to know whether  $\lim_{n\to \infty}\sum_{i = 0}^{n}\mathbf{Q}^i\mathbb{R}_1\mathbb{A}^{n - i}$  this limit exists. For even  $n$  we can replace  $n = 2k$  and:
>
> $$
> \sum_ {i = 0} ^ {2 k} \mathbb {Q} ^ {i} \mathbb {R} _ {1} \mathbb {A} ^ {2 k - i} = \sum_ {j = 0} ^ {k} \mathbb {Q} ^ {2 j} \mathbb {R} _ {1} + \sum_ {j = 0} ^ {k - 1} \mathbb {Q} ^ {2 j + 1} \mathbb {R} _ {1} \mathbb {A} =
> $$
>
> where we split the initial sum into two terms: the first contains the even indices and the last one the odd indices. Note that if  $i$  is even then also  $2k - 2j$  will be also even, so  $\mathbb{A}^{2k - 2j} = \mathbb{1}$  and thus is absent in the first term. Whereas for the second one we remember that  $\mathbb{A}^{2k + 1 - 2j} = \mathbb{A}$ . We can rewrite the two sums
>
>
> by using the associative property thus obtaining:
>
> $$
> =\left(\sum_{j=0}^{k}\mathbb{Q}^{2j}\right)\mathbb{R}_{1}+\left(\sum_{j=0}^{k-1}\mathbb{Q}^{2j}\right)\mathbb{Q}\mathbb{R}_{1}\mathbb{A}\xrightarrow{k\to\infty}\left[\mathbb{1}-\mathbb{Q}^{2}\right]^{-1}(\mathbb{R}_{1}+\mathbb{Q}\mathbb{R}_{1}\mathbb{A})
> $$
>
> Where in the last step we used the fact that the two sums are both geometric and, for large $k$, they converge to the same value that is $[\mathbb{1}-\mathbb{Q}^{2}]^{-1}$. Recall that we are dealing with matrices, so the term $[\mathbb{1}-\mathbb{Q}^{2}]$ is a matrix itself, of which we need to take the inverse.
>
> Whereas for odd $n=2k+1$. Using the same argument and splitting the sum into two sums with even and odd indices, and recalling how $\mathbb{A}^{n}$ behaves for different $n$ we obtain:
>
> $$
> \sum_{i=0}^{2k+1}\mathbb{Q}^{i}\mathbb{R}_{1}\mathbb{A}^{2k+1-i}=\sum_{j=0}^{k}\mathbb{Q}^{2j}\mathbb{R}_{1}\mathbb{A}+\sum_{j=0}^{k}\mathbb{Q}^{2j+1}\mathbb{R}_{1}=
> $$
>
> That can be rewritten by collecting the common factors as:
>
> $$
> \left(\sum_{j=0}^{k}\mathbb{Q}^{2j}\right)(\mathbb{R}_{1}\mathbb{A}+\mathbb{Q}\mathbb{R}_{1})\xrightarrow{k\to\infty}\left[\mathbb{1}-\mathbb{Q}^{2}\right]^{-1}(\mathbb{R}_{1}\mathbb{A}+\mathbb{Q}\mathbb{R}_{1})
> $$
>
> where as before we recognized the geometric sum.
>
> The limits of the two different subsequences are the same if it holds that:
>
> $$
> [\mathbb{1}-\mathbb{Q}^{2}]^{-1}(\mathbb{R}_{1}+\mathbb{Q}\mathbb{R}_{1}\mathbb{A})=[\mathbb{1}-\mathbb{Q}^{2}]^{-1}(\mathbb{R}_{1}\mathbb{A}+\mathbb{Q}\mathbb{R}_{1})
> $$
>
> Where we should have checked that $\mathbb{Q}$ is invertible. But recalling that it is a stochastic process matrix, then we now that it must be invertible and so $\mathbb{Q}$, $\mathbb{Q}^{2}$ and $[\mathbb{1}-\mathbb{Q}]$ are. Rearranging the terms:
>
> $$
> \mathbb{R}_{1}+\mathbb{Q}\mathbb{R}_{1}\mathbb{A}=\mathbb{R}_{1}\mathbb{A}+\mathbb{Q}\mathbb{R}_{1}\Rightarrow(\mathbb{1}-\mathbb{Q})\mathbb{R}_{1}=(\mathbb{1}-\mathbb{Q})\mathbb{R}_{1}\mathbb{A}
> $$
>
> That returns us the condition for them to be equal that is:
>
> $$
> \mathbb{R}_{1}=\mathbb{R}_{1}\mathbb{A}
> $$
>
> Note that the term $\mathbb{R}_{1}\mathbb{A}$ is nothing more but $\mathbb{R}_{1}$ where we switched the columns. So the limit for the two subsequences coincide, thus making the general limit exist, only if the columns of $\mathbb{R}_{1}$ are identical. In a statistical point of view, it gives us the condition for the general limit to exist that when we enter a periodic class from a transient state, we do it uniformly. It is indeed a generalization of what we saw some time ago.

> [!question] Exercise 4.7.2 (Chap V - P. 1.7)
>
> Shocks occur to a system according to a Poisson process of rate  $\lambda$ . Suppose that the system survives each shock with probability  $\alpha$ , independently of other shocks, so that its probability of surviving  $k$  shocks is  $\alpha^k$ . What is the probability of surviving at time  $t$ ?
>
> Solution. This exercise can be solved in two ways. The first one, that is the more linear, we want to find:
>
> $$
> P[\text{survive at time } t] = \sum_{k=0}^{\infty} P[\text{survive at time } t \mid k \text{ shocks occurred}] P[k \text{ shocks occurred}] =
> $$
>
> Where we used the law of total probability. We know in addiction that the probability for  $k$  shocks to occur is Poisson distributed with parameter  $\lambda$ , and for the system to survive  $k$  shocks is  $\alpha^k$ . So we obtain:
>
> $$
> = \sum_ {k = 0} ^ {\infty} \alpha^ {k} \frac {e ^ {- \lambda t} (\lambda t) ^ {k}}{k !} = e ^ {- \lambda t} \sum_ {k = 0} ^ {\infty} \frac {(\alpha \lambda t) ^ {k}}{k !} = e ^ {- \lambda t} e ^ {\lambda \alpha t} = e ^ {- \lambda (1 - \alpha) t}
> $$
>
> Where we simply took out of the sum the term independent of  $k$  and finally we applied the sum definition of the exponential function. For the second path to solve this exercise, we should have noticed that the last result could be interpreted as the probability of having 0 events, for a process with parameter  $\lambda (1 - \alpha)$ .
>
> ![[Stochastic_Processes_2020_p166_img55.jpeg]]
> Figure (4.21) - In the problem (4.7.2), once a shock as occurred the system can either survive with probability  $\alpha$ , or not survive with probability  $1 - \alpha$ .
>
> The probability, once a shock occurred, for the system to be alive is then  $\alpha$ , whereas with probability  $1 - \alpha$  it would be fatal. So we have already seen as a split Poisson process is a Poisson process itself with the rate rescaled, in this case by a factor  $\lambda(1 - \alpha)$ , where the  $\lambda$  belongs to the original process. We are requested to compute then the probability for no shock of the "fatal" kind to occur up to time  $t$ , that is a Poisson with parameter  $\lambda(1 - \alpha)$  and  $k = 0$ : it is indeed equal to the one we have found above.

> [!question] Exercise 4.7.3 (Chap V - P. 1.10)
>
> Customers arrive at a facility at random according to a Poisson process of rate  $\lambda$ . There is a waiting time cost of  $c$  per customer per unit time. The customer gather at the facility and are processed or dispatched in groups at fixed times  $T, 2T, 3T, \ldots$ . Any time we dispatch some customers, there is a dispatch cost of  $K$ . The process is depicted in the following graph.
>
> 1. What is the total dispatch cost during the first cycle from time 0 to time  $T$ ?
> 2. What is the mean total customer waiting cost during the first cycle?
> 3. What is the mean total customer waiting + dispatch cost per unit time during the first cycle?
> 4. What value of  $T$  minimizes this mean cost per unit time?
>
> ![[Stochastic_Processes_2020_p167_img56.jpeg]]
> Figure (4.22) - The number of customers in a dispatching system as a function of time for problem (4.7.3)

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

> [!question] Exercise 4.7.4 (Chap V - Ex. 2.4)
>
> Suppose that a book of 600 pages contains a total of 240 typographical errors uniformly distributed over the pages. Develop a Poisson approximation for the probability that three particular successive pages are error-free.
>
> Solution. When we make the assumption that errors are uniformly distributed, then it implies that each error can be found in a page with probability 1/600. The number of errors on a unique given page we know it follows a binomial distribution, where $p=1/600$ is rather small and conversely $n=240$ is quite high. The given distribution can be approximated by a Poisson with rate $np$, and in formula:
>
> $$
> \text{Binom}\left(n=240,p=\frac{1}{600}\right)\simeq\text{Poisson}(np=0.4)
> $$
>
> That is the distribution of number of errors on a given page. Making the assumption that each error is independent of the others, and more specifically on the others on different pages, we should notice that we are computing the probability of having 0 errors on three different and disjoint intervals. It does not matter the order of the pages, so we can neglect the request of the problem that they need to be successive, as long as they are distinct pages. The probability requested will be Poisson distributed itself, with rate that is $3\cdot np$: three times the one we stated before for a single page. Formally:
>
>
> $$
> P[3\text{ pages are error-free}]\simeq e^{-1.2}
> $$
>
> There is no difference indeed when considering any three pages, or consecutive three pages of the book: the total size of the interval (i.e. number of pages) is the relevant quantity for the Poisson process and not not their position as long as they are disjoint.

> [!question] Exercise 4.7.5 (Chap V - Ex. 2.5)
>
> Suppose that $N$ points are uniformly distributed over the surface o fa circular disk of radius $r$. Determine the probability distribution for the number of points within a distance of 1 of the origin as $N\to\infty$, $r\to\infty$ in such a way that the ratio $N/(\pi r^{2})=\lambda$ is still constant.
>
> Solution. The extension of Poisson processes to bidimensional systems is quite natural: once we know that the points that fall inside a certain surface are Poisson distributed, we know for sure that their number will depend exclusively on the measure of the area, and will be independent of both the position and the shape because of the stationary increments property. In addition, when we consider two disjoint areas, their increments will be independent of each other. These are the postulates for bidimensional Poisson processes.
>
> ![[Stochastic_Processes_2020_p169_img57.jpeg]]
> Figure (4.23) – Bidimensional Poisson processes will be independent of both the position and the shape of the two areas, as long as they are disjoint. The number of events counted will be indeed function only of the measure.
>
> We want now to count how many points fall in the small circle of radius 1, given that they are uniformly distributed in the larger circle of radius $r$. Each of these points has the probability of being inside the inner circle of radius $R=1$, that is the ratio between the two areas:
>
> $$
> P[\text{being inside small circle}]=\frac{\pi R^{2}}{\pi r^{2}}=\frac{1}{r^{2}}
> $$
>
> Number of points in the small circle will be then binomial of the kind ($n=N,p=1/r^{2}$). Now, in the limit as $N\to\infty$, $r\to\infty$ s.t. the average number of points per unit area $N/(\pi r^{2})=\lambda$ is still constant: $\lambda$ is indeed the density of points. It follows that $N/r^{2}=\pi\lambda$ will be fixed as well. Recall that when in a Binomial distribution we let in the limit $N\to\infty$ and $p\to 0$ keeping their product constant, we obtain a Poisson distribution with parameter $\lambda\pi$, that is the average number of points in the inner circle.
>
>
> We have shown that when we pick a large number of uniformly distributed points in a surface, it can be assimilated to a 2-dim Poisson process because the probability of falling in any area in the limit where  $N, r \to \infty$  will be Poisson.
>
> ![[Stochastic_Processes_2020_p170_img58.jpeg]]
> Figure (4.24) - Sketch depicting the situation of problem, where the inner circle has radius 1 while the other  $r$ .

> [!question] Exercise 4.7.6 (Chap V - Ex. 3.6)
>
> For  $i = 1, \dots, n$  let  $\{X_i(t); t \geqslant 0\}$  be independent Poisson processes, each with the same parameter  $\lambda$ . Find the distribution of the first time that at least one event has occurred in every process.

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


> [!question] Exercise 4.7.7 (Chap V - P. 3.6)
>
> Customers arrive at a holding facility at random according to a Poisson process having rate  $\lambda$ . The facility processes in batches of size  $Q$ . That is, the first  $Q - 1$  customers wait until the arrival of the  $Q$ -th customer. Then all are passed simultaneously, and the process repeats. Service times are instantaneous. Let  $N(t)$  be the number of customers in the holding facility at time  $t$ . Assume that  $N(0) = 0$  and let  $T = \min(t \geqslant 0; N(t) = Q)$  be the first dispatch time.
>
> Show that:
>
> 1.  $\mathbb{E}[T] = Q / \lambda$
> 2. the expected total waiting time is  $\mathbb{E}[\int_0^T N(t)dt] = [1 + 2 + \dots + (Q - 1)] / \lambda = Q(Q - 1) / 2\lambda$ .
>
> ![[Stochastic_Processes_2020_p171_img60.jpeg]]
> Figure (4.26) - Sketch depicting the situation of problem 4.7.7
>
> Solution. a) First it is to be noted that interarrival times between customers are exponential because we are dealing with a Poisson process with parameter  $\lambda$ . Obviously  $T$  will be the time we need to wait for the  $Q$ -th customer to arrive, and so it is the sum of probability of  $Q$  exponentials all with parameter  $\lambda$ . Its expected value will be Poisson:
>
> $$
> \mathbb {E} [ T ] = \sum_ {i = 1} ^ {Q} \frac {1}{\lambda} = \frac {Q}{\lambda} = \frac {\# \mathrm {o f u s e r s}}{\mathrm {a v e r a g e t i m e b e t w e e n u s e r s}}
> $$
>
> b) Recall that the expected time we are requested to compute is the area subtended by curves shown in figure (4.26), but in addition we should note that both  $T$  and  $N(t)$  are random variables. Now we see that first user has to wait  $Q - 1$  arrivals before being dispatched, the second one  $Q - 2$  and so forth, up to the  $Q$ -th customer that has no waiting time. The total amount time waited will be the sum of the all the waiting time of the users, that is the sum of all integers from 1 through  $Q - 1$ , normalized to the size of the interval  $\lambda$ . We could have noted instead, that the sum we are looking for is the sum of  $Q$  rectangles, whose height goes from 0 through  $Q - 1$ , while its base is an exponential random variable that on average measures  $1 / \lambda$  for all of them. Using the Gauss summation formula for the first  $Q$  integers, or
>
>
> eventually making the product in order to compute the area, we finally obtain the value we are looking for:
>
> $$
> \mathbb{E}\left[\int_{0}^{T}N(t)dt\right]=[1+2+...+(Q-1)]/\lambda=Q(Q-1)/2\lambda
> $$

> [!question] Exercise 4.7.8 (Chap V - Ex. 4.1)
>
> Let $\{X(t);t\geqslant 0\}$ be a Poisson process of rate $\lambda$. Suppose it is known that in the first unit interval we have $n$ arrivals: $X(1)=n$. For $n=1,2,...$ determine the mean of the first arrival time $W_{1}$.
>
> Solution. If we condition on the number of arrivals, the arrival times are jointly distributed as independent and uniform. Consequently, $W_{1}$ has the same statistics of the minimum of $n$ uniform random variables:
>
> $$
> W_{1}=min(U_{i},i=1,2...,n)
> $$
>
> So the probability of the minimum to be bigger than a certain value $a$, given we have $n$ arrivals, is equivalent to the probability for all the random variables to be bigger than the same value:
>
> $$
> P[W_{1}>a]=P[\text{all }U_{i}^{\prime}s<a,i=1,2...,n]=(P[U>a])^{n}=(1-a)^{n}
> $$
>
> Where we used the property that all $U_{i}$’s are independent, and we assumed that $a\in[0,1]$, so the probability for $U_{i}$ to be bigger than it is just $1-a$ for each of them. Recall that this is all conditioned on the event that we have $n$ arrivals. The expectation value of $W_{1}$ given $n$ arrivals will be the integral of the tail distribution $P[W_{1}>a]$:
>
> $$
> \mathbb{E}[W_{1}|n\text{ arrivals in }[0,1]]=\int_{0}^{1}P[W_{1}>a]da=\int_{0}^{1}(1-a)^{n}da=\frac{1}{n+1}
> $$
>
> Thus concluding our exercise.

> [!question] Exercise 4.7.9 (Chap V - Ex. 4.3)
>
> Customers arrive at a certain facility according to a Poisson process of rate $\lambda$. Suppose that it is known that five customers arrived in the first hour. Determine the mean total waiting time $\mathbb{E}[W_{1}+W_{2}+W_{3}+W_{4}+W_{5}]$.
>
> Solution. As the previous exercise, we are given the number of arrivals that is 5: the $W_{i}$’s have a joint probability distribution that is like i.i.d. uniform random variables in the interval $[0,1]$h. Each of them has an average of 1/2hr, consequently their sum will be 2h30min.
>
>
> ###### Exercise 4.7.10 (Chap V - Ex. 4.5):
>
> Customers arrive at a certain facility according to a Poisson process of rate $\lambda$. Suppose that is know that five customers arrived in the first hour. Each customer spends a time in the store that is a random variable, exponentially distributed with parameter $\alpha$ and independent of the other customer times, and then departs. What is the probability that the store is empty at the end of the first hour?
>
> Solution. We can start again by conditioning on the number of arrivals that is 5, and each of them will distribute according to an i.i.d uniform distribution in the interval $[0,1]$h. The probability that the store is empty is the probability that all users have left after the first hour, a single user indeed does not depart within time $t$ with probability:
>
> $$
> P[\text{user has not departed}]=P[W+Y>t]=\vspace*{-0.1cm}
> $$
>
> Where $W$ is the arrival time and $Y$ is the service time. We now need to condition over the number of arrivals, and then replace the variable $W$ with $U$ that distributes uniformly. Picking moreover $t$ to be 1hr and conditioning over the uniform arrival time, we obtain:
>
> $$
> =P[U+Y>1]=\int_{0}^{1}P[Y>1-u]du=\int_{0}^{1}e^{-\alpha(1-u)}du=\frac{1-e^{-\alpha}}{\alpha}
> $$
>
> Where we used the fact that $Y$ distributes exponentially and then we integrated. We have just found the probability that a user is still in the system, consequently its complementary to 1 will be the probability that a user has already departed. Finally, since the times for all the users are independent of each other, the joint probability will be their product and thus obtaining:
>
> $$
> P[\text{system is empty}|5\text{ arrivals in }[0,1]]=P[\text{all users have left}|\text{ we had 5 users}]=\vspace*{-0.1cm}
> =\left(1-\frac{1-e^{-\alpha}}{\alpha}\right)^{5}
> $$
>
>
> CHAPTER 5
>
> Renewal Phenomena
>
> In renewal phenomena we can always find a time called renewal or regeneration time. This is a special time for which the process, in a statistical sense, begins anew, i.e. starts from scratch.
>
> ![[Stochastic_Processes_2020_p174_img61.jpeg]]
> Figure (5.1) - In a renewal process, every time that a renewal occurs we can consider as if the process anew starts.
>
> What happens is that we are looking into a phenomenon that starts from time 0. After some random time, an event occurs. In order to characterize the evolution of the system from the starting point, we need to describe the distribution according to which events occur. But the peculiarity of renewal phenomena is that, given that an event has occurred, the future statistics from that moment on will be identical to the one that started from time 0.
>
> Summarizing: any time there is an event, the system renews itself and statistically the evolution of the system starting from any of these events is indistinguishable. The renewal property comes from the fact that the times between two consecutive events are independent and identically distributed. The renewal theory essentially studies the times that passes between two consecutive events, and the properties that such class of functions of i.d.d., nonnegative random variables shares among its members.

# 5.1 Renewal processes

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
Figure (5.2) - The relation between the interoccurrence times  $X_{i}$ , the total time  $W_{i}$  and the renewal counting process  $N(t)$ .

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

Recall that $N(t)$ is the number of renewals up to time $t$, whereas $W_N(t)$ is the time of the latest renewal up to (or at) time $t$. The next renewal will occur indeed at time $W_{N(t)+1}$. Being in $t$, the latest renewal occurred at $\delta_t$ ago, while the next renewal will occur at the next time $\gamma_t$. The sum of these two random


![[Stochastic_Processes_2020_p178_img63.jpeg]]
Figure (5.3) - The excess life  $\gamma_{t}$ , the current life  $\delta_{t}$ , and the total life  $\beta_{t}$ .

variables, that is the total length of the renewal interval, will be the total life as defined above.

# 5.2 Examples of Renewal Processes

Among renewal processes we can consider some examples that are:

- Poisson Processes A Poisson process  $\{N(t), t \geqslant 0\}$  with parameter  $\lambda$  is a renewal counting process having the exponential interoccurrence distribution:

$$
F (x) = 1 - e ^ {\lambda x} \qquad x \geqslant 0
$$

- Traffic flow The distances between successive cars on an indefinitely long single-lane highway are often assumed to for a renewal process. So also the time durations between consecutive cars passing on a fixed location
- Processes Associated with queues In a single-server queueing process there are embedded many natural renewal processes. We cite two examples:

- If the customer arrival times form a renewal process, then the times of the starts of successive busy periods generate a second renewal process
- For the situation in which the input process (the arrival pattern of customers) is Poisson, the successive moments in which the server passes from a busy to a free state determine a renewal process

- Renewal Processes in Markov Chains Let  $Z_0, Z_1 \ldots$  be a recurrent Markov chain. Suppose  $Z_0 = i$ , and note that it is indeed irrelevant how we reached this state in order to determine the future behavior of the system. Every time we land to a given state, evolution will be statistically indistinguishable from the previous/future ones. Consider now the durations (elapsed number of steps) between successive visits to state  $i$ . Specifically, let  $W_0 = 0$ ,

$$
W _ {1} = \min (n > 0; Z _ {n} = i)
$$


and

$$
W_{k+1}=min(n>W_{k};Z_{n}=i)\qquad k=1,2...
$$

Since each of these times is computed from the same starting state $i$, the Markov property guarantees that $X_{k}=W_{k}-W_{k-1}$ are independent and identically distributed, and thus each visit of a generic state $X_{k}$ generates a renewal process.

![[Stochastic_Processes_2020_p179_img64.jpeg]]
Figure (5.4) – We can identify some interesting moments when dealing with queue processes, for example the moments when the first user arrives (white dots) or the last one departs (black dots). The latters are renewal instants if arrivals are i.i.d. memoryless, while the formers are renewal instants for delayed renewal processes if arrival times are i.i.d..

Processes Associated with queues

We see that whenever the system empties, meaning that it finds itself in state $0$, previous customers are not important to determine the future evolution of the system. Practically the system will have no memory of previous users and service times once it has emptied. These are indeed renewal instants.
Note that if the arrival process is memoryless, arrivals to an empty system will have all the same full distribution, as it we would start from time $0$. This guarantees that there is no need to remember when the last arrival occurred. So, starting at the point where the system empties, the memorylessness property will tell us that the next user will arrive according to an exponential distribution. Consequently the instants when the system becomes empty are renewal times (black dots in 5.4). In other words, at any of these points we only know that the next arrival will be Poisson so we can forget about whatever happened in the past.
If arrivals were not Poisson, the just stated points would not be renewal instants: the times passed from the last arrival would be correlated to the residual time for the next arrival to occur.
However, when there is an arrival to an empty queue (white dots in 5.4) the next state of the system will be $1$. These time instants are renewal times as well: statistically the evolutions starting from them are indistinguishable. Note that it is different from before, when we considered a class of points equivalent to the "time $t=0$" one, now the situation is the same when we the very first arrival occurred. For this class of points we can even relax the constraints and forget about the memoryless assumption for the interarrival times: they just need to be i.i.d. in order to be a renewal process. This class is called delayed


renewal processes.

# 5.3 The Poisson Process

We have just stated that the Poisson process with parameter  $\lambda$  is a renewal process, one of the simplest ones, and so let us study it under this point of view. Its interoccurrence times are exponentially distributed as  $F(x) = 1 - e^{-\lambda x}, x \geqslant 0$ .

# The Renewal Function  $\mathbf{N}(t)$

We know that  $N(t)$  is Poisson distributed:

$$
P [ N (t) = k ] = \frac {(\lambda t) ^ {k} e ^ {- \lambda t}}{k !} \qquad k = 0, 1 \dots .
$$

and its expectation value is linear in  $t$ :

$$
M (t) = \mathbb {E} [ N (t) ] = \lambda t
$$

# Excess Life  $\gamma_{t}$

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
Figure (5.5) - The excess life  $x$ , at time  $t$ , is how long we will have to wait after the present instant in order to make the next event occur

# Current life  $\delta_t$

We now look backwards starting from  $t$ .

$P[\delta_t \geqslant x]$  is the probability that we have no events in the interval  $[t - x, t]$ ,


that is equivalent to the probability of no events in the interval of length  $[0, x]$ . We thus obtain the same exponential distribution for the Excess life, but with one more condition:  $0 \leqslant \delta_t \leqslant t$ . It is quite reasonable, since current life cannot be bigger than  $t$ . We can write this as:

$$
P [ \delta_ {t} \leqslant x ] = \left\{ \begin{array}{l l} 1 - e ^ {- \lambda x} & \text {f o r} 0 \leqslant x <   t \\ 1 & \text {f o r} t \leqslant x \end{array} \right.
$$

One should have noticed that looking backwards or forwards statistically does not make any big difference: we do find a similar distribution, but the truncation at time  $t = 0$ . It does not make any sense indeed to look back before the starting point, whereas future is in principle infinite. This is formally translated into the fact that the distribution of  $\delta$  is truncated at  $t = 0$ , meanwhile the exponential distribution for  $\gamma$  might be infinite.

![[Stochastic_Processes_2020_p181_img66.jpeg]]
Figure (5.6) - We require now that both events  $\gamma_t > x, \delta_t > y$  hold, that is equivalent to require that no events occur in the interval  $[0, x + y]$  because of the property of Poisson processes.

# Joint Distribution of  $\gamma_{t}$  and  $\delta_t$

We want now to compute the probability of the joint event  $(\gamma_{t} > x, \delta_{t} > y)$  at a generic instant  $t$ . This can happen only when no events occur in both intervals (see fig.5.6): looking backwards we must not see any event later than  $t - y$  and, in addition, in the future no events must occur before  $t + x$ . Since we are dealing with a Poisson process, this can be translated as having no events in a longer interval, that is the sum of the previous two:  $(t - y, t + x]$ . Or equivalently we can require no events in the interval of a total length of  $(0, y + x]$ , being the process memoryless. The joint distribution we are looking for will be thus exponential and² for any  $y < t$ :

$$
P [ \gamma_ {t} > x, \delta_ {t} > y ] = \left\{ \begin{array}{l l} e ^ {- \lambda (x + y)} & \text {i f} x > 0, 0 <   y <   t \\ 0 & \text {i f} y \geqslant t \end{array} \right.
$$

For a Poisson process, one should observe that  $\gamma_{t}$  and  $\delta_t$  are independent, since their joint distribution factors as the product of their marginal distributions. We would have expected this: sitting on the time instant  $t$ ,  $\gamma_{t}$  depends on the

2recall the truncation discussed above


past whereas $\delta_t$ depends on the future, which are indeed disjoint time intervals.

## Mean Total Life $\mathbb{E}[\beta_t]$

We can find the expectation of $\beta_t$ as follows, recalling its definition as the sum $\beta_t = \gamma_t + \delta_t$ and exploiting the linearity of the operator $\mathbb{E}(\cdot)$:

$$
\mathbb{E}[\beta_t] = \mathbb{E}[\gamma_t] + \mathbb{E}[\delta_t] =
= \frac{1}{\lambda} + \int_0^\infty P[\delta_t > x] \, dx = \frac{1}{\lambda} + \int_0^t e^{-\lambda x} \, dx = \frac{1}{\lambda} + \frac{1}{\lambda} (1 - e^{-\lambda x}) \tag{5.4}
$$

Where we used the fact that $\delta_t$ is a truncated exponential, non null only in the interval $(0,t]$, and $\gamma_t$ distributes exponentially with parameter $\lambda$ so its expectation value is $1/\lambda$. We note that being the time between events exponential, so the mean has a $1/\lambda$ common factor.

Observe that the mean total life is significantly larger than the mean life of $1/\lambda = \mathbb{E}[X_k]$ of any particular renewal interval. Recall that $X_k$ is the interoccurrence times between two events, and in this case relates to $\gamma_t$ and $\delta_t$. We moreover note as $t >> 1$, the expression (5.4) for $\mathbb{E}[\beta_t]$ is approximately twice the mean life $1/\lambda$. In the next section we will go deeper into it.

## 5.3.1 The sampling paradox

Now we are going to discuss how it is possible for $\beta_t$ to have an expected value that is twice as large as the $1/\lambda = \mathbb{E}[X_k]$.

Let us consider the following renewal process: let us take a sequence of $X_i$'s which are separate and consecutive events as depicted in the figure 5.7.

![[Stochastic_Processes_2020_p182_img67.jpeg]]
Figure (5.7) – When we pick at random a time $t$, it is more likely that it falls in a longer interval. In this case it would be $X_2$ because it is the largest one.

We want to compute $\mathbb{E}[X_k]$, once an index $k$ has been picked at random with an uniform probability. In this way are sure that the result we will find is valid in general: index has been chosen randomly, and all $X_k$'s do follow the same statistics. We can indeed select the index $k$ an other way: once we have chosen a time $t$, the correspondent $X_k$ will be the interval that contains time $t$. We want to evaluate whether the statistics obtained by these two ways of selecting $X_k$ are the same one.

The answer is no. In the first case, where we pick the index $k$ randomly, each $X_k$ will have the same probability of being chosen and so the statistics will be the same of $F(x)$. Whereas, sampling in time we bias our statistics towards


longer intervals because the probability of  $t$  to fall in them is obviously higher. The latter way is indeed the same way as we choose  $\beta_{t}$ : we first pick a time instant  $t$ , and  $\beta_{t}$  will be the interval which contains this time. Consequently, the statistics of  $\beta_{t}$  will be biased towards longer intervals because they are the intervals where  $t$  is more likely to fall. This is the reason why  $\mathbb{E}[\beta_t]$  is larger than the  $\mathbb{E}[X_k]$  of a generic interval  $X_{k}$  sampled according to the first rule.

# Bus stop - example

An other example is given by the following situation: let us suppose we have a bus that runs twice every hour. However, it does not run precisely every half an hour: so that the intervals of the two runs are not equally large. This process can be seen as two asynchronous buses that have two different travel-times so that one of them lags and runs some time later. Let us suppose that we do not know at what time the bus goes and we, at a random time  $t$ , go to the bus station. The only thing known is that there are two lines that run once per hour. We may think that, since there are two lines, the expected time between two buses is 1/2hr, and so the average waiting time is 1/4hr (15min). This argument is actually wrong, and now we will show it.

Let us suppose that  $a$  is the time lag between two consecutive runs, that are by assumption made by the two different lines.

If  $a \to 0$ , both buses come at the same time and so the amount of time we need to wait for the next run (that are indeed two runs!) is 1hr. So the time we will need to wait, on average, becomes 30min.

Whereas, if  $a \to 1/2\mathrm{hr}$ , we obtain the previous argument where the average waiting time turns out to be  $1/4\mathrm{hr}$  and so  $15\mathrm{min}$ . We clearly see how the average waiting time depends on the time lag  $a$  between two runs.

![[Stochastic_Processes_2020_p183_img68.jpeg]]
Figure (5.8) - There are two buses that come twice per hour to a bus stop at two different moments. The difference in time between two consecutive runs is respectively  $a$  and  $1 - a$ . The system therefore has period 1hr.

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

### 5.4 Long run Behaviour

We want now to study as usual the asymptotic behaviour for the renewal processes.

We start by showing some simple asymptotic results, but before doing so, it is needed to make explicit a notation: $S_{n}\equiv W_{n}=\sum_{k=1}^{n}X_{k}$, that is the absolute time of the $n-th$ event, will be called sometimes $S_{n}$ according to the notation used in some books.

The first result we prove comes from the Law of large numbers: we want


to find:

$$
\lim_{n\to\infty}\frac{S_{n}}{n}=\lim_{n\to\infty}\frac{\sum_{k=1}^{n}X_{k}}{n}=\mathbb{E}[X]=\mu>0\qquad\text{w. prob. 1}
$$

where we used the fact that $X_{k}$’s are i.i.d. and their sum, divided by their number, with probability 1 tends to their expectation value. Under the assumption that $X_{k}$’s are positive random variables: $\mu>0$. This is reasonable: the time that it takes to observe $n$ events normalized to the total number of events returns the time average between two events, and so in the limit it will tend to its statistical average, namely $\mu$.

When we count an infinite number of renewals, for $n\to\infty$, the time taken to count them must also be infinite. We have just stated that $\mu>0$, and so in the limit it is needed that $S_{n}\to\infty$ too, since $\mu\neq 0$. Consequently we cannot have infinite number of renewals in finite time:

$$
\lim_{n\to\infty}S_{n}=\infty
$$

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

Proposition. With probability 1

$$
\frac{N(t)}{t}\to\frac{1}{\mu}+o(t)\qquad\text{as }t\to\infty
$$

where $\mu$ is the expectation value of $X$.

This proposition tells us that the *rate* at which $N(t)\to\infty$ is linear in $t$.

> [!note] Proof.
>
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
> Recalling that *in the limit strict inequalities must become large inequalities*:
>
> $$
> \mu\leqslant\frac{t}{N(t)}\leqslant\mu
> $$
>
> that is verified only when $\frac{N(t)}{t}=\mu$. This happens *with probability 1* because our result is based on something that in turn is valid with prob 1, namely *Law of large numbers*. In addition, being $N(t)$ a random variable this is not a limit in the "regular sense", nevertheless we can say that the limit is true *with probability 1*. Consequently, the probability for the statement not being true is null, thus concluding our proof. ∎
>
>
> The Renewal Function
>
> Recall now the formula we derived for the expected number of counts in the interval $(0,t]$:
>
> $$
> M(t)=\mathbb{E}[N(t)]=\sum_{j=1}^{\infty}F_{j}(t)
> $$
>
> where
>
> $$
> F_{j}(t)=P[S_{j}\leqslant t]\qquad t\geqslant 0
> $$
>
> Our first task will be to *show* that $M(t)$ is finite $\forall t>0$: we assumed this when we derived the first formula, but actually we had not proved it yet.
>
> $F_{n}(t)$ is the distribution of the sum of $n$ *i.i.d.* *random variables*, namely the $X$’s. The sum can be split into two components: the sum $\sum_{0}^{m}$ and the remaining $\sum_{n-m}^{m}$, where $0<m<n$.
>
> The distribution of these partial sums is the convolution between $F_{n-m}$ and $F_{m}$:
>
> $$
> F_{n}(t)=\int_{0}^{t}F_{n-m}(t-\xi)dF_{m}(\xi)\leqslant F_{n-m}(t)F_{m}(t)\qquad 1\leqslant m\leqslant n-1
> $$
>
> Where the inequality holds being $F_{n}(t)$ *monotone*. In addition we can bound it by using the product of two terms whose indices must sum to $n$.
>
> $M(t)$ can in turn be rewritten as the double sum over the indices $k,r$ that, it can be checked, spans all the values for the index $j=1,2,...,\infty$:
>
> $$
> M(t)=\sum_{j=1}^{\infty}F_{j}(t)=\sum_{n=0}^{\infty}\sum_{k=1}^{r}F_{nr+k}(t)
> $$
>
> The last term can be *upperbounded* in a *similar way* we shown above, using the product $F_{r}(t)F_{n-1r+k}$. The latter can be in turn upperbounded by $F_{r}(t)F_{n-2r+k}$ and so forth, iteratively, for $n$ times:
>
> $$
> \sum_{n=0}^{\infty}\sum_{k=1}^{r}F_{nr+k}(t)\leqslant\sum_{n=0}^{\infty}\sum_{k=1}^{r}(F_{r}(t))^{n}\;F_{k}(t)=\overbrace{\left(\sum_{n=0}^{\infty}(F_{r}(t))^{n}\right)}^{\text{converges geom. if }F_{r}(t)<1}\underbrace{\left(\sum_{k=1}^{r}F_{k}(t)\right)}_{\leqslant r}
> $$
>
> Last inequality holds because $F_{k}(t)$ is independent of $n$ and $(F_{r}(t))^{n}$ of $k$, it is allowed then to factorize these terms. The second one is both finite and less than $r$, being $F_{k}(t)$ a distribution with values between $0$ and $1$.
>
> It can be observed that the first term *converges geometrically* if $F_{r}(t)<1$, because $F_{r}(t)$ is a probability. The condition that $F_{r}(t)<1$ holds only when we choose $r$ appropriately. Let us prove now that we can *always* choose an $r$ in order to make the *infinite sum converge*. Before doing so, one should note that the first inequality holds *without any condition* on $r$, except the one that
>
>
> $r$  must be finite.

> [!abstract] Theorem 5.4.1. 
> Theorem 5.4.1.  $\forall t, \exists r$  such that  $F_{r}(t) < 1$
>
> ![[Stochastic_Processes_2020_p188_img69.jpeg]]
> Figure (5.9) - Clearly having fixed  $F(t = 0) = 0$ , we will be always able to find a  $t_0 \neq 0$  for which  $F(t_0) < 1$  because  $F(t)$  is continuous.

> [!note] Proof.
> Proof. Clearly we can always find a  $t_0 > 0$  s.t.  $F(t_0) < 1$  and  $F(t) < 1$  for  $t < t_0$ . This is always valid because we stated that  $F(0) = 0$ . The only case in which would not be possible to find such  $t_0$  would be if immediately  $F(0) = 1$ , which cannot be.
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

### 5.5 The Renewal Argument


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
$$ (5.7)

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

> [!abstract] Theorem 5.5.1.
>
> Suppose $a(t)$ is a bounded function, even for $t\to\infty$. Then there exists one and only one function $A(t)$ bounded on finite intervals that satisfies
>
> $A(t)=a(t)+\int_{0}^{t}A(t-y)dF(y)$ (5.9)
>
>
> This solution is:
>
> $A(t)=a(t)+\int_{0}^{t}a(t-x)dM(x)$ (5.10)
>
> where $M(t)=\sum_{k=1}^{\infty}F_{k}(t)$ is the renewal function.
>
> Proof of the theorem is omitted.
>
> We can see that (5.9) and (5.10) differ only by the convolution arguments. One should note in addition that in (5.10) everything that is known stands on the rhs: once $\sum_{k=1}^{\infty}F_{k}(t)$ is specified, $M(t)$ can be easily found, while the unknown term is on the lhs. This shows that the solution is explicit. Computing the integral may be difficult and might not even be solvable analytically, but this is just a practical matter. The most important thing is that the integral can be computed, being it explicit.
>
> Renewal theory allows us to solve the problem of finding some interesting statistical quantities by first conditioning over $X_{1}$, and then by removing this condition when considering the different cases in the Renewal Equations that follow. Their solution is generally unique and is given by (5.10).

#### Applications - $\mathbb{E}[S_{N(t)+1}]$

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
Figure (5.11) – We have two different cases that correspond to the relative position to $X$ wrt the time we pick. In the case that a general $t^{\prime}>X$, we count a renewal and reshift our time axis as we did before and the other quantities rescale accordingly.

For the first expression, we start again by invoking the *Renewal Argument*:

$$
\mathbb{E}[S_{N(t)+1}|X_{1}=x]=\begin{cases}x&\text{if }x>t\\
x+A(t-x)&\text{if }x\leqslant t\end{cases}
$$ (5.13)

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

One other result for $t\to\infty$ is the so called Elementary Renewal Theorem (proof omitted), that states the following:

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

Recalling now the theorem we have stated before, whose proof is omitted, we can now sketch what its statement asserts:

![[Stochastic_Processes_2020_p195_img71.jpeg]]
Figure (5.12) – In the limit as $t\to\infty$, $M(t)$ will grow linearly.

Note as $M(t)$ is linearly increasing wrt $t$, and so as $t\to\infty\quad M(t)\simeq\frac{t}{\mu}$.

It is a very intuitive result: if $\mu$ is the average renewal time, we will approximately count the ratio of the time $t$ passed, normalized to the mean time between two consecutive events $\mu$. This is not obvious indeed, and it is shown in the proof, which we will not consider.

#### 5.6.1 The Basic Renewal Theorem

The elementary renewal theorem asserts that, for infinite time horizons:

$$
\lim_{t\to\infty}\frac{M(t)}{t}=\frac{1}{\mu}
$$

But we want now to show what happens when the time intervals are not infinite any more. Let us consider the following situation:

We want to compute now on average how many renewals occur in the shorter interval we highlighted in the figure, namely $(t,t+h)$, for any value of $h$. In other words we want to know what is the increment of the process $M(t)$ in a


![[Stochastic_Processes_2020_p196_img72.jpeg]]
Figure (5.13) - For any value of  $h$ , we want to compute the average increment in the interval  $(t, t + h)$ . This increment will be  $N(t + h) - N(t)$ , while their expectation value  $M(t + h) - M(t)$ .

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

> [!abstract] Theorem 5.6.1. Let  $F$  be the distribution function of a positive random variable with mean  $\mu$ . Let  $M(t) = \sum_{k=1}^{\infty} F_k(t)$  be the renewal function associated with  $F$ . Let  $h > 0$  be fixed. Then
> Theorem 5.6.1. Let  $F$  be the distribution function of a positive random variable with mean  $\mu$ . Let  $M(t) = \sum_{k=1}^{\infty} F_k(t)$  be the renewal function associated with  $F$ . Let  $h > 0$  be fixed. Then:
>
> 1. If  $F$  is not arithmetic, then:
>
> $$
> \lim _ {t \to \infty} [ M (t + h) - M (t) ] = h / \mu
> $$
>
> 2. If  $F$  is arithmetic, the same limit holds, provided  $h$  is a multiple of the span  $\lambda$ .
>
> We see that the theorem distinguishes two cases: whether  $F$  is arithmetic or not. For our purposes,  $F$  not arithmetic means that the random variable, which describes the inter event time  $X$ , has a continuous distribution. In this case,
>
>
> regardless of the value of $h$, the previous formulation of the theorem applies.
> Whereas if $F$ is arithmetic and therefore $X$ distribution is discrete, the only possible values that $X$ can take are multiple of a common value named span and denoted by $\lambda$.
> An issue with the granularity arises: $h$ can not be anything but a multiple of $\lambda$, otherwise some boundaries effect would make our thesis not true.
> In conclusion the Renewal theorem states that the average increment of the process in an interval of length $h$, in the long run, is proportional to the length of this interval $h$ according to the constant $1/\mu$. This is valid for any $h$ if the $X$’s are continuous, while for $h$ such that are multiples of $\lambda$ if the $X$’s are discrete.

#### Asymptotic results of N(t)

One other asymptotic result is: standardizing $N(t)$ by subtracting its asymptotic mean and normalizing to its standard deviation, it converges to the normal distribution:

$$
\lim_{t\to\infty}P\left[\frac{N(t)-t/\mu}{\sqrt{t\sigma^{2}/\mu^{3}}}\leqslant x\right]=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{x}e^{-y^{2}/2}dy
$$

#### Asymptotic results of Age and Excess Life

Other useful results deal with the Limiting Distribution of Age and Limiting Distribution of Excess Life ($\gamma_{t}$).
Let us assume that the lifetimes $X_{i}$’s are continuous random variables with finite mean $\mu$. Let $\gamma_{t}=W_{N(t)+1}-t$ be the excess life at time $t$. The excess life has the limiting distribution:

$$
\lim_{t\to\infty}P[\gamma_{t}\leqslant x]=\frac{1}{\mu}\int_{0}^{x}[1-F(y)]dy
$$

This result, whose proof is omitted, can be found once again by mean Renewal Argument.

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

Figure (5.14) – $\{\delta_{t}\geqslant y\ \mbox{and}\ \gamma_{t}\geqslant x\}$ if and only if $\{\gamma_{t-y}\geqslant x+y\}$

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

#### 5.6.2 Delayed Renewal Processes

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

## 5.6.3 Alternating Renewal Process

An other important type of renewal process, that is often found in exercise, is the so called Alternating Renewal Process.

Let us suppose that we have a renewal process with the usual sequence of  $X$ 's that represent the time intervals between two consecutive events. Let us suppose that  $Y_{i}$  represents a portion of the duration  $X_{i}$ , as depicted in the figure (5.15):

![[Stochastic_Processes_2020_p200_img73.jpeg]]
Figure (5.15) - A renewal process in which an associated random variable  $Y$  represents a portion of the  $i$ -th renewal interval.

We moreover assume that  $Y$ 's are i.i.d. as the  $X$ 's are, and in addition  $X_{j}$  and  $Y_{i}$  are independent of each other for all indexes such that  $i \neq j$ . In other words, the only dependent random variable are  $X_{i} = Y_{i}$ . One other obvious condition is that  $Y_{i}$  cannot exceed  $X_{i}$ .

Let us now compute the probability that picking a random time  $t$  it will fall into an  $Y_{i}$  interval, rather than its complementary  $X_{i} - Y_{i}$ . In other words, we want to know the fraction of times the system is in state 1 (ON state), having denoted  $Y_{i}$  in this way, rather than in the remaining interval having it labelled as state 0 (OFF state). In particular we are looking for these fractions in the limit  $t \to \infty$ , taking into account that all these ON/OFF cycles are


independent of each other and have the same distributions.

Let  $p(t)$  the probability that  $t$  falls in a portion denoted by  $Y_{i}$  (ON state). When  $X_{1}, X_{2}, \ldots$  are continuous random variables, the renewal theorem implies the following important asymptotic evaluation:

$$
\lim _ {t \to \infty} p (t) = \frac {\mathbb {E} [ Y _ {1} ]}{\mathbb {E} [ X _ {1} ]}
$$

One should have noticed that this is the fraction of time that the system is in  $ON$  state during each cycle/renewal interval. Moreover, it is reasonable that a long run behavior, that is  $\lim_{t\to \infty}p(t)$ , will reduce to a simple fraction: different intervals of the renewal processes are statistically equivalent. Each one of them is thus representative for the whole process, which is the repetition of identically distributed and independent intervals. When we know what happens in a single interval, anything about the whole process will be characterized as well being it its repetition. This is indeed a very important example, and many times there are exercises where we need to apply this result.

![[Stochastic_Processes_2020_p201_img74.jpeg]]
Figure (5.16) - A system can be either in  $BUSY$  or in  $IDLE$  state, depending on the presence of users.

A Queueing Model Let us now study again a queueing model, but using Renewal processes formalism.

Recall that a queueing process is a process in which customers arrive at some designated place where a service of some kind is being rendered. When an user arrives, the service will take place until the last customer leaves the system. For some times then the system will be empty, and after one other arrival the service will start again.

As depicted in fig.(5.16), we can tell two different different type of intervals: IDLE when no users are there, and BUSY when service is taking place. We have already discussed that, once there is an arrival in an empty system, those are renewal instants, whereas the moments where the system empties may be renewal instants as well, as long as inter arrival times are memoryless.

This labelling leads us to a Delayed Renewal process, having the first interval a distribution different from the others. Each cycle repeats for ever, and it starts with a  $BUSY$  state before being  $IDLE$  and so forth. A very common question is to compute the fraction of time spent by the system in the two different states. The answer is the ratio between the average of the  $BUSY$  and  $IDLE$  intervals, once we have been able to characterize these time


intervals. Formally:

$$
\lim_{t\to\infty}p(t)=\frac{\mathbb{E}[BUSY]}{\mathbb{E}[BUSY+IDLE]}
$$

As a Network-fashioned consideration, note that when the system is busy, it produces useful work. As an example we can consider a server that can send some data out of a node. If there is no data, the server is still able to send in principle, but cannot send anything because there is nothing to be sent (IDLE). On the other hand, if data is present, the server will be BUSY until it will have sent all the data out of the node, producing some useful work. The traffic that the system will handle usefully will be the datarate available, that is a specific of the system, times the probability that the system is busy, that is the probability above.

#### 5.6.4 Proof of basic limit theorem for M.C.

Now that we have studied Renewal and Delayed Renewal processes we are finally able to proof the Basic Limit Theorem for Markov Chains. We recall that the theorem statement is the following:

> [!abstract] Theorem 5.6.2.
>
> For a recurrent irreducible and aperiodic Markov Chain or, equivalenty, for a recurrent and aperiodic class it holds that:
>
> $$
> \lim_{n\to\infty}P_{jj}^{(n)}=\lim_{n\to\infty}P_{ij}^{(n)}=\pi_{j}=\frac{1}{\sum_{n=1}^{\infty}nf_{jj}^{(n)}}=\frac{1}{m_{j}}
> $$

> [!note] Proof.
>
> In order to prove the theorem, let us first fix a time $t$ and introduce the number of visits to state $j$ up to time $t$: namely $N_{j}(t)$. Note as $j$ is recurrent since it belongs to a recurrent class.
> Now, in the case that the chain starts at state $j$, then $N_{j}(t)$ is a traditional renewal process, being the initial and final states the same. The distribution of interevent times is therefore discrete: every time we visit state $j$ there is a renewal, and by the Markov property every visit is a renewal itself. Obviously, we can return only in a discrete non-negative number of steps not less than 1: the recurrence time or inter event time is an integer, positive random variable. Using the terminology of renewal theory, the distribution of inter event times $X$’s is arithmetic with span $\lambda=1$. Inter event times can be obviously only multiple of this number.
> Renewal theorem ensures us that, for any increment $h$ that is multiple of the span, we have:
>
> $$
> \lim_{t\to\infty}[M(t+h)-M(t)]=h/\mu
> $$
>
> Where we need to tell what is $\mu$.
> Now one should note that the increment in a single time unit step $N_{j}(n)$ can
>
>
> be rewritten as the sum:
>
> $$
> N_{j}(n)=N_{j}(n-1)+\mathbb{1}[X_{n}=j]
> $$
>
> Where the indicator function denotes the possible visit to state $j$ at time $n$, that may or may not occur. Let us take now the expectation value of the equation (5.16), conditioned on the initial state $X_{0}=j$.
>
> $\mathbb{E}[\mathbb{1}[X_{n}=j]]$ is the probability of being in state $j$ at a time step $n$, given it started in $j$ at time $0$. Whereas $\mathbb{E}[N_{j}(n)]=M(n)$, being it a renewal process. We obtain:
>
> $$
> \mathbb{E}[\ \mathbb{1}[X_{n}=j|X_{0}=j]\ ]=P_{jj}^{(n)}=M(n)-M(n-1)\xrightarrow{n\to\infty}\frac{1}{m_{j}}
> $$
>
> One should note that, taking the limit as $n\to\infty$, the time span of this difference $M(n)-M(n-1)$ is indeed a multiple of $h=\lambda=1$. Therefore the hypotheses of Renewal theorem hold, and the latter can be applied. We can obtain the mean $\mu=m_{j}$ from the comparison of the two expressions above. This means that, given we start our process in state $j$, the mean $\mu$ is the average recurrence time $m_{j}$. Hence the probability for large $n$ to return in state $j$, once we have started in it, is the inverse of the average recurrent time.
>
> Now let us consider the case where the chain is *periodic* with period $d$. We can take the difference between the counters in two different moments:
>
> $$
> N_{j}(nd)-N_{j}(nd-d)=\sum_{i=nd-d+1}^{nd}\mathbb{1}[Y_{i}=j]
> $$
>
> that is equal to the sum of indicators function in the times between $[nd-d+1,nd]$. Because of the periodicity, in the case where we start at state $j$ all the terms in the sum are $0$ except the one $i=nd$: we cannot visit that state in a time-step different than a multiple of the period.
>
> Now we take the expectation of both members in (5.17) and condition onto the fact that we have started in $Y_{0}=j$. We finally obtain a similar expression to the one we have already seen, that differs only by the times difference that now is a period $d$:
>
> $$
> \mathbb{E}\left[\sum_{i=nd-d+1}^{nd}\mathbb{1}[Y_{n}=j|Y_{0}=j]\ \right]=P_{jj}^{(nd)}=M(nd)-M(nd-d)\xrightarrow{n\to\infty}\frac{1}{m_{j}}
> $$
>
> Obviously, being the chain periodic, the average return times will be a multiple of the period $d$. The span for this case will be $\lambda=d$ that is equal to the time difference $h$ itself: $h=\lambda=d$. Therefore the Renewal theorem can be applied, and thus we obtain the result we have already found for the periodic case.
>
> Note that, up to now, we only have proved a little piece of the equations in the statement of the theorem, namely for the *aperiodic* case when we start in $j$:
>
> $$
> \lim_{n\to\infty}P_{jj}^{(n)}=\frac{1}{m_{j}}
> $$
>
>
> Now we want to start in a state $i\neq j$, and so prove that:
>
> $$
> \lim_{n\to\infty}P^{(n)}_{jj}=\lim_{n\to\infty}P^{(n)}_{ij}
> $$
>
> For this case we note that $N_{j}(t)$ is a *delayed* renewal process: all $X$’s except the very first one are equal to a return time $j\to j$. The initial $X_{1}$ will be instead the first passage time $i\to j$, so it will have a different distribution from the other $X$’s. Finally, being a delayed renewal process, we know that the same-as-before asymptotic results apply regardless of the choice of state $i$, by simply applying the same arguments. We have not made any statement about the way passages to state $j$ occur, and so the renewal process may be of *any* kind. In this way we have shown that the limit (5.18) is not dependent on the starting state as long as it belongs to the same class, thus concluding our proof.
>
> $$
> \square
> $$

### 5.7 Renewal Reward Processes

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

> [!abstract] Theorem 5.7.1.
>
> If $\ \mathbb{E}[R]<\infty\$ and $\ \mathbb{E}[X]<\infty\$, then:
>
> 1.
>
>
> 1. with probability 1, it holds that the average number of rewards per unit time in the long run is:
>
> $$
> \frac {R (t)}{t} \rightarrow \frac {\mathbb {E} [ R ]}{\mathbb {E} [ X ]} \quad \text{as } t \rightarrow \infty
> $$
>
> 2. the same result applies to the function  $\mathbb{E}[R(t)]$  in the limit:
>
> $$
> \frac {\mathbb {E} [ R (t) ]}{t} \rightarrow \frac {\mathbb {E} [ R ]}{\mathbb {E} [ X ]} \quad \text{as } t \rightarrow \infty
> $$

> [!note] Proof. In order to prove 1), we can rewrite
> Proof. In order to prove 1), we can rewrite:
>
> $$
> \frac {R (t)}{t} = \frac {\sum_ {n = 1} ^ {N (t)} R _ {n}}{t} = \left(\frac {\sum_ {n = 1} ^ {N (t)} R _ {n}}{N (t)}\right) \left(\frac {N (t)}{t}\right)
> $$
>
> Recall that in the limit  $N(t) \xrightarrow{t \to \infty} \infty$  with probability 1. Applying the strong law of large numbers we obtain for the first factor:
>
> $$
> \frac {\sum_ {n = 1} ^ {N (t)} R _ {n}}{N (t)} \rightarrow \mathbb {E} [ R ] \quad t \rightarrow \infty
> $$
>
> and by the same law for renewal processes:
>
> $$
> \frac {N (t)}{t} \rightarrow \frac {1}{\mathbb {E} [ X ]} \quad t \rightarrow \infty
> $$
>
> thus ending the proof for 1).
>
> Proof for 2) is omitted. One should note that is not so obvious: the reason is that if a limit is true in the probabilistic way, it does not imply the same result when taking the true limit, thus needing to be shown.
>
> $\frac{R(t)}{t}$  can be interpreted as the average reward per unit time, but we can also compute the average reward per some other quantities but the time, so using a different metric. As an example we can compute the average energy spent per correctly delivered packet, a relevant quantity in packet transmission systems. In this way we end up having the average metric of one kind per unit of another metric.
>
> This situation is described in the following corollary:
>
> Corollary. Let  $R_{1}(t)$  and  $R_{2}(t)$  be two reward functions. Then:
>
> $$
> \frac {R _ {1} (t)}{R _ {2} (t)} \xrightarrow {t \to \infty} \frac {\mathbb {E} [ R _ {1} ]}{\mathbb {E} [ X ]} \frac {\mathbb {E} [ X ]}{\mathbb {E} [ R _ {2} ]} = \frac {\mathbb {E} [ R _ {1} ]}{\mathbb {E} [ R _ {2} ]} \quad \text{with probability 1}
> \frac {\mathbb {E} [ R _ {1} (t) ]}{\mathbb {E} [ R _ {2} (t) ]} \xrightarrow {t \to \infty} \frac {\mathbb {E} [ R _ {1} ]}{\mathbb {E} [ R _ {2} ]} \quad \text{with probability 1}
> $$
>
> 3recall that $R(t)$ is indeed a random variable in $t$
>
>
> Where  $R_{1}(t)$  and  $R_{2}(t)$  can be any metric.
>
> As an example if  $R_{1}(t)$  is the energy spent and  $R_{2}(t)$  is the number of the correctly distributed packets up to time  $t$ , then the energy per packet will be the ratio between these two quantities.
>
> Once again we see that what happens in an infinitely long evolution time, is the same as for  $\frac{R(t)}{t}$ : it is totally represented by metric valid at the shorter renewal interval level. This is because a renewal process repeats for ever intervals that are statistically identical, therefore a metric computed on one of them is representative for the overall evolution of the process.

# 5.7.1 Regenerative processes

Let us consider a stochastic process  $\{X(t), t \geqslant 0\}$  with state space  $\{0,1,2,\ldots\}$  having the property that there exist time instants at which the process (probabilistically) restarts itself. That is equivalent to say that, with probability 1, we can find a time  $S_{1}$  such that the continuation of the process beyond  $S_{1}$  is a probabilistic replica of the whole process starting from 0. If the process was in state  $j$  at the beginning, there will be a moment  $S_{1}$  when the process will be in state  $j$  and restart again.

Note that it is a necessary condition, and not a sufficient: being in the same state as the starting one does not imply that the evolution will be identically to the one as if we have started anew. There is one exception indeed, that are the Markov Chains: when we find ourselves in the same state as the initial one, we know that is sufficient to say that the process will renew itself from that point on.

Now we want to state the relationship between the a Renewal process and a Regenerative process. The latter refers to the actual evolution of the process.

![[Stochastic_Processes_2020_p206_img75.jpeg]]
Figure (5.17) - In a regenerative process, when we sit at the starting point  $t = 0$ , or at  $S_{1}$  or  $S_{2}$  it does not make any difference when we look forward to the statistically evolution of the process. Note that we may visit  $j$ -th state at some instants that does not necessarily are regeneration instants. This would be actually different for a Markov chain.

Note as every regenerative process contains a renewal process: the instants at which the process regenerates are renewal instants. However the renewal process only counts time and tells where renewal instants are, whereas the regenerative process has more than only the renewal structure. It refers to the actual evolution of the process as well, that can take only integer-valued states: regenerative process has got in addition the statistics of the different states and hence the evolution among them.


Let  $X$  be a renewal process. In each renewal interval we can define some portion that we label with  $Y_{i}$ . This should remind us of Alternating processes, where  $X_{i}$  and  $Y_{i}$  started at the same time instants, and so  $Y_{i}$  belong to the initial part of the renewal interval  $X_{i}$ .

Now, instead, the only condition for every  $Y_{i}$  is that the sum of its corresponding disjoint intervals must be a number between 0 and  $X_{i}$ .

![[Stochastic_Processes_2020_p207_img76.jpeg]]
Figure (5.18) - A more general formulation for an alternating process, where the "ON" states may be disjoint and more than one per renewal interval.

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

### 5.8 Semi-Markov Processes

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
Figure (5.19) – Z(t) is a semi-Markov process, every time there is a transition to state $i$ a new cycle begins and so those are regenerative instants. Note as it may happen that between two consecutive renewal instants we do not visit any other state (see $S_{2},S_{3}$).

As depicted in figure (5.19), every time we enter state $i$ the process restarts as if anew. More generally, a semi-Markov process is a regenerative process with the property: every cycle starts when we enter state $i$, then we may either remain for some times or some cycles or move away from it, until we go back to $i$ and the process restarts.

We have defined $\mu_{i}$ as the average time in $i$ before making a transition, whereas $\mu_{ii}=\mathbb{E}[S]$ is the average time between consecutive visits to state $i$, and so the average duration of a cycle. We can write now the long run probability that our process at time $t$ is in state $i$, given in started in $j$:

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

#### 5.8.1 Some clarifications on Regenerative and Semi-Markov Processes

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

#### 5.8.2 Semi-Markov process probabilities

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


> [!question] Exercise 5.8.2 (Chap VII- Prob. 4.1)
>
> A Markov chain  $X_0, X_1, X_2 \ldots$  has the transition probability matrix:
>
> $$
> \mathbf {P} = \begin{array}{c c c c} & 0 & 1 & 2 \\ 0 & \left[ \begin{array}{c c c} 0.3 & 0.7 & 0 \\ 0.6 & 0 & 0.4 \\ 0 & 0.5 & 0.5 \end{array} \right] \end{array}
> $$
>
> A sojourn in a state is an uninterrupted sequence of consecutive visits to that state. Hence it begins when we come to a state and finish once we leave it.
>
> 1. Determine the mean duration of a typical sojourn in state 0
> 2. Using renewal theory, determine the long run fraction of time that the process is in state 1.
>
> ![[Stochastic_Processes_2020_p216_img78.jpeg]]
> Figure (5.20) - Transition diagram for problem 5.8.2.
>
> Solution. 1) It can be easily computed once we remember that, for a Markov chain, the mean duration of the stay in a state is a geometric random variable, whose parameter is the probability of leaving the state, namely 0.7. Its inverse will correspond to the average of the distribution, and so the mean duration is:
>
> $$
> \mathbb {E} [ \text {s t a y i n 0} ] = \frac {1}{0 . 7} = \frac {1 0}{7} \simeq 1. 4 2
> $$
>
> Similarly we can compute the expected stay in state 2:
>
> $$
> \mathbb {E} [ \text {s t a y i n 2} ] = \frac {1}{0 . 5} = 2
> $$
>
> and the expected stay in state 1.
>
> $$
> \mathbb {E} [ \text {s t a y i n 1} ] = 1
> $$
>
> The latter is indeed 1, because once we are in this state, with probability 1 we know that we will go out next time step.
>
> 2) Note that every time we visit state 1 is a renewal instant. Any time we land into it we will move exactly after 1 time unit to either 0 or 2 state. We will stay there some time, according to a geometric distribution, before a new renewal instant when going back to 1.
>
> This should remind us of the Alternating renewal processes: we may define
>
>
> ![[Stochastic_Processes_2020_p217_img79.jpeg]]
> Figure (5.21) - For this particular exercise (5.8.2), we have that 1 is a regenerative state. Using renewal formalism, it is an alternating renewal process, and so we can refer to the duration of our stay in 1, as  $Y_{i}$ .
>
> state 1 by  $Y$ , where our stay will deterministically last exactly 1 time-step before leaving for some other state. We can therefore compute the expectation values for both the  $Y$ 's and the  $X$ 's, the latter being the average duration of a cycle, namely how much time is needed in order to come back to 1. Starting from state 1, after one time unit, we may leave with different probability either to state 0 or state 2, and spend there some time before returning to 1 and so starting a new cycle.
>
> $$
> \mathbb {E} [ Y ] = 1
> \mathbb{E}[\text{return time to 1}] = \mathbb{E}[X] = 1 + P_{10}\cdot \mathbb{E}[\text{stay in 0}] + P_{12}\cdot \mathbb{E}[\text{stay in 2}] = 1 + 0.6\cdot \frac{10}{7} +0.4\cdot 2 = \frac{93}{35}
> $$
>
> We can finally compute the probability for the chain being in state 1:
>
> $$
> \pi_ {1} = P [ \text {chain is in state 1} ] = \frac {1}{93 / 35} = \frac {35}{93}
> $$
>
> Note that for this specific case, where the chain spends exactly one time unit in state 1,  $\mathbb{E}[X]$  is the average return time and  $\pi_1$  is the inverse of the average recurrence time. We could have also gone through this problem also by solving the system of stationary equations  $\vec{\pi} = \vec{\pi} \cdot P$ , finally obtaining the same result for  $\pi$ .

> [!question] Exercise 5.8.3 (Chap VII- Ex. 4.1)
>
> Consider the triangular lifetime density  $f(x) = 2x$  for  $0 < x < 1$ . Determine an asymptotic expression for the expected number of renewals up to time  $t$ . Hint. Use the equation:
>
> $$
> \lim _ {t \to \infty} \left[ M (t) - \frac {t}{\mu} \right] = \frac {\sigma^ {2} - \mu^ {2}}{2 \mu^ {2}}
> $$
>
> Solution. We obviously have that:
>
> $$
> M (t) \simeq \frac {t}{\mu} + \frac {\sigma^ {2} - \mu^ {2}}{2 \mu^ {2}}
> $$
>
> where we need to compute  $\mu, \sigma$ .
>
>
> ![[Stochastic_Processes_2020_p218_img80.jpeg]]
> Figure (5.22) -  $\mathrm{pdf(x)}$  for the triangular lifetime density  $f(x) = 2x$  for both problems (5.8.3) and (5.8.4) in the interval  $0 < x < 1$ .
>
> $$
> \mathbb {E} [ X ] = \mu = \int_ {0} ^ {1} x f (x) d x = \int_ {0} ^ {1} 2 x ^ {2} d x = \frac {2}{3}
> \mathbb {E} [ X ^ {2} ] = \mu^ {2} + \sigma^ {2} = \int_ {0} ^ {1} x ^ {2} f (x) d x = \int_ {0} ^ {1} 2 x ^ {3} d x = \frac {1}{2}
> \sigma^ {2} = \mathbb {E} [ X ^ {2} ] - \mu^ {2} = \frac {1}{2} - \frac {4}{9} = \frac {1}{18}
> \frac {\sigma^ {2} - \mu^ {2}}{2 \mu^ {2}} = \frac {1 / 18 - 4 / 9}{2 \cdot 4 / 9} = - \frac {7}{16}
> $$
>
> Finally we can write:
>
> $$
> M (t) \simeq \frac {t}{\mu} + \frac {\sigma^ {2} - \mu^ {2}}{2 \mu^ {2}} = \frac {3}{2} t - \frac {7}{16}
> $$
>
> **Exercise 5.8.4 (Chap VII- Ex. 4.2):**
>
> Consider the triangular lifetime density  $f(x) = 2x$  for  $0 < x < 1$ . Determine an asymptotic expression for the probability distribution of excess life. Using this distribution, determine the limiting mean excess life and compare with the general result following equation:
>
> $$
> \lim  _ {t \rightarrow \infty} P [ \gamma_ {t} \leqslant x ] = \frac {1}{\mu} \int_ {0} ^ {x} [ 1 - F (y) ] d y \tag {5.25}
> $$
>
> **Solution.** With respect to the density distribution  $f(x) = 2x$ , its corresponding distribution is  $F(X) = X^2$  in (0,1). We can compute either (5.25) or its complementary:
>
> $$
> \lim _ {t \to \infty} P [ \gamma_ {t} > x ] = \frac {1}{\mu} \int_ {x} ^ {\infty} (1 - F (y)) d y
> $$
>
> that we have already studied previously. Replacing  $F(y)$  with its value and considering the interval where the integrand is non zero:
>
> $$
> \frac {1}{\mu} \int_ {x} ^ {1} (1 - y ^ {2}) d y = \frac {1}{\mu} \left[ \frac {2}{3} - x + \frac {x ^ {3}}{3} \right] = \frac {3}{2} \left[ \frac {2}{3} - x + \frac {x ^ {3}}{3} \right] = 1 - \frac {3}{2} x + \frac {x ^ {3}}{2} = \lim _ {t \to \infty} P [ \gamma_ {t} \geqslant x ]
> $$
>
>
> $\mu$ was the one from the previous exercise. The expectation value, in the limit, will be the integral:
>
> $$
> \mathbb{E}[\gamma_{t}]=\int_{0}^{\infty}P[\gamma_{t}>x]dx=\int_{0}^{1}\left(1-\frac{3}{2}x+\frac{x^{3}}{2}\right)dx=1-\frac{3}{4}+\frac{1}{8}=\frac{3}{8}
> $$
>
> where this is the asymptotic expected value for the excess life for this problem. We have seen previously (see eq. 5.15 at page 198) that we can compute $\mathbb{E}[\gamma_{t}]$ by using $\sigma$ and $\mu$. Therefore:
>
> $$
> \frac{\sigma^{2}+\mu^{2}}{2\mu}=\frac{1/18+4/9}{2\cdot 2/3}=\frac{1/2}{4/3}=\frac{3}{8}
> $$
>
> that is the same result we obtained before, thus concluding this problem.

> [!question] Exercise 5.8.5 (Chap VII- Ex. 4.5)
>
> What is the limiting distribution of excess life when renewal lifetimes have the uniform density $f(x)=1$, for $0<x<1$?
>
> Solution. Being $f(x)=1$ uniform in $(0,1)$, we easily know that $\mu=1/2$ and $F(X)=X$. Its limiting distribution follows the general result written in the previous exercise (5.25):
>
> $$
> \lim_{t\to\infty}P[\gamma_{t}>z]=\frac{1}{\mu}\int_{z}^{\infty}(1-F(x))dx=\frac{1}{\mu}\int_{z}^{1}(1-x)dx=\int_{z}^{1}2(1-x)dx=(1-z)^{2}\quad z\in(0,1)
> $$
>
> where we replaced $\mu$ with its value $1/2$. The complementary to $1$ probability will consequently be:
>
> $$
> \lim_{t\to\infty}P[\gamma_{t}\leqslant z]=1-(1-z)^{2}\quad z\in(0,1)
> $$

> [!question] Exercise 5.8.6 (Chap VII- Ex. 5.1)
>
> Jobs arrive at a certain service system according to a Poisson process of rate $\lambda$. The server will accept an arriving customer only if it is idle at time of arrival. Potential customers arriving when the system is busy are lost. Suppose that the service times are independent random variables with mean service time $\mu$.
>
> - Show that the long run fraction of time that the server is idle is $1/(1+\lambda\mu)$.
> - What is the long run fraction of potential customers that are lost?
>
> Solution. Let us suppose that we start when the system is empty (IDLE) and we wait for the first arrival. After an average time $1/\lambda$ an user will arrive according to an exponential distribution, and will set the system state in BUSY
>
>
> ![[Stochastic_Processes_2020_p220_img81.jpeg]]
> Figure (5.23) - Graphical description of exercise (5.8.6). We start with our system in IDLE state and, after a period whose average value is  $1 / \lambda$ , an user arrives and will be served in a period of time whose average is  $\mu$ , in which the system will be BUSY. Clearly the sum IDLE+BUSY is a renewal interval.
>
> for an average time period of  $\mu$ . Once the system is emptied again, it will wait for an other customer to arrive and repeat this process. Note that the distribution of arrivals is memoryless, and therefore independent of the time when the system empties. This is indeed an Alternating renewal process.
>
> We recall, from the theory, that the probability for the system to be  $IDLE$  is the ratio between the expected time duration for  $BUSY$  time, and for a single cycle:
>
> $$
> P [ \mathrm {s e r v e r I D L E} ] = \frac {\mathbb {E} [ I D L E ]}{\mathbb {E} [ I D L E + B U S Y ]} = \frac {1 / \lambda}{1 / \lambda + \mu} = \frac {1}{1 + \lambda \mu}
> $$
>
> We can now find the fraction of potential customers that are lost in two different ways. Let us consider the renewal process we are dealing with, and define two different rewards: the first one is the number of users that have been accepted, that for each cycle is obviously one. So the its expected number is deterministically known:
>
> $$
> \mathbb {E} [ \text {a c c e p t e d u s e r s i n a r e n e w a l c y c l e} ] = 1
> $$
>
> Conversely, the number of arriving users in a cycle is the average time duration of the cycle times the arrival rate:
>
> $$
> \mathbb {E} [ \text {a r r i v i n g u s e r s i n a r e n e w a l c y c l e} ] = (1 / \lambda + \mu) \lambda = 1 + \lambda \mu
> $$
>
> Among this number of users, we know that only one will be accepted, while the remaining ones will not. Therefore, the probability:
>
> $$
> \begin{array}{l} P [ \text {u s e r i s r e j e c t e d} ] = \frac {\mathbb {E} [ \text {r e j e c t e d u s e r s} ]}{\mathbb {E} [ \text {a r r i v i n g u s e r s} ]} = \\ = \frac {\mathbb {E} [ \text {a r r i v i n g u s e r s} ] - \mathbb {E} [ \text {a c c e p t e d u s e r s} ]}{\mathbb {E} [ \text {a r r i v i n g u s e r s} ]} = \frac {\lambda \mu}{1 + \lambda \mu} \\ \end{array}
> $$
>
> The second way to obtain the same result is the following one.
>
> Instead of computing  $P[\text{server IDLE}]$ , we could have looked for the  $P[\text{server BUSY}]$  that is its complementary to 1. In addition, the probability for a user to be rejected is the same one as the probability for an arriving user to find the system BUSY. Recall now that Poisson Arrivals See Time Averages, and so the probability seen by an arriving user is the probability  $P[\text{server BUSY}]$ . And
>
>
> so:
>
> $$
> P[\text{server BUSY}]=1-P[\text{server IDLE}]=\frac{\lambda\mu}{1+\lambda\mu}
> $$
>
> This result could be obtained also using renewal theory: we should have defined the rewards in a renewal cycle we introduced above, and finally compute the ratio. Alternatively, we could have found what is the probability for an arriving user to find the system BUSY, that would be statistically equivalent for him to be rejected.

> [!question] Exercise 5.8.7 (Chap VII- Ex. 5.1)
>
> A certain type component has two states:
>
> $$
> 0=\text{OFF}\qquad 1=\text{OPERATING}
> $$
>
> In state 0, the process remains there a random length of time, which is exponentially distributed with parameter $\alpha$, and then moves to state 1. The time in state 1 is exponentially distributed with parameter $\beta$, after which the process returns to state 0.
>
> The system has two of these components, A and B with distinct parameters, as shown in the table (LABEL:eq:system) below.
>
> In order for the system to operate, at least one of the components A and B must be operating (a parallel system). Assume that the component stochastic processes are independent one of another.
>
> 1. In the long run, what fraction of time is the system inoperational (not operating)?
> 2. Once the system enters the failed state, what is the mean duration there prior to returning to operation?
> 3. Define a cycle as the time between the instant that the system first enters the failed state and the next such instant. Using renewal theory, find the mean duration of a cycle.
> 4. What is the mean system operating duration between successive system failures?
>
> |  Component | Operating Failure Rate | Repair Rate  |
> | --- | --- | --- |
> |  A | $\beta_{A}$ | $\alpha_{A}$  |
> |  B | $\beta_{B}$ | $\alpha_{B}$  |
>
> Table (5.1) – Table depicting all parameters for both components A and B in exercise (5.8.7).
>
> Solution. 1) We should note that for a single component there are many intervals statistically equal one to another. These are indeed Renewal intervals,
>
>
> ![[Stochastic_Processes_2020_p222_img82.jpeg]]
> Figure (5.24) - A possible evolution in time for a single component of the process, that may be working or not for different time intervals exponentially distributed whose averages are respectively  $1 / \alpha$  and  $1 / \beta$ . Note as every time we return to state 0 it is a Renewal instant.
>
> where the Renewal instants are the ones where we land in state 0. More specifically we can identify an Alternating renewal process, whose state are  $ON$  or  $OFF$ . The probability that a single component is operating will consequently be:
>
> $$
> P [ \text {c o m p o n e n t} i \text {w o r k i n g} ] = \frac {1 / \beta_ {i}}{1 / \alpha_ {i} + 1 / \beta_ {i}} = \frac {\alpha_ {i}}{\alpha_ {i} + \beta_ {i}} \tag {5.26}
> $$
>
> Recall now that the system has two components, whose  $\alpha_{i}$  and  $\beta_{i}$  are different, and independent of each other. Clearly, the two probabilities for a component to be down are the complementary to 1 of (5.26):
>
> $$
> P [ A d o w n ] = \frac {\beta_ {A}}{\alpha_ {A} + \beta_ {A}} \qquad P [ B d o w n ] = \frac {\beta_ {B}}{\alpha_ {B} + \beta_ {B}}
> $$
>
> We have just stated that the two processes are independent, and so the joint probability for both of them of being down is their product:
>
> $$
> P [ A d o w n, B d o w n ] = P [ A d o w n ] \cdot P [ B d o w n ] = \left(\frac {\beta_ {A}}{\alpha_ {A} + \beta_ {A}}\right) \left(\frac {\beta_ {B}}{\alpha_ {B} + \beta_ {B}}\right)
> $$
>
> ![[Stochastic_Processes_2020_p222_img83.jpeg]]
> Figure (5.25) - Diagram for point 2 of ex. 5.8.7. We start when both components are OFF, and we wait until either of the two independent exponential processes with rate  $\alpha_{A}$  and  $\alpha_{B}$  occurs, in order for the system to be recovered. We denote with  $T_{A}$  and  $T_{B}$  the times for respectively component  $A$  and  $B$  to recover.
>
> 2) It is requested to compute the probability, once both  $A$  and  $B$  are down, for the system to recover. We know that this happens when one of the components recovers, which eventually occurs according to an exponential with rate  $\alpha_{A}$  or  $\alpha_{B}$ . We denote by  $T_{A}$  and  $T_{B}$  the times when recover happens for the two components, and so the time for which the system will be down:
>
> $$
> \text {t i m e s y s t e m i s d o w n} = \min  \left(T _ {A}, T _ {B}\right)
> $$
>
> We need now to find the statistics of this minimum. See that when the minimum
>
>
> of two values is bigger of a certain number, it implies that both of them will be bigger than the same number:
>
> $$
> P[min(T_{A},T_{B})>a]=P[T_{A}>a\ ,\ T_{B}>a]=P[T_{A}>a]\cdot P[T_{B}>a]=\
> $$
>
> Where we used the fact that the single statistics of $T_{A}$ and $T_{B}$ are independent of each other. We indeed know them, as they are exponentially distributed. And so we can write:
>
> $$
> =P[T_{A}>a]\cdot P[T_{B}>a]=e^{-\alpha_{A}a}\cdot e^{-\alpha_{B}a}=e^{-(\alpha_{A}+\alpha_{B})a}
> $$
>
> Note as the probability for the minimum being bigger than $a$ is itself an exponential random variable, whose rate is the sum of the two different parameters $(\alpha_{A}+\alpha_{B})$. This is obviously valid only for exponential random variables, or for combined random processes, but does not apply for more general cases. The average time the system will remain down is therefore the inverse of the rate just found, and so:
>
> $$
> \mathbb{E}[\text{Sojourn System down}]=\frac{1}{\alpha_{A}+\alpha_{B}}
> $$
>
> ![[Stochastic_Processes_2020_p223_img84.jpeg]]
> Figure (5.26) – Diagram for point 3 of ex. 5.8.7. We start in state $(0,0)$, and so where both components are down. Successively it will be alternatively in states $(0,1),(1,0),(1,1)$ where the system will be working, until both goes down again and we fall back into $(0,0)$ state. This is indeed a Renewal instant. We can define an alternating renewal process out of this, where our $Y$ will be the period while the system is not working.
>
> 3) We should notice as every time we enter state $(0,0)$, the future evolution starting from this point will be statistically indistinguishable: since both components are down, the system will not work. Note as the repair time is exponential in both cases and therefore memoryless. It is indeed a renewal instant included in an alternating renewal process.
> The probability that the system is down is the ratio between the two intervals $\mathbb{E}[\text{system down}]$ and $\mathbb{E}[\text{cycle}]$. We know both the the expected value for the duration of time interval while the system is down and the ratio value, computed in the previous points of the exercise.
> So we can invert the formula, thus obtaining:
>
> $$
> \mathbb{E}[\text{cycle}]=\frac{\mathbb{E}[\text{system down}]}{P[\text{system down}]}=\frac{1/(\alpha_{A}+\alpha_{B})}{\left(\frac{\beta_{A}}{\alpha_{A}+\beta_{A}}\right)\left(\frac{\beta_{B}}{\alpha_{B}+\beta_{B}}\right)}
> $$
>
> 4) We are requested to find the expected time duration of the interval that is complementary to the duration of a cycle, and so the second interval denoted
>
>
> as  $(0,1),(1,0),(1,1)$  in image (5.26). As we can clearly see graphically:
>
> $$
> \mathbb{E}[\mathrm{cycle}] = \mathbb{E}[\mathrm{system~down}] + \mathbb{E}[\mathrm{system~working}]
> $$
>
> Where we can compute it by using the results obtained previously, therefore:
>
> $$
> \mathbb{E}[\mathrm{system~working}] = \mathbb{E}[\mathrm{cycle}] - \mathbb{E}[\mathrm{system~down}] = \left(\frac{1}{\alpha_A + \alpha_B}\right)\left(\frac{(\alpha_A + \beta_A)(\alpha_B + \beta_B)}{\beta_A\beta_B} -1\right)
> $$
>
> Note that if we wanted to compute directly  $\mathbb{E}[\mathrm{system~working}]$  we could have done it, in principle. But we also would have to take into account that the number of trajectories leading us to a failure of the system, namely  $(0,0)$ , is infinite.
>
> In order to obtain its average duration, we would need first to count all possible combinations and therefore their probability making the calculations very risky and tedious. Whereas Renewal theory comes in our help, giving us a shortcut to compute the average stay in a single state. Once we have the average stay in a single state, in this case  $(0,0)$ , we can model our problem as an alternating process and leading us to simple formula that can be easily inverted.

> [!question] Exercise 5.8.8 (Chap VII- Ex. 5.4)
>
> A lazy professor has a ceiling fixture in his office that contains two light bulbs. To replace a bulb, the professor must fetch a ladder, and being lazy, when a single bulb fails, he waits until the second bulb fails before replacing them both. Assume that the length of life of the bulbs are independent random variables.
>
> - If the lifetimes of the bulbs are exponentially distributed, with the same parameter, what fraction of time, in the long run, is our professor's office half lit (only one bulb is working)?
> - What fraction of time, in the long run, is our professor's office half lit if the bulbs that he buys have the same uniform  $(0,1)$  lifetime distribution?
>
> ![[Stochastic_Processes_2020_p224_img85.jpeg]]
> Figure (5.27) - Representation for point 1 of ex. 5.8.8. We start our problem when both bulbs are working, and after the second one breaks, we assume that the replacement is instantaneous and it is a renewal instant. Under these assumptions, it is a Alternating renewal process.
>
> Solution. 1) Obviously, as depicted in figure (5.27), it is an Alternating renewal process between the states where both bulbs are working (2) and only one is working (1). This is indeed true only in the case where the replacement
>
>
> is instantaneous, otherwise we would have taken into account also the time needed in order to replace the bulb, and so defining a new state.
>
> The probability for the office to be half lit is therefore the probability of being in state 1, using the renewal theory. We assumed, for this point, that each lifetime  $X_{i}$  is exponentially distributed with parameter  $\beta$ . So, the time when one of them breaks is an exponential random variable itself, whose rate of failure is the rate of failure of two single bulbs  $(2 \cdot 1\beta)$ . This means the average of this time is half of the time for one of them to break. Once the first one is burnt, the time elapsed for the second one to break in turn is an exponential random variable with parameter  $1 / \beta$ . Recall that the exponential distribution is memoryless, and therefore the second remaining light bulb has a whole lifetime  $1 / \beta$  ahead, being it as if new. The probability we are looking for is:
>
> $$
> P [ \mathrm {h a l f} \mathrm {l i t} ] = \frac {1 / \beta}{2 / \beta + 1 / \beta} = \frac {2}{3}
> $$
>
> Note that the last result is valid only when the distribution is memoryless, but more in general we have a situation as depicted in figure (5.28)
>
> ![[Stochastic_Processes_2020_p225_img86.jpeg]]
> Figure (5.28) - More general case for ex. 5.8.8. Cycle is still the same, but distributions for the time intervals intervals may change.
>
> In order to find the statistics of the moment where the first bulb breaks, we do consider a certain time value  $a$  and find the probability for  $\min(X_1, X_2)$  to be greater than it. Note as it is equivalent to state that both of them must be greater than  $a$ , and so if we assume that lifetimes are independent one another, and in a later passage that they are identically distributed:
>
> $$
> P [ \min (X _ {1}, X _ {2}) > a ] = P [ X _ {1} > a, X _ {2} > a ] = P [ X _ {1} > a ] \cdot P [ X _ {2} > a ] = (P [ X > a ]) ^ {2} = (1 - F (a)) ^ {2}
> $$
>
> Conversely, when we want to find the statistics of the maximum between  $MAX(X_1, X_2)$  we can set it to be smaller than  $a$ . And so, using in addition the fact that lifetimes are identically distributed, and so their distribution is the same one:
>
> $$
> P [ M A X (X _ {1}, X _ {2}) \leqslant a ] = P [ X _ {1} \leqslant a, X _ {2} \leqslant a ] = P [ X _ {1} \leqslant a ] \cdot P [ X _ {2} \leqslant a ] = (P [ X \leqslant a ]) ^ {2} = (F (a)) ^ {2}
> $$
>
> We now compute their expectation values:
>
> $$
> \mathbb {E} [ \min ] = \int_ {0} ^ {\infty} P [ \min > a ] d a = \int_ {0} ^ {\infty} (1 - F (a)) ^ {2} d a
> \mathbb{E}[MAX]=\int_{0}^{\infty}P[MAX>a]da=\int_{0}^{\infty}(1-F(a)^{2})da
> $$
>
> This result is valid for any distribution $F(a)$, as long as they are independent one another.
> If $X\sim exp(\beta)$, then its distribution is $F(a)=1-e^{-\beta a}$, hence the expectation values:
>
> $$
> \mathbb{E}[min]=\int_{0}^{\infty}e^{-2\beta a}da=\frac{1}{2\beta}
> \mathbb{E}[MAX]=\int_{0}^{\infty}(2e^{-\beta a}-e^{-2\beta a})da=\frac{3}{2\beta}
> $$
>
> 2) In the case where this distribution is $X\sim U[0,1]$, then $F(a)=a,\;a\in(0,1)$. Expectation values are then:
>
> $$
> \mathbb{E}[min]=\int_{0}^{1}(1-a)^{2}da=\frac{1}{3}
> \mathbb{E}[MAX]=\int_{0}^{1}(1-a^{2})da=\frac{2}{3}
> $$
>
> And so the probability for the office to be half lit, in the long run:
>
> $$
> P[\text{half lit}]=1-\frac{\mathbb{E}[min]}{\mathbb{E}[MAX]}=\frac{1}{2}
> $$
>
> that is less than what we obtained in the exponential lifetime case.
>
>
> CHAPTER 6

# Analysis of the GoBackN Protocol

The GoBackN Protocol is a data transmission protocol which sends data in packets of some bits through a channel. There is in addition an other channel implemented for reliability and control: for every packet the sender is notified whether the packet has been correctly received. If so, transmission is successful. In the other case, so if the packet is either lost or corrupted, then a negative acknowledgment requests the sender for another transmission. It is a very common protocol in networks, and it is useful because it permits to deal with errors by retransmitting the corrupted data.

GoBackN protocol is particularly designed for accepting packets in order. So, if a packet is either lost or corrupted, then it will need to be retransmitted. Because of the design, it will be needed to retransmit sequentially the following packets regardless whether there were errors concerning it. A sketch for this protocol is shown in the figure below (6.1).

![[Stochastic_Processes_2020_p227_img87.jpeg]]
Figure (6.1) - Representation of a possible evolution GoBackN protocol: once the sender is notified that a packet is corrupted, it goes back to that packet and retransmits it again followed by its consecutive, ordered packets. A packet, identified by the number above, may be successfully received (0) or may contain an error (1) and therefore the necessity to send it again. In this particular case, the Roundtrip time is equal to  $N = 3$ .

Usually, when designing a GoBackN, we define  $N$  as the Roundtrip time, i.e. the number of time steps after which the sender is notified about an eventual error. As a consequence, every time a channel at time  $t$  has an error, its packet will be sent again at time  $t + N$ . Note as in the interval of time  $(t + 1, t + N - 1)$  the sender has not been notified about the bad channel yet, and so keeps sending packets until it receives the acknowledgment that there has been an error. From that moment on, it will resume the transmission sequentially starting from that specific packet that was incorrect. We assume, for sake of simplicity, that there are always packets to be sent, and so there are no empty slots.

There might be other protocols, with referral to image (6.1) we could for example retransmit only the packet corrupted, that are 3, 4, and then resume the transmission from the last packet it has successfully received. This is called Selective Repeat. It is indeed more efficient, since we do not need to send packets that were correctly delivered more than once. This requires in addition the faculty for the receiver to be able to accept packets out of order, finally reordering them, once the complete sequence has been dispatched successfully up to the last channel. Then the transmission starts again.

This is not what GoBackN does, so to keep the receiver simple. In fact it does not accept packets out of order, and moreover when packets have a sequence different from the expected one, they are simply rejected as for the ($X$) in the image above (6.1). We can see that every time there is an error, the sequence restarts from the appropriate time. If this happens, once the incorrect packet has been sent, the subsequent $N-1$ channels will be retransmitted no matter whether they have been successfully transmitted, and so they are at first ignored. In each time slot, the channel may be in two different states: good (0), or bad (1).

On the other hand, from the point of view of the protocol. not all slots contain the so called throughput opportunities. A throughput opportunity is defined as the average number of successful packets received and accepted by the protocol per slot. A slot can therefore be a throughput opportunity when, if the slot is good, that packet is counted as a success. With referral to image (6.1) first three packets are throughput opportunities, while the fourth and the fifth are not. Note that the third one actually is a throughput opportunity: despite the fact that the packet is not correct, it still has been received as well as accepted. Given the bad transmission, fourth and fifth ones indeed are not accepted, regardless their channel state. because of the protocol and so they are not throughput opportunities. For the point of view of the protocol packets fourth and fifth do not even exist, since only the retransmitted ones will be considered. What the protocol sees is not every single slot, but every slot as long as the transmission is successful. When an error occurs, it will skip $N-1$ slots and look at the channel $N$ slots later. We can see it as a sampling rule: every time there is a success, then sample at the very next slot. Whereas if a failure occurs, then sample $N$ slots later. Sampled slots will be indeed the only slots seen by the protocol. In the computation of throughput opportunity, and so the efficiency of our protocol, we will count then all packets received and accepted normalized by the number of all packets sent, regardless they were correct/wrong or had been skipped or accepted.

This is a very simple data transmission protocol. It is common use in networking courses to study a protocol by adding some errors in i.i.d. channels, according to some probability and independently, and see how the system behaves. Even though there is some memory in our process, let us still assume that we can model our system by using a 2-state Markov chain which are 0 and 1. There may be also a certain distribution that describes how these states are distributed statistically. We will now try to find the throughput of this protocol using several ways and for different cases, where in all of them Markov errors


will be present. Models will differ by the feedback behavior, that is to say the acknowledgements that the sender receives, that might be either perfect (no error) or subject to errors, that in turn might be Markov or independent.

#### 6.0.1 Markov packet errors - Error free feedback

Let us consider the GoBackN protocol on a Markov channel, where data packet errors follow a two-state Markov chain. Transmissions may be either be $0$ for good channel or $1$ for bad channels. Acknowledgments are error-free and the round-trip of the system is $m$ slots. This means that if a packed transmitted in slot $t$ is corrupted, the sender will be notified by the end of slot $t+m-1$ and the packet will be retransmitted in slot $t+m$.
Let the two-channel matrix be:

$$
\mathbf{C}=\begin{bmatrix}p_{00}&p_{10}\\
p_{10}&p_{11}\end{bmatrix}
$$

whose entries are the transition probabilities for good and bad states. Note as if a channel is good, then the system will look at the very next slot, whose state will depend of the transition probabilities shown in $\mathbf{C}.$ Whereas if a channel is bad, the next time the protocol will look at the channel will be $m$ slots later. The transition probability we need to consider for this case is therefore different, namely the $m$-step transition probability.
These probabilities are given by:

$$
\mathbf{C}^{m}=\begin{bmatrix}p_{00}(m)&p_{10}(m)\\
p_{10}(m)&p_{11}(m)\end{bmatrix}
$$

From the point of view of the protocol operation, this channel is sampled every slot when transmissions are correct, and once every $m$ slots when errors occur. Therefore, every time state $\mathbf{0}$ is visited, one success is counted (one packet was indeed correctly delivered) and the time spent in that state before the next transition is $\mathbf{1}$ slot. On the other hand, when we visit state $1$ (bad channel), no successes are counted and the time spent in that state before the next transition is $m$ slots.
Accordingly, the transition probabilities from each state are taken either from $\mathbf{C}$ or $\mathbf{C}^{m}$ depending on the time spent, so that the transition matrix for the protocol model is:

$$
\mathbf{P}=\begin{bmatrix}p_{GG}(m)&p_{GB}(m)\\
p_{BG}(m)&p_{BB}(m)\end{bmatrix}=\begin{bmatrix}p_{00}&p_{10}\\
p_{10}(m)&p_{11}(m)\end{bmatrix}
$$ (6.1)

whereas the time $T$ and reward $R$ (success) metrics in the two states are:

$T_{G}=1\quad T_{B}=m\quad R_{G}=1\quad R_{B}=0$ (6.2)

Note as when we have a bad channel, we must take into account that we spend


![[Stochastic_Processes_2020_p230_img88.jpeg]]
Figure (6.2) – Protocol may be either in a good state (good channel) or in a bad state (bad channel). In the first case, reward and time metrics will be both one. On the other hand, if the channel is bad, the reward will be null and the time will be $m$ time slots. Transition probabilities between these states are either one-step or $m$-step, according to which channel we are in, as stated in (6.1)

$m$ time slots in the bad state, and therefore draw our transition probabilities from the $m$-step transition matrix $\mathbf{C}^m$. All what is depicted in figure (6.2) defines a complete, despite very simple, semi-Markov model with rewards. We can find the embedded Markov-chain that looks only at the transition probabilities between states in $\mathbf{P}$. In addition there is the time distribution: it is equal for all transition probabilities leaving a same state, namely 1 for the good state, and $m$ for the bad one. Finally there is an other metric, the reward metric, that counts the number of successes we have. We can therefore ask ourselves to compute, in the long run, what is the average reward/successes per unit time: namely the throughput.

In order to compute the throughput we need first to find the limiting probabilities for the embedded Markov chain, and then apply the results we have found for the renewal reward theory. Given the transition probability $\mathbf{P}$, the limiting probabilities for a two states Markov chain are proportional to the probability of moving into that state from the others. So:

$$
\pi_G = \frac{p_{10}(m)}{p_{01} + p_{10}(m)} \quad \pi_B = \frac{p_{01}}{p_{01} + p_{10}(m)} \tag{6.3}
$$

and, if $R(t)$ counts the number of successful packets in $[0,t]$, the protocol throughput is given by the limit:

$$
\lim_{t \to \infty} \frac{R(t)}{t}
$$

We know this, from the theory of rewards-renewal processes, to be equal with probability 1 to:

$$
\lim_{t \to \infty} \frac{R(t)}{t} = \eta = \frac{\pi_G R_G + \pi_B R_B}{\pi_G T_G + \pi_B T_B} = \frac{p_{10}(m)}{p_{10}(m) + m p_{01}} \quad \text{w.prob. 1}
$$

that is the final expression for the throughput. We simply substituted the values we have just found in (6.3) for $\pi_G$ and $\pi_B$ and in (6.2) for $T$'s and $R$'s. This last expression is measured in unit of (packets/slot).

A special case is when errors are i.i.d. with probability $\epsilon$, and so $\mathbf{C}$ and the


throughput becomes:

$\mathbf{C}=\mathbf{C}^{m}=\begin{bmatrix}1-\epsilon&\epsilon\cr 1-\epsilon&\epsilon\end{bmatrix}\qquad\eta_{iid}=\frac{1-\epsilon}{1-\epsilon+m\epsilon}$ (6.4)

We can note that the probability of going to a *good* state, i.e. where the second index is 0, is always $1-\epsilon$. Whereas the probability to go to a bad state denoted by the second index equal to 1, is always $\epsilon$.

These last results could have been derived invoking renewal theory. Recall from (6.2) that *every time we land into state $G$* we obtain *1 reward*, moreover this is a *renewal time* being it a Markov chain. The evolution of the process will therefore restart as if from scratch every time we land in this state, and so a new *cycle* will restart and last until we come back to $G$ again. Each of these renewal cycle will contain exactly *one* reward, since we can visit state $G$ only once per cycle. The *average duration* of a renewal cycle *will be* obviously the average return time to this state, namely *the average recurrence time*. Putting together the information about the number of rewards per cycle (one) and its average duration, we can compute the throughput as the ratio between these quantities.

In order to find the average recurrence time, we use the *first-step analysis* and we evaluate the duration of all transitions that bring us back to $G$ and their probabilities. For these computations, recall that the time we spend in a state is a geometric random variable whose mean is the inverse of the probability of leaving the state, in this case $(p_{10}(m))^{-1}$. We must pay attention moreover that this transition takes exactly $m$ time steps, and so the mean we are looking for is $m/p_{10}(m)$. In formulas:

$m=1\cdot p_{00}+p_{01}\left[1+\frac{m}{p_{10}(m)}\right]=1+\frac{mp_{01}}{p_{10}(m)}$

where $p_{00}+p_{10}=1$.

The *throughput* (average fraction of time spent in state $G$) is then:

$\eta=P_{G}=\lim_{t\rightarrow\infty}P[Z(t)=G|Z(0)=i]=m_{G}^{-1}=\frac{p_{10}(m)}{p_{10}(m)+mp_{01}}$

as we already found before.

#### 6.0.2 Bidirectional Markov packet errors - 4 states model

Now we suppose that errors can occur in the reverse direction as well: i.e. the feedback channel might not successfully transmit the data. We now assume that the error process for the feedback channel is a Markov process, whose possible states are either 1 *bad transmission*, or 0 *good transmission*. These states are labelled as $q_{ij}$ and are different from the $p_{kl}$ that correspond to the transmission channel: indeed they are two different channels that transmit two different kind of packets, whose data may be different in length and encoding as well. Therefore the error structure is not *the same one in both directions*.


We now need to take into account all the possible combinations for data channel and feedback channel. That is, for  $q_{ij}$  the subscript  $i$  corresponds to the success of the transmission, while the  $j$  to the correctness of the acknowledgment. The process can be depicted as follows:

![[Stochastic_Processes_2020_p232_img89.jpeg]]
Figure (6.3) - Graphical representation for the 4-states GoNBack protocol. These 4 states a cover all possible combinations for the success/failure for transmissions of the packets and successive acknowledgments. Consequently the only state that denotes a success and therefore a reward is the  $(0,0)$  one.

$q_{00}$  denotes a packet successfully transmitted, and acknowledgment correctly received, whereas in  $q_{11}$  both of them are bad channels.

$q_{10}$  instead refers to a packet that is in error, but the acknowledgement is correct, while  $q_{01}$  viceversa.

The only state that corresponds to a success can be only  $q_{00}$ , whose time duration associated is 1 slot, whereas the other ones will denote a failure. In the case there is a failure in some data channel, we know that the corresponding feedback will be received  $m$  time slots later. The time associated to all transitions going out of these three states will be therefore  $m$ : the corresponding transition probabilities will be computed according to the  $m$  steps in both directions.

The transition probability matrix for this protocol will be:

|   | (0,0) | (0,1) | (1,0) | (1,1)  |
| --- | --- | --- | --- | --- |
|  P = | (0,0) | p00q00 | p00q01 | p01q00  |
|   |  (0,1) | p00(m)q10(m) | p00(m)q11(m) | p01(m)q10(m)  |
|   |  (1,0) | p10(m)q00(m) | p10(m)q01(m) | p11(m)q00(m)  |
|   |  (1,1) | p10(m)q10(m) | p10(m)q11(m) | p11(m)q10(m)  |

Note as the first row, corresponding to the success state, has all 1-step transition probabilities. Whereas the other rows are made up of  $m$ -step transition probabilities, according to what we said before.

Therefore the structure shown in (6.2), and the just written transition probability matrix and the metrics of reward/failure provide the complete semi-Markov model for this special protocol, where Markov errors can occur in both directions. We can use now the formula (5.24) applied to our problem: we choose the second metric to be the time.


The average throughput is then obtained in the limit as:

$$
\eta = \frac {\sum_ {i} \pi_ {i} R _ {i}}{\sum_ {i} \pi_ {i} T _ {i}} = \frac {\pi_ {(0 , 0)}}{\pi_ {(0 , 0)} + m (1 - \pi_ {(0 , 0)})}
$$

In the numerator the only non-null term is for the state  $(0,0)$ , and so  $R_{(0,0)} = 1$ . In the denominator we have that  $T_{(0,0)} = 1$  with probability  $\pi_{(0,0)}$ , while for the other states we will have that  $T = m$  with probability  $1 - \pi_{(0,0)}$ .

For this case we will not express  $\pi_{(0,0)}$  in a closed form, being the computations very tedious. We would indeed need to solve the stationary equations for (6.5) numerically, then find  $\pi_{(0,0)}$  and finally the average throughput.

## 6.0.3 Bidirectional Markov packet errors - 3 states model

Let us now consider a special case where the feedback channel has i.i.d. errors with probability  $\delta$ , but states are the same ones in  $\mathbf{C}$  matrix.

We can now split state  $G$  into two different states: in order to explicitly distinguish the cases with correct  $(G_0)$  and erroneous feedback  $(G_1)$ , respectively.

We note as  $G_0$  corresponds to state  $(0,0)$  of the figure (6.5), whereas  $G_1$  relates to state  $(0,1)$  of the same picture: despite the success in the transmission of the packet, there is an error in the acknowledgement.  $B$  does not need to be split: regardless the feedback state, it remains a failure. Moreover since errors are i.i.d., the next feedback state will have the same probability as the previous ones and so it does not depend on the previous feedbacks.

![[Stochastic_Processes_2020_p233_img90.jpeg]]
Figure (6.4) - Representation of the embedded Markov chain for the 3-states model for GoBackN protocol, where feedback errors are i.i.d. We note as the state  $B$  is not split,  $G_{0}$  corresponds to a success, while  $G_{1}$  to a failure.

Starting from  $G_{0}$  we know both packet and acknowledgement were correct, and we may stay there if both transmission and feedback are again correct with probability respectively  $p_{00}$  and  $1 - \delta$ . In the case that feedback is not correct (prob.  $\delta$ ) while acknowledgement is not (prob.  $p_{00}$ ) we go to  $G_{1}$ , from where we will leave in  $m$  steps depending on the goodness of data and feedback channels.

This picture can be obtained both from (6.2) and (6.5). In the first case we split  $G$  into  $G_{0}$  and  $G_{1}$ . In the second case, states  $(1,0)$  and  $(1,1)$  can be combined into a whole state  $B$  since there is no need to keep memory on the previous feedback state. As before, for the success state  $G_{0}$  we have 1 reward and 1 slot, while for the bad channels  $G_{1}$  and  $B$  we have no reward and  $m$  time


slots. We can solve the Markov chain whose transition matrix is:

$$
\mathbf {P} = \begin{array}{l l l l} & G _ {0} & G _ {1} & B \\ G _ {0} & (1 - \delta) p _ {0 0} & \delta p _ {0 0} & p _ {0 1} \\ G _ {1} & (1 - \delta) p _ {0 0} (m) & \delta p _ {0 0} (m) & p _ {0 1} (m) \\ B & (1 - \delta) p _ {1 0} (m) & \delta p _ {1 0} (m) & p _ {1 1} (m) \end{array}
$$

and compute the throughput recalling that:

$$
R _ {G _ {0}} = 1 \quad R _ {G _ {1}} = R _ {B} = 0 \qquad T _ {G _ {0}} = 1 \quad T _ {G _ {1}} = T _ {B} = m
\eta = \frac {\pi_ {G _ {0}}}{\pi_ {G _ {0}} + m (1 - \pi_ {G _ {0}})} \tag {6.6}
$$

Solving the stationary equations  $\vec{\pi} = \vec{\pi}\mathbf{P}$  we find, for the first equations:

$$
\pi_ {G _ {0}} = \pi_ {G _ {0}} (1 - \delta) p _ {0 0} + \pi_ {G _ {1}} (1 - \delta) p _ {0 0} (m) + \pi_ {B} (1 - \delta) p _ {1 0} (m) \tag {6.7}
\pi_ {G _ {1}} = \pi_ {G _ {0}} \delta p _ {0 0} + \pi_ {G _ {1}} \delta p _ {0 0} (m) + \pi_ {B} \delta p _ {1 0} (m) \tag {6.8}
$$

Note that the first and the second column of the transition matrix are the same one in terms of  $p$ 's, except for the factors  $(1 - \delta)$  and  $\delta$ . Therefore the right hand sides of (6.8) are proportional according to  $\delta / (1 - \delta)$ .

We can compute then the ratio between  $\pi_{G_0}$  and  $\pi_{G_1}$  and find:

$$
\pi_ {G _ {1}} = \frac {\delta}{1 - \delta} \pi_ {G _ {0}} \tag {6.9}
$$

and, from the normalization condition retrieve  $\pi_B$ :

$$
\pi_ {B} = 1 - \pi_ {G _ {0}} - \pi_ {G _ {1}} = 1 - \pi_ {G _ {0}} - \frac {\delta}{1 - \delta} \pi_ {G _ {0}} = 1 - \frac {\pi_ {G _ {0}}}{1 - \delta} \tag {6.10}
$$

Therefore, we have from rewriting (6.9) and (6.10):

$$
(1 - \delta) \pi_ {G _ {1}} = \delta \pi_ {G _ {0}} \qquad (1 - \delta) \pi_ {B} = 1 - \delta - \pi_ {G _ {0}}
$$

Using these last two expressions in (6.8):

$$
\pi_ {G _ {0}} = \pi_ {G _ {0}} (1 - \delta) p _ {0 0} + \delta \pi_ {G _ {0}} p _ {0 0} (m) + (1 - \delta - \pi_ {G _ {0}}) p _ {1 0} (m)
\pi_ {G _ {0}} (1 - (1 - \delta)) p _ {0 0} - \delta p _ {0 0} (m) + p _ {1 0} (m)) = (1 - \delta) p _ {1 0} (m)
$$

and using  $p_{00} = 1 - p_{01}$  and  $p_{00}(m) = 1 - p_{01}(m)$  we obtain:

$$
\pi_ {G _ {0}} = \frac {(1 - \delta) p _ {1 0} (m)}{(1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) + p _ {1 0} (m)}
$$


while:

$$
\begin{array}{l} 1 - \pi_ {G _ {0}} = 1 - \frac {(1 - \delta) p _ {1 0} (m)}{(1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) + p _ {1 0} (m)} = \\ \frac {(1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) + p _ {1 0} (m)}{(1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) + p _ {1 0} (m)} \\ \end{array}
$$

We can substitute these two expressions for  $\pi_{G_0}$  and  $1 - \pi_{G_0}$  in (6.6), where we care only about the numerator since the denominator is equal for the just mentioned expressions and therefore cancels, finally obtaining the throughput:

$$
\eta = \frac {(1 - \delta) p _ {1 0} (m)}{[ (1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) + \delta p _ {1 0} (m) ] m + (1 - \delta) p _ {1 0} (m)} \tag {6.11}
$$

## 6.0.4 Bidirectional Markov packet errors - 2 states model

Since there is no need to keep memory of the feedback channel state (as feedback errors are i.i.d.), the same protocol can be represented with only two states, i.e.  $G$  and  $B$ . By splitting  $G$  we make the good transmission channel to be deterministic: we can know deterministically whether there will be either the reward and how much time passes depending on which state we are, so  $G_0$  or  $G_1$ , and therefore the goodness of the feedback. We can merge these two states, with the consequence that a visit to this state may return different outcomes with different probabilities.

![[Stochastic_Processes_2020_p235_img91.jpeg]]
Figure (6.5) - Representation of the embedded Markov chain for the 2-states model for GoBackN protocol, where feedback errors are i.i.d.

When we visit state  $G$  we may have either a reward with probability  $(1 - \delta)p_{00}$  or not with probability  $\delta p_{00}(m)$  depending on the feedback. The two states now have been merged, and so the outcome is probabilistic.

We know eventually how to threat these semi-Markov processes from the theory, where rewards follow a certain distribution. Visit to  $B$  is always a failure.

In summary, for a visit to state  $G$  we have:

- reward: 1 with prob.  $(1 - \delta)$  and 0 with prob.  $\delta$ , average  $R_{G} = (1 - \delta)$
- time: 1 with prob.  $(1 - \delta)$  and m with prob.  $\delta$ , average  $T_{G} = (1 - \delta) + m\delta$
- transition to  $\mathrm{G}$  with prob.  $(1 - \delta)p_{00} + \delta p_{00}(m)$
- transition to B with prob.  $(1 - \delta)p_{01} + \delta p_{01}(m)$

whereas for a visit to state  $B$  we have that:

- no reward:  $R_{B} = 0$


time: always $m$, $T_{B}=m$
- transition to G with prob. $p_{10}(m)$
- transition to B with prob. $p_{11}(m)$

All this scheme defines entirely our semi-Markov model. Equivalently it can be expressed in the following forms:

$\mathbf{P}=\left\lVert(1-\delta)p_{00}+\delta p_{00}(m)\quad(1-\delta)p_{01}+\delta p_{01}(m)\right\rVert$ (6.12)

and the reward and time vectors are:

$\mathbf{R}=\binom{R_{G}}{R_{B}}=\binom{1-\delta}{0}\qquad\mathbf{T}=\binom{T_{G}}{T_{B}}=\binom{1-\delta+m\delta}{m}$

Now we need to compute the throughput $\eta=\frac{\sum_{i}\pi_{i}R_{i}}{\sum_{i}\pi_{i}T_{i}}=\frac{\pi_{G}R_{G}+\pi_{B}R_{B}}{\pi_{G}T_{G}+\pi_{B}T_{B}}$.
$\pi$’s are the limiting probabilities for the matrix (6.12), and keeping in mind the direct formula for the limiting probabilities for a two states Markov chain:

$\pi_{G}$ $=\frac{p_{10}(m)}{p_{10}(m)+(1-\delta)p_{01}+\delta p_{01}(m)}$
$\pi_{B}$ $=\frac{(1-\delta)p_{01}+\delta p_{01}(m)}{p_{10}(m)+(1-\delta)p_{01}+\delta p_{01}(m)}$

Finally the throughput:

$\eta$ $=\frac{\pi_{G}R_{G}+\pi_{B}R_{B}}{\pi_{G}T_{G}+\pi_{B}T_{B}}=\frac{(1-\delta)\pi_{G}}{(1-\delta+m\delta)\pi_{G}+m(1-\pi_{G})}=$
$=\frac{(1-\delta)p_{10}(m)}{(1-\delta+m\delta)p_{10}(m)+m[(1-\delta)p_{01}+\delta p_{01}(m)]}$

that is equal to (6.11), as expected: two models that represent the same system must return the same values, despite they might be different.
If we consider the case where also errors in data channel are i.i.d. with probability $\epsilon$, we replace $p_{01}$ and $p_{01}(m)$ with $\epsilon$, and $p_{10}(m)$ with $1-\epsilon$, then throughput becomes:

$\eta_{iid}$ $=\frac{(1-\delta)(1-\epsilon)}{(1-\delta+m\delta)(1-\epsilon)+m[(1-\delta)\epsilon+\delta\epsilon]}$
$=\frac{(1-\delta)(1-\epsilon)}{(1-\delta)(1-\epsilon)+m[1-(1-\delta)(1-\epsilon)]}$

Comparing this last result with (6.4), we recognize that a system with i.i.d. errors in both directions with probabilities of success $1-\epsilon$ and $1-\delta$, respectively, is equivalent to a system with error-free feedback in which the success probability on the direct channel is the product of the two,


i.e. $(1-\epsilon)(1-\delta)$. In other words, if we have i.i.d. errors in both directions, as long as the product of the two rates is the same, then the specific probabilities are not important. We can therefore assign "all" the error rate to a direction, and set it equal to the product computed before. Doing so, we obtain a system that is equivalent. We can even slightly change the weights of probabilities and find an other equivalent system, as long as the product remains constant.

## 6.1 Counting processes and their statistics

We will now study a new argument that may seem unrelated from what we have just seen up to now. However, coming to a conclusion, we will note that our topics will be very similar to Markov models with metrics: this will allow us to use results we already know for renewal and semi-Markov processes.

We would like now to find the statistics of the number of successful slots up to time $n$. We assume the process is Markovian and binary, and so we denote:

$$
0 = \text{correct transmission} \quad 1 = \text{erroneous transmission}
$$

In other words we observe a sequence of $n$ consecutive states, and see how many of them are successful and how many are not.

Let us define the conditional probability that we observe $k$ good slots in time horizon of length $n$, and moreover we observe that the process is at state $j$ at time $n$ given it started in state $i$. We have four variables: $i$ sets the condition of where the chain started at time 0, whereas $j$ indicates the destination state at time $n$. The other two quantities introduced are $n$ that counts the total number of transitions we are considering, and $k$ which corresponds to how many visits we have made to the successful state. Formally:

$$
\phi_{ij}(k,n) = P[k \text{ good slots in } 0,1,...,n-1, \text{ } j \text{ in } n \mid i \text{ in } 0] \tag{6.13}
= P \left[ \sum_{m=0}^{n-1} \mathbb{1}\{X_m = 0\} = k, X_n = j \mid X_0 = i \right]
$$

where we count the number of visits in state 0 thanks to the indicator function.

We can solve it recursively, using a similar argument to the one we used for first-step analysis: we can exploit the Markov property to write recursive relationships. First we need to condition on last transition, and so at time $n-1$. We then try to find how a chain starting from state $i$ can visit at time $n$ the $j$-th state, having visited the 0 state a certain amount of times. By conditioning we mean that we must take into account that last state can be either $j \in \{0,1\}$.

In the first case, the last transition is a success and happens with probability $p_{0j}$, hence at time $n-1$ there must have been only $k-1$ visits to state 0 in order to reach the total of $k$ successes, and from this argument the factor $\phi_{i0}(k-1,n-1)$. On the other hand, if the last transition is to state 1


(i.e. a failure) with probability $p_{1j}$, at the very previous time step we must have visited the state $0$ all the times we are asked for, namely $k$, and the term $\phi_{i1}(k,n-1)$ follows.

In formulas:

$\phi_{ij}(k,n)=\phi_{i0}(k-1,n-1)p_{0j}+\phi_{i1}(k,n-1)p_{1j}\quad n>0,\ k\leqslant n$ (6.14)

that is valid for all $n>0$ and for $k\leqslant n$ since we cannot have more successes than transitions.

We have found now the statistics at the $n$-th time step, i.e. $\phi_{ij}(k,{\bf n})$, in function of a similar statistics at the $n-1$-th time step, i.e. $\phi_{i0}(k-1,{\bf n-1})$ and $\phi_{i1}(k,{\bf n-1})$. This is indeed a recursive relation that allows us to go back in time up to the very first time step, where we hit the boundary condition. The boundary condition, for $n=0$, describes the situation where no transition can occur and so initial and ending states coincide. Therefore:

$$
\phi_{ij}(k,0)=\begin{cases}1&\text{for }i=j,k=0,n=0\\
0&\text{otherwise}\end{cases}=\delta_{ij}\delta(n)\delta(k)
$$ (6.15)

that tells us that the probability is $1$ only if states $i$ and $j$ coincide, meaning that no transition occurred ($n=0$) and consequently no success ($k=0$) as well.

We can rewrite this argument using Kronecker’s delta $\delta_{ij}$ and Dirac’s delta ($\delta(n)$ , $\delta(k)$) formalism, as stated above.

Moreover it holds that:

$$
\phi_{ij}(k,n)=0\qquad k<0\quad\text{or}\quad n<0\quad\text{or}\quad k>n
$$

because clearly it does not have any sense to make a negative number of transitions/successes, or have a number of successes larger than the number of transitions. Hence (6.14)+(6.15)+(6.16) completely define the statistics that we are looking for. First we note that (6.14) is zero for $n=0$, while (6.15) is not and so only the latter applies. Whereas when $n>0$ (6.14) applies, the other ones do not, being all of them $0$. We can sum them, since they refer to different cases, in order to consider all possible values for $n$:

$$
\phi_{ij}(k,n)=\phi_{i0}(k-1,n-1)p_{0i}+\phi_{i1}(k,n-1)p_{1j}+\delta_{ij}\delta(n)\delta(k)
$$

or taking into account that $i\in\{0,1\}$ and $j\in\{0,1\}$, we can arrange the $\phi_{ij}(k,n)$ in matricial form:

$$
\phi(k,n)=\begin{pmatrix}\phi_{00}(k,n)&\phi_{01}(k,n)\\
\phi_{10}(k,n)&\phi_{11}(k,n)\end{pmatrix}
$$ (6.17)

that in turn can be rewritten as the matrix equation, where we consider all possible combinations of values for $i$ and $j$ for the expression $\phi_{ij}(k,n)$


$\phi_{ij}(k,n)=\phi(k-1,n-1)\begin{pmatrix}p_{00}&p_{01}\cr 0&0\end{pmatrix}+\phi(k,n-1)\begin{pmatrix}0&0\cr p_{10}&p_{11}\end{pmatrix}+\delta(n)\delta(k)\hbox{\rm 1\hskip-2.84526pt1}_{2}$

Let us define the two following matrices:

$\mathbf{P}(0)=\begin{pmatrix}0&0\cr p_{10}&p_{11}\end{pmatrix}\qquad\mathbf{P}(1)=\begin{pmatrix}p_{00}&p_{01}\cr 0&0\end{pmatrix}$

And finally:

$\phi_{ij}(k,n)=\phi(k-1,n-1)\mathbf{P}(0)+\phi(k,n-1)\mathbf{P}(1)+\delta(n)\delta(k)\hbox{\rm 1\hskip-2.84526pt1}_{2}\qquad n\geqslant 0$ (6.18)

where we note that $\mathbf{P}(1)$ contains the *good* transitions that start from $0$, whereas $\mathbf{P}(0)$ contains the *bad* transitions that start from $1$.

Matrix $\mathbf{P}(i)$ through the index $i$ therefore counts the number of successes, that is $1$ for $i=1$ and $0$ for $i=0$. $\phi_{ij}(k,n)$ can be split into two terms: one where we have $k-1$ successes at the time step before and the remaining success is provided by $\mathbf{P}(1)$, whereas if we have already $k$ successes, no more are needed and $\mathbf{P}(0)$ follows.

We can apply the same analysis to *any finite-state* Markov chain where we want to distinguish between two types of transitions. In other words we can *divide all possible transitions, whose number is finite, into two groups according to some criterion*. After, we pick one group and write all its transitions into a matrix setting to zero the other ones, and finally we do the same with the other group. We thus obtain two matrices of the same kind of $\mathbf{P}(i)$, whose sum is the general transition probabilities matrix $\mathbf{P}$. By doing this, we are essentially counting the transitions of the type $\mathbf{P}(1)$. Obviously this argument can be generalized to a generic transition *counting* or *labelling*, by using the same machinery.

The analysis we have made so far is very similar to first-step analysis, but the condition we set on the *last* transition and not on the *first* one. If we did this way:

$\phi_{0j}(k,n)$ $=p_{00}\phi_{0j}(k-1,n-1)+p_{01}\phi_{1j}(k,n-1)+\delta_{0j}\delta(n)\delta(k)$
$\phi_{1j}(k,n)$ $=p_{10}\phi_{0j}(k-1,n-1)+p_{11}\phi_{1j}(k,n-1)+\delta_{1j}\delta(n)\delta(k)$

Where for the first expression, having we started in the *good* state, we have already counted one success and therefore we need $k-1$ successes in the elapsing $n-1$ time steps. Conversely, if we start in $1$ state the first transition is *bad*, and so regardless the destination of the following transition we need to count $k$ successes in the next $n-1$ time steps.

In matrix form:

$\phi(k,n)=\mathbf{P}(1)\phi(k-1,n-1)+\mathbf{P}(0)\phi(k,n-1)+\delta(n)\delta(k)\hbox{\rm 1\hskip-2.84526pt1}_{2}\qquad n\geqslant$


Comparing the last result with (6.18) we can see that the terms are actually the same ones, and so expressions are equal including the same boundary conditions, except for the order of the matrix products that is reversed. This is what we expected, being them two models describing the same quantities, and obviously they must provide a unique result.

We started from a counting problem, where we wanted to count the visits to a given state in a Markov chain, and found the recursive relation (6.18) that we are going to solve.

#### 6.1.1 Transform methods for recursive equations

The equation:

$\phi(k,n)=\mathbf{P}(1)\phi(k-1,n-1)+\mathbf{P}(0)\phi(k,n-1)+\delta(n)\delta(k)\mathbb{1}_{2}\qquad n\geqslant$ (6.19)

can be solved either by computing the solution recursively, where we compute the quantities pointed out in the equations for increasing $n$, or using the transform method. This can be done because we are dealing with relations of the kind $\phi(k,n)=f(\phi(k-1,n-1))$, and so they can be mapped into an other domain where they are easier to solve.

We apply a transform, which is similar to $z$-transform, to our $\phi(k,n)$ noting that it must be done in a two dimensional domain:

$\varphi(s,z)=\sum_{k=0}^{+\infty}s^{k}\sum_{n=0}^{+\infty}z^{n}\phi(k,n)$

Note as the only difference from the $z$-transform is the sign of the exponential. Using this formalism, whenever we have a time shift (i.e. in the original variable $n\to n+1$), we only need to multiply the transform by the correspondent variable to the power that points out the time difference. Specifically the transform version for (6.19):

$\varphi(s,z)=\varphi(s,z)\mathbf{P}(1)sz+\varphi(s,z)\mathbf{P}(0)z+\mathbb{1}$ (6.20)

where we applied, with regards to initial condition, the fact that the transform of $\delta(n)$, $\delta(k)$ is 1. Solving for $\varphi(s,z)$:

$\varphi(s,z)=[\mathbb{1}-\mathbf{P}(1)sz-\mathbf{P}(0)z]^{-1}=[\mathbb{1}-z(\mathbf{P}(1)s+\mathbf{P}(0))]^{-1}$
$=\sum_{n=0}^{+\infty}\left[\mathbf{P}(1)s+\mathbf{P}(0)\right]^{n}z^{n}$ (6.21)

where in the last passage we use an equivalent formulation of the scalar geometric sum, that is $\sum_{k=0}^{+\infty}u=(1-a)^{-1}$. This formula can be rewritten in matricial form, where it holds that:

$\sum_{k=0}^{+\infty}\mathbb{A}^{k}=[\mathbb{1}-\mathbb{A}]^{-1}$


and $\mathbb{A}=z(\mathbf{P}(1)s+\mathbf{P}(0))$.

Comparing this last result (6.21) with the definition (6.20), we can easily invert transform with respect to $z$. Therefore:

$\varphi(s,n)=\sum_{k=0}^{+\infty}s^{k}\phi(k,n)=\text{transform over $k$ for a fixed $n=\left(\mathbf{P}(1)s+\mathbf{P}(0)\right)^{n}$}$ (6.22)

Now we want to make the second step, i.e. find the coefficients for $s^{k}$. This can be done in principle, by expanding $\left(\mathbf{P}(1)s+\mathbf{P}(0)\right)^{n}$ the $n$-th grade polynomial and finding the matrix coefficient for $s$. Matrix coefficient for $s^{k}$ will be $\phi(k,n)$, according to transform definition.

> [!example] Example 16
>
> Let us study an example using the results we have just obtained. We want to find the average number of good slots in $0,1,2,...,n-1$ given an initial state $i$. We can recall the definition (6.13) of $\phi_{ij}(k,n)$, where we focus only on the number of good slots and not on the final state. In order to do so, we need to sum (i.e.) over all possible $j$. Therefore it is needed to sum up the first row of matrix (6.17), so obtaining :
>
> $\varphi_{i0}(s,n)+\varphi_{i1}(s,n)$ (6.23)
>
> which is the transform of the statistics of the number of successes, given the initial state. In addition, the latter is the generating function of the number visits to state $0$ in a fixed time $0,1,2,...,n-1$ and given we start in $i$, and can be obtained by computing (6.22).
>
> We want to stress another time that we need to sum over $j$, otherwise we would have the joint distribution where we would take into account the different landing states. The average number of successes can be obtained by deriving one time (6.23) and finally setting $s=1$:
>
> $\varphi^{\prime}(1,n)=\frac{d\varphi(s,n)}{s}\Big{|}_{s=1}$
>
> Recall that now we are dealing with matrices where order of multiplication does matter.
>
> When we compute the first derivative for (6.21), we can not apply the "plain" rule for scalars i.e. $f^{\prime}([ax+b]^{n})=an(ax+b)^{n-1}$: in the intermediate passage we would end up with $n$ addends of the kind $a(ax+b)^{n-1}$ that are actually the same one. We need indeed to take into account now that deriving the $k$-th term of the product may return different result from the other $k-1$-th or $k+1$-th, because they are matrices. So we obtain:
>
> $\varphi^{\prime}(1,n)=\frac{d\varphi(s,n)}{s}\Big{|}_{s=1}=\sum_{k=0}^{n-1}\Big{(}\mathbf{P}(1)s+\mathbf{P}(0)\Big{)}^{k}\mathbf{P}(1)\Big{(}\mathbf{P}(1)s)+\mathbf{P}(0)\Big{)}^{n-1-k}\Big{|}_{s=1}=$
>
>
> $$
> = \sum_{k=0}^{n-1} \mathbf{P}^k \mathbf{P}(1) \mathbf{P}^{n-1-k}
> $$
>
> where we used the fact that $\mathbf{P}(0) + \mathbf{P}(1) = \mathbf{P}$. What we want to compute is given by the sum of each row in the matrices shown in the last expression. Formally, in matrix notation, this is represented by:
>
> $\varphi'(1,n)\left( \begin{array}{c}1\\ 1 \end{array} \right) = \text{we sum the elements of each row, i.e. over the final state } j =$
>
> $$
> = \sum_{k=0}^{n-1} \mathbf{P}^k \mathbf{P}(1) \mathbf{P}^{n-1-k} \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \sum_{k=0}^{n-1} \mathbf{P}^k \mathbf{P}(1) \left( \begin{array}{c} 1 \\ 1 \end{array} \right) =
> $$
>
> where we used the fact that $\mathbf{P}^{n-1-k}$ is a transition probability matrix, and therefore all rows sum to 1. Consequently the product $\mathbf{P}^{n-1-k} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ returns $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ itself.
>
> Recalling $\mathbf{P}(1) = \begin{pmatrix} p_{00} & p_{01} \\ 0 & 0 \end{pmatrix}$, the product $\begin{pmatrix} p_{00} & p_{01} \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.
>
> Consequently:
>
> $$
> = \sum_{k=0}^{n-1} \mathbf{P}^k \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \left( \begin{array}{c} \sum_{k=0}^{n-1} \mathbf{P}_{00}^{<k>} \\ \sum_{k=0}^{n-1} \mathbf{P}_{10}^{<k>} \end{array} \right) \tag{6.24}
> $$
>
> where we "keep" only the first column of $\mathbf{P}$, and get the average over $k$ steps. Another way to see it, is that we want to compute:
>
> $$
> \begin{pmatrix}
> \mathbb{E}[\# \text{successes in } 0, ..., n-1 \mid X_0 = 0] \\
> \mathbb{E}[\# \text{successes in } 0, ..., n-1 \mid X_0 = 1]
> \end{pmatrix}
> =
> \begin{pmatrix}
> \varphi_{00}'(1, n) + \varphi_{01}'(1, n) \\
> \varphi_{10}'(1, n) + \varphi_{11}'(1, n)
> \end{pmatrix}
> =
> \varphi'(1, n) \begin{pmatrix} 1 \\ 1 \end{pmatrix}
> $$
>
> That is what we have just obtained. Note that we found this result by using the transform formalism. For the result (6.24) by the way, we can use the "old" and simple one:
>
> $$
> \begin{aligned}
> \mathbb{E}[\# \text{of visits to } 0 \mid X_0 = i] &= \mathbb{E}\left[ \sum_{k=0}^{n-1} \mathbb{1}\{X_k = 0\} \mid X_0 = i \right] = \\
> &= \sum_{k=0}^{n-1} \mathbb{E}\left[ \mathbb{1}\{X_k = 0\} \mid X_0 = i \right] = \sum_{k=0}^{n-1} P[X_k = 0 \mid X_0 = i]
> \end{aligned}
> $$
>
> where the last one is the $k$-step transition probability from 0 to $i$, that is the result (6.24).
>
> 242</k></k>

#### 6.1.2 Generalization

Recalling now the equation:

$$\phi(k,n)=\phi(k-1,n-1)\mathbf{P}(1)+\mathbf{P}(0)\phi(k,n-1)+\delta(n)\delta(k)\mathbf{\mathbb{1}}_{2}\qquad n\geqslant$$

we see as $\phi(k,n)$ has been rewritten as the sum of two transition types: the one where we have a success $\mathbf{\mathbb{P}}(1)$ term, and the other one $\mathbf{\mathbb{P}}(0)$ where no successes occur.

Now we want to study a more general case, where we associate an integer metric to each transition. Let $\mathbf{P}(l)$ be the matrix that contains all elements of $\mathbf{P}$ that correspond to a reward of the deterministic metric $l$. We have that:

$$\phi(k,n)=\sum_{l=0}^{+\infty}\phi(k-l,n-1)\mathbf{P}(l)+\delta(n)\delta(k)\mathbf{\mathbb{1}}_{2}$$ (6.25)

Where we note that in order to accumulate $k$ total reward at time $n$, we must have accumulated $k-l$ total reward up to time $n-1$. Moreover, in this generalization, the condition $k\leqslant n$ does not apply any more. Transforming (6.25) we obtain:

$$\varphi(s,z)=\varphi(s,z)\psi(s)z+\mathbf{\mathbb{1}}$$

where $z$ factor is due to the time delay $n-1$, and where we have introduced:

$$\psi(s)=\sum_{l=0}^{+\infty}\mathbf{P}(l)s^{l}$$

This is indeed not surprising at all: $\phi(k-l,n-1)\mathbf{P}(l)$ can be seen as a discrete convolution in $k,l$, and so the sum over all possible values of $l$ returns the product of the convolution.

As we did before, we can solve for $\varphi(s,z)$ keeping in mind that $\psi(s)$ is now a polynomial in $s$:

$$\varphi(s,z)=[\mathbf{\mathbb{1}}-\psi(s)z]^{-1}$$

Now we can retrieve the transform for $\phi(k,n)$ and fixed $n$, so being able to write:

$$\varphi(s,n)=[\psi(s)]^{n}$$

in a similar way we did before, where the only values for $l\in\{0,1\}$.

Let us discuss a little what we have found up to now by pointing out some facts:

- we still can find the average number of rewards in $0,1,...,n-1$ as before, that was a particular case where $\psi(s)=\mathbf{P}(0)+\mathbf{P}(1)s$. That is to say we can compute it by finding the first derivative of the generating function in $s=1$, noting that this function is composed by a linear combination of all possible initial states.


- the 2-d transform $\varphi(s,z)$ is a linear combination of some matrices multiplied by the product of $s$ and $z$ to a certain power. These matrices describe the probabilities for a certain transition to occur. More specifically, $s$ labels the successes/rewards, while $z$ the number of transitions.
- each transition $i\to j$ has a "label" $\psi_{ij}(s)$. Indeed $\psi(s)$ is a matrix of polynomial, of which every element corresponds to a specific transition that can be labelled accordingly.
- nothing forces us to have a random metric for each transition, contrary to what we have done up to now. In other words, for a specific transition we may have a reward that changes with different probability. That is, we can have:

$\psi_{ij}(s)=\sum_{l=0}^{+\infty}P_{ij}(l)s^{l}$

where $P_{ij}(l)$ is the *joint* probability of transition $i\to j$ *and* that the value of the metric is $l$.
Consequently for each transition we have a probability distribution that tells us how much reward we obtain.

Properties of $\psi_{ij}(s)$:

1. $\psi_{ij}(1)=P_{ij}\qquad\psi(1)=\mathbf{P}$

when $s=1$ we can sum over all $l$ possible rewards, and so *remove its dependence in the joint probability* $P_{ij}(l)$. In this way $\psi(1)$ becomes the transition probability matrix $\mathbf{P}$ of the chain
2. $\frac{\psi_{ij}(s)}{p_{ij}}$ is the generating function of the distribution of the metric, once we have *fixed* the *transition* $i\to j$. Note that for $s=1$, this ratio becomes $1$, and so it is moreover *normalized*
3. $\psi_{ij}^{\prime}(s)=\frac{d\psi_{ij}}{ds}\Big{|}_{s=1}=P_{ij}\cdot\text{average metric on }i\to j$
4. if the metric is the reward, recalling the definition of the average reward for a visit to state $i$, then $R_{i}=\sum_{j}P_{ij}R_{ij}$ that we have already computed in 2), and so $R_{i}=\sum_{j}\psi_{ij}^{\prime}(1)$.
- We can define multiple metrics, i.e. $s$ could be vector $\vec{s}=(s_{1},s_{2},...)$ instead of a single variable. Each of its component will therefore counts a different metric. In this case, the average becomes:

$p_{ij}\cdot\text{average of the }k\text{-th metric on }i\to j=\frac{\partial\psi_{ij}(s_{1},s_{2},...)}{\partial s_{k}}\Big{|}_{\vec{s}=\vec{1}}$
- How to compute $\psi_{ij}(\vec{s})$.
First we state that there is a Markov model underlying transitions $i\to j$. Then:


1. let $\varepsilon(i,j)$ be the set of all events that correspond to a transition from state $i \to j$
2. let each event $A$ in this set have the probability $P[A]$
3. let each event $A$ correspond to a different value for the metric, that is equivalent to state that we define $A$ as a possible value for the joint probability $\vec{s}(A) = s_1^{l_1(a)} s_2^{l_2(a)}$ ..., where $l_k(A)$ is the value of the metric that corresponds to event $A$
4. under all these assumptions, it holds that:

$$
\psi_{ij}(\vec{s}) = \sum_{A \in \varepsilon(i,j)} P[A] \vec{s}(A)
$$

thus it becomes a counting exercise: we should need to make a list of all possible events and each with its own probability and value of the metric, and then group the these elements according to the transition they produce. Each of them will be an entry for the matrix $\psi$.

Note that:

$$
\psi_{ij}(\vec{s} = \vec{1}) = \sum_{A \in \varepsilon(i,j)} P[A] = P_{ij}
$$

Now, recall that we have just found that the average $k$-th metric times the probability $i \to j$:

$$
R_{ij}^{(k)} P_{ij} = \left. \frac{\partial \psi_{ij}(\vec{s})}{\partial s_k} \right|_{\vec{s} = 1} = \psi_{ij}^{(k)} \, {}' (s)
$$

and, summing over $j$:

$$
\sum_j R_{ij}^{(k)} P_{ij} = \sum_j \psi_{ij}^{(k)} \, {}' (s) = R_i^{(k)} \tag{6.26}
$$

that is the average $k$-th reward accumulated so far.

From the renewal reward theory we have found that with probability 1:

$$
\lim_{t \to \infty} \frac{R^{(1)}(t)}{R^{(2)}(t)} = \frac{\sum_i \pi_i R_i^{(1)}(t)}{\sum_i \pi_i R_i^{(2)}(t)} = \frac{\sum_i \pi_i \sum_j \psi_{ij}^{(1)} \, {}' (1)}{\sum_i \pi_i \sum_j \psi_{ij}^{(2)} \, {}' (1)} =
$$

where we replaced $R_i^{(1)}(t)$ and $R_i^{(2)}(t)$ using (6.26) and by right multiplying it time $\vec{1}$: when we right multiply a matrix by a vector of $\vec{1}$, we obtain a column vector where each element is the sum of the corresponding row of the matrix.

$$
= \frac{\sum_{i} \pi_i \left. \frac{\partial \psi_{ij}(\vec{s})}{\partial s_1} \right|_{\vec{s} = 1} \cdot \vec{1}}{\sum_{i} \pi_i \left. \frac{\partial \psi_{ij}(\vec{s})}{\partial s_2} \right|_{\vec{s} = 1} \cdot \vec{1}} = \frac{ \overbrace{\vec{\pi}}^{\text{row}} \cdot \overbrace{ \left. \frac{\partial \psi_{ij}(\vec{s})}{\partial s_1} \right|_{\vec{s} = 1} \cdot \vec{1} }^{\text{column}} }{ \underbrace{ \vec{\pi} \cdot \left. \frac{\partial \psi_{ij}(\vec{s})}{\partial s_2} \right|_{\vec{s} = 1} \cdot \vec{1} }_{\text{scalar}} }
$$


We should have recognized that the sum over the  $i$ -th component of the product  $\pi_i$  and the column vector  $\left.\frac{\partial\psi_{ij}(\vec{s})}{\partial s_k}\right|_{\vec{s} = 1}\cdot \vec{1}$  is the definition of the scalar product, and therefore the last expression follows.

Note that we have just found the average value of metric 1 per unit of metric 2 in the limit as  $t \to \infty$ . In order to compute it, all we need is the matrix  $\psi(\vec{s})$ : it contains both the transition probability matrix and the information needed for the metric. In fact we can obtain  $\mathbf{P} = \psi(\vec{s} = \vec{1})$  and, from this, compute the limiting distribution of the chain  $\vec{\pi} = \vec{\pi}\mathbf{P}$ . Whereas in order to compute the  $R^{(k)}$  it is sufficient to compute the first partial derivative of  $\psi(\vec{s})$  wrt  $s_k$  and set  $\vec{s} = \vec{1}$ .

It is important to point out that once we have defined our system, computing  $\psi_{ij}(\vec{s})$  for all transitions, in the way we stated above, we can obtain for example the ratio  $\lim_{t\to \infty}\frac{R^{(1)}(t)}{R^{(2)}(t)}$  thanks to a standard procedure. Obviously this does not take into account technical difficulties that may arise during calculations, that are unbounded from the theoretical result we have just written.

One other important result is that if we consider matricial operations, such as the ones in the ratio above, the number of states is not important. We can therefore have so many states as we want, as long as we are able to find the matrix  $\psi_{ij}\vec{s}$ , and the theory we have just gone through will give us the correct result. This is indeed a general result.

# 6.1.3 GoBackN protocol - Transform approach

As a concrete example of the generalization for computing the matrix  $\psi_{ij}(\vec{s})$ , we will now study the GoBackN protocol with i.i.d. feedback errors with probability  $\delta$ . Recalling its transition diagram.

![[Stochastic_Processes_2020_p246_img92.jpeg]]
Figure (6.6) - Representation of the embedded Markov chain for the 2-states model for GoBackN protocol, where feedback errors are i.i.d. with probability  $\delta$ .

We want in fact to build a model for the protocol shown in (fig 6.6), in order to achieve some results using the formalism we have just introduced. According to the list we have written above, in order to compute  $\psi_{ij}\vec{s}$  we have to proceed through the following steps: define the set  $\varepsilon(i,j)$  of all events, then find both the probability for each event, namely  $P[A]$ , and the corresponding metrics, finally grouping what we have just computed by which transition they refer to.

Now recall that our reward is different from zero, and so the time slot reward is 1, only when we both start from a good state and the acknowledgement is correct. The only rows of the table (???) that satisfy to these requirements are the first two.

This is indeed a very simple model, and so we can deal with the whole list


|  from | to | probability | reward | time  |
| --- | --- | --- | --- | --- |
|  G | G | (1-δ)p00 | 1 | 1  |
|  G | B | (1-δ)p01 | 1 | 1  |
|  G | G | δp00(m) | 0 | m  |
|  G | B | δp01(m) | 0 | m  |
|  B | G | (1-δ)p10(m) | 0 | m  |
|  B | B | (1-δ)p11(m) | 0 | m  |
|  B | G | δp10(m) | 0 | m  |
|  B | B | δp11(m) | 0 | m  |

Table (6.1) - Table depicting all possible combinations for good/bad transmission and good/bad acknowledgement. We have 4 possible transitions between states  $B, G$ , with probability  $p_{ij}$  that corresponds to the correctness of transmission, times the two possible outcomes for the feedback that might be correct with probability  $1 - \delta$  or wrong with probability  $\delta$ . Hence the total number of entries, i.e. rows, is 8.

manually. If it had been more complicated, then we would have found some algorithm in order to compute it automatically for example being helped by a software.

We need to group all the entries in the  $(\ref{eq:1})$  by transition, and we can see that there are actually 4 of them:  $G \to G, B \to G, G \to B, B \to B$ . If we pick as an example all rows that belong to  $G \to G$  transition, they will result in the same  $\psi_{GG}$  and the consequent sum will be over only two events. Of course this applies to all the remaining transitions.

The final step, in order to define  $\psi_{ij}(\vec{s})$ , is to compute the product  $P[A_k]\vec{s}[A_k]$  for each event that belongs to a certain group. The sum will consist in two terms, that are the two distinct events  $A_1, A_2$ , are the product of the probability of each event times  $s_1^{l_1}s_2^{l_2}$ , where  $s_i$  denotes the which metric we are referring to, and  $l_i$  the metric value. Each element of the following matrix will be the result of the just mentioned computation for all possible states:

| ψ(s1,s2) = | (ψGGψGB) | $(1-δ)p_{00}s_1s_2+δp_{00}(m)s_{2m}$ | $(1-δ)p_{01}s_1s_2+δp_{01}(m)s_{2m}$ |
| ---------- | -------- | ------------------------------------ | ------------------------------------ |
|            | ψBGψBB)  |                                      |                                      |

We will show now that this matrix contains all the information about the model. Transition probability matrix can be obtained as:

|  P = ψ(1,1) = | (1-δ)p00 + δp00(m) | (1-δ)p01 + δp01(m)  |
| --- | --- | --- |
|   | p10(m) | p11  |

and consequently the limiting probabilities:

|  πG = p10(m)/p10(m) + (1-δ)p01 + δp01(m) | πB = 1 - πG = (1-δ)p01 + δp01(m)/p10(m) + (1-δ)p01 + δp01(m)  |
| --- | --- |


While $P_{ij}R_{ij}$ are the elements of:

$$
\left. \frac {\partial \psi}{\partial s _ {1}} \right| _ {s _ {1} = s _ {2} = 1} = \left( \begin{array}{c c} (1 - \delta) p _ {0 0} & (1 - \delta) p _ {0 1} \\ 0 & 0 \end{array} \right)
$$

and $P_{ij}T_{ij}$ are the elements of:

$$
\left. \frac {\partial \psi}{\partial s _ {2}} \right| _ {s _ {1} = s _ {2} = 1} = \left( \begin{array}{c c} (1 - \delta) p _ {0 0} + m \delta p _ {0 0} (m) & (1 - \delta) p _ {0 1} + m \delta p _ {0 1} (m) \\ m p _ {1 0} & m p _ {1 1} \end{array} \right)
$$

Consequently $\vec{R}$ and $\vec{T}$, i.e. the column vectors associated to the states found by summing over rows:

$$
\vec {R} = \left. \frac {\partial \psi}{\partial s _ {1}} \right| _ {s _ {1} = s _ {2} = 1} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \left( \begin{array}{c} 1 - \delta \\ 0 \end{array} \right)
\vec {T} = \left. \frac {\partial \psi}{\partial s _ {2}} \right| _ {s _ {1} = s _ {2} = 1} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \left( \begin{array}{c} 1 - \delta + m \delta \\ m \end{array} \right)
$$

Finally, we can compute the **throughput** having all the information we need:

$$
\text {throughput} = \frac {\pi_ {G} R _ {G} + \pi_ {B} R _ {B}}{\pi_ {G} T _ {G} + \pi_ {B} T _ {B}} = \frac {(1 - \delta) p _ {1 0} (m)}{(1 - \delta + m \delta) p _ {1 0} (m) + m [ (1 - \delta) p _ {0 1} + \delta p _ {0 1} (m) ]}
$$

that is the same result we have computed before.

We have just shown that the matrix $\psi(s_1, s_2)$ contains all the information we need in order to compute the statistical quantities we are usually interested in. It is indeed a very useful and powerful tool, moreover matricial notation is more compact and, very important, independent of the size of the system.

## 6.1.4 GoBackN protocol - Generalization

We could have computed the throughput, and consequently all the statistics, the other way around using the original approach.

We therefore split $\mathbf{P} = \mathbf{P}_S + \mathbf{P}_F$, that are respectively the transition matrices for successes and failures. Note that we used to call these matrices $\mathbf{P}(1)$ and $\mathbf{P}(0)$, when we were considering the feedback with no error. Now instead we need to pay attention to which transition probabilities between states $G, B$ of the matrix $\mathbf{P}$ belong to $\mathbf{P}_S$ and which to $\mathbf{P}_F$, they can be indeed split in turn. Thus write:

$$
\mathbf {P} _ {S} = \text {transition matrix for successes} = \left( \begin{array}{c c} (1 - \delta) p _ {0 0} & (1 - \delta) p _ {0} 1 \\ 0 & 0 \end{array} \right)
\mathbf {P} _ {F} = \text {transition matrix for failures} = \left( \begin{array}{c c} \delta p _ {0 0} (m) & \delta p _ {0 1} (m) \\ \delta p _ {1 0} (m) & \delta p _ {1 1} (m) \end{array} \right)
$$


and moreover:

$\psi(s_{1},s_{2})=\mathbf{P}_{S}s_{1}s_{2}+\mathbf{P}_{F}s_{2}^{m}$

where we have chosen the metric according to whether we have a success or not.
We can write recursive relations as we did before, but taking into account that metrics are now 2:

$\phi(k_{1},k_{2},n)=\phi(k_{1}-1,k_{2}-1,n)\mathbf{P}_{S}+\phi(k_{1},k_{2}-m,n)\mathbf{P}_{F}+\mathbb{1}\delta(n)\delta(k_{1})\delta(k_{2})\qquad n\geqslant 0$

Note that if the last transition $n-1\to n$ is a success, then we need at the previous time step the metrics $k_{1}-1$ and $k_{2}-1$. Conversely, if it is a failure, at the previous time step we must have $k_{1}$ for rewards and $k_{2}-m$ for time slots. To the initial condition we apply the same argument we already discussed.
By transforming the last equation we find:

$\varphi(s_{1},s_{2},z)=\varphi(s_{1},s_{2},z)[\mathbf{P}_{S}s_{1}s_{2}z+\mathbf{P}_{F}s_{2}^{m}z]+\mathbb{1}$

and solving for $\varphi(s_{1},s_{2},z)$:

$\varphi(s_{1},s_{2},z)=[\mathbb{1}-(\mathbf{P}_{S}s_{1}s_{2}+\mathbf{P}_{F}s_{2}^{m})z]^{-1}$

and fixing the number of transitions $n$:

$\varphi(s_{1},s_{2},n)=[\mathbf{P}_{S}s_{1}s_{2}+\mathbf{P}_{F}s_{2}^{m}]^{n}=[\psi(s_{1},s_{2})]^{n}$

If we take the partial derivatives we can compute the averages. With respect to the first variable:

$\frac{\partial\varphi(s_{1},s_{2},n)}{\partial s_{1}}=\sum_{k=0}^{n-1}\Big{(}\mathbf{P}_{S}s_{1}s_{2}+\mathbf{P}_{F}s_{2}^{m}\Big{)}^{k}\mathbf{P}_{2}s_{2}\Big{(}\mathbf{P}_{S}s_{1}s_{2}+\mathbf{P}_{F}s_{2}^{m}\Big{)}^{n-1-k}$
$\frac{\partial\varphi(s_{1},s_{2},n)}{\partial s_{1}}\Big{|}=\sum_{k=0}^{n-1}\mathbf{P}^{k}\mathbf{P}_{S}\mathbf{P}^{n-1-k}$

That is a result already found before.
We want to stress out once again that taking the transform, fixing $n$, and summing over columns, namely:

$\sum_{j}\varphi_{ij}(s_{1},s_{2},n)$

is the *joint* generating function of the number of *successes* and the number of slots per $n$ transitions, given that the initial state is $i$.
The *marginal* generating function of successes and slots, given the initial state,


are obtained from above by setting $s_2 = 1$ and $s_1 = 1$, respectively. Therefore:

$$
\left(\mathbb {E} [ \# \text{ of successes in } 0, 1 \dots , n - 1 \mid X _ {0} = G ] \right) = \frac {\partial \varphi (\vec {s} , n)}{\partial s _ {1}} \Big | _ {\vec {s} = \vec {1}} \cdot \binom {1} {1} \tag {6.28}
$$

and

$$
\left(\mathbb {E} [ \# \text{ of slots in } 0, 1 \dots , n - 1 \mid X _ {0} = G ] \right) = \frac {\partial \varphi (\vec {s} , n)}{\partial s _ {2}} \Big | _ {\vec {s} = \vec {1}} \cdot \binom {1} {1}
$$

We want now to compute (6.28), using the results for intermediate matricial products we have computed before:

$$
\frac {\partial \varphi (\vec {s} , n)}{\partial s _ {1}} \Big | _ {\vec {s} = \vec {1}} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \mathbf {P} _ {S} \mathbf {P} ^ {n - 1 - k} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \cdot \vec {R}
$$

where $\vec{R} = \mathbf{P}\cdot \binom{1}{1}$. The last expression is the average number of successes in $n$ transition. If we want to compute its expected value, we take the limit:

$$
\left(\mathbb {E} [ \# \text{ of successes per transition} \mid X _ {0} = G ] \right) = \lim _ {n \to \infty} \frac {1}{n} \left(\sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \cdot \vec {R}\right) =
$$

but note that $\vec{R}$ is independent of $n$, thus we can factorize:

$$
= \left(\lim _ {n \to \infty} \frac {1}{n} \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k}\right) \cdot \vec {R} = \left( \begin{array}{c} \vec {\pi} \cdot \vec {R} \\ \vec {\pi} \cdot \vec {R} \end{array} \right) = \left( \begin{array}{c} \pi_ {G} R _ {G} + \pi_ {B} R _ {B} \\ \pi_ {G} R _ {G} + \pi_ {B} R _ {B} \end{array} \right) =
= \left( \begin{array}{c} (1 - \delta) \pi_ {G} + 0 \cdot \pi_ {B} \\ (1 - \delta) \pi_ {G} + 0 \cdot \pi_ {B} \end{array} \right) = \left( \begin{array}{c} (1 - \delta) \pi_ {G} \\ (1 - \delta) \pi_ {G} \end{array} \right)
$$

where the limit will have all rows equal, and more precisely equal to $\pi$. Note as the last result is the same one for both $X_0 = G$ and $X_0 = B$, and so independent of the initial state as expected.

Similarly for the number of slots:

$$
\varphi (s _ {1}, s _ {2}, n) = [ \mathbf {P} _ {S} s _ {1} s _ {2} + \mathbf {P} _ {F} s _ {2} ^ {m} ] ^ {n}
$$

When computing the second derivative we obtain a slightly different term, that is:

$$
\frac {\partial \varphi (s _ {1} , s _ {2} , n)}{\partial s _ {2}} = \sum_ {k = 0} ^ {n - 1} \left(\mathbf {P} _ {S} s _ {1} s _ {2} + \mathbf {P} _ {F} s _ {2} ^ {m}\right) ^ {k} \left(\mathbf {P} _ {S} s _ {1} + m \mathbf {P} _ {F} s _ {2} ^ {m - 1}\right) \left(\mathbf {P} _ {S} s _ {1} s _ {2} + \mathbf {P} _ {F} s _ {2} ^ {m}\right) ^ {n - 1 - k}
$$


and setting  $\vec{s} = \vec{1}$ :

$$
\frac {\partial \varphi (s _ {1} , s _ {2} , n)}{\partial s _ {2}} \Big | _ {\vec {s} = \vec {1}} = \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} (\mathbf {P} _ {S} + m \mathbf {P} _ {F}) \mathbf {P} ^ {n - 1 - k} = \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} (\mathbf {P} _ {S} + m (\mathbf {P} - \mathbf {P} _ {S})) \mathbf {P} ^ {n - 1 - k} =
\sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} (m \cdot \mathbf {P} - (m - 1) \mathbf {P} _ {S}) \mathrm {)} \mathbf {P} ^ {n - 1 - k} = m \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {n} - (m - 1) \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \mathbf {P} _ {S} \mathbf {P} ^ {n - 1 - k}
$$

where we just made the computation and split the expression into two factors. Note that the second term is common with the other partial derivative wrt  $s_1$ . If we then right multiply the last expression by the vector  $\vec{1}$ :

$$
\begin{array}{l} \frac {\partial \varphi (s _ {1} , s _ {2} , n)}{\partial s _ {2}} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \left(m \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {n} - (m - 1) \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \mathbf {P} _ {S} \mathbf {P} ^ {n - 1 - k}\right) \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) = \\ = m \underbrace {\sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {n}} _ {n \cdot \vec {1}} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) - (m - 1) \underbrace {\sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \mathbf {P} _ {S} \mathbf {P} ^ {n - 1 - k} \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right)} _ {\sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \cdot \vec {R} \text { as we computed before}} = \\ \end{array}
$$

where the first term is the sum of  $n$  vectors all equal to  $\vec{1}$ . Finally:

$$
= m \cdot n \cdot \left( \begin{array}{c} 1 \\ 1 \end{array} \right) - (m - 1) \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \cdot \vec {R}
$$

We can compute, as before:

$$
\left( \begin{array}{l} \mathbb {E} [ \# \text { of slots per transition} \mid X _ {0} = G ] \\ \mathbb {E} [ \# \text { of slots per transition} \mid X _ {0} = B ] \end{array} \right) = \lim  _ {n \to \infty} \frac {1}{n} \left(m \cdot n \left( \begin{array}{l} 1 \\ 1 \end{array} \right) - (m - 1) \sum_ {k = 0} ^ {n - 1} \mathbf {P} ^ {k} \cdot \vec {R}\right) =
$$

with similar calculations to what we did before for the successes:

$$
= \left( \begin{array}{c} m - (m - 1) \vec {\pi} \cdot \vec {R} \\ m - (m - 1) \vec {\pi} \cdot \vec {R} \end{array} \right) = \left( \begin{array}{c} \vec {\pi} \cdot \vec {R} + m (1 - \vec {\pi} \cdot \vec {R}) \\ \vec {\pi} \cdot \vec {R} + m (1 - \vec {\pi} \cdot \vec {R}) \end{array} \right)
$$

In this case as well the two rows are the same, being the asymptotic result independent of the initial state.

Finally the throughput of the system is:

$$
\lim _ {n \to \infty} \frac {\# \mathrm {o f s u c c e s s e s i n} 0 , . . . , n - 1}{\# \mathrm {o f s l o t s i n} 0 , . . . , n - 1} = \frac {(\# \mathrm {o f s u c c e s s e s i n} 0 , . . . , n - 1) / n}{(\# \mathrm {o f s l o t s i n} 0 , . . . , n - 1) / n} =
$$

that with probability 1, for the law of large numbers:

$$
\frac {\mathbb {E} [ \# \text { of successes per transition} ]}{\mathbb {E} [ \# \text { of slots per transition} ]} = \frac {(1 - \delta) \pi_ {G}}{(1 - \delta) \pi_ {G} + m (1 - (1 - \delta) \pi_ {G})} = \frac{(1-\delta)p_{10}(m)}{(1-\delta)p_{10}(m)+m[(1-\delta)p_{01}+\delta p_{01}(m)+\delta p_{10}(m)]}
$$

here we replaced the expectation values per transition with the values we have just computed and remembering that $\vec{\pi}\cdot\vec{R}=(1-\delta)\pi_{G}$. Note that we do not have a condition on the initial state, being this result asymptotic. By replacing with the values of the limiting probabilities $\pi_{G}$ and $\pi_{B}$ from (6.27), we can rewrite the throughput as above, as we found before in (6.11).
We have thus shown that we can use different approaches to study our problem. These are either the probabilistic approach linked to the recursive technique, or the transform method to solve the recursion, or this last approach based on the $\psi$, where we combine together into "transition functions" the transition probabilities as well as the statistics of the related metrics. Obviously, the results we find must be the same ones.


Bibliography

- [1] M.A. Pinsky and S. Karlin. An introduction to stochastic modeling. 4th ed. Academic Press, 2011. isbn: 0233814167.
- [2] M. Zorzi. “Stochastic Processes course at University of Padua”. Handwritten notes. 2020.
- [3] S. Karlin and H. Taylor. A first course in stochastic processes. 2nd ed. Academic Press, 1975. isbn: 0123985536.
- [4] S. Ross. Applied probability models with optimization applications. 2nd ed. Dover, 1996. isbn: 0486673146.


# Analytical index

|  C |   | Total probability | 7  |
| --- | --- | --- | --- |
|  Chain | 7 |  |   |
|  Correlation | 10 | M |   |
|  F |   | Markov |   |
|   |  | Process | 27  |
|  Function |  | Mean | 9  |
|  Cumulative distribution | 8 | Moment |   |
|  Probability density | 8 | Central | 9  |
|  G |   | S |   |
|  Generating function |  | States |   |
|  Probability | 12 | communication | 70  |
|   |  | periodicity | 72  |
|  I |  | recurrent and transient | 74  |
|  Independence | 7 | Stochastic process | 6  |
|  Irreducibility | 71 |  |   |
|  L |   | V |   |
|  Law |  | Variance | 9  |