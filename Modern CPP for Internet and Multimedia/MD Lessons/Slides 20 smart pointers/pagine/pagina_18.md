Shared pointer

• `std::shared_ptr<string> sp = std::make_shared<string>("s");` is the exception-safe way to create a shared pointer:
  • It handles the case when the object is created but there’s a memory allocation fail to create the pointer: it is a (really rare) leak
• `sp.use_count();` // provides the value pointed by `use_count`
• `sp.use_reset();` // sp decreases the counter by 1 and then loses the pointer it was pointing to, loosing also the counter value. It becomes an empty shared pointer pointing to `nullptr`
• `string* p = sp.get();` // returns the raw pointer
• A custom deleter can be used
  • In this course we just use the default one

---

**Immagini estratte:**

![Figura estratta 1](images/p18_img01.jpg)
