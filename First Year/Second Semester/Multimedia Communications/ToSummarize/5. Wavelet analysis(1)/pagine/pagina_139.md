Trade-off between robustness and rate

Error robustness can be achieved by several strategies:

▶ Error correction codes are very effective but demand a considerable increase of the coding rate: they are typically used only on small, sensitive data such as heades and metadata

▶ Error robustness of compressed signals is achieved by using markers that allow to recover the synchronization of the lossless code and stop error propagation

▶ Markers are periodically inserted into the bit-stream: increasing the period improves robustness because stops earlier the propoagation of errors.

▶ However, using markers increase the file size and also request marker emulation preventions strategies, usually achieved with bit stuffing, with further file size increase

---

**Immagini estratte:**

![Figura estratta 1](images/p139_img01.jpg)
