# Deadzone quantization

Pushing further this idea, we can design a quantizer where the central cell is larger than the others. This allows for removing more small-valued oscillations, while keeping a fine resolution on non-zero values. This is called deadzone quantization (DZQ) and is very commonly used in data compression. Using the threshold value $\tau$, the DZQ can be implemented as:

$$i = \begin{cases} 
\operatorname{sign}(x) \cdot \left\lfloor \frac{|x| + \frac{\tau}{2}}{\Delta} \right\rfloor & \text{if } |x| \ge \tau \\
0 & \text{if } |x| < \tau 
\end{cases}$$

$$\hat{x} = \begin{cases} 
\operatorname{sign}(i) \cdot \Delta \left( |i| + \frac{1-\tau}{2} \right) & \text{if } i \neq 0 \\
0 & \text{if } i = 0 
\end{cases}$$

encoder

decoder

---

**Immagini estratte:**

![Figura estratta 1](images/p37_img01.jpg)
