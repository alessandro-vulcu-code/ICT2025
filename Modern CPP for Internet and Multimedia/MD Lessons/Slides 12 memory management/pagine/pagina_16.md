Simple handle class for int*

```cpp
class Handle {
    int* p; // pointer to int
public:
    Handle(int* pp) :p{pp} { }
    int& operator*() { return *p; }
    ~Handle() { delete p; }
};

// example of usage
void f()
{
    Handle obj_handle {new int{10}};
    std::cout << *obj_handle;
} // obj_handle goes out of scope
// and calls delete on p
```

this overrides the dereferencing operator *, so that dereferencing on the handle returns the value of the object pointed to by the member pointer.

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)
