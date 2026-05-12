Default constructors

• Built-in types have default constructors, but they are not implicitly invoked for local or free-store variables
  void f() {
    int a {}; // 0
    int a1; // undefined value
  }

• If a class has data members with types reference or const (which need to be initialized when the object is constructed):
  • use in-class initializers for these variables
  • define a default constructor that initializes them
    struct Work {
      char& flag_ref;
      const char flag{'a'}; // in-class initializer
      Work() {flag_ref[flag]; }; // default constr

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p20_img01.jpg)
