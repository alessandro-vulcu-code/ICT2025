# Input sequence: ACFD

- **Start:** [0, 1]
- **A:** [0, 0.4)
  Center: 0.2. Precision: $p_1/2 = 0.2$.
  $L(1) = -\lceil \log_2 p_1 \rceil + 1$
- **C:** [0.24, 0.30)
  Center: 0.275. Precision: $p_1 p_3/2$.
  $L(2) = -\lceil \log_2 p_1 + \log_2 p_3 \rceil + 1$
- **F:** [0.297, 0.30)
  Center: 0.2985. Precision: $p_1 p_3 p_6/2$.
  $L(3) = -\lceil \log_2 p_1 + \log_2 p_3 + \log_2 p_6 \rceil + 1$
- **D:** [0.29925, 0.2997)
  Center: 0.299475. Precision: $p_1 p_3 p_6 p_4/2$. $L(3) = -\lceil \log_2 p_1 + \log_2 p_3 + \log_2 p_6 + \log_2 p_4 \rceil + 1$

![Graph](image_url)