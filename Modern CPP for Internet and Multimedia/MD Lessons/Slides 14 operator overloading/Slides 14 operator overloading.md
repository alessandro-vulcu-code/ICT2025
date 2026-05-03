<!-- Pagina 1 -->

Operators overloading

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

1. Rules for operator overloading
2. Redefining <<
3. Overloading special operators

[c++pl] Chapters 18

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Operator overloading

It is possible to redefine operators for a certain user-defined type

```cpp
class Complex { // very simplified complex

    double re, im;

public:
    Complex(double r, double i) :re{r}, im{i} { }
    Complex operator+(const Complex&);
    Complex operator*(const Complex&);
};

The name of an operator is "operator" followed by the symbol a * b = a.operator*(b)

// so that you can write
Complex c = Complex{2, 3} + Complex{5, 6};
Complex d = c * Complex{0, 1};
```

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

Operator overloading

• It is possible to redefine the following operators:

+   -   *   /   %   ^   &
I   ~   !   =   <   >   +=
-=   *=   /=   %=   ^=   &=   |=
<<   >>   >>=   <<<=   ==   !=   <=
>=   &&   II   ++   --   ->*   ,
->   []   ()   new   new[]   delete   delete[]

Stroustrup, Bjarne. The C++ programming language. Pearson Education, 2013, page 529

• It is not possible to define new operators or redefine

• :: (scope resolution), . (member selection), .* (member selection through pointer to member)
• sizeof, alignof, typeid
• ?:: (ternary operator)

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img01.jpg)


---

<!-- Pagina 5 -->

Binary and unary operators

Binary operators

• Two arguments
  • Non-static member with the form `aa.operator@(bb)`
  • Non-member function with the form `operator@(aa, bb)`

Unary operators

• One argument (prefix or postfix)
  • Non-static member with the form `aa.operator@()`
  • Non-member with the form `operator@(aa)`

this is necessary for operators where aa is not in our control:
• built-in types
• user-defined types defined by someone else

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)


---

<!-- Pagina 6 -->

Overloading operators

• It is necessary to explicitly overload all the operators to be used
  • For example, the compiler does not infer operator+=() from operator+() and operator=()

• The rules related to passing arguments apply also in this case (value for built-in types, const lvalue references for user-defined types)

• It can be common to return a reference to this (with return type X& for user-defined type X)
  • useful for non-static member operators

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)


---

<!-- Pagina 7 -->

Operator <<

It is generally overloaded to concatenate output on std::cout or other streams

• << for built-in types is directly overloaded in the ostream header
• for user-defined types, it must be overloaded with a non-member function declaration
  • the first argument is of type std::cout – but we cannot add our function declarations into the definition of the ostream class
• if the overloaded operator needs access to the private members of the user-defined type it wants to manipulate:
  • call to a member function
  • friend keyword

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)


---

<!-- Pagina 8 -->

Call to a member function

```cpp
std::ostream& operator<< (std::ostream& out, const Y& y)
{
    return y.someFunction(out);
}

class Y
{
private:
    int j;
public:
    std::ostream& someFunction(std::ostream& out)
    {
        out << j;
        return out;
    }
}
```

Overloading <

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)


---

<!-- Pagina 9 -->

```cpp
friend keyword

class Y
{
private:
    int j;
    friend std::ostream& operator<<
        (std::ostream& out, const Y& y);

public:
    ...
}    j is private in Y!

std::ostream& operator<<(std::ostream& out, const Y& y)
{
    out << y.j;    the overloaded operator is defined as non-
    member in the innermost enclosing scope
    (e.g., the namespace for a class)
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

friend keyword

• friend is a powerful keyword
• it must be used with care, as it can break the encapsulation principle

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Overloading special operators

operator[]
• subscript operator
• it provides subscript access meaning to elements of user-defined types
• for example, the elements of a std::vector<T> can be accessed with []

operator()
• function call operator
• it is used to create function objects (or functors): objects that behaves as functions

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

Functors

```java
class CalculateAverageOfPowers {
public:
    CalculateAverageOfPowers(float p) :
        acc(0), n(0), p(p) {}
    void operator() (float x) {
        acc += pow(x, p); n++;
    }
    float getAverage() const { return acc / n; }

private:
    float acc; int n; float p;
};

we can call
CalculateAverageOfPowers functor{1};
functor(10); // this is a function call using the operator
// () on the object!
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Functors: example

• An interesting use is for the std::for_each loop

```cpp
CalculateAverageOfPowers avg{2};
std::vector<float> dataA {0.1, 0.2, 10};
std::vector<float> dataB {1, 2, 3};
std::vector<float> dataC {0.5, 8, 99};

avg = std::for_each(dataA.begin(), dataA.end(), avg);
avg = std::for_each(dataB.begin(), dataB.end(), avg);
avg = std::for_each(dataC.begin(), dataC.end(), avg);
```

call avg for each member of dataA/B/C (and it maintains a state across the different calls!)

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Functors: example

```python
CalculateAverageOfPowers avg{2};
std::vector<float> dataA {0.1, 0.2, 10};

avg = std::for_each(dataA.begin(), dataA.end(), avg);

1. Initialize avg: it will have p = 2 as exponent for the pow operation, n = 0, acc = 0
2. Call the overloaded operator () for avg on the first element of dataA
   • acc += pow(0.1, 2) → acc = 0.01
   • n++ → n = 1
3. Call the overloaded operator () for avg on the second element of dataA
   • acc += pow(0.2, 2) → acc = 0.05
   • n++ → n = 2
4. Call the overloaded operator () for avg on the third element of dataA
   • acc += pow(10, 2) → acc = 100.05
   • n++ → n = 3
5. What if we call getAverage() now?
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)
