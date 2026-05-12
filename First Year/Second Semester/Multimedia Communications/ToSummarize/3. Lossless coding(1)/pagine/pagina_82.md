```markdown

Introduction
Princ. Info Theory
Optimal coding
Other Techniques
Neural Lossless Coding
Conclusions

| Symbol | A | B | C | D | E | F |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Probability | 0.4 | 0.2 | 0.15 | 0.15 | 0.05 | 0.05 |

Input sequence: ACFD

▶ Start: [0, 1)

▶ A: [0, 0.4)
Center: 0.2. Precision: $p_1/2 = 0.2$.
$L(1) = -\lceil \log_2 p_1 \rceil + 1$

▶ C: [0.24, 0.30)
Center: 0.275. Precision: $p_1 p_3/2$.
$L(2) = -\lceil \log_2 p_1 + \log_2 p_3 \rceil + 1$

▶ F: [0.297, 0.30)
Center: 0.2985. Precision: $p_1 p_3 p_6/2$.
$L(3) = -\lceil \log_2 p_1 + \log_2 p_3 + \log_2 p_6 \rceil + 1$

54/102 18.03.26 Lossless coding principles Marco Cagnazzo
```