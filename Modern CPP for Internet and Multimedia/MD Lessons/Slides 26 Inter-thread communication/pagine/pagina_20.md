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
