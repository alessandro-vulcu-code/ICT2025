POSIX Signals

• When a signal is sent, the operating system interrupts the target process' normal flow of execution to deliver the signal. If the process has previously registered a signal handler, that routine is executed. Otherwise, the default signal handler is executed.

• Most common signals:
  • SIGABRT // abort the process, usually caused by another signal
  • SIGFPE // erroneous arithmetic operation (division by 0)
  • SIGINT // interrupt the process from terminal (CTR+C)
  • SIGKILL // terminate immediately the process (cannot be caught)
  • SIGPIPE // write to a pipe (mechanism for inter-process communication) without a process connected to the other hand
  • SIGSEGV // invalid virtual memory reference or segmentation fault
  • SIGTERM // identical to SIGINT

---

**Immagini estratte:**

![Figura estratta 1](images/p32_img01.jpg)
