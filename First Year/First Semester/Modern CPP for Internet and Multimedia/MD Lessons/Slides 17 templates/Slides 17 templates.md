<!-- Pagina 1 -->

Templates

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

1. Templates
2. Example of template
3. Class templates
4. Member templates
5. Function templates
6. Variadic templates

[c++pl] Chapter 23, (28.6)

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Templates

Templates provide the support for generic programming

• represent general concepts that may be applicable to different types (e.g., a vector can hold integers, strings, etc)

• the type is a parameter for the template – and templates are type-safe as everything is checked at compile time

• widely used in the standard library

compile-time polymorphism (vs the run-time polymorphism achieved with base classes)

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

Templates - example

```cpp
template<typename C>
class MyString {
public:
    String();
    explicit String(const C*) { // impl }
    String(const String&) { // impl }
    String operator=(const String&) { // impl }
    // ...
    C& operator[](int n) {
        return ptr[n];
    }
    String& operator+=(C c) { // impl }
    // ...
private:
    static const int short_max = 15;
    int sz;
    C* ptr; // ptr points to sz Cs
};
```

this declares the template
C is then used inside the template
declaration as if it was any other
type name

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)


---

<!-- Pagina 5 -->

Templates - example

```java
template<typename C>
class MyString {
public:
...
```

template<typename C> is equivalent to the mathematical formulation “for all C” ($\forall C$)

• in C++11 there however no implicit way to specify the conditions that a template type has to specify (i.e., “such that...”)

• this has been introduced in C++20
  • “concepts” – characteristics that a template should have
```

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)


---

<!-- Pagina 6 -->

Templates

In C++ it is possible to have
• class templates
• function templates

Once the type has been specified at compile time, a class (function) template is exactly the same as a normal class
• no run-time overhead

MyString<char> or MyString<wchar_t> are a class and they can be used as any other class

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)


---

<!-- Pagina 7 -->

Template implementation guidelines

1. Start from a particular case
   • for example, create MyString implementation without the template that has a char as type

2. Debug it and make sure it works

3. Extend the implementation to a generic template case
   • for example, modify the MyString implementation that has the template structure and a generic type C

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)


---

<!-- Pagina 8 -->

Class templates

• Declared in the same way as MyString
• All the members **must** be defined and declared
• Put the definition in the header file, otherwise linker error

```java
// my-string.h
template<typename C>
class MyString {
public:
    MyString() { // do something }
    ...

• It is not possible to overload the name of a class template
    template<typename C> class MyString { ... };
    class MyString { ... }; // compilation error
```

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)


---

<!-- Pagina 9 -->

Template instantiation

• The instantiation is the process of generating a class from the template + the type arguments
• This class is a “specialization” of the template

During instantiation
• the compiler generates only the members that are actually used
• type checking is applied to this step
  • but checking of the requirements of the type for the template is not performed

Type equivalence:
• Templates with aliases as arguments are the same type

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Class template members

Same type of members and rules as for ordinary classes

• data members
• member functions
• type aliases
• member types and templates
• friends (need to add <> after the name of the function)

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Type aliases

Particularly useful for templates

• the type T is available only to the template
• with an alias, it is possible to refer to it outside the template as well
• the same alias can be used for different templates, to write generic algorithms (“associated types”)
• example: `iterator or value_type`

```cpp
template<typename T>
class Vector {
public:
    using value_type = T;
    using iterator = Vector_iter<T>;  // Vector_iter
    // is another class
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

# Member templates

Members can be templates as well

```cpp
template<typename S>
class complex {

S re, im;

public:
    complex() :re{}, im{} {}

    complex(S rr, S ii =0) : re{rr}, im{ii} { }

    complex(const complex&) = default;

    template<typename T>
    complex(const complex<T>& c) :
        re{c.real()}, im{c.imag()} { }

// ... };
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Member templates

```cpp
template<typename S>
class complex {

S re, im;

public:
    template<typename T>
    complex(const complex<T>& c) :
        re{c.real()}, im{c.imag()} { }

// ... };

```

• by using a different type for the data members and the arguments of the constructor, it is possible to have well-defined conversions between inner types

```cpp
complex<float> cf1 {};
complex<double> cd1 {cf1}; // ok – float to double
complex<float> cf2 {cd1}; // error – narrowing
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Member templates

• Member templates cannot be virtual
• Template constructors are not used to generate default copy/move constructors
  • if a template copy/move constructor is needed, you need to define it

default copy – automatically generated by the compiler if needed

```cpp
complex(const complex&) = default;

template<typename T>
complex(const complex<T>& c) :
  re{c.real()}, im{c.imag()} { }
```

template copy – not automatically generated by the compiler

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Function templates

• The need for a function template arises when class templates are used
  • for example, a vector can hold any type to be sorted
    template<typename T> void sort(std::vector<T>&);

• The template type argument is deduced from the function arguments
• Function templates are fundamental for generic programming
• Function templates can be overloaded
  • Same name, different arguments
  • The compiler will select the specialization that is the best fit for the set of arguments

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p15_img01.jpg)


---

<!-- Pagina 16 -->

Function templates: example

```cpp
template<typename T1, typename T2>
std::pair<T1,T2> make_pair(T1 a, T2 b)
{
    return {a,b};
}

// .....
auto x = make_pair(1,2);
// x is a std::pair<int,int>

auto y = make_pair(string("New York"),7.7);
// y is a std::pair<string,double>
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p16_img01.jpg)


---

<!-- Pagina 17 -->

Function templates: example

• If the parameters cannot be deduced automatically, it is necessary to specify them with the `<>` notation
• For example, “factory” functions used to create other objects (and have no arguments related to the type)

```cpp
template<typename T>
T* create();

void f()
{
    int* p = create<int>();
    int* q = create(); //ERROR
}
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)


---

<!-- Pagina 18 -->

Function templates: lvalue and rvalue

• It is possible to distinguish lvalues and rvalues as arguments even with function templates

```cpp
template<typename T>
class Xref {
public:
    Xref(int i, T* p); // pointer
    Xref(int i, T& lvref); // lvalue ref
    Xref(int i, T&& rvref); // rvalue ref

private:
    T* elem;
}
```

---

**Immagini estratte:**

![Figura estratta 1](p18_img01.jpg)


---

<!-- Pagina 19 -->

Variadic templates

• C++ type-safe mechanism to provide an arbitrary number of parameters with arbitrary types

```cpp
template<typename T, typename ... Args>
void f(T value, Args ... args)
{
    // do something
    // with value
    f(args ... );
}
```

parameter pack: sequence of type and value pairs from which the first is automatically removed at every recursive call

at the second call, the first entry is removed from args ... and passed as T value
• need to account for the case with an empty args

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p19_img01.jpg)
