Sequence containers

1. `std::vector<T, A>`  
   contiguous allocation

2. `std::deque<T, A>`

3. `std::list<T, A>`  
   non-contiguous allocation

4. `std::forward_list<T, A>`  
   type of the object in the container

   type of the allocator, by default `std::allocator<T>` (no need to change it unless for specific reasons)

in general, use `std::vector<T>` unless you have other specific needs

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)
