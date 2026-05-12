Copy

x = y is a proper copy operation if it satisfies

• equivalence, i.e., after x = y, any operation f() on x and y yields the same results
• independence, i.e., after x = y, an operation f(x) should not change the state of y

C++ provides

• copy constructor – X(const X&)
  • it initializes a new object and the resources (e.g., memory) it needs, and initializes member values to copy the argument

• copy assignment – X& operator = (const X&)
  • it must deal with an already constructed object (on the left side of the assignment) and its resources

---

**Immagini estratte:**

![Figura estratta 1](images/p29_img01.jpg)
