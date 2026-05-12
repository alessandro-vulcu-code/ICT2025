<!-- Pagina 1 -->

Pointers, Arrays and References

Modern C++ Programming for ICT
Filippo Campagnaro
filippo.campagnaro@unipd.it

---

**Immagini estratte:**

![Figura estratta 1](images/p01_img01.jpg)

![Figura estratta 2](images/p01_img04.jpg)

![Figura estratta 3](images/p01_img03.jpg)

![Figura estratta 4](images/p01_img02.jpg)


---

<!-- Pagina 2 -->

Outline

1. Pointers
2. Arrays
3. Pointers and arrays
4. References

[c++pl] Chapter 7

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Pointer

• Given type T, T* is the type “pointer to T”

It holds the address of an object of type T

```c
char c = 'a';
char* p = &c;

labels for memory addresses
p: &c
c: 'a'

char c2 = *p; // c2 is 'a'
dereferencing or indirection returns the value at the address in the pointer
```

3

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

```markdown

void* and nullptr

• Void* is the type “pointer to object of unknown type”
  • Limited set of operations are allowed:
    • Assign to other void*
    • Compare with other void*
    • Explicitly convert to another type using `static_cast<T>()` (unsafe)
  • Generally used to pass (or return) pointers to (from) functions without assumptions on the type
  • Very low-level

• nullptr is the value of a pointer that does not point to any object
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)


---

<!-- Pagina 5 -->

```cpp
void* and nullptr

void f(int* pi)
{
    void* pv {pi}; // allowed
    *pv; // compilation error, cannot dereference *void
    // because the type is not implicitly known
    ++pv; // compilation error, cannot increment *void
    // because it does not know the size of the type

    void* pv2 {pi};
    bool pointToSameAddress {pv == pv2};

    int* pi2 {static_cast<int*>(pv)};
    double* pi3 {static_cast<double*>(pv)};
    //allowed but leads to logical errors!

    pi3 = nullptr; // does not point to anything
}
```

---

**Immagini estratte:**

![Figura estratta 1](p05_img01.jpg)


---

<!-- Pagina 6 -->

Pointers and Ownership

• Resource: something that is acquired and then released
  • memory
  • file

• A pointer is often as a handle to a resource

• Confusing: it is not possible to distinguish a pointer that owns a resource from one that does not

```c
int i2 = 7;
int* i = &i2; // i does not own resources

int* i3 = new int{7}; // i3 owns object on the free storage
```

• Rule of thumb: place pointers that own resources in an handle class (class that manages resources with constructors and destructors)

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)


---

<!-- Pagina 7 -->

Pointers and const

```javascript
const char* p = “unipd”; → the object is const, not the pointer!

const char* const p2 = “unipd”; → both const

• An object which is const with a pointer may be accessed in other ways
  • Useful to have pointers to const objects as function arguments
  • The function cannot modify the object!
```

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)


---

<!-- Pagina 8 -->

Arrays

• Given type T, T[size] is an array of elements of type T

• Sequence of objects in memory – low-level facility

• Access with
  • Subscript operator [ ]
  • Index from 0 to size – 1
  • NO runtime range checks!
  • With a pointer

• Allocation options:
  • Static
  • Stack
  • Free storage (or heap)

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)


---

<!-- Pagina 9 -->

Array initialization

• List of values

```c
int v1[] = {1,2,3,4}; // the size is automatic
int v2[8] = {1,2,3,4}; // → 1,2,3,4,0,0,0,0
int v3[2] = {1,2,3,4}; // compilation error
```

• Arrays cannot be copied

```c
int v1[] = {1,2,3,4};
int v4[4] = v1; // error
```

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

String literals

• Character sequence in double quotes
• Represented by `array of chars` terminated by ‘\0’
• Statically allocated (i.e., safe to return from function)

The type is constant (cannot change the value)

```cpp
const char stringExample[] = "Unipd";
std::cout << sizeof(stringExample) << std::endl; // $\textcircled{6}$
```

return the size of an expression or a data type, measured in number of bytes

5 chars + the termination ‘\0’

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Pointers and arrays

• The name of an array can be used as a pointer to its first element
  ```c
  int v[] = {1,2,3,4};
  int* p1 = v;
  int* p2 = &v[0];
  bool pointToSameAddress {p1 == p2}; //this is true
  ```
  ```c
  int* pOneBeyondLast = v + 4;
  int* pOther = v + 7;
  ```

all the position outside the range [v + 0, v + size] are undefined: do not do that! Risk of overwriting other variables or segfault

• it is valid to have a pointer to the element beyond the last element of the array, but it cannot be read from or written to
• useful to implement low-level algorithms

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

Pointers and arrays

```c
const int size = 4;
int v[size] = {1,2,3,4};

for(int * p1 = v; p1 < v + size; ++p1)
{
    std::cout << *p1 << std::endl;
}

// equivalent to

for(int index = 0; index < size; ++index)
{
    std::cout << v[index] << std::endl;
}

const char* strLit = "unipd";

for(; (*strLit ≠ '\0'); ++strLit)
{
    std::cout << *strLit << std::endl;
}
```

• The arrays **do not** carry implicit information on their **size**!
• When passing a pointer to an array to a function (this is the only possible way), one needs to carry along the info on the size

With string literals, it is possible to use this condition without info on the size

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Operators on pointers

• It is possible to apply operators to pointers
• They operate on the address (i.e., the value of the operator), not on the values the address points to!
• The increment (decrement) depends on the type of the object pointed to by the pointer
  T arrayt[4];
  T* pt = arrayt;
  pt++; // the numeric value is pt + sizeof(T)
• Subtraction $q - p$ is valid only for elements in the range of the array -> returns the number of elements in the range [p, q)
• Addition of pointers is not allowed (just integer values)

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

References

• A pointer differs from a name:
  • Different syntax
  • Can point to different objects at different times
  • It may be a `nullptr`

• A reference is an alias for an object (same performance as pointers) but
  • Access to the reference with the same syntax as a name
  • Always refer to the object to which it was initialized
  • No null reference

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Lvalue References

• They refer to objects whose value can be changed

```c
int var {1};
int &ref {var};
int var2 = ref + 4;
int* pointer = &ref;
++ref;
++pointer;
```

• always need initialization
• cannot be changed after
• a reference can be used in the same way of a name
• points to var
• increase var
• increase the value of pointer

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p15_img01.jpg)


---

<!-- Pagina 16 -->

Rvalue References

• Refer to temporary objects, to be modified and not used again (destructive read)
• Enables optimizations (e.g., turns copy into move)

```c
int && ref {1};
```

lvalue with type rvalue reference

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p16_img01.jpg)


---

<!-- Pagina 17 -->

Optimizations with rvalue references

Classic swap function without rvalues and move semantic

```cpp
template<class T>
swap(T& a, T& b) // "old-style swap"
{
    T tmp {a}; // two copies of a
    a = b; // two copies of b
    b = tmp; // two copies of tmp (aka a)
}

3 copy operations + destructors + memory consumption
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)


---

<!-- Pagina 18 -->

Optimizations with rvalue references

Classic swap function with rvalues

```cpp
template<class T>
swap(T& a, T& b)
{
    T tmp {static_cast<T&&>(a)};
    a = static_cast<T&&>(b);
    b = static_cast<T&&>(tmp);
}
```

this is equivalent to `std::move(tmp)`

`std::move()` does not move, but casts to an rvalue reference so that types with move constructors or assignment can exploit it

```cpp
T tmp {std::move(a)};
a = std::move(b);
b = std::move(tmp);
```

this returns an rvalue reference of type T&& to a

if T has a move constructor (more later), there is a benefit to pass a with an rvalue reference, because it will exploit a move operation instead of a copy operation

no unneeded copies!

---

**Immagini estratte:**

![Figura estratta 1](p18_img01.jpg)
