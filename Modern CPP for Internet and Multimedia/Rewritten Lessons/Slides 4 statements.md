# Statements

## Outline
- [Statements Overview](#statements-overview)
  - [Statement Categories](#statement-categories)
  - [Declarations as Statements](#declarations-as-statements)
- [Selection Statements](#selection-statements)
  - [if Statements](#if-statements)
  - [Conditions and Conversions](#conditions-and-conversions)
  - [Logical Operators and Lazy Evaluation](#logical-operators-and-lazy-evaluation)
  - [Conditional Expression](#conditional-expression)
  - [switch Statement](#switch-statement)
  - [switch Termination](#switch-termination)
  - [default Case](#default-case)
- [Iteration Statements](#iteration-statements)
  - [Range-for Statements](#range-for-statements)
  - [for Statements](#for-statements)
  - [Pre-Increment and Post-Increment](#pre-increment-and-post-increment)
  - [while Statements](#while-statements)
  - [do Statements](#do-statements)
- [Jump Statements](#jump-statements)
  - [Loop Exit](#loop-exit)

## Study Notes

This lesson follows **[c++pl] Chapter 9** and explains how C++ statements control execution order.

### Statements Overview

#### Statement Categories

A **statement** is a part of a program that specifies execution. Declarations and expressions ending with `;` are statements.

The main statement categories in C++ are:

1. **Expression statements**.
2. **Compound statements**, which are sequences of statements between `{}`.
3. **Selection statements**, such as `if`, `if else`, and `switch`.
4. **Iteration statements**, such as `while`, `do`, and `for`.
5. **Jump statements**, such as `break`, `continue`, and `return`.
6. **Declaration statements**.
7. **try blocks** for exception handling.
8. **Empty statements**, written as `;`.

#### Declarations as Statements

A declaration is itself a statement. It is executed when control passes through it.

This supports better locality: declare a variable when it is needed and when a useful initializer is available. This minimizes uninitialized variables and avoids declaring something far away from its first use. The slide notes that this does not apply in the same way to variables declared `static`, which will be discussed with functions.

### Selection Statements

#### if Statements

The basic form is:

```cpp
if (condition) statement
```

The condition can be an expression or a declaration. Good practice is to use a **compound statement** after `if`, even when there is only one statement. Without braces, only the first statement is controlled by the `if`.

Braces are also necessary if the body declares a variable that should be used inside the conditional block. A single declaration without a surrounding block would go out of scope immediately and would usually be pointless.

C++ also allows declaring and initializing a variable in the condition. The variable's scope ends at the end of the controlled statement, which improves locality and reduces uninitialized state.

#### Conditions and Conversions

A condition can be a `bool` or an expression implicitly convertible to `bool`.

```cpp
int x = 1
if (x) // equivalent to if(x != 0)
{
    // do something
}

int *p = &x
if(p) // eq. to if(p != nullptr)
{
    // do something
}
```

The source is missing semicolons after `int x = 1` and `int *p = &x`. The intended point is that nonzero integers convert to `true`, zero converts to `false`, non-null pointers convert to `true`, and null pointers convert to `false`.

#### Logical Operators and Lazy Evaluation

Logical operators combine conditions:

- `a && b`: logical AND, true only if both conditions are true.
- `a || b`: logical OR, true if at least one condition is true.
- `!a`: logical NOT, true if `a` is false.

C++ uses **short-circuit evaluation** for `&&` and `||`: it evaluates the left operand first and evaluates the right operand only if needed.

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

When `c1` is false, `c1 && c2` is already false, so the second operand is skipped. This can be useful, but it must be intentional and clear, especially when the skipped expression calls a function with side effects.

#### Conditional Expression

The **conditional expression**, also called the ternary operator, selects one of two expressions based on a condition.

```cpp
val = expression1 ? expression2 : expression3;
```

Use it only for simple expressions.

```cpp
// with ternary operator
int x = 1;
int x2 = (x==1) ? 2 : 3;
```

This assigns `2` to `x2` if `x == 1`, otherwise `3`.

```cpp
// equivalent to
int x2;
if (x == 1) {
  x2 = 2;
}
else {
  x2 = 3;
}
```

The `if` form is longer but clearer when the logic becomes more complex.

#### switch Statement

A `switch` selects among a set of alternatives identified by `case` labels.

```cpp
switch (variable)
{
    case val1:
// code
    case val2:
// code
}
```

The switched value must have an integer type, an enum type, or a user-defined type implicitly convertible to integer or enum. A `switch` can generate more efficient compiled code than a long chain of `if` statements in some cases.

#### switch Termination

Each `case` should normally be terminated with `break` or `return`. `break` exits the `switch`; `return` exits the enclosing function. If no termination statement is present, execution **falls through** to the next case. Intentional fallthrough should be explicitly commented.

```cpp
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

The source is missing semicolons after `print(value)` and `something(value)`. The example shows intentional fallthrough from `do_and_print` to `print`.

#### default Case

A `switch` may include a `default` case.

```cpp
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

`default` can handle the common case or values not covered by explicit cases, for example by raising an exception. The source warns not to use `default` with enumerators when exhaustive checking is desired: without `default`, the compiler can warn if not all enumerator values are handled.

### Iteration Statements

#### Range-for Statements

A **range-for** loop iterates over each element of a range. It works with sequences that provide a begin and end iterator, such as C++ arrays and `std::vector<T>`.

```cpp
std::vector<int> v {1,2,3,4};
for (int value : v)
{
    std::cout << value << std::endl;
}
```

This loop copies each element into `value`. A loop over values cannot modify the original elements. To modify them, the loop variable must be a reference, for example `for (int& value : v)`.

#### for Statements

A traditional `for` loop is more general than a range-for loop.

```cpp
for (int i = 0; i < 10; i++)
{
    std::cout << i << std::endl;
}
```

The variable `i` is declared and initialized in the loop header, and its scope ends at the loop body. If it must remain available after the loop, declare it before the loop.

`auto` can be convenient with iterators:

```cpp
std::vector<T> c;
for (auto p = c.begin(); p != c.end(); ++p)
{
  // do something
}
```

The source used a non-ASCII not-equal sign; valid C++ uses `!=`.

The `for` statement is flexible:

```cpp
int i = 0;
for (; i < 10;)
{
  i++;
}
```

This is valid, but a `while` statement is usually clearer when the loop no longer follows the typical initialization-condition-increment pattern.

#### Pre-Increment and Post-Increment

**Pre-increment** increments first and then evaluates the new value. **Post-increment** evaluates the old value and increments afterward.

In C++, pre-increment is preferred when the two forms are equivalent, as in many loops. For fundamental types there is usually no performance difference. For user-defined types, such as standard-library iterators, post-increment may require an extra temporary object.

#### while Statements

A `while` statement checks its control condition first. If the condition is true, it executes the body.

```cpp
int i = 0;
while (i < 10)
{
    // do something
    ++i;
}
```

`while` is often clearer than `for` when the loop condition is complex or does not depend on a single loop variable.

#### do Statements

A `do` statement executes the body first, then checks the condition.

```cpp
int i = 0;
do
{
    ++i;
} while (i < 10);
```

The body is executed at least once. If the condition depends on state used inside the body, that state must be valid before the first execution.

### Jump Statements

#### Loop Exit

If a loop condition is omitted or always true, the loop does not terminate by itself. C++ provides statements that can exit or alter loop execution:

- `break` exits the nearest enclosing `switch` or iteration statement.
- `continue` skips the rest of the current iteration and proceeds to the next iteration.
- `return` exits not only the loop but also the function that contains it.

If a loop exit depends on a condition, it is often clearer to put that condition directly in the `for` or `while` control expression instead of hiding it inside the loop body.

## 5 Mins Questions

No 5 mins questions are present in the source material.

## Final Summary

Statements define the execution flow of a C++ program. Declarations are statements, so variables should be declared near first use and initialized immediately when possible. Selection statements choose among alternatives: `if` handles conditional execution, the ternary operator handles simple expression selection, and `switch` handles case-based selection.

Iteration statements repeat work: range-for is best for traversing ranges, traditional `for` is useful for index or iterator control, `while` fits condition-driven loops, and `do` guarantees one execution. Jump statements such as `break`, `continue`, and `return` change control flow, but they should be used clearly because they can make loop behavior harder to follow.
