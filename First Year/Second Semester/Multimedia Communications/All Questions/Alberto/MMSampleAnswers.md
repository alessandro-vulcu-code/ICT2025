<!-- Pagina 1 -->

Principles of image compression. Discuss the criteria for evaluating a compression algorithm: rate, quality, [Bonus: robustness, delay, complexity].

Modulations: reduce media size, we exploit spatial temporal and psychovisual redundancies.

2 types of expression:
- Lossless → 1:1 representation, perfect reconstruction
- Lossy → decoded to signal we love so much
- Visually complex → Higher compression ratio

Evaluation Rate →
$R = \frac{B_{our}}{N_M}$
$R = \frac{B_{our}}{T}$
Video Audio [bps]

Correlation Ratio $T = \frac{R_{inv}}{B_{our}}$
$D(f_i) = \frac{1}{N_M} N g(f_i f_j)^2$
$D(w(f_i f_j)) = \frac{1}{N_M} N w * g(f_i f_j)^2$

A zero-mean Gaussian random signal has an autocorrelation function:

$$r_X(n - m) = E[X(n)X(m)] = \sigma^2\rho^{|n - m|}$$

1. Consider the predictor $V(n) = X(n - 1)$. For which values of $n$ the prediction gain is positive?
2. Optimal linear predictor is $V(n) = -\sum_{i=1}^{P} a_i x_{n-i}$, with $a = -R_X^1 r, R_X(i,j) = r_X(i-j), r = [r_X(1) \cdots r_X(P)]^T$.
   Find optimal linear predictor of order $P = 1$ and compute prediction gain, compare then with previous case.

3. Compute the optimal predictor of order 2. Compare with the previous cases

$$G_p = \frac{\sigma_x^2}{\sigma_y^2}$$
$$Y(n) = X(n) - V(n)$$
$$\frac{1}{2} X(n) - X(n-1)$$
$$G_p = \log \frac{\sigma^2}{\sigma_e^2}$$
$$r_y = \sum_{i=1}^{P} [X(n)(X(n-1))] \sigma^2 \rho^{|n - m|}$$
$$\frac{1}{2} \sigma_e^2$$
$G_p \geq dB$
1
1. Consider the predictor $V(n) = X(n - 1)$. For which values of $n$ the prediction gain is positive?
2. Optimal linear predictor is $V(n) = -\sum_{i=1}^{P} a_i x_{n-i}$, with $a = -R_X^1 r, R_X(i,j) = r_X(i-j), r = [r_X(1) \cdots r_X(P)]^T$.
   Find optimal linear predictor of order $P = 1$ and compute prediction gain, compare then with previous case.

3. Compute the optimal predictor of order 2. Compare with the previous cases

---

<!-- Pagina 2 -->

Draw and comment on the schemes of predictive quantization (encoder and decoder)

Discuss the principles of lossless coding

• Based on Data statistical Properties
  VLC - short cw for possible symbols, long cw for not-possible symbols
  LLC → Some length for each cw
  Definitions:
    • Alphabet $X = \{ X_1, \dots, X_m \}$ symbols to encode
    • Code : $X \rightarrow [0,1]^*$ → set of finite-length bitstrings

ZTEOs:
  McMillan → Best Prefix code $\Longleftrightarrow$ Best possible decodible code
  Kraft → $\sum_{i=1}^{n} 2^{-li}$ $\ll 1 \Longleftrightarrow$ Most efficient code with lengths $\{l_1, \dots, l_m\}$
  Optimal code $\sum_{i=1}^{n} 2^{-ci} = 1$
  Kraft's proof on Greedy construct $^2$ Algorithm
$$\begin{array}{c}
x(n) \\
\Sigma \\
y(n) \\
Q \\
\hat{y}(n) \\
Euc/Dec \\
\Sigma \\
x(n) \\
V(n) \\
P \\
\hat{x}(n) \\
P \\
\end{array}$$

We use the postitive Data as a feedback
Note: linear is affine $\Rightarrow$ Error Propagation!
McMillan → Best Prefix code $\Longleftrightarrow$ Best possible decodible code
Kraft → $\sum_{i=1}^{n} 2^{-li}$ $\ll 1 \Longleftrightarrow$ Most efficient code with lengths $\{l_1, \dots, l_m\}$
Optimal code $\sum_{i=1}^{n} 2^{-ci} = 1$
Kraft's proof on Greedy construct $^2$ Algorithm

---

<!-- Pagina 3 -->

Consider a source that emits the symbols A, B, C, D, E, and F. The probabilities of these symbols are given in the following table:

$$p_A = 0.3, p_B = 0.1, p_C = 0.05, p_D = 0.18, p_E = 0.15, p_F = 0.22$$

- Describe the Huffman Algorithm
- Compute Huffman code for this distribution
- Compare the average length of the Huffman code with the distribution entropy

Algorithm: South Hand by Prost, table 2. Least paddle nodes merge, iterate until splee nodes.

$$\begin{array}{ccccccc}
A & 0.3 & A & AF & D & 0.7 & A \\
F & 0.22 & F & D & 0.4 & C & 0.18 \\
D & 0.18 & D & B & C & E & 0.15 \\
E & 0.15 & E & B & C & E & 0.3 \\
B & 0.1 & B & C & E & F & 0.05
\end{array}$$

$$\begin{array}{ccccccc}
A & B & C & D & F \\
0.6 + 0.3 + 0.15 + 0.3 + 0.54 + 0.66 = 2.55 g/L \\
H = \sum p_i g_i = 2.40 g/L
\end{array}$$

Why arithmetic encoder is preferred over Huffman for high-performance lossless coding?

It allows to perform block coding with linear complexity.

Arithmetic coding is suboptimal, but asymptotically optimal.

You encode one symbol using one number.

Average length $Y < H(x) + \frac{2}{n} \rightarrow H(x)$ (instead of $Y < H(x) + 1$)

Arithmetic coding is also good for context-based coding.
3
3

---

<!-- Pagina 4 -->

Motion estimation: give the principles of the block matching approach. Give at least one cost function. [Bonus]. Discuss the regularization issue

Block Matchy: • Split Images into Blocks $B_{pq}$ with $(P, q) \in N \times M$
ISEA: estimate motion using staggered motions of small objects
Comparing style block亮度 $f_K(B_{pq})$ with a window $f_M(B_{pq}, 9-j)$

Criterion:
• SSD (sum of spined diffuse) $J_{\text{SSD}}(n_j, j) = \sum_{m \in M} [f(n_m, k) - f(n-m, m-j, h)]^2$
• SAD (sum of Absolute Diffuse) $J_{\text{SAD}}(n_j, j) = \sum_{m \in M} |f(n_m, k) - f(n-m, m-j, h)|$
• REG (Regular Norm-Based Criterion) $\rightarrow$ Solves problems of SSD/SAD
$\overline{J_{\text{REG}}}(n_j, j) = \|f_K(B_{pq}) - f_M(B_{pq}, 9-j)\|^2 + \lambda R(n_j, j)$

ISSUE: estimate of largeess Reyls (artifacts) $\Rightarrow$ Prediction factor

Discuss the advantages and the disadvantages of Intra, Predictive, and Bidirectional images in a GOP for video coding.

Coding Mode Selection

Intro: No temporal prediction
Transform-Based coding
Available for Mimeses (High Rate, Low Distortion)

I frames: low complexity, low rate
Random Access points
Independent frames

Inter: MS/MC-based temporal prediction
Transform coding
only available for non-latent frames (Lower Rate, Higher Distortion)

P frames:
• Polaroid cause latent coded or later coded
• Higher complexity
• High companion ratio for a given quality wrt. I frames
• Predictive for previous AF

B frames: Very high complexity, very high companion ratio, predicted from both previous AF
*block → Eve choose $f_{intra}$, forward pred., both pred., bidirectional prediction)
---
```markdown
Motion estimation: give the principles of the block matching approach. Give at least one cost function. [Bonus]. Discuss the regularization issue

Block Matchy: • Split Images into Blocks $B_{pq}$ with $(P, q) \in N \times M$
ISEA: estimate motion using staggered motions of small objects
Comparing style block亮度 $f_K(B_{pq})$ with a window $f_M(B_{pq}, 9-j)$

Criterion:
• SSD (sum of spined diffuse) $J_{\text{SSD}}(n_j, j) = \sum_{m \in M} [f(n_m, k) - f(n-m, m-j, h)]^2$
• SAD (sum of Absolute Diffuse) $J_{\text{SAD}}(n_j, j) = \sum_{m \in M} |f(n_m, k) - f(n-m, m-j, h)|$
• REG (Regular Norm-Based Criterion) $\rightarrow$ Solves problems of SSD/SAD
$\overline{J_{\text{REG}}}(n_j, j) = \|f_K(B_{pq}) - f_M(B_{pq}, 9-j)\|^2 + \lambda R(n_j, j)$

ISSUE: estimate of largeess Reyls (artifacts) $\Rightarrow$ Prediction factor

Discuss the advantages and the disadvantages of Intra, Predictive, and Bidirectional images in a GOP for video coding.
```
```
```
Motion estimation: give the principles of the block matching approach. Give at least one cost function. [Bonus]. Discuss the regularization issue

Block Matchy: • Split Images into Blocks $B_{pq}$ with $(P, q) \in N \times M$
ISEA: estimate motion using staggered motions of small objects
Comparing style block亮度 $f_K(B_{pq})$ with a window $f_M(B_{pq}, 9-j)$

Criterion:
• SSD (sum of spined diffuse) $J_{\text{SSD}}(n_j, j) = \sum_{m \in M} [f(n_m, k) - f(n-m, m-j, h)]^2$
• SAD (sum of Absolute Diffuse) $J_{\text{SAD}}(n_j, j) = \sum_{m \in M} |f(n_m, k) - f(n-m, m-j, h)|$
• REG (Regular Norm-Based Criterion) $\rightarrow$ Solves problems of SSD/SAD
$\overline{J_{\text{REG}}}(n_j, j) = \|f_K(B_{pq}) - f_M(B_{pq}, 9-j)\|^2 + \lambda R(n_j, j)$

ISSUE: estimate of largeess Reyls (artifacts) $\Rightarrow$ Prediction factor

Discuss the advantages and the disadvantages of Intra, Predictive, and Bidirectional images in a GOP for video coding.
```

---

<!-- Pagina 5 -->

Why the geometric mean of the variances of a random vector is key information to evaluate the rate-distortion performance of a quantizer?

Geometric Mean $\rightarrow$ becomes smaller as the values become different write others

To maximize the Carly-Gold $G_{TR} = \frac{\sigma^2}{g_{AM}, y}$
$\Rightarrow$ We need to find an outlier transform
$Y = \tau X$
that minimizes $\sigma^2_{AM}, y$

Distorting inputs or G.M.

$D^*OC \sigma^2_{GM}$

Write the resource allocation problem for transform coding. Derive the Huang-Schulteiss formula

Minimize $D$ under Rate constraint
$\min D(R) = \frac{1}{M} \sum_{k=0}^{M-1} C_k \sigma^2_k 2^{-2R_k}$
s.t. $\sum_{k=0}^{M-1} R_k \leq R_{OT}$

$\Rightarrow$ Logarithm method
$J(R^*, \lambda) = \frac{1}{M} \sum_{k=0}^{M-1} C_k \sigma^2_k 2^{-2R_k} + \lambda \left( \sum_{k=0}^{M-1} R_k - R_{OT} \right)$

setting $\frac{\partial J}{\partial R_k} = 0, \frac{\partial J}{\partial \lambda} = 0$

HS $\Rightarrow R_{K^*} = \frac{R_{OT}}{M} + \frac{1}{2} g_k \left[ \frac{C_k \sigma^2_k}{g_{AM}, y} \right]$
5
$$\begin{align*}
C_{GM} &= \frac{M}{\sum_{k=0}^{M-1} C_k} \\
\sigma^2_{GM} &= \frac{M}{\sum_{k=0}^{M-1} C_k}
\end{align*}$$

---

<!-- Pagina 6 -->

Describe the principles of the JPEG standard

JPEG → • Standard → Only decoder is regulated, cooperation for the ENC.
• Guarantees Interoperability

Encoding strategy
Block → abstract avg rate → DCF → Quantization Mid-Tread VQ → Fig. 209
Energety Calibration (Huffman)

Quality defined by a Sally factor
$$S_F = \begin{cases} 
5000/Q & Q \in [1, 50] \\
200-2Q & Q \in [50, 98] \\
1 & Q = 100 
\end{cases}$$

Methodator
• JFIF → rewards Interoperability
• Density units x/4 denting
• EXIF → Can include proprietary data
• Also add Comment Info
• GPS info
• Date/Time
• Camera Settings

Describe the intra-coding modes in H.264. [Optional] Discuss also the Intra modes in H.265

Inter-prediction: exploit spatial prediction array registers
H.264 → 9 predictive types for 4×4 subblocks → 16 available choices
4 for 16×16 subblocks → 4 available choices

H.265 → 35 modes (33 directions + DC + Planar)
Uses 3-candidate MPM List to predict the mode
6
```markdown
Describe the principles of the JPEG standard

JPEG → • Standard → Only decoder is regulated, cooperation for the ENC.
• Guarantees Interoperability

Encoding strategy
Block → abstract avg rate → DCF → Quantization Mid-Tread VQ → Fig. 209
Energety Calibration (Huffman)

Quality defined by a Sally factor
$$S_F = \begin{cases} 
5000/Q & Q \in [1, 50] \\
200-2Q & Q \in [50, 98] \\
1 & Q = 100 
\end{cases}$$

Methodator
• JFIF → rewards Interoperability
• Density units x/4 denting
• EXIF → Can include proprietary data
• Also add Comment Info
• GPS info
• Date/Time
• Camera Settings

Describe the intra-coding modes in H.264. [Optional] Discuss also the Intra modes in H.265

Inter-prediction: exploit spatial prediction array registers
H.264 → 9 predictive types for 4×4 subblocks → 16 available choices
4 for 16×16 subblocks → 4 available choices

H.265 → 35 modes (33 directions + DC + Planar)
Uses 3-candidate MPM List to predict the mode
```

---

<!-- Pagina 7 -->

Describe the principle of the deblocking in-loop filter of H.264

Transform dequantization are applied to low-pass blocks
→ at low bitrates → 7 blocking intervals at black boundaries

Deblocking Filter in H.264:
• Analyzes edge between 4x4 blocks
• Filtering colorantly with code mode, mV, quantizer of self-loss
→ Basically we dequantize antiflect anchoring.

(A&S Comp.) Explain the difference between Source-Based (Parametric) coding and Sink-Based (Perceptual) coding

Source-Based: exploits physical constraints of sound generation
→ Intelligibility & Low Latency

Sink-Based: exploits physical characteristics of the human ear
→ Fidelity & Perceptual Transparency
7

---

<!-- Pagina 8 -->

(A&S Comp.) Describe the “Analysis-by-Synthesis” (AbS) loop used in CELP (Code Excited Linear Prediction) codecs and why it represents an improvement over simple LPC-10.

LPC-10 uses a simplified excitation model (impulse train or white noise) that often results in unnatural-sounding speech. CELP improves this by using a codebook-based excitation (not just periodic pulses and white noise), introduces a closed loop search, and uses perceptual quality. The AbS loop functions as a “mini-decoder” inside the encoder: for each potential excitation vector from the codebook, the encoder synthesizes the speech and compares it against the original input. It then selects the vector that minimizes the perceptually weighted error, ensuring the chosen excitation yields the highest quality reconstruction, which is significantly more flexible and robust than the static LPC-10 excitation.

(A&S Comp.) What is the role of the psychoacoustic masking model in perceptual audio coding, and how is it used to allocate bits?

Psychoacoustic Masking model
• Design objective → achieve “transparent quality” by rendering information based on the model

• Analysis steps:
  • Spectral Analysis
  • Identification of the windows
  • Find Masking curves (spreading functions)
  • Simulation of the Array
  → Used to remove bits we “canNOT” hear.

(A&S Comp.) Describe the principles of the LPC10 speech coding scheme

LPC-10 → Standard (F.S. 1015), CBR 2.4 Kbps (54 bits/22.5 ms frames)

Principle: Voiced sounds → max spectral detail & padded info.
Unvoiced → lower spectral detail, error protection bits to improve robustness

In detail → Bit Allocation:

| Voice | Unvoice |
| :--- | :--- |
| 41 (P=10) | 20 (P=4) |
| 7 | 0 |
| 5 | 5 |
| 1 | 1 |
| 0 | 28 |

Pot 545. 546.
---
---

---

<!-- Pagina 9 -->

(A&S Comp.) Draw the scheme and describe the operation of the functional blocks of an MP3 encoder

A&S Comp.) Why are Line Spectrum Frequencies (LSF) preferred over direct quantization of LPC coefficients ($a_i$)?

Perfect for Carly:
• We quantize the frequencies $w_i$
• If quant. error moves 2 frequencies to swap $\Rightarrow$ detected instability
• Decoder first restores strict interlocky $\Rightarrow$ 100% single filter

(A&S Comp.) Regarding the Opus audio codec, what is the primary technical advantage of its hybrid design?

Hybrid mode uses both SILK and CELT cogs:
• SILK $\rightarrow$ LPC-based, optimized for speech (8-12 kbps)
• CELT $\rightarrow$ MDCF-based, optimized for audio & music (high bitrate)

Key feature $\rightarrow$ Seamless Adaptation on the fly

(A&S Comp.) Which of the following best describes current research trends in the future of multimedia audio coding?

• NR video quality for streaming
• noise QoE prediction
• generation AI quality assessment
• Perceptual needs for AI-generated needs

For Carly $\Rightarrow$ Executive NL Transform with near zero overhead
$\Rightarrow$ Toward Reduction Carly → (A)
<table><tr><td>(A&S Comp.) Why are Line Spectrum Frequencies (LSF) preferred over direct quantization of LPC coefficients ($a_i$)?</td></tr><tr><td>Perfect for Carly:
• We quantize the frequencies $w_i$
• If quant. error moves 2 frequencies to swap $\Rightarrow$ detected instability
• Decoder first restores strict interlocky $\Rightarrow$ 100% single filter</td></tr><tr><td>(A&S Comp.) Regarding the Opus audio codec, what is the primary technical advantage of its hybrid design?</td></tr><tr><td>Hybrid mode uses both SILK and CELT cogs:
• SILK $\rightarrow$ LPC-based, optimized for speech (8-12 kbps)
• CELT $\rightarrow$ MDCF-based, optimized for audio & music (high bitrate)</td></tr><tr><td>Key feature $\rightarrow$ Seamless Adaptation on the fly</td></tr><tr><td>(A&S Comp.) Which of the following best describes current research trends in the future of multimedia audio coding?</td></tr><tr><td>NR video quality for streaming
noise QoE prediction
generation AI quality assessment
Perceptual needs for AI-generated needs</td></tr><tr><td>For Carly $\Rightarrow$ Executive NL Transform with near zero overhead
$\Rightarrow$ Toward Reduction Carly → (A)</td></tr></table>

---

<!-- Pagina 10 -->

(TC&JPEG) Explain the role of the Geometric Mean of variances in transform coding and how it relates to the coding gain.

In block coding with optimal resource allocation (e.g., using the Huang-Schulteiss formula), the resulting quantization distortion is proportional to the geometric mean of the variances of the transformed coefficients. The coding gain $G_T$ is defined as the ratio between the distortion of direct sample-by-sample quantization and the distortion achieved by transform coding. Since orthogonal transforms preserve the arithmetic mean of the variances (energy conservation) but alter their distribution, a transform that achieves high energy compaction, thereby minimizing the geometric mean of the variances, maximizes the coding gain.

(TC&JPEG) Describe the problem of “frequency leakage” in the Discrete Fourier Transform (DFT) when applied to signal compression and how the Discrete Cosine Transform (DCT) addresses it.

Frequency leakage: It occurs on sampling and periodizing the signal if there are big jumps in signal at period start/end with the DCT we put a “mirror” instead of periodizing. We reduce the big jumps.

(TC&JPEG) Explain the entropy coding process for AC coefficients in the JPEG standard and the significance of the “End of Block” (EOB) symbol.

AC coefficients represented by run-length category, amplitude encoded as in DC cosine couples

$EOB = (0, 0)$ means there are no non-zero values $\neq 0$ in the block.

Run Category $\rightarrow \max 12$
$K = \prod_{p=1}^{12} |DC_p| + 1|$ each category has $2^k$ values

First order control
$$V_{de-DC_{n-1}}$$
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10

---

<!-- Pagina 11 -->

(TC&JPEG) Draw the scheme and describe the functional blocks of a JPEG encoder.

(TC&JPEG) Compare the block-based DCT approach used in JPEG with the wavelet-based decomposition used in JPEG2000, specifically in terms of how they handle the image signal and the resulting artifacts.

JPEG uses an 8x8 block-based DCT, which processes the image in independent segments. While computationally efficient, this approach often leads to “blocking artifacts” at low bitrates because discontinuities at the block boundaries become visible. In contrast, JPEG2000 utilizes the Discrete Wavelet Transform (DWT), which performs a multiresolution analysis of the entire image (or large tiles). By applying the transform across the image, JPEG2000 avoids the rigid boundaries of JPEG. As a result, instead of blocking, JPEG2000 tends to exhibit “ringing” artifacts (blurring near sharp edges) at very low bitrates, providing a more visually pleasing subjective quality compared to traditional block-based methods.

(TC&JPEG) Explain the fundamental shift in Rate-Distortion (R-D) optimization from classical codecs (e.g., JPEG) to neural compression methods.

Classical codecs rely on combinatorial selection, where the optimization process searches through a pre-defined, discrete set of tools (like fixed transform basis functions and quantization step sizes) to minimize distortion at a given bit-rate. In contrast, neural compression uses continuous learning. It treats optimization as a design process in a continuous space, utilizing gradient descent to physically shape the network’s filter weights by minimizing a differentiable loss function $\mathcal{L} = D + \lambda R$. Consequently, the transform in neural compression is not fixed but is “born” from the data and specifically tailored to the targeted bit-rate.

(TC&JPEG) Describe the JPEG lossless coding process applied to the following table of quantized DCT coefficients:

$$\begin{bmatrix}
10 & 3 & 0 & 0 & 0 & 0 \\
-2 & 1 & 0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 & 0 & 0 \\
0 & 4 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}$$
11
11

---

<!-- Pagina 12 -->

(TC&JPEG) What is the primary purpose of an orthogonal transform in the context of the transform coding paradigm?

(A) Sparsification of the Signal

(TC&JPEG) In the context of JPEG compression, what is the role of the quantization table?

(B) Table standardized by JPEGs

(TC&JPEG) Which statement regarding the relationship between the Arithmetic Mean (AM) and Geometric Mean (GM) of variances in transform coding is correct?

(A) Correct answer: A. Comment: Because orthogonal transforms are isometries, they preserve the $L^2$ norm, which implies that the sum of the variances (related to the AM) remains constant, while the transform aims to minimize the GM to reduce distortion.

(TC&JPEG) What is a primary advantage of the hierarchical (multiresolution) decomposition offered by the Wavelet Transform in JPEG2000?

(B) Progressive Decomposition of Density Images, Add details later

(TC&JPEG) Which of the following is a key reason why JPEG2000 is generally more efficient than JPEG?

(D) Data prioritization → Members
• No dependency among code blocks → Less error propagation
• No Block-Based Transform → No blocking artifacts

(TC&JPEG) What is the primary purpose of adding Additive Uniform Noise during the training phase of a neural codec?

(A) Comment: Quantization is a “staircase” function with zero derivative almost everywhere, which blocks back-propagation. Adding uniform noise $\sim u(-0.5, 0.5)$ acts as a continuous relaxation, allowing gradients to flow during training.

(TC&JPEG) Why do Convolutional Neural Networks (CNNs) outperform Multi-Layer Perceptrons (MLPs) when applied to image compression?

(A) MLPs treat images as flattened vectors, ignoring spatial topology and causing a “parameter explosion.” CNNs exploit local spatial correlations using sliding filters, which is much more efficient for image data.
12
12

---

<!-- Pagina 13 -->

(LLCod) Explain the difference between Fixed-Length Coding (FLC) and Variable-Length Coding (VLC), and describe why VLC is theoretically superior for non-equiprobable sources.

Code C: $x_i \in X \rightarrow x_i \in [0,1]$

FLC:
All codewords have length
Fig. M7 of bits/symbol

VLC:
Different codewords $\rightarrow$ different lengths
Ki: Length of CW Ci
$\Rightarrow$ Lossless coding
Prefix code
Non-equiprobable symbols (Huffman code)

We exploit this foot to design lower slater codes to most probable symbol (Huffman code)

(LLCod) Discuss the importance of the prefix condition in Variable-Length Coding and how it relates to the concept of instantaneous decodability.

Prefix condition $\Rightarrow$ No codeword is a descendant of another (in the tree)
No codeword is a prefix for any other word

Since the prefix condition is valid $\Rightarrow$ We have instantaneous decodability
1:1 Mapping Symbol $\leftarrow$ Bits

TEO:
McMillan $\rightarrow$ Best prefix code $\Rightarrow$ Best decodable code
Kraft Ineq. $\rightarrow \sum 2^{-k_i} \leq 1$ $\Longleftrightarrow$ Instantaneous code with lengths $\{l_1, \dots, l_m\}$

(LLCod) Explain the mechanism behind Arithmetic Coding and why it is often preferred over Huffman coding in practical, high-performance applications.

Arithmetic coding maps an entire input message sequence to a single fractional number within the range [0, 1]. The range is recursively subdivided based on the probability of each incoming symbol. This approach allows to implement block coding of the input message, without having to generate the full, exponentially-complex dictionary as Huffman would do. Its overhead is larger than Huffman’s (2 bits per block instead of one), but, as the block size grows large, it becomes negligible

(LLCod) What are the two distinct mechanisms by which “block coding” improves the efficiency of lossless compression?

Block coding improves performance through two primary contributions. First, for sources with dependencies, the joint entropy of a block $H(X^K)$ is strictly less than the sum of individual marginal entropies $\sum H(X_i)$, meaning that encoding blocks allows the system to exploit inter-symbol correlations. Second, even for independent variables, block coding addresses the “1-bit penalty” inherent in non-dyadic probability distributions; by grouping $K$ symbols, the overhead of rounding codeword lengths to integer bits is distributed across the entire block, effectively becoming 1/K per symbol and vanishing as $K$ approaches infinity.-
13
13

---

<!-- Pagina 14 -->

(LLCod) Provide a synthetic comparison between the main lossless coding techniques (Exp-Golomb, Huffman, Arithmetic, Dictionary, Neural) in terms of complexity and Latency, and provide a typical use case for each of them

| Method | Efficiency | Complexity | Latency | Use Case |
| :---: | :---: | :---: | :---: | :---: |
| Newel (sota) | High | Ultra High | High | SOTA Ing/ViL. |
| Arithmetic | High | High | Med. | BI Level Ing, CABAC |
| Dictionary | Universal | Moderate | Low/med | Repeating Patterns |
| Huffman | Good → High | Low/med | Very low | JPEG, Gravel Purpose |
| Exp-Golomb | Good | Very low | Negligible | Metodora, Resilient |

(LLCod) Describe the principle of the Huffman coding. For the following probability distribution, compute the optimal lossless code, and compare its average length to the source’s entropy

$$p_A = 0.35, p_B = 0.1, p_C = 0.07, p_D = 0.08, p_E = 0.12, p_F = 0.28$$

Sort $\rightarrow$

| Symbol | ENC | Product |
| :---: | :---: | :---: |
| A | 11 | 0.35 |
| B | 010 | 0.10 |
| C | 000 | 0.07 |
| D | 001 | 0.08 |
| E | 011 | 0.12 |
| F | 10 | 0.28 |

$$H_2 = \sum p_i c_i$$
14

---

<!-- Pagina 15 -->

(LLCod) According to Kraft’s inequality, which condition must be satisfied for an instantaneous (prefixx) code to exist with lengths $\{l_1, \dots, l_M\}$?

Kraft’s inequality provides the necessary and sufficient condition for the existence of a prefix code. If the equality holds, the code is complete (or maximal), meaning no more codewords can be added without violating the prefix property.

(LLCod) Which of the following statements best describes the behavior of the Shannon entropy $H(X)$ for a binary random variable with probability $p$?

$$H(x) = -\sum P_x g_2 P_x$$

$$P_x \rightarrow 0 \quad P_x \rightarrow 1 \Rightarrow H(x) \rightarrow 0$$

(LLCod) Why is Lempel-Ziv (e.g., LZW) considered a “universal” coding algorithm?

Universality $\rightarrow$ No preamble Knowledge of source statistics or prior distribution
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15

---

<!-- Pagina 16 -->

(MMQuEv) Explain the difference between subjective and objective quality evaluation in multi-media systems and why both are necessary.

Subjective evaluation involves human participants who rate content based on their personal experience (Quality of Experience - QoE), which is considered the “gold standard” because it directly reflects human perception. However, it is time-consuming, expensive, and not suitable for real-time applications. Objective evaluation uses mathematical models and algorithms to predict quality scores (Quality of Service - QoS). Objective metrics are fast and repeatable, making them ideal for monitoring and optimization, but they may not perfectly correlate with human visual or auditory perception in all scenarios. Therefore, objective metrics are often validated against subjective test data to ensure reliability.

(MMQuEv) What are the key stages involved in designing a subjective quality test according to standardized guidelines?

We need to standardize:
- LAB equipment
- Data set
- Test methodology
- Score Processing

To be repeatable:
- Viewing distance
- Closest angle
- Room-environment color scheme
- Monitor specs (residual contrast, brightness ...)

(MMQuEv) Describe the main categories of objective quality metrics based on the availability of the original “reference” signal.

Availability of the subjective refinement:
Full Reference → PSNR is $G \frac{255^2}{MSE(H)}$, $SSIM = G \frac{C_P}{H}$
Full Refinement → NIRE, BRISSUE, CLIP-1QA
Reduced Refinement → RRED

(MMQuEv) In the context of subjective testing, what is the main purpose of a “screening” phase for participants?

A Comment: To guarantee the validity of subjective results, it is essential that subjects can perceive the stimuli correctly; screening ensures they meet the minimum sensory requirements defined by standards.

(MMQuEv) Which of the following best describes the “Full-Reference” (FR) objective quality assessment approach?

(A) We need the whole signal

(MMQuEv) Why is statistical analysis a critical component of subjective quality evaluation?
(C) Reuse our data
Remove outliers
We also need to take into account:
- Classes
- Color sensitivity
- Expert/not experts
- Visual problem
We also need to take into account:
- Classes
- Color sensitivity
- Expert/not experts
- Visual problem

---

<!-- Pagina 17 -->

(S&P Qnt) Explain the difference between a “mid-tread” and a “mid-rise” quantizer in the context of uniform quantization for signed data.

Mid-tread

Mid-Rise

In 0 there is a threshold
there is a value

Better to use because of zero-count fluctuations $x = 0$

(S&P Qnt) Define the concept of a “deadzone” in a quantizer and explain why it is frequently employed in lossy compression systems.

Deadzone ≠ Zero central area where all data is set to 0
In the quantization process

It is frequently used to filter out the signal fluctuations that are zero-counted.

(S&P Qnt) Why is scalar quantization alone often considered insufficient for effective compression of non-sparse data?

Scalar quantization $\Rightarrow$ regular distance may be large

Improvement in performance using:

• Prediction Quantization → reduce signal variance
• Block Coloring → exploit signal diversity
• Transform Coding → miter the signal sparse
17

---

<!-- Pagina 18 -->

(S&P Qnt) What is the condition for a predictive quantization system to be effective, and how is the “coding gain” defined?

Predictive quantization is effective if and only if the resulting prediction error has a smaller variance than the original signal. The coding gain (or prediction gain, $G_P$) is defined as the ratio between the variance of the original signal $\sigma_X^2$ and the variance of the prediction error $\sigma_Y^2$, expressed in decibels: $G_P = 10 \log_{10} \left( \frac{\sigma_X^2}{\sigma_Y^2} \right)$. A positive coding gain indicates that the prediction successfully reduced the signal’s energy, thereby improving the overall SNR for a given bit rate.

(S&P Qnt) Draw the scheme of a linear predictive quantization scheme, and motivate the structure, with particular attention to the use of a decoding loop at the encoder side

The predictor $\mathcal{P}$ must be fed with the same data at the encoder and the decoder, otherwise there will be a drift. Thus, prediction is used to compute the quantized value $\hat{x}(n)$, which in turn is fed to the linear predictor.

(A) What is the primary purpose of the predictor in a predictive quantization system?

The core objective of predictive quantization is to leverage the correlation between neighboring samples to create a residual signal that is easier to compress than the raw input.

(S&P Qnt) In a predictive quantization system, if the prediction $v(n)$ is nearly equal to $x(n)$, what happens to the variance of the signal $y(n)$ being sent to the quantizer?

$v(n) \approx x(n)$ prediction $\Rightarrow$ good
$y(n) = x(n) - v(n) \rightarrow 0 \Rightarrow y(n) \rightarrow 0$
18
18

---

<!-- Pagina 19 -->

(S&P Qnt) When selecting a linear predictor of order $P$ for a random process, how does the prediction error variance typically behave as the order increases?

$$y(n) = \sum_{n=0}^{P} \partial_n X_n = Fitting x \quad A(z) = \sum_{n=0}^{P} \partial_n z^{-n}$$

Typically an increase in the filter order improves Prediction Gain but for higher orders we get also an increased overload and negligible performance improvement (big P)

(S&P Qnt) In high-resolution uniform quantization, what is the approximate relationship between the SNR and the bit rate ($R$)?

$$\text{SNR} = 10 \log_2 \frac{E[x^2]}{5} = 10 \lg_2 \frac{\theta_x^2}{A^2/12} z^{2R} \approx 6R - 10 \lg_2 \frac{\theta}{3}$$

(AdapStrm) Describe the fundamental architectural differences between a “Push-based” streaming system (e.g., RTP/UDP) and a “Pull-based” system (e.g., DASH).

In push-based architectures, the server dictates the data flow, sending packets to the client according to a server-controlled schedule. This typically requires specialized transport mechanisms and can be problematic for network traversal. Conversely, pull-based systems shift control to the client, which autonomously requests media segments via standard HTTP. This allows the system to utilize standard web infrastructure, such as Content Delivery Networks (CDNs), and enables the client to adapt its requests based on local monitoring of network throughput and buffer state.

(AdapStrm) Analyze the role of the client-side buffer in the context of stability and Quality of Experience (QoE).

Client has to decide applying $K(n)$ and then decide it adaptively $R$ dynamically.

QoE is affected by:

- # ad duration of Puffering Events
- # ad episode of quality changes
- per segment video quality
- duration of initial buff. time

All depends on the client-side buffer.
19
19

---

<!-- Pagina 20 -->

(AdaptStrm) Define “Switching Penalty” and discuss its impact on perceived video quality.

$$\text{Reduction of QoE} \Rightarrow \phi(\Delta) = \begin{cases} 0 & \Delta = 0 \\ \Delta + 5 & \Delta > 0 \\ \frac{\Delta}{2} & \Delta < 0.5 \end{cases}$$

Impact:
Any quality metric, or refinement is imagining perse, better to have constant behavior than frequently changing.

$$\Rightarrow QoE \propto C / \phi(\Delta)$$

(AdaptStrm) Explain the evolution of the playout buffer level $B(t)$ using a mathematical model. In your explanation, describe the dynamics of the “playback” (draining) phase and the “rebufferization” (stalling) phase.

The dynamics of the buffer $B(t)$ are modeled as a continuous-time differential equation:

$$\frac{dB(t)}{dt} = C(t) - R(t),$$

where $C(t)$ is the download rate (throughput) and $R(t)$ is the consumption rate (playback bit-rate).

Playback Phase $B(t) > 0$: During normal operation, the system consumes data at rate $R(t)$. If the download rate $C(t)$ exceeds $R(t)$, the buffer fills. If $C(t) < R(t)$, the buffer drains. The video playback proceeds continuously as long as the buffer level remains above zero.

Rebufferization Phase $B(t) = 0$: When the buffer level reaches zero, playback must stop to avoid an underflow error. The system enters a stall state where $R(t) = 0$ and the buffer level is forced to remain at zero until the accumulated downloaded data exceeds the playback requirement again. The time spent in this state is known as the “rebuffering time,” which is a primary negative factor for the user’s Quality of Experience (QoE).

(AdaptStrm) What is the primary motivation for using HTTP-based protocols for video streaming?

Standard HTTP compatibility is the defining feature of DASH, ensuring that streaming traffic can traverse virtually all enterprise and residential network barriers without specialized hardware.

(AdaptStrm) What is the consequence of an ABR algorithm that systematically overestimates the available bandwidth?

Overestimating throughput causes the client to request data chunks that exceed the current network capability, directly leading to buffer starvation.

(AdaptStrm) Which metric is a direct indicator of streaming QoE from the end-user’s perspective?

Users evaluate streaming quality primarily through the lens of continuous, uninterrupted viewing and perceptual stability, rather than low-level networking metrics like packet loss or hardware versions.

(AdaptStrm) At what stage in the session lifecycle does a DASH client process the Media Presentation Description (MPD)?

The MPD functions as the foundational manifest of the content; the client must ingest this metadata initially to identify the available variants and determine how to construct the requests for specific media segments.
20

---

<!-- Pagina 21 -->

(ME) Describe the difference between “motion field” and “optical flow”.

• (ZD) Motion Field → Project of PHY moment into the image plane
• Optical flow → Apparent motion of a continuum pattern

Often the two things are the same, but not always true

(ME) Explain the Horn and Schunck algorithm’s core principle for dense optical flow estimation.

The algorithm treats optical flow estimation as a global optimization problem. It combines two terms: a data attachment term, which minimizes the residual of the optical flow equation $(u_f + v_f + f_1 = 0)$, and a regularization term that penalizes spatial variations in the velocity field $(\nabla u^2 + \nabla v^2)$. By using a Lagrange multiplier, it forces the flow field to be smooth, effectively resolving the flow estimation problem. In practical applications, the images are spatially sampled and the HS algorithm iteratively converges toward the solution.

(ME) Discuss the Rate-Distortion trade-off when selecting block sizes in motion estimation.

Imagine $L = R + \lambda D$

Rate $R = D_{kl}$ $q(9(x)) p(g)$

Distortion $D = E [\rho(x, x)]$

Trade-off $\Rightarrow$ Higher $\lambda =$ higher quality

Lower $\lambda =$ lower compression

In ME tracking:

$$J(v) = d(v) + \lambda_{ME}$$

$$r(v)$$

High $\lambda_{ME}$ → minimizing colony cost

Low $\lambda_{ME}$ → odgy cost not important just minimize d

(ME) Which of the following is a disadvantage of using the Sum of Squared Differences (SSD) as a matching criterion?

SSD squares the prediction errors, which heavily weights large outliers (e.g., pixels violating the constant illumination hypothesis), often leading to irregular motion vectors compared to SAD.
21
(A)

---

<!-- Pagina 22 -->

(ME) What is the main benefit of the Hexagon Search strategy compared to Full Search?

(D) Hexagon search → evolution of the diamond search
→ more regular shape
→ new step only 3 points to check more
Wrt fill search → 32% of tests to check

(ME) What does an affine motion model allow that a pure translational model does not?

(B) Affine motion models allow other than translation also:
• Rotation → Camera Tilt
• Zoom In/Out → Magnifying effect
The entire motion field is powered by only 6 parameters
$$V = b + B_p = \begin{bmatrix} b_1 \\ b_2 \end{bmatrix} + \begin{bmatrix} b_3 & b_4 \\ b_5 & b_6 \end{bmatrix} P$$

(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying a predictor at new substring it from the original signal
we get a wider more sparse signal ⇒ better compressed with PSDG-like methods-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22
```mark-22
```
(ME) What is the main benefit of the Hexagon Search strategy compared to Full Search?

(D) Hexagon search → evolution of the diamond search
→ more regular shape
→ new step only 3 points to check more
Wrt fill search → 32% of tests to check

(ME) What does an affine motion model allow that a pure translational model does not?

(B) Affine motion models allow other than translation also:
• Rotation → Camera Tilt
• Zoom In/Out → Magnifying effect
The entire motion field is powered by only 6 parameters
$$V = b + B_p = \begin{bmatrix} b_1 \\ b_2 \end{bmatrix} + \begin{bmatrix} b_3 & b_4 \\ b_5 & b_6 \end{bmatrix} P$$

(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying a predictor at new substring it from the original signal
we get a wider more sparse signal ⇒ better compressed with PSDG-like methods-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22-22
```
(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying a predictor at new substring it from the original signal we get a wider more sparse signal ⇒ better compressed with PSDG-like methods-22
```
(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying a predictor at new substring it from the original signal we get a wider more sparse signal ⇒ better compressed with PSDG-like methods-22
(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying a predictor at new substring it from the original signal we get a wider more sparse signal ⇒ better compressed with PSDG-like methods-22
(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying a predictor at new substring it from the original signal we get a wider more sparse signal ⇒ better compressed with PSDG-like methods-22
(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying a predictor at new substring it from the original signal we get a wider more sparse signal ⇒ better compressed with PSDG-like methods-22
(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying a predictor at new substring it from the original signal we get a wider more sparse signal ⇒ better compressed with PSDG-like methods-22
(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying a predictor at new substring it from the original signal we get a wider more sparse signal ⇒ better compressed with PSDG-like methods-22
(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying a predictor at new substring it from the original signal we get a wider more sparse signal ⇒ better compressed with PSDG-like methods-22
(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying a predictor at new substring it from the original signal we get a wider more sparse signal ⇒ better compressed with PSDG-like methods-22
(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying a predictor at new substring it from the original signal we get a wider more sparse signal ⇒ better compressed with PSDG-like methods-22
(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying a predictor at new substring it from the original signal we get a wider more sparse signal ⇒ better compressed with PSDG-like methods-22
(VCP) Why is the temporal prediction error usually more efficient to encode than the original video signal?

Good: get a sparse signal
Original video signal ⇒ not really sparse
By coplying

---

<!-- Pagina 23 -->

(VCP) Describe the function of the “Mode Selection” step in a hybrid video encoder.

$$D = \sum_{k=1}^{K} D_k(n_i, q), R = \sum_{k=1}^{K} R_k(n_i, q) \Rightarrow J(n_i, q, \lambda) = D + \lambda R$$

$$J_K(n_i, q, \lambda) = D_K(n_i, Q) + \lambda R_K(n_i, Q)$$ (Block wise quantization step)

$Q \equiv$ quantization step, for each $q \Rightarrow$ quantize $\lambda$ for MPEG-2 and H.264

$$\lambda = \frac{\partial Q^2}{\partial q} + \frac{\partial Q}{\partial \lambda}$$ $$\lambda = C_2 \frac{\partial Q}{\partial \lambda}$$ $$\lambda = \sqrt{\lambda}$$

(VCP) How does the “Channel Buffer” controller manage the trade-off between target rate and video quality?

The controller monitors the buffer occupancy. If the buffer level exceeds a high threshold (indicating bits are being produced faster than they can be sent), it increases the quantization step size to lower the bit-rate. Conversely, if the buffer falls below a low threshold, it decreases the quantization step size to improve quality by using more bits.

(VCP) What is the primary role of an “I-frame” in a GOP structure?

I-frames are coded independently (Intra-coded), which makes them the only frames that can be decoded without reference to others, acting as anchors.

(VCP) In the context of motion vector coding, why is a Median Predictor (MVP) used?

Since motion in a scene is usually continuous, adjacent blocks have similar vectors. By predicting the current vector from neighbors (A, B, C), we only need to encode the difference (MVD), which is typically small and sparse.

(VCP) What happens in the decoder when it receives an “Inter-coded” block?

In Inter-mode, the decoder relies on the motion information provided in the bitstream to find the predictor in the frame buffer and adds the decoded residual to it.
23
The document contains mathematical equations and text related to video encoder technology. The headings include "(VCP) Describe the function of the 'Mode Selection' step in a hybrid video encoder." and "(VCP) How does the 'Channel Buffer' controller manage the trade-off between target rate and video quality?".

The equations involve summations, matrix multiplication, and algebraic operations. The text discusses the relationship between the buffer level, quantization step size, and video quality in a hybrid video encoder. It also explains the role of an "I-frame" in a GOP structure and how a Median Predictor (MVP) is used for motion vector coding.

The document appears to be a technical report or academic paper, likely intended for researchers or professionals in the field of video processing or computer vision.
The document contains mathematical equations and text related to video encoder technology. The headings include "(VCP) Describe the function of the 'Mode Selection' step in a hybrid video encoder." and "(VCP) How does the 'Channel Buffer' controller manage the trade-off between target rate and video quality?".

The equations involve summations, matrix multiplication, and algebraic operations. The text discusses the relationship between the buffer level, quantization step size, and video quality in a hybrid video encoder. It also explains the role of an "I-frame" in a GOP structure and how a Median Predictor (MVP) is used for motion vector coding.

The document appears to be a technical report or academic paper, likely intended for researchers or professionals in the field of video processing or computer vision.

---

<!-- Pagina 24 -->

(ModernVC) What is the specific scope of video compression standards like H.266/VVC?

H.266/VVC → We get max efficiency but require high computational complexity.
Next-Gen Content (8K 360° video, VR)
Introduces flexibility in space partitioning (blocks), with MTT trees
Loonging at Ternary splits
And provides 65 directional modes for Intro frame prediction

(ModernVC) Explain the advantage of the “Coding Tree Unit” (CTU) structure introduced in HEVC/VVC.

Unlike fixed-size macroblocks, CTUs allow for flexible, recursive partitioning (Quad-tree and Multi-type trees). This enables the encoder to use very large blocks (up to 128x128) for homogeneous areas like sky or walls, and fine-grained, small blocks for detailed textures or object boundaries, significantly improving R-D efficiency in high-resolution video.

(ModernVC) What are the roles of VCL and NAL in modern video standards?

VCL → Video coding layer
Prod. Dept. handles pure compression
NAL → Non-Abstractive layer
L's sliding deck. Takes VCL slices encapsulates them
God: provide an interleaver to map video on RTP/IP, MPEG

(ModernVC) What is the main purpose of the CABAC entropy coder in modern standards?

CABAC → Context Adaptive Binary Antithetic Coding

A) Gain sensitivity on the coding point while keeping lossless
It adapts possibilities dynamically based on previous spatial ctxt.

(ModernVC) Why are “Tiles” considered “hardware-friendly” in VVC and HEVC?

Tiles restrict motion vectors and prediction dependencies to specific boundaries, allowing multiple CPU or GPU cores to process different parts of the same frame simultaneously.

(ModernVC) What is the function of an “In-Loop Filter” like the Adaptive Loop Filter (ALF)?

Since quantization is lossy and block-based, it creates artifacts like blocking or ringing. Filters inside the reconstruction loop ensure these artifacts are smoothed before the frame is stored in the buffer as a reference for future frames.
24
24