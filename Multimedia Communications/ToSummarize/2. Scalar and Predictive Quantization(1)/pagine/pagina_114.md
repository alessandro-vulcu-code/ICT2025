Predictive Quantization Drift Example

▶ Simple predictive scheme: prediction is the previous value
▶ 3-bit quantizer (7 levels): [-9, -6, -3, 0, 3, 6, 9]
▶ Encoder uses non-quantized values for prediction
▶ Decoder uses quantized (reconstructed) values for prediction

| Step | Original Signal | Encoder | Encoder | Decoder | Decoder |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | | Prediction | Error | Quantized Error | Prediction | Reconstructed Value |
| 1 | 10 | - | - | 9 | - | 9 |
| 2 | 11 | 10 | 1 | 0 | 9 | 0 |
| 3 | 12 | 11 | 1 | 0 | 9 | 0 |
| 4 | 13 | 12 | 1 | 0 | 9 | 0 |
| 5 | 14 | 13 | 1 | 0 | 9 | 0 |
| 6 | 18 | 14 | 4 | 3 | 9 | 3 |
| 7 | 21 | 18 | 3 | 3 | 12 | 3 |
| 8 | 18 | 21 | -3 | -3 | 15 | -3 |

68/78 06.03.26 Scalar and Predictive Quantization Marco Cagnazzo

---

**Immagini estratte:**

![Figura estratta 1](images/p114_img01.jpg)
