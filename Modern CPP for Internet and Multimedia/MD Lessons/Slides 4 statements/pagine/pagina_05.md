Selection statements - if

if (condition) statement

Expression or declaration

Good practice: use a compound statement (i.e., enclose it in a block) – otherwise:
• if there is more than one statement after the if, only the first is considered to be the statement conditioned by the if
• for example, variables can be declared and initialized only in a compound statement
it would be pointless to have a single instruction that declares a variable that is not used as it goes out of scope before the next instruction

• It is possible to declare and initialize a variable in a condition
• The scope ends at the end of the statement after the if
• The condition will test the value of the variable
• Improve locality and minimize uninitialized variables!

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)
