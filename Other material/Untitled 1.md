

### 1.0 Introduction to LP Modal Theory under the Weak-Guide Approximation

Linearly Polarized (LP) modal theory provides a strategically simplified yet highly accurate framework for analyzing the propagation of light within modern optical fibers. Its importance lies in its ability to reduce the complexity of the full electromagnetic solution without sacrificing significant precision for the most common types of fiber. This simplification is made possible by a key assumption known as the **weak-guide approximation**, which is valid for nearly all contemporary communication fibers.

The foundational assumptions of LP modal theory are as follows:

- **The Weak-Guide Approximation:** This central tenet posits that the refractive indices of the fiber's core ($\mathbf{n_{co}}$) and cladding ($\mathbf{n_{cl}}$) are very close to one another ($\mathbf{n_{co} \approx n_{cl}}$). In practical fibers, this difference is typically on the order of $1\%$ or less.
    
- **Mode Simplification:** The exact solution to Maxwell's equations in a cylindrical step-index fiber yields complex hybrid modes (TE, TM, HE, and EH). The weak-guide approximation allows these distinct mode families to be combined into a single, simpler set of Linearly Polarized ($\mathbf{LP}$) modes. This transformation from a complex vector problem (solving for four coupled hybrid modes) into a much more tractable scalar problem (solving the Helmholtz equation for a single field component) is the key strength of the approximation, making an analytical solution readily attainable.
    
- **Field Characteristics:** Under this approximation, the electromagnetic field propagating in the fiber is considered to be almost purely Transverse Electro-Magnetic ($\mathbf{TEM}$). This means its longitudinal components ($\mathbf{E_z}$ and $\mathbf{H_z}$) are negligible compared to its transverse components. Furthermore, the field is assumed to maintain a nearly constant polarization across the entire cross-section of the fiber.
    

These assumptions provide a robust analytical model that accurately describes the behavior of guided light.

---

### 2.0 Mathematical Formulation of the Guided Modes

The analysis of guided modes begins by decomposing the electromagnetic field into its transverse and longitudinal components within the framework of Maxwell's equations.

The electric ($\mathbf{E}$) and magnetic ($\mathbf{H}$) fields are expressed as having a transverse component (subscript $t$), a longitudinal component (subscript $z$), and a propagation factor:

$$\mathbf{E}(x, y, z) = [\mathbf{E}_t(x, y) + \mathbf{E}_z(x, y) \cdot \mathbf{\hat{z}}] \cdot \exp(-j\beta z)$$

$$\mathbf{H}(x, y, z) = [\mathbf{H}_t(x, y) + \mathbf{H}_z(x, y) \cdot \mathbf{\hat{z}}] \cdot \exp(-j\beta z)$$

The wave equation for the transverse electric field is given by:

$$\mathbf{[1]} \quad \nabla^2\mathbf{E}_t - (\beta^2 - k^2)\mathbf{E}_t = 0$$

All other field components can be found using the following relations:

$$\mathbf{[2]} \quad j\beta E_z = \nabla \cdot \mathbf{E}_t$$

$$\mathbf{[3a]} \quad j\omega\mu_0\mathbf{H}_t = \mathbf{\hat{z}} \times \nabla E_z + j\beta\mathbf{E}_t$$

$$\mathbf{[3b]} \quad j\beta H_z = \nabla \cdot \mathbf{H}_t$$

The wave number $\mathbf{k^2}$ is defined by:

- **In the core:** $\mathbf{k^2 = k_{co}^2 = \omega^2\mu_0\epsilon_{co}}$
    
- **In the cladding:** $\mathbf{k^2 = k_{cl}^2 = \omega^2\mu_0\epsilon_{cl}}$
    

For a guided mode, the propagation constant $\mathbf{\beta}$ must satisfy: $\mathbf{k_{cl} < \beta < k_{co}}$, which translates to an effective refractive index ($\mathbf{n_{eff}}$) constraint:

$$n_{cl} < n_{eff} < n_{co} \quad \text{where } \beta = \left(\frac{\omega}{c}\right) \cdot n_{eff}$$

The following real quantities are defined based on $\mathbf{\beta}$ to simplify the solution:

$$\chi_{co}^2 = k_{co}^2 - \beta^2 \quad (\text{where } \chi_{co}^2 \geq 0)$$

$$\chi_{cl}^2 = \beta^2 - k_{cl}^2 \quad (\text{where } \chi_{cl}^2 \geq 0)$$

$$\chi_{co} = \sqrt{k_{co}^2 - \beta^2}$$

$$\chi_{cl} = \sqrt{\beta^2 - k_{cl}^2}$$

---

### 3.0 Solving the Wave Equation using Separation of Variables

Applying the LP approximation ($\mathbf{E_x = 0}$), the vector wave equation converts to the scalar Helmholtz equation in cylindrical coordinates, $\mathbf{\nabla^2E_y + \chi^2E_y = 0}$, which is solved via separation of variables:

$$E_y(r, \phi) = f(r)g(\phi)$$

This leads to the two independent ordinary differential equations, linked by the separation constant $\mathbf{\nu^2}$:

$$\mathbf{[4]} \quad \frac{d^2g}{d\phi^2} + \nu^2g = 0$$

$$\mathbf{[5]} \quad \frac{d^2f}{dr^2} + \frac{1}{r}\frac{df}{dr} + \left(\chi^2 - \frac{\nu^2}{r^2}\right)f = 0$$

#### Solution for the Azimuthal Component

For physical continuity and periodicity, the separation constant $\mathbf{\nu}$ must be an integer, $\mathbf{n = 0, 1, 2, \dots}$.

#### Solution for the Radial Component

The radial solution depends on the region:

- In the Core ($\chi_{co}^2 > 0$): The solution uses Bessel functions of the first kind ($\mathbf{J_n}$), as $\mathbf{Y_n}$ diverges at $\mathbf{r=0}$.
    
    $$f_{co}(r) = A \cdot J_n(\chi_{co}r)$$
    
- In the Cladding ($\chi_{cl}^2 > 0$): The solution uses modified Bessel functions of the second kind ($\mathbf{K_n}$), as $\mathbf{I_n}$ grows indefinitely as $\mathbf{r \to \infty}$.
    
    $$f_{cl}(r) = B \cdot K_n(\chi_{cl}r)$$
    

---

### 4.0 Derivation of the Characteristic Equation

The allowed propagation constants $\mathbf{\beta}$ are found by enforcing boundary conditions (continuity of $\mathbf{E_{tan}}$ and $\mathbf{D_{norm}}$) at the core-cladding interface ($\mathbf{r=a}$).

Continuity of the Tangential Electric Field ($\mathbf{E_{tan}}$) yields the amplitude ratio:

$$\frac{A}{B} = \frac{K_n(\chi_{cl}a)}{J_n(\chi_{co}a)}$$

The **weak-guide approximation ($\epsilon_{co} \approx \epsilon_{cl}$)** makes the $\mathbf{E_{tan}}$ and $\mathbf{D_{norm}}$ continuity conditions nearly equivalent. The approximate expression for the transverse electric field is:

$$\mathbf{[8]} \quad E_t(r, \phi) = \begin{cases} q \frac{J_n(\chi_{co}r)}{J_n(\chi_{co}a)} \cos(n\phi + \phi_0), & \text{in the core} \\ q \frac{K_n(\chi_{cl}r)}{K_n(\chi_{cl}a)} \cos(n\phi + \phi_0), & \text{in the cladding} \end{cases}$$

Using the continuity of the longitudinal electric field ($\mathbf{E_z}$), the fundamental **Characteristic Equation for LP modes** is derived:

$$\mathbf{[9]} \quad \frac{\chi_{co} a \cdot J'_{n}(\chi_{co} a)}{J_n(\chi_{co} a)} = - \frac{\chi_{cl} a \cdot K'_{n}(\chi_{cl} a)}{K_n(\chi_{cl} a)}$$

---

### 5.0 Mode Cut-Off Conditions and Normalized Parameters

A mode's **cut-off** condition occurs when its propagation constant equals that of the cladding, $\mathbf{\beta = k_{cl}}$, causing $\mathbf{\chi_{cl} = 0}$. The cut-off condition derived from [9] is:

$$J_n(\chi_{co} a) = 0 \quad \text{or} \quad J_{n \pm 1}(\chi_{co} a) = 0$$

- The **fundamental mode, $\mathbf{LP_{0,1}}$, has a cut-off frequency of zero** and propagates at all wavelengths.
    
- The first higher-order mode is $\mathbf{LP_{1,1}}$, with an approximate cut-off wavelength:
    
    $$\lambda_{c,11} \approx 2.612 \cdot a \cdot NA$$
    

To establish universal dispersion curves, the following normalized parameters are used:

- Normalized Frequency (V-number):
    
    $$V = \frac{2\pi a}{\lambda} \cdot NA$$
    
- Normalized Propagation Constant:
    
    $$b = \frac{\beta^2 - k_{cl}^2}{k_{co}^2 - k_{cl}^2}$$
    

#### 5.1 Experimental Verification of Cut-Off

The cut-off wavelength is experimentally verified using the **bend-loss method**. The principle is that modes closer to cut-off are more sensitive to bend losses. Measuring the spectrum difference between a straight and a bent fiber reveals loss peaks, which correspond to the wavelengths at which specific mode groups ($\mathbf{LP_{1,1}}$, $\mathbf{LP_{0,2}/LP_{2,1}}$, etc.) are stripped away by the bend.

---

### 6.0 Physical Properties and Degeneracy of LP Modes

Mode **degeneracy** refers to multiple modes sharing the same propagation constant $\mathbf{\beta}$, arising from the fiber's cylindrical symmetry.

- **Polarization Degeneracy:** Every $\mathbf{LP_{n,p}}$ mode has two orthogonal polarization states (e.g., $x$ and $y$ polarized) that share the same $\mathbf{\beta}$, resulting in a **two-fold degeneracy**.
    
- **Azimuthal Degeneracy:** For $\mathbf{n > 0}$, the azimuthal term $\mathbf{\cos(n\phi + \phi_0)}$ has $\mathbf{\cos(n\phi)}$ and $\mathbf{\sin(n\phi)}$ components, representing two distinct spatial orientations, adding another **two-fold degeneracy of orientation**.
    

**Total Degeneracy Summary:**

- $\mathbf{LP_{0,p}}$ modes: **Two-fold degenerate** (Polarization only).
    
- $\mathbf{LP_{n,p}}$ modes ($\mathbf{n > 0}$): **Four-fold degenerate** (Polarization and Azimuthal orientation).
    

---

### 7.0 Power Propagation and Orthogonality

Power propagation is analyzed using the time-averaged Poynting vector ($\mathbf{P}$), which, under the weak-guide approximation, is directed along the fiber axis ($\mathbf{\hat{z}}$):

$$\mathbf{H}_t \approx \left(\frac{\beta}{\omega\mu_0}\right) \cdot (\mathbf{\hat{z}} \times \mathbf{E}_t)$$

$$\mathbf{P} = \frac{1}{2} \cdot \mathbf{E}_t \times \mathbf{H}_t^* = \left(\frac{\beta}{2\omega\mu_0}\right) \cdot |\mathbf{E}_t|^2 \cdot \mathbf{\hat{z}}$$

The LP modes possess the fundamental property of **orthogonality**, meaning the spatial cross-product of any two different modes ($\eta$ and $\nu$) integrated over the cross-section ($\mathbf{S}$) is zero:

$$\frac{1}{2} \int_S (\mathbf{E}_\eta \times \mathbf{H}_\nu^*) \cdot \mathbf{\hat{z}} dS = \delta_{\eta,\nu}$$

The profound implication is that when multiple modes propagate simultaneously, the **total power ($\mathbf{W}$) is a linear sum** of the powers carried by each individual mode, dramatically simplifying multi-mode fiber analysis:

$$W = \sum_{\eta} |c_\eta|^2$$

where $\mathbf{c_\eta}$ is the excitation coefficient of the $\eta$-th mode.

---

Would you like me to elaborate on the physical meaning of the V-number and its importance in determining whether a fiber is single-mode or multi-mode?