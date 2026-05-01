# Dictionary Coding: Advanced Insights

## The LZW Patent Controversy

- GIF used LZW, which was patented by Unisys.
- In the late 90s, Unisys began enforcing royalties for software developers.
- PNG was developed as a "free" alternative, choosing LZ77 (Deflate) specifically to bypass these legal constraints.

## Modern Web (Brotli & Zstd)

- Modern algorithms like Brotli use a static dictionary.
- This dictionary contains common strings found in web traffic (HTML tags, JS keywords).
- Pre-warming the dictionary allows for high compression even on very small files.

---

**Immagini estratte:**

![Figura estratta 1](images/p153_img01.jpg)
