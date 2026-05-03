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
