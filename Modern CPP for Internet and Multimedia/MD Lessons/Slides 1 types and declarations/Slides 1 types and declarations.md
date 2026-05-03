<!-- Pagina 1 -->

C++ Types and Declarations

Modern C++ Programming for ICT
Filippo Campagnaro
filippo.campagnaro@unipd.it

---

<!-- Pagina 2 -->

Outline

1. C++ fundamental types
2. Sizes
3. Declarations
4. Scope
5. Initialization
6. Objects
7. Const


<!-- Pagina 3 -->

C++ types

Fundamental Types
Available without any additional declaration
Example: int, bool

User-Defined Types
Introduced by the user and/or by a library header
Example: std::vector

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

Fundamental Types

• **Boolean** (bool)
  • One value between true (1) or false (0)
  • Used to represent logical conditions or results of logical operations

  • `bool b1 {1 = 0}`;

---

<!-- Pagina 5 -->

Fundamental Types

• **Character** (e.g., char)
  • Different types are available (char, signed char, unsigned char, wchar_t)
  • **Almost** always char has 8 bit
  • 7 bit are enough to represent ASCII
  • signed vs unsigned char:
    • A char may be represented either as signed or unsigned
    • Implementation-defined behavior (Windows vs Linux, 32 vs 64 bit, arm vs x86)
  • Character literals
    • Single character in **single** quotes (e.g., ‘a’, ‘0’) of type char
    • Special characters represented with ‘\’ (the escape character) + letter (e.g., ‘\n’)
    • The ASCII number associated to a literal can also be represented on **hexadecimal** base – using the ‘\x’ + number
  • char c1 = ‘a’;
  • char c2 = ‘\x61’; char c3 = 97;
  • std::cout << c1 << std::endl; // print a
  • std::cout << c2 << std::endl; // print a
  • std::cout << c3 << std::endl; // print a

---

---

<!-- Pagina 6 -->

Fundamental Types

• **Integer** (e.g., int)
  • Different types are available:
    • int, signed int, unsigned int
    • short int, long int, long long int

• **Floating point** (e.g., double)
  • Different types are available, with different precisions (implementation-defined):
    • float (single-precision)
    • double (double-precision)
    • long double (extended-precision)

• **void**
  • Used to indicate that a function does not return values
  • Used as type of a pointer to unknown object (more on this later)

---



---

<!-- Pagina 7 -->

Sizes

• Implementation-defined
  • The standard leaves the size of the fundamental types to the implementation
  • Well-defined given a certain implementation, but don’t rely on it for portability

Language != what the compiler implements

• Multiple of char
• sizeof function returns the size in number of chars
• Some conditions are always valid, e.g.,
  • 1 ≡ sizeof(char) ≤ sizeof(short) ≤ sizeof(int) ≤ sizeof(long) ≤ sizeof(long long)
  • sizeof(float) ≤ sizeof(double) ≤ sizeof(long double)

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)


---

<!-- Pagina 8 -->

Sizes

• `<cstdint>` header has the definition of types with precise size (e.g., `int16_t`)
  • `int` and `uint32_t` are not portable, `uint_fast32_t` is

• `<cstddef>` header has `size_t` -> type that can hold the size in byte of any object

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)


---

<!-- Pagina 9 -->

Declarations

• A declaration introduces a name (with a type) in a program

• Set of characters starting with a letter that identifies an entity
• Please use naming conventions: camelCase, snake_case
• In the code for classes, we will use camelCase for classes and functions (with Capital letter for classes) and snake_case for variables
• See https://gist.github.com/lefticus/10191322#c-coding-standards-part-1-style

• A definition additionally provides all the information that the program needs to use the entity

• Memory
• If a function, what it does
• If a class, fields and methods
• …

• One and only one definition for each name in a C++ program

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Declarations

Optional prefix static virtual
Base type
Declarator name + optional operator
Optional suffix const noexcept
Optional initializer or function body

static const char* universities[] {"Padova", "Venezia"};
The type cannot be omitted
* and [] are declarator operators

int a_number {10};
const char* str_c {"example of declaration"};
std::vector<double> double_vec {0.1, 0.4, 0.5};

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Declarator operators

| Declarator Operators |
|-----------------------|
| prefix * pointer |
| prefix *const constant pointer |
| prefix *volatile volatile pointer |
| prefix & lvalue reference (§7.7.1) |
| prefix && rvalue reference (§7.7.2) |
| prefix auto function (using suffix return type) |
| postfix [] array |
| postfix () function |
| postfix -> returns from function |

Stroustrup, Bjarne. The C++ programming language. Pearson Education, 2013, page 154

• Prefix/postfix
  • Postfix operators bind tighter than prefix operators
    • char*universities[] //array of pointers to chars
    • char(*universities)[] //pointer to array of chars
  • In general, put a space where needed
    • char* universities[]

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

Scope

• A name can be used only in specific parts of a program
• Fundamental for C++ resource management
• Different scopes:

• Local
  Declared in a function, valid from declaration to the end of the block

```c
f()
{
    Block: from { to }
    int a {10};
    std::cout << a << std::endl;
}
// a does not exist here

• Class
  Member name if defined in class `but` outside functions
  The scope extends to the class block (from { after the declaration to the end })
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Scope

• Different scopes:
  • Namespace
    Namespace member name if defined in namespace `but` outside functions, enum, classes, etc
    The scope extends from the point of declaration to the end of the namespace
  • Global
    Name defined in outside functions, enum, classes, namespaces
    The scope extends from the point of declaration to the end of the file, and can be accessed from other files by using external linkage
  • Statement scope
    Name defined in () part of `for`, `while`, `if`, `switch`
    The scope extends from point of declaration to } of the statement

```cpp
for(int index = 0; index < 10; ++index)
{
    Scope of index
    std::cout << index << std::endl;
}
// index does not exist here
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Scope

```cpp
int global_var {10}; // global index

namespace Example {
int namespace_scope_var {5}; // namespace scope

class ExampleClass {
    int class_scope_var;
    void f() {
        int local_scope_var {2};
        for (int statement_scope_idx = 0;
             statement_scope_idx < local_scope;
             ++statement_scope_idx) {
            std::cout << statement_scope_idx;
        }
    }
} // end of class ExampleClass scope
} // end of namespace Example scope
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Hiding or shadowing

• Names can be redefined in nested blocks: minimize or avoid it!

```cpp
int index = 10; // global x

void f()
{
    char index = 'a'; // local index 1
    std::cout << index << std::endl;
    for(int index = 0; index < 10; ++index)
    {
        // statement index
        std::cout << index << std::endl;
    }

    {
        double index = 0.2; // local index 2 hides 1
        std::cout << index << std::endl;
    }
    index = 'b'; // assign to local index 1
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)


---

<!-- Pagina 16 -->

Initialization

```c
T a1 {v}; → Introduced in C++11
• Does not allow narrowing
  int a1 {0.2}; //compilation error
• Strongly recommended except with auto
• {} indicates initialization with default value
(if present)

T a2 = {v};

T a3 = v;

T a4(v);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)


---

<!-- Pagina 17 -->

auto Type Specifier

• automatically infer the type of the variable from the type of the initializer
• do not use the {} initializer with auto – otherwise the type becomes a std::initializer_list<T>
• int a1 = 2292;
  auto a2 = 2292; // a2 is int
• advantage if the type has a long name
• std::vector<T>::iterator a1 = vec.begin();
  auto a1 = vec.begin();

• Use it mainly in small scopes (hard to debug in large scopes)

---

**Immagini estratte:**

![Figura estratta 1](images/p17_img01.jpg)


---

<!-- Pagina 18 -->

Initialize consistently

• If a name is declared and not initialized, the behavior is complex and hard to debug

```cpp
int globalVariable; // means globalVariable{}; → 0
Valid for static, global, namespace names

void f()
{
    int localVariable; // no well-defined value!
}
```

This happens for all local variables and objects on the heap, unless they are user-defined types with a default constructor

---

**Immagini estratte:**

![Figura estratta 1](images/p18_img01.jpg)


---

<!-- Pagina 19 -->

What is a C++ object?

Contiguous region of storage in memory

An object

1. Has identity, i.e., the program has a name/pointer/reference to the object
2. Is not movable, i.e., the program cannot move its value to another location (e.g., another object) and leave the original object in an unspecified state (the only option is the copy)
3. Is referred to by an lvalue

---

**Immagini estratte:**

![Figura estratta 1](images/p19_img01.jpg)


---

<!-- Pagina 20 -->

lvalues and rvalues

| | Has identity | Is movable |
| :--- | :--- | :--- |
| lvalue | Yes | No |
| rvalue | X (it depends) | Yes |

• rvalues are **movable** and may or may not have identity
• For example: temporary values returned by functions

```cpp
std::vector<int> vec1 {1, 2, 3};
auto vec2 = someFunction(vec1);
lvalue rvalue
auto vec3 = vec1;
lvalue
```

---

**Immagini estratte:**

![Figura estratta 1](images/p20_img01.jpg)


---

<!-- Pagina 21 -->

Object lifetime

• The valid lifetime goes from the end of the constructor to the beginning of destructor
  • Automatic – from explicit initialization to out of scope
  • Static – until the program terminates
  • Free store – lifetime explicitly controlled with new and delete
  • thread_local objects – created within a thread and destroyed with it
  • Temporary objects – used in specific cases, generally automatic (destroyed at the end of the full expression using them)

```cpp
std::cout << std::string("tmp").size() << std::endl;
```

another example of rvalue

---

**Immagini estratte:**

![Figura estratta 1](images/p21_img01.jpg)


---

<!-- Pagina 22 -->

Type alias

• Synonym of a certain type
• Can be used alternatively
• Declared with

using viter = std::vector<int>::iterator;
typedef std::vector<int>::iterator viter;

std::vector<int> vec = {1,2,3};
std::vector<int>::iterator a = vec.begin();
viter b = a;

---

**Immagini estratte:**

![Figura estratta 1](images/p22_img01.jpg)


---

<!-- Pagina 23 -->

Const and constexpr

• const keyword declares that an object cannot be modified in the scope after initialization
  • A const object must be initialized when declaring it (unless it is a member variable of a class, more on this later)
  • For example: arguments of functions can be declared const so that the function cannot modify them (just read)

• const exp keyword declares that an expression can be evaluated at compile time
  • based on combination of known values (integers, floating-point values, enums), operators and other constant expression

---

**Immagini estratte:**

![Figura estratta 1](images/p23_img01.jpg)
