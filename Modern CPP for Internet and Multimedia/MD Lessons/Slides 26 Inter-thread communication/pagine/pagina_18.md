Atomic variables

Fortunatelly, C++11 provides a way to set `exit_flag` in thread-safe way without the need of an additional mutex, by using an Atomic variable: `std::atomic<bool> exit_flag;`

• An operation in an object of an atomic type is atomic, i.e.:
  • it is performed by a single thread without interference from other threads

• An atomic object can be used only for simple operations on basic data types (int, bool)
  • atomic operations are very fast: they are made by the hardware, that makes only very simple operations → significantly faster than lock-based operations (about 1/3 of the complexity)

---

**Immagini estratte:**

![Figura estratta 1](images/p18_img01.jpg)
