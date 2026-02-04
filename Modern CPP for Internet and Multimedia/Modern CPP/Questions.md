# 5 mins questions
1. Explain which is the role of preprocessor, compiler and linker.
2. Explain how the switch-case statement works, providing an example.
3. After the operations:
```c++
    uint_fast8_t a = 21;
    uint_fast8_t b = 11;
    uint_fast8_t c = a ^ b;
```
Which is the value of `c`?    
4. What is an lvalue? What is an rvalue?
5. What is a reference? Provide an example.
6. We want to pass a `string s`, an `integer i` and a `double d` as input parameters to a function (they cannot be modified by the function, and it should be efficient). How do we pass them?
    `void fun(... s, ... i, ... d);`
7. Each time you write the word `new`, you then need to write the word `delete`. Who is responsible to perform this operation?
8. An object has been created with `new`; where and when is the object going to be destroyed with `delete`?
9. When should I use `unique_ptr`, `shared_ptr` and `weak_ptr`?
10. How do I pass a `unique_ptr` to functions?
11. How do I use a `weak_ptr`?
12. What’s going on when multiple threads are running in parallel? What is a race condition?
13. What happens if two or more threads access a critical region without any thread safe mechanism?
14. Considering the use of Lambdas in Threads, which is the value of `a` after joining `thr` in each of these cases?
**Case A:**
```cpp
    int main() {
        int a = 0;
        std::thread thr([&a]() {
            a = a + 1;
        });
        thr.join();
    }
```
**Case B:**
```cpp
    int main() {
        int a = 0;
        std::thread thr([](int v) {
            v = v + 1;
        }, a);
        thr.join();
    }
```
**Case C:**
```cpp
    int main() {
        int a = 0;
        std::thread thr([a]() mutable {
            a = a + 1;
        });
        thr.join();
    }
```

# Other questions
1. If no copy or move constructors are declared, what does the compiler do, and how can you explicitly prevent their creation?
    
2. What happens to the default move constructor if you manually declare only a copy constructor for a class?
    
3. Explain the difference between **Shallow Copy** and **Deep Copy**. Why is a shallow copy problematic when a class contains a pointer member (raw, shared, or weak)?
    
4. What is **Object Slicing**, and under what circumstances does it occur during object assignment or passing?
    
5. When a derived class `B` is instantiated, in what order are the constructors called, and how can the base class `A` be initialized?
    
6. Why is it critical to declare the destructor of a base class as `virtual`?
    
7. Explain how the `this` pointer can be used to avoid **shadowing** and how it enables **concatenated operations** (method chaining).
    
8. Provide an example of how to overload the `<<` operator to allow polymorphic printing for a base class `EthConn` and its derived class `TcpServer`.
    
9. Describe the **RAII (Resource Acquisition Is Initialization)** pattern in the context of socket management. How does the class destructor ensure resource safety?
    
10. When handling multiple clients with threads, what is the functional difference between using `std::thread::detach()` and `std::thread::join()`?
    
11. What is the effect of `std::move()` on an lvalue, and what happens to the original object's resource ownership after the move?
    
12. Consider the following code snippet:
```cpp
    void func(int&& r);
    int b = 10;
```
Why does `func(b)` result in a compiler error, while `func(std::move(b))` is acceptable?    

13. According to the "code reviewer" mindset, what are the key points to check to ensure a class is "exam-ready" regarding const correctness and thread safety?

14. Define what a race condition is and explain when it occurs.
    
15. What is a mutex and what is its primary purpose in multithreading?
    
16. Define a critical region (or critical section).
    
17. How should you pass a `std::string` and an `int` as function arguments if they are not to be modified and you want the code to be efficient? Provide the function signature.
    
18. Explain the purpose of `std::weak_ptr`. In which scenarios is it necessary to use it instead of a `std::shared_ptr`?
    
19. Describe the process state diagram and the possible transitions between states (e.g., Ready, Running, Waiting).
    
20. What are condition variables and how are they used to synchronize threads?
    
21. Write a short C++ code snippet that implements a `switch-case` statement.