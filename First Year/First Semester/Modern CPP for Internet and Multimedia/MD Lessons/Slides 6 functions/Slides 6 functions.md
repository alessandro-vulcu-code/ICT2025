<!-- Pagina 1 -->

Functions

Programming for Telecommunications
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

1. Function declarations
2. Returning values
3. Local and static variables
4. Argument passing
5. Overloaded functions
6. Pre and post conditions
7. Pointer to function
8. Macros

[c++pl] Chapter 12

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Functions

• Break the code into simple, meaningful chunks and name them
  1. The code is more comprehensible – this helps maintainability
  2. The code can be reused
  3. It is possible to compose multiple functions to obtain combined results, e.g., f(g())
  4. It helps document dependencies
  5. It saves from error-prone control structures

• There is little or no cost in performance in using functions
  • with some precautions, as we will discuss later in this lesson

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

Functions declarations

A function declaration has multiple parts:

• **name** (required)
• **argument list** (required)
  specify the number and type of arguments. The name for each argument is optional for the declaration, required for the definition.
• **return type** (required)
  it may be void, if the function does not return a value
  it can be specified as a prefix or suffix

```cpp
prefix return type name argument list
int sqrt(int number);
auto sqrt(int number) → int;
postfix return type (with auto in the prefix)
```

This is useful for templates, where the type of return is not known a-priori but depends on the type of the arguments.

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)


---

<!-- Pagina 5 -->

Functions declarations

A function declaration has multiple parts:

• **inline** (optional)
  keyword that suggests to the compiler to generate *new code* for every function call, instead than of a single code in memory that is pointed to by every function call. This enables an optimization in terms of execution speed. The compiler is *not required* to respect the inline keyword

• **constexpr** (optional)
  specifies that the function can be evaluated at compile time simple, no loops, no side effects (e.g., no changes to global variables)

• **noexcept** (optional)
  specifies that a function cannot throw an exception

• **static** (optional)
  for linkage, more on this in following lessons

• other keywords for functions defined in classes (member functions)

---

**Immagini estratte:**

![Figura estratta 1](p05_img01.jpg)


---

<!-- Pagina 6 -->

Returning values

• void to specify that no value is returned
• prefix vs postfix return
• the point and value of the return is specified by a return statement
• There can be more than one return in a function, and the function returns when executing the first of them in the logic flow
• Return with a copy
  • a variable of the returned type is initialized and then returned
  • the memory is reused after the function returns, so never return a pointer or a reference to a local non-static variable

```c
int f(int a) {
  if(a == 0) {
    return 1;
  }
  int b = a * 10;
  return b;
}
```

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)


---

<!-- Pagina 7 -->

Returning values

5 ways to exit a function

1. return
2. “falling off at the end”, i.e., reach the end of the function body (only for void return type)
3. by throwing an exception which is not caught locally
4. terminate after an exception which is not caught locally in a noexcept function
5. invocate a system function that does not return (exit())

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)


---

<!-- Pagina 8 -->

Function definition

• A function that is called **must** be defined once
• The definition presents the body of the function

```c
int f(int a)
{
    if(a == 0) {
        return 1;
    }
    int b = a * 10;
    return b;
}
```

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)


---

<!-- Pagina 9 -->

Local and static variables

• A local variable is a name defined in a function
• Every call to the function performs a new initialization of each local variable
• A static variable is different
  • Only the first call to the function creates the object
  • It enables the sharing of a variable across function calls
  • No need to use global variables
  • This can be dangerous, and static variables in functions should be used with care or avoided

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Argument passing

• The suffix () (call or application operator) contains a list of arguments

• When a function is called, store (i.e., memory) is set aside for “formal arguments” or “parameters” (i.e., those specified in the function declaration)

• Each parameter is then initialized with the actual arguments (i.e., those passed by the function caller)

• The compiler:
  • checks the type
  • performs standard or user-defined type conversions

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Pass by value

• When a variable is passed by value from the caller to the called function, the value of the variable is copied into a new variable, which is independent on the first

• The function `does not` modify the variable that is passed to it, but copies the value into a new one and uses that

```cpp
void increment(int a)
{
    ++a;
    std::cout << a << std::endl; // when called
    // as below, this will print 3
}

int a = 2;
increment(a);
std::cout << a << std::endl; // this prints 2 – the
// variable a outside of the function is not modified
```

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

Pass by reference

• When a variable is passed by reference from the caller to the called function, the value of the variable is *not* copied into a new variable

• The function *does directly modify* the variable that is passed to it (unless it is declared const)

```cpp
void increment(int& a)
{
    ++a;
    std::cout << a << std::endl; // when called
    // as below, this will print 3
}

int a = 2;
increment(a);
std::cout << a << std::endl; // this prints 3 – the
// variable a of the caller has been modified by the
// function
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Pass by reference

• It is not a good practice to modify arguments passed by reference
  • It is better to explicitly return the modified value – this makes the code clearer and easier to maintain

• It can be more efficient to avoid the copy (with pass-by-value) of large objects

use const references
for large objects which do not need to be copied and/or modified in the function itself

void f(const LargeType& a)

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Pass by reference

• Pass by const lvalue reference void f(const LargeType& a)
• Pass by rvalue reference (e.g., to bind to a temporary object) void f(LargeType& a)

```cpp
void f(vector<int>&); // (non-const) lvalue ref argument
void f(const vector<int>&); // const lvalue ref argument
void f(vector<int>&); // rvalue reference argument

void g(vector<int>& vi, const vector<int>& vci)
{
    f(vi); // call f(vector<int>&)
    f(vci); // call f(const vector<int>&)
    f(vector<int>{1,2,3,4}); // call f(vector<int>&);
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Guidelines (from C++PL)

Follow these guidelines in order:

1. Pass-by-value for small objects
2. Pass-by-const-lvalue-reference for large objects, not to be modified
3. Return a results with return instead than by modifying the argument
4. Pass-by-rvalue-reference for move and forward (more on this in future lessons)
5. Pass a pointer if the “no object” case can be dealt with and represent “no object” with a nullptr that is portable
6. Pass-by-lvalue-reference only as last option if for some reason the argument needs to be modified by the function, the usage of a pointer can be clearer and easier to understand

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p15_img01.jpg)


---

<!-- Pagina 16 -->

Array arguments

• C++ arrays are not passed by value but by pointer
• When an array is specified as argument, it always decays into a pointer
  historic reasons inherited from C – in the 1970s, the memory of machines was limited, and it is more efficient to pass a pointer to the array than copying the whole array into a new location

```cpp
// these three declarations are equivalent and
// declare the same function
void f(int* p);
void f(int[] a);
void f(int b[1000]);
```

• The information on the size is lost – and not implicitly available to the function
• This another good reason to avoid using arrays, and preferer std::vector or other standard library containers

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p16_img01.jpg)


---

<!-- Pagina 17 -->

Array arguments

• The information on the size is lost – and not implicitly available to the function

• Workarounds:
  • Explicitly pass the size as argument
    void f(int* p, size_t size_of_the_array);

  • Pass a reference type to the array
    void f(int (&r)[1000]);

  the size is compulsory (part of the type), thus the flexibility of this call is limited

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)


---

<!-- Pagina 18 -->

List arguments

A {}-delimited list can be an actual argument to a parameter of type

1. use std::initializer_list<T>
2. reference to array of type T
3. type that can be initialized with the values in the list

```cpp
template<class T>
void f(initializer_list<T>);

template<class T, int N>
void f2(T (&r)[N]);

void g() {
    f({1,2,3,4}); // T is int + initializer_list has size 4
    f2({1}); // T is int N is 1
}
```

---

**Immagini estratte:**

![Figura estratta 1](p18_img01.jpg)


---

<!-- Pagina 19 -->

List arguments

If there is ambiguity, `std::initializer_list<T>` has the precedence – this may cause errors

```cpp
template<class T>
void f(initializer_list<T>);

template<class T, int N>
void f(T (&r)[N]);

struct S { int a; string s; };
void f(S);

void g() {
    f({1,2,3,4}); // T is int + initializer_list has size 4
    f({1,"MKS"}); // calls f(S), not all the values can be
                // implicitly cast to int
    f({1}); // T is int + initializer_list has size 1
}
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p19_img01.jpg)


---

<!-- Pagina 20 -->

Unspecified number of arguments

There are different ways to deal with an unknown number of arguments

1. Variadic templates (arbitrary number of arbitrary types) (more on this when we will study templates)
2. Use `std::initializer_list<T>` (arbitrary number of the same type)
3. Ellipsis (...) (arbitrary number of arbitrary types)
   - not type-safe (the compiler does not know a-priori which are the types of the possible arguments)
   - some user-defined types may not work
   - this may cause errors: use it only if 1 and 2 are not an option

1 and 2 are type safe

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p20_img01.jpg)


---

<!-- Pagina 21 -->

Default arguments

• Sometimes it is useful to have default values for some arguments
• They can be provided for trailing arguments only

```cpp
int f(int a, int b=0, char* c=nullptr); // OK
int g(int =0, int =0, char*); // error
int h(int =0, int, char* =nullptr); // error
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p21_img01.jpg)


---

<!-- Pagina 22 -->

Overloaded functions

• Different functions usually have different names
• It could be convenient to name in the same way different functions that perform the same task on different types

Overloading
(already used for operators, e.g., +)

```cpp
void print(int); // print an int
void print(const char*); // print a C-style string

// using different names leads to more complex code
// and more difficult to maintain
void print_int(int);
void print_char(const char*);
```

---

**Immagini estratte:**

![Figura estratta 1](p22_img01.jpg)


---

<!-- Pagina 23 -->

Automatic overload resolution

• The compiler compares the types of actual and formal arguments – it uses the function that provides the best match, with rules in the following order:
  1. Exact match (no or trivial conversions – array to pointer or viceversa, T to const T)
  2. Match using promotions (to integral types with larger ranges, to floating-point values with higher precision)
  3. Match using standard conversions (int – double, etc)
  4. Match using user-defined conversions
  5. Match using ellipsis
• If two different matches are identified at the highest level of a match, the compiler gives an error
• The return type is not considered for resolution
• Functions in different scopes are not overloaded, i.e., the compiler exactly know which one should be used without the need to resolve

---

**Immagini estratte:**

![Figura estratta 1](p23_img01.jpg)


---

<!-- Pagina 24 -->

Pre and post conditions

• Sometimes there are expectations on the arguments and return (e.g., they are in a certain interval, etc)
• The compiler only checks the type
• Logical criteria that
  • hold for arguments are “pre-conditions”
  • hold for return are “post-conditions”
• It is not always possible to enforce them – there is a trade-off between checking and performance
• Sometimes there are no meaningful checks (especially on a return type)

---

**Immagini estratte:**

![Figura estratta 1](images/p24_img01.jpg)


---

<!-- Pagina 25 -->

Pre and post conditions – good practices

• Write good documentation of your functions by specifying the pre and post conditions AND/OR

• Write code that deals with pre/post conditions, different options
  1. Make sure that every input has a valid result (no preconditions)
  2. Assume that the preconditions hold (rely on the caller, and trade possible crashes for performance)
  3. Check and throw an exception if preconditions are not met
  4. Check and terminate if preconditions are not met

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)


---

<!-- Pagina 26 -->

Pointer to function

• The code for a function is stored in memory
• It is possible to get its address in a pointer
  • It can be used `only` to call the function

```cpp
void error(int s); {
    // implementation
}

void (*efct)(int); // pointer to function that takes
// int as argument and does not return anything

void f() {
    efct = error; // same as efct = &error
    efct(10); // same as (*efct)(10), dereferencing
    // is optional
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)


---

<!-- Pagina 27 -->

Pointer to function

• It is possible to cast to pointer types to other functions, but this must be avoided (bad practice that can lead to errors, more in the code example for this class)

• They are used to parametrize C-style code
  using CFT = int(*)(const* void, const* void);

// function that sorts elements independently on the
// type of base, using cmp for comparisons
ssort(void* base, int size, CFT cmp);
// cmp is a pointer to a specific implementation
// of a function that compares objects of the actual
// type of base

int cmp1(const void* p, const void* q) // Compare int
{
  return *(static_cast<int*>(p)) - *(static_cast<int*>(q));
}

---

**Immagini estratte:**

![Figura estratta 1](images/p27_img01.jpg)


---

<!-- Pagina 28 -->

Pointer to function

• They are used to parametrize C-style code
  using CFT = int(*)(const* void, const* void);

// function that sorts elements independently on the
// type of base, using cmp for comparisons
ssort(void* base, int size, CFT cmp);

// This is not recommended in modern C++, use
  std::vector<int> v {1,3,2,4};
  std::sort(
    v.begin(), v.end(),
    [](const int n1, const int n2) {return n1 < n2;}
  );

lambda function

---

**Immagini estratte:**

![Figura estratta 1](images/p28_img01.jpg)


---

<!-- Pagina 29 -->

Macros

• Inherited from C
• Few meaningful uses in C++
  #define MAX_HEIGHT 720
  void f(int a) {
    int b = a + MAX_HEIGHT;
  }

for this scenario, use a constexpr or a const

• a `dumb` preprocessor will simply replace MAX_HEIGHT with what is defined in the macro (720)
• if you want to use MAX_HEIGHT as a name for a member variable (don’t do it), the preprocessor will replace it with 720 and the code will not compile

• They can be used for conditional compilation

---

**Immagini estratte:**

![Figura estratta 1](images/p29_img01.jpg)


---

<!-- Pagina 30 -->

Conditional compilation

• They can be used for conditional compilation

```c
int a = 10;
#ifdef IDENTIFIER
//some code
#endif //IDENTIFIER (good practice to comment)
a -= 2;
```

Unless IDENTIFIER is identified somewhere in the code before this with #define IDENTIFIER, the code between #ifdef and #endif would not be compiled

---

**Immagini estratte:**

![Figura estratta 1](images/p30_img01.jpg)


---

<!-- Pagina 31 -->

Include guards

• An header file (.h) with some declarations and definitions may be included in multiple files
  e.g., #include <iostream> is included in every file that wants to use std::cout

• There can be errors if the compiler tries to compile the header multiple times (every time it sees an #include)

```c
#ifndef STRUCTS_ENUM_TEST
#define STRUCTS_ENUM_TEST

// code of the header

#endif /* STRUCTS_ENUM_TEST */
```

the first time the header is compiled, STRUCTS_ENUM_TEST is not defined, and this is true

STRUCTS_ENUM_TEST is thus defined

the next times, STRUCTS_ENUM_TEST is defined, and this is false, so the file is not considered for compilation

---

**Immagini estratte:**

![Figura estratta 1](images/p31_img01.jpg)
