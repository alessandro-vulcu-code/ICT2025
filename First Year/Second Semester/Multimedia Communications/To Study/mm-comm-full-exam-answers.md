---
type: exam
status: evolving
tags:
  - multimedia-communications
  - exam
aliases:
  - Full Multimedia Communications Exam Answers
sources:
  - SRC-013
updated: 2026-06-21
---

# Full Multimedia Communications Exam Answers

This page answers the complete question list in `raw/MM_COMM_exam_questions_full.md`. Emoticons from the question file were intentionally removed. Answers are organized by topic and rely on course knowledge, with `raw/mm.pdf` / [[sources/src-013-multimedia-communications-course-pdf|SRC-013]] as the primary local source. Formulas are kept only where they are essential for exam reasoning.

## 1. Introduction, Perception, And Quality Metrics

Primary source: [[sources/src-013-multimedia-communications-course-pdf#Point references|SRC-013, pp. 7-9]].

### Core Block Scheme

![[Pasted image 20260501165037.png]]

1. **Transform**: Linear (DCT, Wavelet) or Non-linear (Neural) — concentrate energy into few coefficients
2. **Prediction**: Spatial or temporal redundancy reduction
3. **Quantization**: Rate reduction through approximation (**the only lossy step**)
4. **Entropy Coding**: Residual redundancy reduction (VLC, Arithmetic coding)

Prediction and transform reorganize information. Quantization removes precision and is therefore the lossy step. Entropy coding is lossless and only removes statistical redundancy left after the previous stages.

### Open-Ended Questions And Answers

#### Open Question 1

**Question:** Describe the three types of redundancy exploited by compression (statistical, psychovisual, semantic) and give a concrete example of each.

**Answer:**

Compression exploits three main kinds of redundancy. Statistical redundancy means neighboring samples or frames tend to be similar; examples are smooth image areas, correlated audio samples, and consecutive video frames. Psychovisual or psychoacoustic redundancy means humans do not perceive all signal details equally; examples are chroma subsampling, frequency-dependent quantization, and audio masking. Semantic redundancy means not all signal information is equally useful for a task; for example, a machine-vision system may need object boundaries or labels more than visually pleasant texture.

#### Open Question 2

**Question:** Explain the *Contrast Sensitivity Function* (CSF): what it is, in which units spatial frequency is measured, where it peaks, and the direct implication for quantization in compression.

**Answer:**

The Contrast Sensitivity Function (CSF) describes how sensitive the human visual system is to contrast at different spatial frequencies. Spatial frequency is measured in cycles per degree or similarly as line cycles over visual angle. The eye is less sensitive at very low and very high spatial frequencies and more sensitive in the middle range. The compression implication is practical: coefficients corresponding to poorly visible frequencies can be quantized more coarsely, while visually important bands deserve finer quantization.

#### Open Question 3

**Question:** Explain *masking* in the auditory system: define frequency masking and temporal masking (pre/post-masking) with their time-scale orders of magnitude.

**Answer:**

Frequency masking in hearing means a strong tone or noise component makes nearby frequencies less audible. If quantization noise stays below the masking curve, it can be present without being perceived. Temporal masking means a loud sound also masks sounds near it in time. Pre-masking is short, on the order of a few milliseconds; post-masking lasts longer, up to around hundreds of milliseconds. Audio codecs use this to hide quantization noise near strong spectral or temporal events.

#### Open Question 4

**Question:** What is the *critical band* and how does it relate to the audibility condition of a set of sinusoids close in frequency?

**Answer:**

A critical band is a frequency interval inside which the ear tends to integrate sound energy rather than resolve every sinusoid separately. If several sinusoids are close in frequency and fall in the same critical band, the listener may perceive combined power more than independent tones. This is why perceptual audio coders allocate bits by bands: the masking threshold is not sample-by-sample but frequency-region dependent.

#### Open Question 5

**Question:**  Compare cones and rods (number, function, lighting conditions) and explain why the RGB→Y conversion weights the green component the most.

**Answer:**

Rods mainly sense brightness and work well in low-light conditions; cones sense color and operate better in normal illumination. The course notes list blue cones as a small minority, green cones as a larger group, and red cones as the largest group. The green component receives strong weight in luminance conversion because human vision is especially sensitive in the green region and because luminance should approximate perceived brightness, not equal RGB arithmetic.

#### Open Question 6

**Question:** Explain the `J:a:b` chroma subsampling notation. Compute the data-reduction factor of 4:2:0 vs full RGB and justify why it is perceptually acceptable.

**Answer:**

Chroma subsampling notation `J:a:b` describes chroma samples over a reference horizontal span. `J` is normally 4, `a` is the number of chroma samples in the first row, and `b` is the number in the second row. In 4:2:0, for a 2x2 pixel area, there are 4 luma samples but only 1 Cb and 1 Cr sample. Compared with full RGB or YCbCr 4:4:4, this uses 6 samples instead of 12, so about half the raw sample count. It is acceptable because the human visual system is more sensitive to luminance detail than chrominance detail.

#### Open Question 7

**Question:**  Compare MSE/PSNR, SSIM and LPIPS: what each measures, pros/cons, and why two images with the **same MSE** can have very different perceived quality.

**Answer:**

MSE and PSNR measure pixel-wise error energy. They are easy to optimize but often disagree with perception because they ignore structure and artifact type. SSIM compares luminance, contrast, and structure, so it better reflects whether image organization is preserved. LPIPS uses neural features and is intended to compare perceptual similarity at a deeper feature level. Two images can have the same MSE while one has random fine noise and the other has blur or geometric distortion; visually those errors feel very different.

#### Open Question 8

**Question:** Draw the *Basic Tools for Compression* scheme (Transform → Prediction → Quantization → Entropy Coding) and indicate which stage is the **only lossy** one and why.

**Answer:**

Basic compression tools can be read as a pipeline:

![[Pasted image 20260501165037.png]]

Transform and prediction are modeling steps. If implemented exactly and before quantization, they do not have to lose information. Quantization maps many possible values to fewer reconstruction values, so different inputs can become identical. That many-to-one mapping is why it is the lossy stage.

#### Open Question 9

**Question:** Define the three SSIM components (luminance, contrast, structure), explain how they combine and the range of the result.

**Answer:**

SSIM is built from three comparisons. Luminance compares average brightness, contrast compares local variance or dynamic range, and structure compares normalized correlation after removing luminance and contrast effects. The components are multiplied, often with exponents controlling their weight. The result is usually interpreted from poor similarity toward 1, where 1 means identical under the metric.

#### Open Question 10

**Question:** What is meant by *machine-centric multimedia* / *task-oriented communication*, and how does the compression objective change vs the human-centric case?

**Answer:**

Machine-centric multimedia means the receiver may be an algorithm rather than a human viewer. In human-centric compression, the objective is perceived quality at low bitrate. In task-oriented compression, the objective can become detection accuracy, classification confidence, segmentation quality, or another task score. This changes what can be discarded: chroma loss may be visually acceptable, but if a machine model needs color cues, discarding chroma may damage the task.

#### Open Question 11

**Question:**  *Principles of image compression.* Discuss the criteria for evaluating a compression algorithm: **rate** and **quality** (PSNR/SSIM/LPIPS), and as a bonus the three extra axes **robustness**, **delay**, **complexity**. Explain the design tensions (e.g. ↑quality vs ↓rate, ↑robustness vs ↓complexity).

**Answer:**

Compression algorithms are evaluated on rate and quality first. Rate tells how many bits are needed; quality tells how much useful or perceived information remains. PSNR, SSIM, and LPIPS are different quality views. Robustness matters because compressed streams propagate bit errors more easily than raw samples. Delay matters because live and interactive applications cannot wait for long buffers or long GOP dependencies. Complexity matters because stronger compression often needs more search, transforms, neural inference, or memory. Design is always a tension: lower rate tends to reduce quality, robustness costs extra bits, and lower delay often reduces coding efficiency.

### Multiple Choice Questions And Answers

#### Multiple Choice 1

**Question:** The HVS Contrast Sensitivity Function peaks:

**Options:**

- A) At very low spatial frequencies.
- B) At mid spatial frequencies (~2–5 cycles/degree).
- C) At very high spatial frequencies.
- D) It is constant across frequencies.

**Answer:**

B. The CSF peaks at middle spatial frequencies.

#### Multiple Choice 2

**Question:** PSNR for 8-bit images is defined as:

**Options:**

- A) $10\log_{10}(255^2/\text{MSE})$
- B) $20\log_{10}(\text{MSE}/255)$
- C) $10\log_{10}(\text{MSE})$
- D) $255^2/\text{MSE}$

**Answer:**

A. For 8-bit images, PSNR uses the squared peak value over MSE.

#### Multiple Choice 3

**Question:** Why is chroma subsampling (4:2:0) applied, and not luma subsampling?

**Options:**

- A) Because chroma takes more bits than luminance.
- B) Because the HVS is much more sensitive to luminance than to chrominance variations.
- C) Because luminance is not compressible.
- D) To avoid blocking artifacts.

**Answer:**

B. Chroma is subsampled because luma detail is more perceptually important.
## 2. Scalar And Predictive Quantization

Primary source: [[sources/src-013-multimedia-communications-course-pdf#Point references|SRC-013, pp. 9-13]].

### Core Block Scheme

![[Pasted image 20260501173300.png]]

The encoder contains a local decoder loop because the decoder will only know reconstructed past samples, not original past samples. Using reconstructed samples on both sides prevents drift.

### Open-Ended Questions And Answers

#### Open Question 1

**Question:**  Explain the difference between a *mid-tread* and a *mid-rise* quantizer in the context of uniform quantization of signed data.

**Answer:**

A mid-tread quantizer has zero as a reconstruction level. Small values around zero are mapped to zero, which is convenient for residuals because many prediction or transform coefficients are close to zero. A mid-rise quantizer has zero as a threshold, not a level; values just below and above zero are pushed to nonzero reconstruction values. For signed compression residuals, mid-rise is usually worse because it amplifies tiny oscillations around zero.

#### Open Question 2

**Question:** Define the concept of a *deadzone* in a quantizer and explain why it is frequently used in lossy compression systems.

**Answer:**

A deadzone is an enlarged quantization interval around zero. Its purpose is to make small coefficients disappear more aggressively. This is useful in lossy compression because after prediction or transform many coefficients are small and perceptually or statistically less important. Mapping them to zero increases sparsity and helps entropy coding.

#### Open Question 3

**Question:** Why is scalar quantization alone often insufficient to compress non-sparse data effectively?

**Answer:**

Scalar quantization alone treats each sample independently. If the original data are not sparse, many samples remain important and the quantizer must spend bits everywhere. Without prediction, transform, or another sparsifying step, scalar quantization mainly reduces precision but does not concentrate information. Compression improves when the signal sent to the quantizer has many near-zero or low-entropy values.

#### Open Question 4

**Question:** What is the condition for a predictive quantization system to be effective, and how is the *coding gain* defined?

**Answer:**

Predictive quantization is effective when the prediction error has lower variance than the original signal. If the residual is smaller and more concentrated around zero, the same quantizer rate gives lower distortion, or the same distortion can be reached at lower rate. Prediction gain compares original variance to residual variance. In words: a predictor is useful only if it makes the signal easier to code.

#### Open Question 5

**Question:** Draw the scheme of a linear predictive quantization system and motivate the structure, with particular attention to the *decoding loop on the encoder side* (the predictor must be fed the same data at encoder and decoder to avoid drift).

**Answer:**

Linear predictive quantization predicts the current sample from reconstructed past samples. The residual is quantized and transmitted. At the decoder, the same predictor reconstructs the same prediction, adds the decoded residual, and obtains the reconstructed sample. The encoder must run this same reconstruction path locally:
![[Pasted image 20260501173300.png]]

If the encoder predicted from original samples but the decoder predicted from reconstructed samples, their states would diverge and errors would accumulate.

#### Open Question 6

**Question:** In high-resolution uniform quantization, derive/justify the "+6 dB SNR per extra bit" rule ($\text{SNR} \approx 6.02\,R + \text{const}$).

**Answer:**

In high-resolution uniform quantization, adding one bit doubles the number of levels and halves the quantization step. Distortion is proportional to the square of the step, so halving the step divides distortion by four. A factor of four in power corresponds to about 6 dB. This is the exam meaning of the "6 dB per bit" rule.

#### Open Question 7

**Question:** Explain the *screening effect*: why does the prediction gain saturate as the linear predictor order $P$ increases?

**Answer:**

The screening effect means prediction gain saturates as predictor order increases. The nearest samples already explain much of the local correlation. Farther samples add less new information because their contribution is partly screened by closer samples. Higher order still may improve performance, but the gain becomes smaller while coefficient signaling, estimation, and complexity increase.

#### Open Question 8

**Question:**  Compare scalar and predictive (DPCM) quantization in terms of the variance of the signal sent to the quantizer and SNR at equal rate.

**Answer:**

Scalar quantization sends the original sample or coefficient to the quantizer, so its variance is whatever the source gives. Predictive quantization sends a residual. If samples are correlated, residual variance is lower than original variance. At equal rate, lower residual variance means smaller distortion relative to the original signal and better SNR. If prediction is bad, residual variance can be high and the system can lose the advantage.

#### Open Question 9

**Question:** *Zero-mean Gaussian signal with autocorrelation $r_X(n-m)=\sigma^2\rho^{|n-m|}$.* (a) With predictor $V(n)=X(n-1)$, for which values of $\rho$ is the prediction gain positive? (b) Optimal linear predictor ($\underline a=-R_X^{-1}\underline r$) of **order $P=1$**: find it, compute the prediction gain and compare with (a). (c) Compute the optimal predictor of **order $P=2$** and compare with the previous cases. *(Full solution of (a)-(b) in numerical exercises Ex 2.2–2.3; for (c) use $R_X=\begin{psmallmatrix}1&\rho\\\rho&1\end{psmallmatrix}\sigma^2$, $\underline r=[\rho,\rho^2]^T\sigma^2$ → $a_1=-\rho,\ a_2=0$: the 2nd tap is zero because an AR(1) is already fully "explained" by an order-1 predictor.)*

**Answer:**

For the Gaussian autocorrelation exercise, with the fixed predictor `V(n)=X(n-1)`, the residual is `X(n)-X(n-1)`. Its variance is `2 sigma^2 (1-rho)`. Prediction gain is positive when this is below `sigma^2`, therefore when `rho > 0.5`. For the optimal order-1 predictor, the best predictor is proportional to `rho X(n-1)`, and the residual variance is `sigma^2(1-rho^2)`. This gives positive gain for any nonzero correlation magnitude. For order 2 with autocorrelation `rho^|k|`, the optimal second coefficient is zero: the process behaves like an AR(1) correlation model, so once `X(n-1)` is known, `X(n-2)` adds no new linear prediction power. Order 2 therefore gives the same gain as optimal order 1.

### Multiple Choice Questions And Answers

#### Multiple Choice 1

**Question:** Primary purpose of the predictor in a predictive quantization system:

**Options:**

- A) Reduce variance / increase sparsity by exploiting inter-sample correlation.
- B) Increase the signal's dynamic range to match the quantizer levels.
- C) Perform transform coding on the whole block.
- D) Completely eliminate quantization noise.

**Answer:**

A. The predictor reduces variance by exploiting correlation.

#### Multiple Choice 2

**Question:** If the prediction $v(n)$ is nearly equal to $x(n)$, what happens to the variance of $y(n)$ sent to the quantizer?

**Options:**

- A) It becomes very small compared to the variance of $x(n)$.
- B) It stays identical.
- C) It increases greatly.
- D) It becomes undefined.

**Answer:**

A. If prediction is good, residual variance becomes small.

#### Multiple Choice 3

**Question:** As the predictor order $P$ increases, the prediction-error variance typically:

**Options:**

- A) Decreases with diminishing returns (screening effect): immediate neighbors already capture almost all the information.
- B) Increases linearly with the order.
- C) Always requires high orders for any gain.
- D) Does not depend on the order.

**Answer:**

A. Higher order usually gives decreasing residual variance with diminishing returns.

#### Multiple Choice 4

**Question:** In high-resolution uniform quantization, the approximate relationship between SNR and rate $R$:

**Options:**

- A) +6 dB SNR per extra bit.
- B) SNR decreases linearly with rate.
- C) SNR constant.
- D) SNR grows as $R^2$.

**Answer:**

A. High-resolution uniform quantization gives about 6 dB per extra bit.
## 3. Lossless Coding

Primary source: [[sources/src-013-multimedia-communications-course-pdf#Point references|SRC-013, pp. 13-17]].

### Core Block Scheme

```text
symbols with probabilities
  -> probability model or dictionary
  -> prefix/arithmetic/dictionary encoder
  -> uniquely decodable bitstream
```

Lossless coding never changes decoded symbols. Its efficiency comes from assigning fewer bits to more likely events or from learning repeated patterns.

### Open-Ended Questions And Answers

#### Open Question 1

**Question:**  Explain the difference between *Fixed-Length Coding* (FLC) and *Variable-Length Coding* (VLC) and why VLC is theoretically superior for non-equiprobable sources.

**Answer:**

Fixed-Length Coding assigns the same number of bits to every symbol. It is simple and easy to parse, but it implicitly treats symbols as equally likely. Variable-Length Coding assigns short codewords to frequent symbols and long codewords to rare symbols. For non-equiprobable sources, VLC lowers average length and moves closer to entropy.

#### Open Question 2

**Question:** Discuss the importance of the *prefix condition* in VLC and how it relates to instantaneous decodability.

**Answer:**

The prefix condition means no codeword is the beginning of another codeword. This makes decoding instantaneous: as soon as a codeword is read, the decoder knows it is complete. Without the prefix condition, a decoder may need to wait for future bits to know whether the current bits are a full word or only the prefix of a longer one.

#### Open Question 3

**Question:**  Explain the mechanism of Arithmetic Coding and why it is often preferred over Huffman in practical, high-performance applications.

**Answer:**

Arithmetic coding represents an entire sequence as an interval inside `[0,1]` that is refined symbol by symbol according to probabilities. It is often preferred over Huffman because it is not forced to assign an integer number of bits to each individual symbol. This matters for skewed probabilities and context-adaptive models, where arithmetic coding can approach entropy more tightly.

#### Open Question 4

**Question:** What are the two distinct mechanisms by which *block coding* improves lossless compression efficiency?

**Answer:**

Block coding improves efficiency in two ways. First, grouping symbols reduces the integer-length penalty because the one-bit overhead is spread over many source symbols. Second, if the source has memory, blocks can capture dependencies between symbols. In that case the relevant limit is entropy rate, not single-symbol entropy.

#### Open Question 5

**Question:**  Provide a synthetic comparison of the main lossless coding techniques (Exp-Golomb, Huffman, Arithmetic, Dictionary, Neural) in terms of complexity and latency, with a typical use case for each.

**Answer:**

Exp-Golomb is simple and good for small integers, especially syntax elements and residual-related values concentrated near zero. Huffman is low-complexity and optimal among prefix codes for a fixed alphabet, but it suffers integer-bit overhead. Arithmetic coding is more complex and may add latency, but it works well with adaptive probability models. Dictionary coding such as LZ77/LZW is universal for repeated strings and text-like patterns because it does not need prior probabilities. Neural lossless coding uses learned probability models and can improve rate on complex sources, but with high computation and model overhead.

#### Open Question 6

**Question:** Describe the principle of Huffman coding. For the following distribution compute the optimal code and compare the average length to the source entropy: A=35%, B=10%, C=7%, D=8%, E=12%, F=28%.

**Answer:**

Huffman coding repeatedly merges the two least probable symbols. For probabilities A=0.35, B=0.10, C=0.07, D=0.08, E=0.12, F=0.28, one valid optimal code is:

| Symbol | Probability | Code |
|---|---:|---|
| A | 0.35 | `11` |
| B | 0.10 | `010` |
| C | 0.07 | `000` |
| D | 0.08 | `001` |
| E | 0.12 | `011` |
| F | 0.28 | `10` |

The average length is about 2.37 bit/symbol. The entropy is about 2.30 bit/symbol. Huffman is therefore close to the entropy bound, with small overhead due to integer code lengths.

#### Open Question 7

**Question:** State Shannon's *Source Coding Theorem* (bounds on average length $\bar{L}$ vs entropy $H$) and what it guarantees.

**Answer:**

Shannon source coding states that for an optimal code, the average length can be made close to entropy. For a memoryless source and a prefix code on single symbols, one has the usual bound `H <= L < H + 1`. By coding long blocks, the average length per source symbol can approach the entropy rate. The theorem does not say every practical code is optimal; it gives the theoretical target.

#### Open Question 8

**Question:** Explain Exp-Golomb coding: for which source statistics it is suited and why it is used in video standards for syntax elements.

**Answer:**

Exp-Golomb coding is suited to nonnegative integers where small values are much more probable than large ones. Signed Exp-Golomb maps signed values to nonnegative integers first. Video standards use it for syntax elements because many mode indices, residual-related quantities, and motion-vector differences are small most of the time.

#### Open Question 9

**Question:** For a binary source with parameter $p$, write $H(p)$, sketch the curve qualitatively and indicate where it is max/min.

**Answer:**

Binary entropy is `H(p)=-p log2 p -(1-p)log2(1-p)`. Qualitatively it is zero at `p=0` and `p=1` because the source is deterministic, and it is maximum at `p=0.5` because uncertainty is highest when both symbols are equally likely.

#### Open Question 10

**Question:** *Source with A,B,C,D,E,F and probabilities $p_A=0.30,\ p_B=0.10,\ p_C=0.05,\ p_D=0.18,\ p_E=0.15,\ p_F=0.22$.* (a) Describe the Huffman algorithm. (b) Build the Huffman code for this distribution. (c) Compare the average length to the entropy. *(Same method as Ex 3.1 but different numbers: $H\approx2.42$ bit/sym; construction: always merge the two least probable symbols.)*

**Answer:**

For probabilities A=0.30, B=0.10, C=0.05, D=0.18, E=0.15, F=0.22, one valid Huffman code is:

| Symbol | Probability | Code |
|---|---:|---|
| A | 0.30 | `10` |
| B | 0.10 | `1111` |
| C | 0.05 | `1110` |
| D | 0.18 | `00` |
| E | 0.15 | `110` |
| F | 0.22 | `01` |

The entropy is about 2.41 bit/symbol and the average length is about 2.45 bit/symbol. Again the code is near optimal; exact bit patterns may differ if ties are broken differently, but lengths and average rate remain optimal.

### Multiple Choice Questions And Answers

#### Multiple Choice 1

**Question:** Kraft's inequality for the existence of a prefix code with lengths $\{l_1,\dots,l_M\}$:

**Options:**

- A) $\sum_{i=1}^M 2^{-l_i} \le 1$
- B) $\sum 2^{-l_i} > 1$
- C) $\sum l_i \le 1$
- D) $\prod 2^{-l_i} \le 1$

**Answer:**

A. Kraft inequality is `sum 2^-li <= 1`.

#### Multiple Choice 2

**Question:** Behavior of the entropy $H(X)$ of a binary variable with probability $p$:

**Options:**

- A) Independent of $p$.
- B) Maximum at $p=0$ or $p=1$.
- C) Minimum at $p=0.5$.
- D) Maximum at $p=0.5$, tends to 0 as $p\to 0$ or $p\to 1$.

**Answer:**

D. Binary entropy is maximum at `p=0.5` and tends to zero near certainty.

#### Multiple Choice 3

**Question:** Why is Lempel-Ziv (LZW) considered "universal"?

**Options:**

- A) It requires no prior knowledge of the source statistics/probabilities.
- B) It produces fixed-length codewords.
- C) It is optimal for every finite sequence.
- D) It uses a static hardcoded dictionary.

**Answer:**

A. LZW is universal because it does not require known probabilities.

#### Multiple Choice 4

**Question:** Huffman's overhead vs the per-symbol entropy (integer-bit rounding penalty) is at most:

**Options:**

- A) < 1 bit/symbol.
- B) Exactly 2 bit/symbol always.
- C) 0 bits always.
- D) Grows unboundedly with the alphabet size.

**Answer:**

A. Symbol-wise Huffman overhead is less than 1 bit/symbol above entropy.
## 4. Transform Coding And JPEG

Primary source: [[sources/src-013-multimedia-communications-course-pdf#Point references|SRC-013, pp. 18-22]].

### Core Block Scheme

```text
JPEG encoder:
  RGB / YCbCr image
    -> optional chroma subsampling
    -> split into 8x8 blocks
    -> subtract 128
    -> 2D-DCT
    -> quantization table
    -> zig-zag scan
    -> DC prediction + AC run-length
    -> entropy coding
    -> JPEG bitstream
```

### Open-Ended Questions And Answers

#### Open Question 1

**Question:** Explain the role of the *geometric mean of the variances* in transform coding and how it relates to the coding gain $G_T$.

**Answer:**

Transform coding tries to create components with unequal variances. If energy is concentrated in few coefficients, bit allocation can spend more bits where variance is high and fewer bits where variance is low. Arithmetic mean variance is preserved by orthogonal transforms, but geometric mean can decrease. The coding gain is linked to this: lower geometric mean after transform means more efficient quantization at equal total rate.

#### Open Question 2

**Question:** Describe the *frequency leakage* problem of the DFT applied to compression and how the DCT solves it.

**Answer:**

DFT assumes periodic extension of the signal. If the block boundaries do not match, artificial jumps appear at the period boundary and create frequency leakage into high frequencies. DCT effectively mirrors the signal before frequency analysis, reducing boundary discontinuities and producing real coefficients. This is why DCT is better suited to block image compression.

#### Open Question 3

**Question:** Explain the entropy coding process for AC coefficients in JPEG and the meaning of the *End of Block* (EOB) symbol.

**Answer:**

JPEG scans quantized AC coefficients in zig-zag order, moving from low toward high frequencies. Since high-frequency coefficients often become zero after quantization, the scan tends to create long zero runs. AC coding represents pairs such as `(run of zeros, category/value)` and uses an End of Block (EOB) symbol when the rest of the block is zero. EOB saves many explicit zero symbols.

#### Open Question 4

**Question:** Draw the scheme and describe the functional blocks of a JPEG encoder.

**Answer:**

JPEG functional blocks are:
![[Pasted image 20260501182627.png]]
```text
image block
  -> level shift
  -> DCT
  -> quantization
  -> zig-zag ordering
  -> DC differential coding
  -> AC run-length coding
  -> Huffman coding
```

The standard mainly constrains decoder syntax and interoperability. Encoder choices, like quality factor or table tuning, can vary.

#### Open Question 5

**Question:**  Compare JPEG's block-DCT approach with JPEG2000's wavelet decomposition regarding how they handle the image signal and the resulting artifacts (blocking vs ringing).

**Answer:**

JPEG uses independent 8x8 block DCTs. This is simple and efficient, but at low bitrate block boundaries become visible because neighboring blocks are quantized independently. JPEG 2000 uses wavelet decomposition over larger regions and supports multiresolution coding. It avoids hard 8x8 blocking but can show ringing near edges. JPEG 2000 also supports precise rate control, resolution scalability, and better error containment through codeblocks.

#### Open Question 6

**Question:**  Explain the fundamental shift in Rate-Distortion optimization from classical codecs (JPEG) to neural methods.

**Answer:**

Classical JPEG uses hand-designed transforms and quantization tables. Rate-distortion optimization is mostly a matter of choosing quantization steps and allocating bits among known transform coefficients. Neural methods learn analysis transform, latent representation, entropy model, and synthesis transform jointly. The shift is from fixed tools plus manual allocation to end-to-end optimization of rate and distortion on data.

#### Open Question 7

**Question:** Describe the JPEG lossless coding process applied to the given table of quantized DCT coefficients (8×8 matrix with values 10, 3, -2, 1, … and zeros): zig-zag scan, run-length and EOB.

**Answer:**

The question mentions an 8x8 coefficient table but the full table is not present in the question file. Therefore a full numerical run-length answer cannot be computed without inventing coefficients. Procedure: take the DC coefficient, encode the difference from previous block DC, zig-zag scan the 63 AC coefficients, replace each nonzero AC value by `(zero-run, category/amplitude)`, insert `(15,0)` for long zero runs, and emit EOB once all remaining coefficients are zero. If the visible start is `10, 3, -2, 1, ...`, DC is 10 and the first AC symbols would encode the first nonzero values in zig-zag order until the missing matrix values are known.

#### Open Question 8

**Question:** Explain why the KLT is the optimal linear transform for decorrelation and why the DCT is used in practice instead.

**Answer:**

KLT is optimal for decorrelation because it aligns transform axes with covariance eigenvectors, producing uncorrelated coefficients and best energy compaction for the given source model. It is not widely used in image codecs because covariance changes across content, eigenvector computation is costly, and the transform itself would need signaling. DCT is fixed, separable, fast, and a good approximation for locally correlated images.

#### Open Question 9

**Question:** Explain how optimal *bit allocation* (e.g. Huang-Schultheiss) distributes bits among coefficients as a function of their variances.

**Answer:**

Huang-Schulteiss allocation gives more bits to coefficients with larger variance and fewer bits to coefficients with smaller variance. At optimum, components are balanced in distortion contribution. In practical terms, smooth or low-energy coefficients may receive zero bits, while important coefficients receive enough precision to reduce global distortion efficiently.

#### Open Question 10

**Question:** *Write the resource allocation problem for transform coding and derive the Huang-Schulteiss formula.* Set up $\min_R \frac1M\sum_k c_k\sigma_k^2 2^{-2R_k}$ subject to $\sum_k R_k\le R_{Tot}$; solve via the Lagrangian ($\partial J/\partial R_k=0$) and impose the constraint to obtain $R_k^*=\frac{R_{Tot}}{M}+\frac12\log_2\frac{c_k\sigma_k^2}{c_{GM}\sigma_{GM}^2}$. Comment: more bits to higher-variance components, equal per-component distortion at the optimum.

**Answer:**

The transform coding resource allocation problem minimizes total distortion under a total bit budget. Using a Lagrangian gives a rate for each coefficient depending on its variance and quantizer constant. The important interpretation is enough for most exam answers: `R_k` increases when `c_k sigma_k^2` is above the geometric mean, decreases when it is below, and may become zero in practical modified algorithms.

### Multiple Choice Questions And Answers

#### Multiple Choice 1

**Question:** Primary purpose of an orthogonal transform in transform coding:

**Options:**

- A) Sparsify the signal by concentrating energy in few large coefficients.
- B) Increase the signal variance.
- C) Make the components statistically dependent.
- D) Reduce the total signal energy before quantization.

**Answer:**

A. Orthogonal transforms sparsify or compact energy.

#### Multiple Choice 2

**Question:** Role of the *quantization table* in JPEG:

**Options:**

- A) Compute the inverse DCT at the decoder.
- B) It is a fixed, mandatory table imposed by the standard.
- C) It performs the frequency analysis of the blocks.
- D) It defines the rate-distortion trade-off by setting the resolution for each DCT coefficient.

**Answer:**

D. Quantization tables control rate-distortion per coefficient.

#### Multiple Choice 3

**Question:** Relationship between arithmetic mean (AM) and geometric mean (GM) of variances under an orthogonal transform:

**Options:**

- A) Any orthogonal transform preserves the AM but may alter the GM.
- B) It alters both.
- C) It preserves the GM but alters the AM.
- D) The AM is minimized by the KLT.

**Answer:**

A. Orthogonal transforms preserve arithmetic mean energy but can change geometric mean.

#### Multiple Choice 4

**Question:** Main advantage of the hierarchical (multiresolution) wavelet decomposition in JPEG2000:

**Options:**

- A) It removes the need for entropy coding.
- B) It enables progressive transmission and scalable reconstruction at multiple resolutions/qualities.
- C) It limits analysis to high frequencies.
- D) It forces 8×8 blocks like JPEG.

**Answer:**

B. Wavelet hierarchy enables progressive and scalable reconstruction.
## 5. Wavelet Analysis And JPEG 2000

Primary source: [[sources/src-013-multimedia-communications-course-pdf#Point references|SRC-013, pp. 22-25]].

### Core Block Schemes

![[Pasted image 20260522132918.png]]

![[Pasted image 20260522133023.png]]

### Open-Ended Questions And Answers

#### Open Question 1

**Question:** State the *time-frequency uncertainty principle* ($\Delta t \cdot \Delta f \ge 1/4\pi$), explain why it imposes a trade-off, and how wavelets address it with adaptive multiresolution (short windows at high frequencies, long at low frequencies).

**Answer:**

The time-frequency uncertainty principle says one cannot have arbitrarily fine time localization and frequency localization at the same time. STFT fixes the window, so the resolution trade-off is the same everywhere. Wavelets adapt scale: short windows analyze high-frequency localized changes, while long windows analyze low-frequency smooth trends. This matches images and signals where edges are local but smooth regions extend.

#### Open Question 2

**Question:**  Compare STFT (rigid tiling) and DWT (adaptive tiling) of the time-frequency plane, linking them to the *trends vs anomalies* image model.

**Answer:**

STFT has rigid tiling: every frequency band uses the same time window size. It is good when a fixed compromise is acceptable. DWT has adaptive tiling: high frequencies get better spatial or temporal localization, low frequencies get better frequency resolution. For image coding, low-frequency trends are broad and smooth, while anomalies such as edges need localized detail coefficients.

#### Open Question 3

**Question:** Draw the scheme of a 1D two-channel filter bank (analysis: $h_0$ LP + $h_1$ HP + decimation ↓2; synthesis: ↑2 + $f_0,f_1$) and indicate where the approximation and detail coefficients arise.

**Answer:**

In a filter bank, the low-pass branch gives approximation coefficients and the high-pass branch gives detail coefficients. Downsampling keeps the total number of samples controlled. The synthesis side upsamples and filters both branches, then sums them to reconstruct. The whole design is useful only if analysis and synthesis filters satisfy reconstruction constraints.

#### Open Question 4

**Question:** State the *Perfect Reconstruction* conditions in the Z-domain (no distortion + aliasing cancellation) and explain what each term represents.

**Answer:**

Perfect reconstruction means the output is only a delayed and scaled version of the input, with no aliasing and no distortion from the filter bank. In the Z-domain this corresponds to two requirements: aliasing terms must cancel, and the non-alias transfer path must be pure delay/gain. In exam words, the decimation creates aliasing, and synthesis filters must cancel it exactly.

#### Open Question 5

**Question:** What are the *vanishing moments* of a filter and how do they relate to sparsity (number of taps ≥ 2p) and the ability to represent polynomials?

**Answer:**

Vanishing moments mean the wavelet/detail filter gives zero response to smooth polynomial signals up to a certain degree. More vanishing moments make smooth regions produce more zeros or small details, improving sparsity. Longer filters are usually needed for more vanishing moments, which increases border handling and complexity.

#### Open Question 6

**Question:** Explain the *border problem* for finite-support signals and compare the three solutions (zero padding, periodization, symmetrization). Why is a symmetric filter needed?

**Answer:**

Finite signals create border problems because filters need samples beyond image boundaries. Zero padding is simple but creates artificial discontinuities. Periodization wraps the signal but can create jumps if ends do not match. Symmetrization mirrors the signal and usually creates smoother boundaries. Symmetric filters are preferred because they preserve edge alignment and avoid phase distortions, but strict orthogonal symmetric FIR filters are severely constrained.

#### Open Question 7

**Question:**  Why are biorthogonal filters (CDF 9/7, 5/3) preferred over orthogonal ones in compression? Cite the fundamental constraint ("the only orthogonal, symmetric, FIR filter is Haar").

**Answer:**

Biorthogonal filters allow separate analysis and synthesis filters. This relaxes the constraints that make orthogonal, symmetric FIR filters almost impossible beyond Haar. CDF 9/7 is effective for lossy image coding because it has good energy compaction with real taps. CDF 5/3 is used for reversible/lossless coding because it can be implemented with integer lifting.

#### Open Question 8

**Question:** Describe a one-level separable 2D-DWT decomposition: the 4 subbands LL/HL/LH/HH, what each contains, and how multiresolution is obtained (recursive decomposition of LL). How many levels are optimal and why?

**Answer:**

In one-level separable 2D-DWT, LL contains the low-low approximation, HL contains horizontal/vertical detail depending on convention, LH contains the other directional detail, and HH contains diagonal/high-frequency detail. Multiresolution is obtained by recursively decomposing LL. The optimal number of levels is a trade-off: more levels improve scale separation but increase overhead, border effects, and may over-decompose small images.

#### Open Question 9

**Question:** Explain the principle of EZW coding: zero-tree structure, inter-scale self-similarity, the 4 symbols (SP/SN/IZ/ZR), and why a single ZR symbol saves many codes. What is quality scalability (bitplane coding)?

**Answer:**

EZW uses the fact that if a wavelet coefficient is insignificant at a coarse scale, many of its descendants may also be insignificant. The symbols are significant positive, significant negative, isolated zero, and zerotree root. A zerotree root can represent a whole insignificant subtree, avoiding many position codes. Bitplane coding gives quality scalability because each additional pass refines already transmitted information.

#### Open Question 10

**Question:** Given a small 4×4 block of DWT coefficients, perform an EZW *dominant pass* and *refining pass* with initial threshold $T = 2^{\lfloor \log_2 \max|c| \rfloor}$.

**Answer:**

The concrete 4x4 DWT coefficient block is not present in the question file, so a numerical dominant/refining pass cannot be completed without inventing data. The method is: choose `T=2^floor(log2 max |c|)`, scan coefficients in subband order, mark coefficients with `|c| >= T` as significant positive or negative, mark insignificant coefficients with significant descendants as isolated zero, and mark insignificant subtrees as zerotree roots. In the refining pass, send the next bitplane for coefficients already found significant, then halve the threshold.

#### Open Question 11

**Question:** Describe the JPEG2000 architecture (Tier 1: DWT 9/7 or 5/3 → fine quantization → arithmetic coding of codeblocks per bitplane; Tier 2: EBCOT). Where does the lossy operation actually happen?

**Answer:**

JPEG 2000 architecture is:

```text
image
  -> tiling
  -> DWT 9/7 lossy or 5/3 reversible
  -> quantization / bitplane representation
  -> codeblocks
  -> Tier 1 arithmetic coding
  -> Tier 2 EBCOT organization and quality layers
  -> codestream
```

The lossy operation is not the arithmetic coder. Loss comes from quantization and especially from truncating coded bitplanes or passes to meet the target rate.

#### Open Question 12

**Question:** Explain EBCOT's Rate-Distortion optimization with the Lagrange multiplier: optimal truncation condition ($\partial D_i/\partial R_i = -\lambda$, same slope for all codeblocks) and how quality layers arise.

**Answer:**

EBCOT computes many possible truncation points for each codeblock. Each truncation has a rate cost and a distortion reduction. The Lagrange multiplier chooses points with comparable rate-distortion slope, so the final stream spends bits where they reduce distortion most efficiently. Quality layers arise by grouping truncation points so that earlier layers give a useful lower-quality version and later layers refine it.

#### Open Question 13

**Question:**  Compare JPEG and JPEG2000 on channel-error robustness (codeblock independence, contained vs catastrophic propagation, resynchronization markers).

**Answer:**

JPEG streams can suffer catastrophic propagation after bit errors because entropy decoding and block order can lose synchronization. JPEG 2000 confines damage more effectively because codeblocks are independently coded and the stream has markers and structure that support resynchronization. The trade-off is overhead and more complex syntax, but robustness and scalability are much better.

### Multiple Choice Questions And Answers

#### Multiple Choice 1

**Question:** The only filter that is simultaneously orthogonal, symmetric and FIR is:

**Options:**

- A) Daubechies 9/7
- B) Haar
- C) CDF 5/3
- D) No FIR filter.

**Answer:**

B. Haar is the only orthogonal, symmetric FIR wavelet in this context.

#### Multiple Choice 2

**Question:** For lossless coding in JPEG2000 the wavelet used is:

**Options:**

- A) Daubechies 9/7 (real-valued taps).
- B) Daubechies 5/3 (integer taps → exact reconstruction).
- C) 8×8 DCT.
- D) 1-tap Haar.

**Answer:**

B. JPEG 2000 lossless uses the reversible 5/3 wavelet.

#### Multiple Choice 3

**Question:** In EBCOT, at the optimal codeblock truncation:

**Options:**

- A) All codeblocks get the same rate.
- B) All codeblocks have the same slope $\partial D/\partial R = -\lambda$ on their R-D curve.
- C) Truncation occurs at the first bitplane.
- D) The total rate cannot be controlled.

**Answer:**

B. EBCOT optimal truncation equalizes rate-distortion slope.

#### Multiple Choice 4

**Question:** A filter with $p$ vanishing moments:

**Options:**

- A) Does not respond to polynomial inputs of degree $< p$ → zero details on smooth regions.
- B) Has exactly $p$ taps.
- C) Is always orthogonal.
- D) Increases the blocking artifact.

**Answer:**

A. Vanishing moments suppress details for smooth polynomial regions.
## 6. Learned Image Compression

Primary source: [[sources/src-013-multimedia-communications-course-pdf#Point references|SRC-013, pp. 25-26]].

### Core Block Scheme

```text
image x
  -> analysis network g_a
  -> latent tensor y
  -> quantization Q
  -> entropy model / arithmetic coding
  -> bitstream
  -> entropy decoding
  -> synthesis network g_s
  -> reconstructed image x_hat
```

### Open-Ended Questions And Answers

#### Open Question 1

**Question:**  Compare the classical paradigm (hand-crafted linear transforms: DCT/DWT) with the neural one (non-linear transforms learned end-to-end). What changes regarding linearity and adaptivity?

**Answer:**

Classical codecs use hand-crafted linear transforms such as DCT or DWT, fixed or manually designed quantization logic, and engineered entropy models. Neural codecs learn nonlinear analysis and synthesis transforms from data. This makes them more adaptive: the transform can learn features that are efficient for the training distribution and the chosen distortion measure.

#### Open Question 2

**Question:** Explain why NIC can be seen as a *non-linear KLT optimized for R-D*. Which limits of the KLT does it overcome?

**Answer:**

NIC can be viewed as a nonlinear KLT because it learns a representation that decorrelates and compacts information, but without being limited to linear covariance eigenvectors. It overcomes KLT limits by learning local, nonlinear, content-dependent transforms and by jointly learning the probability model used for entropy coding.

#### Open Question 3

**Question:** Draw the compression autoencoder scheme: Analysis $g_a$ → quantization $Q$ → entropy coding → Synthesis $g_s$. Indicate what the *latents* are and where compression happens.

**Answer:**

In the autoencoder, latents are the compressed internal representation produced by the analysis network. Compression happens because latents are quantized and entropy-coded, not because pixels are directly stored. The decoder reconstructs from quantized latents, so latent design controls both rate and quality.

#### Open Question 4

**Question:** Write and interpret the Rate-Distortion VAE loss $\mathcal{L} = R + \lambda D$ (rate as KL-divergence, distortion as reconstruction error). What does $\lambda$ control?

**Answer:**

The rate-distortion VAE loss can be read as `L = R + lambda D`. `R` penalizes how many bits are needed to code latents, often through a probability or KL term. `D` penalizes reconstruction error or perceptual distortion. A larger lambda emphasizes quality; a smaller lambda emphasizes compression.

#### Open Question 5

**Question:**  Why compress in the *latent space* instead of pixel space? (decorrelation, Gaussianized distributions, quantization noise hidden in low-perceptual channels).

**Answer:**

Latent space is better than pixel space because the network can decorrelate data, separate important from unimportant information, and produce distributions easier for entropy coding. Quantization noise can also be pushed into latent channels where it has lower perceptual impact. This is the learned equivalent of transform coding and perceptual allocation.

#### Open Question 6

**Question:** Explain the *non-differentiability problem* of quantization (staircase function, zero derivative) and why it blocks backpropagation.

**Answer:**

Rounding quantization is a staircase function. Its derivative is zero almost everywhere and undefined at thresholds. Backpropagation needs useful gradients, so direct hard quantization would block learning in the encoder. This is the central training problem of neural compression.

#### Open Question 7

**Question:** Describe the *Additive Uniform Noise* solution $\mathcal{U}(-0.5, 0.5)$ during training (vs rounding at test time) and its theoretical grounding. Also mention STE and soft quantization as alternatives.

**Answer:**

Additive uniform noise replaces hard rounding during training: instead of `round(y)`, the model uses `y + u` with `u` uniformly distributed around zero. This resembles high-resolution quantization noise and provides a differentiable approximation. At test time the codec still uses real rounding. Other approaches include straight-through estimators and soft quantization, but additive noise is a common clean solution.

#### Open Question 8

**Question:** What is *GDN* (Generalized Divisive Normalization)? Write the formula, explain lateral inhibition, the link to HVS masking, and the Gaussianization useful for entropy coding. Why is it better than ReLU for compression?

**Answer:**

Generalized Divisive Normalization (GDN) normalizes a feature by a learned function of neighboring feature energy. Conceptually it acts like lateral inhibition: strong nearby activity changes the response of a channel. This resembles masking and helps Gaussianize/decorrelate latents, which improves entropy coding. ReLU is useful for classification but less tailored to compression because it does not explicitly normalize local energy or shape latent statistics.

#### Open Question 9

**Question:** Explain the *Scale Hyperprior* (Ballé 2018): why it is needed, how a second autoencoder ($h_a, h_s$) transmits side-information $\hat z$ to predict the $\sigma$ of the latents' conditional prior, and the impact on the total rate.

**Answer:**

The scale hyperprior adds a second latent stream. The main latents `y` are quantized, but their distribution varies spatially. A hyper-encoder analyzes `y`, sends side information `z_hat`, and a hyper-decoder predicts local probability parameters such as scale or standard deviation for `y_hat`. This side information costs bits, but it often reduces total rate because the main entropy model becomes much more accurate.

#### Open Question 10

**Question:**  Explain why CNNs outperform MLPs in image compression (local connectivity, weight sharing, translation invariance, MLP parameter explosion).

**Answer:**

CNNs outperform MLPs in image compression because images have local structure. Convolutions share weights across positions, model local neighborhoods efficiently, and preserve translation behavior. An MLP over pixels would require far more parameters and would not naturally exploit locality.

#### Open Question 11

**Question:** What are *transposed convolutions* and why are they needed in the decoder (learned upsampling, 1-to-N / overlap & sum mechanism)?

**Answer:**

Transposed convolutions are learned upsampling operations used by the decoder. They expand low-resolution latent feature maps into higher-resolution feature maps and finally pixels. The important idea is not "inverse convolution" in a strict algebraic sense, but learned reconstruction from compact spatial features.

#### Open Question 12

**Question:**  JPEG-AI: goals (beat VVC-Intra by ~50%), backbone (hierarchical VAE with hyperprior), *dual-use* human/machine support, and complexity profiles (Dec0/Dec1/Dec2, kMAC/px). Cite pros/cons vs classical codecs (R-D vs computational cost, determinism, hallucinations).

**Answer:**

JPEG AI aims to outperform strong intra image coding tools while supporting human viewing and machine tasks. The course source describes a hierarchical VAE with hyperprior and decoder complexity profiles such as Dec0, Dec1, and Dec2 measured in kMAC/px. Its advantage is rate-distortion efficiency, especially at low bitrate. Its weaknesses are computational cost, energy use, cross-platform determinism, and possible hallucinated details on out-of-distribution content.

### Multiple Choice Questions And Answers

#### Multiple Choice 1

**Question:** Main purpose of adding additive uniform noise during the training of a neural codec:

**Options:**

- A) Make the (staircase) quantization differentiable to enable backpropagation.
- B) Increase spatial resolution.
- C) Filter out high-frequency noise.
- D) Simulate channel errors on the latents.

**Answer:**

A. Additive uniform noise makes training differentiable.

#### Multiple Choice 2

**Question:** Why do CNNs outperform MLPs in image compression?

**Options:**

- A) Local connectivity and weight sharing reduce parameters and enforce translation invariance.
- B) MLPs do not perform non-linear activation.
- C) CNNs are linear.
- D) MLPs need far more data for the same image.

**Answer:**

A. CNNs exploit local connectivity and weight sharing.

#### Multiple Choice 3

**Question:** GDN is used to:

**Options:**

- A) Replace motion compensation.
- B) Normalize features by local energy (lateral inhibition) and Gaussianize the latents for entropy coding.
- C) Increase the bit-rate by adding redundancy.
- D) Convert the image to the frequency domain with the DCT.

**Answer:**

B. GDN normalizes by local energy and helps entropy coding.

#### Multiple Choice 4

**Question:** In the Scale Hyperprior, the side-information $\hat z$ serves to:

**Options:**

- A) Directly reconstruct the pixels.
- B) Predict the standard deviation $\sigma$ of the latents' conditional prior at each spatial location.
- C) Replace quantization.
- D) Remove the decoder.

**Answer:**

B. Hyperprior side information predicts latent distribution scale.

#### Multiple Choice 5

**Question:** A risk of neural codecs absent in classical codecs is:

**Options:**

- A) The blocking artifact.
- B) Decoder drift / cross-platform non-determinism (float) and hallucinations on out-of-distribution inputs.
- C) The lack of entropy coding.
- D) Lossless support.

**Answer:**

B. Neural codecs can suffer determinism and hallucination risks.
## 7. Motion Estimation

Primary source: [[sources/src-013-multimedia-communications-course-pdf#Point references|SRC-013, pp. 26-31]].

### Core Block Scheme

```text
current block or pixel region
  -> search in reference frame
  -> choose motion vector/model minimizing cost
  -> build prediction
  -> encode residual plus motion information
```

### Open-Ended Questions And Answers

#### Open Question 1

**Question:**  Describe the difference between *motion field* and *optical flow*.

**Answer:**

A motion field is the actual displacement or velocity field of scene points or pixels between frames. Optical flow is an estimated apparent motion field derived from brightness changes in image data. Optical flow depends on assumptions such as constant illumination and smoothness; it is not always identical to physical motion because illumination changes, occlusions, and sampling can mislead it.

#### Open Question 2

**Question:** Explain the core principle of the Horn & Schunck algorithm for dense optical flow estimation (data-attachment term from the optical-flow equation + regularization term enforcing smoothness, solved with a Lagrange multiplier).

**Answer:**

Horn and Schunck estimates dense optical flow by combining a data term with a regularization term. The data term comes from the optical-flow equation and says the estimated velocity should explain brightness changes. The regularization term says neighboring velocities should vary smoothly. A Lagrange multiplier balances fidelity to image data and smoothness of the field.

#### Open Question 3

**Question:**  Discuss the Rate-Distortion trade-off in choosing the block size in motion estimation.

**Answer:**

Small blocks adapt well to local motion, edges, and object boundaries, so prediction error can be low. But they require more vectors and more signaling bits, and they may produce noisy vector fields. Large blocks cost fewer motion bits and are simpler, but they cannot represent complex local motion and often leave larger residuals. Rate-distortion optimization chooses the block size that minimizes residual cost plus motion-vector rate.

#### Open Question 4

**Question:** Derive the *optical flow equation* ($u f_x + v f_y + f_t = 0$) from the constant-illumination hypothesis and explain the *aperture problem*.

**Answer:**

Constant illumination assumes the same moving point keeps the same brightness between frames. Linearizing this assumption for small motion gives the optical-flow equation `u f_x + v f_y + f_t = 0`. It provides one equation for two unknowns, horizontal and vertical velocity. This underdetermination is the aperture problem: through a small local window, motion along an edge may be ambiguous.

#### Open Question 5

**Question:**  Compare the SAD, SSD and MAD matching criteria: computational cost, outlier sensitivity, motion-field regularity.

**Answer:**

SSD squares differences, so it directly matches MSE/PSNR optimization but is sensitive to outliers and uses multiplications. SAD sums absolute differences, is cheaper, and often gives robust practical behavior. MAD is SAD normalized by block size, so it is comparable across block sizes. Regularized variants add a penalty for irregular vectors, reducing vector coding cost and improving field coherence.

#### Open Question 6

**Question:**  Compare Full Search and fast searches (Three-Step, Hexagon, Diamond): number of tested vectors vs optimality.

**Answer:**

Full Search tests every candidate in the search window and finds the best vector for that window, but complexity is high. Three-Step Search, Diamond Search, and Hexagon Search test a small pattern and move it iteratively. They greatly reduce candidate evaluations but rely on the error surface being reasonably smooth or unimodal. They are near-optimal in many cases but do not guarantee the global minimum.

#### Open Question 7

**Question:** *Block matching: give the principles of the approach, at least one cost function, and [bonus] discuss the regularization issue.* Explain the regularized cost $J_{REG}(i,j)=\|\mathbf f_k-\mathbf f_h\|_p^p+\lambda R(i,j)$ (penalizes vectors too different from neighbors) and $J(v)=d(v)+\lambda_{ME}\,r(v)$ (MV rate): why it is needed (more regular MVF, lower coding cost) and the effect of $\lambda_{ME}$.

**Answer:**

Block matching compares a current block with displaced candidate blocks in a reference frame. A typical cost is SAD or SSD between block samples. A rate-aware cost adds `lambda` times motion-vector coding cost, and a regularized cost penalizes vectors unlike their neighbors. Larger lambda favors smoother, cheaper vector fields; smaller lambda favors raw prediction accuracy even if the vector field is expensive to signal.

### Multiple Choice Questions And Answers

#### Multiple Choice 1

**Question:** Disadvantage of using SSD as a matching criterion:

**Options:**

- A) It is outlier-sensitive and involves multiplications → higher complexity and irregular motion fields.
- B) It does not compute the prediction-error energy correctly.
- C) It produces a more regular field than SAD.
- D) Impossible to use in iterative searches.

**Answer:**

A. SSD is more complex and outlier-sensitive.

#### Multiple Choice 2

**Question:** Main benefit of the Hexagon Search vs Full Search:

**Options:**

- A) Always guarantees the global minimum.
- B) Only for affine motion models.
- C) Removes sub-pixel interpolation.
- D) Greatly reduces the number of tested vectors while keeping near-optimal performance.

**Answer:**

D. Hexagon Search reduces tested vectors while remaining near-optimal.

#### Multiple Choice 3

**Question:** What does an affine motion model allow that a purely translational one does not?

**Options:**

- A) Fewer parameters and more noise robustness.
- B) It can represent rotation, zoom and shear with six parameters.
- C) It forces the same vector for all pixels.
- D) It computes motion without a reference image.

**Answer:**

B. Affine motion can model rotation, zoom, and shear.
## 8. Video Coding Principles

Primary source: [[sources/src-013-multimedia-communications-course-pdf#Point references|SRC-013, pp. 31-33]].

### Core Block Scheme

![[Pasted image 20260522142252.png]]

```text
hybrid video encoder:
  current frame
    -> mode decision
       -> intra prediction or motion estimation/compensation
    -> subtract prediction -> residual
    -> transform
    -> quantization
    -> entropy coding -> bitstream
    -> inverse quantization + inverse transform
    -> add prediction
    -> reconstructed frame buffer for future prediction
```

### Open-Ended Questions And Answers

#### Open Question 1

**Question:** Why is the temporal prediction error usually more efficient to encode than the original video signal?

**Answer:**

Temporal prediction error is usually easier to encode because consecutive frames are similar. Instead of coding a whole frame, the encoder codes how blocks moved plus the difference between prediction and reality. If motion compensation is good, the residual has low energy and many small coefficients after transform.

#### Open Question 2

**Question:** Describe the function of the *Mode Selection* step in a hybrid video encoder.

**Answer:**

Mode selection chooses among coding options such as intra, inter, skip/direct, partition size, reference frame, and sometimes transform choices. It evaluates the rate-distortion trade-off: a mode with low distortion may require many bits, while a cheap mode may create worse residual. The selected mode minimizes total cost for the current encoder objective.

#### Open Question 3

**Question:** How does the *Channel Buffer* controller manage the trade-off between target rate and video quality (raising/lowering the quantization step based on buffer occupancy)?

**Answer:**

The channel buffer controller prevents output bitrate from overflowing or underflowing the target channel. If the buffer fills too much, the encoder raises the quantization step, lowering quality but reducing bits. If the buffer becomes too empty, it can lower the quantization step, improving quality and spending more bits. Rate control is therefore a feedback loop between buffer state and quantization.

#### Open Question 4

**Question:** Draw the block diagram of a hybrid video encoder (motion estimation/compensation + DCT + quantization + entropy coding + reconstruction loop with frame buffer). Explain why the encoder contains an internal decoder.

**Answer:**

The encoder contains an internal decoder because future predictions at the decoder will use reconstructed frames, not original frames. If the encoder used original frames as references, encoder and decoder predictions would differ and drift would accumulate. The reconstruction loop guarantees both sides use the same reference pictures.

#### Open Question 5

**Question:** Explain the GOP structure and I/P/B frame types: role, dependencies, and impact on compression, random access and latency.

**Answer:**

A Group of Pictures (GOP) combines I, P, and B frames. I frames are intra-coded and provide random access and error reset, but cost many bits. P frames predict from previous reference frames and improve compression with manageable delay. B frames predict from past and future references, improving efficiency further but requiring reordering and adding latency. Real-time systems often avoid B frames.

#### Open Question 6

**Question:** What is the *Median Predictor* for motion vectors and how does coding only the MVD (difference) exploit the spatial correlation of vectors?

**Answer:**

The median predictor for motion vectors estimates the current vector from neighboring vectors, often left, top, and top-right. Since nearby blocks usually move similarly, the difference between actual motion vector and predicted vector is small. Coding this motion-vector difference instead of the full vector reduces bitrate.

#### Open Question 7

**Question:** *Describe the intra-coding modes in H.264. [Optional] Discuss also the Intra modes in H.265.* H.264: directional intra prediction on 4×4/16×16 luma blocks from already-decoded neighboring pixels — 9 modes for 4×4 (DC + 8 directional), 4 for 16×16; the predicted residual is then transformed/quantized. H.265/HEVC: **35 modes** (DC, Planar + 33 directional) on variable-size blocks (CU/PU up to 32×32), with finer angular prediction.

**Answer:**

H.264 intra coding predicts a block from already decoded neighboring pixels using several directional modes. For 4x4 luma blocks there are multiple directional modes plus DC; for 16x16 blocks fewer broader modes are used. The residual after prediction is transformed and quantized. HEVC extends this idea with more angular modes and larger variable blocks, giving finer spatial prediction.

#### Open Question 8

**Question:** *Describe the principle of the H.264 deblocking in-loop filter.* An adaptive filter applied to the edges of 4×4 blocks/macroblocks **inside the reconstruction loop** (before writing the frame to the reference buffer). It reduces blocking artifacts due to block-based quantization; the boundary strength and intensity depend on the value jump at the edge and on coding parameters; it operates on luma and chroma. It improves subjective quality and, being in the loop, also the prediction of subsequent frames.

**Answer:**

The H.264 deblocking filter is applied inside the reconstruction loop, before the reconstructed frame is stored as a reference. It smooths block boundaries created by block transforms and quantization. Its strength depends on coding conditions and boundary differences. Because filtered frames become references, the filter improves both current visual quality and future prediction.

### Multiple Choice Questions And Answers

#### Multiple Choice 1

**Question:** Primary role of an *I-frame* in a GOP structure:

**Options:**

- A) Provide a random-access point and terminate temporal error propagation.
- B) Highest compression ratio via spatial prediction.
- C) Store only the motion vectors.
- D) Temporary buffer for B-frames.

**Answer:**

A. I frames provide random access and stop temporal error propagation.

#### Multiple Choice 2

**Question:** Why is a *Median Predictor* (MVP) used in motion vector coding?

**Options:**

- A) To exploit the spatial correlation between adjacent vectors and reduce the MVD bit-rate.
- B) To compute the background motion better than the foreground.
- C) To force all vectors identical.
- D) To increase complexity and avoid overfitting.

**Answer:**

A. Median MVP exploits spatial correlation of motion vectors.

#### Multiple Choice 3

**Question:** What does the decoder do when it receives an *Inter-coded* block?

**Options:**

- A) It decodes the motion vector and prediction error, then adds them to the block from the reference frame.
- B) It discards the frame and requests retransmission.
- C) It runs a new motion-estimation search.
- D) It uses only spatial filtering.

**Answer:**

A. Inter decoding adds decoded residual to motion-compensated prediction.
## 9. Modern Video Compression Standards

Primary source: [[sources/src-013-multimedia-communications-course-pdf#Point references|SRC-013, pp. 34-35]].

### Core Block Scheme

```text
standardized decoder view:
  bitstream
    -> NALU / OBU parsing
    -> entropy decoding
    -> inverse quantization and inverse transform
    -> intra or inter prediction
    -> reconstruction
    -> in-loop filtering
    -> output and reference pictures
```

### Open-Ended Questions And Answers

#### Open Question 1

**Question:** What is the specific scope of video compression standards like H.266/VVC?

**Answer:**

Standards such as H.266/VVC define bitstream syntax and decoder behavior, not every encoder decision. They specify how coded data must be parsed, predicted, transformed back, filtered, and output. Encoder search strategies, mode pruning, and rate control remain areas where implementations compete.

#### Open Question 2

**Question:** Explain the advantage of the *Coding Tree Unit* (CTU) structure introduced in HEVC/VVC (flexible recursive partitioning, large blocks for homogeneous areas and small ones for textures/edges).

**Answer:**

CTUs allow large blocks in smooth regions and recursive splitting into smaller units near edges, texture, and motion boundaries. This improves high-resolution coding because a fixed 16x16 macroblock is too small for large flat areas and too rigid for complex areas. Flexible partitioning improves rate-distortion efficiency at the cost of a much larger encoder search problem.

#### Open Question 3

**Question:** What are the roles of VCL and NAL in modern video standards?

**Answer:**

VCL contains video coding layer data, such as coded slices and picture content. NAL wraps coded data and parameter information into units suitable for storage or transport. Non-VCL NAL units include sequence and picture parameter sets and supplemental information. This separation lets networks, containers, and decoders handle metadata and picture payloads cleanly.

#### Open Question 4

**Question:**  Compare macroblocks (H.264) and CTU/quad-tree (HEVC/VVC) in terms of R-D efficiency at high resolution.

**Answer:**

H.264 macroblocks are fixed at 16x16 with limited subdivision. HEVC/VVC CTU structures begin with larger units and split recursively. At high resolution, large CTUs avoid wasting bits on signaling many small blocks in smooth areas, while small partitions are still available where detail requires them. The price is complexity: more partitions and modes must be evaluated or pruned.

#### Open Question 5

**Question:** Explain the principle of CABAC: context modeling, binarization, and context-adaptive binary arithmetic coding. Why does it beat Huffman/CAVLC?

**Answer:**

CABAC first binarizes syntax elements into binary decisions, then estimates probabilities using local context, then arithmetic-codes the bins. It beats Huffman/CAVLC because probabilities adapt to neighboring syntax and because arithmetic coding avoids integer-length constraints per symbol. It is more complex but usually more efficient.

### Multiple Choice Questions And Answers

#### Multiple Choice 1

**Question:** Main purpose of the CABAC entropy coder in modern standards:

**Options:**

- A) Adaptively assign shorter bit sequences to more frequent symbols based on context.
- B) Convert the image to the frequency domain.
- C) Replace motion compensation.
- D) Increase the bit-rate by adding redundancy for error correction.

**Answer:**

A. CABAC assigns shorter codes using adaptive context probabilities.

#### Multiple Choice 2

**Question:** Why are *Tiles* "hardware-friendly" in VVC/HEVC?

**Options:**

- A) They allow independent processing of rectangular regions → parallel encoding/decoding.
- B) They improve the quality of moving objects.
- C) They remove the need for entropy coding.
- D) They force the use of a single core.

**Answer:**

A. Tiles allow independent rectangular-region processing.

#### Multiple Choice 3

**Question:** Function of an *In-Loop Filter* like the Adaptive Loop Filter (ALF):

**Options:**

- A) Reduce quantization artifacts and restore details at reconstruction (clean frame in the reference buffer).
- B) Speed up motion estimation.
- C) Generate random grain.
- D) Replace the transform block.

**Answer:**

A. In-loop filters reduce artifacts before frames enter the reference buffer.
## 10. Audio And Speech Compression

Primary source: [[sources/src-013-multimedia-communications-course-pdf#Point references|SRC-013, pp. 36-38]].

### Core Block Schemes

```text
source-based speech coding:
  speech frame -> LPC analysis -> pitch / excitation parameters -> quantization -> bitstream
  decoder -> excitation + synthesis filter -> speech
```

```text
perceptual audio coding:
  audio -> filter bank / MDCT -> spectral coefficients -> quantization -> entropy coding
      \-> psychoacoustic model -> masking thresholds -> bit allocation -----/
```

### Open-Ended Questions And Answers

#### Open Question 1

**Question:**  Explain the difference between *Source-Based* (parametric) and *Sink-Based* (perceptual) coding.

**Answer:**

Source-based coding models how the sound is generated. For speech, it models vocal tract filtering and excitation, so it can be very efficient at low bitrate while preserving intelligibility. Sink-based or perceptual coding models what the listener cannot hear. It is better for music and general audio because it hides quantization noise below masking thresholds.

#### Open Question 2

**Question:** Describe the *Analysis-by-Synthesis* (AbS) loop used in CELP codecs and why it improves over simple LPC-10.

**Answer:**

CELP analysis-by-synthesis makes the encoder simulate the decoder for candidate excitations. It searches adaptive and fixed codebooks, synthesizes possible speech, measures perceptually weighted error, and transmits the best index and gains. This improves over simple LPC-10 because it does not only send a rough voiced/unvoiced excitation; it optimizes excitation shape against reconstructed speech.

#### Open Question 3

**Question:** What is the role of the psychoacoustic masking model in perceptual audio coding and how is it used to allocate bits?

**Answer:**

The psychoacoustic model estimates masking thresholds across frequency and time. The encoder then allocates bits so quantization noise remains below those thresholds when possible. Bands with audible noise risk receive more bits; bands where noise is masked receive fewer. This is why perceptual audio can have low waveform SNR but still sound transparent.

#### Open Question 4

**Question:** Describe the principles of the LPC-10 speech coding scheme.

**Answer:**

LPC-10 divides speech into short frames, estimates an all-pole vocal-tract filter from autocorrelation/Yule-Walker equations, detects voiced or unvoiced excitation, estimates pitch for voiced frames, and sends parameters rather than waveform samples. The decoder reconstructs speech by exciting the inverse filter. It is low-rate and intelligible but not high-fidelity.

#### Open Question 5

**Question:** Draw the scheme and describe the operation of the functional blocks of an MP3 encoder.

**Answer:**

An MP3-style encoder uses a filter bank, psychoacoustic analysis, bit allocation, quantization, and Huffman coding:

```text
PCM audio
  -> analysis filter bank / MDCT
  -> spectral coefficients
  -> quantization and scalefactors
  -> Huffman coding
  -> bitstream

PCM audio
  -> psychoacoustic model
  -> masking thresholds / SMR
  -> bit allocation control
```

#### Open Question 6

**Question:** Draw the general block diagram of a perceptual audio encoder (filter bank/MDCT in parallel with the psychoacoustic model → bit allocation → quantization → entropy coding).

**Answer:**

The general perceptual encoder is the same conceptual structure as MP3/AAC: transform audio into frequency-like coefficients, estimate masking thresholds, allocate quantization precision by band, then entropy-code the quantized data. The psychoacoustic model does not reconstruct audio; it controls where distortion is allowed.

#### Open Question 7

**Question:**  Compare speech coding (LPC/CELP, source model) and music coding (MP3/AAC, perceptual): goals, bitrate, quality.

**Answer:**

Speech coding targets intelligibility and low bitrate by using a source model such as LPC or CELP. Music coding targets transparency, wider bandwidth, and complex spectra by using perceptual transform coding such as MP3 or AAC. Speech coders can work at very low rates because speech production is constrained; music coders need higher rates because music is less predictable and quality expectations are higher.

### Multiple Choice Questions And Answers

#### Multiple Choice 1

**Question:** Why are *Line Spectrum Frequencies* (LSF) preferred over direct quantization of LPC coefficients $a_i$?

**Options:**

- A) They guarantee filter stability (roots on the unit circle, interlacing property that can be verified/corrected).
- B) They give a higher SNR.
- C) They need fewer bits because they are positive integers.
- D) They directly represent the pitch.

**Answer:**

A. LSFs make LPC filter stability easier to preserve.

#### Multiple Choice 2

**Question:** Primary technical advantage of Opus's hybrid design:

**Options:**

- A) Based only on fixed-rate PCM.
- B) It dynamically switches/combines an LPC engine and an MDCT engine to handle speech and music across a wide bitrate range.
- C) It uses a psychoacoustic model identical to MP3.
- D) It avoids all entropy coding.

**Answer:**

B. Opus combines speech and transform coding for varied content and bitrate.

#### Multiple Choice 3

**Question:** Current research trend in the future of multimedia audio coding:

**Options:**

- A) Abandoning lossy in favor of universal lossless.
- B) Increasing PCM bit-depth to 64 bits.
- C) Moving from signal-processing models to end-to-end deep-learning neural codecs.
- D) Replacing packet-based protocols with circuit-switched channels.

**Answer:**

C. Audio coding research increasingly includes end-to-end neural codecs.
## 11. Quality Assessment And QoE

Primary source: [[sources/src-013-multimedia-communications-course-pdf#Point references|SRC-013, pp. 39-41]].

### Core Block Scheme

```text
subjective assessment:
  controlled content -> controlled display/listening setup -> observers -> scores -> MOS/statistics

objective assessment:
  reference and/or output signal -> metric -> predicted quality score
```

### Open-Ended Questions And Answers

#### Open Question 1

**Question:**  Explain the difference between subjective and objective quality evaluation in multimedia systems and why both are necessary.

**Answer:**

Subjective evaluation asks people to judge quality and is the reference for perceived experience. It is expensive, slow, and variable, but it measures what actually matters to users. Objective evaluation computes quality with formulas or models. It is fast and repeatable, but may fail when artifacts affect perception in ways the metric does not capture. Both are needed: subjective tests validate, objective metrics optimize and monitor.

#### Open Question 2

**Question:** What are the key stages in designing a subjective quality test according to standardized guidelines?

**Answer:**

A subjective test must choose representative content, control viewing or listening conditions, screen participants for visual or auditory ability, define rating instructions, choose a method such as ACR, DSIS, or pairwise comparison, randomize presentation, collect scores, remove outliers, and report statistical uncertainty. Without this discipline, MOS values are not trustworthy.

#### Open Question 3

**Question:**  Describe the main categories of objective quality metrics based on the availability of the reference signal (Full-Reference, Reduced-Reference, No-Reference).

**Answer:**

Full-reference metrics compare degraded output with the original signal, as PSNR, SSIM, or VMAF do. Reduced-reference metrics use only selected features from the original and compare them with output features. No-reference metrics use only the degraded output and estimate quality from distortions or learned patterns. FR is usually more reliable but requires the original, while NR is more practical in deployed systems.

#### Open Question 4

**Question:** What is the MOS (Mean Opinion Score) and why is statistical analysis needed (outlier removal, confidence intervals, inter-subject variability)?

**Answer:**

MOS is the average of observer ratings. Statistical analysis is needed because observers disagree, may misunderstand the task, or may be outliers. Confidence intervals separate uncertainty of the estimated mean from real disagreement between subjects. More observers reduce uncertainty, but they do not make content intrinsically less subjective.

#### Open Question 5

**Question:**  Compare QoS and QoE: what they measure and how they correlate. Which network factors impact streaming QoE?

**Answer:**

QoS measures service/network quantities such as throughput, delay, jitter, and packet loss. QoE measures user-perceived experience. They correlate but not linearly: a small packet loss may be invisible if buffered, while one stall can dominate user annoyance. Streaming QoE is affected by visual quality, stalls, startup delay, quality switches, latency, and device/context constraints.

### Multiple Choice Questions And Answers

#### Multiple Choice 1

**Question:** Main purpose of the *screening* phase of participants in subjective tests:

**Options:**

- A) Ensure they have the minimum visual/auditory acuity to judge the content.
- B) Teach them to use editing software.
- C) Determine who is most expert in compression standards.
- D) Select them by age and education only.

**Answer:**

A. Screening ensures minimum sensory ability.

#### Multiple Choice 2

**Question:** What best describes the *Full-Reference* (FR) objective approach?

**Options:**

- A) It requires the original undistorted signal to compare with the processed one.
- B) It evaluates only from the compressed bitstream, with no reference.
- C) It uses AI to "hallucinate" the original.
- D) It relies on the viewer's subjective opinion.

**Answer:**

A. Full-reference metrics require the original signal.

#### Multiple Choice 3

**Question:** Why is statistical analysis critical in subjective evaluation?

**Options:**

- A) To convert ratings into bitrate requirements.
- B) To ignore data contradicting the initial hypothesis.
- C) To remove outliers, account for inter-subject variability, and make the MOS statistically significant.
- D) To reduce the number of participants to zero.

**Answer:**

C. Statistics handle outliers, variability, and MOS significance.
## 12. Adaptive Streaming Systems

Primary source: [[sources/src-013-multimedia-communications-course-pdf#Point references|SRC-013, pp. 41-45]].

### Core Block Schemes

```text
push real-time:
  sender/server -> RTP/RTCP over UDP -> receiver
  goal: low latency, sender-side control

pull adaptive streaming:
  client reads MPD/manifest
  -> estimates throughput and buffer
  -> requests next HTTP segment
  -> updates state
  -> repeats
```

```text
DASH asset:
  MPD
    -> Period
      -> AdaptationSet
        -> Representation
          -> Segments
```

### Open-Ended Questions And Answers

#### Open Question 1

**Question:**  Describe the fundamental architectural differences between *Push-based* streaming (e.g. RTP/UDP) and *Pull-based* (e.g. DASH).

**Answer:**

Push-based streaming sends media continuously from server to receiver, typically over UDP/RTP with control through RTCP or WebRTC mechanisms. It targets low latency and interactive use. Pull-based streaming such as DASH lets the client request segments over HTTP. It targets scalability, CDN caching, and client-side adaptation rather than minimum latency.

#### Open Question 2

**Question:** Analyze the role of the *client-side buffer* in the context of stability and QoE.

**Answer:**

The client-side buffer absorbs throughput variations and network jitter. When the buffer is healthy, playback continues even if one segment download is slow. When it reaches zero, playback stalls, which is highly damaging for QoE. A larger buffer improves stability but increases latency and slows adaptation; a smaller buffer lowers delay but risks stalls.

#### Open Question 3

**Question:** Define the *Switching Penalty* and discuss its impact on perceived video quality.

**Answer:**

Switching penalty is the perceived annoyance caused by frequent or large quality changes. Users often prefer slightly lower stable quality over rapid oscillation between high and low quality. ABR algorithms therefore should not maximize only instantaneous bitrate; they must balance average quality, stall avoidance, and smoothness.

#### Open Question 4

**Question:** Explain the evolution of the playout buffer level $B(t)$ with a mathematical model ($\frac{dB}{dt} = C(t) - R(t)$): describe the playback (draining) phase and the rebufferization (stalling) phase.

**Answer:**

Buffer evolution has two phases. During playback, the buffer fills according to download speed but drains at one second per second of video played. A compact model is `dB/dt = S/R_C - 1`, where `S` is throughput and `R_C` is coding rate. During rebuffering, playback is stopped, so the output drain is zero and `dB/dt = S/R_C`. This creates the saw-tooth behavior emphasized in the course: download raises buffer, playback drains it, and stalls occur when it reaches zero.

#### Open Question 5

**Question:** Explain what the MPD manifest is in DASH and how the client uses it to build segment requests.

**Answer:**

The MPD is the DASH manifest. It tells the client what periods, adaptation sets, representations, bitrates, codecs, resolutions, and segment URLs exist. At the start, the client reads the MPD, chooses an initial representation, downloads initialization data if needed, then requests media segments. During playback it changes representation at segment boundaries based on buffer and throughput.

#### Open Question 6

**Question:**  Explain how an ABR (Adaptive Bitrate) algorithm works: rate-based vs buffer-based logic, and the risk of overestimating available bandwidth.

**Answer:**

ABR estimates what quality level can be downloaded safely. Rate-based logic uses recent throughput estimates and chooses a representation below available bandwidth, often with a safety margin. Buffer-based logic uses buffer occupancy: low buffer means conservative bitrate, high buffer permits higher bitrate. If bandwidth is overestimated, the client requests segments too large to arrive on time, the buffer drains, and stalls occur.

### Multiple Choice Questions And Answers

#### Multiple Choice 1

**Question:** Main motivation for using HTTP-based protocols for video streaming:

**Options:**

- A) Traverse firewalls/NAT using standard web ports (80/443).
- B) Sub-millisecond latency for real-time interaction.
- C) Exclusively reserved bandwidth.
- D) Eliminate all client-side buffering.

**Answer:**

A. HTTP streaming works well with standard web ports and infrastructure.

#### Multiple Choice 2

**Question:** Consequence of an ABR algorithm that systematically overestimates bandwidth:

**Options:**

- A) The client requests segments that cannot be delivered in time → buffer depletion and stalls.
- B) The server increases the link capacity.
- C) Quality improves with no impact on stability.
- D) The MPD is dynamically rewritten.

**Answer:**

A. Overestimating bandwidth causes late segments and stalls.

#### Multiple Choice 3

**Question:** Metric that is a direct indicator of streaming QoE from the end-user's perspective:

**Options:**

- A) Frequency and total duration of playback interruptions (rebuffering).
- B) Number of lost IP packets.
- C) Maximum bit-rate supported by the server.
- D) Browser/app version.

**Answer:**

A. Rebuffering frequency and duration directly affect QoE.

#### Multiple Choice 4

**Question:** At what stage of the session lifecycle does a DASH client process the MPD?

**Options:**

- A) At the start of the session, to acquire the map of available representations.
- B) After every single rendered segment.
- C) Only when the connection is lost.
- D) On request from the authentication server.

**Answer:**

A. The client processes the MPD at session start to learn available representations.

## Cross-Topic Exam Blocks

These block schemes recur across many answers and are worth memorizing more than isolated formulas.

```text
generic lossy codec:
  source -> decorrelation/sparsification -> quantization -> entropy coding
         -> bitstream -> entropy decoding -> inverse quantization -> reconstruction
```

```text
hybrid video:
  prediction from space/time -> residual -> transform -> quantization -> entropy coding
                         ^                                      |
                         |                                      v
                  reconstructed reference frame buffer <- inverse path
```

```text
perceptual coding:
  signal analysis -> perceptual model -> bit allocation -> quantization
```

```text
adaptive streaming:
  encoded representations + MPD + segments
        -> client measurement of throughput/buffer
        -> representation choice
        -> segment request
        -> QoE outcome
```

## Known Gaps In The Question File

- The JPEG 8x8 numerical coefficient table is not included, so only the coding procedure can be answered without inventing coefficients.
- The DWT 4x4 block for the EZW numerical pass is not included, so the exact SP/SN/IZ/ZR sequence cannot be computed without inventing coefficients.
- Modern claims about JPEG AI gains and exact standard status are treated as course-source claims from SRC-013, not externally verified facts.
