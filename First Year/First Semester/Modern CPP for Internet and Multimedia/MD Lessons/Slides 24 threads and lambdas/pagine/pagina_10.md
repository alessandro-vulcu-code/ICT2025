Threads advantages (vs process)

• All the threads of the same process implicitly share the same address space, but they are independent for what concerns execution. This ability is essential for certain applications.
  • E.g., this makes a lot easier infra-threads communication than infra-processes communication

• Threads are easier to create, destroy and manage than processes, because their context is more lightweight.

• It is more efficient to switch from thread to thread (within the same process), that from process to process.

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)
