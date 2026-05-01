```markdown

Optimal coding

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
```