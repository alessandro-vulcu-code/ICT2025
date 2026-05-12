Defaults and resource handles

• This is a handle to an object created with new (it takes care of deleting it):

```cpp
template<class T>
class Handle {
    T* p;
public:
    Handle(T* pp) :p{pp} { }
    T& operator*() { return *p; }
    ~Handle() { delete p; }
};
```

• If a class has a pointer member

• the default constructor will not initialize the pointer -> deleting it in the destructor is dangerous!

• the default destructor will not delete it

• the default copy & move are wrong if the pointer represents ownership (shared state issue)

---

**Immagini estratte:**

![Figura estratta 1](p41_img01.jpg)
