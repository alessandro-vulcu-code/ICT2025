<!-- Pagina 1 -->

Multi-threading

Programming for Telecommunications
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

1. Why do we need parallel programming?
2. Threads vs processes
3. Threads in C++11
4. Join vs detach
5. Lambda functions

MORE INFO: https://www.youtube.com/watch?v=LL8wkskDlbs

“Real-Time Embedded System”, I. Bertinotti, G. Manduchi, CRC press, 1st ed., 2012

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Why do we need parallel programming?

• Multi threading (as well as multi-process) programming is used for parallel programming
• It is essential if your program needs to perform two or more operation in parallel
  • E.g.: a bidirectional chat

```cpp
//Thread 1: read from standard input and send to socket
while(true) {
    getline (std::cin, data);
    write(sk_fd, data, data.size());
}

//Thread 2: read from socket and print to standard output
while(true) {
    read(sk_fd, rx_data, MAX_SIZE);
    std::cout << rx_data << std::endl;
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

Process – definition

• The most central concept in any operating system is the process: an abstraction of a running program.

• Most operating systems can do several things at the same time, for example run a user program while reading from a disk.

• The kernel will switch the CPU from one program to another, thus giving the users the illusion of their parallel execution.

• Keeping track of multiple, parallel activities is hard to do. Hence, operating system designers have introduced a conceptual model, based on sequential processes, to better describe and deal with parallelism.

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p04_img01.jpg)


---

<!-- Pagina 5 -->

Process model

• All the runnable software on the computer, often including the operating system itself, is organized into a number of sequential processes.

• A process is an executing program, and includes all the state information that represents the execution.

• Informally, each process has “its own” virtual CPU, even if in reality the real CPU switches back and forth from process to process.

---

**Immagini estratte:**

![Figura estratta 1](p05_img01.jpg)


---

<!-- Pagina 6 -->

What is inside a Process?

• The program being executed
• The CPU state: program counter, registers, ...
• The memory address space and its contents: variable values, ...
• The state of other resources: files, I/O devices, ...

Observation:

• The process state exactly represents the information that the operating system must be aware of, and must save/restore while switching from one process to another.

• Context switch.

---

**Immagini estratte:**

![Figura estratta 1](p06_img01.jpg)


---

<!-- Pagina 7 -->

Processes Versus Programs

• A program is a static entity, and represents an algorithm expressed in some suitable programming language.

• A process is an activity: the activity consisting of executing the program.

• A process cannot be fully characterized by its corresponding program, because it also has input, output, and a state.

• Several processes can share the same executable code but nevertheless be distinct from each other, because their states are different.

• There is no correspondence between processes and processors: for example, the same processor may be shared among multiple processes through multiprogramming.

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)


---

<!-- Pagina 8 -->

Processes Diagram State (PSD)

I need to block for acquire a resource
Voluntary transition

RUNNING
Depending on CPU load, scheduler decides if I can run or not.
Involuntary transition

BLOCKED
Resource is ready (another process generated it)
Involuntary transition

• A Running process is actually using the CPU at that instant.
• A Ready processes is runnable, but cannot run because it lacks the CPU.
• A Blocked processes is unable to run at that instant (e.g., waiting for an input)

---

**Immagini estratte:**

![Figura estratta 1](p08_img01.jpg)


---

<!-- Pagina 9 -->

Threads

• A thread is the system-level representation of a computer’s facilities for executing a task.
• Threads represent in a natural way multiple activities going on at once in the same application.
• What threads add to the process model is to allow multiple executions to take place in the same process environment. The executions are largely independent of one another.

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

Threads advantages (vs process)

• All the threads of the same process implicitly share the same address space, but they are independent for what concerns execution. This ability is essential for certain applications.
  • E.g., this makes a lot easier infra-threads communication than infra-processes communication

• Threads are easier to create, destroy and manage than processes, because their context is more lightweight.

• It is more efficient to switch from thread to thread (within the same process), that from process to process.

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Threads disadvantages (vs process)

• If a thread crashes, the whole program crashes.
• If a process of a multi-process program crashes, instead, only that process needs to be restarted, while the other processes of the program keep working.
• A multi process program can easily become a distributed program, where different processes run in different machines
• A multithreading program, instead, cannot become a distributed program, as all the threads must run in the same machine
• In this course we do not address distributed programming, so we go with threads 😊

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

# Threads in C++

• Standard library provides the class `std::thread`
• A thread constructor takes a task to be executed (e.g., a function) and the arguments required by that task.
  • Number and types of arguments must match the task requirements
• `thread(Function&& f, Args&&... args);` where:
  • `@f` is the task to be executed
  • `@args` is the list of argument required for that task
• Throws `std::system_error` if the thread could not be started started (e.g., it happens if `pthread` not linked by the linker)

```cpp
void incr(int n_times) {
  for (int i = 0; i < n_times; i++)
    a = a + 1;
}
```

```cpp
int main() {
  std::thread thr(incr, 200);
  thr.join();
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

```markdown
configure.ac – pthread

AC_CHECK_LIB(pthread, pthread_create, [LIBS="$LIBS -lpthread"])#

• This function checks if the pthread library is available or not (running the thread function `pthread_create`). If the check passes, it add lpthread to the libraries to load.
• If you work with threads, you must use it, otherwise it will not compile
• libpthread is a library containing the definition of pthread, i.e., the POSIX threads. It includes four groups of procedures:
  1. Thread management - creating, joining threads etc.
  2. Mutexes
  3. Condition variables
  4. Synchronization between threads using locks and barriers
```

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

# Threads in C++ - join and detach

A dispatched thread must be either joined or detached

• Otherwise, the program crashes after the thread object goes out of scope: its destructor throws an exception
• You cannot join a detached thread (or you get `std::system_error`)
• To `join` a thread means to wait for the end of its execution

```cpp
int a = 0;
int main() {
    std::thread thr(incr, 200);
    ... // other stuff
    thr.join(); //main is blocked here until end of incr
}
```

```cpp
void incr(int n_times) {
    for (int i = 0; i < n_times; i++)
        a = a + 1;
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Threads in C++ - join and detach – 2

• To detach a thread means to let it running independently by the main thread.
  • The variable `thr` does not handle that thread anymore.
  • Used to initiate a thread to complete a task and forget about it.
  • A detached thread that live forever (or decide itself when to terminate) is called daemon.
  • Really dangerous, in general do not use it.

```cpp
int main() {
  std::thread thr(incr,200);
  thr.detach();//main terminates and forgets about thr,
} //that terminates after the program is over!!!
```

• You cannot join a detached thread, or the program crashes → you can check it with the `joinable()` method

```cpp
if(thr.joinable()) { thr.join(); }
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p15_img01.jpg)


---

<!-- Pagina 16 -->

# Threads in C++ - info

Each thread has a unique id, of type `std::thread::id`

- `std::this_thread::get_id()` provides the id of the thread from which it is called
  ```cpp
  int main() {
    auto my_id = std::this_thread::get_id();
  }
  ```

- `thr1.get_id()` provides the id of thread tr1
  - It can be called only in joinable threads (not the detached ones)

```cpp
void print(int a){std::cout<<a;}
int main() {
  std::thread thr1(print,200); // console output
  std::cout << thr1.get_id(); 123782734251776
  thr1.detach();
  std::cout << thr1.get_id();
}
```

- `thread::id of a non-executing thread`
  ```cpp
```

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)


---

<!-- Pagina 17 -->

# Threads in C++ - management

What happens if something (e.g., an exception, a `break` or a `return`) interrupts a function before a thread is joined?

• The thread object goes out of scope, its destructor is called and makes the program crash

• SOL1: for exceptions, after dispatching a thread, use a try-catch block and join in the catch (not that elegant)

• SOL2: Use resource acquisition is initialization (RAII)

```cpp
std::thread thr(incr,200);
try{ ... /* other stuff */ }
catch() {
    thr.join();
}
if(thr.joinable) {
    thr.join();
}
```

```cpp
class A { // RAII
    std::thread thr;
    void incr() {...}
public:
    A:thr(&A::incr,this,200) {}
    ~A() {thr.join();}
};
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)


---

<!-- Pagina 18 -->

Threads in C++ – the task f – 1

@f is the task to be executed:

1. It can be a function

```cpp
// f as a function
int a = 0;
void incr(int n_times) {
    for (int i = 0; i < n_times; i++)
        a = a + 1;
}
int main() {
    std::thread thr(incr, 200);
    ...
}
```

---

**Immagini estratte:**

![Figura estratta 1](p18_img01.jpg)


---

<!-- Pagina 19 -->

Threads in C++ – the task f – 2

@f is the task to be executed:

2. It can be member function, requiring an additional pointer to this

```c
struct A { // f as a function of an object
  int a;
  void incr (int n_times) {
    for (int i = 0; i < n_times; i++)
      a = a + 1;
  }
  void dolncr() {
    std::thread tr(&A::incr, this, 200);
    ...
  }
};
```

It is the way to call a thread that executes `this->incr(200);`

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p19_img01.jpg)


---

<!-- Pagina 20 -->

Threads in C++ – the task f – 3 wrong

@f is the task to be executed:

3. It can be member function, requiring an additional pointer.
Passing it by value is not a good idea

```c
struct A { // f as a function of an object
  int a;
  void incr (int n_times) {
    for (int i = 0; i < n_times; i++)
      a = a + 1;
  }; // end of struct A
int main() {
  A item = {0};
  std::thread thr(&A::incr, item, 200);
  ...
}
```

It is the way to call a thread that executes the incr function to a copy of the object item!!

A item1{item};
item1.incr(200);

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p20_img01.jpg)


---

<!-- Pagina 21 -->

Threads in C++ – the task f – 3 sol1

@f is the task to be executed:

3. It can be member function, requiring an additional pointer.
You should pass it by pointer

```c
struct A { // f as a function of an object
  int a;
  void incr (int n_times) {
    for (int i = 0; i < n_times; i++)
      a = a + 1;
  }; // end of struct A
int main() {
  A item = {0};
  std::thread thr(&A::incr, &item, 200);
  ...
}
```

It is the way to call a thread that executes `item->incr(200);`

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p21_img01.jpg)


---

<!-- Pagina 22 -->

Threads in C++ – the task f – 3 sol2

@f is the task to be executed:

3. It can be member function, requiring an additional pointer.
You can pass it by shared pointer

```c
struct A { // f as a function of an object
  int a;
  void incr (int n_times) {
    for (int i = 0; i < n_times; i++)
      a = a + 1;
  }; // end of struct A
int main() {
  shared_ptr<A> item = make_shared<A>(0);
  std::thread thr(&A::incr, item, 200);
  ...
}
```

It is the way to call a thread that executes `item->incr(200);`

---

**Immagini estratte:**

![Figura estratta 1](p22_img01.jpg)


---

<!-- Pagina 23 -->

Threads in C++ – the task f – 3 sol3

@f is the task to be executed:

3. It can be member function, requiring an additional pointer.
You can enforce to pass it by reference

```c
struct A { // f as a function of an object
  int a;
  void incr (int n_times) {
    for (int i = 0; i < n_times; i++)
      a = a + 1;
  }; // end of struct A
int main() {
  A item = {0};
  std::thread thr(&A::incr, std::ref(item), 200);
  ...
}
```

It is the way to call a thread that executes `item.incr(200);`

---

**Immagini estratte:**

![Figura estratta 1](p23_img01.jpg)


---

<!-- Pagina 24 -->

Threads in C++ – the task f – 4

@f is the task to be executed:
4. It can be a lambda function

```cpp
// f - as a lambda function
int main() {
  std::thread thr( [&]() {
    for (int i = 0; i < n_times; i++)
      a = a + 1;
  });
  ...
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p24_img01.jpg)


---

<!-- Pagina 25 -->

Threads in C++ – function parameters

• The parameters of a function executed in a thread are always passed by `value!` DO NOT TRY TO PASS ANYTHING BY REFERENCE, IT JUST DOESN’T WORK
  • if you do so, it passes it by value or crashes, depending on the implementation
  • If you really need to pass something by reference, you can enforce it by using the wrapper `std::ref(v)`. → be aware that it’s dangerous, as both main thread and thr1 share the same memory.
  → You can pass it by (smart) pointer, just be aware you are sharing the memory

```cpp
void incr(int& v) {
  ++v;
}
int main() {
  int v = 1;
  std::thread thr(incr, std::ref(v));
  ...
  thr.join(); // here v = 2
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)


---

<!-- Pagina 26 -->

Threads in C++ – move

• How can I pass a parameter v to a thread in an efficient way (no copy) without sharing memory between threads?
• `std::move(v)` is the solution -> it castes v as a rvalue reference, i.e., it passes the reference of v, so v loses its reference

```cpp
void print(const std::string& s) {
    std::cout<<"s="<<s<<std::endl;
}
int main() {
    std::string v = "Hi!";
    std::thread thr(print, std::move(v));
    std::cout<<"v="<<v<<std::endl;
    thr.join();
}
```

//output
s=Hi!
v=

v lost the reference

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)


---

<!-- Pagina 27 -->

Lambda function

• Def: a Lambda function (or lambda expression, or lambda) is a simplified notation for defining and using an anonymous function object.
  • It is used whenever you need to call a simple function that you will use like a local variable, so doesn’t make sense to create a function for it

• A lambda is an object of type `std::function<Return(Args)>`
  • Return is the return type
  • Args is the list of parameters

• Some examples:
  • `const std::function<void(int)>`
  • `const std::function<int(int,double)>`

---

**Immagini estratte:**

![Figura estratta 1](images/p27_img01.jpg)


---

<!-- Pagina 28 -->

Lambda function – syntax

Between [] insert the list of parameters that will be captured by the lambda, i.e., passed from the scope where the lambda is created to the scope of lambda.
• By default parameters are passed by const copy
• Writing just = passes all parameters by const copy
• Writing & before the parameter passes them by reference
• Writing just & passes all parameters by reference
• Writing this captures the current object by reference

Between () insert the list of the function parameters, just as in a normal function

```python
[&a] (int x) -> int
```

After -> insert thr returning type

```python
a = a + x;
return a;
```

Between {} insert the body of the function, just as in a normal function

---

**Immagini estratte:**

![Figura estratta 1](images/p28_img01.jpg)


---

<!-- Pagina 29 -->

Lambda function – syntax examples

a is passed by reference

[&a](int x) -> int
{ ... //body}

The function requires an integer parameter

The function returns an int

a is passed by value and can be modified (keyword mutable)

[a](() mutable
{ ... //body}

The function requires no parameters

The function returns nothing (void)

a is passed by value, b by reference

[a,&b](()
{ ... //body}

all passed by value

[=](()
{ ... //body}

all passed by reference

[&](()
{ ... //body}

---

**Immagini estratte:**

![Figura estratta 1](images/p29_img01.jpg)


---

<!-- Pagina 30 -->

Use of lambas

```cpp
std::vector<int> values = {1,2,3};
void executeF(const std::function<void(int)>& f) {
    for(int v : values) {
        f(v);
    }
}

int main() {
    auto lambda = [](int k) {
        std::cout << k << std::endl;
    };
    executeF(lambda);
    executeF([](int k) {
        std::cout << "k = " << k << std::endl;
    });
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p30_img01.jpg)


---

<!-- Pagina 31 -->

Use of lambas – for each

```cpp
int main() {
    std::vector<int> values = {1,2,3};

    std::for_each(values.begin(),values.end(),
        [](int* k) {
            std::cout << "k = " << *k << std::endl;
        });
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p31_img01.jpg)


---

<!-- Pagina 32 -->

Use of Lambas in Threads

```cpp
int main() {
    int a = 0;
    std::thread thr( [&a]() {
        a = a + 1;
    });
    ... // a = 1
}

int main() {
    int a = 0;
    std::thread thr( [](int v) {
        v = v + 1;
    }, a);
    ... // a = 0
}

int main() {
    int a = 0;
    std::thread thr( [a]() mutable {
        a = a + 1;
    });
    ... // a = 0
}

Question: in all these cases, which is the value of a after joining thr?
```

---

**Immagini estratte:**

![Figura estratta 1](images/p32_img01.jpg)
