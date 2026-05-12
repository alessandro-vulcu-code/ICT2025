Why C++, if I’ve learnt Java!

• Java works over a Virtual Machine: your software is “compiled” for the virtual machine, whose interpreter “translates” the instructions for the VM to the instructions for the actual hardware architecture.

• In C++ you must compile in machine code for the target machine for which the code has to be executed, using the proper tool-chain (arm, x86, x64, etc.)

• Way faster: the code is directly executed to the machine!
  • Pay attention: bad programming in C++ may result in slow software

• Drawback: if your software needs to run in different target machines, you need to cross compile it for each target

• In TLC you must be fast (e.g., in a Gbps router, the routing software can’t be the bottleneck!)

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)
