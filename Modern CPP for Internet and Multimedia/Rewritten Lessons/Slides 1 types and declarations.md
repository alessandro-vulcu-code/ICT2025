# C++ Types and Declarations

## Outline
- [C++ Types](#c-types)
  - [Fundamental Types](#fundamental-types)
  - [User-Defined Types](#user-defined-types)
- [Fundamental Type Details](#fundamental-type-details)
  - [Boolean](#boolean)
  - [Characters](#characters)
  - [Integers Floating Point and void](#integers-floating-point-and-void)
- [Sizes and Portability](#sizes-and-portability)
- [Declarations and Definitions](#declarations-and-definitions)
  - [Declarator Operators](#declarator-operators)
- [Scope](#scope)
  - [Kinds of Scope](#kinds-of-scope)
  - [Hiding and Shadowing](#hiding-and-shadowing)
- [Initialization](#initialization)
  - [auto](#auto)
  - [Consistent Initialization](#consistent-initialization)
- [Objects and Value Categories](#objects-and-value-categories)
  - [Objects](#objects)
  - [lvalues and rvalues](#lvalues-and-rvalues)
  - [Object Lifetime](#object-lifetime)
- [Type Aliases](#type-aliases)
- [const and constexpr](#const-and-constexpr)

## Study Notes

### C++ Types

#### Fundamental Types

**Fundamental types** are available without any additional declaration. Examples are `int` and `bool`. They are part of the core language and are used to represent basic values.

#### User-Defined Types

**User-defined types** are introduced by the programmer or by a library header. `std::vector` is an example: it comes from the standard library, but it is still a type defined outside the core set of fundamental types.

### Fundamental Type Details

#### Boolean

`bool` represents one logical value: `true` or `false`. It is used for conditions and logical results. The slide shows:

```cpp
bool b1 {1 = 0};
```

This is malformed C++. The likely intended example is `bool b1 {1 == 0};`, which initializes `b1` to `false`. The distinction is important: `=` is assignment, while `==` is equality comparison.

#### Characters

C++ has several character types: `char`, `signed char`, `unsigned char`, and `wchar_t`. A `char` is **almost always** 8 bits, and 7 bits are enough for ASCII.

Plain `char` may be implemented as signed or unsigned. This is **implementation-defined**, so code that depends on signedness should use `signed char` or `unsigned char` explicitly.

Character literals use single quotes, for example `'a'` or `'0'`. Escape sequences use backslash, such as `'\n'`. A character can also be written through its numeric code, including hexadecimal notation.

```cpp
char c1 = 'a';
char c2 = '\x61';
char c3 = 97;
std::cout << c1 << std::endl; // print a
std::cout << c2 << std::endl; // print a
std::cout << c3 << std::endl; // print a
```

All three variables print `a` on ASCII-compatible systems. The example shows that characters store numeric codes, but character literals are usually clearer than raw numbers.

#### Integers Floating Point and void

**Integer types** include `int`, `signed int`, `unsigned int`, `short int`, `long int`, and `long long int`. Signed types represent negative and positive values; unsigned types represent only non-negative values.

**Floating-point types** include `float`, `double`, and `long double`. Their precision is implementation-defined, although common platforms often follow IEEE-754 conventions.

`void` has two main uses: it marks a function as returning no value, and it can appear in `void*`, a pointer to an object of unknown type.

### Sizes and Portability

The exact size of many fundamental types is **implementation-defined**. A program may know the size for a specific compiler and platform, but portable code should not assume that every implementation uses the same sizes.

```text
Language != what the compiler implements
```

`sizeof` returns a size measured in units of `char`, and `sizeof(char)` is always `1`. The standard guarantees relationships such as:

```text
1 == sizeof(char) <= sizeof(short) <= sizeof(int) <= sizeof(long) <= sizeof(long long)
sizeof(float) <= sizeof(double) <= sizeof(long double)
```

These are relative guarantees, not exact byte sizes.

The `<cstdint>` header provides integer types with size-related names, such as `int16_t`, `uint32_t`, and `uint_fast32_t`. Exact-width types require the implementation to support that exact representation, while `uint_fast32_t` asks for a fast unsigned type with at least 32 bits.

The `<cstddef>` header defines `size_t`, the standard unsigned type capable of representing the size in bytes of any object. It is the type returned by `sizeof`.

### Declarations and Definitions

A **declaration** introduces a name with a type. A **definition** additionally gives the program all information needed to use that entity: storage for an object, a body for a function, or members for a class.

C++ requires one and only one definition for each entity that needs a definition. This is the practical idea behind the **One Definition Rule**.

The source recommends consistent naming conventions, such as camelCase and snake_case, and references:

```text
https://gist.github.com/lefticus/10191322#c-coding-standards-part-1-style
```

A declaration may include an optional prefix, a base type, a declarator, optional suffixes, and an initializer or function body.

```cpp
int a_number {10};
const char* str_c {"example of declaration"};
std::vector<double> double_vec {0.1, 0.4, 0.5};
```

`a_number` is an `int`, `str_c` is a pointer to constant `char`, and `double_vec` is a `std::vector<double>` initialized with three values.

```cpp
static const char* universities[] {"Padova", "Venezia"};
```

Here `universities` is a static array of pointers to constant characters. The type cannot be omitted; `*` and `[]` are **declarator operators**.

#### Declarator Operators

Declarator operators describe pointers, references, arrays, and functions.

| Declarator operator | Meaning |
| --- | --- |
| prefix `*` | pointer |
| prefix `*const` | constant pointer |
| prefix `*volatile` | volatile pointer |
| prefix `&` | lvalue reference |
| prefix `&&` | rvalue reference |
| prefix `auto` | function using suffix return type |
| postfix `[]` | array |
| postfix `()` | function |
| postfix `->` | return type from function |

Postfix declarator operators bind tighter than prefix operators. Parentheses are therefore important.

```cpp
char* universities[];
char (*universities)[];
```

The first declaration is an array of pointers to `char`. The second is a pointer to an array of `char`. This is why spacing and parentheses matter in C++ declarations.

### Scope

**Scope** determines where a name can be used. It is central to C++ resource management because automatic objects are destroyed when their scope ends.

#### Kinds of Scope

A local name is declared inside a block and is visible from its declaration to the end of that block.

```cpp
f()
{
    Block: from { to }
    int a {10};
    std::cout << a << std::endl;
}
// a does not exist here

- Class
  Member name if defined in class `but` outside functions
  The scope extends to the class block (from { after the declaration to the end })
```

This block preserves the source, but it mixes code and slide text. The intended point is that `a` exists only inside the function block. The class-scope text means that a member declared in a class, but outside member functions, is visible within the class body.

Other scopes include:

- **Namespace scope**: a name declared inside a namespace, outside local scopes.
- **Global scope**: a name declared outside functions, classes, enums, and namespaces.
- **Statement scope**: a name declared in the control part of `for`, `while`, `if`, or `switch`.

```cpp
for(int index = 0; index < 10; ++index)
{
    Scope of index
    std::cout << index << std::endl;
}
// index does not exist here
```

`index` exists only inside the `for` statement. The line `Scope of index` is slide text, not valid C++.

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

This example shows nested global, namespace, class, local, and statement scopes. `local_scope` is not declared in the snippet, so that comparison is likely a transcription error.

#### Hiding and Shadowing

**Shadowing** happens when an inner declaration reuses a name from an outer scope. C++ allows it, but it should be minimized because it makes name lookup harder to reason about.

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

The global `index` is hidden by the local `char index`. The loop introduces another `index`, and the nested block introduces a `double index`. After the nested block, `index = 'b';` refers again to the local `char`.

### Initialization

C++ supports several initialization forms:

```text
T a1 {v}; -> Introduced in C++11
- Does not allow narrowing
  int a1 {0.2}; //compilation error
- Strongly recommended except with auto
- {} indicates initialization with default value
(if present)

T a2 = {v};

T a3 = v;

T a4(v);
```

Brace initialization is strongly recommended in many cases because it rejects **narrowing conversions**. For example, `int a1 {0.2};` is a compilation error because the fractional part would be lost.

#### auto

`auto` lets the compiler infer a variable type from its initializer.

```cpp
int a1 = 2292;
auto a2 = 2292; // a2 is int
```

`a2` is deduced as `int`. `auto` is useful for long type names:

```cpp
std::vector<T>::iterator a1 = vec.begin();
auto a1 = vec.begin();
```

Use `auto` mainly in small scopes, where the initializer is visible and the deduced type remains clear. The source warns against `{}` with `auto`, because it may deduce `std::initializer_list<T>` instead of the intended type.

#### Consistent Initialization

Uninitialized variables are a common source of bugs.

```cpp
int globalVariable; // means globalVariable{}; -> 0
Valid for static, global, namespace names

void f()
{
    int localVariable; // no well-defined value!
}
```

The explanatory line inside the code block is slide text. Static, global, and namespace-scope variables are zero-initialized. A local fundamental variable such as `int localVariable;` has an indeterminate value until explicitly assigned.

### Objects and Value Categories

#### Objects

A C++ **object** is a contiguous region of storage in memory. It has **identity**, meaning it can be referred to by a name, pointer, or reference.

The slide says an object is "not movable"; in modern C++, move operations can transfer resources, but the original object still remains alive and valid. It may simply be left in an unspecified but valid state.

#### lvalues and rvalues

| Expression category | Has identity | Is movable |
| --- | --- | --- |
| lvalue | Yes | No |
| rvalue | It depends | Yes |

An **lvalue** has identity. An **rvalue** can be moved from and often represents a temporary.

```cpp
std::vector<int> vec1 {1, 2, 3};
auto vec2 = someFunction(vec1);
lvalue rvalue
auto vec3 = vec1;
lvalue
```

The labels `lvalue rvalue` and `lvalue` are slide annotations, not valid C++. `vec1` is an lvalue because it is named. The return value of `someFunction(vec1)` is an rvalue if the function returns by value. `auto vec3 = vec1;` copies from the lvalue `vec1` unless move semantics or optimizations apply.

#### Object Lifetime

An object's valid lifetime runs from the end of construction to the beginning of destruction.

- **Automatic** objects live until they go out of scope.
- **Static** objects live until program termination.
- **Free-store** objects are controlled with `new` and `delete`.
- **thread_local** objects live for the duration of a thread.
- **Temporary** objects usually live until the end of the full expression that uses them.

```cpp
std::cout << std::string("tmp").size() << std::endl;
```

`std::string("tmp")` is a temporary object. It remains alive long enough for `.size()` to be called, then it is destroyed at the end of the full expression.

### Type Aliases

A **type alias** is a synonym for another type.

```cpp
using viter = std::vector<int>::iterator;
typedef std::vector<int>::iterator viter;

std::vector<int> vec = {1,2,3};
std::vector<int>::iterator a = vec.begin();
viter b = a;
```

Both `using` and `typedef` define `viter` as an alias for `std::vector<int>::iterator`. In modern C++, `using` is usually clearer, especially for alias templates.

### const and constexpr

`const` declares that an object cannot be modified through that name after initialization. A `const` object must be initialized when declared, except for class members initialized by constructors or in-class initializers.

Function parameters can be `const` to state that the function only reads the argument.

The source writes `const exp`, but the C++ keyword is **`constexpr`**. A `constexpr` expression can be evaluated at compile time when its inputs are known at compile time. It is based on known values such as integers, floating-point values, enums, operators, and other constant expressions.

## 5 Mins Questions

No 5 mins questions are present in the source material.

## Final Summary

This lesson introduces the basic vocabulary for reading C++ declarations. **Types** define what values mean, while **declarations** introduce names and **definitions** provide usable program entities. Type sizes are implementation-defined, so portable code should rely on standard headers and documented guarantees rather than assumptions.

Scope controls where names exist and is essential for C++ resource management. Initialization should be explicit, preferably with braces when appropriate, and `auto` should be used where the deduced type remains clear. Finally, objects, lvalues, rvalues, lifetimes, aliases, `const`, and `constexpr` provide the foundation for later topics such as references, move semantics, and resource ownership.
