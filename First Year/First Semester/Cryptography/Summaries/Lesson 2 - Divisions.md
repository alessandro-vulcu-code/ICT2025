## 1.0 The Fundamentals of Divisibility

### 1.1 Introduction to Divisibility
The concept of divisibility is a **foundational pillar** of number theory and modern cryptography. It provides the essential structures upon which secure algorithms are built.

### 1.2 Core Definitions
* **Natural Numbers ($\mathbb{N}$):** $\mathbb{N} = \{0, 1, 2, 3, ...\}$
* **Integers ($\mathbb{Z}$):** $\mathbb{Z} = \{..., -2, -1, 0, 1, 2, ...\}$

**Definition of Divisibility**
Let $a, b \in \mathbb{Z}$, with $b \neq 0$. We say that **$b$ divides $a$** (written as $b | a$) if there exists an integer $c \in \mathbb{Z}$ such that $a = bc$.

> **Example:** $2 | 4$ because $4 = 2 \cdot 2$.

### 1.3 Properties and Special Cases
Let $a, b,$ and $c$ be integers:
* **Property 1 (Transitive):** If $a | b$ and $b | c$, then $\mathbf{a | c}$.
* **Property 2 (Linearity):** If $a | b$ and $a | c$, then $\mathbf{a | (b + c)}$.
* **Property 3 (Multiplication):** If $a | b$, then $\mathbf{a | bc}$ for any integer $c$.

* An **even number** is divisible by 2.
* An **odd number** is not divisible by 2.

### 1.4 Concluding Transition
These rules lead to Euclidean division, which guarantees a unique quotient and remainder.

---

## 2.0 The Euclidean Division Algorithm

### 2.1 Introduction to Euclidean Division
It guarantees the existence of a unique quotient and a unique remainder, essential for algorithms like the Greatest Common Divisor (GCD).

### 2.2 The Euclidean Division Proposition
Let $a$ and $b$ be natural numbers with $b > 0$. There exist **unique** integers $q$ (quotient) and $r$ (remainder) such that:
$$a = bq + r \quad \text{with} \quad 0 \leq r < b$$

* **Link to Divisibility:** $b$ divides $a$ if and only if $r = 0$.

### 2.3 Euclidean Division in Practice
The formulas for $q$ and $r$ (using the floor function $\lfloor x \rfloor$):
$$q = \lfloor a/b \rfloor$$
$$r = a - b \cdot q$$

| Example: $a = 15476$, $b = 137$ | Result |
| :--- | :--- |
| Quotient $q$ | $q = \lfloor 112.96 \rfloor = \mathbf{112}$ |
| Remainder $r$ | $r = 15476 - 137 \cdot 112 = \mathbf{132}$ |
| Equation | $15476 = 137 \cdot 112 + 132$ |

### 2.4 Application Case Study: Secure Voting
Using the division $S = q(N+1) + r$ where $S$ is the final sum and $N$ is the number of voters:
* The **quotient, $q$**, is the number of **YES** votes.
* The **remainder, $r$**, is the number of **NO** votes.
* The **Abstentions** are $N - q - r$.

### 2.5 Concluding Transition
The principle of repeated division is key to number systems, notably binary.

---

## 3.0 Number Systems and Binary Representation

### 3.1 Introduction to Binary
Every integer can be uniquely expressed as a sum of powers of 2, using only the bits $0$ and $1$.

### 3.2 Formal Definition and Conversion Process
If $m = (m_{B-1}...m_{1}m_{0})_{2}$, then $m = m_{0} + m_{1}\times2 + ... + m_{B-1}2^{B-1}$.
The conversion process relies on **repeated Euclidean division by 2**. The sequence of remainders forms the bits, starting from the least significant bit ($m_0$).

| Example: Convert 112 to binary | Quotient | Remainder (Bit) |
| :--- | :--- | :--- |
| $112 = 2 \cdot 56 + 0$ | 56 | $m_0=0$ |
| ... | ... | ... |
| $1 = 2 \cdot 0 + 1$ | 0 | $m_6=1$ |
| **Result:** $112 = (1110000)_2$ (read bottom to top) | | |

### 3.3 Analyzing the Number of Bits
The number of bits $B$ required to represent $m$ is given by:
$$B = \lfloor \log_{2}(m) \rfloor + 1$$

> **Example:** To represent 368,932 ($\log_{2}(368932) \approx 18.4...$):
> $B = \lfloor 18.4... \rfloor + 1 = \mathbf{19}$ bits.

### 3.4 Concluding Transition
This systematic division process powers the Euclidean algorithm for the Greatest Common Divisor.

---

## 4.0 The Greatest Common Divisor (GCD) and the Euclidean Algorithm

### 4.1 Introduction to the GCD
The **Greatest Common Divisor (GCD)** of two integers is the largest integer that divides both without remainder.

### 4.2 Defining the GCD
Let $a$ and $b$ be integers, not both zero. The largest element in the set of their common divisors is $d$, the GCD. We write $d = \text{gcd}(a, b)$.

> **Example:** $\text{Divisors}(12) = \{1, 2, 3, 4, 6, 12\}$. $\text{Divisors}(18) = \{1, 2, 3, 6, 9, 18\}$. $\text{gcd}(18, 12) = \mathbf{6}$.

### 4.3 The Euclidean Algorithm for Computing GCD
It is a highly efficient method based on repeated Euclidean division.
**Steps:**
1.  Initialize $r_0 := a$ and $r_1 := b$.
2.  Divide $r_{i-1}$ by $r_i$: $r_{i-1} = r_{i}q_{i} + r_{i+1}$.
3.  If $r_{i+1} = 0$, the last non-zero remainder, $r_{i}$, is the GCD.

| Example: $\text{gcd}(259, 119)$ | Equation | Remainder |
| :--- | :--- | :--- |
| Step 1 | $259 = 119 \cdot 2 + 21$ | 21 |
| Step 2 | $119 = 21 \cdot 5 + 14$ | 14 |
| Step 3 | $21 = 14 \cdot 1 + 7$ | **7** |
| Step 4 | $14 = 7 \cdot 2 + 0$ | 0 |
| **Result:** $\text{gcd}(259, 119) = \mathbf{7}$ | | |

### 4.4 Concluding Transition
An extension of this algorithm reveals a deeper structural relationship between the numbers and their GCD.

---

## 5.0 The Extended Euclidean Algorithm

### 5.1 Introduction to Linear Combinations
The Extended Euclidean Algorithm expresses the GCD as a special **integer linear combination** of the original numbers. This result is known as **Bézout's Identity**.

### 5.2 Bézout's Identity
If $d = \text{gcd}(a, b)$, then there exist integers $u, v \in \mathbb{Z}$ satisfying:
$$d = au + bv$$
The integers $u$ and $v$ are found by **back-substitution** using the steps of the Euclidean algorithm.

> **Example: $\text{gcd}(259, 119) = 7$**
> 1.  Isolate 7: $7 = 21 - 1 \cdot 14$
> 2.  Substitute 14: $7 = 21 - (119 - 5 \cdot 21) = 6 \cdot 21 - 119$
> 3.  Substitute 21: $7 = 6 \cdot (259 - 2 \cdot 119) - 119 = \mathbf{6(259) - 13(119)}$
> Result: $u = 6$ and $v = -13$.

### 5.3 Worked Exercises
* **Exercise 1: $\text{gcd}(14, 100) = 2$**
    Combination: $2 = (-7) \cdot 14 + (1) \cdot 100$.
* **Exercise 2: $\text{gcd}(182, 630) = 14$**
    Combination: $14 = \mathbf{(7) \cdot 182 + (-2) \cdot 630}$.

### 5.4 Non-Uniqueness of Solutions
The solutions $(u, v)$ for $d = au + bv$ are not unique. If $(u, v)$ is one solution, the pair $\mathbf{(u + kb, v - ka)}$ is also a valid solution for any integer $k$.

### 5.5 Concluding Transition
The special case where $\text{gcd}(a, b) = 1$ defines **coprime integers**, which is paramount in cryptography.

---

## 6.0 Coprime Integers

### 6.1 Introduction to Coprimality
Two integers are **coprime** (or relatively prime) if they share no common divisors other than 1. This property is critical for public-key cryptosystems like **RSA**.

### 6.2 Definition and Characterization
* **Definition:** Two integers $a$ and $b$ are coprime if $\mathbf{\text{gcd}(a, b) = 1}$.
* **Characterization (Bézout):** $a$ and $b$ are relatively prime if and only if there exist integers $u, v$ such that $\mathbf{au + bv = 1}$.

### 6.3 Key Corollaries and Properties
* **Corollary (Euclid's Lemma):** If $p$ is a prime and $p | ab$, then $p | a$ or $p | b$.
* **Proposition for Coprime Numbers:** Let $a$ and $b$ be coprime. If $a | bc$, then $\mathbf{a | c}$.
* **Equation Solutions:** If $a$ and $b$ are relatively prime, the equation $au + bv = c$ has integer solutions for any integer $c$.

### 6.4 Concluding Transition
These properties lead to solving Linear Diophantine Equations.

---

## 7.0 Solving the Linear Diophantine Equation $au + bv = c$

### 7.1 Introduction to Diophantine Equations
These are equations of the form $au + bv = c$ for which only **integer solutions** $(u, v)$ are sought.

### 7.2 The General Case: Condition for Solvability
**Proposition:** The equation $au + bv = c$ has integer solutions $u, v \in \mathbb{Z}$ if and only if $\mathbf{\text{gcd}(a, b) | c}$.

**Strategy:**
1.  Calculate $d = \text{gcd}(a, b)$.
2.  Check if $d | c$. If not, no integer solutions exist.
3.  If yes, the problem can be simplified by dividing by $d$: $(a/d)u + (b/d)v = (c/d)$.

### 7.3 Finding All Solutions
Let $(u_0, v_0)$ be a particular solution, and let $d = \text{gcd}(a, b)$. All integer solutions are of the form:
$$u = u_0 + k\left(\frac{b}{d}\right)$$
$$v = v_0 - k\left(\frac{a}{d}\right) \quad \text{for any integer } k \in \mathbb{Z}$$

### 7.4 Application Case Studies
* **The Postage Stamp Problem (3 cents and 5 cents):** $\text{gcd}(3, 5) = 1$. The largest non-feasible value (Frobenius number) is $3 \cdot 5 - 3 - 5 = \mathbf{7}$.
* **The Shipping Container Problem (11 and 17 units):** $11u + 17v = 102,880$.
    * General Solution: $u = -308,640 + 17k$, $v = 205,760 - 11k$.
    * Non-negative constraints $u, v \geq 0$ limit $k$: $\mathbf{18156 \leq k \leq 18705}$.

### 7.5 Concluding Transition
Our final topic shifts focus to **prime numbers**, the fundamental building blocks of all integers.

---

## 8.0 An Introduction to Prime Numbers

### 8.1 Introduction to Primes
Prime numbers are the fundamental "**atoms**" of the integers. They are indispensable for securing modern digital communication.

### 8.2 Definition and Properties
* **Definition:** A natural number $p \geq 2$ is **prime** if its only positive divisors are 1 and $p$.
* **Euclid's Theorem:** There are **infinitely many** prime numbers.
    * The proof by contradiction involves constructing $M = (p_1 \cdot p_2 \cdot ... \cdot p_N) + 1$.

### 8.3 Primality and Divisibility
**Proposition (Primality Test):** If $n$ is composite, it must have a divisor $a$ such that $\mathbf{1 < a \leq \sqrt{n}}$.
> **Example:** To test 991 ($\sqrt{991} \approx 31.48$), we only check primes $\leq 31$.

**Proposition:** Let $p$ be a prime and $m \in \mathbb{Z}$. If $p \nmid m$, then $\mathbf{\text{gcd}(p, m) = 1}$.

### 8.4 The Fundamental Theorem of Arithmetic
Every integer greater than 1 can be represented as a product of prime numbers in a **unique** way, apart from the order of the factors.