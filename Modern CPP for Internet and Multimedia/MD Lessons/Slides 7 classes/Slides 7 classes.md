<!-- Pagina 1 -->

Classes

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

1. Classes
2. Member functions
3. Access control
4. Constructors
5. Mutability
6. Self-reference
7. Static members
8. Concrete classes

[c++pl] Chapter 16

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Classes

• A class introduces an user-defined type, i.e., a concrete representation of a concept
• The creation of a class allows a programmer to separate the details of the implementation
  • which kind of variables are used to represent the object
  • how the representation interacts with these variables
  • the properties essential to the use of the type
  • the “interface” that an external user can use to manipulate objects of this type

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

Classes basics

• A class is a user-defined type with a set of members

• Members can be
  • data, i.e., variables that represent the state of the type
  • functions, i.e., methods that perform initialization, copy, move, cleanup and all the other actions related to the type

• Members can be
  • public, to represent the class interface
  • private, to hold the implementation details

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img01.jpg)


---

<!-- Pagina 5 -->

Classes basics

• It is possible to access to members with the . operator (for objects) or the → operator (for pointers to objects)

• It is possible to define operators (e.g., + - [ ]) for the type

• A class defines invariants, i.e., a property of a type that holds from its initialization to the destruction

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)


---

<!-- Pagina 6 -->

Example of class

```cpp
class X {
// the representation (implementation) is private
private:
    int m;
public: // the user interface is public
    X(int i = 0) :m{i} { } // constructor
    // member function with definition
    int mf(int i) {
        int old = m;
        m = i;
        return old;
    }
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)


---

<!-- Pagina 7 -->

Example of class usage

```cpp
X var {7};
// a variable of type X, initialized to 7

// a function that interacts with var
int f(X var, X* ptr)
{
    int x = var.mf(7); // access using .
    int y = ptr->mf(9); // access using →
    int z = var.m; // error: cannot access
        // private member
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)


---

<!-- Pagina 8 -->

Member functions

• Functions declared within a class definition
• They are invoked only for variables of the appropriate type
• Definition:
  • in a separate location (usually a .cpp file) than the declaration (usually in header .h file). In this case, the definition needs to have the name of the class
  • in the class declaration
    • small and rarely modified functions – otherwise, the code that uses them is recompiled every time the function is modified
    • they are implicitly inlined
      recall from the class on functions: inline = new code for every function call, instead than of a single code in memory that is pointed to by every function call.

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)


---

<!-- Pagina 9 -->

Example of member functions

```cpp
class X {
    ...
    // member function with inlined definition
    int mf(int i) {
        int old = m;
        m = i;
        return old;
    }
    // member function with only declaration
    int amf(int j);
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Example of member functions

```cpp
class X {
    ...
    int amf(int j);
};

// we need to define it elsewhere
int
X::amf(int j)
{
    return j + 2;
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Access control

It is possible to specify to which members of the class it is possible to access to from other classes. This is useful

• to control the behavior and what can be changed in the representation of an object
• to expose only the public way to interact with a class – easier to update the underlying representation
  • no need to recompile code that uses that class
  • the programmer can only study the public interface

This is achieved with the public and private labels

The friend label can be use to indicate exceptions

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

Example of public/private

```cpp
class X {
  // private unless after a public label
  int m;
  // it is possible to use a private label
  private:
    int m2;
    int doSomething(double d);
  // for public members, it is necessary to use a
  // public label
  public: // the user interface is public
    X(int i =0) :m{i} { } // constructor
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Example of friend classes

```cpp
class Y {
    friend X;
// class x can access both private and public
// members and functions of y
private:
    int v;
    int doSomething(double d);
// for public members, it is necessary to use a
// public label
public: // the user interface is public
    Y(int i =0) :v{i} { } // constructor
};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Structs and classes

• A struct is nothing but a class with all members public by default

• In general,
  • use a struct for a simple data structure
  • use a class to enforce invariants

• A class is better at enforcing invariants
  • the underlying representation can be hidden to external users, which can interact with private members only through specific public methods
  • the class developer can make sure that invariants are enforced through these public methods

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Constructors

• Member functions that have the explicit purpose of initializing objects
• They have the same name of the class, and no return type
• It is possible to use the () and {} notations
  (the latter is more consistent with respect to built-it types, and highlights better what is being done)

$$\text{Date today} = \text{Date}(22,2,1992);$$
$$\text{Date tmrw} = \text{Date}{22,2,1992};$$

• It is possible to have multiple constructors, with different sets of arguments
  The same overloading rules for functions apply

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)


---

<!-- Pagina 16 -->

Explicit constructors

• Implicit conversion: a constructor with a single argument implicitly converts it to the type of the constructor’s class
  • This may not be desirable: the programmer may not want to construct an object
  • It introduces unexpected temporary objects

• explicit keyword prevents a constructor from being used in implicit conversions (otherwise, compilation error)

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)


---

<!-- Pagina 17 -->

Explicit constructors

```java
class Date {
public:
    explicit Date(int d);
}

// ...
Date d = 15; // error
Date d {15}; // ok,
// {} considered explicit

class Date {
public:
    Date(int d);
}

// ...
Date d = 15; // ok, but
// not very clear
```

• It is a good practice to keep single argument constructors explicit
• Unless exceptions, e.g., `std::complex<double> c = 1;` - it naturally creates a complex with only the real part

---

**Immagini estratte:**

![Figura estratta 1](images/p17_img01.jpg)


---

<!-- Pagina 18 -->

In-class initializers

• Classes can have many constructors, accepting different arguments
• It can be useful to have `default` values for the data members
• A constructor can then modify them if needed

```cpp
class Date {
  int d {22};
  int m {02};          in-class initialization
  int y {1992};
public:
  Date(int, int, int); // day, month, year
  Date(int, int); // day, month, year is default
  Date(int); // day, month and year are default
  Date(); // default date, 22/02/1992
  Date(const char*); // date in string representation
  ...
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p18_img01.jpg)


---

<!-- Pagina 19 -->

Mutability

• A name can refer to a object with values which are
  • Mutable
  • Immutable, i.e., const
• Member functions need to work on const objects

1. **Constant member functions**

```c
int getDay() const;
```

const is part of the type, it must be repeated also in the definition

These functions do not modify the value of the object

• Const member functions work on const and non-const objects
• Non-const member functions do not work on const objects

---

**Immagini estratte:**

![Figura estratta 1](images/p19_img01.jpg)


---

<!-- Pagina 20 -->

Mutability

2. Logical constness

A const member function may need to change a member data value, without affecting the actual representation (logical value) of the object

• example: the cache of a string representation of the object value
  class Date {
    int d {22};
    int m {02};
    int y {1992};
    std::string string_cache;
    bool valid_cache;

    public:
      std::string string_rep() const;
  }

• string_rep does not change the status of the object, but it may need to update string_cache if d, m, or y are changed

---

**Immagini estratte:**

![Figura estratta 1](images/p20_img01.jpg)


---

<!-- Pagina 21 -->

Mutability

To address this:

a. declare members mutable – they can be modified even in const objects
• this is ok only if a small part of the object needs to change

```cpp
class Date {
  int d {22};
  int m {02};
  int y {1992};
  mutable std::string string_cache;
  mutable bool valid_cache;
  ...
public:
    std::string string_rep() const;
private:
    void compute_cache_value() const;
```

---

**Immagini estratte:**

![Figura estratta 1](images/p21_img01.jpg)


---

<!-- Pagina 22 -->

# Mutability

```cpp
class Date {
    int d {22};
    int m {02};
    int y {1992};
    mutable std::string string_cache;
    mutable bool valid_cache;

    ...
public:
        std::string string_rep() const;

private:
        void compute_cache_value() const;

        string Date::string_rep() const
        {
            if (!valid_cache) {
                // update string_cache
                compute_cache_value();
                valid_cache = true;
            }
            return string_cache;
        }
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p22_img01.jpg)


---

<!-- Pagina 23 -->

Mutability

To address this:

b. mutability through indirection – the properties that need to be updated can be placed in another object, with a pointer to it as member of the class
• const does not apply to objects accessed through pointers or references

```c
struct cache { bool valid; string rep; };
```

```cpp
class Date {
    int d {22};
    int m {02};
    int y {1992};
    cache* date_cache;
    ...
```

```cpp
    string Date::string_rep() const
    {
        if (!c->valid) {
            // update
            compute_cache_value();
            c->valid = true;
        }
        return c->rep;
    }
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p23_img01.jpg)


---

<!-- Pagina 24 -->

Self-reference

• this is a pointer to the object on which the function was called
  • object of type non-const X -> this has type X*, but is considered an rvalue (it is not possible to get its address or assign to it)
  • object of type const X -> this has type const X*

• most uses are implicit (it is not necessary to specify this→member_value in member functions)
• it could be useful to return a reference to it to chain operations

```python
Date& add_year(int year) { y += year; return *this; }
Date& add_month(int month) { m += month; m = m % 12; return *this; }

Date d {10, 05, 2003}
d.add_year(3).add_month(3);
```

this could be this→m but it is not necessary

---

**Immagini estratte:**

![Figura estratta 1](images/p24_img01.jpg)


---

<!-- Pagina 25 -->

Static members

• A static member is a variable that is part of a class, but not of a specific object of the class
  • Before the first use, they must be defined!

• There is exactly one copy of a static variable per program

• Static member functions can be called without using an object

• They may introduce concurrency issues with multi-threaded programs

```java
class Date {
    int d, m, y;
    static Date default_date;
public:
    Date(int dd =0, int mm =0, int yy =0);
    // ...
    static void set_default(int dd, int mm, int yy);
    // set default_date to Date(dd,mm,yy)
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)


---

<!-- Pagina 26 -->

Static members

```java
class Date {
    int d, m, y;
    static Date default_date;
public:
    Date(int dd =0, int mm =0, int yy =0);
    // ...
    static void set_default(int dd, int mm, int yy);
    // set default_date to Date(dd,mm,yy)
};

// implementation (also in some other parts of the program)

// definition of Date::default_date
Date Date::default_date {16,12,1770};

// definition of Date::set_default
void Date::set_default(int d, int m, int y) {
    // assign new value to default_date
    default_date = {d,m,y};
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)


---

<!-- Pagina 27 -->

Concrete classes

• A “concrete” class defines a small, concrete type

Concrete class
its representation is part
of the definition

vs

Abstract class
interface to multiple
possible implementations
(e.g., some methods are declared but not defined)

• This allows us to
  • place concrete objects in the stack, to allocate them statically in memory or in other objects
  • copy & move objects
  • used objects as named variables (instead than using pointers and references)

• These classes represent simple user-defined types that yield optimal compiler-generated code

• Value-oriented paradigm (not OOP)

---

**Immagini estratte:**

![Figura estratta 1](images/p27_img01.jpg)


---

<!-- Pagina 28 -->

Concrete classes

They typically have
• Constructor
• Functions to examine an object (marked as `const`)
• Functions to modify the object (without the need to know its representation)
• (in case) Classes to report errors
• (in case) Helper functions

not necessarily in the class definition, but – for example – they can be in the same namespace

• Functions to copy and move the objects

See the example Course class in the code for this lesson!

---

**Immagini estratte:**

![Figura estratta 1](images/p28_img01.jpg)
