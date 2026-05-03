Compiler

• Parses (linguistic analysis) the translation unit
• Converts it to assembly code (still human readable ASCII) for a specific CPU instruction set
• Optimizes the assembly code: the use of the registers is minimized, and eliminates the parts of the code that do not need to be executed. Different levels of optimization:
  • O0 (Minimum optimizer) doesn’t optimize: fast compilation, slow code, used for debugging
  • O1 (Restricter optimizer) just removes unused lines, used for debugging
  • O2 (High optimization, DEFAULT) minimizes the use of register, harder to debug
  • O3 (Maximum optimization) optimizes more, poor debug view
• Converts the assembly code into the specific machine instructions producing the actual binary: the object file.
• The compilation step is performed on each translation unit: each translation unit is compiled into a binary object file

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)
