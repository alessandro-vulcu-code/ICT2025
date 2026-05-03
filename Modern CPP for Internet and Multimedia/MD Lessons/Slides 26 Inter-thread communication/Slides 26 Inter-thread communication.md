<!-- Pagina 1 -->

Inter-thread communication with shared memory

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

# Outline

1. Memory Model
2. Race Condition
3. Mutex
4. Condition Variable
5. Atomic
6. Produce Consumer Example

MORE INFO: “Real-Time Embedded System”, I. Bertinotti, G. Manduchi, CRC press, 1st ed., 2012

---

**Immagini estratte:**

![Figura estratta 1](images/p02_img01.jpg)


---

<!-- Pagina 3 -->

Memory Model

• Operations on an object in memory are never directly performed on the object in memory.
• The object is **loaded** into a processor register, **modified** there, and then **written back**.
• What happens if 2 threads try to modify the same object simultaneously?

```cpp
int a = 0;
void incr() {
    a = a + 1;
}
main() {
    incr();
}
```

Time evolution of the CPU Registers
T1: R1 = 0 # load a
T2: R1 = 0+1 modify
T3: a = R1 write back

Time evolution of the value of a
T1: a = 0
T2: a = 0
T3: a = 1

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)


---

<!-- Pagina 4 -->

Race condition

```cpp
int a = 0;
void incr() {
  for (int i = 0; i < 100000; i++){
    a = a + 1;
    std::this_thread::sleep_for(
      std::chrono::microseconds(1));
  }
}

int main() {
  std::thread thr1(incr);
  std::thread thr2(incr);
  thr2.join();
  thr1.join();
  std::cout << a;
}
```

• Two threads modify the same variable in the same moment, so sometimes it happens that one thread reads the “old” value of `a`
• This is a race condition

| Time | a | thr1 | thr2 |
| :--- | :--- | :--- | :--- |
| T1 | a=10 | R1=a=10 | // |
| T2 | a=10 | R1=10+1 | R2=a=10 |
| T3 | a=11 | a=R1=11 | R2=10+1 |
| T4 | a=11 | // | a=R2=11 |

• If you run this code several times, the value of a might change
• Def: a race condition is anything where the outcome of a program depends on the relative ordering of execution of operations on two or more threads.

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img01.jpg)


---

<!-- Pagina 5 -->

producer – consumer problem

```cpp
int main(){
    std::queue<int> q;
    std::thread trb([&](){
        while(true){
            if(q.size()>0) {
                int val = q.front();
                q.pop();
                //use val somehow...
            }}});

        //some operations
        q.push(17);
        q.push(27);
        ..}
```

• Thread a (e.g.: the main thread) produces resources for Thread b
• Thread b consumes the resources produced by Thread a, as soon as they become available
• Solution 1: busy waiting (or spinning)

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)


---

<!-- Pagina 6 -->

Critical Regions (or Critical Sections)

• The critical region is a sequence of statements where the shared resources (memory, cout,...) is accessed, and that must appear to be executed indivisibly to avoid race conditions

```cpp
//race-condition example
void incr() {
  for (int i = 0; i < 100000; i++){
    a = a + 1;
  }
}
int main() {
  std::thread thr1(incr);
  std::thread thr2(incr);
  thr2.join();
  thr1.join();
}
```

```cpp
//producer-consumer example
std::thread trb([](){
  while(true){
    if(q.size()>0) {
      int val = q.front();
      q.pop();
    }
  });
  //some operations
  q.push(17);
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)


---

<!-- Pagina 7 -->

Busy waiting (or spinning)

• The synchronization required to protect a critical region is known as mutual exclusion.

• Solution 1: busy waiting (or spinning): repeatedly checks to see if a condition is true
  • With this code the CPU load goes 100%: it’s not the way to go!
  • Sleeping between cycles would reduce the CPU load, but how much should it sleep?
    • Trade off between speed and load
    • Used only for hardware iterations

• With multiple consumers we may have a race condition!
  • This happens if the second consumer checks the q size just before the first consumer performs the pop

• There must be a better way!

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)


---

<!-- Pagina 8 -->

Mutual exclusion – mutex

• A `mutex` (i.e., a mutual exclusion variable) is an object used to represent the exclusive right to access some resource.

• Only one thread can own a mutex at a time

• To access a resource in `thread-safe way`: acquire the mutex, access the resource, release the mutex.

• To `acquire` a mutex means to gain its exclusive ownership
  • Acquire a mutex may block the thread executing it

• Once the mutex is acquired, you can `access` a critical region without risk of data race

• To `release` a mutex means relinquishing exclusive ownership
  • a release operation will unblock waiting threads.

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)


---

<!-- Pagina 9 -->

Mutex in C++11

• In C++, to acquire a mutex you have to lock it
• And always remember to unlock (i.e., release) it!

```c
std::mutex m_a;
void useMutex() {
    m_a.lock();
    //do stuff
    m_a.unlock();
}
```

• If you forget to unlock the mutex, no one else can acquire (lock) it, causing starvation
• If the functions is interrupted (e.g., with a return) before the unlock, we have a problem!
• C++11 provides two RAII classes, lock_guard and unique_lock, to handle such problem:

• Both lock_guard and unique_lock, unlock the mutex when they go out of scope (RAII: i.e., their constructor locks the mutex, and their destructor unlocks it).

• lock_guard is lighter, but we mostly use unique_lock because it provides more functionalities
• We will see them next..

---

**Immagini estratte:**

![Figura estratta 1](images/p09_img01.jpg)


---

<!-- Pagina 10 -->

# Mutex in C++11 – example

```cpp
#include <mutex> // std::mutex, std::unique_lock
int a = 0; std::mutex m_a;

void doIncr() {
    std::unique_lock<std::mutex> lk_a(m_a);
    a = a + 1;
} // here lk_a goes out of scope, and unlocks the mutex

void incr() {
    for (int i = 0; i < 100000; i++){
        doIncr();
        std::this_thread::sleep_for(
            std::chrono::microseconds(1));
    }
}

int main() {
    std::thread thr1(incr);
    std::thread thr2(incr);
    thr2.join();
    thr1.join();
    std::cout << a << std::endl;
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p10_img01.jpg)


---

<!-- Pagina 11 -->

Mutual exclusion – starvation

• Def: If several threads are blocked on a mutex, the system scheduler could in principle select the thread to be unblocked in such a way that some other unfortunate threads would never get to run. This is called starvation. Why? Because the CPU scheduler does not guarantee fairness.

• Sol: Acquire the mutex for the minimal amount of time (only for accessing critical regions), in order to avoid other threads waiting for the mutex release for no reasons

```c
#include <mutex>
std::mutex m_a;
void useMutex1() {
  while(true) {
    std::unique_lock<
      std::mutex> lk1(m_a);
    //do stuff
  }
}
```

int main() {
  std::thread thr1(useMutex1());
  while(true) {
    std::unique_lock<std::mutex>
      lk2(m_a);
    ...//do other stuff
  }
  ... //do other stuff2
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)


---

<!-- Pagina 12 -->

Mutual exclusion – mutex – deadlock

• Always remember to release the mutex to avoid deadlock (that is a type of starvation)

• Def: deadlock = when one thread waits for a mutex that is never released (from another thread or from itself).

```cpp
#include <mutex>
std::mutex m_a;

void useMutex1() {
  std::unique_lock<std::mutex> lk(m_a);
  //do stuff
}

void useMutex2() {
  std::unique_lock<std::mutex> lk(m_a);
  //do stuff
  useMutex1();//it tries to lock again the same mutex
  → deadlock
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)


---

<!-- Pagina 13 -->

Condition variable (cv) – 1

Def: A condition variable (cv) is a variable used by a thread to wait for an event generated by another thread or a timer.

The (most important) object methods (1) are:

- cv.wait(lck,pred);
  • It unlocks the mutex acquired by the unique_lock lck until the predicate pred becomes true. Then it locks the mutex again.
  • pred must be a boolean function (or a boolean lambda function)

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)


---

<!-- Pagina 14 -->

Condition variable (cv) – 2

The (most important) object methods (2) are:

- cv.wait_for(lck,max_time,pred);
  • It unlocks the mutex acquired by the unique_lock lck until either the predicate pred becomes true or the time max_time elapsed. Then it locks the mutex again.
  • pred must be a boolean function (or a lambda)
  • max_time is of type std::chrono::duration<R,P>, e.g., std::chrono::milliseconds

- cv.notify_one();
  • It unblocks one thread waiting in cv

- cv.notify_all();
  • It unblocks all threads waiting in cv

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)


---

<!-- Pagina 15 -->

Consumer – close to the solution

Steps in thread 1 (consumer)

1. Lock the mutex
2. Wait :
   a) by releasing the mutex
   b) until the predicate (it is a lambda) is true
3. Lock the mutex automatically after stop waiting
4. Consume the generated resource
5. Automatically release the mutex

```cpp
// all #includes..
int main(){
    std::queue<int> q; std::mutex m_a; std::condition_variable cv;

    std::thread tr1([&](){
        while(true){
            std::unique_lock< std::mutex> lk1(m_a);//1.
            cv.wait(lk1 /*2.a)*/, [&]()->bool{
                return !q.empty(); //2.b)
            }); //3.
            q.pop(); //4.
        }//5.
    });

    // producer code
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)


---

<!-- Pagina 16 -->

Producer – close to the solution

Steps in main thread (producer)
1. Lock the mutex
2. Produce the resource (thus the pred of the cond. variable becomes true)
3. Unlock the mutex
4. Notify a thread waiting with the cond. variable that the resource is ready

```c
#include <condition_variable>
#include <mutex> //...all other includes (queue)
int main(){
    std::queue<int> q; std::mutex m_a;
    std::condition_variable cv;
    ... // consumer code

    std::unique_lock< std::mutex> lk2(m_a); //1.
    q.push(17); //2.
    lk2.unlock(); //3.
    cv.notify_one(); //4.
    tr1.join();}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)


---

<!-- Pagina 17 -->

Producer – consumer – exit flag

The previous solution is thread safe, but there are 2 issues:

1. The consumer thread has a while-true statement, i.e. it never ends
   - Solution: while(true) → while(exit_flag) with exit_flag a shared boolean flag
   - The main sets exit_flag to false before joining. Thread-safe? NO!

2. The condition variable predicate is locked until data is inserted in queue (that may never arrive): how to exit from this wait?
   - Sol1: wait_for(lk,max_time,pred) allows exiting after a time max_time
   - Sol2: insert exit_flag (i.e., the same boolean flag of the while) into the pred, and let the main notifying it to the condition variable after setting it. Is it thread safe? NO!

---

**Immagini estratte:**

![Figura estratta 1](images/p17_img01.jpg)


---

<!-- Pagina 18 -->

Atomic variables

Fortunatelly, C++11 provides a way to set `exit_flag` in thread-safe way without the need of an additional mutex, by using an Atomic variable: `std::atomic<bool> exit_flag;`

• An operation in an object of an atomic type is atomic, i.e.:
  • it is performed by a single thread without interference from other threads

• An atomic object can be used only for simple operations on basic data types (int, bool)
  • atomic operations are very fast: they are made by the hardware, that makes only very simple operations → significantly faster than lock-based operations (about 1/3 of the complexity)

---

**Immagini estratte:**

![Figura estratta 1](images/p18_img01.jpg)


---

<!-- Pagina 19 -->

Atomic variables – 2

• The most important methods (all thread-safe, but not the initialization):

  • `std::atomic<int> sn(0); → initialization of an atomic integer variable`
  • `int x = sn.load(); → get the valuer of sn atomically. Same of x = sn;`
  • `sn.store(5); → set the valuer of sn atomically. Same of sn=5;`
  • `int old_sn = sn.exchange(3); → set the valuer of sn atomically and obain the old value of sn.`

• Use atomic only for shared flags or counters

---

**Immagini estratte:**

![Figura estratta 1](images/p19_img01.jpg)


---

<!-- Pagina 20 -->

Consumer – final solution

```cpp
//...all include statements, i.e: queue, mutex, atomic, condition_variable
int main(){
    std::queue<int> q; std::mutex m_a;
    std::condition_variable cv;
    std::atomic<bool> exit_flag(false);
    std::thread tr1([&](){
        while(!exit_flag.load()){ //1.
            std::unique_lock<
                std::mutex> lk1(m_a);//2.
            cv.wait(lk1 , [&]()->bool{ //3.a)
                return !q.empty() //3.b)
                ||exit_flag.load(); //3.c
            }); //4.
            if(!q.empty()) {
                q.pop(); //5.
            }
        } //6.
    });
    ...//code for the producer
}
```

Steps in thread 1 (consumer)

1. Keep cycling until exit flag is true
2. Lock the mutex
3. Wait:
   a) by releasing the mutex
   b) until there is data in the queue, or
   c) until exit flag is true
4. Lock the mutex automatically after waiting
5. Consume the generated resource
6. Automatically unlock the mutex as lk1 goes ot of scope

---

**Immagini estratte:**

![Figura estratta 1](images/p20_img01.jpg)


---

<!-- Pagina 21 -->

Producer–final solution

```cpp
//..all include statements, i.e: queue, mutex, atomic, condition_variable
int main(){
    std::queue<int> q; std::mutex m_a;
    std::condition_variable cv;
    std::atomic<bool> exit_flag(false);
    //..code for the consumer tr1
    std::unique_lock <std::mutex> lk2(m_a); //1.
    q.push(17); //2.
    lk2.unlock(); //3.
    cv.notify_one(); //4.
    exit_flag.store(true); //5.
    cv.notify_all(); //6.
    tr1.join();
}
```

Steps in main thread (producer)
1. Lock the mutex
2. Produce the resource
3. Unlock the mutex
4. Notify a thread waiting with cv that the resource is ready
5. Set the exit flag to true
6. Notify all waiting thread with cv to exit

---

**Immagini estratte:**

![Figura estratta 1](images/p21_img01.jpg)
