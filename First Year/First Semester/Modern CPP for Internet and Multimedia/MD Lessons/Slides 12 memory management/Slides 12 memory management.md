<!-- Pagina 1 -->

Memory management in C++

Modern C++ Programming for ICT
Filippo Campagnaro
campagn1@dei.unipd.it

---

**Immagini estratte:**

![Figura estratta 1](images/p01_img01.jpg)

![Figura estratta 2](images/p01_img04.jpg)

![Figura estratta 3](images/p01_img03.jpg)

![Figura estratta 4](images/p01_img02.jpg)


---

<!-- Pagina 2 -->

Outline

1. C++ programs memory
2. new/delete operators
3. Issues with memory management
4. Resource Acquisition Is Initialization (RAII)

[c++pl] Chapters 9, 11

Chapter 3 from Meyers, S. (2005). *Effective C++: 55 specific ways to improve your programs and designs*. Pearson Education.

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

C++ program memory

Different areas of memory have different uses:

1. **const data area**
   - for data known at compile time
   - no user-defined types (only built-in)
   - available throughout the whole program lifetime
   - read-only

2. **stack**
   - memory for “automatic” variables (e.g., local variables in functions)
   - the memory is allocated sequentially (just before an object is created)...
   - and de-allocated sequentially (stack unwinding)
   - it is not possible to directly manipulate this area of memory

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

C++ program memory

3. free store/heap
• memory allocated with operator new and released with operator delete
• the memory allocation may not match the object lifetime
• this storage can be accessed and manipulated with *void – but there is no direct access to object non-static members or functions

4. global/static memory
• for global and static variables
• it is initialized the first time a global/static variable is met during the execution of the program flow

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)


---

<!-- Pagina 5 -->

C++ memory

Ordered, on top of each other

Stack

Heap

@fhinkel

https://medium.com/fhinkel/confused-about-stack-and-heap-2cf3e6adb771

5

---

**Immagini estratte:**

![Figura estratta 1](p05_img01.jpg)

![Figura estratta 2](p05_img02.jpg)


---

<!-- Pagina 6 -->

Operators new and delete

The free store memory is accessed through the operators

• new
  1. initializes memory and assigns a value
  2. returns a pointer to the memory area

• delete
  1. (in case) call the destructor of the object
  2. deallocate the heap memory

• generally, use {} (or ()) when initializing with new

```cpp
void f() {
  int* a {new int{10}};
  // some code
  delete a;
}
```

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)


---

<!-- Pagina 7 -->

new and delete for arrays

• Array of objects can also be created with new[]
• delete[] can be used to deallocate the whole array
• delete instead applies to the individual objects

This assumes that delete knows the size of the object (or the array of objects) that it has to delete
• Allocations performed with new thus have a small memory overhead to store this information

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)


---

<!-- Pagina 8 -->

new and delete implementation

```cpp
// allocate space for individual object
void* operator new(size_t) throw(std::bad_alloc);

// if (p) deallocate space allocated using operator new()
void operator delete(void* p);

// allocate space for array
void* operator new[](size_t) throw(std::bad_alloc);

// if (p) deallocate space allocated using operator new[]()
void operator delete[](void* p);

new operator vs operator new():
  • the second (operator new()) can be used by the first to allocate size_t uninitialized memory
  • the first (new) is used to construct an object on the free storage or heap, i.e., in order, it calls operator new() and then the constructor of the object
```

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)


---

<!-- Pagina 9 -->

new and delete implementation

• They are defined in the `<new>` header
  • but to use the new operator it is not necessary to include this header

• It is possible to overload new and provide additional parameters to customize its behavior

• delete should be overloaded to cope with the equivalent new

• Example: `placement syntax`
  • additional parameter that represents and area in memory that has already been allocated

```c
char *buf = new char[sizeof(string)]; // pre-allocated buffer
std::string *p = new (buf) std::string("hi"); // placement new
std::string *q = new std::string("hi"); // ordinary allocation
```

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Memory management issues

In general, it is hard to track the state of the objects in the free store

1. Memory leaks
   • call new and never call delete
   • if this is frequent, the system may run out of memory

```c
int f() {
    int* a {new int{10}};

    if (*a = 10)
    {
        return 4;
    }
    delete a;
    return 5;
}
```

if *a is 10, this delete is never reached and the memory pointed by a is never released

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Memory management issues

2. Premature deletion (dangling pointer)
• call delete and then try to reuse the pointer
• this leads to bad write/read operations

```c
int f() {
    int* a {new int{10}};

    if (*a = 10)
    {
        delete a;
    }

    // some code
    *a = 5;
}
```

if *a is 10, the area of memory which a was associated to could now be associated to something else

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

Memory management issues

3. Double deletion
• call delete and then call delete again
• this leads to memory corruption

```c
int f() {
    int* a {new int{10}};

    if (*a = 10)
    {
        delete a;
    }

    // some code
    delete a;
}
```

if *a is 10, the area of memory which a has already been released

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Resource management

These issues extend in general to resources

• a resource is something that is obtained from the OS, and should be returned to it

• examples include
  • memory (heap)
  • files (e.g., through file descriptors)
  • locks for concurrency
  • sockets

• we will focus on the strategies to handle memory, but they can be extended to any of these types of resource

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Efficient memory management

Do not use **new** for local objects
they can be put in the stack

Do not use “naked”
**new** and **delete**
use handle classes

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Resource Acquisition Is Initialization

• Objects (handle classes) can be used to manage resources
• RAII paradigm
  1. Acquire the resources (e.g., memory with new) and
  2. Immediately turn its control to resource-managing objects
• Called RAII because the same statement is used to initialize the handle & acquire the resources
• The resource-managing object then uses its destructor to make sure the resources are released (e.g., calls delete)
  • The destructor of such objects is automatically called when they go out of scope!

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p15_img01.jpg)


---

<!-- Pagina 16 -->

Simple handle class for int*

```cpp
class Handle {
    int* p; // pointer to int
public:
    Handle(int* pp) :p{pp} { }
    int& operator*() { return *p; }
    ~Handle() { delete p; }
};

// example of usage
void f()
{
    Handle obj_handle {new int{10}};
    std::cout << *obj_handle;
} // obj_handle goes out of scope
// and calls delete on p
```

this overrides the dereferencing operator *, so that dereferencing on the handle returns the value of the object pointed to by the member pointer.

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p16_img01.jpg)


---

<!-- Pagina 17 -->

Copy semantic and handle classes

Shallow copy issue: a default copy may not have the results you expect

Other strategies:

1. Prohibit copying (by using =delete or making the copy constructor private)
   Sometimes it does not make sense to copy a resource

2. Reference-count the resource
   Count how many RAII objects point to the resource, increase this by one when copying

3. Transfer ownership
   This however is closer to the move semantic

4. Copy the underlying resource
   Deep copy

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)


---

<!-- Pagina 18 -->

Access to the resources from handles

• It can be useful to provide a way to access the underlying resources
  • for example, an API may accept the raw resource as argument

• This may break encapsulation, but it is not a major problem

1. Get methods (explicit)
2. Implicit conversion (e.g., by overloading * operator)

---

**Immagini estratte:**

![Figura estratta 1](p18_img01.jpg)
