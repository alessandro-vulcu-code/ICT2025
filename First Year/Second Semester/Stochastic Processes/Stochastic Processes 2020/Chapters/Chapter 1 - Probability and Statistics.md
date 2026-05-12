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


Example 1 (Sum of a random number of random variables):

Let $\{X_i\}_{i=1,\dots,N}$ be a set of independent and identically distributed r.v. (i.i.d. for short), which are discrete and non-negative integer-valued ($X_i \in \mathbb{N}$), with probability generating function $g(s)$. Let $N$ be another discrete r.v. with $N \in \mathbb{N}$ and generating function $g_N(s)$, which is independent of all the $\{X_i\}$. We want to find the statistics of the sum of the $N$ random variables:

$$
R = X_1 + \cdots + X_N
$$

Note that we cannot directly apply the "convolution property" of the generating function, i.e. write:

$$
g_R(s) = \mathbb{E}[s^R] = \prod_{i=1}^{N} g(s)
$$

because $N$ is a random variable, with no definite value.

However, we can compute $\mathbb{E}[s^R]$ for a fixed value of $N$ - denoting the result as $\mathbb{E}[s^R|N]$ - and then average this result over all possible choices of $N$. This procedure is just an application of the law of total probability, and in this way we can use the convolution property for all the averaged terms:

$$
\begin{array}{l}
g_R(s) = \mathbb{E}[s^R] = \mathbb{E}[s^{X_1 + \cdots + X_N}] = \\
= \mathbb{E}\{\mathbb{E}[s^{X_1 + \cdots + X_N}|N]\} =
\end{array}
$$


Expanding the outer average:

$$
= \sum_{n=0}^{+\infty} \mathbb{E}[s^{X_1 + \dots + X_n} | N = n] \mathbb{P}[N = n] =
$$

Since $\{X_i\}$ and $N$ are independent, $\mathbb{E}[s^{X_1 + \dots + X_n} | N = n] = \mathbb{E}[s^{X_1 + \dots + X_n}]$, and so:

$$
= \sum_{n=0}^{+\infty} \overline{\mathbb{E}[s^{X_1 + \dots + X_n}]} \mathbb{P}[N = n] =
$$

Finally we can apply the convolution property:

$$
= \sum_{n=0}^{+\infty} g(s)^n \mathbb{P}[N = n] =
$$

And we recognize the expression for the generating function of $N$:

$$
= \mathbb{E}[g(s)^N] = g_N[g(s)]
$$

We can now compute mean and variance by applying (1.9):

$$
\mathbb{E}[R] = \left. \frac{\mathrm{d} g_R(s)}{\mathrm{d} s} \right|_{s=1} = g_N'[g(s)] \cdot g'(s) \Big|_{s=1} = g_N'[g(1)] \cdot \mathbb{E}[X]
$$

And note that:

$$
g(1) = \sum_{k=0}^{+\infty} \mathbb{P}[X = k] = 1
$$

by normalization. So:

$$
\mathbb{E}[R] = g_N'(1) \cdot \mathbb{E}[X] = \mathbb{E}[N] \cdot \mathbb{E}[X]
$$

Intuitively, if $N$ were fixed, the mean of $R$ would be exactly $N$ times the mean of each summed variable. Here $N$ is not fixed, and so we use its mean instead.

For the variance, we first need the second (factorial) moment, and so we derive once again:

$$
g_R''(s) = g_N''[g(s)] (g'(s))^2 + g_N'(g(s)) g''(s)
$$

And then we evaluate at $s = 1$:

$$
\begin{aligned}
g_R''(1) &= g_N''[1] \mathbb{E}[X]^2 + g_N'(1) \mathbb{E}[X^2 - X] = \\
&= \mathbb{E}[N^2 - N] \cdot \mathbb{E}[X]^2 + \mathbb{E}[N] \cdot \mathbb{E}[X^2 - X] = \\
&= \mathbb{E}[N^2] \mathbb{E}[X]^2 - \mathbb{E}[N] \mathbb{E}[X]^2 + \mathbb{E}[N] \mathbb{E}[X^2] - \mathbb{E}[N] \mathbb{E}[X] = \\
&= \mathbb{E}[N^2] \mathbb{E}[X]^2 + \mathbb{E}[N] \operatorname{Var}(X) - \mathbb{E}[N] \mathbb{E}[X]
\end{aligned}
$$

And finally:

$$
\begin{aligned}
\operatorname{Var}(R) &= \mathbb{E}[R^2] - \mathbb{E}[R]^2 = g_R''(1) + g_R'(1) - (g_R'(1))^2 = \\
&= \mathbb{E}[N^2] \mathbb{E}[X]^2 + \mathbb{E}[N] \operatorname{Var}(X) - \underbrace{\mathbb{E}[N] \mathbb{E}[X]} + \underbrace{\mathbb{E}[N] \mathbb{E}[X]}_{\text{var}} \\
&\quad - \mathbb{E}[N]^2 \mathbb{E}[X]^2 =
\end{aligned}
=\mathbb{E}[N]\,\mathrm{Var}(X)+\mathbb{E}[X]^{2}\,\mathrm{Var}(N)
$$

If $N$ were fixed, the variance of $R$ would just be the sum of the variances of the $X_{i}$, i.e. $N$ times $\mathrm{Var}(X)$. So, as $N$ is not fixed, we would expect to see $\mathbb{E}[N]\,\mathrm{Var}(X)$ - which is indeed the first term. However, there is also $\mathbb{E}[X]^{2}\,\mathrm{Var}(N)$. Intuitively, this is because the random number of elements in the sum introduces “more randomness”, making the distribution more “spread out”.

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


Exercise 1.6.1 (Composition of binomial and Poisson):

Suppose $X$ has a binomial distribution with parameters $p$ and $N$, where $N$ has a Poisson distribution with mean $\lambda$. What is the marginal distribution for $X$?

Solution.

Exercise 1.6.2 (Moments of random sums):

Assume that $\xi_{k}$ and $N$ have finite moments:

$$
\mathbb{E}[\xi_{k}] = \mu; \quad \operatorname{Var}[\xi_{k}] = \sigma^{2}
\mathbb{E}[N] = \nu; \quad \operatorname{Var}[N] = \tau^{2}
$$

Show, by using conditional distributions, that the mean and variance of the sum $X = \xi_{k} + \cdots + \xi_{N}$ are:

$$
\mathbb{E}[X] = \mu \nu; \qquad \operatorname{Var}[X] = \nu \sigma^{2} + \mu^{2} \tau^{2}
$$

which are the same results we obtained by using characteristic functions.

Solution.

#### 1.6.2 Distribution of a Random Sum

Suppose that $\{\xi_i\}_{i=1,\dots,\infty}$ are continuous i.i.d. random variables having a probability density function $f(z)$. For $n \geq 1$, the probability density function for the fixed sum $\xi_1 + \dots + \xi_n$ is the $n$-fold convolution of the density $f(z)$, denoted by $f^{(n)}(z)$ and recursively defined by:

$$
f^{(1)}(z) = f(z)
$$

and:

$$
f^{(n)}(z) = \int_{\mathbb{R}} f^{(n-1)}(z - u) f(u) \, \mathrm{d}u \qquad \forall n > 1
$$

Example 3 (Geometric sum of exponential r.v.):

Consider a set of i.i.d. random variables $\xi_{i}$ with exponential distribution:

$$
f(z) = \begin{cases}
\lambda e^{-\lambda z} & z \geq 0 \\
0 & z < 0
\end{cases}
$$

We consider the sum $Z = \xi_1 + \dots + \xi_N$, where $N$ is a discrete random variable with geometric distribution:

$$
p_N(n) = \beta (1 - \beta)^{n-1} \quad \forall n \in \mathbb{N} \setminus \{0\} \tag{1.18}
$$


We already know that the distribution for the sum of a fixed number $n$ of exponential r.v. (i.e. the $n$-fold convolution of $f(z)$) is the Gamma density:

$$
f^{(n)}(z) = \begin{cases}
\frac{\lambda^n}{(n-1)!} z^{n-1} e^{-\lambda z} & z \geq 0 \\
0 & z < 0
\end{cases} \tag{1.19}
$$

So, to derive the pdf of $Z$ we apply the law of total probability, noting that $p_N(0) = 0$:

$$
\begin{aligned}
f_X(z) &= \sum_{n=1}^{+\infty} f^{(n)}(z) p_N(n) = \\
&= \sum_{\substack{(1.19) \\ (1.18)}}^{+\infty} \sum_{n=1}^{+\infty} \frac{\lambda^n}{(n-1)!} z^{n-1} e^{-\lambda z} \beta (1 - \beta)^{n-1} = \\
\end{aligned}
$$

We bring out some factors so that all exponents in the sum are $n - 1$:

$$
= \lambda \beta e^{-\lambda z} \sum_{n=1}^{+\infty} \sum_{n=1}^{+\infty} \frac{[\lambda(1 - \beta)z]^{n-1}}{(n-1)!} =
$$

Shifting to 0 the index of summation we obtain the exponential series:

$$
\begin{aligned}
&= \lambda \beta e^{-\lambda z} \sum_{n=0}^{+\infty} \frac{1}{n!} [\lambda(1 - \beta)z]^{n-1} = \\
&= \lambda \beta e^{-\lambda z} e^{\lambda(1 - \beta)z} = \lambda \beta e^{-\lambda \beta z} \qquad z \geq 0
\end{aligned}
$$

So $X$ has an exponential distribution with parameter $\lambda \beta$.

Equivalently, we could do this with characteristic functions:

$$
\begin{aligned}
g_N(s) &= \sum_{n=1}^{+\infty} \beta (1 - \beta)^{n-1} s^k = \frac{\beta s}{1 - (1 - \beta)s} \\
\phi(t) &= \mathbb{E}[e^{it\xi}] = \int_0^{+\infty} e^{it\xi - \lambda\xi} \lambda \, d\xi = \frac{\lambda}{\lambda - it}
\end{aligned}
$$

The characteristic function of the random sum is obtained by composition:

$$
\begin{aligned}
g_N(\phi(t)) &= \frac{\beta \frac{\lambda}{\lambda - it}}{1 - (1 - \beta) \frac{\lambda}{\lambda - it}} = \frac{\beta \lambda}{\lambda - it - (\lambda - \beta) \lambda} = \\
&= \frac{\beta \lambda}{\beta \lambda - it}
\end{aligned}
$$

Comparing this result with $\phi(t)$ we see that they are characteristic functions of the same distribution, with the substitution $\lambda \leftrightarrow \beta \lambda$. So, the distribution of the random sum is, in fact, an exponential distribution with parameter $\beta \lambda$.


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