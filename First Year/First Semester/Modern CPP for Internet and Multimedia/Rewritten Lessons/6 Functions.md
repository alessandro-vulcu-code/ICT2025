# Functions

## Outline
- [[#Why Functions Matter|Why Functions Matter]]
- [[#Function Declarations|Function Declarations]]
  - [[#Required Parts|Required Parts]]
  - [[#Optional Specifiers|Optional Specifiers]]
- [[#Returning Values|Returning Values]]
  - [[#Return Statements|Return Statements]]
  - [[#Ways to Exit a Function|Ways to Exit a Function]]
  - [[#Function Definitions|Function Definitions]]
- [[#Local and Static Variables|Local and Static Variables]]
- [[#Argument Passing|Argument Passing]]
  - [[#Pass by Value|Pass by Value]]
  - [[#Pass by Reference|Pass by Reference]]
  - [[#Argument Passing Guidelines|Argument Passing Guidelines]]
  - [[#Array Arguments|Array Arguments]]
  - [[#List Arguments|List Arguments]]
  - [[#Unspecified Number of Arguments|Unspecified Number of Arguments]]
  - [[#Default Arguments|Default Arguments]]
- [[#Overloaded Functions|Overloaded Functions]]
  - [[#Automatic Overload Resolution|Automatic Overload Resolution]]
- [[#Pre and Post Conditions|Pre and Post Conditions]]
- [[#Pointer to Function|Pointer to Function]]
- [[#Macros|Macros]]
  - [[#Conditional Compilation|Conditional Compilation]]
  - [[#Include Guards|Include Guards]]

## Related Notes

- [[First Year/First Semester/Modern CPP for Internet and Multimedia/Rewritten Lessons/1. Types And Declarations#Declarations and Definitions|Declarations and definitions]]: provides the naming and type vocabulary used by function interfaces.
- [[2. Pointers, Arrays And References#References|References]]: explains the aliasing semantics behind pass-by-reference and output parameters.
- [[8. Compiler#Preprocessor|Preprocessor]]: covers macros, conditional compilation, and include guards from the build perspective.
- [[14. Operator Overloading#Overloading Rules|Overloading rules]]: extends function overloading ideas to operator functions.
- [[17. Templates#Function Templates|Function templates]]: generalizes functions over types while preserving static type checking.
- [[24. Threads And Lambdas#Thread Tasks and Arguments|Thread tasks and arguments]]: uses free functions, member functions, and parameters as thread entry points.

## Study Notes

This lesson follows **[c++pl] Chapter 12** and explains how C++ functions are declared, defined, called, overloaded, and used as abstraction boundaries.

### Why Functions Matter

Functions break code into simple, meaningful chunks and give those chunks names. This improves readability and maintainability, enables reuse, allows composition such as `f(g())`, documents dependencies, and avoids error-prone control structures.

There is little or no performance cost when using functions carefully. Later topics such as `inline`, `constexpr`, and compiler optimization explain why small functions can often be used without sacrificing speed.

### Function Declarations

#### Required Parts

A function declaration has three required parts:

- **name**;
- **argument list**, specifying number and type of arguments;
- **return type**, which may be `void`.

Argument names are optional in a declaration but required in the definition if the argument is used.

```cpp
prefix return type name argument list
int sqrt(int number);
auto sqrt(int number) -> int;
postfix return type (with auto in the prefix)
```

The first and last lines are slide annotations, not valid C++. The valid declarations are `int sqrt(int number);` and `auto sqrt(int number) -> int;`. The suffix return type form is useful in templates, where the return type may depend on argument types.

#### Optional Specifiers

A declaration can include optional function specifiers:

- **`inline`** suggests that the compiler may generate code at each call site instead of using one shared function body. The compiler is not required to follow this suggestion.
- **`constexpr`** says the function can be evaluated at compile time when given constant-expression inputs. The source describes this as suitable for simple functions with no side effects.
- **`noexcept`** states that the function cannot throw exceptions.
- **`static`** affects linkage; this is discussed in later lessons.
- Additional keywords exist for member functions defined inside classes.

### Returning Values

#### Return Statements

`void` specifies that no value is returned. For non-`void` functions, a `return` statement specifies the returned value and the point where the function exits. A function may have more than one `return`; execution stops at the first one reached by the control flow.

```cpp
int f(int a) {
  if(a == 0) {
    return 1;
  }
  int b = a * 10;
  return b;
}
```

If `a == 0`, the function returns `1`. Otherwise it computes `b` and returns it. Returning by value initializes an object of the return type. Never return a pointer or reference to a local non-static variable, because that object is destroyed when the function returns.

#### Ways to Exit a Function

The source lists five ways to exit a function:

1. Execute a `return`.
2. Fall off the end of the function body, allowed only for `void` functions.
3. Throw an exception that is not caught locally.
4. Terminate after an exception is not caught locally in a `noexcept` function.
5. Invoke a system function that does not return, such as `exit()`.

#### Function Definitions

A function that is called must be defined exactly once in the program. The definition contains the function body.

```cpp
int f(int a)
{
    if(a == 0) {
        return 1;
    }
    int b = a * 10;
    return b;
}
```

This definition matches the earlier example and provides the executable body for `f`.

### Local and Static Variables

A **local variable** is defined inside a function. Each function call creates and initializes a fresh local variable.

A **static local variable** is different: it is created only the first time control reaches its declaration and is shared across later calls. This can avoid global variables, but it also introduces shared state, so static locals should be used carefully or avoided when they make behavior harder to reason about.

### Argument Passing

The call operator `()` contains the actual arguments passed by the caller. When a function is called, storage is set aside for the **formal arguments** or **parameters** declared by the function. Each parameter is initialized from the corresponding actual argument.

The compiler checks argument types and performs standard or user-defined conversions when allowed.

#### Pass by Value

With **pass by value**, the argument is copied into a new parameter object. The function works on the copy, so the caller's object is not modified.

```cpp
void increment(int a)
{
    ++a;
    std::cout << a << std::endl; // when called
    // as below, this will print 3
}

int a = 2;
increment(a);
std::cout << a << std::endl; // this prints 2 - the
// variable a outside of the function is not modified
```

The function prints `3` internally, but the caller's `a` remains `2`. Pass by value is usually appropriate for small objects.

#### Pass by Reference

With **pass by reference**, the argument is not copied. The parameter becomes an alias for the caller's object, so the function can modify that object unless the reference is `const`.

```cpp
void increment(int& a)
{
    ++a;
    std::cout << a << std::endl; // when called
    // as below, this will print 3
}

int a = 2;
increment(a);
std::cout << a << std::endl; // this prints 3 - the
// variable a of the caller has been modified by the
// function
```

Here the caller's `a` is incremented. The source warns that modifying reference arguments is often unclear; returning the modified value usually makes code easier to understand.

For large objects that should not be copied or modified, use a **const lvalue reference**:

```cpp
void f(const LargeType& a);
```

This avoids copying while preventing modification through `a`.

The source then lists reference forms:

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

The third declaration is likely corrupted: an rvalue reference parameter should be written `vector<int>&&`, not `vector<int>&`. As written, the first and third declarations are identical and cannot represent separate overloads. The intended lesson is that lvalue references bind to lvalues, const lvalue references can bind to const objects and temporaries, and rvalue references bind to temporaries for move/forwarding scenarios.

#### Argument Passing Guidelines

The C++PL guidelines from the slide are:

1. Pass by value for small objects.
2. Pass by const lvalue reference for large objects that should not be modified.
3. Return results with `return` instead of modifying an argument.
4. Pass by rvalue reference for move and forwarding.
5. Pass a pointer if the "no object" case is valid, and represent "no object" with portable `nullptr`.
6. Pass by non-const lvalue reference only as a last option when the function must modify the argument; sometimes a pointer makes that mutation clearer.

#### Array Arguments

C++ arrays are not passed by value. When an array is used as a function argument, it **decays** to a pointer. This behavior comes from C and avoids copying the entire array.

```cpp
// these three declarations are equivalent and
// declare the same function
void f(int* p);
void f(int[] a);
void f(int b[1000]);
```

All three declarations describe the same parameter type: `int*`. The size information is lost and is not implicitly available to the function. This is a strong reason to prefer `std::vector` or other standard-library containers.

Workarounds include passing the size explicitly:

```cpp
void f(int* p, size_t size_of_the_array);
```

or passing a reference to an array with size as part of the type:

```cpp
void f(int (&r)[1000]);
```

The array-reference form preserves size information, but it is inflexible because the size is fixed in the parameter type.

#### List Arguments

A brace-delimited list can be passed to:

1. a parameter of type `std::initializer_list<T>`;
2. a reference to an array of type `T`;
3. a type that can be initialized with the listed values.

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

`f({1,2,3,4})` uses `std::initializer_list<int>`. `f2({1})` binds the list to an array reference with `T = int` and `N = 1`.

If overload resolution is ambiguous, `std::initializer_list<T>` has precedence, which can cause surprising calls.

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

`{1,"MKS"}` cannot form an `initializer_list<int>`, so the overload taking `S` is selected.

#### Unspecified Number of Arguments

There are several ways to accept an unknown number of arguments:

1. **Variadic templates**, for arbitrary numbers of arbitrary types.
2. **`std::initializer_list<T>`**, for arbitrary numbers of values of the same type.
3. **Ellipsis `...`**, for arbitrary numbers of arbitrary types.

Variadic templates and initializer lists are type-safe. Ellipsis is not type-safe because the compiler does not know the possible argument types in advance; some user-defined types may not work. Use ellipsis only when the safer options are not possible.

#### Default Arguments

Default values can be supplied only for trailing arguments.

```cpp
int f(int a, int b=0, char* c=nullptr); // OK
int g(int =0, int =0, char*); // error
int h(int =0, int, char* =nullptr); // error
```

`f` is valid because once defaults start, all following parameters also have defaults. `g` and `h` are invalid because a parameter without a default follows parameters with defaults.

### Overloaded Functions

Different functions usually have different names, but it is useful to give the same name to functions that perform the same conceptual task on different types. This is **overloading**.

```cpp
void print(int); // print an int
void print(const char*); // print a C-style string

// using different names leads to more complex code
// and more difficult to maintain
void print_int(int);
void print_char(const char*);
```

The overloaded `print` functions are easier to use and maintain than separate type-specific names such as `print_int` and `print_char`, provided the overload set remains clear.

#### Automatic Overload Resolution

The compiler compares actual argument types with formal parameter types and chooses the best match. The source lists this order:

1. Exact match, including trivial conversions such as array-to-pointer and `T` to `const T`.
2. Promotions, such as smaller integer types to larger integer types or lower-precision floating types to higher-precision ones.
3. Standard conversions, such as `int` to `double`.
4. User-defined conversions.
5. Ellipsis.

If two different functions are tied at the highest match level, compilation fails. The **return type is not considered** for overload resolution. Functions in different scopes are not overloaded with each other because ordinary name lookup first determines which scope's function set is visible.

### Pre and Post Conditions

Functions often have logical expectations that the compiler cannot check. Conditions that must hold for arguments are **preconditions**. Conditions that must hold for the returned result are **postconditions**.

The compiler checks types, but it does not generally check semantic rules such as "this value must be positive" or "this index must be in range". There is a trade-off between checking and performance, and in some cases there is no meaningful runtime check.

Good practice is to document preconditions and postconditions, and optionally enforce them. The source lists four strategies:

1. Make sure every input has a valid result, so there are no preconditions.
2. Assume preconditions hold, relying on the caller and trading safety checks for performance.
3. Check preconditions and throw an exception when they fail.
4. Check preconditions and terminate when they fail.

### Pointer to Function

Function code is stored in memory, and its address can be stored in a **function pointer**. A function pointer can be used only to call the function.

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

The first line is malformed: a declaration would be `void error(int s);`, while a definition would be `void error(int s) { ... }`. `efct` is a pointer to a function taking `int` and returning `void`. Assigning `error` stores the function address, and `efct(10)` calls it.

Casting between incompatible function pointer types should be avoided because it can lead to errors.

Function pointers are often used to parametrize C-style code.

```cpp
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
```

The type alias is corrupted in the source: it should be `const void*`, not `const* void`. The idea is that `CFT` names a comparison-function pointer type. The comparator receives untyped pointers and casts them back to the expected type.

Modern C++ usually prefers standard algorithms and callable objects.

```cpp
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
```

The lambda function `[](const int n1, const int n2) { return n1 < n2; }` is passed directly to `std::sort`. This is type-safe and clearer than a C-style `void*` comparator.

### Macros

Macros are inherited from C and have few meaningful uses in modern C++.

```cpp
#define MAX_HEIGHT 720
void f(int a) {
  int b = a + MAX_HEIGHT;
}
```

For this scenario, prefer `constexpr` or `const`. A macro is handled by the preprocessor as a simple textual replacement. If `MAX_HEIGHT` is used later as a member variable name, the preprocessor still replaces it with `720`, which can make the code fail to compile.

Macros are still useful for **conditional compilation**.

#### Conditional Compilation

```cpp
int a = 10;
#ifdef IDENTIFIER
//some code
#endif //IDENTIFIER (good practice to comment)
a -= 2;
```

Unless `IDENTIFIER` has been defined earlier with `#define IDENTIFIER`, the code between `#ifdef` and `#endif` is not compiled. Commenting the closing `#endif` is good practice in larger files.

#### Include Guards

A header file may be included by many source files. Without protection, the compiler may process the same declarations multiple times.

```cpp
#ifndef STRUCTS_ENUM_TEST
#define STRUCTS_ENUM_TEST

// code of the header

#endif /* STRUCTS_ENUM_TEST */
```

The first time the header is processed, `STRUCTS_ENUM_TEST` is not defined, so the body is included and the macro is defined. On later inclusions, the macro is already defined, so the body is skipped. This pattern is an **include guard**.

## 5 Mins Questions

No 5 mins questions are present in the source material.

## Final Summary

Functions are the basic unit for naming behavior and building reusable program structure. A function declaration specifies the interface: name, parameters, return type, and optional specifiers such as `inline`, `constexpr`, and `noexcept`. A definition supplies the body, and a called function must be defined once.

Argument passing determines ownership and mutation behavior: pass small values by value, large read-only objects by const reference, and use pointers or rvalue references only when their semantics are needed. Overload resolution chooses among functions by argument types, not return type. Preconditions, postconditions, function pointers, and macros are all tools for specific cases, but modern C++ generally favors type-safe interfaces, standard algorithms, lambdas, and constants over low-level C-style mechanisms.
