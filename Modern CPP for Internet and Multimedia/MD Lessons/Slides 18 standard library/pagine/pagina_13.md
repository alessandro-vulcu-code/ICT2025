Container adaptors

They are not containers, they just provide interfaces to other containers for specific functions (in particular, push and pop operations)

1. `std::priority_queue<T, C, Cmp>`  
   it creates a priority queue out of the elements of type T in the container C (by default `std::vector<T>`), according to the priority set by the function Cmp

2. `std::queue<T, C>`  
   queue of elements of type T in a container C (by default `std::deque<T>`)

3. `std::stack<T, C>`  
   stack of elements of type T in a container C (by default `std::vector<T>`)

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)
