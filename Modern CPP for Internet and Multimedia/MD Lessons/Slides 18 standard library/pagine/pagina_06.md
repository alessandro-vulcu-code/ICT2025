stdlib containers

Containers are implemented using templates, with template types for the

• type of object
• allocator, i.e., the function used to allocate and release memory resources – by default `std::allocator<T>` is the pair `new/delete` on objects of type T
• key (if required)
• type of comparison (if required) – for example `<, =`
• a hash function (if required)

It is possible to obtain the size of a container (`c.size()`), check it is empty (`c.empty()`), etc

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)
