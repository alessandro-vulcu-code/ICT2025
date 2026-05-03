Fields in structures

• A bool is at least large as a char
• If a section of the code uses multiple flags, they can be packed together as fields (or bitfields) of a struct
• Notice that this may not lead to optimizations (e.g., larger compiled code but smaller memory space)
• Useful to conform to an external layout (e.g., a packet header)
• The syntax is type variable : number_of_bit
• The address of a bitfield cannot be taken, because it may not begin at the beginning of a byte

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)
