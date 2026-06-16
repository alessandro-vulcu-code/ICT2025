---
geometry: margin=1.5cm
---
# 5 mins questions
1. Explain which is the role of preprocessor, compiler and linker.
	- **Preprocessor:** handles directives like `#include`, `#define` and produces a pure C++ file called *traslation unit*.
	- **Compiler:** converts traslation units into *object files*
	- **Linker:** combines object files and libraries to create the *final executable*

```plaintext
Source file → [Preprocessor] → Translation Unit → [Compiler] → Object File → [Linker] → Executable
```
---

2. Explain how the switch-case statement works, providing an example.
```cpp
switch(variable){
    case 1:
        // case variable == 1
        break;
    case 2:
    case 3:
        // body to run for case variable == 2 or 3
        break;
    default:
        // all the other cases
}
```

---

3. After the operations:
```c++
uint_fast8_t a = 21;
uint_fast8_t b = 11;
uint_fast8_t c = a ^ b;
```
Which is the value of `c`?    
- **Answer:** 30
- **Explanation:** The operator `^` is the bitwise XOR.
    - a=21→(00010101)2​
    - b=11→(00001011)2​
    - c=a⊕b→(00011110)2​ which is 16+8+4+2=30.

---

4. What is an lvalue? What is an rvalue?
	- **lvalue:** An expression that refers to a memory location (it has a persistent address). You can take its address using `&`. Example: a variable name `a`. An lvalue can stay on both size of the `=` operator.
	- **rvalue:** A temporary value that ==does not have a persistent memory address==, typically found on the right side of an assignment. Example: a literal like `1`

---

5. What is a reference? Provide an example.
	- A reference is an alias of an existing  variable. It must be initialized and it can't be changed to refer to another variable
```cpp
	int b = 5;
	int& bb = b;
	bb = 5; // bb and b has the same value 
```
6. We want to pass a `string s`, an `integer i` and a `double d` as input parameters to a function (they cannot be modified by the function, and it should be efficient). How do we pass them?
	`void fun(... s, ... i, ... d);`
    - `void fun(const string& s, int i, double d);` we can pass the string as const reference, the integers by value. For built-in types passing parameters by values is the best way.
---

7. Each time you write the word `new`, you then need to write the word `delete`. Who is responsible to perform this operation?
	- Packet destructor must delete each inserted element, as it owns them now. So, it is the owner of the resource.

8. An object has been created with `new`; where and when is the object going to be destroyed with `delete`?
	- On the **heap**,  This is dynamic memory.
	- Deleted manually by the user or in the destructor if we are using the RAII paradigm, by calling the delete. If never deleted, it causes **memory leak**.

9. When should I use `unique_ptr`, `shared_ptr` and `weak_ptr`?
	- **unique_ptr:** used for exclusive ownership, so only one pointer owns the resource;
	- **shared_ptr:** for shared ownership, so multiple pointers owns the resource via reference counting. when it reaches 0, the pointer is deleted and the resources released;
	- **weak_ptr:** to observe a *shared_ptr* without taking ownership, preventing circular references

10. How do I pass a `unique_ptr` to functions?
	- Since a `unique_ptr` cannot be copied, you must **move** it using `std::move()` (transferring ownership) or pass it by **reference** (if the function shouldn't take ownership). 
	- `void fun(std::unique_ptr<A> ptr);` → called with `fun(std::move(myPtr));`
11. How do I use a `weak_ptr`?
	- You cannot access the object directly from a `weak_ptr`. You must first call `.lock()` to obtain a `shared_ptr`. If the original object was already destroyed, `lock()` returns `nullptr`.


12. What’s going on when multiple threads are running in parallel? What is a race condition?
    - Multiple threads running in parallel share the resources of the same process: without thread-safe code the execution could result in an unpredictable behavior due to shared resources access timing.
    - A race condition is "anything where the outcome of a program depends on the relative ordering of execution of operations on two or more threads."
13. What happens if two or more threads access a critical region without any thread safe mechanism?
    - The final result of the execution / behavior of the program is unpredictable, because we don't know a-priori the order of execution of the instructions.
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
    - NO copy/move constructors? Default ones are used, as well as copy and move assignments
    - To explicitally prevent the creation use the `= delete`. For Example: `~X() = delete;`

2. What happens to the default move constructor if you manually declare only a copy constructor for a class?
    - "if one among a copy/move/destructor operation is declared, no copy/move/destructor operations are default-generated"

3. Explain the difference between **Shallow Copy** and **Deep Copy**. Why is a shallow copy problematic when a class contains a pointer member (raw, shared, or weak)?
    - During a Shallow Copy, we are copying only the pointer of the "internal resource", such that the initial and new object implicitly point the same resource. Using a Deep Copy solves this by creating also a new instance for that object, such that those instance are pointing different memory areas.

4. What is **Object Slicing**, and under what circumstances does it occur during object assignment or passing?
    - Object Slicing occurs when we are casting derived class objects to the base class by value. In that case we slice off the derived class extra information (lose data).

5. When a derived class `B` is instantiated, in what order are the constructors called, and how can the base class `A` be initialized?
    - The first constructor to be called is `A`, then `B`.
    - Class `A` can be initialized before the `B` constructor body , for example `B(params) : A(paramsA) {...}` 

6. Why is it critical to declare the destructor of a base class as `virtual`?
    - If we know that a class has other derived classes, we must declare the destructor as `virtual` to call the correct derived destructor for each instance, such that we avoid memory leaks for example.

7. Explain how the `this` pointer can be used to avoid **shadowing** and how it enables **concatenated operations** (method chaining).
    - `this` keyword allows to recall instance-related variables with same name as other parameters/variables.
    - In overloaded operator methods we can return `this` as class pointer, such that it can be reused in concatenated calls.

8. Provide an example of how to overload the `<<` operator to allow polymorphic printing for a base class `EthConn` and its derived class `TcpServer`.
    ```cpp
    std::ostream& operator<<(std::ostream& o, const EthConn& conn){
        // print is a virtual method also
        conn.print(o);
        return o;
    }
    ```

9. Describe the **RAII (Resource Acquisition Is Initialization)** pattern in the context of socket management. How does the class destructor ensure resource safety?
    - In the RAII paradigm, we use wrapper classes to handle the ownership of the resources such that we are sure that at wrapper initialization the resource is acquired, and at wrapper object destruction the destructor is called, thus releasing back the resources.

10. When handling multiple clients with threads, what is the functional difference between using `std::thread::detach()` and `std::thread::join()`?
    - `std::thread::detach()` separates the thread from the program allowing it to run independently
    - `std::thread::join()` waits for the thread end before continuing with the next instructions

11. What is the effect of `std::move()` on an lvalue, and what happens to the original object's resource ownership after the move?
    - `std::move(var)` on an lvalue moves the ownership of the `var` from the original variable to the newer one.
    - After the ownership has been moved, the original variable remains in an unspecified state. 

12. Consider the following code snippet:
```cpp
void func(int&& r);
int b = 10;
```
Why does `func(b)` result in a compiler error, while `func(std::move(b))` is acceptable?
    - `b` is a lvalue object, it cannot be assigned to an rvalue object.
    - `std::move` is an rvalue operation, so it can be used.

13. According to the "code reviewer" mindset, what are the key points to check to ensure a class is "exam-ready" regarding const correctness and thread safety?
    - check for const correctness on defined/implemented methods
    - avoid memory leaks = use RAII paradigm
    - check resource access is thread-safe
    - use correctly `unique_ptr`, `shared_ptr` and `weak_ptr`
14. Define what a race condition is and explain when it occurs.
    - See 5 min Questions nr. 9

15. What is a mutex and what is its primary purpose in multithreading?
    - MutEx: Mutual Exclusion, it act as a semaphore/traffic light for the resource access. Threads can `.lock()` the resouce, if the resource is not-locked it can be used by the thread and then released with `.release()`. Otherwise the thread remains in a locked state until some other thread releases the lock. If no thread releases the resource we end up in a **dead-lock**.

16. Define a critical region (or critical section).
    - Critical region: part of the code that represents a race condition, so the shared access to the resources.

17. How should you pass a `std::string` and an `int` as function arguments if they are not to be modified and you want the code to be efficient? Provide the function signature.
    - See 5 min questions nr.6, function signature: `void f(const std::string& s, int i)`, for built-in types it is more convenient to pass them by value.

18. Explain the purpose of `std::weak_ptr`. In which scenarios is it necessary to use it instead of a `std::shared_ptr`?
    - `std::weak_ptr` smart pointer has been introduced to fix the circular reference scenario. A "parent" references the "children" using `std::shared_ptr`, while the "children" must use `std::weak_ptr` and call `.lock()`. It doesn't increment the internal counter of the shared pointer

19. Describe the process state diagram and the possible transitions between states (e.g., Ready, Running, Waiting).
    - A **Ready** process is runnable, but cannot run because it lacks the CPU. It is in the pool of the processor
    - A **Running** process is actually using the CPU at that instant.
    - A **Blocked** process is unable to run at that instant (e.g., waiting for the needed resources)

    ```plaintext
    [Ready] <===(Involuntary Transition, scheduler decides what to run)===> [Running]
    [Blocked] >===(Involuntary Transition, after an external event, like I/O)===> [Ready]
    [Running] >===(Voluntary Transition, like for resource waiting)===> [Blocked]
    ```

20. What are condition variables and how are they used to synchronize threads?
    - "A condition variable (cv) is a variable used by a thread to wait for an event generated by another thread or a timer."
    - Example: 
        - `cv.wait(lck, pred);` and `cv.waitfor(lck, timeout, pred);` locks mutex and until pred true [or timeout reached]
        - `cv.notify()` and `cv.notify_all()` unblocks one or all threads in waiting for cv

21. Write a short C++ code snippet that implements a `switch-case` statement.