Raw pointers leak

• Whenever you need to pass an object outside the scope where you created it (funtions, thread, etc), or when you use hierarchy, you need to create a pointer with new
  • It means you are allocating memory to the heap (or free store), while in the pointer placed int the stack, you just keep the address of the heap where the object is created

• Each time you write the word new, you then need to write the word delete

• Question: who is responsible to perform this operation?

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)
