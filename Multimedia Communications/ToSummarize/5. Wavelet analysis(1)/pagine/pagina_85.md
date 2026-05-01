EZW algorithm

1. $k = 0$
2. $n = \lfloor \log_2(|c|_{\max}) \rfloor$
3. $T_k = 2^n$
4. Let $\mathcal{L}$ be the list of all the DWT coefficients, according to the SB scan order (each SB in raster scan)
5. Let $\mathcal{S} = \emptyset$ be the list of significant coefficients
6. while (rate < available rate)
   ▶ Dominant pass
   ▶ Refining pass
   ▶ $T_{k+1} \leftarrow T_k/2$
   ▶ $k \leftarrow k+1$
7. end while

---

**Immagini estratte:**

![Figura estratta 1](images/p85_img01.jpg)
