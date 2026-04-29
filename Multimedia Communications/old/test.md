# Lossless Coding Principles

> **Course:** Multimedia Communications — Prof. Marco Cagnazzo
> **Reference slides:** L03 — Lossless coding principles (74 slides, 11.03.26)

---

# 1. Introduction

**Lossless coding** (also called *lossless compression* or *entropy coding*) is the process of representing a source signal with the minimum possible number of bits, while guaranteeing that the original can be **perfectly reconstructed**. Unlike lossy compression — which trades distortion for a lower rate — lossless coding is bounded below by what information theory allows. You cannot compress past entropy without losing something.

The general pipeline in multimedia compression is:

$$\text{Source} \xrightarrow{\text{Quantization}} \hat{X} \xrightarrow{\text{Entropy Coding}} \text{Bitstream}$$

Lossless coding operates on the *quantized* symbols $\hat{X}$, which already carry the distortion introduced by quantization. The job is to map these symbols to binary codewords as compactly as possible.

> [!info] Fundamental goal
> Given a discrete source $X$ with alphabet $\mathcal{X}$ and probability distribution $p(x)$, find a binary code that minimises the **average codeword length** $\mathcal{L}$, subject to unique decodability.

---

# 2. Principles of Information Theory

## 2.1 Self-information and entropy

The **self-information** (or *surprisal*) of an event $x$ is:

$$i(x) = \log_2 \frac{1}{p(x)} = -\log_2 p(x) \quad [\text{bits}]$$

Rare events carry high information; certain events carry none.

The **Shannon entropy** $H(X)$ is the expected self-information over the whole distribution:

$$\boxed{H(X) = \mathbb{E}[i(x)] = \sum_{x \in \mathcal{X}} p(x) \log_2 \frac{1}{p(x)}} \quad [\text{bits/symbol}]$$

Some properties worth knowing:
- $H(X) \geq 0$, with equality iff $p(x_i) = 1$ for some $i$ (no uncertainty at all)
- $H(X) \leq \log_2 |\mathcal{X}|$, with equality iff $p$ is uniform (maximum uncertainty)
- $H(X)$ is concave in $p$

![[Image Placeholder: Entropy H(X) as a function of p for a binary source — bell-shaped curve peaking at p=0.5]]

## 2.2 Joint entropy, conditional entropy, mutual information

For two random variables $X, Y$:

| Quantity | Definition | Interpretation |
|---|---|---|
| **Joint entropy** | $H(X,Y) = -\sum_{x,y} p(x,y)\log_2 p(x,y)$ | Uncertainty of the pair |
| **Conditional entropy** | $H(X\|Y) = \sum_y p(y) H(X\|Y=y)$ | Residual uncertainty in $X$ given $Y$ |
| **Mutual information** | $I(X;Y) = H(X) - H(X\|Y)$ | How much $Y$ tells us about $X$ |

**Chain rule:** $H(X,Y) = H(Y) + H(X|Y) = H(X) + H(Y|X)$

**Independence bound:** $H(X,Y) \leq H(X) + H(Y)$, with equality iff $X \perp Y$.

This bound is what makes **block coding** worthwhile. Encoding $K$ symbols jointly can never increase per-symbol entropy, and strictly decreases it when there are dependencies:

$$H(X_1 X_2 \ldots X_K) \leq \sum_{i=1}^{K} H(X_i)$$

## 2.3 The Asymptotic Equipartition Property (AEP)

For a stationary ergodic source, almost all long sequences of length $n$ have probability close to $2^{-nH(X)}$. These form the **typical set** $\mathcal{A}_\epsilon^{(n)}$:

- $|\mathcal{A}_\epsilon^{(n)}| \approx 2^{nH(X)}$ — far fewer than the $|\mathcal{X}|^n$ possible sequences
- The typical set has probability approaching 1 as $n \to \infty$

This is the argument behind why compression works at all: we only need short codewords for the $\approx 2^{nH(X)}$ likely sequences, not for every possible one.

## 2.4 Prefix-free codes and the Kraft inequality

A code is **uniquely decodable** if every sequence of codewords maps to exactly one sequence of source symbols. A stronger condition is the **prefix-free** (or *instantaneous*) property: no codeword is a prefix of another, so decoding can happen symbol-by-symbol without lookahead.

> [!info] Kraft inequality
> A binary prefix-free code with codeword lengths $\ell_1, \ell_2, \ldots, \ell_N$ exists *if and only if*:
> $$\sum_{i=1}^{N} 2^{-\ell_i} \leq 1$$

The code corresponds to a **binary tree**: each codeword is a leaf, and the lengths determine the depth of that leaf.

## 2.5 Shannon's source coding theorem

> [!info] Noiseless Source Coding Theorem (Shannon 1948)
> For any uniquely decodable code of a source $X$ with entropy $H(X)$:
> $$H(X) \leq \mathcal{L} < H(X) + 1$$
> where $\mathcal{L} = \sum_i p(x_i) \ell_i$ is the **average code length** in bits/symbol.
>
> $H(X)$ is the hard lower bound — no lossless code can beat it.

The lower bound is achievable in the limit. The upper bound ($H(X)+1$) is what Huffman coding reaches. The up-to-1-bit gap is the **non-dyadic penalty**: it appears when symbol probabilities are not exact powers of 2.

---

# 3. Optimal Coding: Huffman

## 3.1 The Huffman algorithm

**Huffman coding** is a provably optimal prefix-free code for a given probability distribution. More probable symbols get shorter codewords.

**Algorithm (bottom-up tree construction):**
1. Create a leaf node for each symbol, with probability $p(x_i)$
2. While more than one node exists:
   a. Select the two nodes with the lowest probabilities
   b. Merge them into an internal node whose probability is their sum
   c. Assign bit `0` to one branch and `1` to the other
3. Read the codewords by traversing the path from root to each leaf

[[Example: Huffman tree construction for 6-symbol alphabet {A,B,C,D,E,F} at page 37 of this document]]

![[Image Placeholder: Step-by-step Huffman tree construction — merging E(5%) and F(5%) first, then combining with D(15%), etc.]]

**Result for {A=0.4, B=0.2, C=0.15, D=0.15, E=0.05, F=0.05}:**

| Symbol | Probability | Codeword | Length |
|--------|------------|----------|--------|
| A | 0.40 | `0` | 1 |
| B | 0.20 | `100` | 3 |
| C | 0.15 | `101` | 3 |
| D | 0.15 | `110` | 3 |
| E | 0.05 | `1110` | 4 |
| F | 0.05 | `1111` | 4 |

$$\mathcal{L} = 0.4 \cdot 1 + 0.2 \cdot 3 + 0.15 \cdot 3 + 0.15 \cdot 3 + 0.05 \cdot 4 + 0.05 \cdot 4 = \mathbf{2.3 \text{ bits/symbol}}$$
$$H(X) = 0.4\log_2\frac{1}{0.4} + 0.2\log_2\frac{1}{0.2} + 2 \cdot 0.15\log_2\frac{1}{0.15} + 2 \cdot 0.05\log_2\frac{1}{0.05} \approx \mathbf{2.2464 \text{ bits/symbol}}$$

The gap $\mathcal{L} - H(X) \approx 0.054$ bits/symbol — less than 2.4% above entropy.

## 3.2 Performance bounds

Shannon's theorem pins down the Huffman code rate:

$$H(X) \leq \mathcal{L}^* < H(X) + 1$$

where $\mathcal{L}^*$ is the Huffman average code length. No other prefix-free, symbol-by-symbol code can do better.

**Application to French text compression:**

| Metric | Value |
|--------|-------|
| Source entropy | 3.999 bpS |
| Huffman coding rate $\mathcal{L}$ | 4.041 bpS |
| Compression ratio | 1.238 |

![[Image Placeholder: Bar chart of letter probabilities in French vs. Huffman codeword lengths — more probable letters get shorter codes]]

[[Example: Compression of French text with Huffman coding at page 40 of this document]]

## 3.3 Limits: the 1-bit penalty for skewed sources

Huffman must assign *integer-length* codewords. For heavily skewed distributions, this is a real problem.

**Binary image example** (B&W scanned document):
- $\Pr(X = \text{Black}) = p \ll 1$, $\Pr(X = \text{White}) = 1-p$
- $H(X) \ll 1$ bit/symbol
- Huffman code: $B \to 0$, $W \to 1$ → $\mathcal{L} = 1$ bpp

With $p = 13.3\%$ (white = 86.7%): $H(X) = 0.586$ bits/pixel, yet Huffman requires **1 bpp**. That is nearly 70% overhead — the worst-case non-dyadic penalty in full effect.

![[Image Placeholder: B&W image of letter T showing mostly white pixels (86.7%) and black pixels (13.3%)]]

> [!question] Can we do better than Huffman on skewed sources?
> Yes — through **block coding** or **arithmetic coding**, both of which decouple the integer-length constraint from individual symbols.

## 3.4 Block coding and the entropic rate

**Block Huffman coding** encodes groups of $K$ symbols $X^K = (X_1, X_2, \ldots, X_K)$ as a single super-symbol. The per-symbol rate becomes:

$$\mathcal{L}_S = \mathcal{L}/K \quad \Rightarrow \quad \mathcal{L}_S < \frac{H(X^K)}{K} + \frac{1}{K}$$

As $K \to \infty$, the $\frac{1}{K}$ penalty vanishes:

$$\lim_{K \to \infty} \mathcal{L}_S^* = \lim_{K \to \infty} \frac{H(X^K)}{K} = \mathcal{H}(X)$$

where $\mathcal{H}(X)$ is the **entropic rate** of the source. For i.i.d. sources, $\mathcal{H}(X) = H(X)$. For stationary sources with memory, $\mathcal{H}(X) \leq H(X)$, so block coding also exploits statistical dependencies.

**B&W image with block coding:**

| Block size $K$ | $H(X^K)$ | $H(X^K)/K$ | Code rate |
|---|---|---|---|
| 1 | 0.586 bpB | 0.586 bpp | 1.000 bpp |
| 2 | 1.022 bpB | 0.511 bpp | **0.650 bpp** |
| 4 | 1.533 bpB | 0.383 bpp | **0.433 bpp** |

[[Example: Block Huffman coding of B&W image pixels (K=1,2,4) at pages 42–47 of this document]]

**French text block entropy** (inter-letter dependencies lower per-symbol entropy substantially):

| $K$ | Joint Entropy | Per-symbol entropy |
|---|---|---|
| 1 (letters) | 3.999 bpB | 3.999 bpS |
| 2 (digrams) | 7.440 bpB | 3.720 bpS |
| 3 (trigrams) | 9.452 bpB | 3.151 bpS |

[[Example: Block entropy analysis of French text at page 50 of this document]]

## 3.5 Practical limits of block Huffman

Block Huffman is sound in theory but falls apart for large $K$:
- Alphabet size grows as $N^K$ — complexity is **exponential in $K$**
- Joint probability estimation for large blocks is unreliable and data-hungry

**Arithmetic coding** solves the first problem at linear complexity, while reaching the same asymptotic optimality.

---

# 4. Arithmetic Coding

## 4.1 Principle: interval refinement

**Arithmetic coding** encodes an entire message of $n$ symbols as a *single real number* in $[0, 1)$. Each sequence of symbols uniquely maps to a sub-interval of $[0,1)$, with width equal to the sequence's probability.

**Algorithm:**
1. Initialize interval $[low, high) = [0, 1)$
2. For each new symbol $x_i$:
   - Partition the current interval proportionally to symbol probabilities
   - Narrow it to the sub-interval for $x_i$:
     $$low' = low + (high - low) \cdot F(x_i - 1)$$
     $$high' = low + (high - low) \cdot F(x_i)$$
   where $F(x_i)$ is the cumulative distribution function
3. Output any number in the final interval, with sufficient precision

[[Example: Arithmetic coding of sequence ACFD with alphabet {A=0.4, B=0.2, C=0.15, D=0.15, E=0.05, F=0.05} at pages 53–54 of this document]]

![[Image Placeholder: Nested interval refinement diagram for ACFD — each symbol narrows the active interval by the symbol's probability fraction]]

Each symbol needs only two multiplications and two additions to update the interval — $O(n)$ complexity, regardless of block size.

## 4.2 Encoding precision and performance

The output codeword is a number in the final interval, with enough bits to uniquely identify it. The required length for symbol $x_i$ is:

$$\ell_i = \lceil \log_2 p_i \rceil + 1$$

giving per-symbol bounds of:

$$\log_2 p_i + 1 \leq \ell_i < \log_2 p_i + 2$$

At the sequence level:

$$\boxed{H(X) + 1 \leq \mathcal{L}_{AC} < H(X) + 2 \leq \mathcal{L}^* + 2}$$

For a block of $K$ symbols, the per-symbol rate satisfies:

$$\mathcal{L}_S = \mathcal{L}/K \quad \xrightarrow{K \to \infty} \quad \mathcal{H}(X)$$

Arithmetic coding achieves **asymptotic optimality** without the exponential-complexity cost of block Huffman.

## 4.3 Context-based coding

Estimating $P(X^K)$ for large $K$ is impractical. In practice, a symbol usually depends on only a few **neighboring symbols** — its *context*.

> [!info] Context definition
> A **context** is a set of $N_S$ previous symbols that most influence the current one. The number of distinct contexts is at most $N_C = M^{N_S}$, where $M$ is the alphabet size.

Using $N_C$ contexts is equivalent to running $N_C$ independent arithmetic encoders and switching between them. High-order statistical dependencies get modeled without estimating the full joint distribution; for predictable sources, per-context entropy collapses toward zero.

**B&W image with 1-pixel context (left neighbor):**

| Context | $H(X|\text{ctx})$ | $P(\text{ctx})$ |
|---|---|---|
| Previous = White | 0.322 bits | 94.1% |
| Previous = Black | 0.918 bits | 5.9% |

$$H(X|Y) = 0.322 \cdot P(\square) + 0.918 \cdot P(\blacksquare) = \mathbf{0.406 \text{ bpp}}$$

Block-2 Huffman got 0.511 bpp; one context pixel brings it to 0.406 bpp.

## 4.4 Adaptivity

Probability estimates can be updated during encoding as each new symbol arrives, rather than pre-computed from a training set. No probability model is needed upfront (*universal coding*), and non-stationary sources are handled naturally. The main practical difficulty is that robust estimation per context still requires enough data — a small context with little data is noisy.

**Summary of arithmetic coding:**

| Aspect | Advantage |
|---|---|
| Complexity | Linear ($O(n)$, two mults + two sums per symbol) |
| Block coding | Exploits high-order dependencies, removes 1-bit penalty |
| Context-based | Simple model for high-order statistics |
| Adaptivity | Handles non-stationary sources |

| Aspect | Disadvantage/Difficulty |
|---|---|
| Implementation | Can be tricky (finite-precision arithmetic) |
| Initialization | Requires probability model or training data |
| Context selection | Choosing the right context size is non-trivial |

---

# 5. Other Coding Techniques

## 5.1 Exponential-Golomb coding

**Exponential-Golomb (Exp-Golomb) coding** is a **universal code** for integers — no initialization or probability model needed, and any integer can be encoded. Smaller integers get shorter codewords.

### Unsigned integers

To encode $n \geq 0$:
1. $n = 0$ maps to codeword `1`
2. For $n \geq 1$: write $n+1$ in binary using $b = \lfloor \log_2(n+1) \rfloor + 1$ bits
3. Prepend $b-1$ zeros

| $n$ | $n+1$ on $b$ bits | Leading zeros | $c_U(n)$ |
|---|---|---|---|
| 0 | 1 | — | `1` |
| 1 | 10 | 0 | `010` |
| 2 | 11 | 0 | `011` |
| 3 | 100 | 00 | `00100` |
| 4 | 101 | 00 | `00101` |
| 7 | 1000 | 000 | `0001000` |

### Signed integers

Signed integers $n \in \mathbb{Z}$ are mapped to $m(n) \in \mathbb{N}$ via:
- $n > 0$: $m(n) = 2n - 1$
- $n \leq 0$: $m(n) = -2n$

Then $c_S(n) = c_U(m(n))$. This interleaves positive and negative values: $0 \to 0$, $1 \to 1$, $-1 \to 2$, $2 \to 3$, $-2 \to 4$, …

Exp-Golomb coding is used in **H.264/AVC** and **H.265/HEVC** for syntax elements and quantized transform coefficients.

## 5.2 Dictionary-based coding (LZW)

**Dictionary-based (LZW) coding** builds a dictionary of recurring sequences *during* encoding. No pre-training is needed.

**Encoding algorithm:**
1. Initialize the dictionary with all single symbols
2. Read input symbols while extending the current "present" string
3. When the present string + next symbol is **not** in the dictionary:
   - Output the dictionary index of the present string
   - Add the new string (present + next symbol) to the dictionary
   - Reset: present ← next symbol
4. Repeat until end of input

Decoding works the same way in reverse: reconstruct the dictionary from the transmitted indices.

[[Example: LZW encoding of binary sequence `0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 0 1 0 0 0 0 0 1 0` at pages 65–66 of this document]]

![[Image Placeholder: Step-by-step LZW dictionary growth — from {0, 1} to multi-symbol entries as encoding progresses]]

Properties:
- Universal: no initialization or probability model
- Adapts automatically to non-stationary signals
- Used in: **zip**, **gzip**, **bzip2**, GIF, TIFF

## 5.3 Run-Length Encoding (RLE)

**RLE** is designed for sources with long runs of identical symbols — binary images being the canonical case. Instead of coding each pixel, it codes the *length of each run*.

For B&W images, directly Huffman-coding the lengths would require a large alphabet, so each length is decomposed as a **sum of powers of two** (binary representation). Three scan modes:
- **Horizontal mode (HM)**: encodes absolute run length
- **Vertical mode (VM)**: encodes the difference from the run boundary in the row above (if $\leq 3$ pixels)
- **Pass (P)**: skips to the next reference pixel

[[Example: RLE encoding of a 2D B&W image showing horizontal and vertical modes at page 69 of this document]]

![[Image Placeholder: RLE example table showing HM/VM/Pass modes for a 4-row B&W image segment]]

RLE combined with Huffman coding is the basis of **Group 3/4 fax compression** (ITU-T T.4/T.6).

## 5.4 JBIG standards

### JBIG-1

**JBIG-1** (*Joint Bi-level Image Experts Group*, ISO/IEC 11544, ITU-T T.82) is the standard for lossless binary image compression.

- Context-based arithmetic coding with a 10-pixel causal template
- Progressive coding for resolution scalability (decode at coarser resolutions first)
- Two template shapes, each with a single variable pixel position
- A two-row template trades ~5% extra rate for faster encoding

![[Image Placeholder: JBIG-1 10-pixel template shapes — causal context window around the pixel to be coded]]

### JBIG-2

**JBIG-2** (ISO/IEC 14492, ITU-T T.88) handles mixed-content documents by segmenting them first:

| Segment type | Encoding method |
|---|---|
| **Text** | Symbol dictionary: common glyphs stored and referenced by index |
| **Halftone** | Dictionary of *halftone patterns* (gray-level dots) |
| **Other** | Context-based arithmetic coding (as in JBIG-1) |

JBIG-2 data is embedded directly in **PDF files** (version 1.4 and later).

---

# 6. Quantization and Entropy Coding

## 6.1 Joint design

In practice, **quantization (Q)** and **entropy coding (EC)** are not independent. When Q feeds into EC, the quantizer should be designed with that in mind. Three questions follow naturally:
1. Should we change the quantizer knowing EC comes after?
2. Can we estimate the performance of the full Q+EC chain?
3. Which quantizer minimises distortion for a given entropy budget?

## 6.2 Entropy-constrained quantization

A generic (non-uniform) quantizer can be modeled as a **uniform quantizer (UQ)** preceded by a non-linear function $f(x)$. The quantization error energy under the **high-resolution (HR) hypothesis** is:

$$\sigma_Q^2 = \frac{\delta}{12} \int \frac{p_X(x)}{f'^2(x)} dx$$

subject to the entropy constraint $H(\hat{X}) \leq b$ bits/symbol.

Solving via calculus of variations, the optimum requires $f'$ to be **constant** — so the optimal compander is linear, making the **uniform quantizer optimal** under an entropy constraint.

## 6.3 Key results (high-resolution regime)

| Result | Statement |
|---|---|
| Min-entropy | For a given MSE, minimum quantizer entropy is achieved with UQ |
| Min-distortion | For a given entropy budget, minimum MSE is achieved with UQ |
| Gain over Lloyd-Max | UQ+EC gains **2.81 dB** over Lloyd-Max quantizer (no EC) for Gaussian i.i.d. source |
| Rate-distortion behavior | $D \propto 2^{-2R}$ (same slope as the R-D bound) |

> [!info] Implication for codec design
> The conventional wisdom "use Lloyd-Max for optimal quantization" is *wrong* when entropy coding follows. A simple uniform quantizer, combined with entropy coding, strictly outperforms the Lloyd-Max quantizer used without EC. The gain is 2.81 dB for Gaussian sources.

The R-D curve $D \propto 2^{-2R}$ means each extra bit of rate cuts distortion by a factor of 4 (6 dB). Every practical Q+EC system approaches this curve from above.

---

# 7. Summary and comparison

| Technique | Complexity | Adaptivity | Near-optimal? | Use case |
|---|---|---|---|---|
| **Huffman** | $O(N \log N)$ | No (needs prob.) | Yes (symbol-by-symbol) | Fast encoding, known distribution |
| **Block Huffman** | Exponential in $K$ | No | Yes (as $K \to \infty$) | Small alphabets only |
| **Arithmetic** | $O(n)$ linear | Yes | Yes (asymptotically) | High-performance codecs (JPEG2000, HEVC) |
| **Exp-Golomb** | $O(\log n)$ | Yes (universal) | No (sub-optimal) | Video syntax elements (H.264, H.265) |
| **LZW (dictionary)** | $O(n)$ | Yes (universal) | No (sub-optimal) | General-purpose (gzip, zip) |
| **RLE** | $O(n)$ | No | No | Binary images with long runs (fax) |

> [!info] Convergence hierarchy
> $$\underbrace{\mathcal{H}(X)}_{\text{entropic rate}} \leq \underbrace{H(X)}_{\text{i.i.d. entropy}} \leq \underbrace{\mathcal{L}_{\text{Huffman}}}_{\text{symbol-by-symbol}} < H(X) + 1$$
> Block coding and arithmetic coding both converge to $\mathcal{H}(X)$ as block size or sequence length grows.
