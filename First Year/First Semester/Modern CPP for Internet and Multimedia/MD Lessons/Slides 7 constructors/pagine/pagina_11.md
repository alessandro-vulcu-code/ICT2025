Destructor

• Generally, it is called implicitly when
• Object goes out of scope
  void f()
  {
    Tracer tr{"a string"};
    tr goes out of scope: ~Tracer() is called on tr
  }

• delete is called on an object in the free store
  Tracer* tr = new Tracer{"a string"};
  // some code
  delete tr;
  tr is deleted: ~Tracer() is called on tr
  // more code

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)
