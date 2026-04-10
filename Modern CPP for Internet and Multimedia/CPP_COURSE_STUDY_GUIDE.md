# Modern C++ Programming for ICT - Complete Study Guide

**Course:** Modern C++ Programming for ICT  
**Instructor:** Filippo Campagnaro (filippo.campagnaro@unipd.it)  
**Reference:** "The C++ Programming Language" by Bjarne Stroustrup (c++pl)

---

## Table of Contents

1. [Types and Declarations](#1-types-and-declarations)
2. [Pointers, Arrays and References](#2-pointers-arrays-and-references)
3. [Structures and Enumerators](#3-structures-and-enumerators)
4. [Statements](#4-statements)
5. [Namespaces](#5-namespaces)
6. [Functions](#6-functions)
7. [Classes](#7-classes)
8. [Construction, Cleanup, Copy and Move](#8-construction-cleanup-copy-and-move)
9. [How C++ Works - Compiler](#9-how-c-works---compiler)
10. [Autotools](#10-autotools)
11. [Memory Management](#11-memory-management)
12. [Derived Classes and Class Hierarchies](#12-derived-classes-and-class-hierarchies)
13. [Operator Overloading](#13-operator-overloading)
14. [Runtime Polymorphism](#14-runtime-polymorphism)
15. [Templates](#15-templates)
16. [Standard Library](#16-standard-library)
17. [Smart Pointers](#17-smart-pointers)
18. [Bitwise Operators, POD, I/O Streams](#18-bitwise-operators-pod-io-streams)
19. [Socket Programming](#19-socket-programming)
20. [Threads and Lambdas](#20-threads-and-lambdas)
21. [Inter-thread Communication](#21-inter-thread-communication)

---

## 1. Types and Declarations

### 1.1 C++ Types

C++ types are divided into two categories:

| Category | Description | Examples |
|----------|-------------|----------|
| **Fundamental Types** | Available without any additional declaration | `int`, `bool`, `char`, `double` |
| **User-Defined Types** | Introduced by the user and/or by a library header | `std::vector`, `std::string` |

### 1.2 Fundamental Types

#### Boolean Type (`bool`)
- One value between `true` (1) or `false` (0)
- Used to represent logical conditions or results of logical operations

```cpp
bool b1 {1 == 0};  // false
```

#### Character Types (`char`)
- Different types available: `char`, `signed char`, `unsigned char`, `wchar_t`
- Almost always `char` has 8 bits (7 bits enough for ASCII)
- **signed vs unsigned char**: Implementation-defined behavior (Windows vs Linux, 32 vs 64 bit, arm vs x86)

**Character Literals:**
- Single character in single quotes: `'a'`, `'0'`
- Special characters with escape character: `'\n'`, `'\t'`
- Hexadecimal representation: `'\x'` + number

```cpp
char c1 = 'a';
char c2 = '\x61';  // same as 'a'
char c3 = 97;      // same as 'a'
std::cout << c1 << std::endl;  // prints 'a'
```

#### Integer Types
- Different types: `int`, `signed int`, `unsigned int`
- Size variants: `short int`, `long int`, `long long int`

#### Floating Point Types
- Different precisions (implementation-defined):
  - `float` (single-precision)
  - `double` (double-precision)
  - `long double` (extended-precision)

#### Void Type
- Used to indicate that a function does not return values
- Used as type of a pointer to unknown object

### 1.3 Sizes

Sizes are implementation-defined — the standard leaves them to the implementation. They're well-defined for any given platform, but don't rely on specific values if you care about portability. `sizeof` returns the size in chars (bytes).

**Size Relationships (always valid):**
```
1 ≡ sizeof(char) ≤ sizeof(short) ≤ sizeof(int) ≤ sizeof(long) ≤ sizeof(long long)
sizeof(float) ≤ sizeof(double) ≤ sizeof(long double)
```

**Important Headers:**
- `<cstdint>`: Types with precise size (e.g., `int16_t`, `uint32_t`)
- `<cstddef>`: `size_t` - type that can hold size in bytes of any object

### 1.4 Declarations

A **declaration** introduces a name with a type. A **definition** goes further — it provides everything needed to actually use the entity: memory allocation, function implementation, or class fields and methods. Every name can have only one definition in a C++ program.

**Declaration Structure:**

| Optional Prefix | Base Type | Declarator | Optional Suffix | Optional Initializer |
|-----------------|-----------|------------|-----------------|----------------------|
| `static`, `virtual` | type | name + optional operator | `const`, `noexcept` | or function body |

```cpp
static const char* universities[] {"Padova", "Venezia"};
int a_number {10};
const char* str_c {"example of declaration"};
std::vector<double> double_vec {0.1, 0.4, 0.5};
```

**Declarator Operators:**
- `*` (pointer)
- `[]` (array)
- `&` (reference)

**Postfix operators bind tighter than prefix operators:**
```cpp
char* universities[]    // array of pointers to chars
char(*universities)[]    // pointer to array of chars
```

### 1.5 Scope

A name can be used only in specific parts of a program.

**Types of Scope:**

| Scope | Description | Valid From |
|-------|-------------|------------|
| **Local** | Declared in a function | Declaration to end of block `{}` |
| **Class** | Member name in class | Class block start to end |
| **Namespace** | Namespace member | Declaration to end of namespace |
| **Global** | Outside functions, classes, namespaces | Declaration to end of file |
| **Statement** | In `for`, `while`, `if`, `switch` | Declaration to `}` of statement |

```cpp
int global_var {10};  // global scope

namespace Example {
    int namespace_scope_var {5};  // namespace scope
    class ExampleClass {
        int class_scope_var;  // class scope
        void f() {
            int local_scope_var {2};  // local scope
            for (int statement_scope_idx = 0; statement_scope_idx < local_scope; ++statement_scope_idx) {
                std::cout << statement_scope_idx;  // statement scope
            }
        }
    };
}
```

### 1.6 Hiding/Shadowing

Names can be redefined in nested blocks - **minimize or avoid this!**

```cpp
int index = 10;  // global
void f() {
    char index = 'a';  // local index 1 - hides global
    for(int index = 0; index < 10; ++index) {  // statement index
        std::cout << index << std::endl;
    }
    double index = 0.2;  // local index 2 - hides local 1
}
```

### 1.7 Initialization

**C++11 Initialization Syntax:**

```cpp
T a1 {v};      // Recommended - does not allow narrowing
T a2 = {v};    // Copy-list initialization
T a3 = v;      // Copy initialization
T a4(v);       // Direct initialization
```

**Important:** `int a1 {0.2};` causes compilation error (narrowing not allowed)

**Default Initialization with `{}`:**
```cpp
int globalVariable;      // means globalVariable{} -> 0 (valid for static, global, namespace)
void f() {
    int localVariable;   // NO well-defined value! (undefined for local variables)
}
```

### 1.8 auto type specifier

`auto` infers the type from the initializer. Don't use `{}` with `auto` — the type becomes `std::initializer_list<T>`, which is rarely what you want.

```cpp
int a1 = 2292;
auto a2 = 2292;  // a2 is int

// Advantage for long types:
std::vector<T>::iterator a1 = vec.begin();
auto a2 = vec.begin();  // simpler
```

**Use mainly in small scopes** (hard to debug in large scopes)

### 1.9 Objects

An object is a contiguous region of storage in memory. It has identity (the program can name it via a pointer or reference), it is not movable (you can copy the value but not relocate it), and it is referred to by an lvalue.

### 1.10 lvalues and rvalues

| | Has Identity | Is Movable |
|---|-------------|------------|
| **lvalue** | Yes | No |
| **rvalue** | X (depends) | Yes |

- **rvalues** are movable and may or may not have identity
- Example: temporary values returned by functions

```cpp
std::vector<int> vec1 {1, 2, 3};
auto vec2 = someFunction(vec1);  // vec1 is lvalue, return is rvalue
auto vec3 = vec1;  // vec1 is lvalue
```

### 1.11 Object Lifetime

Valid lifetime goes from end of constructor to beginning of destructor.

| Type | Lifetime |
|------|----------|
| **Automatic** | From explicit initialization to out of scope |
| **Static** | Until program terminates |
| **Free store** | Explicitly controlled with `new` and `delete` |
| **thread_local** | Created within thread, destroyed with it |
| **Temporary** | Destroyed at end of full expression |

```cpp
std::cout << std::string("tmp").size() << std::endl;  // temporary rvalue
```

### 1.12 Type Alias

Synonym for a certain type:

```cpp
using viter = std::vector<int>::iterator;
typedef std::vector<int>::iterator viter;  // older syntax

std::vector<int> vec = {1,2,3};
viter b = vec.begin();
```

### 1.13 const and constexpr

**const:** Declares that an object cannot be modified after initialization
- Must be initialized when declaring (unless member variable of a class)

```cpp
const int max_size {100};
```

**constexpr:** Declares that expression can be evaluated at compile time
- Based on combination of known values, operators, and other constant expressions

```cpp
constexpr int max_items {32 * 5};
constexpr double pi {3.14159};
```

---

## 2. Pointers, Arrays and References

### 2.0 5-Minutes Questions

> Typical oral exam questions from this module:
- What is the difference between a **pointer** and a **reference**?
- What is `nullptr`? When do you use it?
- What does `const char* p` mean vs `char* const p`?
- Can a reference be `nullptr`?
- What is an **lvalue reference** vs an **rvalue reference**?
- What does `std::move()` do?
- Why is pointer arithmetic scaled by `sizeof(T)`?

### 2.1 Pointers

**Definition:** Given type `T`, `T*` is the type "pointer to T" - it holds the address of an object of type T

```cpp
char c = 'a';
char* p = &c;  // p holds address of c
char c2 = *p;  // c2 is 'a' (dereferencing/indirection)
```

### 2.2 void* and nullptr

**void*:** Pointer to object of unknown type

**Limited operations allowed:**
- Assign to other `void*`
- Compare with other `void*`
- Explicitly convert using `static_cast<T>()` (unsafe)

```cpp
void f(int* pi) {
    void* pv {pi};     // allowed
    *pv;               // ERROR: cannot dereference void*
    ++pv;              // ERROR: cannot increment void*
    
    int* pi2 {static_cast<int*>(pv)};  // allowed but potentially dangerous
}
```

**nullptr:** Value of pointer that does not point to any object

```cpp
int* p = nullptr;  // does not point to anything
```

### 2.3 Pointers and Ownership

**Resource:** Something acquired and then released (memory, file, etc.)

With raw pointers it is **impossible to tell** from the type alone whether a pointer owns its resource or not:

```cpp
int i2 = 7;
int* i = &i2;           // i does NOT own resources (stack variable)
int* i3 = new int{7};   // i3 OWNS object on free storage — must delete!
```

> **Rule of thumb:** place pointers that own resources inside a **handle class** (RAII), so the destructor handles cleanup. Never leave ownership implicit in a raw pointer.

**Ownership transfer with `std::move`:**
```cpp
// Move makes it explicit that ownership is transferred
std::unique_ptr<int> p1 = std::make_unique<int>(7);
std::unique_ptr<int> p2 = std::move(p1); // p1 is now nullptr
```

### 2.4 Pointers and `const`

Read declarations **right-to-left** to decode them:

```cpp
const char* p  = "unipd";        // pointer to const char  → cannot change *p, can change p
char* const p2 = "unipd";        // const pointer to char  → can change *p2, cannot change p2
const char* const p3 = "unipd";  // const pointer to const char → neither can change
```

**Memory aid:** `const` applies to whatever is immediately to its *left* (or right if nothing is on the left).

**Use case:** Pass pointers to `const` objects as function arguments to prevent the callee from modifying data:
```cpp
void print(const char* s) {  // cannot modify *s inside print
    std::cout << s;
}
```

### 2.5 Arrays

**Definition:** Given type `T`, `T[size]` is an array of elements of type T

- Sequence of objects in memory (low-level facility)
- Access with subscript operator `[]` (index from 0 to size-1)
- **NO runtime range checks!**

**Allocation options:**
- Static
- Stack
- Free storage (heap)

### 2.6 Array Initialization

```cpp
int v1[] = {1,2,3,4};      // size is automatic (4)
int v2[8] = {1,2,3,4};     // -> 1,2,3,4,0,0,0,0
int v3[2] = {1,2,3,4};     // ERROR: too many initializers
```

**Arrays cannot be copied:**
```cpp
int v1[] = {1,2,3,4};
int v4[4] = v1;  // ERROR
```

### 2.7 String Literals

- Character sequence in double quotes
- Represented by array of chars terminated by `'\0'`
- Statically allocated (safe to return from function)

```cpp
const char stringExample[] = "Unipd";
std::cout << sizeof(stringExample) << std::endl;  // 6 (5 chars + '\0')
```

### 2.8 Pointers and Arrays

The name of an array can be used as a pointer to its first element:

```cpp
int v[] = {1,2,3,4};
int* p1 = v;        // pointer to first element
int* p2 = &v[0];    // same as above
bool same {p1 == p2};  // true

int* pOneBeyondLast = v + 4;  // valid pointer (cannot be read/written)
```

**Important:** Arrays do not carry implicit information on their size!

```cpp
const int size = 4;
int v[size] = {1,2,3,4};
for(int* p1 = v; p1 < v + size; ++p1) {
    std::cout << *p1 << std::endl;
}
```

### 2.9 Operators on Pointers

Pointer arithmetic operates on **addresses**, not on the values pointed to. Increments are scaled by `sizeof(T)`:

```cpp
T arrayt[4];
T* pt = arrayt;
pt++;   // numeric address increases by sizeof(T), not by 1
```

**Valid operations:**
| Operation | Result |
|---|---|
| `p + n` | pointer to n-th element after p |
| `p - n` | pointer to n-th element before p |
| `p - q` | number of elements in `[q, p)` (only valid within same array) |
| `p++` / `p--` | advance / retreat by one element |
| `p == q` / `p != q` | compare addresses |

**NOT allowed:** `p + q` (adding two pointers makes no sense)

> Accessing outside the range `[array, array + size]` is **undefined behavior** — risk of overwriting other variables or segfault.

### 2.10 References

**Pointer vs Reference — comparison:**

| Feature | Pointer (`T*`) | Reference (`T&`) |
|---|---|---|
| Syntax | Needs `*` to dereference | Same as name |
| Can be `nullptr` | Yes | **No null reference** |
| Can be reassigned | Yes (can point to different objects) | **No — always bound to initial object** |
| Must be initialized | No | **Yes — always** |
| Performance | Same | Same |

**Reference:** an *alias* for an object — same performance, safer than a pointer.

### 2.11 Lvalue References

Refer to objects whose value can be changed:

```cpp
int var {1};
int& ref {var};  // always needs initialization, cannot be changed after

int var2 = ref + 4;  // var2 = 5
int* pointer = &ref; // points to var
++ref;               // increases var
```

### 2.12 Rvalue References

Refer to temporary objects, to be modified and not used again (destructive read):

```cpp
int&& ref {1};  // lvalue with type rvalue reference
```

**Enables optimizations** (e.g., turns copy into move)

### 2.13 Optimizations with rvalue references

Without rvalues, swap does three copies:

```cpp
template<class T>
void swap(T& a, T& b) {  // "old-style swap"
    T tmp {a};   // copy of a
    a = b;       // copy of b
    b = tmp;     // copy of tmp
}
```

With rvalues, it moves instead — no unnecessary copies:

```cpp
template<class T>
void swap(T& a, T& b) {
    T tmp {std::move(a)};
    a = std::move(b);
    b = std::move(tmp);
}
```

`std::move()` doesn't actually move anything — it casts to an rvalue reference so types with move constructors can take advantage of it.

---

## 3. Structures and Enumerators

### 3.1 Primitive User-Defined Data Types

| Type | Description |
|------|-------------|
| **struct** | Sequence of elements of arbitrary types (from C) |
| **enum** | Type with set of named constants, implicitly cast to integer |
| **enum class** | Scoped enum without implicit conversion to integer |

### 3.2 struct

**Definition:** Aggregate of elements with different types

```cpp
struct Address {
    const char* name;
    int number;
    const char* street;
    const char* town;
    char state[2];
    const char* zip;
};

Address jd = {
    "Jim Dandy",
    61,
    "South St",
    "New Providence",
    {'N','J'},
    "07974"
};
```

**Important:** Two structs are different types even when they have the same members

### 3.3 struct Member Access

```cpp
Address jd;
jd.name = "Jim Dandy";  // direct access

void f(Address& addr) {
    addr.name = "Jim Dandy";
}

void f(Address* addr) {
    addr->name = "Jim Dandy";
    // or
    (*addr).name = "Jim Dandy";
}
```

**By default, members are public**

### 3.4 struct Layout

Members are saved in memory in order declared. Some architectures require alignment:

```cpp
struct Example {
    char first_member;    // 1 byte
    int second_member;    // 4 bytes
    char third_member;    // 1 byte
};
// Size is at least 6, but may be 12 due to alignment
```

### 3.5 struct Declarations

```cpp
struct Example {
    Example* pointer_to_other;  // OK: pointer size is fixed
};

struct Example {
    Example other;  // ERROR: size unknown
};
```

**Forward declaration** is possible

### 3.6 struct Constructors

A struct can have constructors:

```cpp
struct Points {
    std::vector<int> elem;
    Points(int n1, int n2) {
        elem.push_back(n1);
        elem.push_back(n2);
    }
};
```

**If constructor explicitly declared, no default constructor**

### 3.7 Plain Old Data (POD)

Simple types that can be copied/moved without risks (e.g., with `std::memcpy()`)

**A POD must have:**
- No complex layout
- No user-defined copy
- Trivial default constructor (non user-provided)

```cpp
struct Trivial {
    int a;
    Trivial(int aa) : a(aa) { }
    Trivial() = default;  // compiler-generated constructor
};
```

### 3.8 Fields in Structures (Bitfields)

Pack multiple flags together:

```cpp
struct SimpleTcpHeader {
    int source_port : 16;
    int destination_port : 16;
    int sequence_number : 32;
    int ack_number : 32;
    char data_offset : 4;
    char : 3;  // unused
    bool ns : 1;
    bool crw : 1;
    bool ece : 1;
    bool urg : 1;
    bool ack : 1;
    bool psh : 1;
    bool rst : 1;
    bool syn : 1;
    bool fin : 1;
    int window_size : 16;
    int checksum : 16;
    int urgent_pointer : 16;
};
```

**Note:** Address of a bitfield cannot be taken

### 3.9 enum class

Enumerators hold a set of integers named by the user.

**In enum class:**
- **Scoped** - do not exist outside enum class
- **Strongly typed** - do not convert implicitly to int

```cpp
enum class TrafficLight {green, yellow, red};
TrafficLight a = TrafficLight::red;
int a2 = a;              // ERROR: no implicit conversion
bool a3 {a == 2};        // ERROR: no implicit conversion

enum class Other : char {green, blue};  // specify underlying type
```

### 3.10 Operators on enum class

Can specify values for bitfield operations:

```cpp
enum class Printer_flags { 
    acknowledge=1, paper_empty=2,
    busy=4, out_of_black=8, out_of_color=16
};

constexpr Printer_flags operator|(Printer_flags a, Printer_flags b) {
    return static_cast<Printer_flags>(
        static_cast<int>(a)|static_cast<int>(b));
}
```

### 3.11 Plain enum

Enumerators are not scoped and can be converted to int:

```cpp
enum TrafficLight {green, yellow, red};
TrafficLight a = TrafficLight::red;
int a2 = a;       // OK!
bool a3 {a == 2}; // OK!
```

**In general, prefer enum classes** for better defined behavior

---

## 4. Statements

### 4.1 Statement Categories

1. Expression statements
2. Compound statements (sequence between `{}`)
3. Selection statements (`if`, `if else`, `switch`)
4. Iteration statements (`while`, `do`, `for`)
5. Jump statements (`break`, `continue`, `return`)
6. Declaration statements
7. Try blocks (for exception handling)
8. Empty statement (`;`)

### 4.2 Declarations as statements

Declaring variables close to where they're used keeps code local and avoids uninitialized variables:

```cpp
// Good: declare when needed
if (condition) {
    int x = computeValue();  // declared when needed
}
```

### 4.3 Selection Statements - if

```cpp
if (condition) statement
```

**Good practice:** Use compound statement (enclose in block)

**Variable declaration in condition:**
```cpp
if (int x = computeValue(); x > 0) {  // C++17
    // x is in scope here
}
```

### 4.4 if Conditions

Implicit conversion to boolean:

```cpp
int x = 1;
if (x) { }  // equivalent to if(x != 0)

int* p = &x;
if (p) { }  // equivalent to if(p != nullptr)
```

### 4.5 Logical Operators

| Operator | Meaning |
|----------|---------|
| `a && b` | AND - true if both true |
| `a || b` | OR - true if at least one true |
| `!a` | NOT - true if a is false |

### 4.6 Lazy Evaluation

Always check first condition, evaluate second only if needed:

```cpp
bool c1 = false;
bool c2 = true;
if (c1 && c2) { }  // c2 is NOT evaluated

if (c1 && someFunction(c2)) {
    // someFunction is NOT called
}
```

### 4.7 Conditional Expression (Ternary Operator)

```cpp
val = expression1 ? expression2 : expression3;
// if expression1 is true, evaluate expression2, else expression3

int x = 1;
int x2 = (x==1) ? 2 : 3;  // x2 = 2
```

**Use only for simple statements!**

### 4.8 switch Statement

Select among alternatives (case labels):

```cpp
switch (variable) {  // integer or enum type
    case val1:
        // code
        break;
    case val2:
        // code
        break;
    default:
        // code
}
```

**Generates more efficient compiled code than if**

### 4.9 switch Termination

Use `break` or `return` to terminate case. Otherwise, "fall through" to next case:

```cpp
switch (action) {
    case do_and_print:
        act(value);
        // fall through - intentional!
    case print:
        print(value);
        break;
}
```

**Always comment intentional fall-through!**

### 4.10 Range-for Statements

Loop over each element of a range:

```cpp
std::vector<int> v {1,2,3,4};
for (int value : v) {
    std::cout << value << std::endl;
}

// To modify values, use reference:
for (int& value : v) {
    value *= 2;
}
```

Works with sequences that:
- Yield iterator for beginning and end
- Have `begin()`/`end()` member pair

### 4.11 for Statements

```cpp
for (init-statement; condition; expression) statement

for (int i = 0; i < 10; i++) {
    std::cout << i << std::endl;
}
```

**auto may be handy:**
```cpp
std::vector<T> c;
for (auto p = c.begin(); p != c.end(); ++p) {
    // do something
}
```

**Flexibility:**
```cpp
int i = 0;
for (; i < 10;) {
    i++;
}

for (;;) {
    // endless loop
}
```

### 4.12 Pre-increment vs post-increment

Pre-increment (`++i`) increments and then evaluates the new value. Post-increment (`i++`) evaluates the old value, then increments. Prefer pre-increment in C++ when the result doesn't matter — post-increment silently creates a temporary, and for user-defined types like iterators that difference is real.

### 4.13 while Statements

```cpp
int i = 0;
while (i < 10) {
    // do something
    ++i;
}
```

More natural for complex conditions depending on multiple variables

### 4.14 do Statements

Execute body at least once:

```cpp
int i = 0;
do {
    ++i;
} while (i < 10);
```

### 4.15 Loop Exit

**break:** Exit nearest-enclosing switch or iteration statement

**continue:** Skip to next iteration

**return:** Terminate loop and function

---

## 5. Namespaces

### 5.1 Modularity

Modularity means keeping separate concerns separate and exposing functionality only through well-defined interfaces. In C++ you get this from namespaces, classes, and functions.

### 5.2 Namespace Problem

Without namespaces, name clashes occur:

```cpp
// Library for shapes
class Line { /* ... */ };
class Text { /* ... */ };

// Library for text
class Line { /* ... */ };  // CLASH!
class Text { /* ... */ };  // CLASH!
```

### 5.3 Namespace

Represents a set of facilities that belong together. Members are all in scope.

**Namespaces are open** - can add members from multiple locations:

```cpp
namespace TextLibrary {
    class Line { /* ... */ };
    class Text { /* ... */ };
};
```

### 5.4 Access to Namespace Members

**Explicit qualification:**
```cpp
TextLibrary::Line line_object {};

::GlobalMemberName  // access global namespace
```

**using declarations:**
```cpp
using std::string;
string a_string {"hello"};
```

**using directives:**
```cpp
using namespace std;
string a_string {"hello"};
vector<string> vec {a_string};
```

**Warning:** Use with care - may lead to same name clashes namespaces were introduced to avoid. Don't place in global scope of header file!

### 5.5 Argument-Dependent Lookup

Search for function in namespace of its arguments:

```cpp
namespace TextLib {
    class Text { /* ... */ };
    void print(const Text&);  // found by argument-dependent lookup
}

TextLib::Text t;
print(t);  // finds TextLib::print
```

### 5.6 Interfaces

Interfaces should be the only way to access a module's functionality — implementation details stay hidden (data-hiding principle). You define interfaces through namespaces (for libraries and modules) or through classes and OOP.

---

## 6. Functions

### 6.1 Why use functions

Functions make code easier to read and maintain, allow reuse, enable composition, document dependencies, and reduce error-prone control flow. The performance cost is negligible with a few precautions.

### 6.2 Function Declaration

```cpp
// Prefix return type
int sqrt(int number);

// Postfix return type (useful for templates)
auto sqrt(int number) -> int;
```

**Parts:**
- **name** (required)
- **argument list** (required) - names optional for declaration
- **return type** (required) - can be `void`

### 6.3 Optional keywords

| Keyword | Purpose |
|---------|---------|
| `inline` | Hint to generate code inline at each call site (optimization) |
| `constexpr` | Evaluated at compile time (must be simple: no loops, no side effects) |
| `noexcept` | Cannot throw an exception |
| `static` | Controls linkage |

### 6.4 Returning values

A function exits via: a `return` statement; falling off the end (only valid for `void`); an uncaught local exception; `terminate` (when an exception fires inside a `noexcept` function); or a non-returning system call like `exit()`.

Never return a pointer or reference to a local non-static variable.

### 6.5 Local and static variables

Local variables are re-initialized on every call. Static variables are created once on the first call and persist across all subsequent calls.

```cpp
void f() {
    int local = 0;        // new each call
    static int stat = 0;  // created once, persists
}
```

### 6.6 Argument passing

When a function is called, storage is set aside for the formal parameters, each is initialized from the actual arguments, and the compiler checks types and performs any necessary conversions.

### 6.7 Pass by Value

Value is copied into new independent variable:

```cpp
void increment(int a) {
    ++a;  // modifies local copy
}
int a = 2;
increment(a);
std::cout << a << std::endl;  // prints 2 (unchanged)
```

### 6.8 Pass by Reference

No copy, function directly modifies variable:

```cpp
void increment(int& a) {
    ++a;
}
int a = 2;
increment(a);
std::cout << a << std::endl;  // prints 3 (modified)
```

**Better practice:** Explicitly return modified value for clarity

**Use const references** for large objects:

```cpp
void f(const LargeType& a);  // efficient, no copy
```

### 6.9 Pass by Reference Types

```cpp
void f(vector<int>&);              // non-const lvalue ref
void f(const vector<int>&);        // const lvalue ref
void f(vector<int>&&);             // rvalue ref

void g(vector<int>& vi, const vector<int>& vci) {
    f(vi);                          // calls f(vector<int>&)
    f(vci);                         // calls f(const vector<int>&)
    f(vector<int>{1,2,3,4});        // calls f(vector<int>&&)
}
```

### 6.10 Argument Passing Guidelines

1. Pass-by-value for small objects
2. Pass-by-const-lvalue-reference for large objects not to be modified
3. Return result instead of modifying argument
4. Pass-by-rvalue-reference for move and forward
5. Pass pointer if "no object" case needs handling (`nullptr`)
6. Pass-by-lvalue-reference only as last option

### 6.11 Array Arguments

Arrays are passed by pointer, not by value:

```cpp
// These are equivalent:
void f(int* p);
void f(int a[]);
void f(int b[1000]);
```

**Size information is lost!**

**Workarounds:**
```cpp
void f(int* p, size_t size);      // pass size explicitly
void f(int (&r)[1000]);           // pass reference to array
```

**Better:** Use `std::vector` or standard library containers

### 6.12 List Arguments

`{}`-delimited list can be argument to:
1. `std::initializer_list<T>`
2. Reference to array of type T
3. Type that can be initialized with the values

```cpp
template<class T>
void f(initializer_list<T>);

f({1,2,3,4});  // T is int, size 4
```

### 6.13 Unspecified number of arguments

Three options: variadic templates (arbitrary number, arbitrary types, type-safe); `std::initializer_list<T>` (arbitrary number, same type, type-safe); or the C-style ellipsis `...` (arbitrary number, arbitrary types, not type-safe).

### 6.14 Default Arguments

Can be provided for trailing arguments only:

```cpp
int f(int a, int b=0, char* c=nullptr);  // OK
int g(int =0, int =0, char*);             // ERROR
int h(int =0, int, char* =nullptr);       // ERROR
```

### 6.15 Overloaded Functions

Different functions with same name for same task on different types:

```cpp
void print(int);           // print an int
void print(const char*);  // print a C-style string
```

### 6.16 Automatic Overload Resolution

Rules in order:
1. Exact match (no or trivial conversions)
2. Match using promotions
3. Match using standard conversions
4. Match using user-defined conversions
5. Match using ellipsis

**If two matches at highest level, compiler error**

**Return type is NOT considered for resolution**

### 6.17 Pre- and post-conditions

Pre-conditions are what you expect of the arguments; post-conditions are what you guarantee about the return value. Your options: document the conditions and assume they hold (trading safety for performance); check and throw if violated; or check and terminate. At minimum, document them.

### 6.18 Pointer to Function

Code for function stored in memory, can get its address:

```cpp
void error(int s) { /* implementation */ }
void (*efct)(int);  // pointer to function taking int, returning void

void f() {
    efct = error;    // same as efct = &error
    efct(10);       // same as (*efct)(10)
}
```

**Used to parametrize C-style code:**

```cpp
using CFT = int(*)(const void*, const void*);
void ssort(void* base, int size, CFT cmp);
```

**Modern C++ alternative:**
```cpp
std::vector<int> v {1,3,2,4};
std::sort(v.begin(), v.end(), 
    [](const int n1, const int n2) { return n1 < n2; });
```

### 6.19 Macros

Inherited from C, and mostly a bad idea in C++. The preprocessor does dumb text substitution with no type information:

```cpp
#define MAX_HEIGHT 720  // dumb preprocessor replacement
```

Use `constexpr` or `const` instead.

### 6.20 Conditional Compilation

```cpp
#ifdef IDENTIFIER
    // some code
#endif
```

### 6.21 Include Guards

Prevent multiple compilation of headers:

```cpp
#ifndef STRUCTS_ENUM_TEST
#define STRUCTS_ENUM_TEST

// code of the header

#endif /* STRUCTS_ENUM_TEST */
```

---

## 7. Classes

### 7.1 Classes

A class is a user-defined type. It separates implementation details (member variables, internal interactions) from the interface (public methods that operate on objects).

### 7.2 Class members

Members are either data (variables representing state) or functions (methods for initialization, copy, move, cleanup, and operations on the object). Access is either `public` (the interface) or `private` (the implementation).

### 7.3 Class Example

```cpp
class X {
private:
    int m;
public:
    X(int i = 0) : m{i} { }  // constructor
    int mf(int i) {          // member function
        int old = m;
        m = i;
        return old;
    }
};
```

### 7.4 Class Usage

```cpp
X var {7};  // variable of type X, initialized to 7

int f(X var, X* ptr) {
    int x = var.mf(7);    // access using .
    int y = ptr->mf(9);   // access using ->
    int z = var.m;        // ERROR: cannot access private member
}
```

### 7.5 Member functions

Declared inside the class, invoked only on objects of that type. The definition can live in the class itself or in a separate `.cpp` file. In-class definitions are implicitly inlined — use them for small, rarely changing functions.

```cpp
class X {
    int mf(int i) {  // inlined definition
        int old = m;
        m = i;
        return old;
    }
    int amf(int j);  // declaration only
};

int X::amf(int j) {  // definition outside class
    return j + 2;
}
```

### 7.6 Access Control

**public/private:** Control access to members

**friend:** Grant access to specific classes/functions

```cpp
class Y {
    friend X;  // class X can access private members of Y
private:
    int v;
public:
    Y(int i = 0) : v{i} { }
};
```

### 7.7 Structs vs Classes

A `struct` is a class with all members public by default.

**Use:**
- `struct` for simple data structures
- `class` to enforce invariants

### 7.8 Constructors

Member functions for initializing objects:
- Same name as class
- No return type
- Can use `()` or `{}` notation

```cpp
Date today = Date(22,2,1992);
Date tmrw = Date{22,2,1992};
```

**Multiple constructors allowed** (overloading rules apply)

### 7.9 Explicit Constructors

Prevent implicit conversion from single argument:

```cpp
class Date {
public:
    explicit Date(int d);
};

Date d = 15;   // ERROR with explicit
Date d {15};   // OK
```

**Good practice:** Keep single-argument constructors explicit (unless exceptions like `std::complex`)

### 7.10 In-class Initializers

Default values for data members:

```cpp
class Date {
    int d {22};
    int m {02};
    int y {1992};
public:
    Date(int, int, int);  // day, month, year
    Date(int, int);       // day, month, year default
    Date(int);            // day, month and year default
    Date();               // default date
};
```

### 7.11 Mutability

`const` member functions don't modify the object and can be called on both `const` and non-`const` objects. Non-`const` member functions can only be called on non-`const` objects.

```cpp
int getDay() const;  // does not modify object
```

### 7.12 Logical Constness

A const member function may need to change a member without affecting logical representation:

```cpp
class Date {
    mutable std::string string_cache;
    mutable bool valid_cache;
public:
    std::string string_rep() const;
};
```

**Alternative:** Mutability through indirection (pointer to cache object)

### 7.13 Self-reference

`this` is a pointer to the object on which function was called:

```cpp
Date& add_year(int year) { 
    y += year; 
    return *this; 
}

Date d {10, 05, 2003};
d.add_year(3).add_month(3);  // chaining
```

### 7.14 Static members

Belong to the class, not to any specific object — one copy per program. Static member functions can be called without an object instance.

```cpp
class Date {
    static Date default_date;
public:
    static void set_default(int dd, int mm, int yy);
};

// Definition (must be before first use)
Date Date::default_date {16,12,1770};
```

### 7.15 Concrete classes

A small, concrete type where the representation is part of the definition. You can put objects on the stack, allocate them statically, copy and move them, and use them as named variables. Typically includes a constructor, const inspection methods, mutation methods, copy/move functions, and helper functions.

---

## 8. Construction, Cleanup, Copy and Move

### 8.0 5-Minutes Questions

> Typical oral exam questions from this module:
- What is the **order** of constructor/destructor calls in derived classes?
- What is the difference between **copy constructor** and **copy assignment**?
- What is a **shallow copy**? Why is it dangerous?
- What does `std::move()` do? Does it actually move anything?
- What is **RAII** and why is the destructor essential for it?
- When is the **default constructor** not generated automatically?
- What is a **delegating constructor**?
- When would you use `=delete` on a constructor?
- What is a **member initializer list** and why is it more efficient than assignment in the body?

### 8.1 Object Life Cycle

An object is first constructed, then goes through operations until destroyed.

### 8.2 Life-cycle Operations

```cpp
class X {
    X(someargs);      // Ordinary constructor
    X();              // Default constructor
    X(const X&);      // Copy constructor
    X(X&&);           // Move constructor
    X& operator=(const X&);  // Copy assignment
    X& operator=(X&&);       // Move assignment
    ~X();             // Destructor
};
```

**These can be automatically generated by compiler**

### 8.3 Constructors and Destructors

```cpp
struct Tracer {
    std::string mess;
    Tracer(const string& s) : mess{s} {
        std::cout << mess;
    }
    ~Tracer() {
        std::cout << "~ " << mess;
    }
};

int main() {
    Tracer tr{"a string"};
}
// Output: a string
//         ~ a string
```

### 8.4 Constructor

Same name as the class, no return type, establishes invariants. Those invariants must hold through copying and moving too.

### 8.5 Destructor

`~ClassName()` — no arguments, only one per class. Guaranteed to run when the object is destroyed, which is what makes resource cleanup reliable.

---

### 8.5.1 RAII — Resource Acquisition Is Initialization

**RAII** is the central C++ paradigm for safe resource management. The idea is simple:

> *Tie the lifetime of a resource to the lifetime of an object.*

**The two rules:**
1. **Constructor acquires** the resource (e.g. allocates memory with `new`, opens a file, locks a mutex)
2. **Destructor releases** the resource (e.g. calls `delete`, closes the file, unlocks the mutex)

**Resources covered by RAII:**
- Heap memory
- Files (file descriptors)
- Locks for concurrency (mutexes)
- Sockets

**Why RAII is safe:** the destructor is *automatically* called when the object goes out of scope — even if an exception is thrown or a `return` is hit early. You never forget to release.

```cpp
// Minimal RAII handle for an int*
class Handle {
    int* p;
public:
    Handle(int* pp) : p{pp} { }       // acquire
    int& operator*() { return *p; }   // dereference
    ~Handle() { delete p; }           // release — called automatically
};

void f() {
    Handle h {new int{10}};   // resource acquired
    std::cout << *h;
}   // h goes out of scope → ~Handle() calls delete → no leak
```

**RAII with threads** (avoid crashes when function exits before join):

```cpp
class ThreadGuard {
    std::thread thr;
    void task() { /* ... */ }
public:
    ThreadGuard() : thr(&ThreadGuard::task, this, 200) {}
    ~ThreadGuard() { if (thr.joinable()) thr.join(); } // RAII: always joins
};
```

**Copy semantics with RAII handles** — when copying a handle, you must decide what happens to the resource:

| Strategy | How |
|---|---|
| Prohibit copying | `=delete` the copy constructor |
| Reference-count | Increment counter on copy (→ `shared_ptr`) |
| Transfer ownership | Move semantic (→ `unique_ptr`) |
| Deep copy | Allocate new resource and copy values |

---

### 8.6 Destructor Invocation

```cpp
void f() {
    Tracer tr{"a string"};
}  // tr goes out of scope: ~Tracer() called

Tracer* tr = new Tracer{"a string"};
delete tr;  // ~Tracer() called
```

### 8.7 Constructor/Destructor Sequence

**Constructor:**
1. Base class constructor (if derived)
2. Data member constructors
3. Constructor body

**Destructor:**
1. Destructor body
2. Data member destructors
3. Base class destructor (if derived)

### 8.8 Initialization Without Constructors

**Member-wise initialization** (if members public):

```cpp
struct Work {
    std::string name;
    int number;
};

Work some_work {"Teach", 19};
```

**Copy initialization:**
```cpp
Work other_work {some_work};
```

**Default initialization:**
```cpp
Work df_work {};  // empty string "" and 0
```

**WARNING:** Without `{}`, local variables have undefined values for built-in types!

### 8.9 Universal and Uniform Initialization

`{}` is defined as universal and uniform initialization:

```cpp
X* p = new X{4};  // OK
X* p2 = new X=4;  // WRONG

std::vector<int> v1 {77};   // 1 element with value 77
std::vector<int> v2 (77);   // 77 elements with value 0
```

### 8.10 Default constructors

A constructor that can be called with no arguments. You need one when a default value makes logical sense or when the type is used as an element type in a data structure.

```cpp
struct Work {
    Work(std::string a = "work") : name{a} {};
};
```

### 8.11 Initializer-list Constructors

Constructor with `std::initializer_list<T>` argument:

```cpp
template<class T>
class Vector {
public:
    Vector(std::initializer_list<T> s);
};

Vector<int> v {1, 2, 3, 4};
```

**Overload resolution:**
- Empty `{}` -> default constructor
- `{values}` -> initializer-list constructor (has precedence)

### 8.12 Member initialization

Use the member initializer list. Members are initialized in declaration order, before the body runs:

```cpp
ClassName::ClassName(T1 arg1, T2 arg2) :
    member1{arg1},
    member2{arg2}
{
    // body
}
```

Assigning inside the body is less efficient — the member is default-initialized first, then assigned:

```cpp
Person::Person(std::string& n, std::string& a) : name{n} {
    address = a;  // default init + assignment — use initializer list instead
}
```

### 8.13 Delegating Constructors

Define constructor in terms of another:

```cpp
class X {
    int a;
public:
    X(int x) {
        if (0 < x && x <= max) a = x;
        else throw Bad_X(x);
    }
    X() : X{22} {}  // delegates to X(int)
    X(string s) : X{to<int>(s)} {}
};
```

### 8.14 Copy Operations

**Copy constructor:** `X(const X&)`
**Copy assignment:** `X& operator=(const X&)`

**Proper copy satisfies:**
- **Equivalence:** After `x = y`, any operation on x and y yields same results
- **Independence:** After `x = y`, operation on x should not change y

### 8.15 Shallow vs Deep Copy

**Shallow copy:** Copies only pointers, not values pointed to (shared state issue)

```cpp
struct S {
    int* p;
};

S x {new int{0}};
S y {x};  // shallow copy - both point to same int!
```

**Deep copy:** Copies values pointed to:

```cpp
struct S {
    int* p;
    S(const S& a) : p{new int{*a.p}} {}  // deep copy
};
```

### 8.16 Move operations

**Move constructor:** `X(X&&)` / **Move assignment:** `X& operator=(X&&)`

After moving `x` into `y`, `y` owns what `x` had and `x` is left in a valid but resource-free state. `std::move()` just casts to an rvalue reference — it doesn't move anything itself.

```cpp
T tmp {std::move(a)};  // cast to rvalue reference
```

### 8.17 Default operations

By default a class gets: default constructor, copy constructor, move constructor, copy assignment, move assignment, and destructor — all compiler-generated. Control them explicitly with `=default` and `=delete`:

```cpp
class X {
    X(int);
    X(double) = delete;  // prevent use
};

X(1);    // OK
X(0.1);  // ERROR
```

### 8.18 Resource handles

```cpp
template<class T>
class Handle {
    T* p;
public:
    Handle(T* pp) : p{pp} { }
    T& operator*() { return *p; }
    ~Handle() { delete p; }
};
```

Pointer members are tricky: the default constructor won't initialize the pointer, the default destructor won't delete it, and the default copy/move are wrong if the pointer represents ownership. You have to define all of these yourself.

---

## 9. How C++ Works - Compiler

### 9.1 Why C++ vs Java?

Java compiles for a virtual machine; an interpreter then translates to hardware at runtime. C++ compiles directly to machine code for the target architecture, which is why it's faster — but it also means you need to cross-compile for different targets.

### 9.2 Compilation Steps

```
Source file → Preprocessor → Translation unit → Compiler → Object file → Linker → Executable
```

1. **Preprocessing:** Handles `#include`, `#define`, preprocessor directives
2. **Compilation:** Produces object file from translation unit
3. **Linking:** Produces library or executable from object files

### 9.3 Preprocessor

Evaluates preprocessor directives, substitutes into code. Agnostic to C++ syntax.

```cpp
// CPP FILE
#define MAX_HGHT 720
#define AREA(a,b) (a*b)
int maxArea(int a) {
    return AREA(a, MAX_HGHT);
}

// TRANSLATION UNIT
int maxArea(int a) {
    return a*720;
}
```

### 9.4 Include Guards

Prevent multiple inclusion:

```cpp
#ifndef MY_FUN_H
#define MY_FUN_H
inline int incr(int i) {
    return i+1;
}
#endif
```

### 9.5 Compiler

- Parses translation unit
- Converts to assembly code for specific CPU
- Optimizes (O0, O1, O2, O3)
- Converts to machine instructions (object file)

**Object file:** Contains compiled code, can refer to undefined symbols

### 9.6 Linker

- Produces final output from object files
- Links object files by replacing references to undefined symbols
- Can produce shared library or executable

**Common errors:**
- Missing definitions
- Duplicate definitions

### 9.7 Static vs dynamic libraries

A static library is an archive of object files baked into the executable at compile time. The executable is self-contained but large, and changing one file requires recompiling everything.

A dynamic library is loaded at runtime. Only the library itself needs recompiling when something changes.

---

## 10. Autotools

### 10.1 GNU Autotools Suite

- **GNU Autoconf:** Generate configure script
- **GNU Automake:** Simplify creating makefiles
- **GNU Libtool:** Abstraction for portable library creation

### 10.2 Installation Process

```bash
./installer.sh -p <path> -t <flag>
```

Process:
1. `autogen.sh` - prepares environment
2. `configure` - creates makefiles from Makefile.in
3. `make` - compiles source code
4. `make check` - performs tests (optional)
5. `make install` - installs executables and libraries

### 10.3 autogen.sh

```bash
case `uname` in
    Darwin*) glibtoolize ;;
    *) libtoolize ;;
esac
aclocal
autoconf
automake --add-missing
```

### 10.4 configure.ac

Written with mix of shell and M4 macros:
- `AC_` prefix for autoconf macros
- `AM_` prefix for automake macros

**Key macros:**
- `AC_INIT(PFICT, 1.0)` - initialize package
- `AM_INIT_AUTOMAKE` - enable Automake
- `AC_PROG_CXX` - ensure C++ compiler available
- `AC_CONFIG_FILES([...])` - list of Makefile.in to process
- `AC_OUTPUT` - generate config.status and makefiles

### 10.5 Makefile.am

**Top-level:**
```makefile
AUTOMAKE_OPTIONS = foreign
SUBDIRS = m4 basic_utilities example
ACLOCAL_AMFLAGS = -I m4
```

**For executable:**
```makefile
AM_CXXFLAGS = @PFICT_CXXFLAGS@
bin_PROGRAMS = fun_example
fun_example_SOURCES = fun-example.cpp class1.cpp
fun_example_LDADD = @PFICT_LDADD@
```

**For library:**
```makefile
lib_LTLIBRARIES = libb_util.la
libb_util_la_SOURCES = b-utils.cpp
libb_util_la_LIBADD = @PFICT_LIBADD@
```

---

## 11. Memory Management

### 11.0 5-Minutes Questions

> Typical oral exam questions from this module:
- What are the **four memory areas** in a C++ program?
- What is **stack unwinding**?
- What does `new` do? What does `delete` do? In what order?
- What is a **memory leak**? Show an example.
- What is a **dangling pointer**? Show an example.
- What is **double deletion**?
- What is **RAII**? Why is it useful?
- What is **placement new**?
- What is the difference between `delete` and `delete[]`?

### 11.1 C++ Program Memory Areas

C++ programs use **four distinct memory areas**, each with different rules:

| Area | Who allocates | Lifetime | Notes |
|------|--------------|----------|-------|
| **const data** | Compiler | Whole program | Read-only, built-in types only |
| **stack** | Compiler (automatic) | Scope-based (LIFO) | Fast, cannot be directly manipulated |
| **free store / heap** | Programmer (`new`/`delete`) | Programmer-controlled | Flexible but error-prone |
| **global / static** | Compiler | Whole program | Initialized on first use |

**Stack** is the most important to understand:
- Allocation happens *just before* an object is created
- Deallocation happens automatically when the object goes out of scope (**stack unwinding**)
- Stack unwinding also triggers destructors — this is what makes RAII work

```
[Stack grows downward]
    main() frame
      ↳ f() frame  ← local variables live here
          ↳ g() frame
```

### 11.2 Operators `new` and `delete`

**`new` does two things in order:**
1. Calls `operator new()` to allocate raw uninitialized memory (raises `std::bad_alloc` if no space)
2. Calls the constructor to initialize the object

**`delete` does two things in order:**
1. Calls the destructor of the object
2. Calls `operator delete()` to release the memory

```cpp
// Correct use: always use {} for initialization
void f() {
    int* a {new int{10}};
    // ... some code ...
    delete a;
}
```

**Under the hood (defined in `<new>`):**
```cpp
void* operator new(size_t) throw(std::bad_alloc);   // allocates
void  operator delete(void* p);                      // deallocates

void* operator new[](size_t) throw(std::bad_alloc); // for arrays
void  operator delete[](void* p);                    // for arrays
```

> `new` (the operator) ≠ `operator new()` (the function):  
> `new` calls `operator new()` internally, then calls the constructor.

**Placement `new`** — construct object in *already allocated* memory:
```cpp
char* buf = new char[sizeof(std::string)];   // pre-allocated buffer
std::string* p = new (buf) std::string("hi"); // placement new — no allocation
std::string* q = new std::string("hi");       // ordinary allocation
```

### 11.3 `new[]` and `delete[]` for Arrays

```cpp
int* arr = new int[10];   // allocate array of 10 ints
delete[] arr;              // MUST use delete[] for arrays, not delete!
```

> `delete` on an array only destroys the **first** element.  
> `delete[]` destroys all elements. The size is stored internally with a small overhead.

### 11.4 Memory Management Issues

These are the **three classic bugs** with raw pointers:

#### 1. Memory Leak
Call `new`, never call `delete`. If frequent, system runs out of memory.

```cpp
int f() {
    int* a {new int{10}};
    if (*a == 10) {
        return 4;   // LEAK: delete never reached!
    }
    delete a;
    return 5;
}
```

#### 2. Dangling Pointer (Premature Deletion)
Call `delete`, then try to use the pointer. Leads to bad read/write — **undefined behavior**.

```cpp
int f() {
    int* a {new int{10}};
    if (*a == 10) {
        delete a;
    }
    // some code...
    *a = 5;  // DANGER: memory may belong to something else now
}
```

Fix: set pointer to `nullptr` after delete → dereference will crash cleanly.
```cpp
delete a;
a = nullptr;
```

#### 3. Double Deletion
Call `delete` twice on the same pointer. Leads to **memory corruption**.

```cpp
int f() {
    int* a {new int{10}};
    if (*a == 10) {
        delete a;
    }
    // ...
    delete a;  // DANGER: memory already released!
}
```

### 11.5 Resource Management Rules

> **Resources** = anything obtained from the OS that must be returned: memory, files, locks, sockets.

**Two golden rules:**

| Rule | Reason |
|------|--------|
| Do **not** use `new` for local objects | Put them on the stack (automatic lifetime) |
| Do **not** use "naked" `new`/`delete` | Use RAII handle classes instead |

### 11.6 RAII (Resource Acquisition Is Initialization)

**RAII** is *the* C++ idiom for resource safety. See **Section 8.5.1** for the full explanation.

The pattern applied to memory:

```cpp
class Handle {
    int* p;
public:
    Handle(int* pp) : p{pp} { }       // acquire
    int& operator*() { return *p; }   // dereference
    ~Handle() { delete p; }           // release — automatic!
};

void f() {
    Handle obj_handle {new int{10}};
    std::cout << *obj_handle;
}   // obj_handle goes out of scope → ~Handle() → delete called → no leak!
```

**Why this is safe:** even if `f()` throws or returns early, the destructor is always called.

**Accessing the raw resource from a handle** — sometimes an API needs the raw pointer:
```cpp
// Option 1: explicit get()
int* raw = handle.get();

// Option 2: implicit via operator* or operator->
*handle = 5;
```

### 11.7 Copy Semantic and Handle Classes

When you copy a handle, the copy also points to the same resource → **shallow copy problem**.

**Strategies:**

| Strategy | When to use |
|---|---|
| Prohibit copying (`=delete`) | When sharing the resource makes no sense |
| Reference-count | When multiple owners are needed (→ `shared_ptr`) |
| Transfer ownership (move) | When there's always one owner (→ `unique_ptr`) |
| Deep copy | When each handle needs its own independent copy |

---

## 12. Derived Classes and Class Hierarchies

### 12.1 Class relationships

Two fundamental relationships: "part of" (data members) and "extends" (inheritance / class hierarchies).

### 12.2 Class Hierarchy Example

```cpp
class Shape { /* ... */ };
class Square : public Shape { /* ... */ };
class Circle : public Shape { /* ... */ };
```

### 12.3 Inheritance types

There are two kinds. Implementation inheritance reuses facilities from a base class. Interface inheritance lets you use different derived classes interchangeably — that's runtime polymorphism.

### 12.4 Derived Class Example

```cpp
struct Employee {
    string first_name, family_name;
    char middle_initial;
    Date hiring_date;
    short department;
};

struct Manager : public Employee {
    list<Employee*> group;
    short level;
};
```

**Manager has same members as Employee + its own members**

### 12.5 Derived Class Usage

```cpp
void f(Manager m1, Employee e1) {
    std::vector<Employee*> vec {&m1, &e1};  // OK
}

// Manager* is also Employee*
// Manager& is also Employee&
// Employee* is NOT Manager* (explicit conversion needed)
```

### 12.6 Constructors and Destructors in Derived Classes

**Constructor order:**
1. Base class constructor
2. Data member constructors
3. Constructor body

**Destructor order:**
1. Destructor body
2. Data member destructors
3. Base class destructor (only if base destructor is virtual)

**Base class destructors should generally be virtual**

### 12.7 Slicing

When using pointer to base class for derived object, wrong copy constructor may be called:

```cpp
struct X { int m_number; };
struct Y : public X { int m_second_number; };

void f(X* p) {
    X h = *p;  // if p points to Y, only m_number copied (slicing)
}
```

**Solutions:**
- `=delete` copy constructor in base
- Make base class private or protected

### 12.8 Inheriting Constructors

```cpp
class Y : public X {
    using X::X;  // inherits X constructors
};
```

### 12.9 Navigating Class Hierarchies

**Options:**
1. Use objects of single type
2. Type fields (error-prone)
3. Virtual functions
4. Abstract classes

### 12.10 Virtual functions

A `virtual` function can be overridden in a derived class. The argument list must stay the same, and so must the return type — though there's an exception for pointers/references (covariant return types).

```cpp
struct Employee {
    virtual void print() const;
};

struct Manager : public Employee {
    void print() const override;  // overrides virtual
};

void Manager::print() const {
    Employee::print();  // call base implementation
    std::cout << level << std::endl;
}
```

### 12.11 Polymorphism

Virtual enables runtime polymorphism - use different implementations according to actual object:

```cpp
void f(std::vector<Employee*> vec) {
    for (Employee* elem : vec) {
        elem->print();  // correct print() selected at runtime
    }
}
```

**Objects must be manipulated with pointers or references**

### 12.12 Override Control

| Keyword | Purpose |
|---------|---------|
| `virtual` | Function may be overridden |
| `override` | Specifies we want to override virtual (compiler error if not) |
| `final` | Prohibits further override |

```cpp
class Base {
    virtual void f();
    virtual void g() final;  // cannot be overridden
};

class Derived : public Base {
    void f() override;  // OK
    void g() override;  // ERROR: g is final
};
```

### 12.13 Abstract classes

A class with at least one pure virtual function is abstract:

```cpp
virtual T pureVirtualFunction(U arg) = 0;
```

You can't instantiate an abstract class directly. Only derived classes that override all pure virtual methods can be instantiated. This is the mechanism for interface inheritance.

### 12.14 Access Control

| Access | Who Can Access |
|--------|----------------|
| **private** | Member functions and friends of class |
| **protected** | As private + member functions and friends of derived classes |
| **public** | Any function |

**protected data members usually a design error**

### 12.15 Access Control for Base Classes

| Inheritance | Effect |
|-------------|--------|
| **public** | Creates subtype, runtime polymorphism |
| **private** | Restricts interface, base cannot be further derived through derived |
| **protected** | As private, but can be further derived |

### 12.16 Multiple Inheritance

```cpp
class A : public B, public C { /* ... */ };
```

**Replication issue:** If B and C both derive from D, A has two D subobjects

**Solution:** Virtual base class:

```cpp
class B : public virtual D { /* ... */ };
class C : public virtual D { /* ... */ };
```

---

## 13. Operator Overloading

### 13.1 Overview

You can redefine operators for user-defined types:

```cpp
class Complex {
    double re, im;
public:
    Complex(double r, double i) : re{r}, im{i} { }
    Complex operator+(const Complex&);
    Complex operator*(const Complex&);
};

Complex c = Complex{2, 3} + Complex{5, 6};
```

**Operator name:** `operator` followed by symbol

### 13.2 Overloadable Operators

Most operators can be overloaded.

**Cannot overload:**
- `::` (scope resolution)
- `.` (member selection)
- `.*` (member selection through pointer to member)
- `sizeof`, `alignof`, `typeid`
- `?:` (ternary operator)

**Cannot define new operators**

### 13.3 Binary and Unary Operators

**Binary operators:**
- Non-static member: `aa.operator@(bb)`
- Non-member: `operator@(aa, bb)`

**Unary operators:**
- Non-static member: `aa.operator@()`
- Non-member: `operator@(aa)`

**Non-member necessary when left operand not in our control**

### 13.4 Overloading <<

For output streams, must be non-member:

```cpp
std::ostream& operator<<(std::ostream& out, const Y& y) {
    return y.someFunction(out);
}

class Y {
    int j;
public:
    std::ostream& someFunction(std::ostream& out) {
        out << j;
        return out;
    }
};
```

**Or use friend:**

```cpp
class Y {
    int j;
    friend std::ostream& operator<<(std::ostream& out, const Y& y);
};

std::ostream& operator<<(std::ostream& out, const Y& y) {
    out << y.j;
    return out;
}
```

### 13.5 Special Operators

**operator[]:** Subscript operator

**operator():** Function call operator (creates functors)

```cpp
class CalculateAverageOfPowers {
public:
    CalculateAverageOfPowers(float p) : acc(0), n(0), p(p) {}
    void operator()(float x) {
        acc += pow(x, p);
        n++;
    }
    float getAverage() const { return acc / n; }
private:
    float acc;
    int n;
    float p;
};

CalculateAverageOfPowers functor{1};
functor(10);  // function call using operator()
```

### 13.6 Functors Example

```cpp
CalculateAverageOfPowers avg{2};
std::vector<float> dataA {0.1, 0.2, 10};
avg = std::for_each(dataA.begin(), dataA.end(), avg);
// Calls avg for each element, maintains state
```

---

## 14. Runtime Polymorphism

### 14.1 Dynamic Cast

Returns valid pointer if object is of expected type, `nullptr` otherwise:

```cpp
void f(B* ptr) {
    D* der_ptr {dynamic_cast<D*>(ptr)};
    if (der_ptr != nullptr) {
        // use der_ptr
    }
}
```

### 14.2 Run-time Type Information (RTTI)

`dynamic_cast<T*>()` works from polymorphic types (base classes with virtual methods).

Compiler automatically associates information on actual type.

### 14.3 Dynamic Cast: Pointer vs Reference

**Pointer:** Returns `nullptr` on failure (a question)

**Reference:** Throws `bad_cast` exception on failure (an assertion)

```cpp
void f(B& r) {
    try {
        D& der_ref {dynamic_cast<D&>(r)};
    } catch (bad_cast) {
        // handle error
    }
}
```

**In general, prefer pointers for polymorphism**

### 14.4 Misuses of RTTI

Don't use `dynamic_cast` in a constructor. In general, reach for virtual functions and interfaces first — RTTI should be a last resort, not the default way to dispatch on type.

**Wrong approach:**
```cpp
void rotate(Shape* r) {
    if (dynamic_cast<Circle*>(r)) { /* do nothing */ }
    else if (dynamic_cast<Triangle*>(r)) { /* rotate triangle */ }
    // ...
}
```

**Correct approach:**
```cpp
class Shape {
public:
    virtual void rotate() = 0;
};

Shape* ptr_triangle {new Triangle{}};
ptr_triangle->rotate();  // correct rotate() called
```

### 14.5 Other Casts

| Cast | Purpose |
|------|---------|
| `static_cast<T>()` | Convert between related types, no runtime checks |
| `reinterpret_cast<T>()` | Convert between unrelated types (changes bit interpretation) |
| `const_cast<T>()` | Remove constness from pointers/references |

**When to use:**
- `static_cast`: First choice for related types
- `dynamic_cast`: For downcasting polymorphic types with runtime checks
- `const_cast`: Remove constness from non-const objects
- `reinterpret_cast`: Most disruptive, between unrelated types

---

## 15. Templates

### 15.1 Overview

Templates support generic programming: you write one implementation and the type becomes a parameter. Type checking happens at compile time, so templates give you compile-time polymorphism with full type safety.

### 15.2 Template Example

```cpp
template<typename C>
class MyString {
public:
    MyString();
    explicit MyString(const C*);
    MyString(const MyString&);
    MyString operator=(const MyString&);
    C& operator[](int n) { return ptr[n]; }
private:
    int sz;
    C* ptr;
};

MyString<char> s1;       // specialization for char
MyString<wchar_t> s2;    // specialization for wchar_t
```

`template<typename C>` is equivalent to "for all C" (∀C)

### 15.3 Template Implementation Guidelines

1. Start from particular case
2. Debug and make sure it works
3. Extend to generic template case

### 15.4 Class templates

All members must be defined, and the definition must be in the header file — if it's in a `.cpp`, the linker will complain. You can't overload the name of a class template.

### 15.5 Template Instantiation

Process of generating class from template + type arguments.

**During instantiation:**
- Compiler generates only members actually used
- Type checking applied
- Type equivalence: Templates with aliases as arguments are same type

### 15.6 Type Aliases

Particularly useful for templates:

```cpp
template<typename T>
class Vector {
public:
    using value_type = T;
    using iterator = Vector_iter<T>;
};
```

### 15.7 Member Templates

Members can be templates:

```cpp
template<typename S>
class complex {
    S re, im;
public:
    template<typename T>
    complex(const complex<T>& c) : re{c.real()}, im{c.imag()} { }
};

complex<float> cf1 {};
complex<double> cd1 {cf1};  // OK: float to double
```

**Member templates cannot be virtual**

### 15.8 Function Templates

```cpp
template<typename T>
void sort(std::vector<T>&);

template<typename T1, typename T2>
std::pair<T1, T2> make_pair(T1 a, T2 b) {
    return {a, b};
}

auto x = make_pair(1, 2);  // pair<int, int>
```

**Template type argument deduced from function arguments**

### 15.9 Variadic Templates

Type-safe mechanism for arbitrary number of parameters with arbitrary types:

```cpp
template<typename T, typename... Args>
void f(T value, Args... args) {
    // do something with value
    f(args...);  // recursive call
}
```

**Parameter pack:** Sequence of type and value pairs, first removed at each recursive call

---

## 16. Standard Library

### 16.1 Overview

The standard library is specified by the ISO C++ standard, so any conforming implementation provides it. It's portable, efficient, and is the base that most other C++ libraries build on. Everything lives in headers under the `std` namespace.

### 16.2 Containers

Containers hold multiple objects. Sequence containers hold them in order; associative containers support key-based lookups. All containers are resource handles with well-defined copy and move semantics.

### 16.3 Sequence Containers

| Container | Description |
|-----------|-------------|
| `std::vector<T, A>` | Contiguous allocation |
| `std::deque<T, A>` | Non-contiguous |
| `std::list<T, A>` | Doubly-linked list |
| `std::forward_list<T, A>` | Singly-linked list |

**In general, use `std::vector<T>` unless specific needs**

```cpp
std::vector<int> vec {1, 2, 3, 4};
std::list<int> ls {1, 2, 3, 4};
```

### 16.4 Ordered Associative Containers

| Container | Description |
|-----------|-------------|
| `std::map<K, V, C, A>` | Ordered map from K to V |
| `std::multimap<K, V, C, A>` | Map allowing multiple entries with same key |
| `std::set<K, C, A>` | Ordered set |
| `std::multiset<K, C, A>` | Set allowing duplicates |

```cpp
std::map<int, std::string> map_int_s;
map_int_s.insert(std::make_pair(4, "four"));
map_int_s[5] = "five";
auto entry_it = map_int_s.find(4);
```

### 16.5 Unordered Associative Containers

| Container | Description |
|-----------|-------------|
| `std::unordered_map<K, V, H, E, A>` | Unordered map |
| `std::unordered_set<K, H, E, A>` | Unordered set |

### 16.6 Container Adaptors

| Adaptor | Description |
|---------|-------------|
| `std::priority_queue<T, C, Cmp>` | Priority queue |
| `std::queue<T, C>` | Queue |
| `std::stack<T, C>` | Stack |

### 16.7 Almost Containers

| Type | Description |
|------|-------------|
| `std::array<T, N>` | Fixed-size array |
| `std::basic_string<C, Tr, A>` | String representation |

### 16.8 Iterators

Similar to pointers, used to iterate over sequences:

```cpp
std::vector<int> vec {1, 2, 3, 4};
std::vector<int>::iterator vec_iter = vec.begin();
while (vec_iter != vec.end()) {
    ++(*vec_iter);  // increase value
    ++vec_iter;     // move to next
}
```

**Iterator types:**
- Input/output iterators (for streams)
- Forward iterators (only forward)
- Bidirectional iterators (forward/backward)
- Random access iterators (any position)

### 16.9 Algorithms

~80 generic algorithms in `<algorithm>` header.

**Operate on sequences defined by iterator pairs `[b, e)`**

**Non-modifying:**
- `all_of`, `any_of`, `none_of`
- `count`, `find`
- `equal`, `mismatch`, `search`

**Modifying:**
- `for_each`, `transform`
- `copy`, `unique`, `remove`, `replace`
- `rotate`, `random_shuffle`, `swap`

**Sort and search:**
- `sort`, `binary_search`
- `merge`, `min`, `max`

### 16.10 Strings

```cpp
using std::string = std::basic_string<char>;
using std::wstring = std::basic_string<wchar_t>;

std::string empty {};
std::string c_style {"this is a C-style string"};
std::string another {c_style};  // copy
```

### 16.11 I/O Streams

Convert typed values to/from byte sequences.

**Predefined streams:** `std::cout`, `std::cerr`, `std::clog`, `std::cin`

**File streams:**
```cpp
#include <fstream>
std::ofstream fout("test.txt");
fout << "a line" << std::endl;
fout.close();

std::ifstream fin("test.txt");
std::string line;
while (std::getline(fin, line)) {
    std::cout << line << std::endl;
}
fin.close();
```

**String streams:**
```cpp
#include <sstream>
std::stringstream ss {};
ss << "hello" << ",";
std::cout << ss.str() << std::endl;
```

---

## 17. Smart Pointers

### 17.1 5-Minutes Questions

> These are typical oral exam questions from this module:
- What is an **lvalue**? *(an object with identity that is not movable; referred to by a name/pointer)*
- What is an **rvalue**? *(a movable value, typically a temporary; not necessarily has identity)*
- What is a **dangling pointer**?
- What is the difference between `unique_ptr` and `shared_ptr`?
- What happens when a `shared_ptr` use_count reaches 0?
- What is a **cyclic reference** and how do you break it?

### 17.2 Raw pointer problems

A dangling pointer points to memory that's already been freed. Setting it to `nullptr` after `delete` prevents the worst outcomes.

```cpp
char* buffer = new char[256];
delete[] buffer;  // now buffer is dangling
buffer = nullptr;  // now it's not dangling
```

A memory leak is just never calling `delete`.

```cpp
int performTask() {
    char* buffer = new char[256];
    if (some_condition) {
        return 1;  // LEAK: delete never called
    }
    delete[] buffer;
    return 0;
}
```

### 17.3 Smart pointers

The standard library has three pointer wrappers (`#include <memory>`):

| Type | Purpose |
|------|---------|
| `std::unique_ptr` | Scoped pointer, exclusive ownership |
| `std::shared_ptr` | Shared ownership, reference counted |
| `std::weak_ptr` | Avoids circular references |

### 17.4 Unique Pointer

Scoped pointer with **exclusive ownership**:
- Constructor wraps a raw pointer
- Destructor performs `delete` automatically
- **Cannot be copied** (no copy constructor) — only moved
- Most **lightweight** smart pointer (zero overhead vs raw pointer)
- Represents: *"I am the only owner"*

```cpp
// Old style (avoid):
std::unique_ptr<string> up(new std::string("ciao"));

// Preferred (exception-safe, cleaner):
auto up = std::make_unique<std::string>("ciao");  // C++14

// Cannot copy:
// std::unique_ptr<string> up2 = up;  // ERROR: deleted copy constructor

// Can move (transfers ownership):
std::unique_ptr<string> up2 = std::move(up);  // up is now nullptr
```

**`make_unique` vs `new`:** `make_unique` is exception-safe because it constructs the object and creates the `unique_ptr` in a single operation (avoids rare leak if allocation partially fails).

### 17.5 Unique Pointer - Pass to Function

**Solution 1:** Move and return:
```cpp
std::unique_ptr<T1> f1(std::unique_ptr<T1> up) {
    // do stuff
    return up;  // returns by move
}
std::unique_ptr<T1> up1(new T1());
up1 = f1(std::move(up1));
```

**Solution 2:** Pass by const reference:
```cpp
void f2(const std::unique_ptr<T1>& up) {
    // do stuff
}
std::unique_ptr<T1> up1(new T1());
f2(up1);
```

### 17.6 Unique Pointer Methods

```cpp
string* s = up.release();  // returns raw pointer, releases ownership
up.reset();                 // destroys object, releases ownership
up.reset(new string("hi")); // destroys old, acquires new
```

### 17.7 Shared Pointer

Shared ownership with reference counting:

```cpp
std::shared_ptr<string> sp(new string("ciao"));  // use_count = 1
std::shared_ptr<string> sp2 = sp;  // use_count = 2

// When use_count becomes 0, object deleted
```

**Exception-safe creation:**
```cpp
std::shared_ptr<string> sp = std::make_shared<string>("s");
```

### 17.8 Shared Pointer Methods

```cpp
sp.use_count();  // get reference count
sp.reset();      // decrease count, release if 0
string* p = sp.get();  // get raw pointer
```

### 17.9 Shared Pointer Cast

```cpp
std::shared_ptr<B> pb = std::make_shared<D>();
std::shared_ptr<D> pd1 = std::dynamic_pointer_cast<D>(pb);
std::shared_ptr<D> pd2 = std::static_pointer_cast<D>(pb);
```

### 17.10 Circular Reference Problem

When two objects hold `shared_ptr`s to each other, neither use_count ever reaches 0 → **memory leak**:

```cpp
struct Son { std::shared_ptr<Mum> mum; };
struct Mum { std::shared_ptr<Son> son; };

int main() {
    auto son1 = std::make_shared<Son>(); // Son  use_count = 1
    auto mum1 = std::make_shared<Mum>(); // Mum  use_count = 1
    son1->mum = mum1;  // Mum  use_count = 2
    mum1->son = son1;  // Son  use_count = 2
}   // son1 and mum1 go out of scope → use_count drops to 1, NOT 0
    // NEITHER OBJECT IS DESTROYED → MEMORY LEAK!
```

**Visual:**
```
son1 ──→ [Son] ──shared_ptr──→ [Mum] ←──shared_ptr── mum1
           ↑                                  │
           └────────────shared_ptr────────────┘
```

### 17.11 Weak Pointer

`weak_ptr` observes a `shared_ptr` **without participating in ownership** (does not increment use_count). Used to **break cyclic references**.

- Does **not** perform automatic delete
- Cannot use `->` directly — must call `.lock()` first to get a temporary `shared_ptr`
- `.lock()` returns empty `shared_ptr` if the object was already deleted

```cpp
std::shared_ptr<T1> sp = std::make_shared<T1>();
std::weak_ptr<T1> wp = sp;   // use_count still = 1

// Safe access:
if (auto tmp_sp = wp.lock()) {   // tmp_sp is a shared_ptr (use_count += 1)
    tmp_sp->getParam();
}   // tmp_sp goes out of scope (use_count back to 1)

wp.use_count();  // how many shared_ptrs point to the object
wp.expired();    // true if use_count == 0 (object was deleted)
```

**Cyclic reference fixed with `weak_ptr`:**
```cpp
struct Son { std::weak_ptr<Mum> mum; };  // weak: does not own
struct Mum { std::weak_ptr<Son> son; };  // weak: does not own

int main() {
    auto son1 = std::make_shared<Son>(); // Son  use_count = 1
    auto mum1 = std::make_shared<Mum>(); // Mum  use_count = 1
    son1->mum = mum1;  // Mum  use_count = 1 (weak!)
    mum1->son = son1;  // Son  use_count = 1 (weak!)
}   // son1, mum1 go out of scope → use_count → 0 → BOTH DESTROYED ✓
```

### 17.12 Wrong Use of Smart Pointers

```cpp
string* p = new string("ciao");
std::shared_ptr<string> sp(p);   // count = 1
std::shared_ptr<string> sp2(p);  // count = 1 - WRONG!

// Rule: Assign object to smart pointer as soon as created
std::shared_ptr<string> sp1 = std::make_shared<string>("ciao");
```

---

## 18. Bitwise Operators, POD, I/O Streams

### 18.1 Bitwise Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `&` | Bitwise AND | `a & b` |
| `|` | Bitwise OR | `a | b` |
| `^` | Bitwise XOR | `a ^ b` |
| `~` | Complement | `~b` |
| `<<` | Left shift | `a << 2` |
| `>>` | Right shift | `a >> 2` |

```cpp
uint_fast8_t a = 11;  // 0000 1011
uint_fast8_t b = 5;   // 0000 0101
uint_fast8_t c = a & b;  // 0000 0001 = 1
uint_fast8_t d = a | b;  // 0000 1111 = 15
uint_fast8_t e = a ^ b;  // 0000 1110 = 14
```

### 18.2 Access a Bit

```cpp
// Get bit at position offset:
bool val = buffer[(int)floor(offset/8)] >> (7-offset%8) & 1U;

// Set bit at position offset:
buffer[(int)floor(offset/8)] |= 1U << (7-offset%8);
```

### 18.3 Serialize Header with Bitwise Operators

```cpp
struct MacHdr {
    uint_fast8_t sn = 27;
    uint_fast8_t src = 1;
    uint_fast8_t dest = 3;
    const size_t sn_size = 7;
    const size_t addr_size = 6;
    bool serialize(char* buffer, size_t& offset) const;
    bool deserialize(const char* buffer, size_t& offset);
};
```

### 18.4 POD Serialization

For simple structures, use POD with bitfields:

```cpp
struct MacHdr {
    uint_fast8_t sn:7;
    uint_fast8_t src:6;
    uint_fast8_t dest:6;
};

MacHdr hdr1 = {5,4,3};
char buffer[10];
memcpy(buffer, &hdr1, sizeof(hdr1));  // serialize
memcpy(&hdr2, buffer, sizeof(hdr2));  // deserialize
```

### 18.5 File Streams

```cpp
#include <fstream>

// Write
std::ofstream fout("test.txt");
fout << "a line" << std::endl;
fout.close();

// Read
std::ifstream fin("test.txt");
std::string line;
while (std::getline(fin, line)) {
    std::cout << line << std::endl;
}
fin.close();
```

### 18.6 Binary File Streams

```cpp
std::ifstream fin("file.bin", std::ios::binary);
std::ofstream fout("file.bin", std::ios::binary);

char w_buffer[25];
fout.write(w_buffer, size_b);

char r_buffer[25];
fin.read(r_buffer, 25);
```

---

## 19. Socket Programming

### 19.1 What is a socket?

A socket is a standard Unix file descriptor used to communicate with other programs. The network layer handles host-to-host delivery; the transport layer (where sockets live) handles process-to-process. A socket is identified by `<ip_address, port>`.

### 19.2 Socket Types

| Type | Description | Use |
|------|-------------|-----|
| `SOCK_DGRAM` | UDP - fast, unreliable, connectionless | Audio/video, games |
| `SOCK_STREAM` | TCP - reliable, two-way connected | FTP, HTTP, SSH |
| `SOCK_RAW` | Low-level, advanced | Special uses |

### 19.3 Required Headers

```cpp
#include <string.h>      // memset, memcpy
#include <sys/socket.h>  // socket, bind, sockaddr
#include <netinet/in.h>  // sockaddr_in
#include <arpa/inet.h>   // htonl, htons, inet_addr
#include <unistd.h>      // read, write, close
```

### 19.4 Create Socket

```cpp
int socket(family, type, protocol);
// family: AF_INET (IPv4)
// type: SOCK_DGRAM (UDP) or SOCK_STREAM (TCP)
// protocol: 0 for IP

int udp_socket_fd = socket(AF_INET, SOCK_DGRAM, 0);
int tcp_socket_fd = socket(AF_INET, SOCK_STREAM, 0);
```

### 19.5 Address Structure

```cpp
struct sockaddr_in my_addr = {0};
my_addr.sin_family = AF_INET;
my_addr.sin_port = htons(listen_port);
my_addr.sin_addr.s_addr = htonl(INADDR_ANY);  // all interfaces
```

**Byte order functions:**
- `htonl`, `htons`: host to network
- `ntohl`, `ntohs`: network to host

### 19.6 Bind

```cpp
if (bind(sckfd, (struct sockaddr*) &my_addr, sizeof(my_addr)) < 0) {
    // ERROR
}
```

### 19.7 UDP Send/Receive

```cpp
// Receive
struct sockaddr_in srcaddr = {0};
socklen_t addrlen = sizeof(srcaddr);
int recv_bytes = recvfrom(sckfd, rx_buffer, max_size, 0,
    (struct sockaddr*)&srcaddr, &addrlen);

// Send
struct sockaddr_in dest_addr = {0};
dest_addr.sin_family = AF_INET;
dest_addr.sin_port = htons(dest_port);
inet_pton(AF_INET, dest_ip, &dest_addr.sin_addr);
int w_bytes = sendto(sckfd, tx_buf, size2tx, 0,
    (struct sockaddr*)&dest_addr, sizeof(dest_addr));
```

### 19.8 TCP Server

```cpp
// Listen
if (listen(scklist, 5) < 0) { /* ERROR */ }

// Accept
struct sockaddr_in client_addr;
socklen_t addr_l = sizeof(client_addr);
int sockfd = accept(scklist, (struct sockaddr*)&client_addr, &addr_l);

// Receive/Send
int recv_bytes = recv(sockfd, buf, max_size, 0);
int sent_bytes = send(sockfd, buf, size, 0);

close(sockfd);
close(scklist);
```

### 19.9 TCP Client

```cpp
// Connect
struct sockaddr_in serv_addr = {0};
serv_addr.sin_family = AF_INET;
serv_addr.sin_port = htons(server_port);
inet_pton(AF_INET, serv_ip, &serv_addr.sin_addr);

if (connect(sckfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) {
    // ERROR
}

// Send/Receive
send(sckfd, buf, size, 0);
recv(sckfd, buf, max_size, 0);

close(sckfd);
```

### 19.10 SIGPIPE Signal

Sent when writing to socket with hardware fault. Process terminates by default.

**Solution 1:** Ignore signal:
```cpp
struct sigaction act;
memset(&act, '\0', sizeof(act));
act.sa_handler = SIG_IGN;
sigaction(SIGPIPE, &act, NULL);
```

**Solution 2:** Handle signal:
```cpp
void handleIt(int sig_id) { /* handle */ }
act.sa_handler = &handleIt;
sigaction(SIGPIPE, &act, NULL);
```

### 19.11 Socket Options

```cpp
int option = 1;
setsockopt(socketfd, SOL_SOCKET, SO_REUSEADDR, (char*)&option, sizeof(option));
```

---

## 20. Threads and Lambdas

### 20.0 5-Minutes Questions

> Typical oral exam questions from this module:
- What is the difference between a **process** and a **thread**?
- What are the **three states** a process/thread can be in?
- What does **join** do? What does **detach** do?
- What happens if you don't join or detach a thread?
- Can you join a detached thread?
- How do you pass a parameter by reference to a thread?
- What does `std::move()` do when passing to a thread?
- What is the **capture list** of a lambda?
- What is the difference between `[a]` and `[&a]` in a lambda?
- What does `mutable` mean on a lambda?

### 20.1 Why parallel programming?

You need it when a program genuinely has to do two things at once — for example:

```cpp
// Thread 1: read from stdin, send to socket
while(true) {
    getline(std::cin, data);
    write(sk_fd, data, data.size());
}

// Thread 2: read from socket, print to stdout
while(true) {
    read(sk_fd, rx_data, MAX_SIZE);
    std::cout << rx_data << std::endl;
}
```

### 20.2 Process vs thread

A **process** is the OS abstraction of a running program. It has its own virtual CPU, address space, and resources. The OS saves and restores its state (registers, memory, I/O) on a context switch. A program is static; a process is the activity of executing it.

A **thread** is a task running inside a process. Threads share the same address space but execute largely independently. Switching between threads in the same process is cheaper than switching processes.

### 20.2.1 Process State Diagram

A process (or thread) is always in one of three states:

```
                  ┌─────────────────────────────────┐
                  │ needs to block for a resource    │
                  │ (voluntary transition)           │
                  ▼                                  │
            ┌─────────┐    resource ready        ┌──────────┐
            │ BLOCKED │ ──(involuntary)──────────→│  READY   │
            └─────────┘                           └──────────┘
                                                       │
                                                 scheduler picks me
                                                 (involuntary)
                                                       │
                                                       ▼
                                                  ┌─────────┐
                                                  │ RUNNING │
                                                  └─────────┘
```

- **Running:** actually using the CPU at that instant
- **Ready:** runnable but waiting for CPU (scheduler decides)
- **Blocked:** cannot run right now (e.g. waiting for I/O, mutex)

### 20.3 Thread Advantages over Processes

| Advantage | Detail |
|---|---|
| Shared memory | All threads share address space → easy intra-thread communication |
| Lightweight | Easier to create, destroy, manage |
| Fast context switch | Switching within the same process is cheaper than switching processes |

### 20.4 Thread Disadvantages vs Processes

| Disadvantage | Detail |
|---|---|
| Single crash kills all | If one thread crashes, the whole program crashes; a process crash only kills that process |
| No distribution | All threads must run on the same machine; multi-process can become distributed |
| Shared state complexity | Shared memory requires careful synchronization (see §21) |

### 20.5 Threads in C++

```cpp
#include <thread>

void incr(int n_times) {
    for (int i = 0; i < n_times; i++)
        a = a + 1;
}

int main() {
    std::thread thr(incr, 200);
    thr.join();
}
```

**Constructor:** `thread(Function&& f, Args&&... args)`

### 20.6 configure.ac for pthread

```cpp
AC_CHECK_LIB(pthread, pthread_create, [LIBS="$LIBS -lpthread"])
```

### 20.7 Join vs Detach

A dispatched thread **must** be either joined or detached. If neither happens and the `std::thread` object goes out of scope, the destructor calls `std::terminate()` → program crashes.

**Join** — wait for the thread to complete:
```cpp
std::thread thr(incr, 200);
// ... other stuff ...
thr.join();   // main blocks here until incr finishes
```

**Detach** — let thread run independently (fire and forget):
```cpp
std::thread thr(incr, 200);
thr.detach(); // main forgets thr; thr terminates after its task
              // WARNING: if main exits first, thr is killed!
```

- A detached thread that runs forever (or chooses when to stop) is called a **daemon thread**
- **Dangerous in general: do not use detach unless you know exactly what you are doing**
- After detach, `thr` no longer refers to the thread — `get_id()` returns empty

**Safety check before join:**
```cpp
if (thr.joinable()) { thr.join(); }
// joinable() returns false on detached or default-constructed threads
```

### 20.8 Thread ID

```cpp
// From within any thread:
auto my_id = std::this_thread::get_id();

// From outside (only joinable threads):
auto thr_id = thr1.get_id();

// After detach, get_id() prints:
// "thread::id of a non-executing thread"
```

### 20.9 Thread Management with RAII

**Problem:** if an exception or early `return` interrupts a function after a thread is dispatched but before `join()`, the thread destructor crashes the program.

**Solution 1:** try-catch (not elegant):
```cpp
std::thread thr(incr, 200);
try {
    // ... other stuff ...
} catch (...) {
    thr.join();  // join in catch too
}
if (thr.joinable()) { thr.join(); }
```

**Solution 2 (preferred): RAII wrapper** — destructor always joins:
```cpp
class ThreadGuard {
    std::thread thr;
    void incr() { /* ... */ }
public:
    ThreadGuard() : thr(&ThreadGuard::incr, this, 200) {}
    ~ThreadGuard() {
        if (thr.joinable()) thr.join();  // always called, even on exception
    }
};
```

### 20.10 Thread Task Types

The `@f` task argument to `std::thread` can be:

**1. A free function:**
```cpp
int a = 0;
void incr(int n_times) {
    for (int i = 0; i < n_times; i++) a = a + 1;
}
int main() {
    std::thread thr(incr, 200);
    thr.join();
}
```

**2. A member function (with pointer to `this`):**
```cpp
struct A {
    int a;
    void incr(int n_times) {
        for (int i = 0; i < n_times; i++) a = a + 1;
    }
    void doIncr() {
        std::thread tr(&A::incr, this, 200); // this → executes this->incr(200)
    }
};
```

**3. A member function on an *external* object — 4 ways:**

```cpp
struct A { int a; void incr(int n); };

// ❌ WRONG — passes by value (copies the object!):
A item = {0};
std::thread thr(&A::incr, item, 200);  // operates on a COPY of item!

// ✅ Sol 1 — pass by pointer:
std::thread thr(&A::incr, &item, 200); // → item->incr(200)

// ✅ Sol 2 — pass as shared_ptr:
auto item = std::make_shared<A>();
std::thread thr(&A::incr, item, 200);  // → item->incr(200)

// ✅ Sol 3 — enforce pass by reference:
std::thread thr(&A::incr, std::ref(item), 200); // → item.incr(200)
```

**4. A lambda function:**
```cpp
int main() {
    std::thread thr([&]() {
        for (int i = 0; i < n_times; i++) a = a + 1;
    });
    thr.join();
}
```

### 20.11 Thread Parameters

> **Thread function parameters are ALWAYS passed by value!**  
> Trying to pass by reference just silently passes a copy (or crashes depending on implementation).

**Why:** the thread may outlive the caller's stack frame — a reference to a local variable would dangle.

**If you need to share memory:**

```cpp
// ✅ Explicit reference with std::ref (DANGEROUS — shared memory!):
void incr(int& v) { ++v; }
int v = 1;
std::thread thr(incr, std::ref(v));
thr.join();  // v == 2 here
// WARNING: both main and thr share the same v — race condition possible
```

**If you need to pass efficiently without sharing:**

```cpp
// ✅ Move — passes ownership, no copy, no shared memory:
void print(const std::string& s) { std::cout << "s=" << s << std::endl; }
int main() {
    std::string v = "Hi!";
    std::thread thr(print, std::move(v));
    std::cout << "v=" << v << std::endl; // v is now empty (moved-from)
    thr.join();
}
// Output:
// s=Hi!
// v=
```

**Summary:**

| How | Result | Safe? |
|---|---|---|
| pass by value (default) | copy made for thread | ✅ safe |
| `std::ref(v)` | thread uses same v | ⚠️ race condition risk |
| `std::move(v)` | ownership transferred, caller loses v | ✅ safe (no sharing) |
| `shared_ptr` | shared ownership, reference counted | ✅ safe (with mutex) |

### 20.12 Lambda functions

A **lambda** is a shorthand for an anonymous function object. Use one when the function is simple and only needed locally — there's no point naming it. 

A lambda is an object of type `std::function<Return(Args)>`:
```cpp
const std::function<void(int)>    // void function taking one int
const std::function<int(int,double)>  // int function taking int and double
```

**Full syntax:**
```cpp
[capture](parameters) -> return_type { body }
```

**Capture list** — variables from the enclosing scope passed into the lambda:

| Capture | Meaning |
|---|---|
| `[a]` | `a` by **const copy** (cannot modify) |
| `[&a]` | `a` by **reference** |
| `[=]` | **all** variables by const copy |
| `[&]` | **all** variables by reference |
| `[a, &b]` | `a` by copy, `b` by reference |
| `[this]` | current object by reference |
| `[a]() mutable` | `a` by copy, **modifiable** inside lambda |

**Examples:**

```cpp
// a by reference, takes int x, returns int
[&a](int x) -> int { a = a + x; return a; }

// a by value, mutable (can modify local copy), no params, void return
[a]() mutable { a = a + 1; }  // outer a NOT changed

// all by value
[=]() { /* use copies of all captured vars */ }

// all by reference
[&]() { /* use references to all captured vars */ }
```

**Practical use — passing lambdas to algorithms:**
```cpp
std::vector<int> values = {1, 2, 3};

// using for_each
std::for_each(values.begin(), values.end(), [](int k) {
    std::cout << "k = " << k << std::endl;
});

// passing lambda to custom function
void executeF(const std::function<void(int)>& f) {
    for (int v : values) f(v);
}
executeF([](int k) { std::cout << k << std::endl; });
```

### 20.13 Lambda in Threads

**Key question: what is the value of `a` after joining?**

```cpp
int a = 0;

// Case 1: capture by reference
std::thread thr([&a]() { a = a + 1; });
thr.join();
// a == 1  ✓ (thread modified the real a)

// Case 2: capture by value (const copy)
std::thread thr([a]() { a = a + 1; });  // ERROR: a is const, cannot modify
thr.join();
// Doesn't compile! (need mutable)

// Case 3: capture by value, mutable
std::thread thr([a]() mutable { a = a + 1; });
thr.join();
// a == 0  (thread modified its own copy, outer a unchanged)

// Case 4: pass as thread argument (by value)
std::thread thr([](int v) { v = v + 1; }, a);
thr.join();
// a == 0  (v is a copy of a, outer a unchanged)
```

> **Rule of thumb:** capture by `[&]` to share state (but be careful of race conditions!);  
> capture by `[=]` or pass as argument to avoid sharing.

---

## 21. Inter-thread Communication

### 21.0 5-Minutes Questions

> Typical oral exam questions from this module:
- What is a **race condition**? Give an example.
- What is a **critical section/region**?
- What is **mutual exclusion**?
- What is a **mutex**? How do you use it in C++?
- What is the difference between `lock_guard` and `unique_lock`?
- What is **starvation**? How do you avoid it?
- What is **deadlock**? Give an example.
- What is a **condition variable**? What are `wait`, `notify_one`, `notify_all`?
- What is an **atomic variable**? Why is it faster than a mutex?
- Explain the complete producer-consumer pattern.

### 21.1 Memory Model

Operations on objects **never happen directly in memory**. The CPU:
1. **Loads** the object into a register
2. **Modifies** it in the register
3. **Writes back** to memory

This means that `a = a + 1` is **three separate operations**, not one:

```
T1: R1 = a     // load a into register
T2: R1 = R1+1  // add 1
T3: a = R1     // write back
```

If two threads do this *at the same time*, operations from both threads can interleave:

| Time | `a` | Thread 1 | Thread 2 |
|------|-----|----------|----------|
| T1 | 10 | R1 = 10 (load) | — |
| T2 | 10 | R1 = 11 (add) | R2 = 10 (load) |
| T3 | 11 | a = 11 (write) | R2 = 11 (add) |
| T4 | 11 | — | a = 11 (write) |

Result: `a == 11` instead of `12` — **one increment is lost!**

### 21.2 Race Condition Definition

> **Race condition:** anything where the outcome of a program depends on the *relative ordering of execution* of operations on two or more threads.

```cpp
int a = 0;
void incr() {
    for (int i = 0; i < 100000; i++) {
        a = a + 1;  // NOT atomic! → race condition when run from 2 threads
        std::this_thread::sleep_for(std::chrono::microseconds(1));
    }
}
int main() {
    std::thread thr1(incr);
    std::thread thr2(incr);
    thr1.join();
    thr2.join();
    std::cout << a; // not necessarily 200000!
}
```

### 21.3 Producer-Consumer Problem

```cpp
std::queue<int> q;
std::thread consumer([&]() {
    while(true) {
        if (q.size() > 0) {
            int val = q.front();
            q.pop();
        }
    }
});
// Producer: q.push(17);
```

### 21.4 Critical regions

A sequence of statements that accesses shared resources and must appear to execute indivisibly — no other thread can observe it partway through.

### 21.5 Busy waiting

Repeatedly polling a condition pegs the CPU at 100% and wastes cycles. Only use it for hardware interactions where latency demands it.

### 21.6 Mutex

A **mutex** (mutual exclusion variable) is an object that gives one thread at a time **exclusive access** to a resource.

**Operations:**
- **Lock** (acquire): gain exclusive ownership; may block if another thread holds it
- **Unlock** (release): relinquish ownership; unblocks one waiting thread

**Raw mutex (dangerous — easy to forget unlock):**
```cpp
#include <mutex>
std::mutex m_a;
void useMutex() {
    m_a.lock();
    // critical section
    m_a.unlock();   // if you forget this, STARVATION!
                    // if an exception fires before this, DEADLOCK!
}
```

**RAII wrappers (always prefer these):**

| Type | Feature |
|---|---|
| `std::lock_guard<std::mutex>` | Lighter, locks on construction, unlocks on destruction |
| `std::unique_lock<std::mutex>` | More flexible: can unlock/relock manually, required by `condition_variable` |

```cpp
#include <mutex>
int a = 0;
std::mutex m_a;

void doIncr() {
    std::unique_lock<std::mutex> lk(m_a);  // locks m_a
    a = a + 1;
}   // lk goes out of scope → m_a is unlocked automatically (RAII)

void incr() {
    for (int i = 0; i < 100000; i++) {
        doIncr();
        std::this_thread::sleep_for(std::chrono::microseconds(1));
    }
}
int main() {
    std::thread thr1(incr);
    std::thread thr2(incr);
    thr1.join(); thr2.join();
    std::cout << a << std::endl;  // always 200000 now ✓
}
```

### 21.7 Starvation

> **Starvation:** a thread never gets to run because the scheduler always picks other threads to unblock from the mutex.

**Cause:** The CPU scheduler does not guarantee fairness.

**Solution:** **Acquire the mutex for the minimal amount of time** — only during the critical section. Never hold a mutex while doing long work.

```cpp
// BAD: mutex held for entire loop iteration
while (true) {
    std::unique_lock<std::mutex> lk(m_a);
    // do long stuff
}

// GOOD: mutex held only for the critical section
while (true) {
    {
        std::unique_lock<std::mutex> lk(m_a);
        // access shared data — minimal time
    }   // mutex released here
    // do long stuff outside the lock
}
```

### 21.8 Deadlock

> **Deadlock:** a thread waits for a mutex that is never released (from another thread or from itself).

**Classic deadlock — locking the same mutex twice:**
```cpp
std::mutex m_a;

void useMutex1() {
    std::unique_lock<std::mutex> lk(m_a);  // locks m_a
    // do stuff
}

void useMutex2() {
    std::unique_lock<std::mutex> lk(m_a);  // locks m_a
    // do stuff
    useMutex1();  // tries to lock m_a again → DEADLOCK! (same thread)
}
```

**Classic deadlock — two threads, two mutexes in opposite order:**
```cpp
// Thread 1: locks A then B
// Thread 2: locks B then A
// → each waits for the other to release → forever blocked
```

**Prevention:** always lock multiple mutexes in the **same order** across all threads.

### 21.9 Condition Variable

> A **condition variable** lets a thread *wait* for an event generated by another thread, without busy-spinning.

Must always be used **together with a `unique_lock`** on a mutex.

**Key methods:**

| Method | What it does |
|---|---|
| `cv.wait(lck, pred)` | **Atomically** unlocks `lck` and sleeps until `pred()` is true, then relocks |
| `cv.wait_for(lck, duration, pred)` | Same but with a timeout |
| `cv.notify_one()` | Wakes up **one** thread waiting on cv |
| `cv.notify_all()` | Wakes up **all** threads waiting on cv |

> `pred` must be a **bool function or lambda**. The predicate is *re-checked* every time the thread wakes (guards against spurious wakeups).

### 21.10 Producer-Consumer with Condition Variable

**Consumer thread steps:**
1. Lock the mutex
2. Wait (releases mutex) until: queue is not empty **OR** exit flag is true
3. Mutex is automatically re-locked after wait
4. Consume the resource
5. Mutex released as `unique_lock` goes out of scope

**Producer thread steps:**
1. Lock the mutex
2. Push resource into queue (predicate becomes true)
3. Unlock the mutex
4. Notify one waiting consumer

```cpp
#include <queue>
#include <mutex>
#include <condition_variable>

std::queue<int> q;
std::mutex m_a;
std::condition_variable cv;

// Consumer
std::thread consumer([&]() {
    while (true) {
        std::unique_lock<std::mutex> lk(m_a);  // 1. lock
        cv.wait(lk, [&]() { return !q.empty(); }); // 2. wait (releases lk)
                                                    // 3. re-locks lk after
        int val = q.front();
        q.pop();                                    // 4. consume
    }   // 5. lk out of scope → mutex unlocked
});

// Producer
std::unique_lock<std::mutex> lk(m_a);  // 1. lock
q.push(17);                             // 2. produce
lk.unlock();                            // 3. unlock
cv.notify_one();                        // 4. notify
consumer.join();
```

### 21.11 Atomic Variables

> **Atomic variables** allow thread-safe operations on simple types *without a mutex*.  
> An atomic operation is guaranteed to be performed by a single thread with no interference.

```cpp
#include <atomic>
std::atomic<int>  sn(0);      // initialize (NOT thread-safe, do before threads start)
std::atomic<bool> flag(false);

int x  = sn.load();           // get value atomically (same as: x = sn)
sn.store(5);                   // set value atomically (same as: sn = 5)
int old = sn.exchange(3);      // atomically set to 3, return old value
```

**Performance:** atomic operations are implemented in **hardware** → ~3× faster than lock-based operations for simple counters/flags.

**When to use:**
- Shared **flags** (e.g. `exit_flag`)
- Shared **counters** (e.g. packet count)
- NOT for complex objects or compound operations

### 21.12 Complete Producer-Consumer Solution (Final)

Two problems with the naive solution:
1. **Consumer never exits** (infinite `while(true)`) → use `exit_flag`
2. **`cv.wait` may block forever** if no more data arrives → include `exit_flag` in predicate

```cpp
#include <queue>
#include <mutex>
#include <condition_variable>
#include <atomic>

std::queue<int> q;
std::mutex m_a;
std::condition_variable cv;
std::atomic<bool> exit_flag(false);

// ─── CONSUMER THREAD ───────────────────────────────────────────────────
std::thread tr1([&]() {
    while (!exit_flag.load()) {                    // 1. loop until exit flag
        std::unique_lock<std::mutex> lk1(m_a);    // 2. lock mutex
        cv.wait(lk1, [&]() -> bool {              // 3a. release mutex & sleep
            return !q.empty()                     // 3b. wake when: data ready
                || exit_flag.load();              //     OR exit requested
        });                                        // 4. mutex re-locked
        if (!q.empty()) {
            q.pop();                               // 5. consume data
        }
    }                                              // 6. lk1 out of scope → unlock
});

// ─── PRODUCER (main thread) ────────────────────────────────────────────
{
    std::unique_lock<std::mutex> lk2(m_a);        // 1. lock mutex
    q.push(17);                                    // 2. produce
}                                                  // 3. lk2 out of scope → unlock
cv.notify_one();                                   // 4. notify consumer

// ─── SHUTDOWN ──────────────────────────────────────────────────────────
exit_flag.store(true);    // 5. set exit flag (atomic → no mutex needed)
cv.notify_all();          // 6. wake all waiting threads so they see exit_flag
tr1.join();               // 7. wait for consumer to finish
```

**Why notify after setting exit_flag?** The consumer may be sleeping in `cv.wait()`. Without `notify_all()`, it would sleep forever even though `exit_flag` is now true.

---

## Quick Reference Tables

### Fundamental Types

| Type | Size | Description |
|------|------|-------------|
| `bool` | 1+ byte | true/false |
| `char` | 1 byte | character |
| `int` | 4+ bytes | integer |
| `double` | 8 bytes | floating point |
| `void` | - | no type |

### Smart Pointers

| Type | Ownership | Copyable | Use Case |
|------|-----------|----------|----------|
| `unique_ptr` | Exclusive | No (move only) | Single owner |
| `shared_ptr` | Shared | Yes | Multiple owners |
| `weak_ptr` | None | Yes | Break cycles |

### Container Selection

| Need | Container |
|------|-----------|
| General purpose | `vector` |
| Frequent insert/delete at ends | `deque` |
| Frequent insert/delete in middle | `list` |
| Key-value lookup | `map` / `unordered_map` |
| Unique elements | `set` / `unordered_set` |

### Cast Reference

| Cast | Use |
|------|-----|
| `static_cast` | Related types |
| `dynamic_cast` | Polymorphic downcast |
| `const_cast` | Remove const |
| `reinterpret_cast` | Unrelated types |

### Thread Synchronization Summary

| Tool | Header | Use case |
|---|---|---|
| `std::thread` | `<thread>` | Launch a task on a new thread |
| `std::mutex` | `<mutex>` | Protect a critical section |
| `std::lock_guard` | `<mutex>` | RAII lock — lightweight, auto-unlock on scope exit |
| `std::unique_lock` | `<mutex>` | RAII lock — flexible, required by condition_variable |
| `std::condition_variable` | `<condition_variable>` | Sleep until event from another thread |
| `std::atomic<T>` | `<atomic>` | Lock-free flag/counter for simple types |

### RAII Pattern Summary

```cpp
class Resource {
    T* data;
public:
    Resource()  { data = new T(); }   // acquire
    ~Resource() { delete data; }      // release (automatic, even on exception)
    Resource(const Resource&) = delete;            // prohibit copy
    Resource& operator=(const Resource&) = delete; // prohibit copy
    Resource(Resource&& other) : data(other.data) { other.data = nullptr; } // move
};
```

### Memory Management Cheatsheet

| Situation | Solution |
|---|---|
| Local variable | Stack — no `new`/`delete` needed |
| Single owner, heap | `std::unique_ptr<T>` + `make_unique<T>()` |
| Shared ownership | `std::shared_ptr<T>` + `make_shared<T>()` |
| Break cyclic references | `std::weak_ptr<T>` |
| Must use raw pointer | Put it in a RAII handle class |

### Lambda Capture Quick Reference

| Syntax | Meaning |
|---|---|
| `[x]` | x by const copy |
| `[&x]` | x by reference |
| `[=]` | all by const copy |
| `[&]` | all by reference |
| `[x, &y]` | x by copy, y by reference |
| `[=] mutable` | all by copy, modifiable |
| `[this]` | current object by reference |

---

*This study guide covers all major topics from the Modern C++ Programming for ICT course. For detailed implementation and examples, refer to the course slides and code examples.*
