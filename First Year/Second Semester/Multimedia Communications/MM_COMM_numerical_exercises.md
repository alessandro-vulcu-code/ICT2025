# Multimedia Communications — Numerical Exercises (with solutions)

**Course:** Multimedia Communications — Marco Cagnazzo
**Purpose:** practice the **numerical exercises** announced by the professor ("the examination will feature numerical exercises"). Every exercise uses formulas and notation taken directly from `Lessons/`. Full worked solution right below each problem.

> **How to use:** cover the solution, work it by hand, then check. Focus on the *types* (they recur), not the exact numbers.

## Index of types (high-probability ones in bold)
1. Perception & metrics — data rate, **PSNR**, chroma, SNR/bit (L1)
2. **Quantization** — R-D, SNR≈6R, **AR(1) prediction gain**, optimal predictor, **drift** (L2)
3. **Lossless** — entropy, **Huffman**, Kraft, arithmetic, Exp-Golomb, conditional entropy (L3)
4. **Transform/JPEG** — **coding gain**, **HS/greedy bit allocation**, KLT, **JPEG quant/zig-zag/DC** (L4)
5. **Wavelet** — **EZW dominant/refining**, EBCOT Lagrange (L5)
6. Motion Estimation — **SAD/SSD**, search complexity, sub-pixel, affine (L7)
7. Audio — **LPC-10/G.729** bitrate, MDCT critical sampling, SMR (L10)
8. **Streaming** — **buffer dynamics**, download time, startup, rebuffering (L12)

---

# 1. Perception and Quality Metrics (L1)

### Ex 1.1 — Uncompressed video data rate 🔢
HD 4:2:0: luminance $1920\times1080$, 2 chrominance $960\times540$, 8 bit/sample, 50 fps. Compute the raw bitrate and the storage of a 2 h movie.

**Solution.**
$$R = (1920\cdot1080 + 2\cdot960\cdot540)\cdot 8 \cdot 50$$
Pixels/frame $= 2{,}073{,}600 + 2\cdot518{,}400 = 3{,}110{,}400$.
$R = 3{,}110{,}400 \cdot 8 \cdot 50 = 1{,}244{,}160{,}000 \approx \mathbf{1.24\ Gbps}$.
2 h storage $= 1.244\times10^9 \cdot 7200 / 8 \approx 1.12\times10^{12}$ bytes $\approx \mathbf{1.12\ TB}$. → motivates compression.

### Ex 1.2 — PSNR from MSE 🔢
8-bit image, MSE $\mathcal{D}=24.05$. Compute PSNR.

**Solution.** $\text{PSNR}=10\log_{10}\frac{255^2}{\mathcal D}=10\log_{10}\frac{65025}{24.05}=10\log_{10}(2703.7)=\mathbf{34.32\ dB}$.
(Matches the course's JPEG example.)

### Ex 1.3 — 4:2:0 reduction ratio 🔢
How much data reduction does 4:2:0 give vs full RGB (4:4:4)?

**Solution.** Per 4 luma px: RGB$=4+4+4=12$ samples; 4:2:0 $=4+1+1=6$ samples. Ratio $=6/12=0.5$ → **50% reduction**.

### Ex 1.4 — SNR vs bits 🔢
High-resolution uniform quantization: how many dB are gained going from 6 to 8 bit/sample?

**Solution.** Rule $\text{SNR}\approx 6R$ dB → $\Delta = 6(8-6)=\mathbf{12\ dB}$ (≈ +6 dB/bit).

---

# 2. Scalar and Predictive Quantization (L2)

### Ex 2.1 — R-D of uniform quantizer of a uniform RV 🔢⭐
$X\sim\mathcal U(-A/2,A/2)$, $A=256$, uniform quantizer with $R=4$ bits. Compute $\Delta$, $L$, $D$, SNR.

**Solution.**
$L=2^R=16$; $\Delta=A/L=256/16=\mathbf{16}$.
$D=\Delta^2/12=256/12=\mathbf{21.33}$.
$\sigma_X^2=A^2/12=65536/12=5461.3$.
$\text{SNR}=10\log_{10}(\sigma_X^2/D)=10\log_{10}(2^{2R})=10\log_{10}256=\mathbf{24.08\ dB}$ ($\approx 6R$). ✓

### Ex 2.2 — AR(1) prediction gain ⭐🔢
AR(1) Gaussian signal, $\mathbb E[X(n)X(m)]=\sigma^2\rho^{|n-m|}$. Predictor $v(n)=x(n-1)$. Compute $G_P$ for (a) $\rho=0.9$, (b) $\rho=0.95$, (c) the $\rho$ threshold for prediction to be worthwhile.

**Solution.**
$\sigma_Y^2=\mathbb E[(X(n)-X(n-1))^2]=2\sigma^2(1-\rho)$.
$G_P=10\log_{10}\frac{\sigma_X^2}{\sigma_Y^2}=10\log_{10}\frac{1}{2(1-\rho)}$.
(a) $\rho=0.9$: $G_P=10\log_{10}(1/0.2)=10\log_{10}5=\mathbf{6.99\ dB}$.
(b) $\rho=0.95$: $G_P=10\log_{10}(1/0.1)=\mathbf{10\ dB}$.
(c) $G_P>0 \Leftrightarrow 2(1-\rho)<1 \Leftrightarrow \boxed{\rho>1/2}$.

### Ex 2.3 — Optimal predictor (Wiener-Hopf), order 1 🔢
Order-1 predictor $v(n)=-a_1 x(n-1)$. Given $r_X(0)=\sigma_X^2$, $r_X(1)=\rho\sigma_X^2$, find $a_1^{opt}$ and $\sigma_{Y,opt}^2$.

**Solution.** $\underline a^{opt}=-R_X^{-1}\underline r$. For $P=1$: $a_1^{opt}=-r_X(1)/r_X(0)=-\rho$.
$\sigma_{Y,opt}^2=\sigma_X^2+\underline r^T\underline a^{opt}=\sigma_X^2+r_X(1)\cdot(-\rho)=\sigma_X^2(1-\rho^2)$.
For $\rho=0.9$: $\sigma_{Y,opt}^2=0.19\,\sigma_X^2$ → $G_P=10\log_{10}(1/0.19)=\mathbf{7.2\ dB}$ (better than the fixed predictor's 6.99 dB).

### Ex 2.4 — Drift: wrong vs correct scheme ⭐
3-bit quantizer, levels $\{-9,-6,-3,0,3,6,9\}$. Input $x=\{10,11,12,13,14,18\}$. Predictor $v(n)=$ prediction of previous sample. Show that the **wrong** scheme (encoder predicts from original $x$) drifts, the **correct** one (encoder predicts from reconstructed $\tilde x$) does not.

**Solution (correct scheme — first steps).**
Step 1: $x=10$, no prediction, error quantized to 9 → $\tilde x=9$.
Step 2: pred $=\tilde x_1=9$; error $=11-9=2$ → quant to 3 → $\tilde x=9+3=12$.
Step 3: pred $=12$; error $=12-12=0$ → quant 0 → $\tilde x=12$.
Step 4: pred $=12$; error $=13-12=1$ → quant 0 → $\tilde x=12$.
Step 5: pred $=12$; error $=14-12=2$ → quant 3 → $\tilde x=15$.
Step 6: pred $=15$; error $=18-15=3$ → quant 3 → $\tilde x=18$.
Encoder and decoder **synchronized** (both predict from $\tilde x$): no drift.
**Wrong scheme:** the encoder predicts from $x$ (10,11,12,…) but the decoder only has $\tilde x=9$ → the decoder stays at 9 while the encoder advances → reconstruction error **grows** over time (drift). Conclusion: the predictor must be fed the **quantized** data.

---

# 3. Lossless Coding (L3)

### Ex 3.1 — Huffman + entropy (the PDF problem) ⭐🔢
Source: A=35%, B=10%, C=7%, D=8%, E=12%, F=28%. Build the optimal Huffman code, compute $\bar L$ and compare to $H$.

**Solution.**
Entropy: $H=-\sum p_i\log_2 p_i$:
$0.35\!\to\!0.530,\ 0.28\!\to\!0.514,\ 0.12\!\to\!0.367,\ 0.10\!\to\!0.332,\ 0.08\!\to\!0.292,\ 0.07\!\to\!0.269$.
$H=\mathbf{2.30\ bit/symbol}$.

Huffman construction (always merge the two smallest):
- C(.07)+D(.08)=.15
- B(.10)+E(.12)=.22
- {CD}(.15)+{BE}(.22)=.37
- F(.28)+A(.35)=.63
- .63+.37=1.0

Codes (one valid assignment):
| Sym | p | Code | len |
|---|---|---|---|
| A | .35 | 01 | 2 |
| F | .28 | 00 | 2 |
| E | .12 | 111 | 3 |
| B | .10 | 110 | 3 |
| D | .08 | 101 | 3 |
| C | .07 | 100 | 3 |

$\bar L=0.35(2)+0.28(2)+(0.12+0.10+0.08+0.07)(3)=1.26+1.11=\mathbf{2.37\ bit/sym}$.
Efficiency $H/\bar L=2.30/2.37=\mathbf{97\%}$; satisfies $H\le\bar L<H+1$. ✓

### Ex 3.2 — Kraft check 🔢
Do lengths $\{2,2,3,3,3,3\}$ (previous exercise) admit a prefix code?

**Solution.** $\sum 2^{-l_i}=2\cdot 2^{-2}+4\cdot 2^{-3}=0.5+0.5=1\le1$. ✓ **Complete** code (equality).

### Ex 3.3 — Binary entropy and the 1-bit penalty 🔢
B/W image: $P(\square)=86.7\%$, $P(\blacksquare)=13.3\%$. (a) $H(X)$. (b) $\bar L$ with single-pixel Huffman. (c) comment.

**Solution.**
(a) $H=-0.867\log_2 0.867-0.133\log_2 0.133=0.867(0.206)+0.133(2.911)=0.178+0.387=\mathbf{0.586\ bpp}$.
(b) 2-symbol alphabet → Huffman gives 1 bit each → $\bar L=\mathbf{1\ bpp}$.
(c) Waste $=1-0.586=0.414$ bpp: per-symbol Huffman cannot go below 1 bit when $H<1$. Need **block coding** or **arithmetic**.

### Ex 3.4 — Two-pixel block coding 🔢
Same image, 2-px blocks with measured probabilities: $\square\square=80\%$, $\blacksquare\blacksquare=10\%$, $\square\blacksquare=5\%$, $\blacksquare\square=5\%$. Huffman codes: `1`, `00`, `010`, `011`. Compute $\bar L$ per pixel.

**Solution.**
$\bar L_{block}=0.80(1)+0.10(2)+0.05(3)+0.05(3)=0.80+0.20+0.15+0.15=1.30$ bit/block.
Per pixel: $\bar L_S=1.30/2=\mathbf{0.65\ bpp}$ (vs 1.0 single-pixel; block limit $H/2=0.511$). Improves toward entropy.

### Ex 3.5 — Conditional entropy (context coding) 🔢
Previous pixel as context: $P(\square|\square)=94.1\%$, $P(\blacksquare|\square)=5.9\%$, $P(\square|\blacksquare)=33.3\%$, $P(\blacksquare|\blacksquare)=66.7\%$. Given $P(\square)=0.867$, compute $H(X|Y)$.

**Solution.**
$H(X|\square)=-0.941\log_2 0.941-0.059\log_2 0.059=0.0824+0.2410=0.322$.
$H(X|\blacksquare)=-0.333\log_2 0.333-0.667\log_2 0.667=0.528+0.390=0.918$.
$H(X|Y)=P(\square)H(X|\square)+P(\blacksquare)H(X|\blacksquare)=0.867(0.322)+0.133(0.918)=0.279+0.122=\mathbf{0.406\ bpp}$.
Better than $K=4$ block coding → justifies **context-based arithmetic** coding.

### Ex 3.6 — Exp-Golomb 🔢
Unsigned Exp-Golomb of $n=0,3,7$. Then the signed value $n=-2$.

**Solution (unsigned).** Rule: write $n+1$ in binary on $b=\lfloor\log_2(n+1)\rfloor+1$ bits, prepend $b-1$ zeros.
- $n=0$: $n+1=1$ → `1`.
- $n=3$: $n+1=100_2$ ($b=3$) → 2 zeros + `100` → `00100`.
- $n=7$: $n+1=1000_2$ ($b=4$) → 3 zeros + `1000` → `0001000`.

**Signed** $n=-2$: map $m=-2n=4$ (since $n\le0$). Then unsigned EG of 4: $4+1=101_2$ ($b=3$) → `00101`.

---

# 4. Transform Coding and JPEG (L4)

### Ex 4.1 — Coding gain ⭐🔢
Orthogonal transform on a block with output variances $\sigma_1^2=2\sigma^2$, $\sigma_2^2=\sigma^2/100$ (toy example). Compute $G_T$.

**Solution.** OT preserves the AM: $\sigma_{AM}^2=\frac{1}{2}(2\sigma^2+0.01\sigma^2)=1.005\sigma^2$.
$\sigma_{GM}^2=\sqrt{2\sigma^2\cdot0.01\sigma^2}=\sqrt{0.02}\,\sigma^2=0.1414\sigma^2$.
$G_T=\sigma_{AM}^2/\sigma_{GM}^2=1.005/0.1414=\mathbf{7.1}\;(\approx 8.5\ dB)$. The transform compacts energy → gain.

### Ex 4.2 — Huang-Schulteiss bit allocation ⭐🔢
4 Gaussian components (same $c_k$): $\sigma^2=[1000,100,50,1]$, $R_{Tot}=10$ bits. Apply HS and fix negative rates.

**Solution.**
$\bar R=R_{Tot}/4=2.5$. GM$=(1000\cdot100\cdot50\cdot1)^{1/4}=(5{\times}10^6)^{1/4}\approx47.29$.
$R_k=2.5+0.5\log_2(\sigma_k^2/47.29)$:
- $R_1=2.5+0.5\log_2(21.15)=2.5+2.20=4.70$
- $R_2=2.5+0.5\log_2(2.115)=2.5+0.54=3.04$
- $R_3=2.5+0.5\log_2(1.057)=2.5+0.04=2.54$
- $R_4=2.5+0.5\log_2(0.0211)=2.5-2.78=-0.28$ ❌ negative.

Remove $k=4$ (R=0), recompute on 3: GM$=(1000\cdot100\cdot50)^{1/3}=(5{\times}10^6)^{1/3}=171.0$, $\bar R=10/3$:
- $R_1=3.33+0.5\log_2(5.85)=3.33+1.27=4.61$
- $R_2=3.33+0.5\log_2(0.585)=3.33-0.39=2.95$
- $R_3=3.33+0.5\log_2(0.292)=3.33-0.89=2.45$

Floor → $[4,2,2,0]$, total 8, give 2 residual bits to the largest fractional parts ($R_1,R_2$) → $\boxed{R=[5,3,2,0]}$.

### Ex 4.3 — Greedy bit allocation (same problem) 🔢
Verify with the greedy algorithm: $D_k=\sigma_k^2$, each bit quarters the distortion → $D_\ell\leftarrow D_\ell/4$.

**Solution.** Assign 1 bit to the component with max $D$, 10 times:
Start $D=[1000,100,50,1]$.
b1→k1: D1=250. b2→k1: 62.5. b3→k2:25. b4→k1:15.6. b5→k3:12.5. b6→k2:6.25. b7→k1:3.9. b8→k3:3.1. b9→k1:0.98. b10→k2:1.56…
Final rate count: $k1{=}5, k2{=}3, k3{=}2, k4{=}0$ → $\boxed{[5,3,2,0]}$, **identical to HS**.
Total distortion $\approx 0.98+1.56+3.13+1=\mathbf{6.67}$.

### Ex 4.4 — KLT energy compaction 🔢
6-band multispectral, energy per eigenband: 86.37, 7.65, 4.16, 1.67, 0.12, 0.03 %. How many bands for ≥98% energy?

**Solution.** Cumulative: 86.37 → 94.02 → 98.18%. **3 bands** suffice (98.18% ≥ 98%). KLT compacts almost all energy in the first components.

### Ex 4.5 — JPEG: DCT quantization 🔢
DCT coefficient $c=186.2$ at position (0,1), step $q_{0,1}=11$ (standard luma table). Quantize and de-quantize; compute error.

**Solution.** $\tilde c=\text{round}(186.2/11)=\text{round}(16.93)=\mathbf{17}$.
De-quant: $\hat c=17\cdot11=\mathbf{187}$. Error $=187-186.2=0.8$.

### Ex 4.6 — JPEG: DC coding (DPCM + category/amplitude) ⭐🔢
Current block $DC=−2$, previous block $DC_{n-1}=1$. Encode the DC with the JPEG method (category + amplitude). Table: cat1=`010`, cat2=`011`, cat3=`100`.

**Solution.** $DC_P=DC_n-DC_{n-1}=-2-1=-3$.
Category $k=\lceil\log_2(|{-3}|+1)\rceil=\lceil\log_2 4\rceil=2$ → code `011`.
Amplitude: $|{-3}|=3=11_2$ on $k=2$ bits; negative → bitwise complement → `00`.
Stream $=$ `011`+`00` $=$ **`01100`**.
(Compare: $DC_P=+3$ would give `011`+`11`=`01111`.)

### Ex 4.7 — JPEG: zig-zag + run-length 🔢
Quantized block (after zig-zag, DC excluded): $17, 3, 0, 4, 0, 0, 0, 0, \dots$ (then all zeros). Write the AC symbols (run, amplitude) + EOB.

**Solution.** Pairs (run of zeros before the nonzero, value):
- 17 → $(0,17)$
- 3 → $(0,3)$
- 4 → $(1,4)$ (one zero before)
- then all zeros → **EOB** $=(0,0)$.
Sequence: $(0,17)(0,3)(1,4)\,\text{EOB}$.

---

# 5. Wavelet Analysis — EZW / EBCOT (L5)

### Ex 5.1 — EZW: first dominant + refining pass ⭐🔢
4×4 DWT matrix:
$$\begin{bmatrix} 26 & 6 & -13 & 10 \\ -7 & 3 & 6 & 4 \\ 4 & -3 & 3 & -3 \\ 2 & -2 & -2 & 0 \end{bmatrix}$$
Initial threshold $T=2^{\lfloor\log_2\max|c|\rfloor}$. Run dominant pass 1 and refining pass 1 for the significant coefficient.

**Solution.**
$\max|c|=26$ → $n=\lfloor\log_2 26\rfloor=4$ → $T=16$.
**Dominant pass 1:** scan; only $|26|\ge16$ → **SP** (significant positive). All others $<16$ and their subtrees $<16$ → **ZR** (zero-tree root).
Symbols: `[SP, ZR, ZR, ZR]`.
**Refining pass 1:** $26=11010_2$; with $T=16$ the decoder knows $26\in[16,32)$ → midpoint estimate $24$; refining bit $=1$ → $26\in[24,32)$ → new estimate $28$.
Stream: `[SP,ZR,ZR,ZR | 1]`.
**Bitplane 2 ($T=8$):** now $|-13|\ge8$→SN, $|10|\ge8$→SP, $6<8$ but has descendant $13\ge8$→IZ, etc. (threshold halves each pass → bitplane coding, quality scalability).

### Ex 5.2 — EBCOT: optimal Lagrangian truncation 📐🔢
Two codeblocks with R-D slopes $\partial D_1/\partial R_1$ and $\partial D_2/\partial R_2$. Explain the optimality condition and the effect of choosing $\lambda$.

**Solution.** Minimize $\sum_i D_i$ s.t. $\sum_i R_i\le R_{tot}$ → Lagrangian $J=\sum_i(D_i+\lambda R_i)$.
$\partial J_i/\partial R_i=0 \Rightarrow \partial D_i/\partial R_i=-\lambda$ **for every** codeblock.
→ at the optimum all codeblocks are truncated where their **R-D slope is equal** ($=-\lambda$). Large $\lambda$ = low rate (aggressive truncation); several $\lambda$ values = several truncation points = **quality layers**.

---

# 6. Motion Estimation (L7)

### Ex 6.1 — SAD vs SSD on a 2×2 block ⭐🔢
Current block $B_k=\begin{bmatrix}10&12\\14&16\end{bmatrix}$, candidate reference block $B_h=\begin{bmatrix}11&10\\14&20\end{bmatrix}$. Compute SAD and SSD.

**Solution.** Differences: $10-11=-1$, $12-10=2$, $14-14=0$, $16-20=-4$.
$J_{SAD}=|-1|+|2|+|0|+|-4|=\mathbf{7}$.
$J_{SSD}=(-1)^2+2^2+0^2+(-4)^2=1+4+0+16=\mathbf{21}$.
Note: SSD heavily weights the outlier $-4$ (16 out of 21) → more outlier-sensitive, less regular MVF.

### Ex 6.2 — Full Search complexity 🔢
Search window $\pm A$ with $A=7$. How many candidate vectors does Full Search test? For a 16×16 block, how many SAD operations per block?

**Solution.** Candidates $=(2A+1)^2=(15)^2=\mathbf{225}$.
Each SAD on $16\times16=256$ px needs 256 subtract+|·|+add → $225\times256\approx\mathbf{57{,}600}$ ops/block. (This is why Diamond/Hexagon are used: ~17–23 tests, about −90%.)

### Ex 6.3 — Sub-pixel bilinear interpolation 🔢
Half-pixel estimate: integer neighbors $x=100$ (at $n,m$), $y=120$ ($n,m{+}1$), $z=140$ ($n{+}1,m$), $w=160$ ($n{+}1,m{+}1$). Value at $(n+0.5,m+0.5)$.

**Solution.** $f=(1-a)(1-b)x+a(1-b)y+(1-a)b z+ab w$ with $a=b=0.5$:
$=0.25(100)+0.25(120)+0.25(140)+0.25(160)=0.25(520)=\mathbf{130}$.

### Ex 6.4 — Affine model 🔢
Affine model $\mathbf v(\mathbf p)=\mathbf b+\mathbf B\mathbf p$ with $\mathbf b=0$, $\mathbf B=\begin{bmatrix}0&-0.5\\0.5&0\end{bmatrix}$. What motion does it represent? Vector at $\mathbf p=(2,4)$?

**Solution.** $\mathbf B$ antisymmetric → **rotation**. $v_x=-0.5y=-0.5(4)=-2$; $v_y=0.5x=0.5(2)=1$ → $\mathbf v=(-2,1)$. 6 parameters describe the whole field (vs hundreds of block MVs).

---

# 7. Audio Coding (L10)

### Ex 7.1 — G.729 bitrate ⭐🔢
G.729: 80 bits per 10 ms frame. Compute the bitrate.

**Solution.** $R=\frac{80\ \text{bit}}{0.010\ \text{s}}=\mathbf{8000\ bps}=8$ kbps.

### Ex 7.2 — LPC-10 bitrate 🔢
LPC-10: 54 bits per 22.5 ms frame. Verify the 2.4 kbps.

**Solution.** $R=54/0.0225=\mathbf{2400\ bps}=2.4$ kbps. ✓

### Ex 7.3 — MDCT critical sampling 🔢
MDCT with 50% overlap, $M=1024$ new samples/frame. How many samples does the window process and how many spectral coefficients does it produce?

**Solution.** Window $N=2M=\mathbf{2048}$ samples (50% overlap); coefficients $=M=\mathbf{1024}$. # coeff $=$ # **new** samples → no data expansion (critical sampling), even though overlap removes blocking.

### Ex 7.4 — SMR and transparency condition 📐🔢
In a subband: signal power $S_k=60$ dB, masking threshold $\Phi_k=35$ dB. Compute SMR and the minimum SNR for transparency.

**Solution.** $\text{SMR}_k=S_k-\Phi_k=60-35=\mathbf{25\ dB}$. Transparency requires $\text{SNR}_k>\text{SMR}_k=25$ dB: with ~6 dB/bit you need $\lceil25/6\rceil=\mathbf{5}$ bits/sample to keep noise below the threshold.

---

# 8. Adaptive Streaming (L12)

### Ex 8.1 — Segment download time ⭐🔢
$T_S=1$ s, level with $R_C=2$ Mbps, throughput $S_n=1.8$ Mbps. Segment download time? Does it arrive in time?

**Solution.** $T_D=\frac{T_S R_C}{S_n}=\frac{1\cdot2}{1.8}=\mathbf{1.11\ s}$. $T_D>T_S$ → the segment does **not** arrive in time: the buffer drains (slope $S/R_C-1=0.9-1=-0.1$).

### Ex 8.2 — Buffer slope 🔢
Fluid model: $\frac{dB}{dt}=\frac{S}{R_C}-1$ in playout. With $R_C=2.5$ Mbps, compute the slope for $S=3$ Mbps and $S=1$ Mbps.

**Solution.** $S=3$: slope $=3/2.5-1=+0.2$ (buffer grows). $S=1$: slope $=1/2.5-1=-0.6$ (buffer drains fast). When $B=0$ → stall.

### Ex 8.3 — Startup time with piecewise throughput ⭐🔢
$T_S=1$ s, $L=2$ initial segments, $q=3$ with $R_C(3)=2$ Mbps. Throughput: $S_1=1.5$ Mbps in $(0,2)$, $S_2=0.1$ in $(2,3)$, $S_3=1.8$ after. When does playout start?

**Solution.** Bits needed for $L=2$ segments: $N_b=T_S[R_C(3)+R_C(3)]=2+2=4$ Mbit.
Received in $(0,2)$: $2\cdot1.5=3$ Mbit. In $(2,3)$: $1\cdot0.1=0.1$ Mbit. Missing $4-3.1=0.9$ Mbit.
From $t=3$, $S_3=1.8$ → $0.9/1.8=0.5$ s.
Playout starts at $t_{ST}=3+0.5=\mathbf{3.5\ s}$.

### Ex 8.4 — Periodic rebuffering 🔢
Continue Ex 8.3: after $t_{ST}=3.5$, $S=1.8$, $R_C=2$, $B(t_{ST})=2$ s. After how long does the buffer empty?

**Solution.** Playout slope $=1.8/2-1=-0.1$. From $B=2$: time to zero $=2/0.1=\mathbf{20\ s}$ → stall at $t=3.5+20=23.5$ s. Since $S<R_C$, maximum quality causes **periodic rebuffering**. → an ABR strategy lowering quality (e.g. 1 in 5 segments at level 2) is preferable.

### Ex 8.5 — Minimum anti-stall initial buffering 🔢
$R_C(1)=0.5$ Mbps. Throughput $S_1=0.4$ Mbps for $t\in(0,T)$, then $S_2=0.5$ Mbps. Find the minimum $t_{ST}$ (initial buffering duration) that avoids stalls with $q=1$.

**Solution.** During buffering slope $=S_1/R_C=0.4/0.5=0.8$. In playout (before $T$) slope $=0.8-1=-0.2$; after $T$ slope $=0.5/0.5-1=0$.
If $t_{ST}<T$: $B(t_{ST})=0.8\,t_{ST}$, then drains at $-0.2$. Zero at $t^*$: $0.8 t_{ST}-0.2(t^*-t_{ST})=0 \Rightarrow t^*=5t_{ST}$.
To not empty before the change at $T$: $T\le 5t_{ST}$ → $\boxed{t_{ST,\min}=T/5}$.

---

## Pre-exam checklist (most likely numericals)
- [ ] Huffman + entropy + efficiency (Ex 3.1) ⭐
- [ ] AR(1) prediction gain and threshold $\rho>1/2$ (Ex 2.2) ⭐
- [ ] HS / greedy bit allocation (Ex 4.2–4.3) ⭐
- [ ] Coding gain $G_T=\sigma_{AM}^2/\sigma_{GM}^2$ (Ex 4.1) ⭐
- [ ] JPEG: quant + DC category/amplitude + zig-zag (Ex 4.5–4.7) ⭐
- [ ] EZW dominant/refining (Ex 5.1) ⭐
- [ ] SAD/SSD (Ex 6.1) ⭐
- [ ] Streaming: startup + rebuffering + buffer slope (Ex 8.3–8.5) ⭐
- [ ] Quantization R-D, SNR≈6R (Ex 2.1, 1.4)
- [ ] Codec bitrate (G.729/LPC-10), MDCT, SMR (Ex 7.x)

> Formulas to memorize: $D=\sigma_X^2 2^{-2R}$, $\text{SNR}\approx6R$; $G_P=10\log_{10}\frac{1}{2(1-\rho)}$; $\underline a^{opt}=-R_X^{-1}\underline r$; $H=-\sum p\log_2 p$; Kraft $\sum 2^{-l_i}\le1$; $R_k^*=\bar R+\frac12\log_2\frac{c_k\sigma_k^2}{c_{GM}\sigma_{GM}^2}$; $G_T=\sigma_{AM}^2/\sigma_{GM}^2$; DC category $k=\lceil\log_2(|DC_P|+1)\rceil$; $T_D=T_S R_C/S$; $\frac{dB}{dt}=S/R_C-1$.
