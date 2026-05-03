Array arguments

• C++ arrays are not passed by value but by pointer
• When an array is specified as argument, it always decays into a pointer
  historic reasons inherited from C – in the 1970s, the memory of machines was limited, and it is more efficient to pass a pointer to the array than copying the whole array into a new location

```cpp
// these three declarations are equivalent and
// declare the same function
void f(int* p);
void f(int[] a);
void f(int b[1000]);
```

• The information on the size is lost – and not implicitly available to the function
• This another good reason to avoid using arrays, and preferer std::vector or other standard library containers

---

**Immagini estratte:**

![Figura estratta 1](images/p16_img01.jpg)
