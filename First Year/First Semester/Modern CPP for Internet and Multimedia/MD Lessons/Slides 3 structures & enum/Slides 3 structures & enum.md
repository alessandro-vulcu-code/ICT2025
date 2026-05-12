<!-- Pagina 1 -->

Structures and Enumerators

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

1. Structures
2. Enumerator class
3. Plain enumerators

[c++pl] Chapter 8

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Primitive user-defined data types

• Primitive user-defined types, used in C-style programming and with improvements in C++
  1. `struct` (structure, from C programming language): sequence of elements of arbitrary types
  2. `enum`: type with a set of named constants, which can be implicitly cast to an integer
  3. `enum class`: scoped enum without implicit conversion to an integer

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

# struct

• array: aggregate of elements of the same type
• struct: aggregate of elements with different types

## declaration and definition

```c
struct Address {
    const char* name;
    int number;
    const char* street;
    const char* town;
    char state[2];
    const char* zip;
};
```

## initialization

```c
Address jd = {
    "Jim Dandy",
    61,
    "South St",
    "New Providence",
    {'N','J'},
    "07974"
};
```

• two structs are different types even when they have the same members

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)


---

<!-- Pagina 5 -->

# struct

• access to individual members can be done in different ways

```cpp
Address jd;
jd.name = "Jim Dandy";

void f(Address &addr)
{
    addr.name = "Jim Dandy";
}

void f(Address *addr)
{
    addr->name = "Jim Dandy";
    // or
    (*addr).name = "Jim Dandy";
}
```

• by default, members are public

---

**Immagini estratte:**

![Figura estratta 1](p05_img01.jpg)


---

<!-- Pagina 6 -->

struct layout

• members are saved in memory in the order they are declared

```c
struct Example {
    char first_member;
    int second_member;
    char third_member
};
```

The size is `at least 6 (1+4+1)`, because some architectures some types must be aligned to certain boundaries

```c
1
2
3
12
```

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)


---

<!-- Pagina 7 -->

# struct declarations

• the type of the struct is immediately available
  ```c
  struct Example {
    Example* pointer_to_other; // correct: the size
  }; // of a pointer is fixed and defined
```

• but new objects of this type can be declared only after a complete definition
  ```c
  struct Example {
    Example other; // error: the size of example is
  }; // unknown
```

• it is possible to declare the name and define it later (forward declaration)
• struct names (which are types) can be overloaded by variables: `this must be avoided`

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)


---

<!-- Pagina 8 -->

# struct constructors

• a struct is a simple version of a class: it can have constructors

```c
struct Points {
    std::vector<int> elem;
    Points (int n1, int n2) {
        elem.push_back(n1);
        elem.push_back(n2);
    }
};
```

• if a constructor is explicitly declared, then there is no default constructor

• Enforce invariants (conditions that must be always true in the lifetime of an object)

• Reorder/validate/modify arguments

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)


---

<!-- Pagina 9 -->

Plain Old Data (POD)

• Simple types that can be copied or move around in memory without risks (e.g., with std::memcpy())
because they are contiguous in memory. A POD must have
  • No complex layout
  • No user-defined copy
  • Trivial default constructor (non user-provided)

```c
struct Trivial { // just a wrapper, actually useless
  int a;
  Trivial(int aa) : a(aa) { }
  Trivial() = default; // use the compiler generated
  // constructor
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Fields in structures

• A bool is at least large as a char
• If a section of the code uses multiple flags, they can be packed together as fields (or bitfields) of a struct
• Notice that this may not lead to optimizations (e.g., larger compiled code but smaller memory space)
• Useful to conform to an external layout (e.g., a packet header)
• The syntax is type variable : number_of_bit
• The address of a bitfield cannot be taken, because it may not begin at the beginning of a byte

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Fields in structures: TCP header

```c
struct SimpleTcpHeader {
    int source_port : 16;
    int destination_port : 16;
    int sequence_number : 32;
    int ack_number : 32;
    char data_offset : 4; // 4 bit
    char : 3; // these are not used
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

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

enum class

enumerators

• Enumerators hold a set of integers named by the user
• In an enum class, the enumerators are
  • scoped – they do not exist out of the enum class and the same enumerator can be used in other enum classes without clashes
  • strongly typed – they do not convert implicitly to int

enum class TrafficLight {green, yellow, red};
TrafficLight a = TrafficLight::red;
int a2 = a; // compilation error
bool a3 {a = 2}; // compilation error

enum class Other {char {green, blue}; // no name clash!

int by default, but it can be changed

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Operators on enum class

• Enumerators are useful to provide a human-understandable semantic
• It is possible to specify the values – for example to make them work with bitfield operations!

```cpp
enum class Printer_flags { acknowledge=1, paper_empty=2,
    busy=4, out_of_black=8, out_of_color=16};
```

• Operators can then be (re)defined to work with enumerators

```cpp
constexpr Printer_flags operator|(
    Printer_flags a, Printer_flags b) {
    return static_cast<Printer_flags>(
        static_cast<int>(a)|static_cast<int>(b));
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Plain enum

• The enumerators of a plain enum are not scoped and can be converted to int
• In general, prefer enum classes, which provide a better defined behavior

```cpp
enum TrafficLight {green, yellow, red};
TrafficLight a = TrafficLight::red;
int a2 = a; // ok!
bool a3 {a == 2}; // ok!

enum Other char {green, blue}; // error
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)
