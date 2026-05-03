<!-- Pagina 1 -->

Namespaces and code modularization

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

1. Modularity
2. Namespaces
3. Access to namespaces
4. Interfaces

[c++pl] Chapter 14

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Composition problem

• Any realistic program is composed by multiple, separate parts – think of functions, classes, etc
• A good implementation should be based on modularity

keep separate things/concepts /abstractions separate

allow the access only through a well-specified interface

There is not a specific language feature to support modularity, but it can be achieved through namespaces, classes and functions.

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

Need for modularity

• Consider two libraries

```cpp
// a library for shapes
class Shape { /* ... */ };
class Line : public Shape { /* ... */ };
class Poly_line: public Shape { /* ... */ };
class Text : public Shape { /* ... */ };

// a library for text
class Glyph { /* ... */ };
class Word { /* ... */ };
class Line { /* ... */ };
class Text { /* ... */ };
```

• If a program uses both of them, it will not compile, because Line and Text have multiple declarations

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img01.jpg)


---

<!-- Pagina 5 -->

Namespace

• It represents a set of facilities that directly belongs together (e.g., the code of a library) because of
  • logical relationships
  • the functionality these facilities provide

• Members of a namespace are all in scope

• Namespaces are open, i.e., it is possible to add members to a namespace from multiple locations
  • E.g., consider multiple classes in a namespace, defined in multiple files

```javascript
namespace TextLibrary {
  // a library for text
  class Line { /* ... */ };
  class Text { /* ... */ };
}; // end of namespace TextLibrary
```

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)


---

<!-- Pagina 6 -->

Access to namespace members

• Explicit qualification

```cpp
TextLibrary::Line line_object {};

// ::GlobalMemberName can be used to access
// members from the global namespace, which
// are otherwise shadowed by local variables

• using declarations

using std::string;

string a_string {"hello"};
// instead of std::string a_string
```

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)


---

<!-- Pagina 7 -->

Access to namespace members

• using directives

using namespace std;

string a_string {"hello"};
vector<string> vec {a_string}
// instead of std::string a_string
// and std::vector<std::string> vec

Use them with care

• They may lead to the same name clashes that namespaces were introduced to avoid

• Don’t place them in the global scope of an header file (which could be #included anywhere)

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)


---

<!-- Pagina 8 -->

Access to namespace members

• with the argument-dependent lookup
  • search for a function in the namespace of its arguments
  • it is particularly useful for operators

• the rules to find a function with the matching signature are as follows:
  • if the argument is a class member, first check the class, then the namespace
  • if the argument is a namespace member, first check the namespace, then the (eventual) enclosing ones, up to the global
  • if the argument is built-in (int, char, bool, etc), there are no associated namespaces

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)


---

<!-- Pagina 9 -->

Modularization and interfaces

• A program is a combination of separate parts
• Each par needs access to the functionalities provided by another part
• This can be done by defining interfaces
  • They should be the only way to access the functionalities of a part of code (a “module”)
  • The implementation details should be hidden
  • Data-hiding principle of the data abstraction programming paradigm
• Interfaces can be defined with
  • Namespaces (which could define libraries and modules)
  • Classes and object-oriented programming

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Example of modular codebase

TCP module

interacts with the
which hides the
Congestion control implementation
Retransmissions interface
Retransmissions implementation
Header parsing implementation

In this way, the TCP program can use – for example – different congestion control algorithms without changing the code

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)
