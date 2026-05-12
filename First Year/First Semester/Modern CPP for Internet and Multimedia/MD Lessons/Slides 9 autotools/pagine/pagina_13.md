```markdown

./configure (shell script)

• Configure determines platform characteristics and features as specified in configure.ac, and stores the check result in config.status
• Configure runs config.status, that creates the makefiles from Makefile.in
• Configure creates config.log, that contains information about configure process and all the events of a configure fails

Makefile.in is a makefiles template, and the user cannot compile with make before running the configure.

• The configure adds platform characteristics into the makefile (uname, host, CPU, target)
• The configure adds also user specified optional features (paths, enable tests, others)
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)
