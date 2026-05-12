Condition variable (cv) – 2

The (most important) object methods (2) are:

- cv.wait_for(lck,max_time,pred);
  • It unlocks the mutex acquired by the unique_lock lck until either the predicate pred becomes true or the time max_time elapsed. Then it locks the mutex again.
  • pred must be a boolean function (or a lambda)
  • max_time is of type std::chrono::duration<R,P>, e.g., std::chrono::milliseconds

- cv.notify_one();
  • It unblocks one thread waiting in cv

- cv.notify_all();
  • It unblocks all threads waiting in cv

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)
