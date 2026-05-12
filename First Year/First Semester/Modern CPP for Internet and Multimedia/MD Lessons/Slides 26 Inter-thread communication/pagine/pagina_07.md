Busy waiting (or spinning)

• The synchronization required to protect a critical region is known as mutual exclusion.

• Solution 1: busy waiting (or spinning): repeatedly checks to see if a condition is true
  • With this code the CPU load goes 100%: it’s not the way to go!
  • Sleeping between cycles would reduce the CPU load, but how much should it sleep?
    • Trade off between speed and load
    • Used only for hardware iterations

• With multiple consumers we may have a race condition!
  • This happens if the second consumer checks the q size just before the first consumer performs the pop

• There must be a better way!

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)
