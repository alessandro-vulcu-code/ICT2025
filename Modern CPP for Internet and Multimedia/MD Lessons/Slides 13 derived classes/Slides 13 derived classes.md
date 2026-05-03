<!-- Pagina 1 -->

Derived classes and class hierarchies

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

1. Expressing relationships among classes
2. Derived classes
3. Members of derived classes
4. Class hierarchies
5. Virtual and polymorphism
6. Override control
7. Abstract classes
8. Access control

[c++pl] Chapters 20, 21

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Classes and relationships

In order to develop complex concepts, it is necessary to express relationships among classes

The “part of” relationship is expressed through data members
example: the Car class can have four private members of type Wheel

The “extends” relationship is expressed through class hierarchies
this is the basis for object-oriented programming (OOP)

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

Class hierarchies

Base or super class

Square Circle

Derived or sub classes
They represent a more specific concept

```cpp
class Shape { ... };
class Square : public Shape { ... };
class Circle : public Shape { ... };
```

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img01.jpg)


---

<!-- Pagina 5 -->

Inheritance in C++

C++ supports hierarchies through two different mechanisms:

1. Implementation inheritance
   Re-use the facilities (i.e., the actual implementation) provided by a base class

2. Interface inheritance
   Use different derived class interchangeably (they can share the same methods)
   Also known as run-time polymorphism

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)


---

<!-- Pagina 6 -->

Derived class example

```c
struct Employee { // this is used as base class
    // it must be declared
    string first_name, family_name;
    char middle_initial;
    Date hiring_date;
    short department;
}

We now need to implement the class for a manager, which is a specific kind of employee

We can re-use the base implementation of Employee and extends by adding manager-specific characteristics
```

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)


---

<!-- Pagina 7 -->

Derived class example

```csharp
struct Employee { // this is used as base class
    // it must be declared
    string first_name, family_name;
    char middle_initial;
    Date hiring_date;
    short department;
}

this expresses subclassing

struct Manager : public Employee {
    list<Employee*> group;
    short level;
}

Manager has the same members of Employee
+ its own members!
```

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)


---

<!-- Pagina 8 -->

Derived classes representation

Employee
• first name
• family name
• middle initial
• hiring date
• department

Manager
Employee
• first name
• family name
• middle initial
• hiring date
• department

• managed group
• level

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)


---

<!-- Pagina 9 -->

Derived classes

• It is possible to use Manager whenever an Employee is acceptable

```cpp
void f (Manager m1, Employee e1)
{
    std::vector<Employee*> vec {&m1, &e1};
}
```

• NOTE: Do not pass a Manager by value in e1 (slicing, see later)

• A Manager* is also an Employee*
• A Manager& is also an Employee&
• An Employee* is not a Manager*
(in case, an explicit conversion is needed)

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Member functions

A derived class can use public and protected members (data and functions) of the base – as if they were declared in the derived

• no access to private members
• if a function fun() is redefined in the derived class, it is possible to call that of the base BaseClass with a qualifier:

BaseClass :: fun()

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Constructors and destructors

Recall: execution order of constructors and destructors

• The operations that a constructor performs are in a fixed order:

1. (in case the class is derived from another `base` class) the constructor of the base class is called
2. the constructors of the data members of the (derived) class are called
3. the body of the constructor is executed

• The same goes for the operations of the destructor

1. the body of the destructor (of the derived class) is executed,
   • In the case you use pointers to the base class, only if the destructor of the base class is declared virtual
2. the destructors of the data members of the (derived) class are called
3. (in case the class is derived from another `base` class) the destructor of the base class is called

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

Constructors and destructors

• Each derived class can initialize the `base` and the members of the derived class – not directly those of the base

• Destructors of base classes are generally `virtual`

  • in this way, the destructor of subclasses is actually called
  • using `virtual` is the correct approach: the derived class may have more resources to release, or members that need to be cleared by the destructor -> the destructor defined by the base class may not be enough

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Slicing with copy constructors

• The default copy constructor/assignment performs a member-wise copy

• Slicing issue: when using a pointer to the base class for the derived object (e.g., Employee* to refer to Manager*), the **wrong copy constructor** may be called
  • the copied object contains only the copy of the base members
  • the others are left uninitialized

• Solutions
  • =delete the copy constructor in the base class
  • make the base class private or protected (we will see how)

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Slicing with copy constructors

```c
struct X {
    int m_number;
}

struct Y : public X {
    int m_second_number;
}

slicing example

// some code
void f(X *p)
{
    X h = *p; // if p points to a Y, only
    // m_number is copied (slicing)
}

Y example {1, 2};
f(&Y);
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Inheriting constructors

It is possible to inherit all the constructors of a base class, without the need to declare and define new ones

```java
class Y : public X {
    using X::X;
    // this inherits X constructors
    ...
}
```

The derived class may have additional data members, which would not be initialized in this case

• option 1: do not inherit the constructors
• option 2: in-class initializers for the additional members

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)


---

<!-- Pagina 16 -->

Class hierarchies

It is possible to have

• multiple base classes
  (e.g., Temp, Consultant in the example)

• another derived class as base
  (e.g., Temp, Consultant, Director in the example)

Stroustrup, Bjarne. The C++ programming language. Pearson Education, 2013, page 583

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)


---

<!-- Pagina 17 -->

Navigating class hierarchies

Given a type Base*, to which actual type does the object pointed to belong?

• example: an Employee* can be used for an Assistant*, Temp*, Manager*, Director*

There are 4 options to solve this ambiguity:
1. Use objects of a single type
2. Type fields
3. Virtual functions
4. Abstract classes

---

**Immagini estratte:**

![Figura estratta 1](images/p17_img01.jpg)


---

<!-- Pagina 18 -->

Navigating class hierarchies

1. Ensure that only objects of a single type are pointed to in a specific section of your program (e.g., only Assistants)

- this is useful especially when implementing homogeneous containers (e.g., a list with a single type)
- however, this assumption needs to be checked by the developer as it is not enforced by the compiler -> this can lead to errors

---

**Immagini estratte:**

![Figura estratta 1](images/p18_img01.jpg)


---

<!-- Pagina 19 -->

Navigating class hierarchies

2. Type field – the object has a data member that holds the type of the object
• the correctness of this is not enforced by the compiler
• an addition of new derived classes requires changes in other classes
• limited and error prone techniques

```c
struct Employee {
    enum class Empl_type {manager, employee};
    Empl_type m_type;
    ...
    Employee() : m_type{Empl_type::employee} {}
}

struct Manager : public Employee {
    Manager () { m_type = Empl_type::manager; }
    ...
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p19_img01.jpg)


---

<!-- Pagina 20 -->

Navigating class hierarchies - virtual

3. Virtual

A function declared virtual can be redefined (“overridden”) in a derived class

• it must keep the same list of arguments
• it must keep the same return type except for return type pointers or references that can be relaxed from the Base to the Derived class
• the complier and linker will guarantee that the correct function is called
• it is defined in the base class
  • it can be overridden in derived classes only if needed

---

**Immagini estratte:**

![Figura estratta 1](images/p20_img01.jpg)


---

<!-- Pagina 21 -->

Navigating class hierarchies - virtual

```c
struct Employee {
    virtual void print() const;
}

void f (std::vector<Employee*> vec)
{
    for (Employee* elem : vec)
    {
        elem->print();
    }
}
```

Employee* can point to Employee or Manager

here we want to use a different print() for an actual Employee or an actual Manager (there are more members to be printed with a Manager)

---

**Immagini estratte:**

![Figura estratta 1](images/p21_img01.jpg)


---

<!-- Pagina 22 -->

Navigating class hierarchies - virtual

```c
struct Employee {
    virtual void print() const;
    ...
}

void Employee::print() const
{
    std::cout << family_name << std::endl;
}

struct Manager : public Employee {
    void print() const;
    ...
}

void Manager::print() const
{
    Employee::print();
    std::cout << level << std::endl;
}
```

Manager overrides the virtual print() method of Employee

• The call to the print() of the base is needed if the derived has no access to the base private members

• The :: qualifier ensures that the print() from Employee is called – otherwise, infinite recursion

---

**Immagini estratte:**

![Figura estratta 1](images/p22_img01.jpg)


---

<!-- Pagina 23 -->

Polymorphism

Virtual enables runtime polymorphism

• use different implementations of a virtual function according to the actual object on which they are called
• the objects need to be manipulated with pointers or references
• for direct manipulation, the type is already known, there is no space left for polymorphism

```cpp
void f (std::vector<Employee*> vec)
{
    for (Employee* elem : vec)
    {
        elem->print();
    }
}
```

the compiler will automatically select the correct print() function for each of the elements in the vector

---

**Immagini estratte:**

![Figura estratta 1](images/p23_img01.jpg)


---

<!-- Pagina 24 -->

Override control

• In complex class hierarchies, it may be difficult to control what you are overriding
  • Hiding issue: if you declare a function in a subclass with the same name but different arguments, this hides the function of the base, even if declared virtual (no override)

• More specific controls can be used to help the design of inheritance in complex class hierarchies, using
  • virtual
  • override
  • final
  • =0 (abstract classes)

---

**Immagini estratte:**

![Figura estratta 1](images/p24_img01.jpg)


---

<!-- Pagina 25 -->

Override control

• virtual
  • the function *may* be overridden

• override
  • to be used in derived classes (but optional)
  • if used at the end of a function declaration, it specifies that we want to override a virtual function
  • the compiler raises an error if this does not happen
    • for example, because you are actually hiding the function
  • it is not part of the type (do not use it out of the class declaration)
  • last word in the declaration
  • not an actual keyword
    • historical reasons: it has been introduced recently, and many codebases already use it for function and variable names

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)


---

<!-- Pagina 26 -->

Override control

• final
  • a function can be virtual or not
  • different reasons for why a function should not be virtual:
    • it is hard to specify it more without errors
    • there is no need to specify it more

these conditions may become true only after a few derivations

• final prohibits to further override a function that was declared virtual in some upstream base class
• it can be used after a class name to make all methods final and prevent deriving from the class

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)


---

<!-- Pagina 27 -->

Navigating class hierarchies - abstract

4. Abstract classes

A “shape” is an abstract concept that does not actually exist (the employee instead exists)

• It can be logically difficult to give a sense to the definition of virtual functions
  e.g., how do you implement a generic “area” function for a generic shape?

• Abstract classes are those with at least one pure virtual function

$$\text{virtual T pureVirtualFunction(U arg)} = 0;$$

• The definition of a pure virtual function usually is not given in the abstract class

---

**Immagini estratte:**

![Figura estratta 1](images/p27_img01.jpg)


---

<!-- Pagina 28 -->

Abstract classes

• Abstract classes are only **interfaces** for polymorphic types
• Objects of a type represented by an abstract class cannot be created
  • Only those of derived classes that override **all the methods**
  • If a pure virtual function is not overridden, the derived class remains abstract
    • this allows the definition of implementation in stages
    • **interface inheritance**

---

**Immagini estratte:**

![Figura estratta 1](images/p28_img01.jpg)


---

<!-- Pagina 29 -->

Access control

Members (functions, types, constants, variables and classes) can be

• `private` – accessible only by member functions and friends of the class where the member is declared
• `protected` – as private + member functions and friends of the derived classes
• `public` - any function

protected is useful in class hierarchies but open to abuse

---

**Immagini estratte:**

![Figura estratta 1](images/p29_img01.jpg)


---

<!-- Pagina 30 -->

Access control - protected

protected data members are usually a design error

• data corruption if improperly used in derived classes
  • use the minimum number of data members in common base classes

• hard to restructure the code (who knows who is using a certain protected member in derived classes)

• protected functions are generally more useful
  • virtual protected functions can be overridden while being hidden from the interface of the object

---

**Immagini estratte:**

![Figura estratta 1](images/p30_img01.jpg)


---

<!-- Pagina 31 -->

Access control for base classes

A base class can be

• public – the derivation creates a subtype for example X is a kind of B, and they can be used for runtime polymorphism

```python
class X : public B { ... }
```

• private – the derivation restricts the interface to that of a base and changes some details only the derived class is aware that is inheriting from the base, so the base B cannot be further derived through the already derived class Y

```python
class Y : private B { ... }
```

---

**Immagini estratte:**

![Figura estratta 1](images/p31_img01.jpg)


---

<!-- Pagina 32 -->

Access control for base classes

A base class can be
• protected – same as private, but the class can be further derived

```python
class Z : protected B { ... }
```

If not specified, the default is private for classes and public for struct

---

**Immagini estratte:**

![Figura estratta 1](images/p32_img01.jpg)


---

<!-- Pagina 33 -->

Replication issue

A class can inherit from multiple bases
• Public inheritance to inherit the interface
• Private/protected inheritance to inherit implementation details

There may be a replication issue

```java
class A : public B, public C { ... };
class B : public D { ... };
class C : public D { ... };
class D { ... };

A has two objects of type D
• if D is not an abstract class and has data, A may have repeated members
```

---

**Immagini estratte:**

![Figura estratta 1](images/p33_img01.jpg)


---

<!-- Pagina 34 -->

Replication issue – virtual base

• The replication issue can be solved by declaring a base class virtual

```java
class A : public B, public C { ... };
class B : public virtual D { ... };
class C : public virtual D { ... };
class D { ... };
```

---

**Immagini estratte:**

![Figura estratta 1](images/p34_img01.jpg)
