Initialization without constructors

3. Default initialization

It can be called with {}, and it initializes every member to {} (i.e., its default initialization)

DO NOT forget the {}

The default initialization also works without the {}, but the behavior is complex and may lead to errors:

• statically allocated objects: exactly as if {} was used
• local variables and free store objects (the majority of objects you’ll ever use)

• members with user-defined types are default-initialized (e.g., the std::string name in struct Work is initialized to “”)

• members with built-in types are left uninitialized (e.g., the int number in struct Work has an undefined value)

• this difference may be lost when developing: always use {} to default initialize

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p15_img01.jpg)
