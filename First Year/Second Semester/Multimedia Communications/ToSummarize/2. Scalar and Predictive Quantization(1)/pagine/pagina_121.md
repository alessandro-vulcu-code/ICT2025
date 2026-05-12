PQ prediction error

Let us look more closely to the quantized prediction error. In this example, $L = 19$, so the estimated rate is $\log_2 19 \approx 4.25$ bits per sample.

However, we observe that most of the quantization indexes ($\approx 84\%$) are zero. We could use a variable lenght code that uses a short codeword for the index 0 and possibly longer codewords for indexes outside $(-3, 3)$, which account for less than 1% of the total.

Encoding the quantizations indexes with non-trivial encoding strategy (called entropy coding), as we will see later on) changes dramatically the results

---

**Immagini estratte:**

![Figura estratta 1](images/p121_img01.jpg)
