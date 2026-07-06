# 1. Representation and Perception

## Human Eye
CSF = Contrast Sensitivity Funcion, describes how vsible a spatial pattern is as its spatial frequency changes

### Color spaces
**RGB**: an additive color space in which each color is represented by the intensity of red green and blue light.
We use three channels and we have $2^8 = 256$ colors.

**HSV**: perceptual color representation that separates color type (Hue), color purity (saturation) and brightness (value).

**YCbCr**: color representation that separates luminance-like information Y from two chrominance components Cb and Cr. More natural way to identify colors.

#### Frequency Masking Functions
- Strong spectral component makes nearby weaker components difficult or impossible to hear. 
- Specifies hearing threshold.
- We **don't** encode infos that that couldn't be heard.
- If 2 sinwaves $S_m$ are adjacent, we hardly distiguish them.

### Image and Video Representation
Images stored in $N \times M$ matrix.

#### Color sampling
Specifies how many chrominnace samples are retained relative to luminance samples.
Notation used: *J:a:b*, where:
- *J*: horizontal size;
- *a*: chroma samples on first line;
- *b*: chroma samples on second line;
Most used is **4:2:0**, where first row has 2 samples (1-2 + 3-4) and second row reuses the samples (0 further).

#### Compression
Representation of the same source content with fewer bits by removing statistical redundancy and perceptually less important information. 

Basic Tools for Compression scheme:

![[Pasted image 20260629145807.png]]

- Prediction and transform reduce redundancy or concentrate energy;
- **Entropy** is lossless;
- **Quantization** only lossy step -> reduces rate but original cannot be recovered exactly.

**Quantization**:  lossy mapping from continuous set of values to a finite set of reconstruction levels.
- Reduces numvber of bits needed to describe samples  -> quantization error.

#### Quality eval
Define **error image** where given $f$ original image matrix, and $\hat{f}$ the reconstructed one

$$
ε(f, \hat{f} ) = f - \hat{f}
$$
**PSNR**:  logarithmic objective quality measure comparing peak signal power with mean squared reconstruction error.
$$
PSNR(f, \tilde{f}) = 10 \log_{10}\left(\frac{V^2}{D(f, \tilde{f})}\right)
$$


# Compression, Prediction and Lossless Coding

3 types of redundancy:
- **Statistical:** neighboring samples, blocks or frames are correlated;
- **Spatial / temporal**: images and videos contain repeated structures across space and time;
- **Psychovisual**: distortions not perceived by the human visual system can be coarsely quantized.

Compression:
- **Lossless**: output perfect reconstructed, lower compression ratio;
- **Lossy**: decoded output differs from the original, perceptually close, high compression ratio.

**Quantization** is the replacement of each input value with one value selected from a finite reconstruction set.
- It controls the number of symbols, and therefore the number of bits, used to represent samples while introducing a measurable approximation error.
- **Scalar quantization** ≡ we only take a sample at a time, not a vector.
- A **scalar quantizer** processes one sample at a time. It assigns the sample to a quantization cell and represents the entire cell using its reconstruction level or corresponding binary index.

**Rate** is the amount of coded information spent to represent each source sample.
- Measured in bits per sample, or in bits per pixel (bpp) when samples are image pixels; bitrate is in bit/s.

$$
\begin{aligned}
R_{\text{image}} &= \frac{B_{\text{out}}}{N M} \quad [\text{bpp}] \\[6pt]
R_{\text{stream}} &= \frac{B_{\text{out}}}{T} \quad [\text{bit/s}]
\end{aligned}
$$
**Distortion** is the numerical loss introduced by replacing $x(n)$ with its reconstruction $Q(x(n))$. We use MSE to track the error:

$$
\operatorname{MSE}\ d[x(n), Q(x(n))] = |e(n)|^2 = [x(n) - Q(x(n))]^2
$$

For signals of duration $N$:

$$
D = \frac{1}{N} \sum_{n=0}^{N-1} d[x(n), Q(x(n))]
$$

For random signals:

$$
D = \mathbb{E}\left[|X(n) - Q(X(n))|^2\right]
= \mathbb{E}\left[|E(n)|^2\right]
$$

**Uniform Quantization** uses equally spaced thresholds and reconstruction levels.
- Single step size is $\Delta$ -> controls precision and rate
- Smaller steps -> less quantization error, but more bits required.

For signed uniform quantization:
- **Mid-tread**: zero is a reconstruction level. Small values around zero are mapped to zero.
- **Mid-rise**: zero is a decision threshold. Values around zero are mapped to positive or negative non-zero levels.

**Deadzone**: enlarges the interval mapped to zero.
- useful for sparse transform or prediction residuals;
- many small coeffcients become exactly zero and can then be compressed effciently by entropy coding.

**SNR** is the ratio between signal power and error power, expressed in decibels.

**Optimal quantizer:** chooses thresholds and reconstruction levels to minimize an expected distortion for a specified number of levels or rate.

#### Predictive Scalar Quantization

**Predictive scalar quantization** represents the difference between a sample and its prediction rather than quantizing the sample directly.
- If prediction is accurate, the residual has lower variance and can reach the same distortion with fewer bits.
- We want to lower distorsion $D = \sigma_x^2 2^{-2R}$: reduce $\sigma$ or, to keep the same distorsion, lower the rate.

**Sparsification** is the concentration of most signal energy or information into a small number of significant coefficients while the remaining coefficients become small or zero.

**Prediction** estimates the current sample from already available samples. 
We need a v(n) such that y(n) = x(n) ↔ v(n), then the reconstructed ŷ(n) + v(n) = x̂(n).
![[Pasted image 20260629154810.png]]


---

# Lossless Coding

#### Code Types

**Fixed-length code** assigns the same number of bits to every source symbol.
- Simple parsing and constant per-symbol rate.
- Cannot assign shorter descriptions to frequent symbols.
- Assuming all symbols are equally probable.

**Variable-length code** assigns different codeword lengths to different symbols.
- Frequent symbols should receive shorter codewords.
- **Statistical Approach**: use of source entropy $H(x)$, to build an optimal Huffman code.
- **Euristic Approach**: universal coding (LZW).
- **Prefix condition**: each word is not a prefix for other words.
- **Non-equiprobable symbols**.

#### Variable-length codes theorems

**McMillan's Theorem**: The best possible prefix code = the best possible decodable code.

**Kraft's Inequality**: If the equality is verified, we say the code is complete.

$$
\sum_i 2^{-l_i} \leq 1
\quad \Longleftrightarrow \quad
\exists \text{ instantaneous code with lengths } \{l_1, \dots, l_M\}
$$
#### Optimal Code

**Optimal lossless code** minimizes expected codeword length for the source probability distribution while remaining uniquely decodable.

**Shannon's source coding theorem**: entropy is the fundamental average-rate limit for lossless compression.

#### Huffman limits and Arithmetic coding

**Limits of Huffman**:
- Complexity exponential in $K$.
- Joint probability estimation for large blocks is costly and unreliable.
- Cannot handle $H(X) < 1$ efficiently symbol by symbol.

**Arithmetic coding** solves at least the complexity problem: block coding with linear complexity $O(n)$.
- Represents an entire symbol sequence with one fractional interval whose width equals the sequence probability.
- Its average rate can approach entropy without requiring an exponentially large block-code dictionary.

#### Adaptivity and Context-based coding

**Adaptive coding** updates probability estimates while processing the stream.

**Context-based coding** conditions those estimates on already decoded neighboring symbols.

**Adaptivity**: symbol statistics learned during encoding via occurrence counts, updated at both encoder and decoder.

**Context-based**: condition on the $N_S$ previous symbols.
- Reaches the entropy rate $\mathcal{H}$ without massive block sizes.
