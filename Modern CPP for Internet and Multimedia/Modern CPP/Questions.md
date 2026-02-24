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
- Case A: Since a is passed by reference to the thread, it will be modified accordingly, so `a==1` after the join
- Case B: Since a is passed as an integer parameter to the thread function, it won't be modified after the join
- Case C: a is passed by value. The `mutable` keyword allows the lambda to edit the copy of `a` without editing the original one. Without mutable, `a` is read-only. 
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
    - See 5 min question nr. 2

22. What is memory leak?
    - See 5 min question nr. 8

23. What is a dangling pointer? And double deletion? 
    - Dangling pointer is a pointer that references a memory area no longer in use/already free'd or deleted/we don't have access to. Double deletion happens when we try to delete the memory area referenced by dangling pointers. 

24. What is slicing in terms of derived class?
    - See "other question" nr.4

25. What is a dynamic cast?
    - A Dynamic cast is an operator that allows safely cast pointers/references from a base class to derived classes or viceversa using Run-Time Type Information (RTTI) to check whether a conversion is possible. If cast is not valid it returns `nullptr`. 

26. What is the guaranteed size order for fundamental types in C++?
* C++ does not define fixed sizes in bytes for all types, but it guarantees a specific order. For integers: . For floating-point numbers: .

27. What is a "Class Invariant"?
* It is a property (or a set of rules) that must always hold true for an object of a class, from the moment it is constructed until it is destroyed. The constructor is responsible for initially establishing these invariants.

28. What is the technical difference between a `struct` and a `class`?
* The only real difference is the default member visibility. In a `struct`, members are `public` by default, whereas in a `class`, they are `private` by default. Generally, structs are used for simple data aggregates, while classes are used when it is necessary to enforce invariants and hide implementation details.

29. Why is it sometimes better to use `()` instead of `{}` when calling a constructor?
* Although `{}` provides uniform initialization, if a class has a constructor that accepts a `std::initializer_list`, using `{}` will prioritize that constructor. To ensure you are calling an ordinary constructor and to avoid ambiguity (especially with vectors or containers), using `()` is preferable.

30. Why can the default copy assignment cause problems (shallow copy)?
- The copy operation automatically generated by the compiler performs a member-wise copy. If the class contains pointers, only the memory address (the pointer) is copied, not the pointed-to object (shallow copy). This leads to a shared state where two objects point to the same memory, causing potential errors such as a double free.


31. What is the purpose of `public virtual` inheritance?
* It is used to solve the replication problem (or "diamond problem") in multiple inheritance. By declaring a base class as `virtual`, you guarantee that only a single shared instance of that base exists within the hierarchy, avoiding ambiguity and duplication of data members.


32. What are "functors"?
* Functors are classes that overload the function call operator `operator()`. This allows for the creation of objects that behave like functions ("function objects") but can maintain an internal state through their data members.


33. When should `static_cast`, `dynamic_cast`, `const_cast`, and `reinterpret_cast` be used?
* `static_cast`: Used for conversions between related types (e.g., `float` to `int`) or for converting to/from `void*`; it does not perform runtime checks.
* `dynamic_cast`: Used for safe conversions (downcast/crosscast) on polymorphic types (classes with virtual methods). It returns `nullptr` or throws an exception if the cast is invalid.
* `const_cast`: Used to remove the `const` qualifier from a pointer or reference.
* `reinterpret_cast`: Used for conversions between unrelated types (e.g., from a pointer to an integer), reinterpreting the bit sequence in memory.


34. Where should the implementation of a template class be defined?
* The implementation (definition) of a template class must be placed in the header file (`.h`) along with the declaration. If placed in a `.cpp` file, a linker error will occur because the compiler needs access to the full definition to instantiate the template.


35. What is the difference between `vector`/`deque` and `list`/`forward_list` in terms of memory allocation?
* `vector` and `deque` use contiguous memory allocation (elements are stored next to each other in memory).
* `list` and `forward_list` use non-contiguous allocation, where elements are linked via pointers.


36. How are Ordered Containers categorized?
* `map` and `multimap`: Used when the Key is different from the Value ().
* `set` and `multiset`: Used when the Key is the Value ().


37. What characterizes Unordered Containers?
* They are identified by the prefix `unordered_` before the container name (e.g., `unordered_map`).
* Unlike ordered containers (which typically use trees), they use hash functions to manage elements.


38. How do the `begin()` and `end()` methods work with iterators?
* `begin()` returns an iterator pointing to the first element of the container.
* `end()` returns an iterator pointing to the theoretical element *following* the last element. It acts as a sentinel and does not point to a valid element.


39. How do the algorithms `all_of`, `any_of`, and `none_of` function?
* These algorithms take a range (defined by `begin` and `end`) and a predicate (a function or lambda to evaluate).
* `all_of`: Returns true if the predicate is true for **all** elements in the range.
* `any_of`: Returns true if the predicate is true for **at least one** element.
* `none_of`: Returns true if the predicate is false for **all** elements in the range.


40. How does the `insert` method work in a `std::list`?
* The `insert` operation in a list is efficient () once the position is found, as it only requires updating the pointers of the nodes. It does not require shifting elements, unlike in a `vector`.

41. Why do I get strange results when printing an `uint_fast8_t`?
* This happens because many compilers treat `uint_fast8_t` (and `uint8_t`) as a `char` type. When you print it, the system displays the **ASCII character** associated with that bit sequence rather than the numeric value. If the value doesn't correspond to a printable character (like a letter or number), you may see symbols or nothing at all. To fix this, you should cast it to an `int` before printing.


42. Who is responsible for switching between processes?
* The **Kernel** (specifically the **Scheduler**) handles this through a process called a **context switch**. It saves the state of the current process and loads the state of the next one to be executed.


43. What is the definition of a Thread?
* A thread is a system-level representation of a task. It represents an **independent unit of execution** that runs within a process. Crucially, all threads within the same process **share the same address space** and memory, allowing them to access the same global variables and heap.


44. How do you pass a variable by reference to a `std::thread`?
* Even if a function takes a reference, `std::thread` constructors copy or move the arguments by default. To force the thread to take a reference, you must use **`std::ref(var)`** instead of simply passing `&var`.


45. How do Lambda capture clauses (`[]`) work?
* `[=]`: Captures all local variables by **value** (as `const` copies).
* `[&]`: Captures all local variables by **reference**.
* `[&var]`: Captures only the specific variable `var` by reference.
* `[this]`: Captures the **current object** (the pointer to the class instance) by value, allowing access to its members inside the lambda.

46. What is the effect of the `mutable` keyword in a lambda?
* In a capture-by-value lambda (e.g., `[a]() mutable {}`), it removes the **constness** of the copied variables. This allows you to modify the value of `a` inside the lambda's body, but the change remains **local** to the lambda and does not affect the original variable outside.

20. What are atomic vairiables? How can I use them for exit flags?
	- **Atomic variables** (e.g., `std::atomic<bool>`, `std::atomic<int>`) are synchronization primitives provided by C++11 that allow for thread-safe operations on simple data types without using mutexes.
		- **Thread Safety:** Operations on atomic variables are indivisible; they are performed by a single thread without interference from others.
		- **Performance:** They are significantly faster than lock-based operations (approximately 1/3 of the complexity) because they rely on specific hardware instructions rather than software locks.
		- **Key Methods:**
		    - `load()`: Atomically reads the value.
		    - `store(val)`: Atomically sets the value.
		    - `exchange(val)`: Atomically sets a new value and returns the old one.

	In a multi-threaded "Producer-Consumer" scenario, using a standard `bool` for a loop condition is not thread-safe, while using a mutex for a single flag is inefficient. `std::atomic<bool>` provides an optimal solution.

	Here is the correct pattern to ensure threads exit cleanly, even if they are sleeping on a condition variable:

	**1. Declaration** Declare the flag as an atomic boolean, initializing it to false.

```
std::atomic<bool> exit_flag(false);
```

**2. The Consumer (The Worker Thread)** The thread must check the flag in its loop. Crucially, if the thread uses a condition variable (`cv.wait`), the exit flag must be included in the wait predicate. This ensures the thread wakes up and exits even if the work queue is empty.

```
// 1. Loop checks the loaded value
while(!exit_flag.load()){
    std::unique_lock<std::mutex> lk(m_a);

    // 2. Wait until queue has data OR exit_flag is true
    cv.wait(lk, [&](){ return !q.empty() || exit_flag.load(); });

    // 3. Process data if available
    if(!q.empty()) {
        q.pop();
    }
}
```

**3. The Producer (The Main Thread)** To stop the worker thread, you must set the flag and then immediately wake up the thread so it can re-evaluate its condition.

```
// 1. Set the atomic flag to true
exit_flag.store(true);

// 2. Wake up all waiting threads so they check the flag in the cv.wait predicate
cv.notify_all();

// 3. Join the thread
tr1.join();
```