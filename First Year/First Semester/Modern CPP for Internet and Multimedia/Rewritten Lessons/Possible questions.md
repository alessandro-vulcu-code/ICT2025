# Possible oral exam questions

Questions marked **[Prof]** come from `5_min_questions.md` or the Q&A extra questions.

## Types and Declarations

1. What is the difference between a declaration and a definition?
2. What are fundamental types? Give examples of integer, floating-point, character, Boolean, and `void` types.
3. Why are fundamental type sizes implementation-defined, and how do `<cstdint>` types help portability?
4. What is a scope? Explain local, class, namespace, global, and statement scope.
5. What are hiding and shadowing? Give an example.
6. What is the `auto` type specifier, and when should it be used?
7. What is an lvalue? What is an rvalue?
8. What happens if a name is declared without initialization?
9. What is a C++ object?
10. What is object lifetime?
11. Compare automatic, static, free-store, `thread_local`, and temporary object lifetimes.
12. What is brace initialization, and why does it help avoid narrowing?
13. What is the difference between `const` and `constexpr`?
14. What is a type alias, and why can aliases improve readability?
15. **[Prof]** After the operations below, which is the value of `c`?

```cpp
uint_fast8_t a = 21;
uint_fast8_t b = 11;
uint_fast8_t c = a ^ b;
```

## Pointers, Arrays and References

1. What is a pointer?
2. What operations are possible with pointers?
3. What is a raw pointer, and why does it not necessarily express ownership?
4. What is `void*`, and why does it lose type information?
5. What is `nullptr`, and why is it better than `0` or `NULL`?
6. What is the behavior of `const` with pointers?
7. **[Prof]** What is the difference between `const std::string* s` and `std::string* const s`?
8. What is an array, and how can it be initialized?
9. What does it mean that arrays are contiguous?
10. What happens when an array is passed to a function?
11. What is pointer arithmetic, and when is it valid?
12. What is an lvalue reference?
13. What is an rvalue reference?
14. **[Prof]** What is a reference? Provide an example.
15. How do references differ from pointers?
16. Why are rvalue references important for move semantics?

## Structures and Enumerators

1. What are primitive user-defined types?
2. What is a `struct`?
3. How does a `struct` differ from a `class` by default access?
4. What is aggregate initialization?
5. What is an invariant, and can a `struct` enforce one?
6. What is Plain Old Data (POD)?
7. What is memory padding, and why can member order affect object size?
8. What is a bitfield, and when can it be useful?
9. What is an `enum class`?
10. Why is `enum class` safer than plain `enum`?
11. What does it mean that `enum class` is scoped and strongly typed?
12. How can explicit enum values be useful?

## Statements

1. What is a statement in C++?
2. Why is a declaration also a statement?
3. Why should variables be declared near first use and initialized immediately?
4. How does an `if` statement work?
5. How does the ternary conditional operator work, and when is it appropriate?
6. **[Prof]** Explain how the `switch`-`case` statement works, providing an example.
7. What is the role of `break` in a `switch` statement?
8. How does a range-for loop work?
9. Compare `for`, `while`, and `do while` loops.
10. What are `break`, `continue`, and `return`, and how do they affect control flow?
11. What is short-circuit evaluation for `&&` and `||`?
12. What makes a loop condition dangerous or unclear?

## Namespaces and Code Modularization

1. What problem do namespaces solve?
2. How do namespaces support modularity?
3. What is name qualification with `::`?
4. What is the difference between a `using` declaration and a `using namespace` directive?
5. Why can `using namespace std;` be dangerous in headers?
6. What is an interface in modular code?
7. Why should implementation details be hidden?
8. How do namespaces, classes, and functions work together to organize code?
9. What is argument-dependent lookup?
10. How can code be split across headers and source files?

## Functions

1. What is a function declaration?
2. What is a function definition?
3. What are function name, argument list, and return type?
4. What does `void` mean as function return type?
5. What is the difference between passing by value, by pointer, and by reference?
6. **[Prof]** We want to pass a string `s`, an integer `i`, and a double `d` as input parameters to a function. They cannot be modified by the function, and the function should be efficient. How do we pass them?

```cpp
void fun(... s, ... i, ... d);
```

7. When should small values be passed by value?
8. When should large read-only objects be passed by `const` reference?
9. When should a function use pointer parameters?
10. What is function overloading?
11. Why can functions not be overloaded only by return type?
12. What is overload resolution?
13. What are preconditions and postconditions?
14. What is a function pointer?
15. What are macros, and why are they less type-safe than functions or constants?
16. What do `inline`, `constexpr`, and `noexcept` mean for functions?

## Classes

1. What is a class?
2. What are representation, behavior, invariant, and interface?
3. What is the difference between public and private members?
4. Why does access control protect invariants?
5. What is a member function?
6. How can member functions be defined inside or outside class declaration?
7. What is a constructor?
8. What does `explicit` prevent?
9. What is a const member function?
10. What is logical constness?
11. What is `mutable`, and when can it be justified?
12. What is `this`?
13. What are static data members and static member functions?
14. What is a concrete class?
15. How should a class expose a clear interface without exposing representation?

## Compiler, Preprocessor and Linker

1. **[Prof]** Explain the role of the preprocessor, compiler, and linker.
2. What is a translation unit?
3. What does the preprocessor do with `#include`?
4. What are include guards, and why are they necessary?
5. What is conditional compilation?
6. What is the difference between compiler errors and linker errors?
7. What does compiler optimization do?
8. What are object files?
9. What symbols does the linker resolve?
10. What is the difference between static and dynamic libraries?
11. Why are headers not compiled independently?
12. Why do template definitions often need to be visible in headers?

## Construction, Cleanup, Copy and Move

1. What is object life cycle in C++?
2. What does a constructor establish?
3. What does a destructor do?
4. What is RAII, and why is it important?
5. What is the construction and destruction order for class members?
6. Compare default initialization, value initialization, direct initialization, copy initialization, and list initialization.
7. Why is brace initialization often preferred?
8. When can initializer-list constructors affect overload selection?
9. What is aggregate initialization?
10. What is copy construction?
11. What is copy assignment?
12. What should copying preserve: equivalence, independence, or both?
13. Why is default shallow copy dangerous for owning pointers?
14. What is move construction?
15. What is move assignment?
16. What state must a moved-from object be left in?
17. Which default operations can the compiler generate?
18. What does `= delete` mean?
19. What is the Rule of Three/Five idea?
20. Why do resource-owning classes need careful copy and move semantics?

## Memory Management

1. What are the main memory regions in a C++ program?
2. What is stack memory?
3. What is free-store or heap memory?
4. What are static and global storage areas?
5. How do `new` and `delete` work?
6. What is the difference between `new`, `delete`, `new[]`, and `delete[]`?
7. What is a memory leak?
8. What is a dangling pointer?
9. What is double deletion?
10. Why is manual memory management error-prone?
11. What is resource management?
12. How does RAII make cleanup automatic?
13. What is a handle class?
14. Why do handle classes need correct copy and move behavior?
15. Why are smart pointers preferred over raw owning pointers?

## Derived Classes and Class Hierarchies

1. What is inheritance?
2. What is an is-a relationship?
3. What is the difference between implementation inheritance and interface inheritance?
4. What does public inheritance mean for substitutability?
5. What is object slicing?
6. How are base and derived constructors/destructors called?
7. What is a virtual function?
8. What is runtime polymorphism through pointers and references?
9. What does `override` do?
10. What does `final` do?
11. What is a pure virtual function?
12. What is an abstract class?
13. What is the difference between `public`, `protected`, and `private` inheritance or access?
14. What problem can multiple inheritance create?
15. What is a virtual base class?

## Operator Overloading

1. What is operator overloading?
2. Why should overloaded operators preserve intuitive meaning?
3. Which operators cannot be overloaded?
4. What is the difference between member and non-member operator overloads?
5. When must an operator be a non-member?
6. How are binary operators represented as member and non-member functions?
7. How are unary operators represented as member and non-member functions?
8. Why should built-in types usually be passed by value and user-defined types by `const` reference?
9. How is `operator<<` usually implemented?
10. Why should `operator<<` return `std::ostream&`?
11. When is `friend` useful for operator overloading?
12. What is `operator[]`, and what should it return?
13. What is `operator()`, and how does it create a functor?
14. Why are functors useful with standard algorithms?

## Runtime Polymorphism and Casts

1. What is runtime polymorphism?
2. What is an upcast?
3. What is a downcast?
4. What is a crosscast?
5. What is RTTI?
6. What does `dynamic_cast` do?
7. What happens when `dynamic_cast` fails for a pointer?
8. What happens when `dynamic_cast` fails for a reference?
9. Why should RTTI be used sparingly?
10. Why is a virtual function often better than checking actual derived type?
11. What is `static_cast` used for?
12. What is `const_cast` used for?
13. What is `reinterpret_cast` used for?
14. What are smart pointer casts, such as `dynamic_pointer_cast`?

## Templates

1. What is generic programming?
2. What is a template?
3. What is a class template?
4. What is a function template?
5. What is template instantiation?
6. Why do templates usually have no runtime overhead?
7. Why do template definitions usually live in headers?
8. What can a class template contain?
9. What is a member template?
10. What is a template specialization?
11. What is a type alias for a template type?
12. What is a variadic template?
13. What problem do concepts solve in C++20?
14. Why are template error messages often difficult?
15. How are templates used in the Standard Library?

## Smart Pointers

1. What problem do raw pointers create for ownership and lifetime?
2. What is RAII, and how do smart pointers implement it?
3. What is `std::unique_ptr`?
4. What is exclusive ownership?
5. When should `unique_ptr` be used?
6. **[Prof]** When should I use `unique_ptr`, `shared_ptr`, and `weak_ptr`?
7. **[Prof]** How do I pass a `unique_ptr` to functions?
8. What is `std::move`, and why is it needed with `unique_ptr`?
9. What do `release()` and `reset()` do on a `unique_ptr`?
10. What is `std::shared_ptr`?
11. What is reference counting?
12. What does `use_count()` mean?
13. When is `shared_ptr` appropriate, and when is it overused?
14. What is `std::weak_ptr`?
15. **[Prof]** How do I use a `weak_ptr`?
16. How does `weak_ptr` help avoid ownership cycles?
17. What does `lock()` do on a `weak_ptr`?
18. What are common wrong uses of smart pointers?
19. **[Prof]** What is an lvalue?
20. **[Prof]** What is an rvalue?

## Standard Library

1. What is the C++ Standard Library?
2. What categories of facilities does the Standard Library provide?
3. What is the difference between containers, iterators, and algorithms?
4. Why is `std::vector` usually the default sequence container?
5. Compare `vector`, `deque`, `list`, and `forward_list`.
6. Compare ordered associative containers and unordered associative containers.
7. What are `map`, `set`, `unordered_map`, and `unordered_set`?
8. What are container adaptors such as `stack`, `queue`, and `priority_queue`?
9. What is `std::array`?
10. What is an iterator?
11. What do `begin()` and `end()` represent?
12. Compare input, output, forward, bidirectional, and random-access iterators.
13. What is an algorithm in the Standard Library?
14. Why do algorithms operate on iterator ranges rather than directly on containers?
15. Give examples of non-modifying and modifying algorithms.
16. What is `std::string`, and why is it container-like?
17. What are C++ streams?
18. Compare `cout`, `cerr`, `clog`, and `cin`.
19. Compare `ifstream`, `ofstream`, and `fstream`.
20. What are string streams, and when are they useful?

## Socket Programming

1. What is a socket?
2. Why is a socket represented as a file descriptor in POSIX?
3. What is the difference between an IP address and a port?
4. What is the difference between UDP and TCP?
5. What is `SOCK_DGRAM`?
6. What is `SOCK_STREAM`?
7. What headers are needed for basic POSIX socket programming?
8. What is `sockaddr_in`, and which fields must be filled?
9. Why are `htons()` and `htonl()` needed?
10. What does `inet_pton()` do?
11. What does `socket()` return?
12. What does `bind()` do?
13. What does `listen()` do?
14. What does `accept()` do?
15. What does `connect()` do?
16. Compare `send()`/`recv()` with `sendto()`/`recvfrom()`.
17. What is typical UDP server/client flow?
18. What is typical TCP server/client flow?
19. Why must return values from socket calls be checked?
20. What is `SIGPIPE`, and why can it happen when sending on a closed socket?
21. What does `SO_REUSEADDR` do?
22. Why is `close()` important for sockets?
23. How can threads be useful in a socket chat program?

## Threads and Lambdas

1. What is parallel programming?
2. What is the difference between a process and a thread?
3. Why are threads lighter than processes?
4. What memory do threads share?
5. **[Prof]** What's going on when multiple threads are running in parallel?
6. How does `std::thread` start a task?
7. Why must a `std::thread` be joined or detached before destruction?
8. What is the difference between `join()` and `detach()`?
9. Why is `join()` usually preferred?
10. How are thread arguments passed by default?
11. When should `std::ref` be used?
12. How can ownership be transferred to a thread?
13. How can `unique_ptr` or `shared_ptr` be used with threads?
14. What is a lambda function?
15. What is a lambda capture list?
16. Compare capture by value and capture by reference.
17. Why is lifetime important with lambda captures in threads?
18. What is a callable object?
19. Why can lambdas be useful with standard algorithms?
20. Why does sharing memory between threads create risk?

## Inter-thread Communication

1. What is shared memory communication?
2. Why is `a = a + 1` not atomic?
3. **[Prof]** What is a race condition?
4. **[Prof]** What happens if two or more threads access a critical region without any thread-safe mechanism?
5. What is a critical region?
6. What is a mutex?
7. How do `lock()` and `unlock()` protect shared data?
8. Why is manually calling `lock()` and `unlock()` risky?
9. What is RAII locking?
10. What is `std::lock_guard`?
11. What is `std::unique_lock`, and why is it more flexible?
12. What is busy waiting?
13. Why is busy waiting usually inefficient?
14. What is the producer-consumer problem?
15. What is a condition variable?
16. Why must condition variables be used with a predicate?
17. What is a spurious wakeup?
18. How does `wait()` release and reacquire a mutex?
19. What is an atomic variable?
20. When are atomics appropriate?
21. Why are mutexes still needed for complex shared structures like queues?
22. How does the final producer-consumer solution combine mutexes and condition variables?
