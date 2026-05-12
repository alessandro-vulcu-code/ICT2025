# Motion Estimation

**Marco Cagnazzo**
Multimedia Communications — Università di Padova, Dipartimento di Ingegneria dell'Informazione

---

## Outline

- Introduction
- Variational methods
- Block-matching methods
  - Criteria & Strategy
  - Advanced Techniques
- Parametric methods
- Deep Learning methods
- Conclusions

---

## 1. Introduction

### Movement

- Movement is an important visual cue
- It can be a source of information (we need to estimate it)
- Or something we need to account for (to improve compression, processing, etc.)
- Examples: object segmentation, video compression, video stabilization, super-resolution

### Motion and Apparent Motion

- **Physical motion:** actual movement of objects in the world
- **Apparent motion (optical flow):** movement of pixels in an image sequence
- Two sensors to measure physical motion: accelerometers, gyroscopes
- We focus on optical flow
- Optical flow is a 2D vector field describing pixel displacement between consecutive frames

Physical motion ≠ apparent motion:
- Example: rotating sphere with uniform texture → no apparent motion even if there is physical motion
- Example: light source moving → apparent motion even without physical motion of objects

[Figura: Two images showing a scene with motion vectors overlaid illustrating the difference between physical and apparent motion]

### Motion Estimation Applications

- **Video compression:** temporal prediction reduces redundancy
- **Video analysis:** object tracking, action recognition
- **Video enhancement:** deblurring, super-resolution, frame interpolation
- **Medical imaging:** cardiac motion analysis
- **Autonomous driving:** obstacle detection

---

## 2. Variational Methods

- Also called differential or gradient-based methods
- Based on the analysis of image gradients
- Produce a dense motion vector field (one vector per pixel)
- Most important: Horn and Schunck algorithm

### Variational Methods as Optimization Problem

Motion estimation as an optimization problem:

$$\hat{v} = \arg\min_v E(v)$$

$E(v)$ is an energy functional. It typically includes a data term and a regularization term:

$$E(v) = E_{\text{data}}(v) + \lambda E_{\text{smooth}}(v)$$

[Figura: Ship video sequence — reference frame and current frame with motion vector field overlay]

### Optical Flow: Problem Statement

- Given two consecutive frames $f_k$ and $f_h$ ($h = k-1$ or $k+1$)
- Find the displacement field $\mathbf{v}(n,m) = (u(n,m), v(n,m))^T$
- Such that $f_k(n,m) \approx f_h(n - u(n,m), m - v(n,m))$

### Optical Flow: The Displacement Field

- The displacement field $\mathbf{v}(n,m)$ is the optical flow
- It is a 2D vector field
- Each vector represents the displacement of a pixel from one frame to the next

### Optical Flow: The Constant Illumination Hypothesis

Hypothesis:

$$f_k(n,m) = f_h(n - u, m - v)$$

The illumination of a pixel does not change between frames. This is the key hypothesis of optical flow methods.

### Optical Flow: The OF Equation

Taylor expansion of $f_h(n-u, m-v)$:

$$f_h(n-u, m-v) \approx f_h(n,m) - u \frac{\partial f_h}{\partial n} - v \frac{\partial f_h}{\partial m}$$

From the constant illumination hypothesis:

$$f_k(n,m) = f_h(n,m) - u f_n - v f_m$$

Therefore:

$$f_k(n,m) - f_h(n,m) = u f_n + v f_m$$

$$f_t = u f_n + v f_m$$

This is the **OF equation**:

$$\nabla f \cdot \mathbf{v} + f_t = 0$$

One equation, two unknowns: $(u, v)$.

The **aperture problem**: impossible to determine the full motion from a single equation. Need additional constraints.

### Optical Flow: Solving the OF Equation

Horn and Schunck: add smoothness constraint. Minimize:

$$E(u,v) = \iint \left[(\nabla f \cdot \mathbf{v} + f_t)^2 + \lambda^2\left(|\nabla u|^2 + |\nabla v|^2\right)\right] dn\, dm$$

- First term: data fidelity (OF equation)
- Second term: smoothness (regularization)

### OF: The Horn and Schunck Algorithm

The minimization leads to the Euler-Lagrange equations:

$$f_n(f_n u + f_m v + f_t) = \lambda^2 \Delta u$$
$$f_m(f_n u + f_m v + f_t) = \lambda^2 \Delta v$$

Iterative solution using Gauss-Seidel iterations:

$$u^{k+1} = \bar{u}^k - \frac{f_n(f_n \bar{u}^k + f_m \bar{v}^k + f_t)}{\lambda^2 + f_n^2 + f_m^2}$$

$$v^{k+1} = \bar{v}^k - \frac{f_m(f_n \bar{u}^k + f_m \bar{v}^k + f_t)}{\lambda^2 + f_n^2 + f_m^2}$$

Where $\bar{u}^k$ and $\bar{v}^k$ are local averages of $u^k$ and $v^k$.

- The algorithm converges to a unique solution (convex problem)
- The regularization parameter $\lambda$ controls the trade-off between data fidelity and smoothness

[Figura: Optical flow results on rotating sphere and tree sequences]

### OF: The Horn and Schunck Algorithm — Conclusions

**Advantages:**
- Dense field (one vector per pixel)
- Simple and well-understood
- Convex optimization (unique solution)

**Disadvantages:**
- Over-smoothed at motion boundaries
- Constant illumination hypothesis often violated
- Slow for large displacements

---

## 3. Block-Matching Methods

### Block Matching

- The image is divided into blocks of size $P \times Q$
- For each block $B(p,q)$ in the current frame, we search for the best matching block in the reference frame
- The displacement is the motion vector
- Block-matching is the basis of most video compression standards

- Reference frame $f_h$ and current frame $f_k$
- Block $B(p,q)$: block centered at position $(p,q)$ in $f_k$
- We search for the block in $f_h$ that best matches $B(p,q)$
- The motion vector is $(i,j)$ such that $B_{p-i,q-j}$ in $f_h$ best matches $B_{p,q}$ in $f_k$

### Block Matching — Notation

- $f_k(B_{p,q})$: luminance values in block $B_{p,q}$ of frame $f_k$
- Motion vector: $(i,j) \in \mathcal{W}$ (search window)
- Best motion vector:

$$(\hat{i}, \hat{j}) = \arg\min_{(i,j) \in \mathcal{W}} d\left[f_k(B_{p,q}),\, f_h(B_{p-i,q-j})\right]$$

- $d[\cdot, \cdot]$: distortion measure (cost function)
- The motion-compensated prediction of $f_k(B_{p,q})$ is $f_h(B_{p-\hat{i},q-\hat{j}})$
- The prediction error is $f_k(B_{p,q}) - f_h(B_{p-\hat{i},q-\hat{j}})$
- Ideally, the prediction error should be small

Block-matching produces a **piecewise-constant** motion vector field (MVF) — one vector per block. The MVF is used for motion-compensated prediction in video coding.

[Figura: Block diagram showing reference frame with search window and candidate blocks, and illustration of block matching between current and reference frame]

### Evaluation of the MVF

**Mean Squared Error (MSE)** of the motion-compensated prediction:

$$\text{MSE} = \frac{1}{NM} \sum_{n,m} \left[f_k(n,m) - f_h(n - \hat{u}(n,m), m - \hat{v}(n,m))\right]^2$$

**PSNR:**

$$\text{PSNR} = 10 \log_{10} \frac{255^2}{\text{MSE}} \quad \text{[dB]}$$

Higher PSNR = better prediction = less residual to encode.

**Coding cost:**
- A cost measure can be the number of bits needed to losslessly encode the MVF — called the *coding cost*
- The coding cost depends on the technique used to encode the vectors:
  - Fixed-length coding
  - Exp-Golomb coding (possibly, with prediction)
  - Huffman coding
  - Arithmetic coding (possibly, context-based)
- To present a measure related to the MVF rather than to the technique, we can use the **MVF empirical entropy**
- It amounts to estimate the probability of MVF components via their relative frequency in $(u,v)$, and to use this probability in the entropy formula

**Computational complexity:**

In order to compute $\arg\min_{(i,j) \in \mathcal{W}} d[f_k(B_{p,q}), f_h(B_{p-i,q-j})]$, we need:
- For each block $B(p,q)$
- and for each candidate vector $(i,j) \in \mathcal{W}$
- compute one instance of $d[f_k(B_{p,q}), f_h(B_{p-i,q-j})]$

The following choices impact on the computational complexity:
- The block size (which determines the number of blocks)
- The number of candidate vectors (which depends on the search window and on the search strategy)
- The cost function (or criterion) $d$

For each of these parameters' choice, there is a trade-off between complexity, quality and coding cost of the MVF. Understanding this trade-off is of fundamental importance to design an effective ME technique.

**Block size trade-off:**

A large block size $P \times Q$ will typically:
- reduce the complexity (less blocks)
- reduce the coding cost (less blocks means less vectors to encode)
- increase the MSE, because we use a less flexible mathematical model: the MVF is constant on large areas

[Figura: MVF visualizations comparing block sizes 32×32, 16×16, and 8×8]

### Parameters of Motion Estimation

#### Cost Function

Several choices are possible for $d(\cdot, \cdot)$:

**SAD (Sum of Absolute Differences):**

$$d(B_1, B_2) = \sum_{n,m} |B_1(n,m) - B_2(n,m)|$$

**SSD (Sum of Squared Differences):**

$$d(B_1, B_2) = \sum_{n,m} [B_1(n,m) - B_2(n,m)]^2$$

SSD has the smallest MSE, but it is more complex and requires more bits (irregular vectors).

#### Regularized Cost Function

Instead of minimizing $d(v)$, one can minimize a regularized cost function $J$:

$$J(v) = d(v) + \lambda_{ME}\, r(v)$$

- $r(v)$ can be the coding cost (number of bits) of vector $v$
- Adding the regularization means that we can select a vector that does not achieve the best MSE, but costs less bits to be encoded
- The trade-off is driven by $\lambda_{ME}$:
  - Small $\lambda_{ME}$: coding cost is not important, $v$ must only minimize the distance $d$
  - Large $\lambda_{ME}$: minimizing the coding cost is what matters, even at cost of a large "distortion" $d(v)$

[Figura: Comparison of non-regularized MVF vs. regularized MVF on ship sequence; Regularized MVF motion-compensated image and compensation error]

### BM Criteria — Norm-Based Criteria

Let us see how to choose the matching criterion $d$. We have to choose a **dissimilarity** measure between vectors of luminance values. A natural choice is the distance in some metric space — that is the norm of the difference:

$$J(i,j) = \|f_k(B_{p,q}) - f_h(B_{p-i,q-j})\|_p^p \tag{2}$$

Interest cases: $p = 1$ ($\mathcal{L}^1$ norm), $p = 2$ ($\mathcal{L}^2$ norm).

#### Norm-Based Criteria: SSD

If in Eq. (2) we choose $p = 2$ we obtain the criterion called *Sum of Squared Differences*, SSD:

$$J_{\text{SSD}}(i,j) = \sum_{(n,m) \in B_{p,q}} \left[f(n,m,k) - f(n-i,\, m-j,\, h)\right]^2$$

- For a given block size, the SSD minimizes the energy of the MC-ed prediction
- Therefore, the SSD is the best choice in terms of MVF quality

However, the SSD has also several disadvantages:
- It is relatively complex to compute: the criterion $d$ includes a multiplication
- The square operator highlights errors from outliers, resulting sometimes in irregular vectors, which in turns increase the entropy (coding cost) of the MVF
- It does not take into account global illumination changes
- The $p = 1$ norm reduces the impact of the first 2 problems

#### Norm-Based Criteria: SAD

If in Eq. (2) we choose $p = 1$ we get the *Sum of Absolute Differences* or SAD:

$$J_{\text{SAD}}(i,j) = \sum_{(n,m) \in B_{p,q}} |f(n,m,k) - f(n-i,\, m-j,\, h)|$$

- When using SAD, we look for the prediction error with the smallest $\mathcal{L}^1$ norm
- When using SSD, we look for the prediction error with the smallest $\mathcal{L}^2$ norm, i.e., the smallest energy
- As a consequence, the prediction error energy in the SAD case can only be larger than the one in the SSD case

However, the SAD motion vector field is generally more regular than the one estimated with SSD. The reason lies in **outliers**:
- Outliers are pixels affected by large "noise"
- I.e., pixels not respecting the constant illumination hypothesis
- An outlier in position $n, m$ contributes to the cost function with $|f(n,m,k) - f(n-i, m-j, h)|^p$
- Thus, if $p = 2$ a single outlier (or a few but concentrated in a small area) can affect the estimated motion vector

[Figura: Reference image and Current image of tree/garden sequence; MVF comparison SSD (Rate: 2143 bits, PSNR: 22.46 dB) vs SAD (Rate: 2103 bits, PSNR: 22.30 dB); Motion-compensated images SSD vs SAD; MC error comparison SSD vs SAD; MC error (SSD) and Difference image]

**Summary:**
- These MVF are not always regular: the estimation in homogeneous regions depends finally on noise
- Advantage: minimization of the error energy
- Disadvantage: motion artifacts; high coding cost
- Solution: **regularization**
  - Large block sizes, $\mathcal{L}^1$ norm are a form of implicit regularization
  - We can resort to explicit regularization

#### Regularized Norm-Based Criteria

We modify the criterion (2) by penalizing vectors that are too much different from their neighbors. This is accounted for in the function $R(i,j)$. Thus we get:

$$J_{\text{REG}}(i,j) = \|f_k(B_{p,q}) - f_h(B_{p-i,q-j})\|_p^p + \lambda\, R(i,j)$$

For example, $R$ could be the distance between $(i,j)$ and a vector representing the neighborhood, such as the average or the median.

[Figura: SSD without regularization (Rate: 2143 bits, PSNR: 22.46 dB) vs SSD with regularization (Rate: 2008 bits, PSNR: 22.35 dB)]

### Research Strategies

#### Full Search

Naive solution: each vector $(i,j)$ must be tested.
- We compute the criterion $J$ as many times as possible motion vectors: $(N-P)(M-Q)$
- Often, it is enough to consider a smaller region centered in $(p,q)$

We define a **search window** $\mathcal{W}$:

$$\mathcal{W} = \{-A, \ldots, -1, 0, +1, \ldots, A\} \times \{-B, \ldots, -1, 0, +1, \ldots, B\}$$

Typically, $A = B$. If $n = 2A+1$, there are $n^2$ candidate vectors in $\mathcal{W}$.

The **full search** motion estimation consists in computing $J$ for each vector in $\mathcal{W}$, and taking the one that optimizes the criterion.

#### The Cost Function Landscape

The search for the Motion Vector $(i,j)$ is equivalent to finding the **global minimum** in a 3D cost-function surface:
- **Global Minimum:** The optimal vector (lowest residual energy).
- **Local Minima:** Risks for fast search algorithms (traps).
- **Flat areas:** Low texture, motion estimation becomes ambiguous.

[Figura: 3D surface plot of the SSD Error Landscape showing global minimum and local minima]

#### Fast Methods

- Full search demands $n^2$ computations to find the best vector limited to a displacement of $\pm A$ pixels
- Fast methods allow to find motions with the same amplitude $\pm A$ pixels with less than $n^2$ computations
- The basic idea is to test a subset of vectors
- On the other hand, fast methods no longer assure the optimal MV

#### Three Steps Search (3SS)

- The 3SS is based on the assumption that the error function is **unimodal**
- This implies a single global minimum and no local minima that could "trap" the search
- **Risk:** If the surface is complex (multimodal), fast searches may converge to a local minimum, missing the best match
- Successive steps with decreasing stride $(D, D/2, \ldots, 1)$
- Tests 4 or 8 points around the center at each step

[Figura: Visual demo — Current image (Target Block), Reference (i=1, j=0), search pattern overlay, residual map, SSD cost surface — Test 25]

#### Diamond Search

- Uses a diamond-shaped pattern (**Large Diamond Search Pattern** — LDSP)
- The pattern "moves" until the minimum is at the center
- Final refinement with a **Small Diamond** (SDSP)
- 3 to 5 new points per iteration (9 for the first)

[Figura: Grid showing LDSP (red squares) and SDSP (green diamonds) patterns; Sequence of LDSP movements followed by SDSP refinement]

[Figura: Visual demo — Current image (Target Block), Reference (i=6, j=3), diamond search pattern overlay, residual map, SSD cost surface — Test 23]

#### Hexagon Search

- Evolution of Diamond Search (H.264/AVC)
- More regular shape (6-sided) for more uniform displacement speed
- Fewer computations per step: only 3 new points if the center is not the minimum

[Figura: Grid showing LHP (Large Hexagon Pattern, red squares) and SHP (Small Hexagon Pattern, green diamonds); Sequence of hexagon pattern movements]

[Figura: Visual demo — Current image (Target Block), Reference (i=0, j=3), hexagon search pattern labeled COS, residual map, SSD cost surface — Test 17]

#### Comparison of Search Strategies

In this example, all methods converge to the same optimal vector, but with vastly different numbers of tested vectors:

| Strategy | Tests | Δ% |
|----------|-------|-----|
| Full Search (FS) | 225 | Baseline |
| 2D-Log Search | 25 | ~-89% |
| Diamond Search | 23 | ~-90% |
| Hexagon Search | 17 | ~-92% |

**Key Takeaways:**
- **Unbounded Search:** Diamond and Hexagon are iterative. Unlike FS, they aren't limited by a fixed $n$ and can "follow" the motion across the frame.
- **Reliability:** While FS guarantees the global minimum, fast methods can get stuck in local minima (though rare in natural video).

#### Modern Fast Search: TZSearch

The **Test Zone Search (TZSearch)** is the reference algorithm for recent standards. It adaptively switches between different strategies to handle large blocks (up to 64×64).

**The Three Phases of TZSearch:**
1. **Search Predictors:** Initial tests on vectors from spatial and temporal neighbors. If the error is low enough, the search stops early.
2. **Adaptive Loop:** If no predictor is good, it uses a Diamond/Square search with increasing steps.
3. *(Full refinement phase)*

**Key Advantage:** More robust against **local minima** compared to simple Diamond or Hexagon search.

### Block Matching: Subpixel Precision

[Figura: Six panels showing block displacement at integer pixel positions (v=(5,3)) and half-pixel positions (v=(5.5,2.5))]

**Hierarchical approach:**
- First we find $(\hat{i}, \hat{j}) \in \mathbb{Z}^2$;
- then we test $\left(\hat{i} \pm \tfrac{1}{2},\, \hat{j} \pm \tfrac{1}{2}\right)$;
- then we verify the $1/4$-pixel neighbors, etc.

[Figura: Grid showing integer pixel positions (circles), selected full-pixel vector (red dot), and tested half-pixel positions (crosses)]

It is possible to evaluate $f(n+a, m+b, k)$ via interpolation:

$$f(n,m) = x \qquad f(n+1,m) = y$$
$$f(n,m+1) = z \qquad f(n+1,m+1) = w$$

**Bilinear interpolation:** horizontal and vertical average of pixels:

$$f(n+a, m+b) = (1-a)(1-b)\,x + a(1-b)\,y + (1-a)b\,z + ab\,w$$

More complex interpolation techniques have been proposed (high order filters).

### Block Matching: Variable Block Size

- Underlying hypothesis in BM: motion is homogeneous in a block
- It is not true if a block contains object's borders
- **Solution 1: smaller blocks**
  - Improved precision
  - Increased complexity
  - Increased coding cost (number of motion vectors per image)
- **Solution 2: variable-size blocks**
  - Additional coding cost and complexity: only if necessary
  - Hierarchical approach: a block is split if the value of the criterion is too big
  - This solution is adopted in recent video coding standards

**Algorithm:**

**Input:** Frame $F$, Ref. frame $R$, Initial block size $B$, $\lambda$  
**Output:** Motion vectors and partitioning

```
for each block b of size B in F do
    Calculate J(v) = D + λR for b;
    Divide b into four sub-blocks;
    for each sub-block s_i do
        Calculate J_i(v) = D_i + λR_i for s_i;
    end
    J_sub = Σ^4_{i=1} J_i(v)
    if J_sub < J(v) then
        Apply algorithm to each sub-block;
    else
        Keep b & store MV;
    end
end
```

**Where:**
- $D$: Distortion measure (e.g., SAD, SSD)
- $R$: Rate measure (bits to encode motion vector)
- $\lambda$: Lagrange multiplier for rate-distortion optimization
- $v$: Motion vector

**Note:**
- The algorithm is applied recursively to sub-blocks
- Termination condition: minimum block size or $J(v)$ no longer decreases
- The process balances between motion estimation accuracy and coding efficiency

---

## 4. Parametric Methods

### Definitions

- Using parametric models means that the motion vector field is modeled as a close-form function of the pixel position
- The degrees of freedom are the *parameters* of the mathematical function
- The parametric model can be unique for all the scene (**global motion estimation**); or one can use a different parametric model per region
- In turns, the region can be an object (in this case, we first need to *segment* the image to find the objects) or a pre-determined set of pixels, e.g., a block

Block-matching methods can be seen as a special form of parametric methods, where the MVF is a block-wise constant function, with two free parameters per block (pure translation). The regions are the blocks.

More general models can be conceived:
- Less parameters → Robust estimation, but less generality, can miss the complexity of motion
- More parameters → Prone to overfitting, more complex but also more general

### Translational Model

- The simplest motion model is the translational one
- This model corresponds to the case of a rigid object that translates orthogonally to the optic axis without rotations
- Let $\mathbf{v}(\mathbf{p})$ be the instantaneous velocity in position $\mathbf{p} = [x, y]^T$ on the image plane
- Components $v_x$ and $v_y$ of $\mathbf{v}$ do not vary with $\mathbf{p}$, they depend on camera parameters and on object motion
- In other words, the model is a constant vector (two parameters):

$$\mathbf{v}(\mathbf{p}) = \begin{bmatrix} v_x \\ v_y \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \end{bmatrix}$$

This model is only characterized by two parameters, $b_1$ and $b_2$.

### Affine Model

- The affine model is more complex, but it can represent a large variety of motions
- Its equation is:

$$\mathbf{v}(\mathbf{p}) = \mathbf{b} + \mathbf{B}\mathbf{p} = \begin{bmatrix} b_1 \\ b_2 \end{bmatrix} + \begin{bmatrix} b_3 & b_4 \\ b_5 & b_6 \end{bmatrix} \mathbf{p}$$

- It includes translation as a special case when $\mathbf{B} = 0$
- It is based on 6 parameters, two for $\mathbf{b}$ and four for $\mathbf{B}$
- The relatively small number of parameters makes their estimation robust

### Affine Models: Examples

**Translation:**

[Figura: Vector field showing uniform translation]

$$\mathbf{b} = \begin{bmatrix} 0.5 \\ 2 \end{bmatrix} \qquad \mathbf{B} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$$

$$v_x = 0.5, \quad v_y = 2$$

**Zoom in:**

[Figura: Vector field showing diverging vectors from center (zoom in)]

$$\mathbf{b} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \qquad \mathbf{B} = \begin{bmatrix} 0.5 & 0 \\ 0 & 0.5 \end{bmatrix}$$

$$v_x = 0.5x, \quad v_y = 0.5y$$

**Zoom out:**

[Figura: Vector field showing converging vectors toward center (zoom out)]

$$\mathbf{b} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \qquad \mathbf{B} = \begin{bmatrix} -0.5 & 0 \\ 0 & -0.5 \end{bmatrix}$$

$$v_x = -0.5x, \quad v_y = -0.5y$$

**Rotation:**

[Figura: Vector field showing circular rotation pattern]

$$\mathbf{b} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \qquad \mathbf{B} = \begin{bmatrix} 0 & -0.5 \\ 0.5 & 0 \end{bmatrix}$$

$$v_x = -0.5y, \quad v_y = 0.5x$$

**A Compact Representation:** Despite the visual complexity, the entire motion field is governed by only **6 parameters**, which replace the hundreds of individual vectors that would be needed with block-matching.

The transformation in a real example is a combination of:
1. **Rotation:** The camera tilt.
2. **Zoom In:** The magnifying effect.
3. **Translation:** Global shift.

[Figura: 1. Original Frame ($f_k$); 2. Warped Frame ($f_{k-1}$ transformed); 3. Global Affine Motion Field]

### Indirect Estimation

A first approach consists in first estimating a dense field (e.g. with optical flow), and then deducing the global motion from it solving an optimization problem, typically with least square techniques.

Let $u(n,m)$ and $v(n,m)$ be the estimated dense field components.  
Let $u_\pi(n,m)$ and $v_\pi(n,m)$ be some dense fields depending on the parameter set $\pi$.
- For example, for affine models, $\pi = [b_1\, b_2\, b_3\, b_4\, b_5\, b_6]$

Indirect estimation amounts to:

$$\pi^* = \arg\min_\pi \sum_{n,m \in \mathcal{R}} \left[u(n,m) - u_\pi(n,m)\right]^2 + \left[v(n,m) - v_\pi(n,m)\right]^2$$

- Indirect estimation looks for the parameters that make the model the closest to the estimated MVF
- This distance minimization may be solved with a gradient descent
- **Disadvantage:**
  - Strong dependency from the first dense estimation
  - It needs a support region $\mathcal{R}$ with homogeneous motion

### Direct Estimation

With Direct Estimation, the parameters are introduced in the estimation phase.

For example, OF equation becomes:

$$\pi^* = \arg\min_\pi \sum_{n,m \in \mathcal{R}} \left[u_\pi(n,m) f_x(n,m) + v_\pi(n,m) f_y(n,m) + f_t(n,m)\right]^2$$

Another approach consists in minimizing the SSD or the SAD computed on the parametrized MVF:

$$\pi^* = \arg\min_\pi \sum_{n,m \in \mathcal{R}} [e(n,m)]^2 \quad \text{with}$$

$$e(n,m) = f(n - u_\pi(n,m),\, m - v_\pi(n,m),\, t-1) - f(n,m,t)$$

SAD-based block matching can be seen as a special case of direct parametric estimation where the motion model is a pure translation, i.e. special case of affine model with $\mathbf{B} = 0$.

---

## 5. Deep Learning Methods

### Deep Learning for Motion Estimation

**The Shift in Paradigm:**  
Traditional methods (Differential or Block-based) rely on hand-crafted models. Deep Learning approaches treat motion estimation as a supervised or unsupervised learning problem, typically implemented via Convolutional Neural Networks (CNNs).

**Key Requirements:**
- Specialized architectures for pixel-level correspondence.
- Large-scale datasets for training (Synthetic or Real).
- High computational power for inference (GPUs).

### Training Challenges: Ground Truth Availability

Optical flow ground truth is hard to obtain for real-world sequences.

**Data Solutions:**
- **Synthetic Datasets:** Using computer graphics (e.g., FlyingChairs, Sintel) to provide perfect labels.
- **Data Augmentation:** Geometric and photometric transformations to increase diversity.
- **Unsupervised Learning:** Minimizing the photometric error between the current frame and the warped reference.

### First Generation: FlowNet (2015)

[Figura: FlowNetSimple (FlowNetS) and FlowNetCorr (FlowNetC) architectures with encoder-decoder structure and upconvolution layers]

**Key Concepts:**
- First end-to-end CNN for motion.
- **FlowNetS:** Simple concatenation of input frames.
- **FlowNetC:** Explicit correlation layer between feature maps.

> Dosovitskiy et al. (2015). FlowNet: Learning Optical Flow with Convolutional Networks

**Performance & Bottlenecks:**  
While revolutionary, the first FlowNet models struggled with small displacements and fine details compared to classical variational methods.

- **Data dependency:** Performance is heavily tied to the *Flying Chairs* dataset quality.
- **Inference Speed:** ≈ 10-100 FPS on a mid-range GPU (much faster than traditional global optimization).
- **Weakness:** Large errors in regions with repetitive patterns due to the limited receptive field of early CNN layers.

### Second Generation: FlowNet 2.0

[Figura: FlowNet 2.0 architecture showing stacked FlowNet modules (FlowNetC, FlowNetS, FlowNet-SD) with Large Displacement and Small Displacement branches]

**Improvements:**
- **Stacked** architectures.
- **Specific sub-networks** for small motions.
- **Advanced training** on synthetic data.

> Ilg et al. (2017). FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks

**Architectural Refinement:**  
FlowNet 2.0 stacks multiple FlowNet modules, significantly reducing the End-Point Error (EPE) at the cost of increased complexity.

- **Model Size:** Large memory footprint due to the "stacking" of multiple networks (FlowNetC + FlowNetS).
- **Schedule:** Introduced a complex training schedule (multi-stage training on different datasets).
- **Small Displacement Module:** A specialized sub-network for slow motions, where original FlowNet failed.
- **Efficiency:** Trade-off between FlowNet2 (most accurate) and FlowNet2-s (faster, lighter).

### Third Generation: PWC-Net (2018)

[Figura: PWC-Net architecture with feature pyramids, warping layer, cost volume layer, optical flow estimator, and context network]

**Hybrid Design:**
- **Pyramidal** feature extraction.
- **Feature Warping**.
- **Local Cost Volume** calculation.

> Sun et al. (2018). PWC-Net: CNNs for Optical Flow Using Pyramid, Warping, and Cost Volume

**The Power of Priors:**  
By using Cost Volumes and Warping, PWC-Net achieves SOTA accuracy with 17x fewer parameters than FlowNet2.

- **Complexity:** Extremely efficient. The Cost Volume is computed locally (limited search range), keeping the GPU memory usage low.
- **Execution Time:** ≈ 30ms for Sintel resolution images.
- **Evaluation:** Outstanding results on *KITTI* benchmarks, proving high generalization from synthetic to real-world driving sequences.

### SOTA: RAFT (2020)

[Figura: RAFT architecture with feature encoder, context encoder, all-pairs correlation volume, and GRU update operator producing optical flow]

**Innovation:**
- **Recurrent** update (GRU).
- **All-pairs correlation** volume.
- **No spatial pyramids**.

> Teed & Deng (2020). RAFT: Recurrent All-Pairs Field Transforms for Optical Flow

**The New Standard:**  
RAFT maintains a high-resolution flow field throughout the process, avoiding the loss of detail typical of coarse-to-fine pyramids.

- **Iterative Logic:** The number of GRU iterations can be tuned at inference time (Trade-off: Speed vs. Quality).
- **Complexity:** Computing all-pairs correlation is memory-intensive, but optimized via a "Correlation Pyramid".
- **Generalization:** Unprecedented "zero-shot" generalization (trained on synthetic data, works perfectly on real video).
- **Inference:** Slower than PWC-Net but significantly more precise on thin structures and motion boundaries.

### Synthesis of Deep Learning Architectures

**Evolutionary Milestones:**  
Deep Learning for Motion Estimation has evolved through different paradigms, progressively integrating physical priors and iterative refinement logic.

- **FlowNet (2015/17):** Demonstrated the feasibility of direct dense flow regression using end-to-end CNNs
- **PWC-Net (2018):** Improved efficiency and accuracy by embedding classic vision concepts: Pyramids, Warping, and Cost Volumes
- **RAFT (2020):** Reached state-of-the-art precision through iterative updates using a Gated Recurrent Unit (GRU) and all-pairs correlation

### DL-Based ME: Perspectives and Challenges

**Analysis vs. Compression:**  
While DL methods dominate analysis tasks (Optical Flow), their integration into real-time systems and video coding standards requires balancing accuracy with practical constraints.

**Main Advantages:**
- Robustness to occlusions and large displacements
- High precision in complex textureless areas

**Current Challenges:**
- **Generalization:** Performance drops on data differing from training sets
- **Computational Cost:** High memory and power requirements for SOTA methods

---

## 6. Conclusions

### Motion Estimation: Wrap-up

- Motion Estimation allows to extract motion information from videos
- It focuses on *optical flow* rather than physical motion (other sensors can be used to assess the physical motion)
- Block-matching: conceptually simple, commonly used for video compression
- Neural networks: emerging framework, very effective for analysis tasks

### Summary Diagram

[Figura: Mind map — Motion Estimation → {Optical flow, Block-Matching ME → Temporal Prediction in Video Compression}; Block-Matching ME → Design Parameters: {Block Size, Motion Model (Translation, Affine), Cost Function (SSD, SAD), Vector Precision (e.g. quarter-pixel), Search Area/Strategy, Regularization ($\lambda$, $R(\cdot)$)}; Block-Matching ME → Trade-offs: {Prediction Quality (PSNR), Estimation Time, Coding Cost (Bitrate), Memory Requirements}]
