Dynamic cast: pointer vs reference

dynamic_cast works with pointers and references

• the pointer that is returned can be a nullptr:
  • dynamic_cast<T*>(p) is a question – “is the object pointed to by p of type T?”
  • the programmer has to check if what is returned is a nullptr

```cpp
void f(Base* p)
{
    Der* p_dev {dynamic_cast<Der*>(p);
    if (p_dev ≠ nullptr)
    {
        // some code using p_dev
    }
    else { // cannot use p_dev! }
}
```

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)
