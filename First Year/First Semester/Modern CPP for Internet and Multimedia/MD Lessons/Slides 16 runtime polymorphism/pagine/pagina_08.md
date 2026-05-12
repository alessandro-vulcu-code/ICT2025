Dynamic cast: pointer vs reference

dynamic_cast works with pointers and references

• the reference must always be associated to an object, and there is no nullptr equivalent for a reference

• dynamic_cast<T&>(r) is an assertion – “the object referred to by r is of type T”
• the dynamic_cast performs a check on whether the assertion is valid or not
• if not valid, a bad_cast exception is thrown
• in general, it is better to use pointers for polymorphism

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)
