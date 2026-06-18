# Multimedia Communications — Exam Questions (complete set)

**Course:** Multimedia Communications — Marco Cagnazzo
**Goal:** cover the whole program (`Lessons/ 1–12`). Merges the questions from `MM_COMM_sample_questions.pdf` and `questionsMM.pdf` with extra questions covering the topics absent (or only touched) in the PDFs.

## Legend
- `[PDF]` = question present in the professor's sample file (`MM_COMM_sample_questions.pdf`).
- `[Q2]` = question present in the professor's second set (`questionsMM.pdf`), not already covered by the first.
- `[+]` = extra question (same style as the professor's).
- Question-type tags: **🧩 block diagram** · **⚖️ comparison** · **📐 principle/explanation** · **🔢 numerical exercise** · **✅ multiple choice**.

> **Coverage note.** The original PDFs cover well: Quantization, Lossless, Transform/JPEG, Motion Estimation, Video Coding, Modern standards, Audio, Quality, Streaming. **Missing** were dedicated sections on: **(1) Introduction, perception and quality metrics (L1)**, **(2) Wavelet analysis / JPEG2000 DWT side (L5)**, **(3) Learned Image Compression (L6)**. Sections 1, 5, 6 below fill these gaps.

---

# 1. Introduction, Perception and Quality Metrics  *(L1 — gap in the PDF)*

## Open-Ended

1. `[+]` **📐** Describe the three types of redundancy exploited by compression (statistical, psychovisual, semantic) and give a concrete example of each.
2. `[+]` **📐** Explain the *Contrast Sensitivity Function* (CSF): what it is, in which units spatial frequency is measured, where it peaks, and the direct implication for quantization in compression.
3. `[+]` **📐** Explain *masking* in the auditory system: define frequency masking and temporal masking (pre/post-masking) with their time-scale orders of magnitude.
4. `[+]` **📐** What is the *critical band* and how does it relate to the audibility condition of a set of sinusoids close in frequency?
5. `[+]` **⚖️** Compare cones and rods (number, function, lighting conditions) and explain why the RGB→Y conversion weights the green component the most.
6. `[+]` **📐** Explain the `J:a:b` chroma subsampling notation. Compute the data-reduction factor of 4:2:0 vs full RGB and justify why it is perceptually acceptable.
7. `[+]` **⚖️** Compare MSE/PSNR, SSIM and LPIPS: what each measures, pros/cons, and why two images with the **same MSE** can have very different perceived quality.
8. `[+]` **🧩** Draw the *Basic Tools for Compression* scheme (Transform → Prediction → Quantization → Entropy Coding) and indicate which stage is the **only lossy** one and why.
9. `[+]` **📐** Define the three SSIM components (luminance, contrast, structure), explain how they combine and the range of the result.
10. `[+]` **📐** What is meant by *machine-centric multimedia* / *task-oriented communication*, and how does the compression objective change vs the human-centric case?
11. `[Q2]` **📐⚖️** *Principles of image compression.* Discuss the criteria for evaluating a compression algorithm: **rate** and **quality** (PSNR/SSIM/LPIPS), and as a bonus the three extra axes **robustness**, **delay**, **complexity**. Explain the design tensions (e.g. ↑quality vs ↓rate, ↑robustness vs ↓complexity).

## Multiple Choice

1. `[+]` **✅** The HVS Contrast Sensitivity Function peaks:
   - A) At very low spatial frequencies.
   - B) **At mid spatial frequencies (~2–5 cycles/degree).**
   - C) At very high spatial frequencies.
   - D) It is constant across frequencies.
2. `[+]` **✅** PSNR for 8-bit images is defined as:
   - A) $10\log_{10}(255^2/\text{MSE})$ **(correct)**
   - B) $20\log_{10}(\text{MSE}/255)$
   - C) $10\log_{10}(\text{MSE})$
   - D) $255^2/\text{MSE}$
3. `[+]` **✅** Why is chroma subsampling (4:2:0) applied, and not luma subsampling?
   - A) Because chroma takes more bits than luminance.
   - B) **Because the HVS is much more sensitive to luminance than to chrominance variations.**
   - C) Because luminance is not compressible.
   - D) To avoid blocking artifacts.

---

# 2. Scalar and Predictive Quantization  *(L2)*

## Open-Ended

1. `[PDF]` **⚖️** Explain the difference between a *mid-tread* and a *mid-rise* quantizer in the context of uniform quantization of signed data.
2. `[PDF]` **📐** Define the concept of a *deadzone* in a quantizer and explain why it is frequently used in lossy compression systems.
3. `[PDF]` **📐** Why is scalar quantization alone often insufficient to compress non-sparse data effectively?
4. `[PDF]` **📐** What is the condition for a predictive quantization system to be effective, and how is the *coding gain* defined?
5. `[PDF]` **🧩** Draw the scheme of a linear predictive quantization system and motivate the structure, with particular attention to the *decoding loop on the encoder side* (the predictor must be fed the same data at encoder and decoder to avoid drift).
6. `[+]` **🔢** In high-resolution uniform quantization, derive/justify the "+6 dB SNR per extra bit" rule ($\text{SNR} \approx 6.02\,R + \text{const}$).
7. `[+]` **📐** Explain the *screening effect*: why does the prediction gain saturate as the linear predictor order $P$ increases?
8. `[+]` **⚖️** Compare scalar and predictive (DPCM) quantization in terms of the variance of the signal sent to the quantizer and SNR at equal rate.
9. `[Q2]` **🔢** *Zero-mean Gaussian signal with autocorrelation $r_X(n-m)=\sigma^2\rho^{|n-m|}$.* (a) With predictor $V(n)=X(n-1)$, for which values of $\rho$ is the prediction gain positive? (b) Optimal linear predictor ($\underline a=-R_X^{-1}\underline r$) of **order $P=1$**: find it, compute the prediction gain and compare with (a). (c) Compute the optimal predictor of **order $P=2$** and compare with the previous cases. *(Full solution of (a)-(b) in numerical exercises Ex 2.2–2.3; for (c) use $R_X=\begin{psmallmatrix}1&\rho\\\rho&1\end{psmallmatrix}\sigma^2$, $\underline r=[\rho,\rho^2]^T\sigma^2$ → $a_1=-\rho,\ a_2=0$: the 2nd tap is zero because an AR(1) is already fully "explained" by an order-1 predictor.)*

## Multiple Choice

1. `[PDF]` **✅** Primary purpose of the predictor in a predictive quantization system:
   - A) **Reduce variance / increase sparsity by exploiting inter-sample correlation.**
   - B) Increase the signal's dynamic range to match the quantizer levels.
   - C) Perform transform coding on the whole block.
   - D) Completely eliminate quantization noise.
2. `[PDF]` **✅** If the prediction $v(n)$ is nearly equal to $x(n)$, what happens to the variance of $y(n)$ sent to the quantizer?
   - A) **It becomes very small compared to the variance of $x(n)$.**
   - B) It stays identical.
   - C) It increases greatly.
   - D) It becomes undefined.
3. `[PDF]` **✅** As the predictor order $P$ increases, the prediction-error variance typically:
   - A) **Decreases with diminishing returns (screening effect): immediate neighbors already capture almost all the information.**
   - B) Increases linearly with the order.
   - C) Always requires high orders for any gain.
   - D) Does not depend on the order.
4. `[PDF]` **✅** In high-resolution uniform quantization, the approximate relationship between SNR and rate $R$:
   - A) **+6 dB SNR per extra bit.**
   - B) SNR decreases linearly with rate.
   - C) SNR constant.
   - D) SNR grows as $R^2$.

---

# 3. Lossless Coding  *(L3)*

## Open-Ended

1. `[PDF]` **⚖️** Explain the difference between *Fixed-Length Coding* (FLC) and *Variable-Length Coding* (VLC) and why VLC is theoretically superior for non-equiprobable sources.
2. `[PDF]` **📐** Discuss the importance of the *prefix condition* in VLC and how it relates to instantaneous decodability.
3. `[PDF]` **⚖️** Explain the mechanism of Arithmetic Coding and why it is often preferred over Huffman in practical, high-performance applications.
4. `[PDF]` **📐** What are the two distinct mechanisms by which *block coding* improves lossless compression efficiency?
5. `[PDF]` **⚖️** Provide a synthetic comparison of the main lossless coding techniques (Exp-Golomb, Huffman, Arithmetic, Dictionary, Neural) in terms of complexity and latency, with a typical use case for each.
6. `[PDF]` **🔢** Describe the principle of Huffman coding. For the following distribution compute the optimal code and compare the average length to the source entropy: A=35%, B=10%, C=7%, D=8%, E=12%, F=28%.
7. `[+]` **📐** State Shannon's *Source Coding Theorem* (bounds on average length $\bar{L}$ vs entropy $H$) and what it guarantees.
8. `[+]` **📐** Explain Exp-Golomb coding: for which source statistics it is suited and why it is used in video standards for syntax elements.
9. `[+]` **🔢** For a binary source with parameter $p$, write $H(p)$, sketch the curve qualitatively and indicate where it is max/min.
10. `[Q2]` **🔢** *Source with A,B,C,D,E,F and probabilities $p_A=0.30,\ p_B=0.10,\ p_C=0.05,\ p_D=0.18,\ p_E=0.15,\ p_F=0.22$.* (a) Describe the Huffman algorithm. (b) Build the Huffman code for this distribution. (c) Compare the average length to the entropy. *(Same method as Ex 3.1 but different numbers: $H\approx2.42$ bit/sym; construction: always merge the two least probable symbols.)*

## Multiple Choice

1. `[PDF]` **✅** Kraft's inequality for the existence of a prefix code with lengths $\{l_1,\dots,l_M\}$:
   - A) **$\sum_{i=1}^M 2^{-l_i} \le 1$**
   - B) $\sum 2^{-l_i} > 1$
   - C) $\sum l_i \le 1$
   - D) $\prod 2^{-l_i} \le 1$
2. `[PDF]` **✅** Behavior of the entropy $H(X)$ of a binary variable with probability $p$:
   - A) Independent of $p$.
   - B) Maximum at $p=0$ or $p=1$.
   - C) Minimum at $p=0.5$.
   - D) **Maximum at $p=0.5$, tends to 0 as $p\to 0$ or $p\to 1$.**
3. `[PDF]` **✅** Why is Lempel-Ziv (LZW) considered "universal"?
   - A) **It requires no prior knowledge of the source statistics/probabilities.**
   - B) It produces fixed-length codewords.
   - C) It is optimal for every finite sequence.
   - D) It uses a static hardcoded dictionary.
4. `[+]` **✅** Huffman's overhead vs the per-symbol entropy (integer-bit rounding penalty) is at most:
   - A) **< 1 bit/symbol.**
   - B) Exactly 2 bit/symbol always.
   - C) 0 bits always.
   - D) Grows unboundedly with the alphabet size.

---

# 4. Transform Coding and JPEG  *(L4)*

## Open-Ended

1. `[PDF]` **📐** Explain the role of the *geometric mean of the variances* in transform coding and how it relates to the coding gain $G_T$.
2. `[PDF]` **📐** Describe the *frequency leakage* problem of the DFT applied to compression and how the DCT solves it.
3. `[PDF]` **📐** Explain the entropy coding process for AC coefficients in JPEG and the meaning of the *End of Block* (EOB) symbol.
4. `[PDF]` **🧩** Draw the scheme and describe the functional blocks of a JPEG encoder.
5. `[PDF]` **⚖️** Compare JPEG's block-DCT approach with JPEG2000's wavelet decomposition regarding how they handle the image signal and the resulting artifacts (blocking vs ringing).
6. `[PDF]` **⚖️** Explain the fundamental shift in Rate-Distortion optimization from classical codecs (JPEG) to neural methods.
7. `[PDF]` **🔢** Describe the JPEG lossless coding process applied to the given table of quantized DCT coefficients (8×8 matrix with values 10, 3, -2, 1, … and zeros): zig-zag scan, run-length and EOB.
8. `[+]` **📐** Explain why the KLT is the optimal linear transform for decorrelation and why the DCT is used in practice instead.
9. `[+]` **📐** Explain how optimal *bit allocation* (e.g. Huang-Schultheiss) distributes bits among coefficients as a function of their variances.
10. `[Q2]` **📐🔢** *Write the resource allocation problem for transform coding and derive the Huang-Schulteiss formula.* Set up $\min_R \frac1M\sum_k c_k\sigma_k^2 2^{-2R_k}$ subject to $\sum_k R_k\le R_{Tot}$; solve via the Lagrangian ($\partial J/\partial R_k=0$) and impose the constraint to obtain $R_k^*=\frac{R_{Tot}}{M}+\frac12\log_2\frac{c_k\sigma_k^2}{c_{GM}\sigma_{GM}^2}$. Comment: more bits to higher-variance components, equal per-component distortion at the optimum.

## Multiple Choice

1. `[PDF]` **✅** Primary purpose of an orthogonal transform in transform coding:
   - A) **Sparsify the signal by concentrating energy in few large coefficients.**
   - B) Increase the signal variance.
   - C) Make the components statistically dependent.
   - D) Reduce the total signal energy before quantization.
2. `[PDF]` **✅** Role of the *quantization table* in JPEG:
   - A) Compute the inverse DCT at the decoder.
   - B) It is a fixed, mandatory table imposed by the standard.
   - C) It performs the frequency analysis of the blocks.
   - D) **It defines the rate-distortion trade-off by setting the resolution for each DCT coefficient.**
3. `[PDF]` **✅** Relationship between arithmetic mean (AM) and geometric mean (GM) of variances under an orthogonal transform:
   - A) **Any orthogonal transform preserves the AM but may alter the GM.**
   - B) It alters both.
   - C) It preserves the GM but alters the AM.
   - D) The AM is minimized by the KLT.
4. `[PDF]` **✅** Main advantage of the hierarchical (multiresolution) wavelet decomposition in JPEG2000:
   - A) It removes the need for entropy coding.
   - B) **It enables progressive transmission and scalable reconstruction at multiple resolutions/qualities.**
   - C) It limits analysis to high frequencies.
   - D) It forces 8×8 blocks like JPEG.

---

# 5. Wavelet Analysis and JPEG2000  *(L5 — gap in the PDF)*

## Open-Ended

1. `[+]` **📐** State the *time-frequency uncertainty principle* ($\Delta t \cdot \Delta f \ge 1/4\pi$), explain why it imposes a trade-off, and how wavelets address it with adaptive multiresolution (short windows at high frequencies, long at low frequencies).
2. `[+]` **⚖️** Compare STFT (rigid tiling) and DWT (adaptive tiling) of the time-frequency plane, linking them to the *trends vs anomalies* image model.
3. `[+]` **🧩** Draw the scheme of a 1D two-channel filter bank (analysis: $h_0$ LP + $h_1$ HP + decimation ↓2; synthesis: ↑2 + $f_0,f_1$) and indicate where the approximation and detail coefficients arise.
4. `[+]` **📐** State the *Perfect Reconstruction* conditions in the Z-domain (no distortion + aliasing cancellation) and explain what each term represents.
5. `[+]` **📐** What are the *vanishing moments* of a filter and how do they relate to sparsity (number of taps ≥ 2p) and the ability to represent polynomials?
6. `[+]` **📐** Explain the *border problem* for finite-support signals and compare the three solutions (zero padding, periodization, symmetrization). Why is a symmetric filter needed?
7. `[+]` **⚖️** Why are biorthogonal filters (CDF 9/7, 5/3) preferred over orthogonal ones in compression? Cite the fundamental constraint ("the only orthogonal, symmetric, FIR filter is Haar").
8. `[+]` **🧩** Describe a one-level separable 2D-DWT decomposition: the 4 subbands LL/HL/LH/HH, what each contains, and how multiresolution is obtained (recursive decomposition of LL). How many levels are optimal and why?
9. `[+]` **📐** Explain the principle of EZW coding: zero-tree structure, inter-scale self-similarity, the 4 symbols (SP/SN/IZ/ZR), and why a single ZR symbol saves many codes. What is quality scalability (bitplane coding)?
10. `[+]` **🔢** Given a small 4×4 block of DWT coefficients, perform an EZW *dominant pass* and *refining pass* with initial threshold $T = 2^{\lfloor \log_2 \max|c| \rfloor}$.
11. `[+]` **🧩** Describe the JPEG2000 architecture (Tier 1: DWT 9/7 or 5/3 → fine quantization → arithmetic coding of codeblocks per bitplane; Tier 2: EBCOT). Where does the lossy operation actually happen?
12. `[+]` **📐** Explain EBCOT's Rate-Distortion optimization with the Lagrange multiplier: optimal truncation condition ($\partial D_i/\partial R_i = -\lambda$, same slope for all codeblocks) and how quality layers arise.
13. `[+]` **⚖️** Compare JPEG and JPEG2000 on channel-error robustness (codeblock independence, contained vs catastrophic propagation, resynchronization markers).

## Multiple Choice

1. `[+]` **✅** The only filter that is simultaneously orthogonal, symmetric and FIR is:
   - A) Daubechies 9/7
   - B) **Haar**
   - C) CDF 5/3
   - D) No FIR filter.
2. `[+]` **✅** For lossless coding in JPEG2000 the wavelet used is:
   - A) Daubechies 9/7 (real-valued taps).
   - B) **Daubechies 5/3 (integer taps → exact reconstruction).**
   - C) 8×8 DCT.
   - D) 1-tap Haar.
3. `[+]` **✅** In EBCOT, at the optimal codeblock truncation:
   - A) All codeblocks get the same rate.
   - B) **All codeblocks have the same slope $\partial D/\partial R = -\lambda$ on their R-D curve.**
   - C) Truncation occurs at the first bitplane.
   - D) The total rate cannot be controlled.
4. `[+]` **✅** A filter with $p$ vanishing moments:
   - A) **Does not respond to polynomial inputs of degree $< p$ → zero details on smooth regions.**
   - B) Has exactly $p$ taps.
   - C) Is always orthogonal.
   - D) Increases the blocking artifact.

---

# 6. Learned Image Compression (Neural)  *(L6 — gap in the PDF)*

## Open-Ended

1. `[+]` **⚖️** Compare the classical paradigm (hand-crafted linear transforms: DCT/DWT) with the neural one (non-linear transforms learned end-to-end). What changes regarding linearity and adaptivity?
2. `[+]` **📐** Explain why NIC can be seen as a *non-linear KLT optimized for R-D*. Which limits of the KLT does it overcome?
3. `[+]` **🧩** Draw the compression autoencoder scheme: Analysis $g_a$ → quantization $Q$ → entropy coding → Synthesis $g_s$. Indicate what the *latents* are and where compression happens.
4. `[+]` **📐** Write and interpret the Rate-Distortion VAE loss $\mathcal{L} = R + \lambda D$ (rate as KL-divergence, distortion as reconstruction error). What does $\lambda$ control?
5. `[+]` **⚖️** Why compress in the *latent space* instead of pixel space? (decorrelation, Gaussianized distributions, quantization noise hidden in low-perceptual channels).
6. `[+]` **📐** Explain the *non-differentiability problem* of quantization (staircase function, zero derivative) and why it blocks backpropagation.
7. `[+]` **📐** Describe the *Additive Uniform Noise* solution $\mathcal{U}(-0.5, 0.5)$ during training (vs rounding at test time) and its theoretical grounding. Also mention STE and soft quantization as alternatives.
8. `[+]` **📐** What is *GDN* (Generalized Divisive Normalization)? Write the formula, explain lateral inhibition, the link to HVS masking, and the Gaussianization useful for entropy coding. Why is it better than ReLU for compression?
9. `[+]` **🧩** Explain the *Scale Hyperprior* (Ballé 2018): why it is needed, how a second autoencoder ($h_a, h_s$) transmits side-information $\hat z$ to predict the $\sigma$ of the latents' conditional prior, and the impact on the total rate.
10. `[+]` **⚖️** Explain why CNNs outperform MLPs in image compression (local connectivity, weight sharing, translation invariance, MLP parameter explosion).
11. `[+]` **📐** What are *transposed convolutions* and why are they needed in the decoder (learned upsampling, 1-to-N / overlap & sum mechanism)?
12. `[+]` **⚖️** JPEG-AI: goals (beat VVC-Intra by ~50%), backbone (hierarchical VAE with hyperprior), *dual-use* human/machine support, and complexity profiles (Dec0/Dec1/Dec2, kMAC/px). Cite pros/cons vs classical codecs (R-D vs computational cost, determinism, hallucinations).

## Multiple Choice

1. `[PDF]` **✅** Main purpose of adding additive uniform noise during the training of a neural codec:
   - A) **Make the (staircase) quantization differentiable to enable backpropagation.**
   - B) Increase spatial resolution.
   - C) Filter out high-frequency noise.
   - D) Simulate channel errors on the latents.
2. `[PDF]` **✅** Why do CNNs outperform MLPs in image compression?
   - A) **Local connectivity and weight sharing reduce parameters and enforce translation invariance.**
   - B) MLPs do not perform non-linear activation.
   - C) CNNs are linear.
   - D) MLPs need far more data for the same image.
3. `[+]` **✅** GDN is used to:
   - A) Replace motion compensation.
   - B) **Normalize features by local energy (lateral inhibition) and Gaussianize the latents for entropy coding.**
   - C) Increase the bit-rate by adding redundancy.
   - D) Convert the image to the frequency domain with the DCT.
4. `[+]` **✅** In the Scale Hyperprior, the side-information $\hat z$ serves to:
   - A) Directly reconstruct the pixels.
   - B) **Predict the standard deviation $\sigma$ of the latents' conditional prior at each spatial location.**
   - C) Replace quantization.
   - D) Remove the decoder.
5. `[+]` **✅** A risk of neural codecs absent in classical codecs is:
   - A) The blocking artifact.
   - B) **Decoder drift / cross-platform non-determinism (float) and hallucinations on out-of-distribution inputs.**
   - C) The lack of entropy coding.
   - D) Lossless support.

---

# 7. Motion Estimation  *(L7)*

## Open-Ended

1. `[PDF]` **⚖️** Describe the difference between *motion field* and *optical flow*.
2. `[PDF]` **📐** Explain the core principle of the Horn & Schunck algorithm for dense optical flow estimation (data-attachment term from the optical-flow equation + regularization term enforcing smoothness, solved with a Lagrange multiplier).
3. `[PDF]` **⚖️** Discuss the Rate-Distortion trade-off in choosing the block size in motion estimation.
4. `[+]` **📐** Derive the *optical flow equation* ($u f_x + v f_y + f_t = 0$) from the constant-illumination hypothesis and explain the *aperture problem*.
5. `[+]` **⚖️** Compare the SAD, SSD and MAD matching criteria: computational cost, outlier sensitivity, motion-field regularity.
6. `[+]` **⚖️** Compare Full Search and fast searches (Three-Step, Hexagon, Diamond): number of tested vectors vs optimality.
7. `[Q2]` **📐** *Block matching: give the principles of the approach, at least one cost function, and [bonus] discuss the regularization issue.* Explain the regularized cost $J_{REG}(i,j)=\|\mathbf f_k-\mathbf f_h\|_p^p+\lambda R(i,j)$ (penalizes vectors too different from neighbors) and $J(v)=d(v)+\lambda_{ME}\,r(v)$ (MV rate): why it is needed (more regular MVF, lower coding cost) and the effect of $\lambda_{ME}$.

## Multiple Choice

1. `[PDF]` **✅** Disadvantage of using SSD as a matching criterion:
   - A) **It is outlier-sensitive and involves multiplications → higher complexity and irregular motion fields.**
   - B) It does not compute the prediction-error energy correctly.
   - C) It produces a more regular field than SAD.
   - D) Impossible to use in iterative searches.
2. `[PDF]` **✅** Main benefit of the Hexagon Search vs Full Search:
   - A) Always guarantees the global minimum.
   - B) Only for affine motion models.
   - C) Removes sub-pixel interpolation.
   - D) **Greatly reduces the number of tested vectors while keeping near-optimal performance.**
3. `[PDF]` **✅** What does an affine motion model allow that a purely translational one does not?
   - A) Fewer parameters and more noise robustness.
   - B) **It can represent rotation, zoom and shear with six parameters.**
   - C) It forces the same vector for all pixels.
   - D) It computes motion without a reference image.

---

# 8. Video Coding Principles  *(L8)*

## Open-Ended

1. `[PDF]` **📐** Why is the temporal prediction error usually more efficient to encode than the original video signal?
2. `[PDF]` **📐** Describe the function of the *Mode Selection* step in a hybrid video encoder.
3. `[PDF]` **📐** How does the *Channel Buffer* controller manage the trade-off between target rate and video quality (raising/lowering the quantization step based on buffer occupancy)?
4. `[+]` **🧩** Draw the block diagram of a hybrid video encoder (motion estimation/compensation + DCT + quantization + entropy coding + reconstruction loop with frame buffer). Explain why the encoder contains an internal decoder.
5. `[+]` **📐** Explain the GOP structure and I/P/B frame types: role, dependencies, and impact on compression, random access and latency.
6. `[+]` **📐** What is the *Median Predictor* for motion vectors and how does coding only the MVD (difference) exploit the spatial correlation of vectors?
7. `[Q2]` **📐** *Describe the intra-coding modes in H.264. [Optional] Discuss also the Intra modes in H.265.* H.264: directional intra prediction on 4×4/16×16 luma blocks from already-decoded neighboring pixels — 9 modes for 4×4 (DC + 8 directional), 4 for 16×16; the predicted residual is then transformed/quantized. H.265/HEVC: **35 modes** (DC, Planar + 33 directional) on variable-size blocks (CU/PU up to 32×32), with finer angular prediction.
8. `[Q2]` **🧩📐** *Describe the principle of the H.264 deblocking in-loop filter.* An adaptive filter applied to the edges of 4×4 blocks/macroblocks **inside the reconstruction loop** (before writing the frame to the reference buffer). It reduces blocking artifacts due to block-based quantization; the boundary strength and intensity depend on the value jump at the edge and on coding parameters; it operates on luma and chroma. It improves subjective quality and, being in the loop, also the prediction of subsequent frames.

## Multiple Choice

1. `[PDF]` **✅** Primary role of an *I-frame* in a GOP structure:
   - A) **Provide a random-access point and terminate temporal error propagation.**
   - B) Highest compression ratio via spatial prediction.
   - C) Store only the motion vectors.
   - D) Temporary buffer for B-frames.
2. `[PDF]` **✅** Why is a *Median Predictor* (MVP) used in motion vector coding?
   - A) **To exploit the spatial correlation between adjacent vectors and reduce the MVD bit-rate.**
   - B) To compute the background motion better than the foreground.
   - C) To force all vectors identical.
   - D) To increase complexity and avoid overfitting.
3. `[PDF]` **✅** What does the decoder do when it receives an *Inter-coded* block?
   - A) **It decodes the motion vector and prediction error, then adds them to the block from the reference frame.**
   - B) It discards the frame and requests retransmission.
   - C) It runs a new motion-estimation search.
   - D) It uses only spatial filtering.

---

# 9. Modern Video Compression Standards  *(L9)*

## Open-Ended

1. `[PDF]` **📐** What is the specific scope of video compression standards like H.266/VVC?
2. `[PDF]` **📐** Explain the advantage of the *Coding Tree Unit* (CTU) structure introduced in HEVC/VVC (flexible recursive partitioning, large blocks for homogeneous areas and small ones for textures/edges).
3. `[PDF]` **📐** What are the roles of VCL and NAL in modern video standards?
4. `[+]` **⚖️** Compare macroblocks (H.264) and CTU/quad-tree (HEVC/VVC) in terms of R-D efficiency at high resolution.
5. `[+]` **📐** Explain the principle of CABAC: context modeling, binarization, and context-adaptive binary arithmetic coding. Why does it beat Huffman/CAVLC?

## Multiple Choice

1. `[PDF]` **✅** Main purpose of the CABAC entropy coder in modern standards:
   - A) **Adaptively assign shorter bit sequences to more frequent symbols based on context.**
   - B) Convert the image to the frequency domain.
   - C) Replace motion compensation.
   - D) Increase the bit-rate by adding redundancy for error correction.
2. `[PDF]` **✅** Why are *Tiles* "hardware-friendly" in VVC/HEVC?
   - A) **They allow independent processing of rectangular regions → parallel encoding/decoding.**
   - B) They improve the quality of moving objects.
   - C) They remove the need for entropy coding.
   - D) They force the use of a single core.
3. `[PDF]` **✅** Function of an *In-Loop Filter* like the Adaptive Loop Filter (ALF):
   - A) **Reduce quantization artifacts and restore details at reconstruction (clean frame in the reference buffer).**
   - B) Speed up motion estimation.
   - C) Generate random grain.
   - D) Replace the transform block.

---

# 10. Audio and Speech Compression  *(L10)*

## Open-Ended

1. `[PDF]` **⚖️** Explain the difference between *Source-Based* (parametric) and *Sink-Based* (perceptual) coding.
2. `[PDF]` **📐** Describe the *Analysis-by-Synthesis* (AbS) loop used in CELP codecs and why it improves over simple LPC-10.
3. `[PDF]` **📐** What is the role of the psychoacoustic masking model in perceptual audio coding and how is it used to allocate bits?
4. `[PDF]` **📐** Describe the principles of the LPC-10 speech coding scheme.
5. `[PDF]` **🧩** Draw the scheme and describe the operation of the functional blocks of an MP3 encoder.
6. `[+]` **🧩** Draw the general block diagram of a perceptual audio encoder (filter bank/MDCT in parallel with the psychoacoustic model → bit allocation → quantization → entropy coding).
7. `[+]` **⚖️** Compare speech coding (LPC/CELP, source model) and music coding (MP3/AAC, perceptual): goals, bitrate, quality.

## Multiple Choice

1. `[PDF]` **✅** Why are *Line Spectrum Frequencies* (LSF) preferred over direct quantization of LPC coefficients $a_i$?
   - A) **They guarantee filter stability (roots on the unit circle, interlacing property that can be verified/corrected).**
   - B) They give a higher SNR.
   - C) They need fewer bits because they are positive integers.
   - D) They directly represent the pitch.
2. `[PDF]` **✅** Primary technical advantage of Opus's hybrid design:
   - A) Based only on fixed-rate PCM.
   - B) **It dynamically switches/combines an LPC engine and an MDCT engine to handle speech and music across a wide bitrate range.**
   - C) It uses a psychoacoustic model identical to MP3.
   - D) It avoids all entropy coding.
3. `[PDF]` **✅** Current research trend in the future of multimedia audio coding:
   - A) Abandoning lossy in favor of universal lossless.
   - B) Increasing PCM bit-depth to 64 bits.
   - C) **Moving from signal-processing models to end-to-end deep-learning neural codecs.**
   - D) Replacing packet-based protocols with circuit-switched channels.

---

# 11. Quality Assessment and QoE  *(L11)*

## Open-Ended

1. `[PDF]` **⚖️** Explain the difference between subjective and objective quality evaluation in multimedia systems and why both are necessary.
2. `[PDF]` **📐** What are the key stages in designing a subjective quality test according to standardized guidelines?
3. `[PDF]` **⚖️** Describe the main categories of objective quality metrics based on the availability of the reference signal (Full-Reference, Reduced-Reference, No-Reference).
4. `[+]` **📐** What is the MOS (Mean Opinion Score) and why is statistical analysis needed (outlier removal, confidence intervals, inter-subject variability)?
5. `[+]` **⚖️** Compare QoS and QoE: what they measure and how they correlate. Which network factors impact streaming QoE?

## Multiple Choice

1. `[PDF]` **✅** Main purpose of the *screening* phase of participants in subjective tests:
   - A) **Ensure they have the minimum visual/auditory acuity to judge the content.**
   - B) Teach them to use editing software.
   - C) Determine who is most expert in compression standards.
   - D) Select them by age and education only.
2. `[PDF]` **✅** What best describes the *Full-Reference* (FR) objective approach?
   - A) **It requires the original undistorted signal to compare with the processed one.**
   - B) It evaluates only from the compressed bitstream, with no reference.
   - C) It uses AI to "hallucinate" the original.
   - D) It relies on the viewer's subjective opinion.
3. `[PDF]` **✅** Why is statistical analysis critical in subjective evaluation?
   - A) To convert ratings into bitrate requirements.
   - B) To ignore data contradicting the initial hypothesis.
   - C) **To remove outliers, account for inter-subject variability, and make the MOS statistically significant.**
   - D) To reduce the number of participants to zero.

---

# 12. Adaptive Streaming Systems  *(L12)*

## Open-Ended

1. `[PDF]` **⚖️** Describe the fundamental architectural differences between *Push-based* streaming (e.g. RTP/UDP) and *Pull-based* (e.g. DASH).
2. `[PDF]` **📐** Analyze the role of the *client-side buffer* in the context of stability and QoE.
3. `[PDF]` **📐** Define the *Switching Penalty* and discuss its impact on perceived video quality.
4. `[PDF]` **🔢/📐** Explain the evolution of the playout buffer level $B(t)$ with a mathematical model ($\frac{dB}{dt} = C(t) - R(t)$): describe the playback (draining) phase and the rebufferization (stalling) phase.
5. `[+]` **📐** Explain what the MPD manifest is in DASH and how the client uses it to build segment requests.
6. `[+]` **⚖️** Explain how an ABR (Adaptive Bitrate) algorithm works: rate-based vs buffer-based logic, and the risk of overestimating available bandwidth.

## Multiple Choice

1. `[PDF]` **✅** Main motivation for using HTTP-based protocols for video streaming:
   - A) **Traverse firewalls/NAT using standard web ports (80/443).**
   - B) Sub-millisecond latency for real-time interaction.
   - C) Exclusively reserved bandwidth.
   - D) Eliminate all client-side buffering.
2. `[PDF]` **✅** Consequence of an ABR algorithm that systematically overestimates bandwidth:
   - A) **The client requests segments that cannot be delivered in time → buffer depletion and stalls.**
   - B) The server increases the link capacity.
   - C) Quality improves with no impact on stability.
   - D) The MPD is dynamically rewritten.
3. `[PDF]` **✅** Metric that is a direct indicator of streaming QoE from the end-user's perspective:
   - A) **Frequency and total duration of playback interruptions (rebuffering).**
   - B) Number of lost IP packets.
   - C) Maximum bit-rate supported by the server.
   - D) Browser/app version.
4. `[PDF]` **✅** At what stage of the session lifecycle does a DASH client process the MPD?
   - A) **At the start of the session, to acquire the map of available representations.**
   - B) After every single rendered segment.
   - C) Only when the connection is lost.
   - D) On request from the authentication server.

---

## Program coverage summary

| # | Lesson | In the PDFs? | In this doc |
|---|--------|--------------|-------------|
| 1 | Introduction / Perception / Quality metrics | ❌ absent | ✅ section 1 (new) |
| 2 | Scalar & Predictive Quantization | ✅ | ✅ PDF + extra |
| 3 | Lossless coding | ✅ | ✅ PDF + extra |
| 4 | Transform coding / JPEG | ✅ | ✅ PDF + extra |
| 5 | Wavelet analysis / JPEG2000 | ⚠️ only via JPEG2000 | ✅ section 5 (new) |
| 6 | Learned Image Compression | ⚠️ 3 scattered MCQs | ✅ section 6 (new) |
| 7 | Motion Estimation | ✅ | ✅ PDF + extra |
| 8 | Video Coding Principles | ✅ | ✅ PDF + extra |
| 9 | Modern Video Compression Standards | ✅ | ✅ PDF + extra |
| 10 | Audio Coding | ✅ | ✅ PDF + extra |
| 11 | Quality Assessment & QoE | ✅ | ✅ PDF + extra |
| 12 | Adaptive Streaming | ✅ | ✅ PDF + extra |

> Professor's reminder: the list is **indicative, not exhaustive**; the exam will also include **numerical exercises** and topics not present here. Favor block diagrams, comparisons, and explanation of principles over the mere formula.
