Mutual exclusion – mutex

• A `mutex` (i.e., a mutual exclusion variable) is an object used to represent the exclusive right to access some resource.

• Only one thread can own a mutex at a time

• To access a resource in `thread-safe way`: acquire the mutex, access the resource, release the mutex.

• To `acquire` a mutex means to gain its exclusive ownership
  • Acquire a mutex may block the thread executing it

• Once the mutex is acquired, you can `access` a critical region without risk of data race

• To `release` a mutex means relinquishing exclusive ownership
  • a release operation will unblock waiting threads.

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)
