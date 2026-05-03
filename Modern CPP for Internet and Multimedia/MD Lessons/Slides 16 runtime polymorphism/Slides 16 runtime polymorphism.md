<!-- Pagina 1 -->

Class hierarchies and run-time polymorphism

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

1. Dynamic cast
2. Run-time type information (RTTI)
3. Misuses of RTTI
4. Class hierarchies
5. Other casts

[c++pl] Chapters 22

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Class hierarchies

It is possible to navigate complex class hierarchies (with multiple inheritance, inheritance from derived bases)

Recall: it is possible to use a pointer/reference to a base for a derived type

• in this example, a pointer A* could refer to an object D or E or F – which is the type of the actual object?

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

Class hierarchies

It is possible to navigate complex class hierarchies (with multiple inheritance, inheritance from derived bases)

• Cast C to E: `downcast` – the compiler may not know if it is correct
• Cast E to C: `upcast` – always ok for the compiler
• Cast from F to D: `crosscast` – the compiler may not know if it is correct

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img01.jpg)


---

<!-- Pagina 5 -->

Dynamic cast

C++ has a typed conversion operation that
• returns a valid pointer if the object is of the expected type
• nullptr otherwise

```cpp
void f(B* ptr)
{
    D* der_ptr {dynamic_cast<D*>(ptr)};
}

if ptr points to an object of type D, der_ptr is valid,
otherwise is a nullptr
```

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)


---

<!-- Pagina 6 -->

Run-time type information

dynamic_cast<T*>() is used when the compiler cannot check a priori if a conversion is correct

• it works from polymorphic types (base classes with virtual methods)
  • the target can be a concrete class with no virtual methods

• the compiler automatically associates information on the actual type of an object, which is then used at run-time (run-time type information or RTTI)

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)


---

<!-- Pagina 7 -->

Dynamic cast: pointer vs reference

dynamic_cast works with pointers and references

• the pointer that is returned can be a nullptr:
  • dynamic_cast<T*>(p) is a question – “is the object pointed to by p of type T?”
  • the programmer has to check if what is returned is a nullptr

```cpp
void f(Base* p)
{
    Der* p_dev {dynamic_cast<Der*>(p);
    if (p_dev ≠ nullptr)
    {
        // some code using p_dev
    }
    else { // cannot use p_dev! }
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)


---

<!-- Pagina 8 -->

Dynamic cast: pointer vs reference

dynamic_cast works with pointers and references

• the reference must always be associated to an object, and there is no nullptr equivalent for a reference

• dynamic_cast<T&>(r) is an assertion – “the object referred to by r is of type T”
• the dynamic_cast performs a check on whether the assertion is valid or not
• if not valid, a bad_cast exception is thrown
• in general, it is better to use pointers for polymorphism

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)


---

<!-- Pagina 9 -->

Capturing bad_cast exception

• Exceptions are raised when an error is met at runtime in a C++ program
• A bad_cast is raised when a dynamic_cast fails to cast to the reference specified as type
• It is possible to enclose these dynamic_casts in try/catch blocks

```cpp
void f(B& r) {
    try {
        D& der_ref {dynamic_cast<D&>(r)};
        // other operations
    } catch (bad_cast) {
        // handle the error
    }
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Multiple inheritance

dynamic_cast returns nullptr in case of multiple inheritance

- there is only one component class, but both rx and tx inherit from it
- both the tx and rx will have a base object of type component

- a conversion from radio to storable is ok
- a conversion from radio to component is not ok, as radio has two component subobjects

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Misuses of RTTI

• do not use dynamic_cast in a constructor
  • the information on the object you are constructing is not complete

• use RTTI only when necessary
  • compile-time type checking (i.e., no run-time polymorphism – directly use the exact type) is safer and has less run-time overhead

• prefer interfaces and virtual functions
  • when it is possible to design base classes

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

Misuses of RTTI

This is the wrong approach

```cpp
void rotate(Shape* r) {
    if (dynamic_cast<Circle*>(r)) {
        // do nothing
    }
    else if (dynamic_cast<Triangle*>(r)) {
        // ... rotate triangle ...
    }
    else if (dynamic_cast<Square*>(r)) {
        // ... rotate square ...
    }
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Correct approach

It is better to use a virtual method in the base and override it

```java
class Shape {
public:
    virtual void
rotate() = 0;
    // ...
}

class Circle : public
Shape{
public:
    void rotate();
    // ...
}

class Triangle : public
Shape{
public:
    void rotate();
    // ...
}

class Square : public
Shape{
public:
    void rotate();
    // ...
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Correct approach

Then, when you want to rotate any shape

```javascript
Shape* ptr_triangle {new Triangle{}};

// ...

ptr_triangle→rotate();
// the rotate() implementation of the class
// triangle will be used
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Other casts

```cpp
static_cast<T>()
```

• converts between related types
  • pointers in hierarchies
  • integral to enumerators
  • floating point types to integral (and vice versa)

• it does not examine the object it casts from
  • no run-time costs, no checks

• the compiler cannot assume anything on memory pointed by void*: dynamic_cast does not work with void*
```

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)


---

<!-- Pagina 16 -->

Other casts

reinterpret_cast<T>()

• conversion between unrelated types (e.g., integer and pointer)
• it changes how the bit pattern in memory is interpreted

const_cast<T>()

• it removes constness from pointers and references that point to something that is not const

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)


---

<!-- Pagina 17 -->

When to use casts - recap

static_cast
• try it first, for conversions between related types and from void*
• for downcasts with polymorphic types, it does not do run-time type checking: prefer dynamic_cast

dynamic_cast
• for downcasting/crosscasting polymorphic types with run-time type checking

const_cast
• for removing constness from pointers and references to non const objects

reinterpret_cast
• the most disruptive, it converts between unrelated types (e.g., int* to int)

---

**Immagini estratte:**

![Figura estratta 1](images/p17_img01.jpg)
