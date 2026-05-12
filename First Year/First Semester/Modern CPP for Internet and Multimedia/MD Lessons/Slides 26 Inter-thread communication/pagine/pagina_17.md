Producer – consumer – exit flag

The previous solution is thread safe, but there are 2 issues:

1. The consumer thread has a while-true statement, i.e. it never ends
   - Solution: while(true) → while(exit_flag) with exit_flag a shared boolean flag
   - The main sets exit_flag to false before joining. Thread-safe? NO!

2. The condition variable predicate is locked until data is inserted in queue (that may never arrive): how to exit from this wait?
   - Sol1: wait_for(lk,max_time,pred) allows exiting after a time max_time
   - Sol2: insert exit_flag (i.e., the same boolean flag of the while) into the pred, and let the main notifying it to the condition variable after setting it. Is it thread safe? NO!

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)
