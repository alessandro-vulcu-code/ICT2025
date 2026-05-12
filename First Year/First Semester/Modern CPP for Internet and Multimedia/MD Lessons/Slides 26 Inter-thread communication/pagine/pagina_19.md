Atomic variables – 2

• The most important methods (all thread-safe, but not the initialization):

  • `std::atomic<int> sn(0); → initialization of an atomic integer variable`
  • `int x = sn.load(); → get the valuer of sn atomically. Same of x = sn;`
  • `sn.store(5); → set the valuer of sn atomically. Same of sn=5;`
  • `int old_sn = sn.exchange(3); → set the valuer of sn atomically and obain the old value of sn.`

• Use atomic only for shared flags or counters

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p19_img01.jpg)
