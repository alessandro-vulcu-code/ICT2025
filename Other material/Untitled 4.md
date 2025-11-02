Certamente. Ecco il documento sull'analisi della dispersione tradotto in inglese e riformattato con le formule $\LaTeX$ racchiuse in `$$ $$` per Obsidian.

---

## 📝 Analysis of Dispersion and Light Propagation in Optical Fibers

### Executive Summary

This document analyzes the fundamental principles governing the propagation of a light pulse within multimode optical fibers and the phenomenon of total internal reflection, based on notes from the "Fiber Optics" course by Luca Palmieri.

- **Multimode Propagation:** A light pulse in a multimode optical fiber is described as a linear superposition of a finite number $N$ of propagating modes. Each mode is characterized by a specific field $\mathbf{E}_n$ and a propagation constant $\beta_n$.
    
- **Dispersion Effect:** Due to the non-negligible bandwidth of the pulse, different spectral components and different modes travel at different speeds. By using a first-order approximation of the propagation constant for narrowband signals, it is shown that the output pulse is the sum of $N$ replicas of the input pulse. Each replica, associated with a specific mode, undergoes a unique time delay, proportional to $\beta_{n,1}z$. This temporal misalignment among modes is the main cause of **intermodal dispersion**, leading to pulse broadening and distortion.
    
- **Total Internal Reflection (TIR):** This is the fundamental physical mechanism that allows light confinement within the fiber core. It occurs when a light wave, traveling in a medium with a higher refractive index ($n_1$), strikes the interface with a medium of a lower refractive index ($n_2$) at an angle of incidence $\theta_i$ greater than the critical angle $\theta_c$. Under these conditions, the entire optical power is reflected, ensuring wave guidance.
    

---

### 1. Light Pulse Propagation in Optical Fiber

The analysis of light pulse propagation in a multimode optical fiber reveals how the modal structure of the medium influences the shape of the transmitted signal.

#### 1.1. Representation of the Electric Field

In a multimode optical fiber, the total electric field $\mathbf{E}$ that propagates can be represented as the linear superposition of all $N$ guided modes. Using the complex phasor representation for sinusoidal fields, the field is described by the following equation:

$$\mathbf{E}(x, y, z) = \sum_{n=1}^{N} c_n \mathbf{E}_n(x, y) \exp(-j\beta_n z)$$

Where:

- $N$: Is the total number of propagating modes.
    
- $c_n$: Are the complex coefficients weighting the contribution of each mode.
    
- $\mathbf{E}_n(x, y)$: Is the transverse field distribution of the $n$-th mode.
    
- $\beta_n$: Is the propagation constant of the $n$-th mode.
    

#### 1.2. Analysis in the Frequency Domain

To describe the propagation of a pulse (which inherently has a non-negligible bandwidth), it is necessary to move to the frequency domain. Assuming the entire field is modulated by a signal with spectrum $A(\omega)$ and neglecting the frequency dependence of the modal fields, the expression becomes:

$$\mathbf{E}(x, y, z, \omega) = A(\omega) \sum_{n=1}^{N} c_n \mathbf{E}_n(x, y) \exp(-j\beta_n(\omega + \omega_0)z)$$

In this equation:

- $\omega_0 = 2\pi f_0$: Is the angular frequency of the optical carrier.
    
- $\omega = 2\pi f$: Is the angular frequency extending over the baseband of the modulating signal.
    
- $A(\omega)$: Is the Fourier transform of the complex signal envelope (baseband spectrum).
    

#### 1.3. Analysis in the Time Domain and the Phenomenon of Dispersion

The electric field in the time domain $\mathbf{e}(t)$ is obtained through the inverse Fourier transform. For narrowband signals, a fundamental approximation is introduced: the **Taylor series expansion of the propagation constant** $\beta_n$, truncated at the first order (linear approximation):

$$\beta_n(\omega + \omega_0) \approx \beta_n(\omega_0) + \left(\frac{d\beta_n}{d\omega}\right)\Big|_{\omega_0} \cdot \omega = \beta_{n,0} + \beta_{n,1}\omega$$

By applying this approximation to the inverse Fourier transform integral, the final expression for the field in the time domain is obtained:

$$\mathbf{e}(t) = \sum_{n=1}^{N} c_n \mathbf{E}_n \exp(-j\beta_{n,0}z) a(t - \beta_{n,1}z)$$

This equation is central to understanding intermodal dispersion:

1. The output signal is the sum of $N$ replicas of the original signal envelope, $a(t)$.
    
2. Each replica, associated with mode $n$, arrives at the destination with a specific time delay $\mathbf{\tau_n = \beta_{n,1}z}$.
    

Since the term $\beta_{n,1}$ (the inverse of the mode's group velocity, $v_{g,n}^{-1}$) is different for each mode, the pulses associated with each mode arrive at different times. This causes the total pulse to broaden and distort, a phenomenon known as modal dispersion.

---
