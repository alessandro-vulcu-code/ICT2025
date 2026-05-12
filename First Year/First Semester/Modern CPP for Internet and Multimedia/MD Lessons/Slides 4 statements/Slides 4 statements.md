<!-- Pagina 1 -->

Statements

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

1. Statements and declarations
2. Selection statements
3. Iteration statements
4. Jump statements

[c++pl] Chapter 9

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Statements

• Declarations and expressions ending with ;
• Parts of a program that specify the order of execution
• The categories of statements available in C++ are
  1. expression statements
  2. compound statements (sequence of statements between {})
  3. selection statements (if, if else, switch)
  4. iteration statements (while, do, for)
  5. jump statements (break, continue, return)
  6. declaration statements
  7. try blocks (try) for exception handling
  8. empty statement (;)

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

Declarations as statements

• A declaration is a statement
• The instruction is executed when the control passes through the declaration
  • Allow better locality of the code
  • Minimize uninitialized variables do not declare it and initialize it later – a declaration as a statement makes it possible to introduce the variable when is needed and a value is available for it
  • This does not hold for variables declared static more on this when we discuss functions

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)


---

<!-- Pagina 5 -->

Selection statements - if

if (condition) statement

Expression or declaration

Good practice: use a compound statement (i.e., enclose it in a block) – otherwise:
• if there is more than one statement after the if, only the first is considered to be the statement conditioned by the if
• for example, variables can be declared and initialized only in a compound statement
it would be pointless to have a single instruction that declares a variable that is not used as it goes out of scope before the next instruction

• It is possible to declare and initialize a variable in a condition
• The scope ends at the end of the statement after the if
• The condition will test the value of the variable
• Improve locality and minimize uninitialized variables!

---

**Immagini estratte:**

![Figura estratta 1](p05_img01.jpg)


---

<!-- Pagina 6 -->

if conditions

• You can use a boolean value or an expression
• If different from a boolean, there is an implicit conversion

```c
int x = 1
if (x) // equivalent to if(x≠0)
{
    // do something
}

int *p = &x
if(p) // eq. to if(p≠nullptr)
{
    // do something
}
```

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)


---

<!-- Pagina 7 -->

if conditions – logical operators

It is possible to use logical operators to combine conditions

• a &amp; b - and, true if both conditions are true
• a || b - or, true if at least one of the two conditions is true
• !a – not, true if a is false

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)


---

<!-- Pagina 8 -->

# if conditions – lazy evaluation

• Lazy evaluations
  • Always check the first condition in expressions with logical operators
  • Evaluate the second only it the first is not enough
  • Pay attention when using functions (e.g., with a boolean return type) in conditions

```cpp
bool c1 = false;
bool c2 = true;
if (c1 && c2)
{ // c2 is not evaluated }
if (c2 && c1)
{ // both evaluated }
if (c1 && someFunction(c2))
{
  // someFunction(c2) is not evaluated
  // this may be done on purpose (always comment it!)
  // it could also lead to errors if not done on purpose
}
```

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)


---

<!-- Pagina 9 -->

Conditional expression

• The conditional expression or ternary operator allows the selection of an expression among two, according to the evaluation of a third expression
• Use it only for simple statements!
  ```javascript
  val = expression 1 ? expression 2 : expression 3
  ```
  ```javascript
  // with ternary operator
  int x = 1;
  int x2 = (x==1) ? 2 : 3;
  ```

  ```javascript
  // equivalent to
  int x2;
  if (x == 1) {
    x2 = 2;
  }
  else {
    x2 = 3;
  }
  ```

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

## switch statement

• Select among a set of alternatives (case labels)

```c
switch (variable)
{
    case val1:
// code
    case val2:
// code
}
```

with type integer or enum (or user-defined type that can be implicitly converted to integer or enum)

• Generate more efficient compiled code with respect to if

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

## switch statement - termination

• Terminate the code of the case
  • Use break (exits the switch) or return (exits the function with the switch)
  • Otherwise, the next case is executed ("fall through")
  • Explicitly comment is fall though is intentional

```c
switch (action)
{
    case do_and_print:
        act(value);
        // no need to implement print
        // fall through the next case
    case print:
        print(value)
        break;
    case something_else:
        something(value)
        break;
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

# switch statement - default

• There is a default case
  • Handle the most common case
  • Handle the cases that are not covered by the switch (e.g., by raising an exception)

```c
switch (action)
{
  case 1:
    // code
    break;
  case 2:
    // code
    break;
  default:
    // code
}
```

• Do not use it with enumerators
  • The compiler can warn if the set of cases does not match the set of values of the enumerator

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Range-for statements

• Loop and access to each element of a range
• They work with sequences or ranges – entities that
  • yield an iterator for the beginning and the end of the sequence
  • have a begin/end member pair
  • Examples: C++ arrays, std::vector<T>

```cpp
std::vector<int> v {1,2,3,4};
for (int value : v)
{
    std::cout << value << std::endl;
}
```

• Loops over values cannot modify the values
  • If the values needs to be modified, the loop variable needs to be a reference

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

for statements

• More general than range-for statements

```cpp
for (int i = 0; i < 10; i++)
{
    std::cout << i << std::endl;
}
```

• a variable (as int i) can be declared and initialized here, and the scope ends at }
• if it has to be available after the end of the for loop, it can be declared and initialized before

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

# for statements

• auto may be handy
  ```c
  std::vector<T> c;
  for (auto p = c.begin(); p ≠ c.end(); ++p)
  {
    // do something
  }
  ```

• there is flexibility in the statement of the for loop
  ```c
  int i = 0;
  for (; i < 10;)
  {
    i++;
  }
  ```

• in these cases, however, a while statement is clearer

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p15_img01.jpg)


---

<!-- Pagina 16 -->

for statements – pre increment

• pre-increment: increment, and then evaluate the new value
• post-increment: increment the value but evaluate the old value

• In C++, pre-increment is preferred when they are equivalent (e.g., in for loops)
  • It avoids the (implicit) generation of an extra temporary variable
  • No difference with fundamental types
  • Performance difference with user-defined types (e.g., iterators on standard library data structures)

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p16_img01.jpg)


---

<!-- Pagina 17 -->

## while statements

• Check the control condition, if true execute

```c
int i = 0;
while (i < 10)
{
    // do something
    ++i;
}
```

• It could be more natural to expression complex conditions with a while than with a for (which depends more logically on a single variable)

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)


---

<!-- Pagina 18 -->

do statements

• Execute, then check the control condition and execute again if true

```c
int i = 0;
do
{
    ++i;
} while (i < 10);
```

• The body of the statement is executed at least once
• If some logic about the condition is used in the body of the loop, the condition needs to hold at the first execution

---

**Immagini estratte:**

![Figura estratta 1](p18_img01.jpg)


---

<!-- Pagina 19 -->

Loop exit

• If the condition is omitted, or it is always true, the loop does not exit

It is possible to terminate a loop

• break statement – get out of the nearest-enclosing switch or iteration statement
  • if it depends on a condition, it is better to put the condition in the for/while

• continue statement – skip to the next iteration of an iteration statement
  • the code between the continue and the end of the block does not execute

• a return terminates a loop, but also the function that encloses the loop

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p19_img01.jpg)
