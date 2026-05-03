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
