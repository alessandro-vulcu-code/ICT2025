<!-- Pagina 1 -->

Smart pointers

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

1. Resource Management – raw pointers problem
2. Unique Pointer
3. Shared Pointer
4. Weak Pointer

MORE INFO: “The C++ Programming Language”, B. Stroustrup, Fourth Edition, Addison-Wesley, CH 34.3
"Effective Modern C++", Scott Meyers, First Edition, O-Reilly, CH 4 - 6

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

5 minutes questions

• What is an lvalue?
• What is an rvalue?

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

Raw pointers leak

• Whenever you need to pass an object outside the scope where you created it (funtions, thread, etc), or when you use hierarchy, you need to create a pointer with new
  • It means you are allocating memory to the heap (or free store), while in the pointer placed int the stack, you just keep the address of the heap where the object is created

• Each time you write the word new, you then need to write the word delete

• Question: who is responsible to perform this operation?

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)


---

<!-- Pagina 5 -->

Dangling pointer - example

You are trying to access a pointer whose associated object has been deleted, so it doesn’t point to any valid memory.

Very dangerous: in the case the distruction is still pending, you may access the old content, so your test may not recognize it.

```cpp
char* buffer = new char [256];
delete []buffer;
std::cout << *buffer
```

THIS IS A DANGLING POINTER!
RESULT = UNDEFINED BEHAVIOR
ONE of the MAIN BUGS in C++

```cpp
char* buffer = new char [256];
delete []buffer; // now buffer is dangling
buffer = null; // now it is not dangling anymore
```

---

**Immagini estratte:**

![Figura estratta 1](p05_img01.jpg)


---

<!-- Pagina 6 -->

Raw pointers leak - example

```c
int performTask() {
    char* buffer = new char [256];

    ...
    ... // Some code here
    ... // of several lines
    ... // that may trow exception
    ... // or return something
    ... // before the end is reached
    ...
    delete []buffer;
    return 0;
}
```

THIS IS A LEAK!

Unless you don’t handle each case, remembering to write delete[] everywhere (in each try-catch blocks, before each return, etc.)

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)


---

<!-- Pagina 7 -->

Raw pointers memory leak - example

```c
int performTask() {
    char* buffer = new char [256];
    ...
    ...
    ...
    if(<some_condition>) {
        return 1;
    }
    delete []buffer;
    return 0;
}
```

THIS IS A MEMORY LEAK!

Unless you don’t handle each case, remembering to write delete[] everywhere (in each try-catch blocks, before each return, etc.)

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)


---

<!-- Pagina 8 -->

Raw pointers memory leak - example

```c
int performTask() {
    char* buffer = new char [256];

    ...
    ...
    ...
    if(<some_condition>) {
        delete []buffer;
        return 1;
    }
    delete []buffer;
    return 0;
}
```

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)


---

<!-- Pagina 9 -->

Pointers: avoiding leaks

• Sol1: handle each case, paying attention to writing `delete[]` everywhere the scope may be interrupted (in each `try-catch` blocks, before each `return`, etc.)
  • Writing code like this is very messy, you must pay a lot of attention and it is hard to maintain

• Sol2: RAII (Resource allocation is initialization), i.e., let a wrapper class allocate the pointer on construction and remove the allocation on destruction

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Smart Pointers

Like usual, the standard library does it for you 😊
It provides 3 pointer wrappers to do that:

• Unique pointer
  • a scoped pointer
• Shared pointer
  • to pass the pointer around between methods and threads
• Weak pointer
  • to avoid smart pointer circular (or cyclic) reference

• With shared and unique pointers, you can use → like with pointers
• To use them, #include<memory>

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Unique pointer

Unique pointer
it is a scoped pointer, i.e.:

• its constructor takes a new raw pointer and wraps it
  `std::unique_ptr<string> up(new std::string("ciao"));`

• its destructor performs the delete
  • i.e., the pointed object is destroyed when up goes out of scope, or when it is assigned to another unique pointer

Main characteristics:

• It cannot be copied (no copy constructor), just moved
• It is the most lightweight smart pointer
• It represents the exclusive ownership of a pointer

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

Unique pointer – who owns it?

• `std::unique_ptr<string> up2 = up; // not allowed!!`

• `std::unique_ptr<string> up2 = std::move(up); // up releases its ownership of its raw pointer, and gives it to up2`

```cpp
void function f1(std::unique_ptr<T1> up) {
    //do stuff
}

std::unique_ptr<T1> up1 (new T1 ());
f1(up1); // not allowed!!

f1(std::move(up1)); // IT WORKS, BUT BE AWARE THE OBJECT IS DESTROYED INSIDE THE FUNCTION f1!!!
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Unique pointer – pass it to a function

Sol1: move it to the argument of the function, and return it.

• Returning a unique pointer by value means moving it, i.e., returning it with move()

```cpp
std::unique_ptr<T1> f1(
    std::unique_ptr<T1> up) {
    //do stuff with up
    return up; // returns it by move
}

std::unique_ptr<T1> up1(new T1());
up1 = f1(std::move(up1));
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Unique pointer – pass it to a function - 2

Sol2: pass it by const ref

```cpp
void f2(
    const std::unique_ptr<T1>& up) {
    //do stuff with up
}

std::unique_ptr<T1> up1(new T1());
f2(up1);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Unique pointer

Other useful stuff:

• `string* s = up.release();` // returns the raw pointer, and up releases its ownership: up won’t point to it anymore and won’t delete it when destroyed. up now points to nullptr

• `up.reset();` // up loses the ownership of the pointer and destroys the object

• `up.reset(new string("hi"));` // up loses the ownership of the old pointer and destroys the old object acquiring the ownership of the new pointer

• Explicit constructor (no implicit constructor)

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p15_img01.jpg)


---

<!-- Pagina 16 -->

Shared pointer

• It represents shared ownership.
  std::shared_ptr<string> sp(new string("ciao")); // *use_count = 1

• It is a counted pointer: it keeps track of how many shared pointers are pointing to the object (the copy constructor increments a pointer to a counter use_count)
  std::shared_ptr<string> sp2 = sp; // *use_count=2

• When the counter becomes zero, the pointer will be deleted automatically
  • The destructor does something like this:
    (*use_count)--;
    if(*use_count ≤ 0) {
      delete p;
    }

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p16_img01.jpg)


---

<!-- Pagina 17 -->

Shared pointer example

```cpp
int fun1(shared_ptr<T1> sp) { //*use_count=3
  sp... //DO STUFF
  return 0;
} //sp goes out of scope: *use_count=2

main() {
  shared_ptr<T1> sp1 =
    make_shared <T>(val); // *use_count = 1

  auto sp2 = sp1; // *use_count = 2
  int x = fun1(sp1);
} // sp1 and sp2 go out of scope:
// *use count = 0, pointed object is
// destroyed
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)


---

<!-- Pagina 18 -->

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

![Figura estratta 1](p18_img01.jpg)


---

<!-- Pagina 19 -->

Shared pointer Cast

• Dynamic cast: std::dynamic_pointer_cast<D>(s_ptr)
• Static cast: std::static_pointer_cast<D>(s_ptr)
• Const cast: std::const_pointer_cast<const D>(s_ptr)

E.g., D derives from B.

```cpp
std::shared_ptr<B> pb = std::make_shared<D>();
std::shared_ptr<D> pd1 =
std::dynamic_pointer_cast<D>(pb);
if(pd1 ≠ nullptr) {...}
std::shared_ptr<D> pd2 =
std::static_pointer_cast<D>(pb);
std::shared_ptr<const D> c_pd =
std::const_pointer_cast<const D>(pb);
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p19_img01.jpg)


---

<!-- Pagina 20 -->

Wrong use of shared pointer

```c
struct Son{
    shared_ptr<Mum> mum
};
struct Mum{
    shared_ptr<Son> son
};
main() {
    shared_ptr<Son> son1 =
        make_shared <Son>();
    shared_ptr<Mum> mum1 =
        make_shared <Mum>();
    son1→mum = mum1; // obj2 use_count = 2
    mum1→son = son1; // obj1 use_count = 2
} CYCLIC REFERENCE → MEMORY LEAK!!
NONE OF THE SHARED PTR GOES OUT OF SCOPE
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p20_img01.jpg)


---

<!-- Pagina 21 -->

Wrong use of shared pointer

```c
struct Son{
    shared_ptr<Mum> mum
};
struct Mum{
    shared_ptr<Son> son
};
main() {
    shared_ptr<Son> son1 =
        make_shared <Son>();
    shared_ptr<Mum> mum1 =
        make_shared <Mum>();
    son1->mum = mum1; // obj2 use_count = 2
    mum1->son = son1; // obj1 use_count = 2
} CYCLIC REFERENCE → MEMORY LEAK!!
NONE OF THE SHARED PTR GOES OUT OF SCOPE
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p21_img01.jpg)


---

<!-- Pagina 22 -->

Solving circular reference: use weak pointers

```c
struct Son{
    weak_ptr<Mum> mum
};
struct Mum{
    weak_ptr<Son> son
};
main() {
    shared_ptr<Son> son1 =
        make_shared <Son>();
    shared_ptr<Mum> mum1 =
        make_shared <Mum>();
    son1->mum = mum1; // obj2 use_count = 1
    mum1->son = son1; // obj1 use_count = 1
} NOW THEY ARE CORRECTLY DESTROYED
```

---

**Immagini estratte:**

![Figura estratta 1](p22_img01.jpg)


---

<!-- Pagina 23 -->

Weak Pointer

• It refers to an object managed by a shared_ptr
  shared_ptr<T1> sp = make_shared<T1>();
  weak_ptr<T1> wp1 = sp1;

• It does not take the ownership of a pointer
• It does not perform any automatic delete to the pointer
• You cannot perform any delete to the pointer with a weak pointer: this is the main difference it has with a raw pointer
• You cannot use → operator directly, to do that you first need to call the function lock()

---

**Immagini estratte:**

![Figura estratta 1](p23_img01.jpg)


---

<!-- Pagina 24 -->

Weak Pointer

• `lock()` returns a shared pointer to the object pointed by the weak pointer, so that object can be accessed in safe way
• It returns an empty shared pointer if the weak pointer is expired

```javascript
if(auto tmp_sp = wp.lock()){ //it checks if tmp_sp is not empty
  tmp_sp → getParam();
} // the shared pointer tmp_sp goes out of scope

use_count() checks how many shared pointer points to that object

expired() checks if use_count() = 0
```

---

**Immagini estratte:**

![Figura estratta 1](images/p24_img01.jpg)


---

<!-- Pagina 25 -->

Wrong use of smart pointers

```cpp
string* p = new string("ciao");
std::shared_ptr<string> sp(p); // count = 1
std::shared_ptr<string> sp2(p); // count = 1

• Who is responsible of deleting the object?

To avoid this problem follow this rule:

• An object should be assigned to a smart pointer as soon as it is created

std::shared_ptr<string> sp1 =
    std::make_shared<string>("ciao");
```

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)


---

<!-- Pagina 26 -->

Lab 2 bis variant – smart pointer

• In the Packet class use a map of shared pointers to headers instead of raw pointers: how does the method `addHeader()` change? (work on your own lab2 branch)

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)
