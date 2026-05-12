Predictive Quantization Drift Example

▶ Simple predictive scheme: prediction is the previous value
▶ 3-bit quantizer (7 levels): [-9, -6, -3, 0, 3, 6, 9]
▶ Encoder uses quantized values for prediction
▶ Decoder uses quantized (reconstructed) values for prediction

| Step | Original Signal | Encoder | Encoder | Decoder | Decoder |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | | Prediction | Error | Quantized Error | Prediction | Received Error | Reconstructed Value |
| 1 | 10 | - | - | 9 | - | 9 | 9 |
| 2 | 11 | 9 | 2 | 3 | 9 | 3 | 12 |
| 3 | 12 | 12 | 0 | 0 | 12 | 0 | 12 |
| 4 | 13 | 12 | 1 | 0 | 12 | 0 | 12 |
| 5 | 14 | 12 | 2 | 3 | 12 | 3 | 15 |
| 6 | 18 | 15 | 3 | 3 | 15 | 3 | 18 |
| 7 | 21 | 18 | 3 | 3 | 18 | 3 | 21 |
| 8 | 18 | 21 | -3 | -3 | 21 | -3 | 18 |

---

**Immagini estratte:**

![Figura estratta 1](images/p116_img01.jpg)
